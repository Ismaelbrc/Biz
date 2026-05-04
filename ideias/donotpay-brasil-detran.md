# DoNotPay Brasil — DETRAN GO + DF

Produto de contestação automática de multas de trânsito.
Foco inicial: Goiás e Distrito Federal como mercado-piloto.

---

## Por Que Começar por GO + DF

| Critério | GO | DF |
|----------|----|----|
| Frota de veículos | ~3.5M | ~1.8M |
| Perfil de renda | Médio-alto em Goiânia | Alto em Brasília |
| Densidade de radar | Alta (BR-060, BR-153, BR-414) | Alta (EPTG, Eixão, BR-040) |
| Digitalização do DETRAN | Média | Alta |
| Distância entre capitais | 209km — mesma equipe serve os dois |
| Perfil B2B | Transportadoras + agronegócio GO | Frotas governamentais + empresariais DF |

**Insight estratégico:** DF tem o maior número de veículos per capita do Brasil
e uma população com alta propensão a pagar por conveniência. GO tem volume de
rodovias federais com radares de velocidade média — as multas de maior valor.
Juntos, são um mercado de ~5M veículos com características complementares.

---

## O Sistema de Contestação de Multas no Brasil

Todo motorista tem **dois momentos** para contestar — cada um com prazo fatal:

```
INFRAÇÃO COMETIDA
      ↓
NOTIFICAÇÃO DE AUTUAÇÃO (NIA)
  → Prazo: 15 dias úteis para indicar condutor real (se não era você)
  → Prazo: 15 dias úteis para DEFESA PRÉVIA (antes de virar penalidade)
      ↓ (se defesa prévia negada ou não interposta)
NOTIFICAÇÃO DE PENALIDADE (NIP)
  → Prazo: 30 dias corridos para recurso na JARI
      ↓ (se JARI nega)
CETRAN (recurso estadual) ou CONTRAN (infração federal)
  → Prazo: 30 dias corridos
      ↓ (se negado)
JUDICIAL (JEC ou vara especializada)
```

**O maior erro dos motoristas:** deixar passar o prazo da defesa prévia
achando que só pode recorrer depois. A defesa prévia tem taxa de sucesso
maior e impede a pontuação na CNH antes da decisão.

### Fundamentos mais comuns e taxa estimada de sucesso

| Fundamento | Aplicação | Sucesso estimado |
|-----------|-----------|-----------------|
| Equipamento sem certificado INMETRO válido | Radar, lombada eletrônica | 60-75% |
| Prazo de notificação extrapolado | Carta chegou após 30 dias da infração | 70-85% |
| Sinalização irregular ou ausente | Falta de placa de velocidade antes do radar | 50-65% |
| Erro de identificação de placa/veículo | OCR errado da câmera | 80-90% |
| Obras na via com velocidade reduzida sem sinalização | BR-060, obras constantes em GO | 40-55% |
| Condutor diferente + indicação formal | Veículo empresarial | 75-85% |
| Caso fortuito documentado | Fuga de situação de risco) | 30-45% |
| Radar em local proibido (CONTRAN 396) | Dentro de 1km de sinal de velocidade | 55-70% |

---

## DETRAN Goiás — Especificidades

**Órgãos autuadores em GO:**
- DETRAN GO — vias urbanas e estaduais
- PRF (Polícia Rodoviária Federal) — BRs (060, 153, 414, 040)
- AGETOP — rodovias estaduais concessionadas
- Prefeituras (Goiânia, Aparecida, Anápolis) — vias municipais

**Processo digital atual:**
- Portal DETRAN GO tem consulta de multas por placa/RENAVAM
- JARI GO aceita recurso online via portal (criado em 2021)
- Documentos aceitos em PDF
- Prazo de resposta da JARI: 30 dias úteis (na prática: 60-90 dias)

**Particularidades de GO:**
- BR-153 (Belém-Brasília) atravessa o estado — altíssimo volume de multas de caminhoneiros
- Goiânia tem sistema de câmeras municipais gerido pela Aetraffic/Perkons
- DETRAN GO tem convênio com municípios do interior — recurso via JARI estadual mesmo para multas municipais
- Agronegócio: frotas de implementos agrícolas com classificação irregular são fonte frequente de autuação

**O que precisa de validação:**
- URL atual do portal de recursos online do DETRAN GO
- Formato aceito dos documentos de defesa (campo aberto ou formulário estruturado)
- Se há API pública de consulta de multas ou só scraping

---

## DETRAN DF — Especificidades

**Órgãos autuadores no DF:**
- DETRAN DF — vias urbanas do DF
- DER-DF — Eixo Rodoviário, EPTG, vias estruturais
- PRF — trechos de BR dentro do DF (BR-020, BR-040, BR-060, BR-070)
- SEMOB — transporte público (ônibus, táxi)

