# Cota — Cotação de Suprimentos via WhatsApp com IA

O comprador fala o que precisa. A IA define o escopo, consulta
os fornecedores e devolve o mapa de cotação. Tudo pelo WhatsApp.

---

## O Problema

Todo negócio compra suprimentos. E toda compra começa da mesma forma:

```
Gerente da clínica manda mensagem no WhatsApp para 5 distribuidoras:
  "Oi, tudo bem? Preciso de luva descartável M, avental e máscara.
   Pode me passar o preço?"

Distribuidora 1: responde em 4h com tabela em PDF ilegível
Distribuidora 2: "pode mandar a lista completa?" (não leu a mensagem)
Distribuidora 3: responde só da luva, esquece os outros itens
Distribuidora 4: não responde
Distribuidora 5: liga às 18h quando o gerente já foi embora

Gerente compila tudo em uma planilha às 19h para comparar.
Descobre que comparou luvas de marcas diferentes.
Começa de novo.

Tempo total: 4-6 horas de trabalho de uma pessoa.
Frequência: 2-4 vezes por mês.
```

Isso acontece em clínicas, construtoras, restaurantes, escolas,
escritórios, indústrias, comércios. Em toda empresa que compra
suprimentos sem um setor de compras estruturado — ou seja, em
99% das PMEs brasileiras.

**O Cota elimina as 6 horas. O comprador fala, o sistema cota,
o mapa chega no WhatsApp.**

---

## O Mercado

```
PMEs no Brasil: 20M+ empresas (SEBRAE)
Com necessidade de cotação recorrente: ~5M
Frequência média: 3 cotações por mês
Tempo gasto por cotação: 4-6 horas
Valor do tempo perdido (custo de oportunidade): enorme

Setores com maior volume de cotação e dor mais aguda:

CONSTRUÇÃO CIVIL:
  → 400.000+ empresas de construção ativas (CBIC)
  → Empreiteiras, construtoras, reformadoras
  → Cotam: cimento, ferro, madeira, tinta, elétrico, hidráulico,
    cerâmica, argamassa — dezenas de itens por compra
  → Ticket médio por cotação: R$5.000-50.000
  → Frequência: semanal ou quinzenal
  → Alta dor: erro na cotação = obra parada

SAÚDE:
  → 150.000+ clínicas, consultórios, laboratórios, farmácias
  → Cotam: EPI, material cirúrgico, medicamentos, limpeza hospitalar
  → Alta padronização de produto (código ANVISA = especificação única)
  → Ticket médio: R$2.000-15.000
  → Frequência: quinzenal ou mensal

ALIMENTAÇÃO:
  → 1M+ restaurantes, lanchonetes, panificadoras, buffets
  → Cotam: insumos, embalagens, descartáveis, limpeza
  → Alta frequência (semanal)
  → Ticket médio: R$500-5.000

ESCRITÓRIO / SERVIÇOS:
  → Papelaria, cartuchos, limpeza, informática
  → Menor ticket mas altíssimo volume e recorrência
  → Cliente mais fácil de digitalizar

FOCO INICIAL: construção civil e saúde em GO + DF
  → Alta dor → alto valor percebido → disposição a pagar maior
  → Fornecedores locais mapeáveis em 30 dias
  → Ticket alto = modelo de comissão viável além da assinatura
```

---

## O Fluxo Completo

### Do lado do comprador

