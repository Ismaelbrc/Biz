"""
Demo mode – gera relatório HTML com dados realistas de 2025
sem precisar de conexão com OLX/Webmotors/FIPE.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from models import Car
from output.reporter import generate_html, save_json
from config import REPORT_HTML, REPORT_JSON

# Preços FIPE de referência (agosto 2025)
DEMO_CARS: list[Car] = [
    Car(
        id="wm_10011", source="webmotors",
        url="https://www.webmotors.com.br/carros/anuncio/demo1",
        title="Honda HR-V EX CVT 2018",
        brand="Honda", model="HR-V", version="EX CVT 1.8", year=2018,
        price=46_900, km=58_000, transmission="CVT Automático",
        has_airbag=True, location="Goiânia",
        images=["https://placehold.co/400x250/1e3a5f/fff?text=Honda+HR-V+2018"],
        fipe_price=69_450, fipe_model_name="HR-V EX CVT 1.8",
        discount_pct=32.5,
        is_opportunity=True, opportunity_score=82.0,
        alerts=["🔥 33% abaixo da FIPE – oportunidade rara!", "✅ Airbag confirmado",
                "✅ KM baixa: 58.000 km", "🔍 Verificar histórico no DETRAN-GO antes de comprar"],
    ),
    Car(
        id="olx_20022", source="olx",
        url="https://www.olx.com.br/item/demo2",
        title="Toyota Corolla GLi 2.0 2016 AT",
        brand="Toyota", model="Corolla", version="GLi 2.0 Flex AT", year=2016,
        price=51_500, km=76_000, transmission="Automático",
        has_airbag=True, location="Anápolis",
        images=["https://placehold.co/400x250/991b1b/fff?text=Toyota+Corolla+2016"],
        fipe_price=76_200, fipe_model_name="Corolla GLi 2.0 Flex",
        discount_pct=32.4,
        is_opportunity=True, opportunity_score=78.4,
        alerts=["🔥 32% abaixo da FIPE", "✅ Airbag confirmado",
                "🔍 Verificar histórico no DETRAN-GO antes de comprar"],
    ),
    Car(
        id="wm_10033", source="webmotors",
        url="https://www.webmotors.com.br/carros/anuncio/demo3",
        title="Hyundai Creta Pulse 1.6 2019 AT",
        brand="Hyundai", model="Creta", version="Pulse 1.6 AT", year=2019,
        price=56_800, km=44_000, transmission="Automático",
        has_airbag=True, location="Goiânia",
        images=["https://placehold.co/400x250/14532d/fff?text=Hyundai+Creta+2019"],
        fipe_price=83_900, fipe_model_name="Creta Pulse 1.6 AT",
        discount_pct=32.3,
        is_opportunity=True, opportunity_score=77.1,
        alerts=["🔥 32% abaixo da FIPE", "✅ Airbag confirmado",
                "✅ Baixíssima KM: 44.000 km", "🔍 Verificar histórico no DETRAN-GO antes de comprar"],
    ),
    Car(
        id="wm_10044", source="webmotors",
        url="https://www.webmotors.com.br/carros/anuncio/demo4",
        title="Jeep Compass Longitude 2019 AT",
        brand="Jeep", model="Compass", version="Longitude 2.0 AT", year=2019,
        price=58_500, km=62_000, transmission="Automático",
        has_airbag=True, location="Goiânia",
        images=["https://placehold.co/400x250/1e3a5f/fff?text=Jeep+Compass+2019"],
        fipe_price=86_200, fipe_model_name="Compass Longitude 2.0 AT",
        discount_pct=32.1,
        is_opportunity=True, opportunity_score=74.5,
        alerts=["🔥 32% abaixo da FIPE", "✅ Airbag confirmado",
                "✅ KM baixa: 62.000 km", "🔍 Verificar histórico no DETRAN-GO antes de comprar"],
    ),
    Car(
        id="olx_20055", source="olx",
        url="https://www.olx.com.br/item/demo5",
        title="Chevrolet Cruze LTZ Turbo 2018 AT",
        brand="Chevrolet", model="Cruze", version="LTZ 1.4 Turbo AT", year=2018,
        price=54_900, km=71_000, transmission="Automático",
        has_airbag=True, location="Aparecida de Goiânia",
        images=["https://placehold.co/400x250/7c2d12/fff?text=Chevrolet+Cruze+2018"],
        fipe_price=79_800, fipe_model_name="Cruze LTZ 1.4 Turbo",
        discount_pct=31.2,
        is_opportunity=True, opportunity_score=70.0,
        alerts=["🔥 31% abaixo da FIPE", "✅ Airbag confirmado",
                "🔍 Verificar histórico no DETRAN-GO antes de comprar"],
    ),
    Car(
        id="wm_10066", source="webmotors",
        url="https://www.webmotors.com.br/carros/anuncio/demo6",
        title="Volkswagen Jetta Highline TSI 2017 DSG",
        brand="Volkswagen", model="Jetta", version="Highline 1.4 TSI DSG", year=2017,
        price=57_900, km=53_000, transmission="Automático DSG",
        has_airbag=True, location="Goiânia",
        images=["https://placehold.co/400x250/0f172a/fff?text=VW+Jetta+2017"],
        fipe_price=83_700, fipe_model_name="Jetta Highline 1.4 TSI",
        discount_pct=30.8,
        is_opportunity=True, opportunity_score=68.5,
        alerts=["🔥 31% abaixo da FIPE", "✅ Airbag confirmado",
                "✅ KM baixa: 53.000 km", "🔍 Verificar histórico no DETRAN-GO antes de comprar"],
    ),
    Car(
        id="olx_20077", source="olx",
        url="https://www.olx.com.br/item/demo7",
        title="Fiat Toro Freedom 1.8 AT 2018",
        brand="Fiat", model="Toro", version="Freedom 1.8 AT", year=2018,
        price=54_000, km=88_000, transmission="Automático",
        has_airbag=True, location="Anápolis",
        images=["https://placehold.co/400x250/4a044e/fff?text=Fiat+Toro+2018"],
        fipe_price=77_400, fipe_model_name="Toro Freedom 1.8 AT",
        discount_pct=30.2,
        is_opportunity=True, opportunity_score=62.0,
        alerts=["🔥 30% abaixo da FIPE", "✅ Airbag confirmado",
                "🔍 Verificar histórico no DETRAN-GO antes de comprar"],
    ),
    Car(
        id="wm_10088", source="webmotors",
        url="https://www.webmotors.com.br/carros/anuncio/demo8",
        title="Honda Fit EX CVT 2017",
        brand="Honda", model="Fit", version="EX CVT 1.5", year=2017,
        price=37_500, km=39_000, transmission="CVT Automático",
        has_airbag=True, location="Senador Canedo",
        images=["https://placehold.co/400x250/083344/fff?text=Honda+Fit+2017"],
        fipe_price=53_800, fipe_model_name="Fit EX CVT 1.5",
        discount_pct=30.3,
        is_opportunity=True, opportunity_score=65.0,
        alerts=["🔥 30% abaixo da FIPE", "✅ Airbag confirmado",
                "✅ Baixíssima KM: 39.000 km", "🔍 Verificar histórico no DETRAN-GO antes de comprar"],
    ),
    Car(
        id="wm_10099", source="webmotors",
        url="https://www.webmotors.com.br/carros/anuncio/demo9",
        title="Renault Duster Oroch Dynamique 2018",
        brand="Renault", model="Duster Oroch", version="Dynamique 2.0 AT", year=2018,
        price=45_900, km=67_000, transmission="Automático",
        has_airbag=True, location="Trindade",
        images=["https://placehold.co/400x250/1c1917/fff?text=Renault+Oroch+2018"],
        fipe_price=64_100, fipe_model_name="Duster Oroch Dynamique 2.0",
        discount_pct=28.4,
        is_opportunity=True, opportunity_score=54.0,
        alerts=["✅ 28% abaixo da FIPE", "✅ Airbag confirmado",
                "🔍 Verificar histórico no DETRAN-GO antes de comprar"],
    ),
    Car(
        id="olx_20100", source="olx",
        url="https://www.olx.com.br/item/demo10",
        title="Ford EcoSport Titanium 2.0 2017 AT",
        brand="Ford", model="EcoSport", version="Titanium 2.0 AT", year=2017,
        price=43_500, km=82_000, transmission="Automático",
        has_airbag=True, location="Goiânia",
        images=["https://placehold.co/400x250/292524/fff?text=Ford+EcoSport+2017"],
        fipe_price=60_200, fipe_model_name="EcoSport Titanium 2.0 AT",
        discount_pct=27.7,
        is_opportunity=True, opportunity_score=51.0,
        alerts=["✅ 28% abaixo da FIPE", "✅ Airbag confirmado",
                "🔍 Verificar histórico no DETRAN-GO antes de comprar"],
    ),
    Car(
        id="wm_10111", source="webmotors",
        url="https://www.webmotors.com.br/carros/anuncio/demo11",
        title="Nissan Kicks SV 1.6 CVT 2019",
        brand="Nissan", model="Kicks", version="SV 1.6 CVT", year=2019,
        price=55_000, km=47_000, transmission="CVT Automático",
        has_airbag=True, location="Goiânia",
        images=["https://placehold.co/400x250/172554/fff?text=Nissan+Kicks+2019"],
        fipe_price=75_900, fipe_model_name="Kicks SV 1.6 CVT",
        discount_pct=27.5,
        is_opportunity=True, opportunity_score=55.0,
        alerts=["✅ 28% abaixo da FIPE", "✅ Airbag confirmado",
                "✅ Baixíssima KM: 47.000 km", "🔍 Verificar histórico no DETRAN-GO antes de comprar"],
    ),
    Car(
        id="olx_20122", source="olx",
        url="https://www.olx.com.br/item/demo12",
        title="Fiat Cronos Precision AT 2020",
        brand="Fiat", model="Cronos", version="Precision 1.3 AT", year=2020,
        price=42_900, km=28_000, transmission="Automático",
        has_airbag=True, location="Anápolis",
        images=["https://placehold.co/400x250/4a1942/fff?text=Fiat+Cronos+2020"],
        fipe_price=58_700, fipe_model_name="Cronos Precision 1.3 AT",
        discount_pct=26.9,
        is_opportunity=True, opportunity_score=53.0,
        alerts=["✅ 27% abaixo da FIPE", "✅ Airbag confirmado",
                "✅ Baixíssima KM: 28.000 km", "🔍 Verificar histórico no DETRAN-GO antes de comprar"],
    ),
]

TOTAL_LISTINGS = 412   # simulated total analyzed


def run_demo():
    from rich.console import Console
    console = Console()

    html = generate_html(TOTAL_LISTINGS, DEMO_CARS, html_file=REPORT_HTML)
    save_json(TOTAL_LISTINGS, DEMO_CARS, json_file=REPORT_JSON)

    console.print(f"\n[bold green]✅ Relatório demo gerado![/bold green]")
    console.print(f"[cyan]{os.path.abspath(html)}[/cyan]")
    console.print("[dim]Abra o arquivo no navegador para ver.[/dim]\n")


if __name__ == "__main__":
    run_demo()