**Processo digital atual:**
- DETRAN DF tem um dos portais mais avançados do país
- e-DETRAN DF: serviços online com autenticação Gov.br
- Recurso de JARI DF: aceita protocolo 100% digital
- JARI DF tem sessões quinzenais — resposta mais rápida que a média nacional
- DF integrado ao SINESP (sistema nacional)

**Particularidades do DF:**
- Alto volume de veículos oficiais (governo federal, GDF) — frota empresarial
- Plano piloto tem câmeras de velocidade média (início e fim de trecho)
  → Multas de velocidade média são contestáveis se calibração não estiver pública
- Muitos servidores públicos com CNH profissional — perda de pontos é crítica
- EPTG e Eixo: radares com histórico de contestação por sinalização deficiente
- DF tem CETRAN DF ativo com jurisprudência mais favorável ao motorista que a média

**O que precisa de validação:**
- API ou endpoint do e-DETRAN DF para consulta de multas
- Formato exato dos formulários de defesa prévia e JARI DF
- Se CETRAN DF publica suas decisões (base de jurisprudência)

---

## Arquitetura Técnica do MVP

### Fluxo do produto

```
USUÁRIO
  ↓
Envia placa + RENAVAM via WhatsApp ou web
  ↓
MÓDULO 1 — CONSULTA
  → Scraping/API DETRAN GO e DETRAN DF
  → Retorna: lista de multas com data, infração, valor, prazo de recurso
  → Alerta: "Você tem X multas. Y podem ser contestadas. Prazo mais urgente: Z dias."
  ↓
MÓDULO 2 — TRIAGEM
  → Para cada multa:
    - Identifica órgão autuador (qual JARI é competente)
    - Verifica prazo (defesa prévia ainda aberta? JARI ainda aberta?)
    - Classifica fundamento principal (IA analisa código de infração + local + data)
    - Score de probabilidade de sucesso (0-100%)
  → Apresenta apenas multas com score > 40% (não defende o indefensável)
  ↓
MÓDULO 3 — GERAÇÃO DE DEFESA
  → LLM gera peça de defesa completa com:
    - Qualificação do requerente
    - Descrição dos fatos
    - Fundamento jurídico (CTB + resoluções CONTRAN aplicáveis)
    - Pedido claro (anulação ou conversão em advertência)
  → Template diferente por órgão: DETRAN GO, DETRAN DF, PRF, DER-DF
  → Usuário revisa e assina digitalmente (assinatura ICP-Brasil ou gov.br)
  ↓
MÓDULO 4 — PROTOCOLO
  → Submete defesa no portal do órgão competente
  → Gera número de protocolo
  → Configura monitoramento automático de resposta
  ↓
MÓDULO 5 — ACOMPANHAMENTO
  → Verifica status semanalmente
  → Se negado na JARI: notifica usuário com recomendação (CETRAN vale? Judicial?)
  → Se prazo de CETRAN aberto: oferece continuar por R$X adicional
```

### Stack técnica para o MVP

```
Interface:        WhatsApp Business API (via Z-API ou Evolution API)
                  Landing page simples (Next.js)

Consulta multas:  Playwright/Puppeteer para scraping dos portais
                  SINESP API (pública, dados de veículo e infrações)
                  Monitoramento de captcha com 2captcha ou Anti-Captcha

Triagem/IA:       Claude API (análise do código de infração + local)
                  Base de dados: resoluções CONTRAN + jurisprudência JARI GO e DF
                  Score de probabilidade: modelo treinado com histórico de resultados

Geração de peça:  Claude API com prompt estruturado por tipo de infração
                  Templates versionados por órgão autuador
                  Revisão humana para multas acima de R$500 (risco jurídico)

Protocolo:        Playwright para submissão nos portais
                  Monitoramento de resposta por scraping ou e-mail parsing
                  Fallback: gera PDF para o usuário protocolar presencialmente

Assinatura:       Gov.br (gratuito, nível prata/ouro) ou D4Sign (R$0,30/doc)

Backend:          Node.js + PostgreSQL
                  Filas com BullMQ para processos assíncronos
                  n8n para orquestração de automações sem código
```

### O que NÃO construir no MVP
- App mobile nativo (WhatsApp resolve)
- Integração com todos os 26 estados (vai chegar lá, mas não agora)
- IA própria (Claude API é suficiente e mais rápido)
- Módulo de CETRAN/CONTRAN (validar mercado antes de construir segunda instância)

---

## Modelo de Receita

### Estrutura de pricing

```
CONSULTA GRATUITA
  → "Você tem 3 multas. 2 são contestáveis. Potencial: R$580 em multas canceladas."
  → CTA: "Contestar por R$0 — paga só se ganhar"

CONTESTAÇÃO — SUCCESS FEE
  → Multas até R$200:     R$49 fixo se ganhar
  → Multas R$200-500:     25% do valor da multa se ganhar
  → Multas acima R$500:   20% do valor da multa se ganhar
  → Nada cobrado se perder

PLANO FROTA (B2B)
  → Até 10 veículos:      R$299/mês (inclui consulta + contestação ilimitada)
  → 11-50 veículos:       R$699/mês
  → 51-200 veículos:      R$1.800/mês
  → Relatório mensal de economia incluído
```