```
PASSO 1 — Pedido pelo WhatsApp (linguagem natural)

  Comprador:
  "Preciso cotar para obra de reforma:
   - 50 sacos de cimento CP II 50kg
   - 20 barras de ferro 3/8" 12m
   - 10 latas de tinta Suvinil branca 18L
   Entrega em Goiânia Setor Bueno. Preciso até sexta."

PASSO 2 — IA extrai e confirma o escopo

  Cota:
  "Entendi! Confirmando o pedido:

   ✅ Cimento CP II 50kg — 50 sacos
   ✅ Ferro CA-50 3/8" (9,5mm) 12m — 20 barras
   ✅ Tinta Suvinil Premium Fosco Branco Neve 18L — 10 latas

   Entrega: Setor Bueno, Goiânia-GO
   Prazo necessário: até sexta-feira (09/05)

   Precisa de nota fiscal? (sim/não)
   Forma de pagamento preferida? (à vista / 30 dias / 60 dias)"

  Comprador: "sim nota fiscal, prefiro 30 dias mas aceito à vista"

PASSO 3 — Sistema consulta 3-5 fornecedores

  [transparência para o comprador]
  Cota: "Certo! Consultando fornecedores agora.
   Você recebe o mapa de cotação em até 4 horas."

PASSO 4 — Mapa de cotação devolvido pelo WhatsApp

  Cota envia:
  → Mensagem resumo no WhatsApp
  → PDF completo com o mapa detalhado

  [mensagem resumo]
  "Mapa de cotação pronto! 🗺️

   Melhor preço total: Distribuidora MixConstrução — R$3.847
   Entrega mais rápida: Casa do Construtor — amanhã, R$4.120

   Veja o mapa completo em PDF ↓"

  [PDF enviado no WhatsApp]
```

---

## O Mapa de Cotação — O Produto Entregue

```
┌─────────────────────────────────────────────────────────────────┐
│ MAPA DE COTAÇÃO                          DATA: 07/05/2026       │
│ Empresa: Reformas Silva Ltda             Prazo: até 09/05       │
│ Entrega: Setor Bueno, Goiânia-GO         NF: Sim | Pgto: 30d   │
├─────────────────────────────────────────────────────────────────┤
│ ITEM 1 — Cimento CP II 50kg (50 sacos)                         │
│                                                                 │
│  Fornecedor          │ Preço/saco │ Total    │ Prazo │ Pgto     │
│  ──────────────────────────────────────────────────────────    │
│  MixConstrução       │  R$38,50   │ R$1.925  │ 2d    │ 30d ✅  │
│  Casa do Construtor  │  R$41,00   │ R$2.050  │ 1d    │ À vista  │
│  Construfort GO      │  R$37,90   │ R$1.895  │ 4d    │ 30d ✅  │
│  Leroy Merlin        │  R$40,50   │ R$2.025  │ 3d    │ 30d ✅  │
│                                                                 │
│  ★ Melhor preço: Construfort GO (R$1.895) — mas entrega em 4d  │
│  ★ Dentro do prazo: MixConstrução (R$1.925, 2d, 30d)          │
├─────────────────────────────────────────────────────────────────┤
│ ITEM 2 — Ferro CA-50 3/8" 12m (20 barras)                      │
│                                                                 │
│  Fornecedor          │ Preço/barra│ Total    │ Prazo │ Pgto     │
│  ──────────────────────────────────────────────────────────    │
│  MixConstrução       │  R$47,00   │  R$940   │ 2d    │ 30d ✅  │
│  Ferrodist Goiânia   │  R$43,50   │  R$870   │ 3d    │ À vista  │
│  Construfort GO      │  R$45,00   │  R$900   │ 4d    │ 30d ✅  │
│                                                                 │
│  ★ Melhor preço: Ferrodist (R$870) — sem 30d, entrega em 3d   │
│  ★ Melhor combo (preço + prazo + pagamento): MixConstrução     │
├─────────────────────────────────────────────────────────────────┤
│ ITEM 3 — Tinta Suvinil Branco Neve 18L (10 latas)              │
│                                                                 │
│  Fornecedor          │ Preço/lata │ Total    │ Prazo │ Pgto     │
│  ──────────────────────────────────────────────────────────    │
│  Tintas Goiânia      │  R$98,00   │  R$980   │ 1d    │ 30d ✅  │
│  MixConstrução       │  R$103,00  │ R$1.030  │ 2d    │ 30d ✅  │
│  Leroy Merlin        │  R$109,90  │ R$1.099  │ 3d    │ 30d ✅  │
│                                                                 │
│  ★ Melhor preço: Tintas Goiânia (R$980, entrega amanhã, 30d)  │
├─────────────────────────────────────────────────────────────────┤
│ RESUMO — MELHOR COMBINAÇÃO                                      │
│                                                                 │
│  Opção A — Um fornecedor só (simplicidade):                     │
│    MixConstrução: R$3.895 total | Entrega 2d | 30d             │
│                                                                 │
│  Opção B — Menor preço global (dividir pedido):                │
│    Construfort GO (cimento): R$1.895                            │
│    Ferrodist (ferro): R$870                                     │
│    Tintas Goiânia (tinta): R$980                               │
│    Total: R$3.745 — economia de R$150 vs. opção A              │
│    Desvantagem: 3 notas fiscais, 3 entregas                     │
│                                                                 │
│  RECOMENDAÇÃO DO COTA:                                          │
│  Para sua obra com prazo apertado (sexta), Opção A é a         │
│  melhor escolha: um fornecedor, um frete, uma NF.              │
│  Diferença de preço não justifica a complexidade operacional.  │
└─────────────────────────────────────────────────────────────────┘

[botões no WhatsApp]
[✅ Aprovar compra com MixConstrução]  [✏️ Ajustar]  [📞 Falar com fornecedor]
```

