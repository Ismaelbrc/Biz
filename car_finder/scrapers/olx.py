"""OLX car scraper – parses __NEXT_DATA__ embedded JSON from Next.js pages."""
import json
import re
import time
from typing import Optional
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup

from config import FILTERS, MAX_PAGES, REQUEST_DELAY
from models import Car

_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
}

_BASE = "https://www.olx.com.br"

_KNOWN_BRANDS = [
    "Volkswagen", "VW", "Chevrolet", "GM", "Fiat", "Ford", "Honda", "Toyota",
    "Hyundai", "Renault", "Nissan", "Peugeot", "Citroën", "Citroen",
    "Mitsubishi", "Kia", "Jeep", "BMW", "Mercedes", "Audi", "Volvo",
    "Land Rover", "Dodge", "Chery", "JAC", "Caoa Chery", "Suzuki",
    "Subaru", "Alfa Romeo", "Seat", "Skoda", "BYD",
]


class OLXScraper:
    def search_all(self, locations: list) -> list[Car]:
        all_cars: list[Car] = []
        seen: set[str] = set()
        for loc in locations:
            for car in self._search_location(loc["olx_path"], loc["name"]):
                if car.id not in seen:
                    seen.add(car.id)
                    all_cars.append(car)
        return all_cars

    def _search_location(self, path: str, city: str) -> list[Car]:
        params = {
            "monetaryvalue": 1,
            "monetaryvalue_max": FILTERS["price_max"],
            "auto_yearfrom": FILTERS["year_min"],
            "auto_yearto": FILTERS["year_max"],
            "auto_mileageto": FILTERS["km_max"],
            "auto_gearbox": "Autom%C3%A1tico",
        }
        base = f"{_BASE}/{path}/autos-e-pecas/carros-vans-e-utilitarios"
        cars: list[Car] = []

        for page in range(1, MAX_PAGES + 1):
            qs = urlencode(params) + (f"&o={page}" if page > 1 else "")
            try:
                r = requests.get(f"{base}?{qs}", headers=_HEADERS, timeout=15)
                if r.status_code != 200:
                    break
                found = _parse_page(r.text, city)
                if not found:
                    break
                cars.extend(found)
                time.sleep(REQUEST_DELAY)
            except Exception as exc:
                print(f"  [OLX] {city} p{page}: {exc}")
                break

        return cars


# ── Parsers ──────────────────────────────────────────────────────────────────

def _parse_page(html: str, city: str) -> list[Car]:
    cars = _parse_next_data(html, city)
    return cars if cars else _parse_html(html, city)


def _parse_next_data(html: str, city: str) -> list[Car]:
    try:
        soup = BeautifulSoup(html, "lxml")
        tag = soup.find("script", id="__NEXT_DATA__")
        if not tag:
            return []
        data = json.loads(tag.string)
        pp = data.get("props", {}).get("pageProps", {})
        ads = pp.get("ads") or pp.get("listing", {}).get("listing", {}).get("ads", [])
        return [c for ad in ads for c in [_parse_ad(ad, city)] if c]
    except Exception:
        return []


def _parse_html(html: str, city: str) -> list[Car]:
    """Minimal HTML fallback."""
    cars = []
    try:
        soup = BeautifulSoup(html, "lxml")
        for a in soup.select("a[href*='/item/']"):
            href = a.get("href", "")
            title_el = a.find(["h2", "h3", "span"])
            title = title_el.get_text(strip=True) if title_el else ""
            if not (href and title):
                continue
            m = re.search(r"R\$\s*([\d\.]+)", a.get_text())
            price = _to_float(m.group(1)) if m else None
            if not price:
                continue
            uid = href.rstrip("/").split("-")[-1]
            brand, model = _split_brand_model(title)
            cars.append(Car(
                id=f"olx_{uid}", source="olx",
                url=href if href.startswith("http") else f"{_BASE}{href}",
                title=title, brand=brand, model=model, version="",
                year=0, price=price, location=city,
            ))
    except Exception:
        pass
    return cars


def _parse_ad(ad: dict, city: str) -> Optional[Car]:
    try:
        lid  = str(ad.get("listId") or ad.get("id") or "")
        subj = str(ad.get("subject") or ad.get("title") or "")
        url  = str(ad.get("url") or ad.get("link") or "")

        price = ad.get("priceValue") or ad.get("price")
        if isinstance(price, str):
            price = _to_float(re.sub(r"[^\d]", "", price))
        price = float(price or 0)
        if price <= 0:
            return None

        props: dict = {}
        for p in ad.get("properties") or []:
            if isinstance(p, dict):
                props[p.get("name", "")] = p.get("value", "")

        year = int(props.get("regdate") or props.get("year") or 0)
        km_raw = props.get("mileage") or props.get("km") or ""
        km = int(re.sub(r"[^\d]", "", str(km_raw))) if km_raw else None
        transmission = str(props.get("gearbox") or props.get("transmission") or "")

        loc = ad.get("location") or {}
        city_out = loc.get("municipio") or loc.get("city") or city

        images = []
        for img in ad.get("images") or []:
            images.append(img.get("original") or img.get("url") or "" if isinstance(img, dict) else str(img))
        images = [i for i in images if i][:3]

        brand, model = _split_brand_model(subj)

        return Car(
            id=f"olx_{lid}", source="olx", url=url,
            title=subj, brand=brand, model=model, version="",
            year=year, price=price, km=km,
            transmission=transmission, has_airbag=None,
            location=city_out, images=images,
        )
    except Exception:
        return None


# ── Helpers ───────────────────────────────────────────────────────────────────

def _split_brand_model(title: str) -> tuple[str, str]:
    up = title.upper()
    for brand in _KNOWN_BRANDS:
        if brand.upper() in up:
            rest = title[up.index(brand.upper()) + len(brand):].strip()
            model = rest.split()[0] if rest.split() else ""
            return brand, model
    parts = title.split()
    return (parts[0] if parts else ""), (parts[1] if len(parts) > 1 else "")


def _to_float(val) -> Optional[float]:
    try:
        return float(str(val).replace(".", "").replace(",", "."))
    except (ValueError, TypeError):
        return None
