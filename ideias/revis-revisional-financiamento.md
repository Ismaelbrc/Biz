# Revis — Revisional de Financiamento Automatizado

Você pagou mais do que devia. O banco sabe. Ninguém te contou.

---

## O Problema Central

O brasileiro que financia um carro ou imóvel assina um contrato
de 15-50 páginas sem entender o que está no papel. O banco conta
com isso. E cobra.

```
Contrato de financiamento de veículo — Banco Pan — 2023

Valor financiado:         R$45.000
Prazo:                    60 meses
Parcela mensal:           R$1.187

O que o cliente vê:       "Parcela de R$1.187 por 60 meses"
O que o cliente não vê:
  → Seguro prestamista embutido:   R$127/mês (não solicitado)
  → Tarifa de avaliação do bem:    R$380 (cobrada no ato)
  → IOF calculado com alíquota errada: diferença de R$312
  → Taxa efetiva: 2,89%/mês vs. média BACEN da modalidade: 2,31%/mês

Valor cobrado a mais nos 60 meses:  R$7.840
O cliente nunca soube.
```

Isso não é exceção. É a regra.

O STJ tem centenas de decisões reconhecendo essas práticas como abusivas.
Existem escritórios de advocacia que ganham R$5M/ano só com revisionais.
Mas o processo ainda é caro, demorado e inacessível para quem mais precisa.

**O Revis automatiza o que antes exigia R$2.000 em honorários adiantados
e 18 meses de processo para saber se havia irregularidade.**

---

## O Mercado

```
Financiamento de veículos:
  → 15M+ contratos ativos (BACEN, 2024)
  → Ticket médio de irregularidade estimada: R$4.000-9.000
  → Taxa de irregularidade (seguros + IOF + juros acima da média): ~20%
  → Mercado potencial: 3M casos × R$6.000 médio = R$18B recuperável

Financiamento imobiliário:
  → 8M+ contratos ativos (SFH + SFI)
  → Irregularidades mais comuns: TR vs IPCA (revisional pós-2019),
    seguro habitacional inflado, TAC cobrada indevidamente
  → Ticket médio muito maior: R$20.000-150.000 recuperável
  → Processo mais complexo (vara cível, não JEC)

Empréstimo pessoal / crédito consignado:
  → 60M+ operações ativas
  → Irregularidades: IOF, seguros, juros acima da tabela
  → Ticket menor (R$500-3.000) mas volume enorme

Foco inicial: financiamento de veículos
  → Contratos padronizados (fácil automação)
  → Valores certos para JEC (até ~R$30k = até 40 salários mínimos)
  → Alta irregularidade documentada por STJ/BACEN
  → Mercado massivo com dor clara e resultado mensurável
```

---

## Os Bancos e as Irregularidades

### Quem financia veículos no Brasil

| Banco | Market share | Irregularidade mais comum |
|-------|-------------|--------------------------|
| Santander | 22% | Seguro prestamista obrigatório |
| BV (ex-Votorantim) | 18% | Tarifa de avaliação + IOF |
| Bradesco | 15% | Capitalização indevida |
| Banco Pan | 13% | Pacote de seguros embutidos |
| Itaú | 12% | Juros acima da média BACEN |
| Caixa | 8% | Tarifa de registro |
| Outros | 12% | Variado |

### As 6 irregularidades mais frequentes

**1. Seguro prestamista não solicitado**
O banco embute seguro de vida + desemprego na parcela sem perguntar.
Fundamento: CDC Art. 51, VI + Resolução BACEN 4.656. O consumidor
tem direito de escolher a seguradora — o banco não pode impor.
Valor típico: R$80-200/mês × 48-60 meses = R$3.840-12.000.

**2. IOF calculado com alíquota ou base errada**
IOF de financiamento tem alíquota diária (0,0041%) × prazo + 0,38% fixo.
Bancos frequentemente calculam sobre valor bruto antes de descontar
a entrada, ou usam prazo incorreto.
Valor típico: R$200-800 por contrato.