---

## Como o Sistema Cota os Fornecedores

### Fase 1 — Rede manual curada (MVP)

```
Antes de qualquer automação: banco de dados de fornecedores
por categoria + região, com contatos reais (WhatsApp ou e-mail).

Para cada cotação:
  → IA gera RFQ padronizado por fornecedor
  → Sistema dispara via WhatsApp Business API automaticamente
  → Fornecedor responde no próprio WhatsApp (texto, tabela, PDF)
  → IA processa a resposta e extrai: preço, prazo, condição, disponibilidade
  → Se resposta ambígua: follow-up automático ("confirme o prazo de entrega")
  → Após 2h sem resposta: lembrete automático
  → Após 4h: descarta e usa os que responderam

Equipe operacional no MVP:
  → 1-2 "cotadores" que monitoram respostas difíceis de parsear
  → Papel principal é qualidade control, não trabalho manual
  → Objetivo: automatizar 80%, humans fazem os 20% edge cases
```

### Fase 2 — Portal do fornecedor

```
Fornecedor cadastrado acessa portal web simples:

  → Recebe notificação: "Nova cotação disponível para você"
  → Vê o RFQ estruturado: itens, quantidades, prazo, local de entrega
  → Preenche: preço unitário, prazo de entrega, condições de pagamento
  → Submete em 3 minutos

Vantagem para o fornecedor:
  → Recebe leads qualificados (comprador com pedido real, não curioso)
  → Não precisa mais responder WhatsApp descoordenado
  → Histórico de cotações e win rate (quantas ganhou)

Receita do fornecedor:
  → Primeiros 3 meses grátis
  → Depois: R$99/mês para receber RFQs ilimitados
  → Ou: R$5 por cotação recebida (pay-per-lead)
```

### Fase 3 — Scraping de preços públicos

```
Para produtos com preços online:
  → Leroy Merlin, C&C, Telhanorte: scraping automático de preço
  → Kalunga, Staples: escritório
  → Mercado Livre B2B: marketplace geral
  → Distribuidoras com catálogo online

Esses preços entram automaticamente no mapa sem precisar de RFQ.
Fornecedores tradicionais (sem preço online) entram via Fase 1/2.
```

---

## Arquitetura Técnica

