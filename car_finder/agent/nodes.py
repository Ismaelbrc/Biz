"""
Graph nodes – each receives SearchState and returns a partial update dict.

Flow:  scrape_node → fipe_node → score_node → report_node
"""
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from rich.console import Console

from config import FIPE_CACHE_FILE, REPORT_HTML, REPORT_JSON
from models import Car

console = Console(stderr=True)


# ─────────────────────────────────────────────────────────────────────────────
# Node 1 – Scrape
# ─────────────────────────────────────────────────────────────────────────────

def scrape_node(state: dict) -> dict:
    from scrapers.olx import OLXScraper
    from scrapers.webmotors import WebmotorsScraper

    locations = state["locations"]
    errors: list[str] = list(state.get("errors", []))
    raw_cars: list[dict] = []
    seen_ids: set[str] = set()
    t0 = time.time()

    def _run_scraper(name: str, fn):
        try:
            cars = fn()
            console.print(f"  ✔ {name}: [green]{len(cars)}[/green] anúncios")
            return cars
        except Exception as exc:
            msg = f"{name}: {exc}"
            console.print(f"  ✘ {name}: [red]{exc}[/red]")
            errors.append(msg)
            return []

    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = {
            pool.submit(_run_scraper, "OLX",       lambda: OLXScraper().search_all(locations)): "olx",
            pool.submit(_run_scraper, "Webmotors", lambda: WebmotorsScraper().search_all(locations)): "webmotors",
        }
        for f in as_completed(futures):
            for car in f.result():
                if car.id not in seen_ids:
                    seen_ids.add(car.id)
                    raw_cars.append(car.to_dict())

    stats = dict(state.get("stats", {}))
    stats["scrape"] = {"count": len(raw_cars), "elapsed_s": round(time.time() - t0, 1)}

    return {"raw_cars": raw_cars, "stats": stats, "errors": errors}


# ─────────────────────────────────────────────────────────────────────────────
# Node 2 – FIPE enrichment
# ─────────────────────────────────────────────────────────────────────────────

def fipe_node(state: dict) -> dict:
    from services.fipe import FipeService

    fipe = FipeService(cache_file=FIPE_CACHE_FILE)
    raw = state["raw_cars"]
    errors: list[str] = list(state.get("errors", []))
    enriched: list[dict] = []
    t0 = time.time()
    hits = 0

    for i, d in enumerate(raw, 1):
        car = Car.from_dict(d)
        console.print(f"  FIPE [{i}/{len(raw)}] {car.title[:45]:<45}", end="\r")

        if car.brand and car.model and car.year:
            try:
                price, name = fipe.lookup(car.brand, car.model, car.year)
                if price:
                    car.fipe_price = price
                    car.fipe_model_name = name
                    car.discount_pct = round((price - car.price) / price * 100, 1)
                    hits += 1
            except Exception as exc:
                errors.append(f"FIPE {car.id}: {exc}")

        enriched.append(car.to_dict())

    console.print()  # newline after \r loop

    stats = dict(state.get("stats", {}))
    stats["fipe"] = {"total": len(raw), "hits": hits, "elapsed_s": round(time.time() - t0, 1)}

    return {"enriched": enriched, "stats": stats, "errors": errors}


# ─────────────────────────────────────────────────────────────────────────────
# Node 3 – Filter + Score
# ─────────────────────────────────────────────────────────────────────────────

def score_node(state: dict) -> dict:
    from services.scorer import score_car

    filters = state["filters"]
    enriched = state["enriched"]
    errors: list[str] = list(state.get("errors", []))
    scored: list[dict] = []
    opps: list[dict] = []
    t0 = time.time()

    for d in enriched:
        car = Car.from_dict(d)
        car = score_car(car, filters)
        scored.append(car.to_dict())
        if car.is_opportunity:
            opps.append(car.to_dict())

    opps.sort(key=lambda c: (c.get("discount_pct") or 0, c.get("opportunity_score") or 0), reverse=True)

    stats = dict(state.get("stats", {}))
    stats["score"] = {
        "total": len(scored),
        "opportunities": len(opps),
        "elapsed_s": round(time.time() - t0, 1),
    }

    return {"scored": scored, "opportunities": opps, "stats": stats, "errors": errors}


# ─────────────────────────────────────────────────────────────────────────────
# Node 4 – Report
# ─────────────────────────────────────────────────────────────────────────────

def report_node(state: dict) -> dict:
    from output.reporter import generate_html, save_json

    opps = state["opportunities"]
    total = len(state["raw_cars"])
    errors: list[str] = list(state.get("errors", []))
    t0 = time.time()

    cars = [Car.from_dict(d) for d in opps]

    html_path = generate_html(total, cars, html_file=REPORT_HTML)
    json_path = save_json(total, cars, json_file=REPORT_JSON)

    stats = dict(state.get("stats", {}))
    stats["report"] = {"elapsed_s": round(time.time() - t0, 1)}

    return {
        "report_html": html_path,
        "report_json": json_path,
        "stats": stats,
        "errors": errors,
    }
