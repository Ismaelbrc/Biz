# INSS Inteligente

Plataforma de diagnóstico, requerimento e revisão de benefícios previdenciários.
Copycat de: Atticus (EUA — Social Security Disability), adaptado para o ecossistema
INSS brasileiro com escopo muito mais amplo.

---

## Por Que É a Maior Oportunidade do Portfolio

```
40M beneficiários ativos
60M contribuintes (CLT + MEI + autônomo + facultativo)
Reforma da Previdência de 2019 → confusão que dura até hoje
Revisão da vida toda (STF 2022) → 1-2M elegíveis, prazo prescricional de 10 anos
BPC: 35M+ famílias potencialmente elegíveis, maioria não cadastrada
```

Três problemas simultâneos que o mercado não resolve:

1. **Quem ainda não se aposentou:** não sabe quando pode, em qual regra de transição
   se encaixa, quanto vai receber, se tem tempo especial que não conhece
2. **Quem teve benefício negado:** não sabe por quê, não sabe como recorrer,
   desiste ou paga advogado caro para um processo que podia ser automatizado
3. **Quem já recebe:** pode estar recebendo menos do que tem direito
   — por cálculo errado, por não ter pedido a revisão, por CNIS com falhas

O Atticus americano foca só no nicho de disability e levantou US$46M.
O INSS brasileiro tem 5x mais tipos de benefício e 4x o tamanho da população alvo.

---

## Os Produtos — Do Simples ao Complexo

### Produto 1: Diagnóstico de Aposentadoria (gratuito → aquisição)

**O que faz:**
```
Usuário conecta Gov.br (nível prata ou ouro)
  ↓
Plataforma puxa CNIS completo via API Gov.br
  ↓
Algoritmo calcula:
  - Tempo de contribuição real (com lacunas identificadas)
  - Melhor regra de transição para este perfil
  - Data mais cedo possível para cada modalidade
  - RMI estimado (Renda Mensal Inicial) para cada cenário
  - Se há período de tempo especial (insalubre/periculoso) não registrado
  ↓
Entrega: "Você pode se aposentar em MM/AAAA pelo valor de R$ X.
Pela regra de pontos você recebe R$200 a mais. Mas tem 3 meses de
contribuição faltando no seu CNIS — isso pode atrasar tudo."
```

**Por que é o produto de entrada:**
Não custa nada e entrega valor real imediatamente. Qualquer brasileiro com 40+
anos deveria fazer isso uma vez. É o "declaração de IR gratuita" do previdenciário.

---

### Produto 2: Regularização do CNIS (pago)

**O problema:** CNIS errado é silencioso e devastador.
Causas comuns: empresa não recolheu o INSS mesmo descontando do salário,
período de contribuição como autônomo sem carnê registrado, contribuição
como MEI não vinculada, fusão de empresas que perdeu histórico.

**O que faz:**
```
Identifica lacunas no CNIS comparando com CTPS digital (quando disponível)
  ↓
Gera carta de comunicação para empresa responsável
  ↓
Se empresa não existe mais: monta processo de reconhecimento via documentos
  (holerites, recibos, declaração de IR dos anos em questão)
  ↓
Protocola exigência no INSS ou PGFN dependendo do caso
  ↓
Monitora até regularização
```

**Receita:** R$299-499 fixo por período regularizado
**Por que importa:** cada mês de contribuição faltando pode atrasar a aposentadoria
em mais de um mês (regras de transição são não-lineares)

---

### Produto 3: Requerimento Assistido (pago)

**O que faz:**
```
Define a modalidade certa de aposentadoria para o perfil
  ↓
Gera checklist personalizado de documentos
  ↓
Preenche o formulário do Meu INSS automaticamente
  ↓
Protocolao requerimento via automação no portal
  ↓
Monitora prazo e status semanalmente
  ↓
Se pendência: notifica com instrução clara de como resolver
  ↓
Se negado: aciona Produto 4
```

**Receita:** R$199-399 fixo (pago antes do resultado)
**Benchmarks:** despachante cobra R$300-800 por esse serviço, sem automação,
sem monitoramento, sem diagnóstico prévio

---

### Produto 4: Recurso de Negativa (pago)

**O processo administrativo de recurso:**
```
INSS nega
  ↓
30 dias para recurso na JRPS (Junta de Recursos da Previdência Social)
  ↓
Se nega novamente: 30 dias para CRPS (Conselho de Recursos)
  ↓
Se nega: JEF (Juizado Especial Federal) — precisa de advogado
```

**O que automatiza:**
- LLM lê a carta de negativa e identifica o motivo exato
- Classifica: erro de documentação (corrigível), erro de mérito (contestável),
  negativa de perícia médica (precisa de advogado), erro de cálculo (contestável)