**3. Taxa de juros acima da média de mercado**
BACEN publica mensalmente a taxa média por modalidade (código 203, 206, etc.).
STJ Súmula 293: se a taxa contratada supera a média sem justificativa,
pode ser reduzida.
Valor típico: diferença de 0,5-1,5%/mês × 48-60 meses = R$3.000-8.000.

**4. Capitalização indevida (anatocismo)**
Juros sobre juros. Proibido no crédito ao consumidor (STJ Súmula 121
+ CDC). Acontece quando o banco usa tabela Price com capitalização
composta em modalidade que deveria usar SAC ou tabela simples.
Valor típico: R$1.500-6.000 dependendo do prazo.

**5. TAC (Taxa de Abertura de Crédito)**
STJ Súmula 566 (2016): TAC é ilegal em contratos firmados após 2008.
Ainda aparece disfarçada como "tarifa de cadastro" ou "tarifa de serviço".
Valor típico: R$200-1.200 cobrado uma vez.

**6. Tarifa de avaliação de bem**
Cobrar para avaliar o próprio bem dado em garantia é abusivo (CDC).
O STJ tem entendimento consolidado contra essa prática em veículos.
Valor típico: R$300-600 por contrato.

---

## O Produto — Fluxo Completo

```
ETAPA 1: DIAGNÓSTICO (gratuito ou R$29)
  ↓
  Usuário envia: contrato (foto/PDF) ou preenche os campos manualmente
    → Banco, modalidade, valor financiado, prazo, taxa informada,
      parcela, seguros incluídos, tarifas cobradas
  ↓
  Motor de análise:
    → OCR extrai dados do PDF/foto
    → Consulta taxa média BACEN para a modalidade + data
    → Calcula IOF correto pela fórmula legal
    → Identifica seguros e tarifas embutidas
    → Recalcula parcela sem as irregularidades
  ↓
  Resultado em minutos:
    "Encontramos 3 irregularidades no seu contrato.
     Valor estimado de recuperação: R$6.840.
     Quer continuar?"

ETAPA 2: VERIFICAÇÃO E ACEITE (sucesso = ativação do success fee)
  ↓
  Usuário confirma dados e assina contrato de honorários
  (success fee de 25% do valor recuperado)
  ↓
  Plataforma gera:
    → Carta extrajudicial ao banco (30 dias para responder)
    → Se banco responder favorável: calcula ajuste, monitora quitação
    → Se banco não responder ou negar: vai para Etapa 3

ETAPA 3A: JEC AUTOMATIZADO (valores até R$30k)
  ↓
  Plataforma gera petição inicial completa:
    → Qualificação das partes
    → Histórico do contrato
    → Fundamentação jurídica (STJ, BACEN, CDC)
    → Pedidos: revisão + devolução em dobro (CDC Art. 42 parágrafo único)
    → Cálculo do valor pedido
  ↓
  Usuário assina (assinatura digital)
  ↓
  Protocolo no JEC via SEEU ou sistema estadual
  (JEC não exige advogado para causas até 20 SM)
  ↓
  Plataforma monitora: audiência, acordo, sentença

ETAPA 3B: AÇÃO REVISIONAL (valores acima de R$30k)
  ↓
  Referral para advogado parceiro especializado em revisional
  Comissão de referral: 15% dos honorários do advogado
  Plataforma envia dossiê completo pré-elaborado ao advogado
  (economiza 6-8h de trabalho do advogado = parceiro feliz)
```

---

## Motor de Análise — Tecnologia

### Extração de contrato

```python
# Exemplo de pipeline de extração

def analisar_contrato(arquivo):
    # 1. OCR do PDF/imagem
    texto_bruto = ocr_engine.extract(arquivo)  # Tesseract + pré-processamento

    # 2. Parsing estruturado via Claude API
    dados = claude.extract_structured({
        "banco": "...",
        "modalidade": "...",  # CDC veículo, CDC moto, imobiliário SFH, etc.
        "valor_financiado": float,
        "valor_entrada": float,
        "prazo_meses": int,
        "taxa_mensal_informada": float,
        "taxa_anual_CET": float,
        "parcela_mensal": float,
        "seguros": [{"tipo": str, "valor_mensal": float}],
        "tarifas": [{"tipo": str, "valor": float}],
        "data_contrato": date,
        "iof_cobrado": float
    })

    return dados
```