```
ENTRADA
  → WhatsApp Business API (número dedicado por cliente ou número central)
  → Webhook recebe mensagem do comprador

PROCESSAMENTO DA SOLICITAÇÃO (Claude API)
  → Extração de entidades: itens, quantidades, especificações, prazo, local
  → Geração de perguntas de clarificação (se necessário)
  → Padronização: normaliza unidades, converte especificações técnicas
    ("ferro 3/8" → CA-50 9,5mm, "cimento comum" → CP II ou CP III?)
  → Matching de fornecedores: categoria × região × histórico de resposta

DISPARO DE RFQ
  → WhatsApp Business API → fornecedores cadastrados
  → Email (fallback para fornecedores sem WhatsApp ativo)
  → Portal web (para fornecedores na Fase 2)

COLETA E PARSING DE RESPOSTAS
  → Webhook recebe respostas dos fornecedores
  → Claude API parseia resposta em linguagem natural:
    "temos cimento por 38,50 o saco, entrego em 2 dias, 30 dias"
    → { item: "cimento CP II 50kg", preco_unit: 38.50, prazo_dias: 2, condicao: "30d" }
  → Se resposta em PDF/tabela: Claude Vision extrai os dados
  → Follow-up automático para respostas incompletas

GERAÇÃO DO MAPA
  → Motor de comparação: ordena por preço, prazo, condição
  → Algoritmo de recomendação:
    → Regra 1: dentro do prazo solicitado
    → Regra 2: aceita a condição de pagamento solicitada
    → Regra 3: menor preço entre os que satisfazem 1 e 2
    → Insight: diferença percentual entre melhor e pior
  → Geração do PDF: LaTeX ou Puppeteer + HTML template
  → Envio: PDF no WhatsApp + resumo em texto

STACK
  → Backend: Node.js + PostgreSQL
  → IA: Claude API (claude-opus-4-7 para extração e parsing)
  → WhatsApp: Z-API ou Twilio WhatsApp Business
  → PDF: Puppeteer (Node.js serverside)
  → Scraping: Playwright (para preços públicos)
  → Fila: BullMQ (para processar cotações assíncronamente)
  → Infra: Railway ou Render (simple, sem overhead de AWS no MVP)
```

---

## Modelo de Receita

### Para o comprador (B2B)

| Plano | Preço | Para quem |
|-------|-------|-----------|
| **Starter** | R$199/mês | Até 10 cotações/mês, até 5 itens por cotação |
| **Pro** | R$399/mês | Até 30 cotações/mês, itens ilimitados, histórico completo |
| **Enterprise** | R$899/mês | Ilimitado, múltiplos usuários, API, integração com ERP |
| **Pay-per-use** | R$29/cotação | Para quem usa esporadicamente |

### Para o fornecedor (B2B)

| Modelo | Preço | Proposta |
|--------|-------|---------|
| **Freemium** | R$0 | Até 5 RFQs/mês (para entrar na rede) |
| **Standard** | R$99/mês | RFQs ilimitados, painel de win rate |
| **Premium** | R$199/mês | Destaque na listagem + analytics avançado |
| **Pay-per-lead** | R$5-15/RFQ | Para fornecedores que preferem não assinar |

### Unit economics por cliente comprador

```
CAC (B2B outbound + conteúdo): R$300-600
ARPU médio: R$299/mês
Churn estimado: 4%/mês
LTV: R$299 × (1/0,04) = R$7.475

Payback: 1-2 meses
Margem bruta: ~70% (custo de IA + infraestrutura + cotador é baixo)
```

### Projeção

```
Ano 1 (GO + DF, construção + saúde):
  Compradores ativos: 200 empresas × R$299 médio = R$59.800/mês
  Fornecedores pagantes: 150 × R$99 = R$14.850/mês
  Total MRR Ano 1: ~R$75.000/mês → R$900.000/ano

Ano 2 (expansão setorial + nacional):
  Compradores: 800 × R$350 médio = R$280.000/mês
  Fornecedores: 500 × R$120 = R$60.000/mês
  Total MRR Ano 2: ~R$340.000/mês → R$4M/ano
```

---

## Distribuição

### Para compradores

**Canal 1 — Associações comerciais e setoriais**
AECB (Associação das Empresas de Construção de Brasília),
Sinduscon-GO, CRF-GO (farmácias/clínicas) têm base de associados
com necessidade idêntica. Parceria = acesso direto.

**Canal 2 — Contadores e consultores**
O contador da PME sabe quem tem problema de controle de compras.
Indicação com comissão de R$100 por cliente ativado.

**Canal 3 — Conteúdo de gestão para PME**
"Como fazer cotação sem perder horas" — tema com busca ativa.
Calculadora: "quanto você perde por mês em tempo de cotação?"
(usuário informa: quantas cotações por mês × quantas horas cada uma)
Resultado: "Você gasta R$X/mês em tempo de cotação. O Cota custa R$199."

