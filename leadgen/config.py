"""Critérios do ICP (Ideal Customer Profile) para o desafio 1:

Encontrar pessoas físicas donas de imóvel que estão anunciando o imóvel
para alugar por conta própria (sem passar por imobiliária) — são o público-alvo
para vender um sistema de administração de aluguel.
"""

from dataclasses import dataclass, field


# Palavras que indicam que o anúncio é de uma imobiliária/corretor, não do
# dono do imóvel. Qualquer anúncio com forte presença desses termos é
# descartado.
IMOBILIARIA_KEYWORDS = [
    "imobiliária",
    "imobiliaria",
    "creci",
    "corretor",
    "corretora",
    "administradora de imóveis",
    "consultor imobiliário",
]

# Palavras que reforçam que quem está anunciando é o próprio proprietário.
PROPRIETARIO_KEYWORDS = [
    "direto com o proprietário",
    "direto com proprietario",
    "sem imobiliária",
    "sem imobiliaria",
    "particular",
    "trato direto",
    "alugo direto",
]


@dataclass
class SearchParams:
    """Parâmetros de uma rodada de busca."""

    cidade: str = "São Paulo"
    estado_uf: str = "sp"
    categoria: str = "imoveis"
    tipo_negocio: str = "aluguel"  # aluguel | venda
    max_paginas: int = 2
    max_anuncios: int = 40


@dataclass
class ExportConfig:
    output_dir: str = "data"
    formato: str = "csv"  # csv | json


DEFAULT_SEARCH = SearchParams()
DEFAULT_EXPORT = ExportConfig()
