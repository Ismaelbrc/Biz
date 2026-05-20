"""OLX car scraper – parses Next.js __NEXT_DATA__ embedded JSON."""
import json
import re
import time
from typing import List, Optional
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup

from config import FILTERS, MAX_PAGES_PER_LOCATION, REQUEST_DELAY
from models import Car

_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

_BASE = "https://www.olx.com.br"

_KNOWN_BRANDS = [
    "Volkswagen", "VW", "Chevrolet", "GM", "Fiat", "Ford", "Honda", "Toyota",
    "Hyundai", "Renault", "Nissan", "Peugeot", "Citroën", "Citroen",
    "Mitsubishi", "Kia", "Jeep", "BMW", "Mercedes", "Audi", "Volvo",
    "Land Rover", "Dodge", "Chery", "JAC", "Caoa Chery", "Suzuki",
    "Subaru", "Alfa Romeo", "Seat", "Skoda",
]


class OLXScraper:
    def search_all(self, locations: list) -> List[Car]:
        all_cars: List[Car] = []
        seen_ids: set = set()

        for loc in locations:
            cars = self._search_location(loc["olx_path"], loc["name"])
            for c in cars:
                if c.id not in seen_ids:
                    seen_ids.add(c.id)
                    all_cars.append(c)

        return all_cars

    def _search_location(self, olx_path: str, city_name: str) -> List[Car]:
        params = {
            "monetaryvalue": 1,
            "monetaryvalue_max": FILTERS["price_max"],
            "auto_yearfrom": FILTERS["year_min"],
            "auto_yearto": FILTERS["year_max"],
            "auto_mileageto": FILTERS["km_max"],
            "auto_gearbox": "Autom%C3%A1tico",
        }
        base_url = f"{_BASE}/{olx_path}/autos-e-pecas/carros-vans-e-utilitarios"

        cars: List[Car] = []

        for page in range(1, MAX_PAGES_PER_LOCATION + 1):
            query = urlencode(params)
            url = f"{base_url}?{query}" + (f"&o={page}" if page > 1 else "")

            try:
                resp = requests.get(url, headers=_HEADERS, timeout=15)
                if resp.status_code != 200:
                    break
                page_cars = _parse_page(resp.text, city_name)
                if not page_cars:
                    break
                cars.extend(page_cars)
                time.sleep(REQUEST_DELAY)
            except Exception as exc:
                print(f"  [OLX] {city_name} pág {page}: {exc}")
                break

        return cars


# ---------------------------------------------------------------------------
# Page parsers
# ---------------------------------------------------------------------------

def _parse_page(html: str, default_city: str) -> List[Car]:
    cars = _parse_next_data(html, default_city)
    if cars:
        return cars
    return _parse_html_fallback(html, default_city)


def _parse_next_data(html: str, default_city: str) -> List[Car]:
    try:
        soup = BeautifulSoup(html, "lxml")
        tag = soup.find("script", id="__NEXT_DATA__")
        if not tag:
            return []
        data = json.loads(tag.string)
        ads = (
            data.get("props", {})
                .get("pageProps", {})
                .get("ads", [])
        )
        if not ads:
            # Try alternative structure used in some OLX pages
            ads = (
                data.get("props", {})
                    .get("pageProps", {})
                    .get("listing", {})
                    .get("listing", {})
                    .get("ads", [])
            )
        return [c for ad in ads for c in [_parse_ad(ad, default_city)] if c]
    except Exception:
        return []


def _parse_html_fallback(html: str, default_city: str) -> List[Car]:
    """Very basic fallback – returns minimal Car objects."""
    cars = []
    try:
        soup = BeautifulSoup(html, "lxml")
        for a_tag in soup.select("a[href*='/item/']"):
            href = a_tag.get("href", "")
            if not href:
                continue
            title_el = a_tag.find(["h2", "h3", "span"])
            title = title_el.get_text(strip=True) if title_el else ""
            if not title:
                continue
            price_match = re.search(r"R\$\s*([\d\.]+)", a_tag.get_text())
            price = _to_float(price_match.group(1)) if price_match else None
            if not price:
                continue
            uid = href.rstrip("/").split("-")[-1]
            brand, model = _extract_brand_model(title)
            cars.append(Car(
                id=f"olx_{uid}",
                source="olx",
                url=href if href.startswith("http") else f"https://www.olx.com.br{href}",
                title=title,
                brand=brand,
                model=model,
                version="",
                year=0,
                price=price,
                location=default_city,
            ))
    except Exception:
        pass
    return cars


def _parse_ad(ad: dict, default_city: str) -> Optional[Car]:
    try:
        list_id = str(ad.get("listId") or ad.get("id") or "")
        subject = str(ad.get("subject") or ad.get("title") or "")
        url = str(ad.get("url") or ad.get("link") or "")

        # Price
        price = ad.get("priceValue") or ad.get("price")
        if isinstance(price, str):
            price = _to_float(re.sub(r"[^\d]", "", price))
        price = float(price or 0)
        if price <= 0:
            return None

        # Properties dict
        props: dict = {}
        for p in ad.get("properties") or []:
            if isinstance(p, dict):
                props[p.get("name", "")] = p.get("value", "")

        year = int(props.get("regdate") or props.get("year") or 0)
        km_raw = props.get("mileage") or props.get("km") or ""
        km = int(re.sub(r"[^\d]", "", str(km_raw))) if km_raw else None
        transmission = str(props.get("gearbox") or props.get("transmission") or "")

        # Location
        loc = ad.get("location") or {}
        city = loc.get("municipio") or loc.get("city") or default_city

        # Images
        images = []
        for img in ad.get("images") or []:
            if isinstance(img, dict):
                images.append(img.get("original") or img.get("url") or "")
            elif isinstance(img, str):
                images.append(img)
        images = [i for i in images if i][:3]

        brand, model = _extract_brand_model(subject)

        return Car(
            id=f"olx_{list_id}",
            source="olx",
            url=url,
            title=subject,
            brand=brand,
            model=model,
            version="",
            year=year,
            price=price,
            km=km,
            transmission=transmission,
            has_airbag=None,
            location=city,
            images=images,
        )
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------

def _extract_brand_model(title: str) -> tuple:
    upper = title.upper()
    for brand in _KNOWN_BRANDS:
        if brand.upper() in upper:
            idx = upper.index(brand.upper())
            rest = title[idx + len(brand):].strip()
            parts = rest.split()
            model = parts[0] if parts else ""
            return brand, model
    parts = title.split()
    return (parts[0] if parts else ""), (parts[1] if len(parts) > 1 else "")


def _to_float(val) -> Optional[float]:
    try:
        return float(str(val).replace(".", "").replace(",", "."))
    except (ValueError, TypeError):
        return None