**Canal 4 — WhatsApp grupos de empresários**
Grupos de CDL (Câmara de Dirigentes Lojistas), grupos de empresários
setoriais. Produto que resolve dor real se espalha naturalmente.

### Para fornecedores

**Canal 1 — Abordagem direta**
Distribuidoras e atacadistas de GO + DF visitados pessoalmente.
Proposta: "você vai receber pedidos qualificados direto no WhatsApp,
sem precisar prospectar." CAC zero para o fornecedor.

**Canal 2 — Sindicatos de distribuidores**
SINDIMETAL-GO, Sindifar-GO (distribuidoras farmacêuticas),
ACED-GO (distribuidoras em geral) têm base organizada.

---

## Diferenciação vs. Alternativas

```
ALTERNATIVAS ATUAIS:

1. Fazer na mão (WhatsApp + planilha):
   → 4-6 horas por cotação
   → Informação despadronizada, comparação difícil
   → Custo: caro em tempo de pessoa qualificada

2. Mercado Eletrônico / Ariba (SAP):
   → Para grandes empresas, não PMEs
   → Implantação leva meses, custa R$10.000+
   → Fornecedor precisa ser cadastrado no sistema

3. Cotações.com e similares:
   → Portal web (não WhatsApp)
   → Sem IA — o comprador ainda faz o trabalho de especificar
   → Sem parsing de respostas — sem mapa automático

4. Marketplaces B2B (Mercado Livre, Amazon Business):
   → Só para produtos disponíveis no estoque do marketplace
   → Não funciona para serviços, produtos customizados, materiais de obra

POSICIONAMENTO DO COTA:
  → WhatsApp-first: onde o comprador já está
  → IA que entende linguagem natural: não precisa saber o código do produto
  → Mapa de cotação pronto: não precisa compilar a resposta dos fornecedores
  → Para PMEs: sem implantação, sem treinamento, sem contrato anual
```

---

## Expansão Natural do Produto

```
V1: Cotação de produtos (o que está descrito aqui)

V2: Cotação de serviços
  → "Preciso de 3 orçamentos para reforma do banheiro da clínica"
  → Mesma lógica, mas fornecedores são prestadores de serviço
  → Mais complexo (escopo mais subjetivo) — mas enorme mercado

V3: Histórico e inteligência de compra
  → "Você pagou R$38,50 no cimento em março. Em maio o fornecedor
     está cobrando R$43,00. Aumento de 14,9%. Média do mercado: +8%."
  → Dashboard de tendência de preço por insumo
  → "Melhor época para comprar cimento em Goiânia: outubro-novembro (menor demanda)"

V4: Pedido automático
  → Comprador aprova o fornecedor pelo WhatsApp
  → Sistema gera e envia o pedido de compra automaticamente
  → Fornecedor confirma no portal
  → Integração com nota fiscal (para fornecedores com NF eletrônica)

V5: Gestão de fornecedores
  → Score de fornecedor: pontualidade, aderência ao preço cotado, qualidade
  → "Esse fornecedor entregou atrasado 3 vezes. Recomendamos não usar."
  → Base de dados de avaliação colaborativa (rede de compradores)
```

---

## Roadmap

### Mês 1 — Validação manual
```
→ Processo 100% manual com IA de apoio
→ Comprador manda pedido no WhatsApp → analista humano extrai escopo
  (com ajuda do Claude) → liga/WhatsApp para fornecedores → monta mapa em Google Sheets
  → envia PDF pro comprador
→ Meta: 20 cotações realizadas
→ Cobrar: R$29/cotação (validar disposição a pagar)
→ Aprender: quais setores têm resposta mais rápida dos fornecedores
```

### Mês 2 — Automação da extração e do RFQ
```
→ WhatsApp Business API conectado
→ Claude API extrai o escopo automaticamente
→ Sistema dispara RFQ para fornecedores via WhatsApp
→ Analista ainda monitora e faz parsing manual das respostas
→ Sistema monta o mapa automaticamente (só preenche os dados)
→ Meta: 60 cotações/mês com 1 analista
```

