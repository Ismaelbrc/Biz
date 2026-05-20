"""Scores each car and marks it as an opportunity if it passes all filters."""
from typing import List

from config import FILTERS
from fipe import FipeService
from models import Car


class OpportunityScorer:
    def __init__(self, fipe: FipeService):
        self.fipe = fipe

    def score_all(self, cars: List[Car]) -> List[Car]:
        results = []
        total = len(cars)
        for i, car in enumerate(cars, 1):
            print(f"  [{i}/{total}] {car.title[:50]:<50}", end="\r")
            results.append(self._score(car))
        print()
        return results

    def _score(self, car: Car) -> Car:
        alerts: List[str] = []
        score = 0.0

        # ── Hard filters ──────────────────────────────────────────────
        if car.year and (car.year < FILTERS["year_min"] or car.year > FILTERS["year_max"]):
            car.alerts = [f"Ano {car.year} fora do intervalo"]
            return car

        if car.price > FILTERS["price_max"]:
            car.alerts = ["Preço acima do limite"]
            return car

        if car.km is not None and car.km > FILTERS["km_max"]:
            car.alerts = [f"{car.km:,} km acima do limite".replace(",", ".")]
            return car

        # Transmission check
        if car.transmission:
            trans_lower = car.transmission.lower()
            is_auto = any(kw in trans_lower for kw in FILTERS["automatic_keywords"])
            if not is_auto:
                car.alerts = [f"Câmbio '{car.transmission}' – não automático"]
                return car
        # If transmission unknown, keep the car but flag it

        # Airbag: skip only if explicitly False
        if car.has_airbag is False:
            car.alerts = ["Sem airbag informado"]
            return car

        # ── FIPE lookup ───────────────────────────────────────────────
        fipe_price = None
        if car.brand and car.model and car.year:
            fipe_price, fipe_name = self.fipe.lookup(car.brand, car.model, car.year)
            if fipe_price:
                car.fipe_price = fipe_price
                car.fipe_model_name = fipe_name
                discount = (fipe_price - car.price) / fipe_price
                car.discount_vs_fipe = discount

                if discount < FILTERS["fipe_discount_min"]:
                    car.alerts = [f"Apenas {discount:.0%} abaixo da FIPE (mínimo {FILTERS['fipe_discount_min']:.0%})"]
                    return car

                # Discount tiers
                if discount >= 0.35:
                    alerts.append(f"🔥 {discount:.0%} abaixo da FIPE – oportunidade rara!")
                    score += 80
                elif discount >= 0.30:
                    alerts.append(f"🔥 {discount:.0%} abaixo da FIPE")
                    score += 60
                else:
                    alerts.append(f"✅ {discount:.0%} abaixo da FIPE")
                    score += 40
            else:
                # No FIPE data – include with caveat, low score
                alerts.append("⚠️ Preço FIPE não encontrado – compare manualmente")
                score += 10

        # ── Bonus scoring ─────────────────────────────────────────────
        if car.has_airbag is True:
            score += 5
            alerts.append("✅ Airbag confirmado")
        else:
            alerts.append("⚠️ Airbag: verifique no anúncio")

        if car.km is not None:
            if car.km < 40_000:
                score += 20
                alerts.append(f"✅ Baixíssima quilometragem: {car.km:,} km".replace(",", "."))
            elif car.km < 70_000:
                score += 10
                alerts.append(f"✅ Quilometragem baixa: {car.km:,} km".replace(",", "."))

        if car.year and car.year >= 2017:
            score += 5

        if not car.transmission:
            alerts.append("⚠️ Câmbio: verifique no anúncio (filtro automático aplicado na busca)")

        # Always remind about vehicle history
        alerts.append("🔍 Verificar histórico veicular no DETRAN-GO antes de comprar")

        car.is_opportunity = True
        car.opportunity_score = round(score, 1)
        car.alerts = alerts
        return car
