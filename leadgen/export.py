from __future__ import annotations

import csv
import json
import os
from datetime import datetime

FIELDS = [
    "id",
    "titulo",
    "url",
    "preco",
    "localizacao",
    "tipo_anunciante",
    "score",
    "motivo",
]


def export_leads(leads: list[dict], output_dir: str = "data", formato: str = "csv") -> str:
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if formato == "json":
        path = os.path.join(output_dir, f"leads_{timestamp}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(leads, f, ensure_ascii=False, indent=2)
        return path

    path = os.path.join(output_dir, f"leads_{timestamp}.csv")
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for lead in leads:
            writer.writerow(lead)
    return path