### Motor de cálculo de irregularidades

```python
def calcular_irregularidades(dados_contrato):
    irregularidades = []

    # 1. Verificar taxa vs. média BACEN
    taxa_media_bacen = bacen_api.get_taxa_media(
        modalidade=dados_contrato.modalidade,
        data=dados_contrato.data_contrato
    )
    if dados_contrato.taxa_mensal > taxa_media_bacen * 1.15:  # 15% acima = potencial abuso
        diferenca = (dados_contrato.taxa_mensal - taxa_media_bacen)
        valor_cobrado_a_mais = calcular_diferenca_price(
            principal=dados_contrato.valor_financiado,
            taxa_cobrada=dados_contrato.taxa_mensal,
            taxa_justa=taxa_media_bacen,
            n=dados_contrato.prazo_meses
        )
        irregularidades.append({
            "tipo": "JUROS_ACIMA_MEDIA",
            "valor_recuperavel": valor_cobrado_a_mais,
            "fundamentacao": "STJ Súmula 293 + taxa média BACEN modalidade " + dados_contrato.modalidade
        })

    # 2. Verificar IOF
    iof_correto = calcular_iof_legal(
        valor=dados_contrato.valor_financiado - dados_contrato.valor_entrada,
        prazo=dados_contrato.prazo_meses
    )
    if dados_contrato.iof_cobrado > iof_correto * 1.01:  # tolerância de 1%
        irregularidades.append({
            "tipo": "IOF_INCORRETO",
            "valor_recuperavel": dados_contrato.iof_cobrado - iof_correto,
            "fundamentacao": "Decreto 6.306/2007 + alíquota 0,0041%/dia"
        })

    # 3. Verificar seguros
    for seguro in dados_contrato.seguros:
        if not seguro.foi_solicitado_pelo_cliente:
            valor_total = seguro.valor_mensal * dados_contrato.prazo_meses
            irregularidades.append({
                "tipo": "SEGURO_NAO_SOLICITADO",
                "produto": seguro.tipo,
                "valor_recuperavel": valor_total,
                "fundamentacao": "CDC Art. 51 VI + Circular SUSEP 468/2013"
            })

    # 4. Verificar TAC / tarifas indevidas
    for tarifa in dados_contrato.tarifas:
        if tarifa.tipo in ["TAC", "cadastro", "abertura_credito", "avaliacao_bem"]:
            irregularidades.append({
                "tipo": "TARIFA_INDEVIDA",
                "produto": tarifa.tipo,
                "valor_recuperavel": tarifa.valor,
                "fundamentacao": "STJ Súmula 566 + Resolução BACEN 3.919/2010"
            })

    return irregularidades
```

### Gerador de petição

```python
def gerar_peticao_jec(dados_contrato, irregularidades, dados_cliente):
    # Claude API gera petição personalizada com:
    # - dados reais do contrato
    # - fundamentação jurídica específica para cada irregularidade encontrada
    # - jurisprudência do STJ relevante
    # - cálculo detalhado do valor pedido
    # - pedido de devolução em dobro (CDC Art. 42, parágrafo único)

    peticao = claude.generate_document(
        template="peticao_jec_revisional",
        dados={
            "cliente": dados_cliente,
            "banco": dados_contrato.banco,
            "contrato": dados_contrato,
            "irregularidades": irregularidades,
            "valor_total_pedido": sum(i["valor_recuperavel"] for i in irregularidades) * 2,
            # Art. 42: devolução em dobro do cobrado indevidamente
        }
    )

    return peticao
```

---

## Modelo de Receita

### Estrutura de precificação

| Etapa | O que cobra | Valor |
|-------|-------------|-------|
| Diagnóstico | Gratuito (freemium) ou pago | R$0 ou R$29 |
| Carta extrajudicial | Fixo | R$49 |
| Petição JEC | Success fee 25% | Apenas se ganhar |
| Referral ação judicial | Comissão de referral | 15% dos honorários do parceiro |
| Monitoramento de contrato ativo | Assinatura | R$9,90/mês |

