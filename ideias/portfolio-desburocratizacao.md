# Portfolio: Desburocratização + Automação

Cinco negócios core + três alavancas institucionais (cartórios, DETRAN, energia).
Cada um é um copycat de modelo provado fora do Brasil, operando em mercado real,
com automação como vantagem competitiva central.

---

## 1. DoNotPay Brasil

**Copycat de:** DoNotPay (EUA), Fairpay (UK)
**Tese:** O Brasil tem 100M+ multas de trânsito por ano, bilhões em cobranças indevidas
de telecom/banco e um Juizado Especial Cível que poucos sabem usar. Tudo isso pode
ser automatizado — a contestação, o protocolo, o acompanhamento.

### O que automatiza
```
Multa de trânsito
  → OCR lê o documento
  → IA identifica fundamento legal (irregularidade na sinalização, prazo de notificação,
     erro de autuação, câmera sem certificação)
  → Gera recurso completo no padrão do DETRAN estadual
  → Protocola via portal eletrônico
  → Monitora prazo de resposta e aciona 2ª instância se negado

Cobrança indevida (telecom, banco, seguro)
  → Usuário descreve a cobrança
  → IA compara com contrato e legislação (CDC)
  → Gera carta de contestação + protocolo formal
  → Se não resolvido em 5 dias: abre PROCON digital automaticamente
  → Se não resolvido em 15 dias: gera petição para JEC e guia o usuário no protocolo

Cancelamento de serviço
  → Identifica cláusula de fidelidade
  → Calcula multa devida (ou disputa se indevida)
  → Gera e envia carta de cancelamento via protocolo
```

### Modelo de receita
| Produto | Preço | Gatilho |
|---------|-------|---------|
| Assinatura mensal | R$29/mês | Uso ilimitado de contestações |
| Success fee multa | 30% da multa cancelada | Só cobra se ganhar |
| Success fee cobrança | 20% do valor recuperado | Só cobra se ganhar |
| B2B (frotas, empresas) | R$500-2.000/mês | Volume de casos |

