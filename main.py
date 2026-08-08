"""CLI do graph agent de captação de leads (donos de imóvel para alugar).

Uso:
    python main.py --cidade "São Paulo" --uf sp --max-anuncios 40
    python main.py --mock          # roda com dados de exemplo, sem rede
"""

from __future__ import annotations

import argparse
import logging

from dotenv import load_dotenv

from leadgen.graph import build_graph


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Graph agent de captação de leads")
    parser.add_argument("--cidade", default="São Paulo")
    parser.add_argument("--uf", default="sp")
    parser.add_argument("--max-paginas", type=int, default=2)
    parser.add_argument("--max-anuncios", type=int, default=40)
    parser.add_argument("--output-dir", default="data")
    parser.add_argument("--mock", action="store_true", help="usa dados de exemplo, sem acessar a internet")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING)

    agent = build_graph()
    final_state = agent.invoke(
        {
            "cidade": args.cidade,
            "uf": args.uf,
            "max_paginas": args.max_paginas,
            "max_anuncios": args.max_anuncios,
            "output_dir": args.output_dir,
            "mock": args.mock,
        }
    )

    for line in final_state.get("log", []):
        print(f"- {line}")

    leads = final_state.get("qualified_leads", [])
    print(f"\n{len(leads)} leads qualificados (donos de imóvel anunciando aluguel direto):")
    for lead in leads:
        print(f"  [{lead['score']:>3}] {lead['titulo']} — {lead['localizacao']} — {lead['url']}")

    if final_state.get("exported_path"):
        print(f"\nArquivo: {final_state['exported_path']}")


if __name__ == "__main__":
    main()