### Por que success fee funciona aqui

```
Caso típico de veículo:
  Irregularidades encontradas: R$6.840
  Devolução em dobro (CDC Art. 42): R$13.680 pedido
  Acordo típico (70% do pedido): R$9.576

  Honorário Revis (25%): R$2.394
  Net do cliente: R$7.182

  CAC do cliente: R$0 (diagnóstico gratuito)
  Custo por caso (análise + petição + acompanhamento): R$120-200
  Margem bruta por caso ganho: ~R$2.200

  Taxa de conversão diagnóstico → petição: ~35%
  (só avança quem tem irregularidade real e valor significativo)
  Taxa de êxito nos casos levados ao JEC: ~65%
  (base em dados de escritórios especializados em revisional)
```

### Projeção conservadora

```
Ano 1 (GO + DF, aquisição orgânica):
  Diagnósticos realizados:      2.000/mês
  Casos com irregularidade:     700/mês (35%)
  Petições protocoladas:        420/mês (60% dos com irregularidade)
  Casos ganhos/mês:             273/mês (65% dos peticionados)
  Ticket médio de success fee:  R$2.400
  MRR de success fee:           R$655.000/mês → R$7,8M/ano

  Mais realista (com sazonalidade, inadimplência de acordo):
  → R$3-4M no primeiro ano
```

---

## Distribuição

### Canal 1 — Despachantes e financeiras independentes

O despachante de veículos é o intermediário natural. Ele processou
o financiamento, sabe que o banco embutiu seguros, tem a relação com o cliente.
Muitos despachantes já oferecem serviços paralelos informalmente.

Proposta para o despachante:
- Acesso à plataforma para diagnosticar contratos dos seus clientes
- Comissão de R$300-600 por caso ativado
- "Produto extra" que aumenta a receita sem trabalho adicional

**Meta**: 200 despachantes parceiros em GO + DF = canal semi-automático.

### Canal 2 — Leilões e compradores de veículos usados

Pessoa que compra carro com financiamento herdado (refinanciamento) —
esses contratos têm alta taxa de irregularidade histórica.
Integração com plataformas de leilão (Mega Leilões, Bidfree) e
classificados (OLX, iCarros) como parceria de distribuição.

### Canal 3 — Conteúdo de finanças pessoais

Criadores de conteúdo sobre finanças pessoais no Brasil têm audiência
massiva — Thiago Nigro, Me Poupe, Nathalia Arcuri. O tema "banco cobrou
errado no seu financiamento" tem alto engajamento.

Formato ideal: ferramenta gratuita de diagnóstico que o criador divulga.
"Coloca o teu contrato lá e vê quanto te roubaram." Viralizável.

### Canal 4 — Sindicatos e associações de trabalhadores

Trabalhador com financiamento de veículo para trabalhar (mototaxista,
motorista de app, representante comercial) — público com alta taxa de
financiamento e menor acesso a informação jurídica.

Parceria com sindicatos: plataforma diagnóstica como benefício do sindicato.
Custo de aquisição quase zero, volume garantido.

### Canal 5 — SEO de alta intenção

Buscas com altíssima intenção de compra:
- "meu financiamento tem juros abusivos"
- "como contestar seguro de financiamento"
- "revisional de financiamento funciona"
- "banco cobrou IOF errado no financiamento"

CPC baixo porque é nicho jurídico-financeiro, não massa.
Uma landing page com calculadora gratuita converte bem.

---

## Operação — Como Escala sem Advogado Próprio

### A questão da OAB

JEC não exige advogado para causas até 20 salários mínimos (~R$30k).
A plataforma gera o documento, o usuário assina e protocola.
Isso é "assistência técnica" — não exercício de advocacia.

Para causas acima de R$30k (ações revisionais na vara cível):
a plataforma faz o dossiê, o advogado parceiro revisa e assina.
Plataforma não representa — apresenta.

