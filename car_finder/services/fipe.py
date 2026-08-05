"""FIPE price lookup with local JSON cache and fuzzy brand/model matching."""
import json
import os
import time
from typing import Optional

import requests
from thefuzz import fuzz, process

from config import FIPE_CACHE_TTL

_APIS = [
    "https://parallelum.com.br/fipe/api/v2",
    "https://fipe.parallelum.com.br/api/v2",
]
_HEADERS = {"User-Agent": "Mozilla/5.0"}


class FipeService:
    def __init__(self, cache_file: str = "fipe_cache.json"):
        self.cache_file = cache_file
        self.cache: dict = self._load()

    # ── cache ────────────────────────────────────────────────────────────────

    def _load(self) -> dict:
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def _save(self) -> None:
        with open(self.cache_file, "w", encoding="utf-8") as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)

    def _fresh(self, key: str) -> bool:
        e = self.cache.get(key)
        return bool(e and (time.time() - e.get("_at", 0)) / 86400 < FIPE_CACHE_TTL)

    # ── HTTP ─────────────────────────────────────────────────────────────────

    def _get(self, endpoint: str):
        if self._fresh(endpoint):
            return self.cache[endpoint]["data"]
        for base in _APIS:
            try:
                r = requests.get(f"{base}{endpoint}", headers=_HEADERS, timeout=10)
                r.raise_for_status()
                data = r.json()
                self.cache[endpoint] = {"data": data, "_at": time.time()}
                self._save()
                time.sleep(0.2)
                return data
            except Exception:
                continue
        return None

    # ── FIPE API helpers ─────────────────────────────────────────────────────

    def brands(self) -> list[dict]:
        d = self._get("/cars/brands")
        return d if isinstance(d, list) else []

    def models(self, brand_code: str) -> list[dict]:
        d = self._get(f"/cars/brands/{brand_code}/models")
        return (d.get("models") or []) if isinstance(d, dict) else []

    def years(self, brand_code: str, model_code: str) -> list[dict]:
        d = self._get(f"/cars/brands/{brand_code}/models/{model_code}/years")
        return d if isinstance(d, list) else []

    def price(self, brand_code: str, model_code: str, year_code: str) -> Optional[float]:
        d = self._get(f"/cars/brands/{brand_code}/models/{model_code}/years/{year_code}")
        if isinstance(d, dict):
            raw = str(d.get("price", "")).replace("R$", "").replace(".", "").replace(",", ".").strip()
            try:
                return float(raw)
            except ValueError:
                pass
        return None

    # ── Public API ───────────────────────────────────────────────────────────

    def lookup(self, brand: str, model: str, year: int) -> tuple[Optional[float], Optional[str]]:
        """Return (fipe_price, fipe_model_name) or (None, None)."""
        all_brands = self.brands()
        if not all_brands:
            return None, None

        # Match brand
        bnames = [b["name"] for b in all_brands]
        bmatch = process.extractOne(brand, bnames, scorer=fuzz.token_sort_ratio)
        if not bmatch or bmatch[1] < 65:
            return None, None
        bcode = next(b["code"] for b in all_brands if b["name"] == bmatch[0])

        # Match model
        all_models = self.models(bcode)
        if not all_models:
            return None, None
        mnames = [m["name"] for m in all_models]

        # Try combined "Brand Model" first for better specificity
        combined = f"{bmatch[0]} {model}"
        cmatch = process.extractOne(
            combined, [f"{bmatch[0]} {n}" for n in mnames], scorer=fuzz.token_sort_ratio
        )
        matched_name = (cmatch[0].replace(f"{bmatch[0]} ", "", 1)
                        if cmatch and cmatch[1] >= 55 else None)
        if not matched_name:
            m2 = process.extractOne(model, mnames, scorer=fuzz.token_sort_ratio)
            if not m2 or m2[1] < 55:
                return None, None
            matched_name = m2[0]

        mcode = next(m["code"] for m in all_models if m["name"] == matched_name)

        # Find year options (multiple fuel types share the same year)
        all_years = self.years(bcode, mcode)
        year_opts = [y for y in all_years if str(year) in str(y.get("name", ""))]
        if not year_opts:
            return None, None

        prices = [p for yo in year_opts for p in [self.price(bcode, mcode, yo.get("code", ""))] if p]
        if not prices:
            return None, None

        return sum(prices) / len(prices), matched_name
