"""Generates HTML report and JSON dump."""
import json
import os
from datetime import datetime

from jinja2 import Environment, FileSystemLoader

from models import Car

_TPL_DIR = os.path.join(os.path.dirname(__file__), "templates")


def generate_html(total_listings: int, opportunities: list[Car], html_file: str = "oportunidades.html") -> str:
    env = Environment(loader=FileSystemLoader(_TPL_DIR))
    tpl = env.get_template("report.html")

    discounts = [c.discount_pct for c in opportunities if c.discount_pct is not None]

    html = tpl.render(
        cars=opportunities,
        generated_at=datetime.now().strftime("%d/%m/%Y %H:%M"),
        total_listings=total_listings,
        total_opportunities=len(opportunities),
        best_discount=f"{max(discounts, default=0):.0f}",
        avg_discount=f"{(sum(discounts) / len(discounts)):.0f}" if discounts else "0",
    )
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    return html_file


def save_json(total_listings: int, opportunities: list[Car], json_file: str = "resultados.json") -> str:
    data = {
        "generated_at": datetime.now().isoformat(),
        "total_listings": total_listings,
        "total_opportunities": len(opportunities),
        "opportunities": [c.to_dict() for c in opportunities],
    }
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return json_file
