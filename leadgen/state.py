"""Estado compartilhado entre os nós do graph agent (LangGraph)."""

from __future__ import annotations

from typing import TypedDict


class Listing(dict):
    """Um anúncio de imóvel para alugar.

    Estrutura (dict simples para ficar fácil de serializar/exportar):
      id, titulo, url, preco, bairro, cidade, descricao,
      tipo_anunciante ("particular" | "imobiliaria" | "desconhecido"),
      telefone_link, publicado_em, score, motivo_score
    """


class LeadGenState(TypedDict, total=False):
    cidade: str
    max_anuncios: int
    mock: bool

    raw_listings: list[dict]
    enriched_listings: list[dict]
    qualified_leads: list[dict]
    rejected_listings: list[dict]

    exported_path: str
    log: list[str]
