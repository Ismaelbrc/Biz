"""Webmotors car scraper using their internal search API."""
import re
import time
from typing import List, Optional
from urllib.parse import urlencode, quote

import requests

from config import FILTERS, MAX_PAGES_PER_LOCATION, REQUEST_DELAY
from models import Car

_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "pt-BR,pt;q=0.9",
    "Referer": "https://www.webmotors.com.br/",
    "Origin": "https://www.webmotors.com.br",
}

_BASE_SEARCH = "https://www.webmotors.com.br/carros/estoque"
_API = "https://www.webmotors.com.br/api/search/car"
_PER_PAGE = 24


class WebmotorsScraper:
    def search_all(self, locations: list) -> List[Car]:
        all_cars: List[Car] = []
        seen_ids: set = set()

        for loc in locations:
            city = loc["wm_city"]
            state = loc["wm_state"]
            cars = self._search_location(city, state)
            for c in cars:
                if c.id not in seen_ids:
                    seen_ids.add(c.id)
                    all_cars.append(c)

        return all_cars

    def _search_location(self, city: str, state: str) -> List[Car]:
        search_params = {
            "EstadoCidade": f"{state}-{city}",
            "AnoModelo": FILTERS["year_min"],
            "AnoModeloAte": FILTERS["year_max"],
            "PrecoAte": FILTERS["price_max"],
            "KMAte": FILTERS["km_max"],
            "Cambio": "Automatico",
        }
        search_url = f"{_BASE_SEARCH}?{urlencode(search_params)}"

        cars: List[Car] = []

        for page in range(1, MAX_PAGES_PER_LOCATION + 1):
            api_params = {
                "url": search_url,
                "actualPage": page,
                "displayPerPage": _PER_PAGE,
                "order": 1,
                "showMenu": "true",
                "returnFacets": "false",
            }
            try:
                resp = requests.get(_API, params=api_params, headers=_HEADERS, timeout=15)
                resp.raise_for_status()
                data = resp.json()
            except Exception as exc:
                print(f"  [Webmotors] {city} pág {page}: {exc}")
                break

            results = data.get("SearchResults") or []
            if not results:
                break

            for item in results:
                car = _parse_item(item)
                if car:
                    cars.append(car)

            total = int(data.get("TotalCount") or 0)
            if page * _PER_PAGE >= total:
                break

            time.sleep(REQUEST_DELAY)

        return cars


# ---------------------------------------------------------------------------
# Parser helpers
# ---------------------------------------------------------------------------

def _parse_item(item: dict) -> Optional[Car]:
    try:
        spec = item.get("Specification") or {}

        brand = (spec.get("Make") or {}).get("Value") or ""
        model = (spec.get("Model") or {}).get("Value") or ""
        version = (spec.get("Version") or {}).get("Value") or ""
        year = int((spec.get("Year") or {}).get("ModelYear") or 0)
        price = float((spec.get("Price") or {}).get("Price") or 0)
        km = (spec.get("Mileage") or None)
        transmission = (spec.get("Transmission") or {}).get("Value") or ""

        if price <= 0:
            return None

        seller = item.get("Seller") or {}
        city = seller.get("City") or ""

        # Airbag detection from Optionals list
        optionals = spec.get("Optionals") or []
        has_airbag: Optional[bool] = None
        opt_lower = [str(o).lower() for o in optionals]
        if any("airbag" in o or "air bag" in o for o in opt_lower):
            has_airbag = True
        elif optionals:
            has_airbag = False

        # Build listing URL
        link = item.get("Link") or {}
        raw_link = link.get("Link") or "" if isinstance(link, dict) else str(link)
        url = f"https://www.webmotors.com.br{raw_link}" if raw_link.startswith("/") else raw_link

        # Images
        media = item.get("Media") or []
        images = [m.get("MediumImage") or m.get("LargeImage") or "" for m in media if isinstance(m, dict)]
        images = [i for i in images if i][:3]

        uid = str(item.get("UniqueId") or "")
        title = spec.get("Title") or f"{brand} {model} {year}"

        return Car(
            id=f"wm_{uid}",
            source="webmotors",
            url=url,
            title=title,
            brand=brand.title(),
            model=model.title(),
            version=version,
            year=year,
            price=price,
            km=int(km) if km else None,
            transmission=transmission,
            has_airbag=has_airbag,
            location=city,
            images=images,
        )
    except Exception:
        return None