- Para erros corrigíveis: gera nova documentação e reprotocola
- Para erros contestáveis: gera recurso administrativo completo com jurisprudência
- Para casos que precisam de JEF: referral para advogado previdenciário parceiro
  (plataforma cobra referral fee de 20-30% do honorário do advogado)

**Receita:**
- Recurso administrativo: R$399 fixo
- Referral para JEF: R$0 para usuário + 25% do honorário do advogado parceiro
  (advogado cobra 10-25% do retroativo, plataforma fica com 25% disso)

---

### Produto 5: Revisão de Benefício — O Alto Ticket

**Por que é o maior produto:**
Quem já recebe aposentadoria pode estar recebendo menos do que deveria.
Dois cenários principais:

**Cenário A: Revisão da Vida Toda (STF 2022)**
O STF decidiu que aposentados podem incluir salários de antes de julho/1994
no cálculo do benefício. Quem contribuiu valores altos antes do Plano Real
pode ter um aumento significativo — e receber os retroativos dos últimos 10 anos.

```
Perfil elegível:
  → Aposentou antes de 2020
  → Tinha salários altos antes de julho/1994 (início do Plano Real)
  → O cálculo atual usa só contribuições de 1994 em diante

Processo:
  → Plataforma puxa histórico de contribuições (CNIS + documentos antigos)
  → Simula cálculo com e sem período pré-1994
  → Se há diferença > R$200/mês: vale a pena entrar com revisão
  → Retroativo = diferença mensal × meses desde concessão (até 10 anos)
  → Ticket típico: R$20.000-80.000 em retroativo

Receita: success fee de 10-15% do retroativo
Ticket médio de receita: R$2.000-12.000 por caso
```

**Cenário B: Erros de Cálculo Comum**
- RMI calculado com salários errados no CNIS
- Tempo especial não computado corretamente
- Fator previdenciário aplicado quando não deveria (ou vice-versa)
- Reajuste anual aplicado incorretamente

```
Processo: análise automática do extrato de benefício (PDF que o INSS envia)
→ Comparação com cálculo próprio
→ Se há divergência: protocola pedido de revisão administrativo
→ Se negado: encaminha para JEF via advogado parceiro
```

---

### Produto 6: BPC (Benefício de Prestação Continuada)

**O que é:** R$1.518/mês (1 salário mínimo) para:
- Idosos com 65+ anos de baixa renda (renda familiar per capita < 1/4 do salário mínimo)
- Pessoas com deficiência de qualquer idade em situação de vulnerabilidade

**O problema:** 35M+ potencialmente elegíveis. Processo de inscrição complexo,
exige CadÚnico atualizado, laudo médico para deficientes, entrevista social.
Muitas famílias elegíveis que nunca se inscreveram porque não sabem como.

**O que automatiza:**
```
Usuário responde 8 perguntas (renda, composição familiar, idade, deficiência)
  ↓
IA verifica elegibilidade — resultado imediato
  ↓
Se elegível: checklist de documentos e CadÚnico
  ↓
Agendamento automático no CRAS mais próximo (via API do MDS)
  ↓
Para deficientes: orientação sobre laudo médico e perícia INSS
  ↓
Acompanhamento do processo
```

**Receita:**
- R$149 fixo por inscrição (o benefício vale R$18k/ano — R$149 é irrelevante)
- Ou modelo social: parceria com prefeituras e ONGs que pagam pela triagem

---

## Arquitetura Técnica

### Integrações críticas

```
Gov.br (autenticação + dados)
  → CNIS completo (histórico de vínculos e contribuições)
  → Extrato de benefício atual
  → Dados cadastrais e documentais
  → Protocolo de requerimentos no Meu INSS
  → Acompanhamento de processos
  → Nível mínimo: prata (selfie + documento)

CNIS (via Gov.br)
  → API REST disponível para beneficiário via OAuth
  → Retorna: competências, salários de contribuição, vínculos, carência

Meu INSS (automação)
  → Playwright para preenchimento de formulários
  → Monitoramento de status por scraping
  → Fallback: geração de PDF para protocolo presencial

CadÚnico (para BPC)
  → API do Ministério do Desenvolvimento Social
  → Verificação de cadastro e elegibilidade
```

### Motor de cálculo previdenciário

Essa é a parte mais complexa tecnicamente. O algoritmo precisa:

```
Input: CNIS completo (lista de vínculos com competências e salários)

Processar:
  1. Calcular carência (meses com contribuição ≥ salário mínimo)
  2. Identificar tempo especial (CBO/CNAE do vínculo → tabela de insalubridade)
  3. Converter tempo especial: multiplicar por 1.2 (mulher) ou 1.4 (homem)
  4. Simular 4 regras de transição:
     → Pedágio 50%: quem faltava < 2 anos em 13/11/2019
     → Pedágio 100%: regime geral + tempo adicional
     → Pontos: 100 (M) / 105 (H) em 2026, progressivo
     → Idade progressiva: 60/62 (M) / 65 (H) com carência
  5. Para cada regra: calcular data mais cedo possível
  6. Calcular RMI (média de 100% dos salários de contribuição desde jul/1994)
  7. Aplicar fator previdenciário quando obrigatório
  8. Simular revisão vida toda: recalcular incluindo pré-1994

Output: tabela comparativa de cenários com data + valor estimado
```

**Complexidade:** A legislação previdenciária tem emendas constitucionais,
leis ordinárias e resoluções do Conselho de Previdência Social que se sobrepõem.
O motor precisa de um jurista previdenciário como consultor técnico permanente.

### Stack sugerida

```
Interface:        WhatsApp Business API (primário — público 60+)
                  Web simples com autenticação Gov.br

Motor de cálculo: Python (lógica previdenciária)
                  Banco de regras versionado por data de vigência
                  Testes automatizados com casos reais como fixtures

LLM (análise):    Claude API
                  → Ler carta de negativa e classificar motivo
                  → Gerar recurso administrativo
                  → Identificar fundamento de revisão

Automação:        Playwright para Meu INSS
                  n8n para orquestração de processos
                  Monitoramento via scraping + parsing de e-mail

Backend:          Python (FastAPI) + PostgreSQL
                  Fila de processos: Celery + Redis

Documentos:       iLovePDF API ou PDF.co para manipulação
                  D4Sign para assinatura digital
                  OCR: Tesseract + GPT-4V para documentos antigos (CTPS física)
```

---

## Modelo de Receita Consolidado

| Produto | Preço | Quando cobra | LTV/ticket |
|---------|-------|-------------|-----------|
| Diagnóstico | Grátis | — | — |
| Regularização CNIS | R$399 | Fixo antecipado | R$399 |
| Requerimento assistido | R$299 | Fixo antecipado | R$299 |
| Acompanhamento mensal | R$39/mês | Recorrente | R$468/ano |
| Recurso administrativo | R$399 | Fixo antecipado | R$399 |
| Referral JEF | Grátis p/ usuário | % do honorário do advogado | R$800-3.000 |
| Revisão vida toda | 12% do retroativo | Success fee | R$2.400-9.600 |
| BPC | R$149 | Fixo antecipado | R$149 |

**Projeção por perfil de cliente:**

```
Cliente simples (diagnóstico + requerimento):
  → Gasto único: R$299
  → LTV: R$299

Cliente com CNIS irregular + requerimento + acompanhamento:
  → Gasto: R$399 + R$299 + R$39×12 = R$1.166
  → LTV: R$1.166

Cliente com negativa + revisão de benefício:
  → Gasto: R$399 (recurso) + 12% do retroativo médio de R$35.000
  → LTV: R$4.599

Carteira de 10.000 clientes mistos:
  → 60% simples × R$299 = R$1.794.000
  → 30% irregular × R$1.166 = R$3.498.000
  → 10% revisão × R$4.599 = R$4.599.000
  Total: ~R$9.9M para 10.000 clientes
```

---

## O Maior Desafio: Distribuição

**O perfil do cliente não é digital-native.**

O público primário é 50-70 anos, muitas vezes com pouca escolaridade,
que não baixa app, não faz Google, e desconfia de sites desconhecidos.

**Onde esse cliente está:**

```
Farmácias (Raia, Pague Menos, UltraFarma)
  → Aposentados vão toda semana buscar remédio
  → Parceria: tablet na farmácia para diagnóstico gratuito no balcão
  → Farmácia ganha R$50-150 por conversão (indicação)

Sindicatos e federações
  → Base de trabalhadores com histórico formal de contribuição
  → Sindicatos querem serviços para associados
  → Modelo: plataforma white-label para o sindicato

Igrejas e centros comunitários
  → Confiança preestabelecida com o público 60+
  → Parceria com pastores/padres que indicam para a comunidade
  → Modelo assistencial + success fee na revisão de benefício

Contadores e despachantes
  → Já têm clientela com essas dúvidas
  → Hoje não conseguem resolver por falta de ferramenta
  → Plataforma B2B: contador usa o sistema para atender seus clientes
  → Cobra R$199/mês por acesso + split do success fee

Agências do Trabalhador / SINE
  → Trabalhadores desempregados que perdem o vínculo e precisam regularizar CNIS
  → Parceria institucional com Ministério do Trabalho (longo prazo)

WhatsApp por indicação
  → "Minha vizinha usou e descobriu que recebia R$300 a menos"
  → NPS alto → word-of-mouth naturalmente alto nesse público
  → Referral: R$100 por indicação convertida
```

