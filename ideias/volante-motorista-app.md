# Volante — Plataforma de Gestão para Motorista de Aplicativo

Back-office completo do motorista de Uber e 99:
ganhos reais, custos, manutenção e frota — tudo em um lugar.

---

## O Problema Central

O motorista de aplicativo é um microempreendedor que não sabe quanto lucra.

```
O que ele acha que ganha:
  Uber + 99 este mês:    R$5.200 ✅

O que ele realmente lucra:
  Recebido das apps:     R$5.200
  - Combustível:        -R$  920  (1.400km × R$0,66/km)
  - Manutenção (prov.): -R$  350  (R$0,25/km)
  - Depreciação:        -R$  600  (carro R$50k, 5 anos, 200k km)
  - Lavagem:            -R$  120
  - Seguro:             -R$  180
  - DAS (MEI):          -R$   70
  Lucro real:            R$2.960 😬
```

Ele trabalhou 180h no mês achando que ganhou R$29/h.
Na verdade ganhou R$16,50/h — menos que o salário mínimo por hora.

Sem saber isso, não consegue tomar nenhuma decisão boa:
quando parar de trabalhar, quando trocar o carro, se vale colocar
um segundo motorista, se deve mudar de horário.

---

## Copycat de Referência

| Produto | País | O que faz |
|---------|------|-----------|
| **Gridwise** | EUA | Analytics de ganhos + previsão de demanda |
| **Stride** | EUA | Gastos e impostos para gig workers |
| **Hurdlr** | EUA | Rastreamento de despesas + milhas para autônomos |
| **Para** | EUA | Transparência de ganhos antes de aceitar corrida |
| **Mystro** | EUA | Multi-app — alterna entre Uber/Lyft/DoorDash automaticamente |

**O gap no Brasil:** nenhum desses existe aqui. O motorista brasileiro
usa planilha no Excel, caderno, ou — na maioria das vezes — não controla nada.

---

## Os Módulos

### Módulo 1 — Ganhos Reais

**Integração com Uber e 99:**
```
Opção A (ideal): API oficial de dados do motorista
  → Uber tem Uber Movement API + dados históricos para parceiros
  → 99 tem programa de parceiros com acesso a dados

Opção B (fallback): leitura de extrato
  → Motorista exporta o extrato semanal/mensal (CSV) e importa
  → OCR do comprovante de repasse

Opção C (manual):
  → Motorista registra ao final do dia — 30 segundos
  → Plataforma faz as médias e tendências
```

**O que o dashboard mostra:**
```
Hoje:
  Corridas: 23
  Km rodado: 187km
  Recebido bruto: R$312
  Custo estimado: R$89
  Lucro estimado: R$223
  R$/hora (8h): R$27,87
  R$/km: R$1,19

Esta semana vs semana passada: +12%
Melhor dia da semana: quinta (R$67,20/h média)
Melhor horário: 7h-9h e 17h-20h
```

**Inteligência de horário:**
```
Com base no seu histórico dos últimos 60 dias:
  → Trabalhar domingo à noite vale 40% menos que sexta
  → Manhã de terça tem menos corridas mas maior ticket médio
  → Seu aeroporto mais próximo: pico às 5h30 e 18h

Sugestão desta semana: "Quinta e sexta à noite + sábado manhã
  = 35h de trabalho, estimativa de R$2.100 líquido."
```

---

### Módulo 2 — Controle de Custos

**Combustível (o maior custo):**
```
Motorista informa: km no odômetro + litros abastecidos + valor pago
  ↓
Plataforma calcula:
  → Consumo real (km/l) e tendência
  → Custo por km rodado
  → Alerta: "Seu consumo caiu de 11km/l para 9km/l.
    Pode ser pneu murcho ou filtro de ar sujo."

Integração Open Finance:
  → Identifica automaticamente compras em postos de gasolina
  → Sugere: "Posto X está R$0,18/l mais barato no seu trajeto habitual"
```

**Todos os custos em um lugar:**
```
Combustível:     automático (Open Finance ou manual)
Manutenção:      gerado pelo módulo de manutenção
Depreciação:     calculada pelo valor do carro + km rodado
Seguro:          cadastrado uma vez, rateado por mês
Lavagem:         registrado pelo motorista
MEI/impostos:    calculado automaticamente sobre o faturamento
IPVA/seguro:     calculado por mês (valor anual ÷ 12)
```

**Relatório mensal simples:**
```
┌─────────────────────────────────┐
│ RESULTADO DO MÊS                │
├─────────────────────────────────┤
│ Recebido (Uber + 99):  R$5.200  │
│ (-) Combustível:      -R$  920  │
│ (-) Manutenção:       -R$  350  │
│ (-) Depreciação:      -R$  600  │
│ (-) Seguro/IPVA:      -R$  180  │
│ (-) Lavagem:          -R$  120  │
│ (-) MEI:              -R$   70  │
│                       ─────────  │
│ LUCRO REAL:            R$2.960  │
│ R$/hora trabalhada:    R$16,44  │
└─────────────────────────────────┘
```

