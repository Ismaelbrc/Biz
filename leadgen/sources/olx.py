"""Scraper do OLX (imóveis para alugar) usando Playwright.

O OLX muda o HTML com alguma frequência, então os seletores abaixo ficam
centralizados em `SELECTORS` para facilitar recalibração sem mexer na lógica.
Se um anúncio não bater com nenhum seletor, ele é simplesmente pulado (o
scraper nunca deve quebrar por causa de 1 card fora do padrão).

Como recalibrar quando o OLX mudar o layout:
  1. `playwright codegen https://www.olx.com.br/imoveis/aluguel` para inspecionar
     os elementos atuais.
  2. Atualizar os valores de SELECTORS abaixo (são seletores CSS).
"""

from __future__ import annotations

import logging
import os
import re
from urllib.parse import quote

from playwright.sync_api import sync_playwright

logger = logging.getLogger("leadgen.olx")

BASE_URL = "https://www.olx.com.br/imoveis/aluguel/estado-{uf}"

SELECTORS = {
    "card": "[data-testid='ad-card'], section[data-ds-component='DS-AdCard']",
    "card_title": "h2, [data-testid='ad-card-title']",
    "card_price": "[data-testid='ad-price'], .olx-ad-card__price",
    "card_location": "[data-testid='ad-card-location'], .olx-ad-card__location",
    "card_link": "a",
    "detail_description": "[data-testid='ad-description'], #description",
    "detail_seller_store": "[data-testid='store-info'], .olx-store-info, a[href*='/loja/']",
    "detail_seller_name": "[data-testid='seller-name'], .olx-user-card__name",
}

IMOBILIARIA_SIGNALS = re.compile(
    r"creci|imobili[aá]ria|loja oficial|an[uú]ncios da loja", re.IGNORECASE
)


class OLXSource:
    """Fonte real: busca anúncios "para alugar" no OLX via navegador headless."""

    def __init__(self, headless: bool = True, user_agent: str | None = None):
        self.headless = headless
        self.user_agent = user_agent or os.getenv(
            "SCRAPER_USER_AGENT",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        )

    def _search_url(self, cidade: str, uf: str, page: int) -> str:
        base = BASE_URL.format(uf=uf.lower())
        q = quote(cidade)
        suffix = f"?o={page}" if page > 1 else ""
        return f"{base}?q={q}{'&' if suffix else ''}{suffix.lstrip('?')}"

    def search(self, cidade: str, uf: str, max_paginas: int, max_anuncios: int) -> list[dict]:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=self.headless)
            context = browser.new_context(user_agent=self.user_agent, locale="pt-BR")
            try:
                return self._search_with_context(context, cidade, uf, max_paginas, max_anuncios)
            finally:
                browser.close()

    def _search_with_context(self, context, cidade, uf, max_paginas, max_anuncios) -> list[dict]:
        listings: list[dict] = []
        page = context.new_page()
        for page_num in range(1, max_paginas + 1):
            if len(listings) >= max_anuncios:
                break
            url = self._search_url(cidade, uf, page_num)
            logger.info("Buscando: %s", url)
            try:
                page.goto(url, timeout=30_000, wait_until="domcontentloaded")
                page.wait_for_selector(SELECTORS["card"], timeout=15_000)
            except Exception as exc:  # noqa: BLE001
                logger.warning("Falha ao carregar %s: %s", url, exc)
                continue

            cards = page.query_selector_all(SELECTORS["card"])
            for card in cards:
                if len(listings) >= max_anuncios:
                    break
                listing = self._parse_card(card)
                if listing:
                    listings.append(listing)
        page.close()
        return listings

    def _parse_card(self, card) -> dict | None:
        try:
            link_el = card.query_selector(SELECTORS["card_link"])
            url = link_el.get_attribute("href") if link_el else None
            if not url:
                return None
            title_el = card.query_selector(SELECTORS["card_title"])
            price_el = card.query_selector(SELECTORS["card_price"])
            loc_el = card.query_selector(SELECTORS["card_location"])
            return {
                "id": url.rstrip("/").split("/")[-1],
                "titulo": title_el.inner_text().strip() if title_el else "",
                "url": url,
                "preco": price_el.inner_text().strip() if price_el else "",
                "localizacao": loc_el.inner_text().strip() if loc_el else "",
            }
        except Exception as exc:  # noqa: BLE001
            logger.debug("Card ignorado: %s", exc)
            return None

    def enrich_all(self, listings: list[dict]) -> list[dict]:
        """Abre cada anúncio para descobrir se é particular ou imobiliária."""
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=self.headless)
            context = browser.new_context(user_agent=self.user_agent, locale="pt-BR")
            page = context.new_page()
            enriched = [self._enrich_one(page, listing) for listing in listings]
            page.close()
            browser.close()
        return enriched

    def _enrich_one(self, page, listing: dict) -> dict:
        body_text = ""
        is_store = False
        try:
            page.goto(listing["url"], timeout=30_000, wait_until="domcontentloaded")
            body_text = page.inner_text("body")
            is_store = page.query_selector(SELECTORS["detail_seller_store"]) is not None
        except Exception as exc:  # noqa: BLE001
            logger.warning("Falha ao abrir anúncio %s: %s", listing.get("url"), exc)

        tipo = "desconhecido"
        if is_store or IMOBILIARIA_SIGNALS.search(body_text):
            tipo = "imobiliaria"
        elif body_text:
            tipo = "particular"

        listing = dict(listing)
        listing["descricao"] = body_text[:2000]
        listing["tipo_anunciante"] = tipo
        return listing