### Mês 3 — Parsing automático de respostas
```
→ Claude API parseia respostas dos fornecedores (texto + PDF)
→ Follow-up automático para respostas incompletas
→ Analista só trata edge cases (10-20% dos casos)
→ Plano de assinatura mensal lançado (R$199/mês)
→ Meta: 30 clientes pagantes
```

### Mês 4-6 — Portal do fornecedor + escala
```
→ Fornecedores respondem via portal web (mais padronizado)
→ Scraping de preços públicos (Leroy, Kalunga, etc.)
→ Expansão para Brasília
→ Meta: 100 clientes compradores + 200 fornecedores na rede
```

---

## Nome e Posicionamento

### Nome: Cota

**Sonoridade:** Co-ta. 2 sílabas. O verbo exato do que o produto faz.
"Vai lá no Cota" — natural em português.
"Cota isso pra mim" — funciona como verbo de comando.

**Disponibilidade:** verificar cota.com.br / cota.app

**Alternativas:**

| Nome | Análise |
|------|---------|
| **Cota** ✅ | O verbo do produto, curto, claro |
| Cotei | Passado: "já cotei pra você" — bom mas menos marca |
| Mapa | Referência ao output — criativo mas pouco acionável |
| Supri | De suprimentos — claro mas soa como apoio/assistência |
| RFQ | Muito técnico para PME brasileira |
| Pediu | Passado, implica conclusão — interessante como alternativa |

### Tagline

> *"Fala o que precisa. A gente cota."*

Ou para o comprador direto:
> *"De 4 horas de cotação para 4 minutos no WhatsApp."*

### Posicionamento por segmento

```
Para o dono da construtora:
  "Você pede a lista de material. Em 4 horas você recebe
   3 orçamentos comparados, com a recomendação do melhor.
   Sem ligar para ninguém."

Para o gerente da clínica:
  "Seu suprimento médico cotado automaticamente todo mês.
   Você aprova pelo WhatsApp."

Para o gestor de compras da PME:
  "O que você gasta o dia fazendo, o Cota faz em 4 horas.
   Sem planilha. Sem ligação."
```

---

## Conexão com o Portfólio

```
Cota é o único produto B2B puro do portfólio — e pode ser
o ponto de entrada para outros produtos nas PMEs clientes:

Construtora usa o Cota para comprar material
  ↓
Assina: "Você tem imóvel alugado para os funcionários?
  Faça o contrato e vistoria digital."
  ↓
Campo Certo: "Você tem empresa rural ou fornece para o agro?
  Regularize sua situação fiscal."
  ↓
Revis: "Você tem financiamento de equipamento ou veículo?
  Verifique se os juros estão corretos."

O Cota também é o produto mais fácil de vender para
empresas que já são clientes de outros produtos do portfólio:
"Você já usa o Assina para seus imóveis. Quer automatizar
as cotações de suprimento da sua empresa também?"
```

---

## Resumo Executivo

**O produto:** agente de IA para cotação de suprimentos B2B via WhatsApp.
Comprador fala o que precisa, sistema extrai escopo, consulta 3-5
fornecedores e devolve mapa de cotação comparativo em até 4 horas.

**O cliente:** PMEs com 5-200 funcionários que compram suprimentos
regularmente mas não têm setor de compras estruturado. Foco inicial:
construtoras e clínicas em GO + DF.

**O diferencial:** WhatsApp-first (onde o comprador já está), IA que
entende linguagem natural (sem necessidade de código de produto ou
formulário), mapa de cotação gerado automaticamente (sem compilação manual).

**O modelo:** assinatura R$199-399/mês para comprador + R$99/mês para
fornecedor. LTV ~R$7.500 por comprador.

**Por que agora:** Claude API tornou o parsing de linguagem natural e
de documentos (PDF, tabelas de preço) economicamente viável.
WhatsApp Business API está disponível para empresas de qualquer porte.
O problema existe há décadas — a tecnologia para resolvê-lo existe desde 2023.

**Nome:** Cota
**Tagline:** "Fala o que precisa. A gente cota."