### Rede de advogados parceiros

Advogados especializados em revisional são abundantes em todas as
capitais brasileiras. Hoje trabalham com honorários de R$1.500-3.000
adiantados + 20-30% do resultado.

Proposta para o advogado parceiro:
- Recebe caso com dossiê completo pré-elaborado (economiza 6h de trabalho)
- Honorário combinado: sem adiantamento + 30% do resultado
- Revis fica com 15% do honorário como comissão de referral
- Advogado fica com 85% × 30% = 25,5% do valor recuperado

Isso é mais rentável que o modelo atual do advogado (que perde tempo
na fase de análise e prospecção), então a rede se forma naturalmente.

---

## Riscos e Mitigações

### Risco 1 — Bancos contestam os cálculos

**Risco:** banco briga na audiência com perito próprio que questiona a metodologia.

**Mitigação:**
- Cálculos baseados exclusivamente em dados públicos do BACEN (incontestáveis)
- Fundamentação jurídica citando súmulas do STJ (não tem como rebater)
- Para casos grandes, advogado parceiro contrata perito contador quando necessário
- A maioria dos bancos prefere acordar a litigar (custo de oportunidade)

### Risco 2 — Regulação da atividade

**Risco:** OAB ou BACEN questionar a plataforma por exercício irregular de advocacia
ou intermediação financeira não regulada.

**Mitigação:**
- Plataforma é "ferramenta tecnológica de análise" — não dá conselho jurídico
- Todo documento tem aviso "gerado por sistema, não constitui conselho jurídico"
- Para ações judiciais, toda a representação passa pelo advogado parceiro credenciado
- Modelo similar ao Sem Parar (não é banco, é intermediário) ou ao iFood (não é restaurante)
- Consulta prévia a OAB estadual antes do lançamento

### Risco 3 — Bancos melhoram a conformidade

**Risco:** com escala, os bancos corrigem os contratos e a taxa de irregularidade cai.

**Mitigação:**
- Há 15M+ contratos ativos com irregularidades históricas — piscina enorme
- Novos contratos continuam com problemas (pressão de margem dos bancos)
- Diversificação para financiamento imobiliário (irregularidades mais complexas,
  menos visadas pelo mercado atual)

### Risco 4 — Concorrência de escritórios de advocacia

**Risco:** escritórios de revisional tradicional copiam o modelo digital.

**Mitigação:**
- Escritórios não constroem produto — têm DNA de serviço
- Vantagem de escala: custo por caso no Revis < R$200, no escritório > R$1.000
- Velocidade de diagnóstico: Revis em 5 minutos, escritório em 5 dias

### Risco 5 — Fraude no success fee (acordo extrajudicial sem comunicar)

**Risco:** usuário faz acordo direto com o banco e não repassa o percentual do Revis.

**Mitigação:**
- Contrato de honorários claro com cláusula de monitoramento
- Para JEC: plataforma acompanha o processo via e-mail da vara
- Para casos de alto valor: retenção no acordo (advogado parceiro gerencia)
- Não é risco diferente do que qualquer escritório enfrenta — é gerenciável

---

## Fundamentos Legais — Resumo

```
STJ Súmula 121:   Juros não podem incidir sobre juros (anatocismo)
STJ Súmula 293:   Taxa de juros acima da média do mercado pode ser reduzida
STJ Súmula 296:   Capitalização de juros anual é válida, mas mensal exige
                  previsão contratual expressa
STJ Súmula 530:   Sem prova da taxa contratada, aplica-se a média do BACEN
STJ Súmula 566:   TAC e TEC não podem ser cobradas em contratos bancários
                  firmados após 2008 sem previsão contratual válida

CDC Art. 42 §ú:   Devolução em dobro do cobrado indevidamente com dolo
CDC Art. 51, VI:  Nulas as cláusulas que impõem seguros sem livre escolha
                  do prestador

BACEN Res. 3.919: Lista taxas permitidas por modalidade bancária
BACEN Res. 4.292: Portabilidade de crédito (base para cálculo correto de CET)

Decreto 6.306/2007: Regulamento do IOF — fórmula de cálculo correta
```

