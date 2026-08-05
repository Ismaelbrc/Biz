"""Pure function: receives a Car + filters dict, returns scored Car."""
from models import Car


def score_car(car: Car, filters: dict) -> Car:
    alerts: list[str] = []
    score = 0.0

    # ── Hard disqualifiers ────────────────────────────────────────────────────
    if car.year and not (filters["year_min"] <= car.year <= filters["year_max"]):
        car.alerts = [f"Ano {car.year} fora do intervalo"]
        return car

    if car.price > filters["price_max"]:
        car.alerts = ["Preço acima do limite"]
        return car

    if car.km is not None and car.km > filters["km_max"]:
        car.alerts = [f"{car.km:,} km acima do limite".replace(",", ".")]
        return car

    if car.transmission:
        trans = car.transmission.lower()
        if not any(kw in trans for kw in filters["automatic_keywords"]):
            car.alerts = [f"Câmbio '{car.transmission}' não é automático"]
            return car

    if car.has_airbag is False:
        car.alerts = ["Airbag não informado / ausente"]
        return car

    # ── FIPE discount check ───────────────────────────────────────────────────
    if car.fipe_price is not None:
        discount = (car.fipe_price - car.price) / car.fipe_price
        if discount < filters["fipe_discount_min"]:
            car.alerts = [f"Apenas {discount:.0%} abaixo da FIPE (mín {filters['fipe_discount_min']:.0%})"]
            return car

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
        alerts.append("⚠️ Preço FIPE não encontrado – verifique manualmente")
        score += 10

    # ── Bonus criteria ────────────────────────────────────────────────────────
    if car.has_airbag is True:
        alerts.append("✅ Airbag confirmado")
        score += 5
    else:
        alerts.append("⚠️ Airbag: confirme no anúncio")

    if not car.transmission:
        alerts.append("⚠️ Câmbio: confirme câmbio automático no anúncio")

    if car.km is not None:
        if car.km < 40_000:
            alerts.append(f"✅ Baixíssima KM: {car.km:,} km".replace(",", "."))
            score += 20
        elif car.km < 70_000:
            alerts.append(f"✅ KM baixa: {car.km:,} km".replace(",", "."))
            score += 10

    if car.year and car.year >= 2017:
        score += 5

    alerts.append("🔍 Verificar histórico no DETRAN-GO antes de comprar")

    car.is_opportunity    = True
    car.opportunity_score = round(score, 1)
    car.alerts            = alerts
    return car
