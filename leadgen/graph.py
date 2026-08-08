"""Graph agent (LangGraph) para o desafio 1: encontrar donos de imóvel
anunciando aluguel por conta própria (sem imobiliária).

Fluxo:
    buscar_anuncios -> enriquecer_anuncios -> qualificar_leads -> exportar_leads

Cada nó recebe o `LeadGenState` inteiro e devolve apenas as chaves que
alterou (padrão LangGraph de merge parcial de estado).
"""

from __future__ import annotations

import logging

from langgraph.graph import END, StateGraph

from leadgen.export import export_leads
from leadgen.qualify import qualify_listing, qualify_with_llm
from leadgen.sources.mock import MockOLXSource
from leadgen.sources.olx import OLXSource
from leadgen.state import LeadGenState

logger = logging.getLogger("leadgen.graph")


def _get_source(state: LeadGenState):
    return MockOLXSource() if state.get("mock") else OLXSource()


def buscar_anuncios(state: LeadGenState) -> dict:
    source = _get_source(state)
    listings = source.search(
        cidade=state.get("cidade", "São Paulo"),
        uf=state.get("uf", "sp"),
        max_paginas=state.get("max_paginas", 2),
        max_anuncios=state.get("max_anuncios", 40),
    )
    logger.info("Encontrados %d anúncios brutos", len(listings))
    return {
        "raw_listings": listings,
        "log": state.get("log", []) + [f"Busca: {len(listings)} anúncios encontrados"],
    }


def enriquecer_anuncios(state: LeadGenState) -> dict:
    source = _get_source(state)
    raw = state.get("raw_listings", [])
    enriched = source.enrich_all(raw)
    logger.info("Enriquecidos %d anúncios", len(enriched))
    return {
        "enriched_listings": enriched,
        "log": state.get("log", []) + [f"Enriquecimento: {len(enriched)} anúncios processados"],
    }


def qualificar_leads(state: LeadGenState) -> dict:
    qualified = []
    rejected = []
    for listing in state.get("enriched_listings", []):
        if listing.get("tipo_anunciante") == "desconhecido":
            listing = qualify_with_llm(listing)
        scored = qualify_listing(listing)
        (qualified if scored["qualificado"] else rejected).append(scored)

    logger.info("Qualificados: %d | Rejeitados: %d", len(qualified), len(rejected))
    return {
        "qualified_leads": qualified,
        "rejected_listings": rejected,
        "log": state.get("log", [])
        + [f"Qualificação: {len(qualified)} leads qualificados, {len(rejected)} rejeitados"],
    }


def exportar_leads(state: LeadGenState) -> dict:
    leads = state.get("qualified_leads", [])
    if not leads:
        return {"exported_path": "", "log": state.get("log", []) + ["Nenhum lead qualificado para exportar"]}

    path = export_leads(leads, output_dir=state.get("output_dir", "data"))
    logger.info("Leads exportados para %s", path)
    return {"exported_path": path, "log": state.get("log", []) + [f"Exportado para {path}"]}


def build_graph():
    graph = StateGraph(LeadGenState)
    graph.add_node("buscar_anuncios", buscar_anuncios)
    graph.add_node("enriquecer_anuncios", enriquecer_anuncios)
    graph.add_node("qualificar_leads", qualificar_leads)
    graph.add_node("exportar_leads", exportar_leads)

    graph.set_entry_point("buscar_anuncios")
    graph.add_edge("buscar_anuncios", "enriquecer_anuncios")
    graph.add_edge("enriquecer_anuncios", "qualificar_leads")
    graph.add_edge("qualificar_leads", "exportar_leads")
    graph.add_edge("exportar_leads", END)

    return graph.compile()
