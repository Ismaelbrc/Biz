"""Centralized search configuration."""

LOCATIONS = [
    {"name": "Goiânia",              "olx_path": "goias/goiania",              "wm_city": "Goiania",             "wm_state": "GO"},
    {"name": "Aparecida de Goiânia", "olx_path": "goias/aparecida-de-goiania","wm_city": "Aparecida de Goiania","wm_state": "GO"},
    {"name": "Senador Canedo",       "olx_path": "goias/senador-canedo",       "wm_city": "Senador Canedo",      "wm_state": "GO"},
    {"name": "Trindade",             "olx_path": "goias/trindade",             "wm_city": "Trindade",            "wm_state": "GO"},
    {"name": "Anápolis",             "olx_path": "goias/anapolis",             "wm_city": "Anapolis",            "wm_state": "GO"},
]

FILTERS = {
    "year_min": 2009,
    "year_max": 2020,
    "price_max": 60_000,
    "fipe_discount_min": 0.20,
    "km_max": 100_000,
    "automatic_keywords": [
        "automático", "automatico", "cvt", "dual", "sequencial",
        "tiptronic", "dct", "s-tronic", "powershift", "auto",
    ],
}

FIPE_CACHE_FILE  = "fipe_cache.json"
FIPE_CACHE_TTL   = 30
REPORT_HTML      = "oportunidades.html"
REPORT_JSON      = "resultados.json"

REQUEST_DELAY    = 1.5
MAX_PAGES        = 10
