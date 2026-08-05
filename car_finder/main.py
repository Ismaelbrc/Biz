#!/usr/bin/env python3
"""
Car Opportunity Graph Agent
Busca oportunidades de carros em OLX e Webmotors usando um LangGraph pipeline.

Uso:
    python main.py                   # busca completa
    python main.py --demo            # gera relatório com dados de demonstração
    python main.py --skip-olx        # pula OLX
    python main.py --skip-webmotors  # pula Webmotors
"""
import argparse
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

from config import FILTERS, LOCATIONS, REPORT_HTML, REPORT_JSON
from models import Car

console = Console()


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo",           action="store_true", help="Relatório demo sem busca real")
    ap.add_argument("--skip-olx",       action="store_true")
    ap.add_argument("--skip-webmotors", action="store_true")
    return ap.parse_args()


def run_graph(skip_olx: bool = False, skip_wm: bool = False):
    """Executes the LangGraph pipeline and returns final state."""
    from agent.graph import build_graph

    initial_state = {
        "locations":     LOCATIONS,
        "filters":       FILTERS,
        "raw_cars":      [],
        "enriched":      [],
        "scored":        [],
        "opportunities": [],
        "report_html":   None,
        "report_json":   None,
        "stats":         {},
        "errors":        [],
    }

    if skip_olx or skip_wm:
        # Patch scrapers at runtime to skip selected sources
        import agent.nodes as nodes_mod
        original = nodes_mod.scrape_node

        def patched_scrape(state):
            from scrapers.olx import OLXScraper
            from scrapers.webmotors import WebmotorsScraper
            from concurrent.futures import ThreadPoolExecutor, as_completed

            locations = state["locations"]
            errors = list(state.get("errors", []))
            raw_cars = []
            seen: set[str] = set()
            t0 = time.time()

            tasks = []
            if not skip_olx:
                tasks.append(("OLX", lambda: OLXScraper().search_all(locations)))
            if not skip_wm:
                tasks.append(("Webmotors", lambda: WebmotorsScraper().search_all(locations)))

            with ThreadPoolExecutor(max_workers=2) as pool:
                futures = {pool.submit(fn): name for name, fn in tasks}
                for f in as_completed(futures):
                    name = futures[f]
                    try:
                        cars = f.result()
                        console.print(f"  ✔ {name}: [green]{len(cars)}[/green]")
                    except Exception as exc:
                        cars = []
                        errors.append(f"{name}: {exc}")
                    for car in cars:
                        if car.id not in seen:
                            seen.add(car.id)
                            raw_cars.append(car.to_dict())

            stats = dict(state.get("stats", {}))
            stats["scrape"] = {"count": len(raw_cars), "elapsed_s": round(time.time() - t0, 1)}
            return {"raw_cars": raw_cars, "stats": stats, "errors": errors}

        nodes_mod.scrape_node = patched_scrape

    graph = build_graph()
    return graph.invoke(initial_state)


def print_summary(state: dict):
    opps = state["opportunities"]
    stats = state.get("stats", {})

    console.print(f"\n[bold green]✅ {len(opps)} oportunidades encontradas![/bold green]")

    if opps:
        tbl = Table(title="Top 15 Oportunidades", box=box.SIMPLE_HEAVY,
                    style="cyan", show_lines=True)
        tbl.add_column("#",        width=3, justify="right")
        tbl.add_column("Anúncio",  width=34)
        tbl.add_column("Preço",    width=11, justify="right")
        tbl.add_column("FIPE",     width=11, justify="right")
        tbl.add_column("Desc.",    width=8,  justify="right")
        tbl.add_column("Ano",      width=5)
        tbl.add_column("KM",       width=9,  justify="right")
        tbl.add_column("Cidade",   width=18)
        tbl.add_column("Fonte",    width=10)

        for i, d in enumerate(opps[:15], 1):
            c = Car.from_dict(d)
            disc = f"{c.discount_pct:.0f}%" if c.discount_pct else "?"
            disc_s = f"[bold red]{disc}[/bold red]" if (c.discount_pct or 0) >= 30 else f"[green]{disc}[/green]"
            tbl.add_row(
                str(i), c.title[:33],
                f"[bold green]R${c.price:,.0f}[/bold green]".replace(",", "."),
                f"R${c.fipe_price:,.0f}".replace(",", ".") if c.fipe_price else "–",
                disc_s,
                str(c.year or "–"),
                f"{c.km:,}".replace(",", ".") if c.km else "–",
                c.location[:17], c.source.upper(),
            )
        console.print(tbl)

    # Timing
    total_s = sum(v.get("elapsed_s", 0) for v in stats.values() if isinstance(v, dict))
    console.print(f"\n[dim]Tempo total: {total_s:.0f}s | "
                  f"Anúncios coletados: {stats.get('scrape', {}).get('count', '?')} | "
                  f"FIPE hits: {stats.get('fipe', {}).get('hits', '?')}[/dim]")

    if state.get("errors"):
        console.print(f"[yellow]⚠ {len(state['errors'])} avisos – veja resultados.json para detalhes[/yellow]")


def main():
    args = parse_args()

    console.print(Panel.fit(
        "[bold]🚗 Car Opportunity Graph Agent[/bold]\n"
        "[dim]LangGraph pipeline: Scrape → FIPE → Score → Report[/dim]\n\n"
        f"Localidades: [yellow]{', '.join(l['name'] for l in LOCATIONS)}[/yellow]\n"
        f"Filtros: {FILTERS['year_min']}–{FILTERS['year_max']} · "
        f"≤R${FILTERS['price_max']:,} · ≤{FILTERS['km_max']:,} km · "
        f"automático · ≥{FILTERS['fipe_discount_min']:.0%} abaixo FIPE".replace(",", "."),
        border_style="purple",
    ))

    if args.demo:
        from demo import run_demo
        run_demo()
        return

    console.print("\n[bold purple]▶ Iniciando graph pipeline...[/bold purple]\n")
    state = run_graph(skip_olx=args.skip_olx, skip_wm=args.skip_webmotors)

    print_summary(state)

    console.print(f"\n[bold]📄 Relatório HTML:[/bold] [cyan]{os.path.abspath(REPORT_HTML)}[/cyan]")
    console.print(f"[bold]📦 Dados JSON:[/bold]   [cyan]{os.path.abspath(REPORT_JSON)}[/cyan]")


if __name__ == "__main__":
    main()