---

## Nome e Posicionamento

### Nome: Revis

**Sonoridade:** Re-vis. Duas sílabas. Fácil de falar, fácil de lembrar.
Funciona como domínio, como @handle, como brand.

**Semântica:** vem de "revisão" — mas sem o peso da palavra inteira.
"Revis" soa como um verbo: "revisa o teu contrato."
Também remete a "revisão veicular" — conexão natural com o segmento de veículos.

**Alternativas analisadas:**

| Nome | Análise |
|------|---------|
| **Revis** ✅ | Curto, semântica correta, registrável |
| Claro | Muito genérico, conflito com Claro Telecom |
| Teto | Criativo (teto de juros), mas pode confundir com imóvel |
| Justo | Forte como posicionamento, fraco como marca |
| Contrato | Genérico demais |
| Contesta | Conflito com Contesto (produto irmão) |
| Retrato | Boa semântica (mostra o retrato real), menos óbvio |

### Tagline

> *"Coloca o contrato. A gente te diz quanto te cobraram a mais."*

Versão mais curta:
> *"O banco cobrou certo? Descubra em 5 minutos."*

### Posicionamento vs. concorrentes

```
Escritório de revisional tradicional:
  → Cobra R$1.500-3.000 adiantado
  → Demora 5-10 dias para análise
  → Você não entende o que está acontecendo

Fazer sozinho:
  → Impossível para 99% das pessoas
  → Exige conhecimento jurídico + financeiro

Revis:
  → Diagnóstico gratuito em 5 minutos
  → Você só paga se ganhar
  → Você entende exatamente o que foi cobrado errado e por quê
```

### Tom de voz

```
Formal     ←——[•]——————————→    Informal
Técnico    ←———[•]—————————→    Acessível
Sério      ←————[•]————————→    Bem-humorado
Distante   ←——————————[•]——→    Próximo
Clássico   ←——————[•]——————→    Moderno
```

**O Revis fala como um amigo que entende de finanças.**
Não é intimidador (como um advogado tradicional).
Não é simplório (como um fintech de consumo).
É o amigo que olhou o teu contrato e te explicou o que estava errado
— com calma, com clareza, sem julgamento.

**Palavras que o Revis usa:**
descobrir, mostrar, calcular, comparar, recuperar, clareza, direito, seu dinheiro

**Palavras que o Revis nunca usa:**
litigância, petição, ação judicial, contestação, tutela
(essas ficam nos documentos — não na comunicação com o cliente)

---

## Arquitetura Técnica

```
ENTRADA
  → Upload de PDF (contrato digitalizado)
  → Foto pelo celular (OCR + pre-processamento)
  → Preenchimento manual (fallback para contratos antigos)

PROCESSAMENTO
  → OCR: Tesseract + pré-processamento de imagem (OpenCV)
  → Extração estruturada: Claude API (claude-opus-4-7 para contratos complexos)
  → Motor de cálculo: Python puro (financialcalc lib + custom IOF engine)
  → Base de dados BACEN: atualização mensal via API pública do BACEN
    (endpoint /odata4/NotaCredito12Meses)

GERAÇÃO DE DOCUMENTOS
  → Carta extrajudicial: template + Claude API (personalização)
  → Petição JEC: template jurídico validado por advogado parceiro
    + preenchimento automático de dados
  → Output: PDF com assinatura digital (DocuSign ou ZapSign)

PROTOCOLOS
  → JEC GO: sistema eProc TJ-GO (Playwright para protocolo automático)
  → JEC DF: sistema PJe TJDFT
  → Carta extrajudicial: e-mail com AR digital + WhatsApp

MONITORAMENTO
  → Scraping de andamento processual (TJ-GO + TJDFT)
  → Alertas WhatsApp: audiência marcada, acordo proposto, sentença
  → Dashboard do usuário: status em tempo real de cada etapa

STACK
  → Backend: Python (FastAPI) + PostgreSQL
  → Frontend: React (web) + React Native (mobile futuro)
  → IA: Claude API (Anthropic SDK com prompt caching)
  → Documentos: LaTeX → PDF server-side
  → Notificações: WhatsApp Business API (Twilio)
  → Pagamentos: Asaas (success fee via split automático)
  → Assinatura digital: ZapSign (BR, mais barato que DocuSign)
```