**Canal que NÃO funciona para esse público:**
- Google Ads puro (pesquisa ativa baixa para "revisar benefício INSS")
- Instagram/TikTok orgânico (não é o canal deles)
- App store (não baixam app)

---

## Risco Jurídico — Mais Sério que no DoNotPay

Calcular direitos previdenciários e gerar recursos é inequivocamente advocacia.
O INSS Inteligente não pode operar sem uma estrutura jurídica adequada.

**Três modelos possíveis:**

**Modelo A: Plataforma de triagem + rede de advogados**
- Plataforma faz o diagnóstico e a análise
- Advogado previdenciário parceiro revisa e assina toda peça jurídica
- Advogado cobra do cliente, plataforma recebe referral fee
- Mais seguro regulatoriamente, margem menor

**Modelo B: Escritório próprio de previdência**
- Abrir escritório de advocacia previdenciária como braço da empresa
- Contratar advogados previdenciários CLT ou sócios
- Produto é o escritório — plataforma é o sistema interno
- Mais controle, mais complexo de operar

**Modelo C: Despachante previdenciário + advogado**
- Despachante previdenciário (não é advogado, mas tem atuação reconhecida)
  faz o requerimento e o recurso administrativo
- Advogado parceiro só para JEF
- Zona cinza — OAB pode questionar
- Funciona hoje, mas é o modelo mais arriscado de longo prazo

**Recomendação:** Modelo A para começar. Construir rede de 20-30 advogados
previdenciários em GO, DF e SP como parceiros. Plataforma faz o trabalho
de triagem e geração — advogado faz a supervisão jurídica e assina.
Split: advogado fica com 40% do fee, plataforma com 60%.

---

## Roadmap de Construção

### Fase 1 — Meses 1-3: Diagnóstico + Requerimento Simples

**Meta:** validar que o diagnóstico gera demanda e que o requerimento
assistido converte pagamento.

Construir:
- Motor de cálculo previdenciário (aposentadoria por idade e regras de transição)
- Integração Gov.br para puxar CNIS
- Interface WhatsApp para diagnóstico
- Processo de requerimento semi-automatizado (automação + revisão humana)
- Parceria com 5 advogados previdenciários GO + DF

KPIs de validação:
- 500 diagnósticos realizados
- 15% de conversão para requerimento pago (R$299)
- NPS > 70

### Fase 2 — Meses 4-6: Recurso + BPC

**Meta:** adicionar o caso de uso de negativa e o público BPC.

Construir:
- LLM para análise de carta de negativa
- Templates de recurso por tipo de negativa
- Fluxo de BPC com integração CadÚnico

KPIs:
- 100 recursos protocolados
- Taxa de sucesso em recursos > 40%
- 200 BPCs instruídos

### Fase 3 — Meses 7-12: Revisão de Benefício

**Meta:** lançar o produto de alto ticket.

Construir:
- Algoritmo de revisão da vida toda
- Upload e OCR de documentos históricos (holerites antigos, CTPS física)
- Parceria com 10 advogados para JEF (os casos que vão para judicial)
- Dashboard de acompanhamento de retroativos

KPIs:
- 500 simulações de revisão realizadas
- 50 processos de revisão abertos
- Ticket médio de success fee > R$3.000

### Fase 4 — Ano 2: Escala e B2B

- Plataforma B2B para contadores e despachantes
- Expansão para SP, MG, RS
- Parceria com sindicatos (1-2 grandes para validar canal)
- Produto de monitoramento contínuo (mudanças na legislação que afetam o benefício)

---

## Por Que Ninguém Fez Ainda

```
Complexidade técnica alta:
  → Motor de cálculo previdenciário é não-trivial
  → 30+ anos de legislação com emendas que se sobrepõem
  → Integração Gov.br exige homologação

Distribuição difícil:
  → Público não digital
  → Canal de aquisição não óbvio

Risco jurídico percebido:
  → Medo da OAB
  → Mas o modelo correto (triagem + advogado parceiro) resolve

Mercado subestimado:
  → Parece "serviço para pobres"
  → Na realidade: revisão de benefício toca classe média e média-alta
    que contribuiu por décadas com salários altos
```

**A janela:** A revisão da vida toda tem prazo prescricional de 10 anos.
Quem se aposentou entre 2015 e 2022 tem até 2025-2032 para pedir.
Quem entrar nesse mercado nos próximos 2 anos pega a maior onda.

---

## Nome e Posicionamento

**Nome sugerido:** Previsio / Previdus / Amparo / Vínculo

**Posicionamento:**
> "Você contribuiu a vida toda.
> A gente garante que vai receber tudo que é seu."

Não é "app de INSS". Não é "fintech previdenciária".
É o especialista previdenciário que qualquer trabalhador brasileiro
merecia ter do lado — mas que era caro demais para a maioria pagar.