### Stack técnica
- OCR para leitura de documentos (Tesseract + GPT-4V)
- LLM com base jurídica brasileira (CDC, CTB, resoluções ANATEL/BACEN)
- Integração com portais de protocolo eletrônico (DETRAN, PROCON digital, e-JEC)
- WhatsApp como canal principal (Brazilians don't use apps for this)

### Tamanho do mercado
- 100M+ multas/ano × taxa de contestação estimada de 15% = 15M potenciais usuários
- R$2.5B/ano em cobranças indevidas de telecom (fonte: ANATEL)
- 40M consumidores com ao menos uma cobrança contestável por ano

### Riscos principais
1. **Regulatório:** OAB pode questionar automação de peças jurídicas — estruturar como
   "assistente" que o usuário assina, não como serviço jurídico autônomo
2. **Integração:** portais de DETRAN variam por estado — 26 integrações necessárias
3. **Taxa de sucesso:** se não ganhar não cobra — modelo exige alta precisão da IA

### Por que agora
LLMs são bons o suficiente para peças jurídicas de baixa complexidade. e-Gov avançou.
A janela de 2-3 anos antes da concorrência perceber isso é real.

---

## 2. INSS Inteligente

**Copycat de:** Atticus (EUA — Social Security Disability), Silvur (EUA — retirement planning)
**Tese:** 40M+ beneficiários do INSS no Brasil. A maioria recebe menos do que tem direito
ou não sabe que tem direito a benefícios que nunca solicitou. O sistema é inacessível para
quem mais precisa — idosos, trabalhadores de baixa renda, informais.

### O que automatiza
```
Diagnóstico de direitos
  → Usuário responde 15 perguntas (histórico de trabalho, idade, saúde)
  → IA cruza com CNIS (via Gov.br API) e extrai histórico contributivo
  → Calcula: data de aposentadoria + valor estimado + benefícios elegíveis agora

Requerimento automatizado
  → Gera documentação necessária com checklist personalizado
  → Preenche formulários do Meu INSS automaticamente
  → Agenda perícia médica se necessário
  → Protocola requerimento via API do Gov.br

Recurso de negativa
  → INSS nega: IA lê o motivo, identifica fundamento de recurso
  → Gera recurso administrativo completo
  → Se negado na esfera administrativa → encaminha para JEF (Juizado Federal)
  → Parceria com advogados previdenciários para casos complexos (referral fee)

Revisão de benefício
  → Benefício já concedido mas potencialmente subavaliado
  → Pós-teto do INSS (2019): revisão de vida toda
  → IA simula todos os cenários e calcula se vale entrar com revisão
```

### Modelo de receita
| Produto | Preço | Base |
|---------|-------|------|
| Diagnóstico | Gratuito | Aquisição |
| Requerimento assistido | R$199 fixo | Conversão |
| Success fee em revisão | 10-15% do valor recuperado | Alto ticket |
| Assinatura monitoramento | R$39/mês | Recorrência |

**Ticket médio de revisão:** R$15.000-50.000 em valores retroativos
**LTV potencial:** R$2.000-7.500 por cliente com revisão

### Complexidade técnica
- Integração com Gov.br (API de autenticação e dados do CNIS)
- Algoritmo de cálculo previdenciário (complexo — diferentes regras por período)
- Base de jurisprudência do TNU (Turma Nacional de Uniformização)
- Parceria com despachantes previdenciários licenciados para representação formal

### Tamanho do mercado
- 40M beneficiários ativos
- 15M trabalhadores informais que vão precisar do INSS e não contribuem corretamente
- Estimativa: R$30B+ em benefícios subaproveitados ou não reclamados
- Revisão de vida toda (STF 2022): potencial de R$200B em revisões possíveis

### Riscos principais
1. **Regulatório INSS:** autarquia pode fechar APIs ou dificultar acesso a CNIS
2. **Complexidade jurídica:** legislação previdenciária tem 30+ emendas — base precisa ser atualizada constantemente
3. **Público-alvo:** idosos e trabalhadores de baixa renda são difíceis de alcançar digitalmente

### Go-to-market
Não é produto digital nativo — é distribuição via:
- Sindicatos e associações de categoria
- Redes de farmácias (onde aposentados vão)
- Igrejas e centros comunitários
- Parcerias com contadores e despachantes

---

## 3. Aravo — Renegociação de Dívidas com IA

**Copycat de:** TrueAccord (EUA), Resolve (EUA), Tally (EUA)
**Nome:** Aravo
**Tese:** 70M negativados no Brasil. O mercado de cobranças é brutal e ineficiente —
taxa de recuperação média de cobrança tradicional é 20%. TrueAccord chegou a 50%+
usando IA para personalizar cada interação. O Aravo faz isso do lado do devedor:
negocia a melhor condição possível e limpa o nome de forma estruturada.

### O que automatiza
```
Mapeamento de dívidas
  → Integração com Serasa, SPC, BACEN (via Open Finance)
  → Agrega todas as dívidas em um painel único
  → Calcula: valor original, juros acumulados, prazo de prescrição,
    poder real de negociação por credor

Negociação inteligente
  → IA modela o comportamento histórico de cada credor
    (Banco X aceita 40% de desconto após 24 meses? Sistema sabe.)
  → Define estratégia: negociar agora vs. esperar prescrição vs. contestar validade
  → Negocia automaticamente via API do Serasa Limpa Nome / Desenrola
  → Se credor não aceita: identifica se há fundamento para contestação judicial

Plano de recuperação de crédito
  → Após quitação: roadmap de reconstrução de score (passo a passo)
  → Monitoramento mensal do Serasa Score
  → Alerta quando novas dívidas aparecem

JEC automatizado para dívidas contestáveis
  → Cobranças com juros acima do legal, multas abusivas, dívidas prescritas
  → Gera petição para JEC, guia o usuário no protocolo
```

### Modelo de receita
| Produto | Preço |
|---------|-------|
| Success fee em negociação | 15% do desconto obtido |
| Assinatura monitoramento | R$19/mês |
| Plano de recuperação premium | R$99/mês por 12 meses |

**Exemplo de valor gerado:**
- Dívida de R$10.000 negociada por R$4.000 = desconto de R$6.000
- Fee do Aravo: R$900 (15% de R$6.000)
- Custo para o usuário: R$900 para quitar R$10.000 por R$4.000

### Vantagem competitiva
O Aravo joga do lado do devedor — modelo oposto ao TrueAccord (que é B2B para credores).
Isso é: maior mercado endereçável, menor CAC (o devedor quer ser ajudado), melhor NPS.

### Infraestrutura existente no Brasil que facilita
- Serasa Limpa Nome já tem APIs de negociação
- Desenrola criou protocolo padronizado com grandes credores
- Open Finance permite aggregar situação financeira completa
- PIX facilita pagamento instantâneo de acordos

### Riscos principais
1. **Inadimplência do próprio usuário:** vai renegociar e não pagar o Aravo
   → Solução: cobrar fee embutido no boleto da renegociação
2. **Concentração de credores:** os 5 maiores bancos respondem por 60% das dívidas
   → Se eles fecharem APIs: renegociação manual assistida por IA
3. **Prescrição:** orientar o usuário a não pagar dívida prescrita pode gerar risco legal

---

## 4. MEI Automatizado

**Copycat de:** Bench (EUA), Coconut (UK), Keeper Tax (EUA)
**Tese:** 15M MEIs no Brasil. Todos têm as mesmas 4 obrigações mensais. Nenhum
produto as resolve completamente de forma automatizada. O mercado existe,
é enorme, e é tecnicamente simples de resolver.

### As 4 obrigações do MEI — todas automatizáveis
```
1. DAS mensal (imposto)
   → Hoje: o MEI gera o boleto no Portal do Empreendedor e paga manualmente
   → Automatizado: débito automático via Pix agendado, dia 20 de cada mês
   → Alerta 5 dias antes com valor + confirmação via WhatsApp

2. Emissão de nota fiscal
   → Hoje: cada prefeitura tem um sistema diferente (50% tem API, 50% é portal)
   → Automatizado: MEI descreve o serviço no WhatsApp → sistema emite NFS-e
   → Envia a nota para o tomador automaticamente

3. DASN-SIMEI (declaração anual)
   → Prazo: até 31 de maio
   → Hoje: 30% dos MEIs perdem o prazo e pagam multa
   → Automatizado: sistema preenche com dados do ano, MEI confirma, envia

4. Alerta de limite
   → MEI pode faturar até R$81k/ano
   → Automatizado: dashboard de faturamento acumulado + alerta quando
     atinge 70%, 90%, 100% — com recomendação de migração para Simples

Bônus — o que o concorrente não faz:
   → Cálculo do pró-labore ótimo (distribuição de lucros vs. pró-labore)
   → Análise "devo migrar para Simples?" com simulação de imposto comparado
   → Gestão de clientes PJ que exigem comprovantes/certidões
```

### Interface: WhatsApp-first
O MEI não usa app. O MEI usa WhatsApp.

```
Bot via WhatsApp:
- "Emitir nota" → guia em 3 mensagens
- "Quanto devo de imposto este mês?" → responde na hora
- "Quantos reais ainda posso faturar no ano?" → responde na hora
- "Venceu meu DAS" → paga automaticamente e confirma
```

### Modelo de receita
| Plano | Preço | O que inclui |
|-------|-------|-------------|
| Grátis | R$0 | Alertas e calculadora |
| Essencial | R$29/mês | DAS automático + DASN |
| Completo | R$59/mês | Tudo + NF + dashboard + suporte |
| Autônomo (sem MEI) | R$49/mês | CARNÊ-LEÃO automático + IR |

### Tamanho do mercado
- 15M MEIs × R$35/mês médio = **R$525M/mês de receita potencial**
- 1M novos MEIs por ano de crescimento orgânico
- Churn baixo: obrigação fiscal não some — cliente fica enquanto o MEI existir

### Diferencial de distribuição
Não é um app na App Store. Distribuição via:
- Sebrae (parceria institucional natural)
- Contabilizei, Abertura Simples (upsell/downsell)
- Bancos digitais (Nubank, Inter, C6 — já têm a base de MEIs)
- YouTube/TikTok de educação financeira para MEIs

### Riscos principais
1. **Concorrência de banco:** Nubank, Inter podem lançar isso internamente
   → Diferencial: especialização + WhatsApp nativo + profundidade de features
2. **Volatilidade regulatória:** limite do MEI muda (já mudou 3x em 10 anos)
   → Oportunidade: cada mudança gera onda de novos clientes confusos
3. **Margem de suporte:** MEIs ligam para tirar dúvida — escalar suporte é caro
   → Solução: IA resolve 80% das dúvidas antes de chegar em humano

---

## 5. Defesa de Frotas

**Copycat de:** TicketKick (EUA), ACS Fleet (EUA), Conduent (EUA para grandes frotas)
**Tese:** Empresa com 30 caminhões recebe ~300 multas/ano. Cada defesa manual
custa 2-4h de trabalho jurídico/administrativo. Ninguém fez um SaaS para
o segmento médio (5-200 veículos) no Brasil.

### O que automatiza
```
Captura de multas
  → Monitoramento diário de consulta de multas por placa (DETRAN + SINFRA)
  → Parsing de e-mails de notificação de infração
  → Integração com sistemas de frota (Sascar, Onixsat, Cobli, Rastreio.net)
  → Notificação imediata ao gestor com prazo de defesa

Análise e priorização
  → IA classifica cada multa por probabilidade de sucesso na defesa:
    - Alta (>70%): gera defesa automática
    - Média (40-70%): apresenta ao gestor para aprovação
    - Baixa (<40%): recomenda pagar com desconto
  → Fundamentos avaliados: irregularidade na sinalização, erro de equipamento,
    prazo de notificação, erro de identificação de condutor, calibração do radar

Geração e protocolo
  → Defesa gerada com jurisprudência do CONTRAN por tipo de infração
  → Personalizada por estado (cada DETRAN tem seus formulários)
  → Upload automático no portal do DETRAN estadual
  → Controle de prazos com alertas (prazo é fatal — perda = infração definitiva)

Reporting
  → Dashboard: multas recebidas × defendidas × ganhas × pagas
  → Economia gerada no mês/ano
  → Motoristas com mais infrações (gestão comportamental)
  → Benchmark por tipo de veículo/rota
```

### Modelo de receita
| Plano | Veículos | Preço/mês |
|-------|----------|-----------|
| Starter | 5-20 | R$800 |
| Growth | 21-100 | R$2.500 |
| Scale | 101-500 | R$6.000 |
| Enterprise | 500+ | Sob consulta |

**ROI típico para cliente:**
- Frota de 50 veículos: ~500 multas/ano × R$200 média = R$100.000/ano em multas
- Taxa de sucesso na defesa: 35-50% = R$35.000-50.000 em multas canceladas
- Custo do sistema: R$30.000/ano
- ROI: >100% no primeiro ano, sem contar horas de trabalho economizadas

### Moat técnico
Integrar os portais de DETRAN dos 26 estados é trabalhoso — leva 12-18 meses.
Quem faz primeiro tem vantagem de 2-3 anos antes de qualquer concorrente replicar.

### Segmentos prioritários
1. **Transportadoras** — maior volume de multas por natureza da operação
2. **Construtoras** — frota pesada, multas de carga
3. **Distribuidores** — caminhões em rota urbana (radar, faixa de ônibus)
4. **Locadoras de veículos** — responsabilidade legal de contestar em nome do cliente

### Riscos principais
1. **Scraping instável:** DETRAN muda layout → quebra integração
   → Mitigação: monitoramento contínuo + time de manutenção
2. **Regulatório:** DENATRAN pode fechar APIs de consulta em massa
   → Mitigação: parceria formal + modelo de negócio legítimo
3. **Taxa de sucesso:** se performance cai, cliente cancela
   → Mitigação: só defender o que a IA classifica como defensável

---

## Alavancas Institucionais: Cartórios, DETRAN, Energia

Esses três não são negócios isolados — são **camadas de infraestrutura** que amplificam os 5 negócios acima e abrem verticais próprias.

---

### Cartórios — A Camada Mais Inexplorada

**Por que é oportunidade:** 14.000 cartórios no Brasil. O e-Notariado existe desde 2017
mas a maioria das integrações ainda é manual. Três processos são automatizáveis agora:

**Vertical 1: Cancelamento de Protesto Automatizado**
- Empresa paga a dívida → cartório de protesto precisa ser notificado → certidão de cancelamento emitida
- Hoje: processo manual, demora 5-15 dias, custa R$150-500 por cartório
- Automatizado: integração com CRA/IEPTB → cancelamento solicitado via API → certidão digital emitida
- **Mercado:** 10M protestos cancelados por ano, R$1.5B em taxas cartoriais
- **Conexão com Aravo:** todo cliente que quita dívida via Aravo precisa cancelar o protesto — pipeline natural

**Vertical 2: Certidões Imobiliárias para Crédito**
- Comprar imóvel, refinanciar, fazer inventário — tudo exige certidões de cartório de imóveis
- Hoje: cada certidão é solicitada manualmente em cada cartório da cadeia dominial
- Automatizado: plataforma agrega solicitação de múltiplas certidões, monitora prazo, consolida
- **Mercado:** 1M+ transações imobiliárias/ano, cada uma exige 5-15 certidões
- **Conexão com Imóvel Regular (ideia #5):** produto nativo para regularização fundiária

**Vertical 3: Monitoramento de Protestos para PMEs**
- PME concede crédito para cliente → não sabe se cliente está em protesto em outro estado
- Automatizado: monitoramento contínuo de protestos nacionais via IEPTB API
- Alerta instantâneo quando fornecedor/cliente entra em protesto
- **Modelo:** R$199-999/mês por empresa conforme volume de CNPJs monitorados

---

### DETRAN — Além das Multas

O DETRAN vai muito além da defesa de multas da Defesa de Frotas.
Três serviços de alto volume ainda não automatizados:

**Serviço 1: IPVA + Licenciamento Autopilot**
- 50M veículos no Brasil pagam IPVA e licenciamento anualmente
- Hoje: notificação chega pelo Correios (quando chega), proprietário tem que lembrar
- 30% dos veículos circulam com licenciamento vencido por esquecimento
- **Produto:** app/WhatsApp que monitora o calendário do seu veículo, avisa com 30 dias
  de antecedência, e paga automaticamente via Pix quando autorizado
- **Receita:** R$9,90/veículo/ano (mais barato que a multa de R$195 por licenciamento vencido)
- **Mercado:** 50M veículos × R$9,90 = R$495M de receita potencial anual

**Serviço 2: Transferência de Propriedade Guiada**
- Comprar ou vender carro é um pesadelo burocrático no Brasil
- Processo: ATPV, vistoria, DETRAN, pagamento de IPVA, DPVAT, CRLV novo
- Cada estado tem variações. Custo de errar: multa + retrabalho + tempo
- **Produto:** R$149-299 por transferência. Usuário envia documentos pelo WhatsApp,
  sistema gera checklist personalizado por estado, guia cada passo, alerta prazo
- **Mercado:** 15M+ transferências por ano no Brasil
- **Conexão com DoNotPay:** se der problema na transferência, contesta automaticamente

**Serviço 3: CNH Digital e Renovação**
- CNH vence a cada 5 anos. A renovação envolve: agendamento no DETRAN,
  exame médico, taxa, emissão
- O agendamento no DETRAN é caótico — filas online de semanas
- **Produto:** monitora disponibilidade de vagas no DETRAN do usuário,
  avisa quando abre vaga no horário preferido, reserva automaticamente
- Agendamento inteligente: como o Doctolib faz para médicos, para o DETRAN
- **Receita:** R$29,90 por agendamento realizado

---

### Companhias de Energia — Três Mercados Distintos

**Vertical 1: Tarifa Social Automatizada**
- 35M+ famílias potencialmente elegíveis para desconto de 65% na conta de luz
- Hoje: processo de inscrição é manual, feito na distribuidora, com fila
- Milhões de famílias elegíveis que nunca se inscreveram
- **Produto:** usuário envia CPF → IA verifica elegibilidade via CadÚnico/NIS →
  se elegível, protocola inscrição automaticamente junto à distribuidora
- **Receita:** R$49,90 por inscrição realizada (pago pela família — economiza R$800-1.200/ano)
- **Escala:** ONGs, igrejas, sindicatos como canal de distribuição
- **Tamanho:** 10M famílias elegíveis × R$49 = R$490M de mercado endereçável

**Vertical 2: Contestação de Conta de Energia**
- Distribuidoras como Enel, Light, Energisa têm histórico de cobranças irregulares:
  releitura errada, bandeira tarifária cobrada indevidamente, estimativa inflada
- ANEEL tem ouvidoria com prazo legal de resposta, mas processo é manual
- **Produto:** usuário fotografa a conta → IA analisa: consumo histórico, tarifa aplicada,
  bandeira correta, multas devidas → identifica irregularidade → protocola na ANEEL/PROCON
- **Receita:** success fee de 20% do valor recuperado
- **Conexão com DoNotPay:** pode ser vertical dentro do produto maior

**Vertical 3: Burocracia de Energia Solar (o maior)**
- Brasil instalou 30GW de energia solar. Meta: 100GW até 2030
- Cada instalação residencial/comercial precisa de homologação pela distribuidora
- Prazo legal: 30 dias. Prazo real: 3-9 meses. Motivo: burocracia interna das distribuidoras
- Esse atraso custa ao setor solar R$2B+/ano em projetos paralisados
- **Produto B2B:** integrador solar usa a plataforma para:
  - Montar processo completo (formulários + laudos + diagramas) no padrão de cada distribuidora
  - Protocolar e monitorar automaticamente
  - Alertar sobre pendências antes que virem reprovação
  - Dashboard de todos os projetos com status em tempo real
- **Receita:** R$99-299/projeto ou R$800-3.000/mês por integrador (SaaS)
- **Mercado:** 500.000 instalações/ano × R$150 médio = **R$75M/ano só neste nicho**
- **Por que é defensável:** cada distribuidora tem regras diferentes e mudam frequentemente —
  manter a base atualizada é o moat

---

## Como Esses Negócios se Conectam

```
ARAVO (dívidas)
  → quita dívida
  → CARTÓRIO: cancela protesto automaticamente
  → SERASA: atualiza score
  → INSS INTELIGENTE: agora que está regular, requer benefício

MEI AUTOMATIZADO
  → MEI tem NF emitida
  → DETRAN: paga IPVA do veículo de trabalho automaticamente
  → ENERGIA: verifica elegibilidade para Tarifa Social (MEI de baixa renda)
  → DONOTPAY: contesta multa do veículo de entrega

DEFESA DE FROTAS
  → DETRAN: integração nativa para consulta de multas
  → DONOTPAY: compartilha base de jurisprudência CONTRAN
  → Escala para PMEs não-frota via DoNotPay B2B

DONOTPAY
  → DETRAN: multas de trânsito (consumer)
  → CARTÓRIO: cancela protesto após quitação
  → ENERGIA: contesta conta indevida
  → JEC: processa qualquer cobrança abusiva
```

**A tese de portfólio:** cada produto resolve uma dor isolada. Mas o cliente que resolve
uma dor tem outras. Quem construir a plataforma de acesso a todos esses serviços
— o "super app da desburocratização" — tem o maior LTV e menor CAC por aquisição.

---

## Prioridade de Entrada

| Negócio | Complexidade | Time to Revenue | Mercado | Score |
|---------|-------------|----------------|---------|-------|
| MEI Automatizado | Baixa | 3 meses | ⭐⭐⭐⭐⭐ | **1º** |
| DoNotPay Brasil | Média | 4 meses | ⭐⭐⭐⭐⭐ | **2º** |
| Aravo | Média | 4 meses | ⭐⭐⭐⭐⭐ | **3º** |
| Defesa de Frotas | Média | 5 meses | ⭐⭐⭐⭐ | **4º** |
| Energia Solar B2B | Média | 3 meses | ⭐⭐⭐⭐ | **5º** |
| INSS Inteligente | Alta | 8 meses | ⭐⭐⭐⭐⭐ | **6º** |
| Tarifa Social | Baixa | 2 meses | ⭐⭐⭐ | **7º** |
| DETRAN Autopilot | Baixa | 3 meses | ⭐⭐⭐⭐⭐ | **8º** |