---

## Roadmap de Lançamento

### Mês 1 — Validação manual
```
→ Analisar 50 contratos manualmente (processo manual completo)
→ Verificar: taxa de irregularidade real, tipos mais comuns em GO+DF
→ Protocoloar 10 petições de JEC com advogado parceiro
→ Documentar: taxa de êxito, tempo médio, valores recuperados
→ Meta: 3 casos ganhos antes de construir o produto
```

### Mês 2 — MVP calculadora
```
→ Landing page com calculadora de diagnóstico manual
  (usuário preenche campos, sistema calcula irregularidades)
→ Sem OCR ainda — campo a campo
→ Resultado mostra: irregularidades detectadas + estimativa de recuperação
→ CTA: "Quer continuar? Fale com a gente pelo WhatsApp"
→ Distribuição: 5 despachantes parceiros em Goiânia
→ Meta: 100 diagnósticos, 30 casos ativados
```

### Mês 3 — Automação de OCR e petição
```
→ OCR de contratos (PDF + foto)
→ Extração automática via Claude API
→ Gerador de carta extrajudicial automático
→ Gerador de petição JEC (validado por advogado)
→ Protocolo semi-automático (assistido, não ainda full-auto)
→ Meta: 300 diagnósticos/mês, 100 casos ativados
```

### Mês 4-6 — Escala
```
→ Protocolo automático no eProc TJ-GO
→ Monitoramento automático de andamento
→ Dashboard de acompanhamento para o usuário
→ Expansão para TJDFT
→ Rede de 50+ advogados parceiros para casos acima de R$30k
→ Meta: 1.000 diagnósticos/mês, 300 casos ativados
```

---

## Conexão com o Portfólio Bismarck

```
Cliente chega pelo Revis (financiamento de veículo)
  ↓
Aravo: "Você também tem dívida em aberto?
  Posso limpar o seu nome."
  ↓
Amparo: "Sua contribuição ao INSS está certa?
  (motoristas de app têm regras específicas)"
  ↓
Contesto: "Você tem multas de trânsito?
  Podemos contestar."
  ↓
Legado: "Tem imóvel ou veículo no seu nome?
  Garanta que vai para quem você quer."

O cliente do Revis (tomador de crédito, inadimplente potencial,
trabalhador com renda variável) tem sobreposição alta com
o público dos outros produtos Bismarck.

LTV combinado: R$4.500-12.000 por cliente ao longo do portfólio.
```

---

## Resumo Executivo

**O produto:** plataforma que analisa contratos de financiamento de veículo,
identifica irregularidades (seguros indevidos, IOF errado, juros acima da média,
taxas ilegais) e recupera o valor cobrado a mais via carta extrajudicial ou JEC.

**O cliente:** qualquer brasileiro com financiamento de veículo ativo ou encerrado
nos últimos 5 anos (prescricional). Foco inicial: GO + DF.

**O modelo:** diagnóstico gratuito → success fee de 25% sobre o valor recuperado.
O cliente não paga nada antecipado. Só paga se ganhar.

**Por que funciona:**
- Irregularidades documentadas e reais (não é especulação jurídica)
- Fundamento legal consolidado no STJ (sem risco jurídico de perda total)
- JEC não exige advogado (escala sem custo fixo de OAB)
- Success fee alinha incentivos (plataforma só ganha se recuperar)
- Diagnóstico gratuito = funil de alta conversão

**Por que agora:**
- 15M+ contratos ativos com irregularidades históricas
- Bancos não corrigiram a prática (seguro prestamista ainda é sistemático)
- JEC digital (eProc) tornou o protocolo remoto possível
- Claude API tornou a extração de contratos em escala viável

**Nome:** Revis
**Tagline:** "Coloca o contrato. A gente te diz quanto te cobraram a mais."
