"""Webmotors car scraper using their internal search API."""
import time
from typing import Optional
from urllib.parse import urlencode

import requests

from config import FILTERS, MAX_PAGES, REQUEST_DELAY
from models import Car

_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "pt-BR,pt;q=0.9",
    "Referer": "https://www.webmotors.com.br/",
    "Origin": "https://www.webmotors.com.br",
    "Sec-Fetch-Mode": "cors",
}

_SEARCH_BASE = "https://www.webmotors.com.br/carros/estoque"
_API         = "https://www.webmotors.com.br/api/search/car"
_PER_PAGE    = 24


class WebmotorsScraper:
    def search_all(self, locations: list) -> list[Car]:
        all_cars: list[Car] = []
        seen: set[str] = set()
        for loc in locations:
            for car in self._search_location(loc["wm_city"], loc["wm_state"]):
                if car.id not in seen:
                    seen.add(car.id)
                    all_cars.append(car)
        return all_cars

    def _search_location(self, city: str, state: str) -> list[Car]:
        search_url = f"{_SEARCH_BASE}?" + urlencode({
            "EstadoCidade": f"{state}-{city}",
            "AnoModelo":    FILTERS["year_min"],
            "AnoModeloAte": FILTERS["year_max"],
            "PrecoAte":     FILTERS["price_max"],
            "KMAte":        FILTERS["km_max"],
            "Cambio":       "Automatico",
        })
        cars: list[Car] = []

        for page in range(1, MAX_PAGES + 1):
            try:
                r = requests.get(_API, headers=_HEADERS, timeout=15, params={
                    "url": search_url, "actualPage": page,
                    "displayPerPage": _PER_PAGE, "order": 1,
                    "showMenu": "true", "returnFacets": "false",
                })
                r.raise_for_status()
                data = r.json()
            except Exception as exc:
                print(f"  [WM] {city} p{page}: {exc}")
                break

            results = data.get("SearchResults") or []
            if not results:
                break

            for item in results:
                car = _parse_item(item)
                if car:
                    cars.append(car)

            if page * _PER_PAGE >= int(data.get("TotalCount") or 0):
                break
            time.sleep(REQUEST_DELAY)

        return cars


# ── Parser ────────────────────────────────────────────────────────────────────

def _parse_item(item: dict) -> Optional[Car]:
    try:
        spec = item.get("Specification") or {}

        brand        = ((spec.get("Make")         or {}).get("Value") or "").title()
        model        = ((spec.get("Model")        or {}).get("Value") or "").title()
        version      = (spec.get("Version")       or {}).get("Value") or ""
        year         = int((spec.get("Year")      or {}).get("ModelYear") or 0)
        price        = float((spec.get("Price")   or {}).get("Price") or 0)
        km           = spec.get("Mileage")
        transmission = (spec.get("Transmission") or {}).get("Value") or ""

        if price <= 0:
            return None

        city = ((item.get("Seller") or {}).get("City") or "")

        # Airbag from Optionals list
        optionals = spec.get("Optionals") or []
        opt_lower = [str(o).lower() for o in optionals]
        has_airbag: Optional[bool] = None
        if any("airbag" in o or "air bag" in o for o in opt_lower):
            has_airbag = True
        elif optionals:
            has_airbag = False

        link = item.get("Link") or {}
        raw  = (link.get("Link") or "") if isinstance(link, dict) else str(link)
        url  = f"https://www.webmotors.com.br{raw}" if raw.startswith("/") else raw

        media  = item.get("Media") or []
        images = [m.get("MediumImage") or m.get("LargeImage") or "" for m in media if isinstance(m, dict)]
        images = [i for i in images if i][:3]

        uid = str(item.get("UniqueId") or "")

        return Car(
            id=f"wm_{uid}", source="webmotors", url=url,
            title=spec.get("Title") or f"{brand} {model} {year}",
            brand=brand, model=model, version=version,
            year=year, price=price,
            km=int(km) if km else None,
            transmission=transmission, has_airbag=has_airbag,
            location=city, images=images,
        )
    except Exception:
        return None