---

### Módulo 3 — Manutenção Inteligente

**O problema:** carro parado = zero receita. Manutenção preventiva
custa 3x menos que corretiva. Motorista raramente faz preventiva
porque não tem controle dos km rodados por tipo de manutenção.

**Perfil do veículo:**
```
Carro: Hyundai HB20 2021
Odômetro atual: 87.340 km
Km rodado este mês: 3.200 km
Km médio por dia: 147 km
```

**Agenda de manutenção automática:**
```
ITEM              INTERVALO   ÚLTIMO     PRÓXIMO    STATUS
Troca de óleo     5.000 km    85.000 km  90.000 km  ⚠️ 2.660 km
Filtro de ar      15.000 km   80.000 km  95.000 km  ✅ OK
Filtro de cabine  15.000 km   75.000 km  90.000 km  ⚠️ 2.660 km
Pneus (rotação)   10.000 km   80.000 km  90.000 km  ⚠️ 2.660 km
Revisão geral     30.000 km   60.000 km  90.000 km  ⚠️ 2.660 km
Alinhamento       10.000 km   85.000 km  95.000 km  ✅ OK
Freios (pastilha) 40.000 km   60.000 km  100.000 km ✅ OK
```

**Alertas inteligentes:**
```
"Sua troca de óleo vence em 2.660 km — aproximadamente 18 dias
  no seu ritmo atual. Agendando na oficina parceira X por R$89?"

"Você está rodando 147km/dia. Com esse ritmo, em 6 meses
  você bate 115.000 km — é hora de considerar trocar o carro."
```

**Integração com oficinas parceiras:**
- Parcerias com redes de oficinas em GO + DF
- Agendamento pelo app com desconto para usuários Volante
- Receita: comissão de 8-12% por serviço agendado

**Histórico completo:**
- Cada manutenção registrada com data, km, valor, oficina
- Relatório para venda do carro: "Carro bem mantido, todas as revisões documentadas"
- Aumenta o valor de revenda em R$2.000-5.000

---

### Módulo 4 — Gestão de Frota

**Quem precisa disso:**
O "dono de frota" — perfil muito comum nas periferias de Goiânia e Brasília:
alguém que tem 2-5 carros e coloca motoristas para rodar, recebendo
um valor fixo diário (diária) ou percentual das corridas.

Esse cara hoje gerencia tudo no WhatsApp e no caderno.
Não sabe qual carro está dando lucro, qual motorista está rodando bem,
qual carro está custando mais em manutenção.

**O que o módulo faz:**
```
Painel da frota:
  Carro 1 (HB20 - motorista João):
    → Recebeu este mês: R$4.800
    → Repasse para João (60%): R$2.880
    → Lucro bruto do dono: R$1.920
    → Custo manutenção: R$420
    → Lucro líquido: R$1.500

  Carro 2 (Cronos - motorista Pedro):
    → Recebeu este mês: R$3.200
    → Repasse para Pedro (60%): R$1.920
    → Lucro bruto do dono: R$1.280
    → Custo manutenção: R$680 ← ALERTA: alto
    → Lucro líquido: R$600 ← ALERTA: baixo

  Total da frota:
    → Receita: R$8.000
    → Lucro líquido: R$2.100
    → R$/carro: R$1.050 médio
```

**Gestão dos motoristas:**
```
Registro de cada motorista: CPF, CNH, vencimento CNH
  → Alerta 60 dias antes da CNH vencer
  → Controle de diárias ou percentual combinado
  → Histórico de pagamentos
  → "João está rodando 20% menos que a média nos últimas 2 semanas"
```

**Regras de negócio configuráveis:**
```
Modelo de repasse:
  → Diária fixa: R$80/dia, motorista fica com o resto
  → Percentual: dono fica com 40%, motorista com 60%
  → Misto: diária + percentual acima de meta

Cálculo automático no fechamento semanal:
  → Quanto cada motorista recebe
  → Geração do comprovante de pagamento (PIX automático futuro)
```

---

### Módulo 5 — Fiscal e MEI

**A situação atual:**
Maioria dos motoristas de aplicativo deveria ser MEI mas não é,
ou é MEI mas não paga o DAS, ou é MEI mas está próximo de estourar o limite
de R$81k sem saber.

```
Ações automáticas:
  → Acompanha faturamento acumulado no ano
  → Alerta quando atingir 70%, 90% e 100% do limite MEI (R$81k)
  → Recomenda: "Com esse ritmo, você vai estourar o MEI em agosto.
    Hora de falar com um contador sobre migrar para ME."
  → Gera guia DAS mensalmente e alerta no vencimento
  → Calcula o quanto de imposto pagou no ano (para IRPF)
  → Conecta com MEI Automatizado (produto do portfólio) para
    emissão de nota fiscal quando necessário (frete, pessoa jurídica)
```