### Projeção conservadora — ano 1

```
Premissas:
  - GO + DF: 5.3M veículos
  - 5% têm multa contestável por mês = 265.000 multas/mês
  - Conversão de 2% = 5.300 contestações/mês
  - Ticket médio por contestação = R$180 (multa média × 25%)
  - Taxa de sucesso na contestação = 45%
  - Cobra só se ganhar → receita = contestações × taxa de sucesso × ticket

Mês 12:
  5.300 contestações × 45% de sucesso × R$180 = R$428.940/mês
  + B2B (50 empresas × R$699 médio) = R$34.950/mês
  Total mês 12: ~R$463.000/mês
  
  CAC estimado: R$35 (Google Ads "contestar multa Goiás/DF")
  Payback: 1 contestação bem-sucedida
```

---

## Risco Jurídico — A Questão da OAB

O DoNotPay original nos EUA teve problemas com a bar association.
No Brasil, a OAB pode questionar se a plataforma está exercendo advocacia sem registro.

**Como estruturar para não ser advocacia:**
1. **O produto gera o documento — o usuário assina e protocola** (modelo assistido, não representação)
2. Para recursos mais complexos (CETRAN, judicial): parceria com escritórios de trânsito
   que revisam e assinam as peças por um valor fixo (R$30-50 por peça)
3. **Termo de serviço claro:** "Esta plataforma fornece assistência técnica e informacional.
   Não constitui serviço jurídico nem relação advogado-cliente."
4. Consultar OAB GO e OAB DF preventivamente — algumas seccionais têm posição favorável
   a legaltech que não representa o cliente

**Referência:** Contraktor, Jurídico.ai, Docket — legaltechs brasileiras que operam
na zona cinza com esse modelo de "assistência" há anos sem problemas com a OAB.

---

## Go-to-Market: GO + DF em 90 Dias

### Mês 1 — Validação sem produto
- Criar landing page com proposta: "Conteste sua multa. Paga só se ganhar."
- Rodar R$2.000 em Google Ads: "contestar multa DETRAN GO", "recurso multa DF"
- Atender as primeiras 50 contestações **manualmente** (founder faz a defesa)
- Objetivo: validar conversão, ticket médio, taxa de sucesso real, objeções comuns

### Mês 2 — MVP WhatsApp
- Bot WhatsApp que consulta multas por placa
- Geração automática da peça de defesa (Claude API)
- Protocolo manual ainda (equipe de 1-2 pessoas)
- Meta: 200 contestações no mês

### Mês 3 — Automação de protocolo
- Playwright automatizando protocolo no portal DETRAN GO e DETRAN DF
- Dashboard interno de acompanhamento
- Primeiros dados de taxa de sucesso real → calibrar score da IA
- Meta: 500 contestações no mês, break-even operacional

### Aquisição por canal

| Canal | CAC estimado | Volume | Prioridade |
|-------|-------------|--------|-----------|
| Google Ads (intenção de compra) | R$25-40 | Alto | 1º |
| Grupos de WhatsApp de motoristas | R$0 | Médio | 2º |
| Parceria com despachantes GO+DF | R$15 (rev share) | Alto | 3º |
| TikTok ("perdi a multa mas você pode ganhar") | R$10 | Alto | 4º |
| B2B direto em transportadoras GO | R$0 (cold outreach) | Médio | 5º |

---

## Expansão Natural

```
GO + DF (MVP)
  ↓ 6 meses
SP + MG (maior mercado, maior concorrência)
  ↓ 12 meses
Nacional (todos os 26 DETRANs)
  ↓
Verticais adjacentes:
  → Multas de ANVISA/Vigilância Sanitária (para empresas)
  → Autos de infração do IBAMA (agronegócio GO)
  → Cobranças indevidas de telecom/banco (DoNotPay completo)
  → Defesa de Frotas (produto B2B escalado)
```

---

## O Nome e Posicionamento

**Aravo** já está reservado para o produto de dívidas.

Sugestões para o DoNotPay Brasil:
- **Contesto** — direto, ação clara
- **Defenda** — empoderamento do motorista
- **Quito** — ambíguo (remete a quitar dívida)
- **Recursa** — técnico demais
- **Absolvo** — interessante, mas jurídico demais

**Posicionamento recomendado:**
> "Você foi multado. Pode não ter que pagar.
> A gente contesta pra você — paga só se ganhar."

Não é "legaltech". Não é "fintech". É o advogado de trânsito
que qualquer brasileiro merecia ter no bolso.
