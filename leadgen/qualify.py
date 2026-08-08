"""Qualificação dos anúncios extraídos.

Critério do desafio 1: pessoa física, dona do imóvel, anunciando para
ALUGAR por conta própria (sem imobiliária/corretor pelo meio).
"""

from __future__ import annotations

import os
import re

from leadgen.config import IMOBILIARIA_KEYWORDS, PROPRIETARIO_KEYWORDS

VENDA_SIGNALS = re.compile(
    r"\bà venda\b|\bvendo\b|\bvenda\b|financiamento|entrada \+ parcelas", re.IGNORECASE
)
ALUGUEL_SIGNALS = re.compile(r"alug|locac|locaç", re.IGNORECASE)


def _text_of(listing: dict) -> str:
    return f"{listing.get('titulo', '')} {listing.get('descricao', '')}".lower()


def qualify_listing(listing: dict) -> dict:
    """Retorna o listing com `score` (0-100), `qualificado` (bool) e `motivo`."""
    text = _text_of(listing)
    tipo = listing.get("tipo_anunciante", "desconhecido")

    listing = dict(listing)

    # "sem imobiliária" / "direto com o proprietário" contêm a palavra
    # "imobiliária" mas significam o oposto de um anúncio de imobiliária —
    # por isso os sinais de proprietário têm prioridade sobre os de imobiliária.
    proprietario_hits = [kw for kw in PROPRIETARIO_KEYWORDS if kw in text]
    imobiliaria_hits = [kw for kw in IMOBILIARIA_KEYWORDS if kw in text]

    if (imobiliaria_hits and not proprietario_hits) or tipo == "imobiliaria":
        listing.update(score=0, qualificado=False, motivo="Anunciante é imobiliária/corretor")
        return listing

    if VENDA_SIGNALS.search(text) and not ALUGUEL_SIGNALS.search(text):
        listing.update(score=0, qualificado=False, motivo="Anúncio é de venda, não de aluguel")
        return listing

    if not ALUGUEL_SIGNALS.search(text):
        listing.update(score=0, qualificado=False, motivo="Não menciona aluguel")
        return listing

    score = 60 if tipo == "particular" else 40
    score += sum(10 for kw in PROPRIETARIO_KEYWORDS if kw in text)
    score = min(score, 100)

    motivo = "Pessoa física anunciando aluguel direto, sem imobiliária"
    listing.update(score=score, qualificado=True, motivo=motivo)
    return listing


def qualify_with_llm(listing: dict) -> dict:
    """Reclassifica anúncios com `tipo_anunciante == 'desconhecido'` usando Claude.

    Só é chamado quando ANTHROPIC_API_KEY está configurada; caso contrário o
    resultado da heurística (`qualify_listing`) é mantido como está.
    """
    if not os.getenv("ANTHROPIC_API_KEY"):
        return listing

    import anthropic

    client = anthropic.Anthropic()
    prompt = (
        "Classifique este anúncio de imóvel. Responda apenas com uma palavra: "
        "'particular' se for o próprio dono anunciando, ou 'imobiliaria' se for "
        "corretor/imobiliária.\n\n"
        f"Título: {listing.get('titulo', '')}\n"
        f"Descrição: {listing.get('descricao', '')[:800]}"
    )
    try:
        resp = client.messages.create(
            model="claude-sonnet-5",
            max_tokens=10,
            messages=[{"role": "user", "content": prompt}],
        )
        answer = resp.content[0].text.strip().lower()
        if "imobil" in answer:
            listing = dict(listing)
            listing["tipo_anunciante"] = "imobiliaria"
        elif "particular" in answer:
            listing = dict(listing)
            listing["tipo_anunciante"] = "particular"
    except Exception:  # noqa: BLE001
        pass
    return listing