---

## Arquitetura Técnica

```
INTEGRAÇÕES
  → Open Finance: identifica receitas e despesas automaticamente
  → Uber Driver API / 99 Pro API: extrato de corridas (parceria ou scraping)
  → WhatsApp Business API: alertas de manutenção + relatório semanal

CORE
  → Motor de cálculo de custos por km
  → Algoritmo de depreciação por modelo/ano/km
  → Agenda de manutenção por modelo de veículo (base de dados tabela FIPE + specs)
  → Dashboard de inteligência de horários (ML sobre histórico do próprio motorista)

STACK
  → Mobile first: React Native (iOS + Android)
  → Backend: Node.js + PostgreSQL
  → Notificações: WhatsApp API (mais usado que push notification por esse público)
  → Pagamentos: Asaas (cobrança recorrente da assinatura)
```

---

## Modelo de Receita

| Plano | Para quem | Preço |
|-------|-----------|-------|
| **Free** | Motorista solo, controle básico | R$0 |
| **Pro** | Motorista solo, controle completo | R$19,90/mês |
| **Frota** | Dono de 2-10 carros | R$59,90/mês |
| **Frota Grande** | 10+ carros | R$149/mês |

**Receitas adicionais:**
- Comissão de oficinas parceiras: 10% por serviço agendado
- Seguro auto: comissão de indicação (R$200-400/apólice)
- Financiamento de veículo: comissão de lead para banco parceiro
- Marketplace de peças: parceria com AutoZone, Leroy, distribuidoras

**Projeção conservadora:**
```
Brasil: 1,5M motoristas ativos de Uber + 99
Conversão para Pro (2%): 30.000 motoristas × R$19,90 = R$597k/mês
Frota (0,5%): 7.500 donos × R$59,90 = R$449k/mês
Total assinatura: ~R$1M/mês no ano 2
+ Receitas de oficinas e seguros: R$200-400k/mês
```

---

## Distribuição

**Canal 1: Grupos de WhatsApp e Telegram de motoristas**
Existem centenas de grupos com 200-500 motoristas cada.
Esses grupos são ativos — compartilham informação de radar,
eventos, promoções de combustível. Um produto útil se espalha
naturalmente nesses grupos.

**Canal 2: YouTube e TikTok de motoristas de app**
Existe um ecossistema de criadores de conteúdo focados em
motoristas de Uber/99 com 100k-500k seguidores.
Parceria com esses criadores = acesso direto à base.

**Canal 3: Postos de combustível (GO + DF)**
O posto é onde o motorista vai todo dia. Parceria com postos
para oferecer o app no momento do abastecimento.
"Abasteceu? Registra no Volante."

**Canal 4: Oficinas mecânicas parceiras**
Oficina entra na rede de parceiros → recomenda o app para os
motoristas que chegam para manutenção → motorista baixa o app
no momento em que mais sente a dor (gastando dinheiro com manutenção).

---

## Por Que o Timing É Certo

```
1. Uber e 99 abriram APIs para parceiros em 2023 — dados de corridas
   acessíveis programaticamente pela primeira vez

2. Open Finance fase 3 (2023): banco identifica automaticamente
   receitas e despesas — custo de registro cai para zero

3. PIX: motoristas já recebem por PIX das apps — transações identificáveis

4. Crescimento do mercado: número de motoristas de app cresceu 40%
   pós-pandemia e ainda cresce

5. Consolidação: motoristas que sobreviveram são os mais profissionais —
   exatamente o perfil que paga por ferramenta de gestão
```

---

## Nome e Posicionamento

**Nome: Volante**
O volante é o instrumento de controle do carro — e da carreira.
"Estar no volante" em português tem duplo sentido: estar dirigindo
e estar no controle. É o nome perfeito para um produto de gestão
para motoristas.

Alternativas: **Corrida** / **KM** / **Rodou** / **Painel**

**Posicionamento:**
> *"Você sabe quanto recebeu. O Volante te mostra quanto você lucrou."*

Essa frase resolve o produto inteiro. A dor é real, universal
entre os motoristas, e o Volante é a resposta direta.

---

## Conexão com o Portfólio

```
Motorista usa Volante para gestão
  ↓
MEI Automatizado: paga o DAS, emite nota quando necessário
  ↓
Amparo (INSS): verifica se está contribuindo corretamente
  (motorista de app tem regras específicas de INSS)
  ↓
DoNotPay (Contesto): contesta multas de trânsito automaticamente
  (motorista tem alto volume de multas)
  ↓
Defesa de Frotas: para o dono com 5+ carros
```

O motorista de aplicativo é o cliente que mais se beneficia
de ter todos os produtos do portfólio — e cada produto vende o próximo.
