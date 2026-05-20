"""Generates the HTML opportunity report and saves results JSON."""
import json
import os
from datetime import datetime
from typing import List

from jinja2 import Environment, FileSystemLoader

from config import REPORT_FILE, RESULTS_FILE
from models import Car

_TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")


def save_json(all_cars: List[Car], opportunities: List[Car]) -> None:
    data = {
        "generated_at": datetime.now().isoformat(),
        "total_listings": len(all_cars),
        "total_opportunities": len(opportunities),
        "opportunities": [_car_to_dict(c) for c in opportunities],
    }
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def generate_html(all_cars, opportunities: List[Car]) -> str:
    env = Environment(loader=FileSystemLoader(_TEMPLATE_DIR))
    tpl = env.get_template("report.html")

    discounts = [c.discount_vs_fipe * 100 for c in opportunities if c.discount_vs_fipe]
    total = len(all_cars) if hasattr(all_cars, "__len__") else 0

    html = tpl.render(
        cars=opportunities,
        generated_at=datetime.now().strftime("%d/%m/%Y %H:%M"),
        total_listings=total,
        total_opportunities=len(opportunities),
        best_discount=f"{max(discounts, default=0):.0f}",
        avg_discount=f"{(sum(discounts) / len(discounts)):.0f}" if discounts else "0",
    )

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    return REPORT_FILE


def _car_to_dict(c: Car) -> dict:
    return {
        "id": c.id,
        "source": c.source,
        "url": c.url,
        "title": c.title,
        "brand": c.brand,
        "model": c.model,
        "year": c.year,
        "price": c.price,
        "km": c.km,
        "transmission": c.transmission,
        "has_airbag": c.has_airbag,
        "location": c.location,
        "fipe_price": c.fipe_price,
        "fipe_model_name": c.fipe_model_name,
        "discount_vs_fipe": round(c.discount_vs_fipe * 100, 1) if c.discount_vs_fipe else None,
        "opportunity_score": c.opportunity_score,
        "alerts": c.alerts,
        "images": c.images,
    }
