"""Fonte falsa usada em `--mock` para testar o graph agent sem rede
(sandbox sem acesso ao OLX, demo, testes automatizados)."""

from __future__ import annotations

_FIXTURES = [
    {
        "id": "1001",
        "titulo": "Apto 2 quartos direto com o proprietário, sem imobiliária",
        "url": "https://www.olx.com.br/anuncio/mock-1001",
        "preco": "R$ 1.800",
        "localizacao": "Vila Mariana, São Paulo - SP",
        "descricao": "Alugo direto, trato direto comigo, sem taxa de imobiliária. Aceito animais.",
        "tipo_anunciante": "particular",
    },
    {
        "id": "1002",
        "titulo": "Casa 3 quartos para alugar - Imobiliária Silva CRECI 12345",
        "url": "https://www.olx.com.br/anuncio/mock-1002",
        "preco": "R$ 3.200",
        "localizacao": "Moema, São Paulo - SP",
        "descricao": "Imobiliária Silva, atendimento profissional, agende uma visita com nosso corretor.",
        "tipo_anunciante": "imobiliaria",
    },
    {
        "id": "1003",
        "titulo": "Kitnet particular, alugo sem burocracia",
        "url": "https://www.olx.com.br/anuncio/mock-1003",
        "preco": "R$ 950",
        "localizacao": "Pinheiros, São Paulo - SP",
        "descricao": "Sou o proprietário, particular, quero alugar rápido pois estou me mudando de cidade.",
        "tipo_anunciante": "particular",
    },
    {
        "id": "1004",
        "titulo": "Studio mobiliado à venda",
        "url": "https://www.olx.com.br/anuncio/mock-1004",
        "preco": "R$ 320.000",
        "localizacao": "Itaim Bibi, São Paulo - SP",
        "descricao": "Vendo studio mobiliado, aceito financiamento.",
        "tipo_anunciante": "particular",
    },
]


class MockOLXSource:
    def search(self, cidade: str, uf: str, max_paginas: int, max_anuncios: int) -> list[dict]:
        return [
            {k: v for k, v in f.items() if k not in ("descricao", "tipo_anunciante")}
            for f in _FIXTURES[:max_anuncios]
        ]

    def enrich_all(self, listings: list[dict]) -> list[dict]:
        by_id = {f["id"]: f for f in _FIXTURES}
        enriched = []
        for listing in listings:
            fixture = by_id.get(listing["id"], {})
            merged = dict(listing)
            merged["descricao"] = fixture.get("descricao", "")
            merged["tipo_anunciante"] = fixture.get("tipo_anunciante", "desconhecido")
            enriched.append(merged)
        return enriched
