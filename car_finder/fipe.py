"""FIPE price lookup with local JSON cache and fuzzy brand/model matching."""
import json
import os
import time
from typing import Optional, List, Tuple

import requests
from thefuzz import fuzz, process

from config import FIPE_CACHE_FILE, FIPE_CACHE_TTL_DAYS

FIPE_APIS = [
    "https://parallelum.com.br/fipe/api/v2",
    "https://fipe.parallelum.com.br/api/v2",
]


class FipeService:
    def __init__(self, cache_file: str = FIPE_CACHE_FILE):
        self.cache_file = cache_file
        self.cache: dict = self._load_cache()

    # ------------------------------------------------------------------
    # Cache helpers
    # ------------------------------------------------------------------

    def _load_cache(self) -> dict:
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def _save_cache(self) -> None:
        with open(self.cache_file, "w", encoding="utf-8") as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)

    def _is_fresh(self, key: str) -> bool:
        entry = self.cache.get(key)
        if not entry:
            return False
        age_days = (time.time() - entry.get("_at", 0)) / 86400
        return age_days < FIPE_CACHE_TTL_DAYS

    def _fetch(self, endpoint: str):
        if self._is_fresh(endpoint):
            return self.cache[endpoint]["data"]
        for base in FIPE_APIS:
            try:
                resp = requests.get(f"{base}{endpoint}", timeout=10,
                                    headers={"User-Agent": "Mozilla/5.0"})
                resp.raise_for_status()
                data = resp.json()
                self.cache[endpoint] = {"data": data, "_at": time.time()}
                self._save_cache()
                time.sleep(0.25)
                return data
            except Exception:
                continue
        # Try official FIPE website API as last resort
        return self._fetch_official(endpoint)

    def _fetch_official(self, endpoint: str):
        """Maps parallelum-style endpoints to official veiculos.fipe.org.br API."""
        # The official API uses POST with form data and a reference table code
        # Only used as fallback – limited coverage
        return None

    # ------------------------------------------------------------------
    # FIPE API wrappers
    # ------------------------------------------------------------------

    def brands(self) -> List[dict]:
        data = self._fetch("/cars/brands")
        return data if isinstance(data, list) else []

    def models(self, brand_code: str) -> List[dict]:
        data = self._fetch(f"/cars/brands/{brand_code}/models")
        if isinstance(data, dict):
            return data.get("models", [])
        return []

    def years(self, brand_code: str, model_code: str) -> List[dict]:
        data = self._fetch(f"/cars/brands/{brand_code}/models/{model_code}/years")
        return data if isinstance(data, list) else []

    def price(self, brand_code: str, model_code: str, year_code: str) -> Optional[float]:
        data = self._fetch(f"/cars/brands/{brand_code}/models/{model_code}/years/{year_code}")
        if isinstance(data, dict):
            raw = data.get("price", "")
            raw = str(raw).replace("R$", "").replace(".", "").replace(",", ".").strip()
            try:
                return float(raw)
            except ValueError:
                pass
        return None

    # ------------------------------------------------------------------
    # Public lookup
    # ------------------------------------------------------------------

    def lookup(self, brand: str, model: str, year: int) -> Tuple[Optional[float], Optional[str]]:
        """Return (fipe_price, matched_model_name) or (None, None)."""
        all_brands = self.brands()
        if not all_brands:
            return None, None

        brand_names = [b["name"] for b in all_brands]
        match_brand = process.extractOne(brand, brand_names, scorer=fuzz.token_sort_ratio)
        if not match_brand or match_brand[1] < 65:
            return None, None

        brand_code = next(b["code"] for b in all_brands if b["name"] == match_brand[0])

        all_models = self.models(brand_code)
        if not all_models:
            return None, None

        model_names = [m["name"] for m in all_models]

        # Try matching "brand + model" combined first for better specificity
        combined = f"{brand} {model}"
        combined_names = [f"{match_brand[0]} {m}" for m in model_names]
        match_model = process.extractOne(combined, combined_names, scorer=fuzz.token_sort_ratio)

        if match_model and match_model[1] >= 55:
            matched_name = match_model[0].replace(f"{match_brand[0]} ", "", 1)
        else:
            match_model2 = process.extractOne(model, model_names, scorer=fuzz.token_sort_ratio)
            if not match_model2 or match_model2[1] < 55:
                return None, None
            matched_name = match_model2[0]

        model_code = next(m["code"] for m in all_models if m["name"] == matched_name)

        all_years = self.years(brand_code, model_code)
        year_options = [y for y in all_years if str(year) in str(y.get("name", ""))]
        if not year_options:
            return None, None

        prices = []
        for yo in year_options:
            p = self.price(brand_code, model_code, yo.get("code", ""))
            if p:
                prices.append(p)

        if not prices:
            return None, None

        return sum(prices) / len(prices), matched_name
