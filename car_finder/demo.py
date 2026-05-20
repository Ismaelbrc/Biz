#!/usr/bin/env python3
"""
Gera um relatório HTML de demonstração com dados fictícios realistas
para mostrar como o buscador funciona quando executado localmente.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from models import Car
from reporter import save_json, generate_html

DEMO_CARS: list[Car] = [
    Car(
        id="wm_11223344", source="webmotors",
        url="https://www.webmotors.com.br/carros/anuncio/example1",
        title="Honda HR-V EX CVT 2018",
        brand="Honda", model="HR-V", version="EX CVT", year=2018,
        price=47_500, km=62_000, transmission="CVT Automático",
        has_airbag=True, location="Goiânia",
        images=["https://via.placeholder.com/400x250/2563eb/fff?text=Honda+HR-V"],
        fipe_price=68_900, fipe_model_name="HR-V EX CVT",
        discount_vs_fipe=0.311,
        is_opportunity=True, opportunity_score=76.1,
        alerts=["🔥 31% abaixo da FIPE", "✅ Airbag confirmado", "🔍 Verificar histórico veicular no DETRAN-GO"],
    ),
    Car(
        id="olx_55667788", source="olx",
        url="https://www.olx.com.br/item/example2",
        title="Toyota Corolla GLi 2016 Automático",
        brand="Toyota", model="Corolla", version="GLi", year=2016,
        price=52_000, km=78_000, transmission="Automático",
        has_airbag=True, location="Anápolis",
        images=["https://via.placeholder.com/400x250/dc2626/fff?text=Toyota+Corolla"],
        fipe_price=75_600, fipe_model_name="Corolla GLi 1.8 Flex",
        discount_vs_fipe=0.312,
        is_opportunity=True, opportunity_score=71.2,
        alerts=["🔥 31% abaixo da FIPE", "✅ Airbag confirmado", "✅ Quilometragem razoável: 78.000 km", "🔍 Verificar histórico veicular no DETRAN-GO"],
    ),
    Car(
        id="wm_99887766", source="webmotors",
        url="https://www.webmotors.com.br/carros/anuncio/example3",
        title="Volkswagen Jetta Highline TSI 2017",
        brand="Volkswagen", model="Jetta", version="Highline TSI", year=2017,
        price=58_900, km=55_000, transmission="Automático DSG",
        has_airbag=True, location="Goiânia",
        images=["https://via.placeholder.com/400x250/16a34a/fff?text=VW+Jetta"],
        fipe_price=84_200, fipe_model_name="Jetta Highline 1.4 TSI",
        discount_vs_fipe=0.301,
        is_opportunity=True, opportunity_score=68.4,
        alerts=["🔥 30% abaixo da FIPE", "✅ Airbag confirmado", "✅ Baixa quilometragem: 55.000 km", "🔍 Verificar histórico veicular no DETRAN-GO"],
    ),
    Car(
        id="olx_44332211", source="olx",
        url="https://www.olx.com.br/item/example4",
        title="Hyundai HB20S Premium 2019 Aut",
        brand="Hyundai", model="HB20S", version="Premium", year=2019,
        price=41_000, km=38_500, transmission="Automático",
        has_airbag=True, location="Aparecida de Goiânia",
        images=["https://via.placeholder.com/400x250/7c3aed/fff?text=Hyundai+HB20S"],
        fipe_price=57_800, fipe_model_name="HB20S Premium 1.6 AT",
        discount_vs_fipe=0.290,
        is_opportunity=True, opportunity_score=64.0,
        alerts=["✅ 29% abaixo da FIPE", "✅ Airbag confirmado", "✅ Baixíssima quilometragem: 38.500 km", "🔍 Verificar histórico veicular no DETRAN-GO"],
    ),
    Car(
        id="wm_13245768", source="webmotors",
        url="https://www.webmotors.com.br/carros/anuncio/example5",
        title="Chevrolet Cruze LTZ Turbo 2018",
        brand="Chevrolet", model="Cruze", version="LTZ Turbo", year=2018,
        price=55_000, km=71_000, transmission="Automático",
        has_airbag=True, location="Goiânia",
        images=["https://via.placeholder.com/400x250/ea580c/fff?text=Chevrolet+Cruze"],
        fipe_price=77_400, fipe_model_name="Cruze LTZ 1.4 Turbo",
        discount_vs_fipe=0.289,
        is_opportunity=True, opportunity_score=60.5,
        alerts=["✅ 29% abaixo da FIPE", "✅ Airbag confirmado", "🔍 Verificar histórico veicular no DETRAN-GO"],
    ),
    Car(
        id="olx_86420975", source="olx",
        url="https://www.olx.com.br/item/example6",
        title="Renault Kwid Intense 2020 Automático",
        brand="Renault", model="Kwid", version="Intense", year=2020,
        price=29_900, km=32_000, transmission="Automático",
        has_airbag=None, location="Senador Canedo",
        images=["https://via.placeholder.com/400x250/0891b2/fff?text=Renault+Kwid"],
        fipe_price=42_500, fipe_model_name="Kwid Intense 1.0 SCe",
        discount_vs_fipe=0.296,
        is_opportunity=True, opportunity_score=58.0,
        alerts=["✅ 30% abaixo da FIPE", "⚠️ Airbag: verifique no anúncio", "✅ Baixíssima quilometragem: 32.000 km", "🔍 Verificar histórico veicular no DETRAN-GO"],
    ),
    Car(
        id="wm_57391840", source="webmotors",
        url="https://www.webmotors.com.br/carros/anuncio/example7",
        title="Ford EcoSport FreeStyle 2017 AT",
        brand="Ford", model="EcoSport", version="FreeStyle", year=2017,
        price=43_500, km=88_000, transmission="Automático",
        has_airbag=True, location="Anápolis",
        images=["https://via.placeholder.com/400x250/854d0e/fff?text=Ford+EcoSport"],
        fipe_price=60_100, fipe_model_name="EcoSport FreeStyle 1.6 AT",
        discount_vs_fipe=0.276,
        is_opportunity=True, opportunity_score=52.3,
        alerts=["✅ 28% abaixo da FIPE", "✅ Airbag confirmado", "🔍 Verificar histórico veicular no DETRAN-GO"],
    ),
    Car(
        id="olx_10293847", source="olx",
        url="https://www.olx.com.br/item/example8",
        title="Kia Sportage EX 2016 Aut",
        brand="Kia", model="Sportage", version="EX", year=2016,
        price=56_000, km=64_000, transmission="Automático",
        has_airbag=True, location="Goiânia",
        images=["https://via.placeholder.com/400x250/475569/fff?text=Kia+Sportage"],
        fipe_price=77_300, fipe_model_name="Sportage EX 2.0 AWD AT",
        discount_vs_fipe=0.276,
        is_opportunity=True, opportunity_score=51.0,
        alerts=["✅ 28% abaixo da FIPE", "✅ Airbag confirmado", "✅ Baixa quilometragem: 64.000 km", "🔍 Verificar histórico veicular no DETRAN-GO"],
    ),
    Car(
        id="wm_29384756", source="webmotors",
        url="https://www.webmotors.com.br/carros/anuncio/example9",
        title="Jeep Renegade Longitude 2018 AT",
        brand="Jeep", model="Renegade", version="Longitude", year=2018,
        price=57_500, km=92_000, transmission="Automático",
        has_airbag=True, location="Trindade",
        images=["https://via.placeholder.com/400x250/1e3a5f/fff?text=Jeep+Renegade"],
        fipe_price=78_900, fipe_model_name="Renegade Longitude 1.8 AT",
        discount_vs_fipe=0.271,
        is_opportunity=True, opportunity_score=46.1,
        alerts=["✅ 27% abaixo da FIPE", "✅ Airbag confirmado", "🔍 Verificar histórico veicular no DETRAN-GO"],
    ),
    Car(
        id="olx_74839201", source="olx",
        url="https://www.olx.com.br/item/example10",
        title="Fiat Cronos Drive 1.3 AT 2019",
        brand="Fiat", model="Cronos", version="Drive AT", year=2019,
        price=38_000, km=41_000, transmission="Automático",
        has_airbag=True, location="Goiânia",
        images=["https://via.placeholder.com/400x250/9333ea/fff?text=Fiat+Cronos"],
        fipe_price=51_500, fipe_model_name="Cronos Drive 1.3 AT",
        discount_vs_fipe=0.262,
        is_opportunity=True, opportunity_score=44.8,
        alerts=["✅ 26% abaixo da FIPE", "✅ Airbag confirmado", "✅ Baixíssima quilometragem: 41.000 km", "🔍 Verificar histórico veicular no DETRAN-GO"],
    ),
]

# Simulate a total of fake listings analyzed
ALL_CARS_COUNT = 347


def main():
    import os
    out = generate_html(
        type("FakeList", (), {"__len__": lambda s: ALL_CARS_COUNT})(),
        DEMO_CARS
    )
    abs_path = os.path.abspath(out)
    print(f"✅ Relatório demo gerado: {abs_path}")
    print("Abra o arquivo no navegador para visualizar.")


if __name__ == "__main__":
    main()
