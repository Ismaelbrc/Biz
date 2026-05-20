#!/usr/bin/env python3
"""
Buscador de Oportunidades de Carros
Busca em OLX e Webmotors na Grande Goiânia e Anápolis.
Filtra por preço, ano, KM, câmbio automático e desconto na FIPE.
"""
import os
import sys
import time
import argparse

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

# Make sure we can import sibling modules when run directly
sys.path.insert(0, os.path.dirname(__file__))

from config import FILTERS, LOCATIONS, REPORT_FILE
from fipe import FipeService
from scraper_olx import OLXScraper
from scraper_webmotors import WebmotorsScraper
from scorer import OpportunityScorer
from reporter import save_json, generate_html
from models import Car

console = Console()


def parse_args():
    ap = argparse.ArgumentParser(description="Busca oportunidades de carros no OLX e Webmotors")
    ap.add_argument("--skip-olx",      action="store_true", help="Pula OLX")
    ap.add_argument("--skip-webmotors",action="store_true", help="Pula Webmotors")
    ap.add_argument("--max-pages",     type=int, default=10, help="Máximo de páginas por localidade")
    ap.add_argument("--no-fipe",       action="store_true", help="Não consulta FIPE (mais rápido)")
    return ap.parse_args()


def main():
    args = parse_args()

    console.print(Panel.fit(
        "[bold cyan]🚗 Buscador de Oportunidades de Carros[/bold cyan]\n"
        f"Localidades: [yellow]{', '.join(l['name'] for l in LOCATIONS)}[/yellow]\n"
        f"Critérios: {FILTERS['year_min']}–{FILTERS['year_max']} · "
        f"Até R${FILTERS['price_max']:,} · Até {FILTERS['km_max']:,} km · "
        f"Automático · ≥{FILTERS['fipe_discount_min']:.0%} abaixo da FIPE",
        title="Configuração", border_style="cyan"
    ))

    all_cars: list[Car] = []

    # ── OLX ──────────────────────────────────────────────────────────
    if not args.skip_olx:
        console.print("\n[bold]📡 Buscando em OLX...[/bold]")
        with Progress(SpinnerColumn(), TextColumn("{task.description}"), console=console) as prog:
            task = prog.add_task("Carregando OLX...", total=None)
            olx_cars = OLXScraper().search_all(LOCATIONS)
            prog.update(task, description=f"OLX: [green]{len(olx_cars)} anúncios[/green]")
        console.print(f"  → {len(olx_cars)} anúncios encontrados no OLX")
        all_cars.extend(olx_cars)

    # ── Webmotors ─────────────────────────────────────────────────────
    if not args.skip_webmotors:
        console.print("\n[bold]📡 Buscando em Webmotors...[/bold]")
        with Progress(SpinnerColumn(), TextColumn("{task.description}"), console=console) as prog:
            task = prog.add_task("Carregando Webmotors...", total=None)
            wm_cars = WebmotorsScraper().search_all(LOCATIONS)
            prog.update(task, description=f"Webmotors: [green]{len(wm_cars)} anúncios[/green]")
        console.print(f"  → {len(wm_cars)} anúncios encontrados no Webmotors")
        all_cars.extend(wm_cars)

    if not all_cars:
        console.print("[red]Nenhum anúncio encontrado. Verifique a conexão com a internet.[/red]")
        return

    console.print(f"\n[bold]Total de anúncios coletados:[/bold] {len(all_cars)}")

    # ── Scoring ───────────────────────────────────────────────────────
    console.print("\n[bold]🔍 Analisando oportunidades vs. FIPE...[/bold]")
    fipe = FipeService()
    scorer = OpportunityScorer(fipe)
    scored = scorer.score_all(all_cars)

    opportunities = sorted(
        [c for c in scored if c.is_opportunity],
        key=lambda c: (c.discount_vs_fipe or 0, c.opportunity_score),
        reverse=True
    )

    # ── Terminal summary ──────────────────────────────────────────────
    console.print(f"\n[bold green]✅ {len(opportunities)} oportunidades encontradas![/bold green]")

    if opportunities:
        _print_table(opportunities[:20])

    # ── Save outputs ──────────────────────────────────────────────────
    save_json(all_cars, opportunities)
    report_path = generate_html(all_cars, opportunities)

    console.print(f"\n[bold]📄 Relatório HTML:[/bold] [cyan]{os.path.abspath(report_path)}[/cyan]")
    console.print(f"[bold]📦 Dados JSON:[/bold]   [cyan]{os.path.abspath('resultados.json')}[/cyan]")
    console.print("\n[dim]Abra o arquivo HTML no navegador para ver o relatório completo.[/dim]")


def _print_table(cars: list[Car]) -> None:
    tbl = Table(title="Top Oportunidades", show_lines=True, style="cyan")
    tbl.add_column("#",         width=3,  justify="right")
    tbl.add_column("Anúncio",   width=34)
    tbl.add_column("Preço",     width=10, justify="right")
    tbl.add_column("FIPE",      width=10, justify="right")
    tbl.add_column("Desconto",  width=9,  justify="right")
    tbl.add_column("Ano",       width=5)
    tbl.add_column("KM",        width=9,  justify="right")
    tbl.add_column("Cidade",    width=18)
    tbl.add_column("Fonte",     width=10)

    for i, c in enumerate(cars, 1):
        discount = f"{c.discount_vs_fipe*100:.0f}%" if c.discount_vs_fipe else "?"
        discount_str = f"[bold red]{discount}[/bold red]" if (c.discount_vs_fipe or 0) >= 0.30 else f"[green]{discount}[/green]"
        fipe_str = f"R${c.fipe_price:,.0f}".replace(",", ".") if c.fipe_price else "–"
        km_str = f"{c.km:,}".replace(",", ".") if c.km else "–"
        price_str = f"R${c.price:,.0f}".replace(",", ".")

        tbl.add_row(
            str(i),
            c.title[:33],
            f"[bold green]{price_str}[/bold green]",
            fipe_str,
            discount_str,
            str(c.year or "–"),
            km_str,
            c.location[:17],
            c.source.upper(),
        )

    console.print(tbl)


if __name__ == "__main__":
    main()
