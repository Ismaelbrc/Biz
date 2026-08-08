# Biz

Business ideas

## Graph agent — captação de leads (donos de imóvel para alugar)

**Desafio 1**: encontrar pessoas físicas donas de imóvel que estão anunciando
o imóvel para **alugar por conta própria** (sem passar por imobiliária) —
esse é o público-alvo para vender um sistema de administração de aluguel.

Agente construído com [LangGraph](https://github.com/langchain-ai/langgraph),
que roda em 4 etapas encadeadas (nós do grafo):

```
buscar_anuncios → enriquecer_anuncios → qualificar_leads → exportar_leads
```

1. **buscar_anuncios**: pesquisa anúncios de aluguel no OLX (Playwright,
   navegador headless) para a cidade informada.
2. **enriquecer_anuncios**: abre cada anúncio e identifica se quem publicou
   é o próprio proprietário (`particular`) ou uma imobiliária/corretor.
3. **qualificar_leads**: aplica as regras do ICP — descarta imobiliárias,
   descarta anúncios de venda, e pontua (`score` 0–100) os anúncios que
   sobram, priorizando quem já sinaliza "direto com o proprietário",
   "sem imobiliária" etc. Anúncios ambíguos podem ser reclassificados por
   Claude se `ANTHROPIC_API_KEY` estiver configurada.
4. **exportar_leads**: grava os leads qualificados em `data/leads_*.csv`.

### Rodando

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium   # baixa o navegador headless, se necessário
cp .env.example .env          # opcional: ANTHROPIC_API_KEY para qualificação por IA

# teste rápido sem acessar a internet (dados de exemplo):
python main.py --mock -v

# rodada real:
python main.py --cidade "São Paulo" --uf sp --max-anuncios 40 -v
```

O resultado (leads qualificados) é impresso no terminal e salvo em
`data/leads_<timestamp>.csv` com colunas: `titulo, url, preco, localizacao,
tipo_anunciante, score, motivo`.

### Estrutura

```
leadgen/
  config.py        # critérios do ICP (palavras-chave de particular vs imobiliária)
  state.py          # estado compartilhado do grafo (LangGraph)
  graph.py           # definição dos nós e do grafo
  qualify.py         # regras de qualificação + fallback via Claude
  export.py           # exportação para CSV/JSON
  sources/
    olx.py            # scraper real (Playwright)
    mock.py           # fonte de dados falsa, para testes sem rede
main.py               # CLI
```

### Recalibrando o scraper

O OLX muda o HTML periodicamente. Os seletores usados ficam centralizados em
`leadgen/sources/olx.py::SELECTORS`. Se o scraper parar de encontrar
anúncios, rode `playwright codegen https://www.olx.com.br/imoveis/aluguel`
para inspecionar o layout atual e atualizar os seletores.

### Próximos passos sugeridos

- Adicionar outras fontes (grupos de bairro no Facebook, Zap Imóveis,
  QuintoAndar) implementando a mesma interface `search()`/`enrich_all()`.
- Extrair WhatsApp/telefone do anúncio para automatizar o primeiro contato.
- Exportar direto para um CRM/Airtable em vez de apenas CSV.
