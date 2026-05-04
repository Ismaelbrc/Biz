# AgroBack — Plataforma Fiscal e Regulatória para o Produtor Rural

Back-office completo do produtor rural brasileiro: nota fiscal, contabilidade,
impostos, CAR e crédito — tudo integrado, tudo automatizado.

---

## O Problema que Ninguém Resolveu

O mercado de software para o agro está lotado de produtos sobre o campo:
drone, mapa de solo, irrigação, manejo de gado, previsão de safra.

Ninguém construiu o back-office fiscal do produtor rural.

E esse back-office é obrigatório, complexo, caro, e completamente manual hoje:

```
Produtor rural típico em GO (500 hectares, soja + gado):

→ Emite nota fiscal do produtor em bloco de papel
→ Leva o bloco para o contador da cidade uma vez por mês
→ Contador faz o Livro Caixa manualmente
→ Em setembro: faz a declaração do ITR sem saber se está pagando certo
→ Em março: faz o IRPF rural sem saber se compensa abrir empresa
→ Paga Funrural sobre cada venda sem saber se tem créditos
→ Quando vai pedir crédito rural: passa semanas juntando documentos
→ CAR: fez sozinho no SICAR, provavelmente errado
```

Resultado: produtor paga mais imposto do que deve, perde crédito rural por
documentação irregular, e gasta R$3.000-8.000/ano com contador que faz tudo
da mesma forma que fazia em 1995.

---

## Os Módulos da Plataforma

### Módulo 1 — Nota Fiscal do Produtor Rural

**O cenário atual:**
- A maioria dos estados ainda usa bloco de notas físico (NFPR em papel)
- Goiás tem NF-e Produtor Rural eletrônica, mas adoção baixa
- Quando o produtor vende para cooperativa ou trading, o comprador emite
  a nota em nome do produtor — e o produtor perde o controle dos dados

**O que automatiza:**
```
Produtor registra a venda: produto, quantidade, comprador, valor
  ↓
Plataforma emite NF-e Produtor Rural (para GO e estados com sistema eletrônico)
  ou gera o preenchimento do bloco físico com todos os campos corretos
  ↓
Dados da venda alimentam automaticamente:
  → Livro Caixa (receita do mês)
  → Cálculo do Funrural devido
  → Controle de faturamento anual (limite do segurado especial)
  → Histórico de vendas para declaração de ITR e IRPF
```

**Por que importa:** cada venda não registrada corretamente é:
- Receita não documentada = problema no IRPF
- Funrural não calculado = passivo fiscal silencioso
- Dado perdido = impossível reconstruir o Livro Caixa no final do ano

---

### Módulo 2 — Livro Caixa Automatizado

O Livro Caixa é o coração da contabilidade do produtor rural pessoa física.
Toda despesa com a atividade rural é dedutível do IRPF — mas só se estiver documentada.

**O que automatiza:**
```
Receitas (automático):
  → Importa as NF-e emitidas/recebidas
  → Integra com banco via Open Finance (depósitos identificados como venda)
  → Cooperativa envia extrato de conta corrente? Plataforma importa

Despesas (semi-automático):
  → Produtor fotografa NF de insumo, combustível, maquinário
  → OCR extrai: valor, fornecedor, data, categoria
  → Plataforma categoriza: despesa operacional, investimento, custeio

Decisão inteligente:
  → Calcula mensalmente: vale mais deduzir despesas reais
    ou usar os 20% de dedução presumida?
  → Alerta quando a dedução real vai superar os 20%
    (sinal para guardar todos os comprovantes)
  → Projeta o imposto de renda do ano com base no resultado atual
```

---

### Módulo 3 — ITR Automatizado

O ITR (Imposto Territorial Rural) é declarado anualmente até setembro.
A maioria dos produtores paga mais do que deve porque não declara corretamente
o grau de utilização da terra.

**Como o ITR funciona:**
- Alíquota varia de 0,03% a 20% dependendo do tamanho e do GU (Grau de Utilização)
- GU = área produtiva ÷ área aproveitável
- Quanto maior o GU → menor a alíquota → menos imposto
- Propriedades improdutivas pagam até 20x mais que produtivas

**O que automatiza:**
```
Integra dados do CAR (área total, uso do solo, vegetação)
  + dados do INCRA (matrícula, módulos fiscais)
  + histórico de produção do Livro Caixa
  ↓
Calcula o GU real da propriedade
  ↓
Simula: "Com GU de X%, você paga R$Y. Declarando a pastagem X
  como área aproveitável, o GU sobe para Z% e você paga R$W."
  ↓
Preenche e envia a DITR automaticamente
  ↓
Monitora prazo (vence em setembro) e emite DARF de pagamento
```

**Impacto típico:** produtor que paga R$2.000/ano de ITR pode reduzir para
R$400-800 só pela correta declaração do GU. A plataforma se paga na primeira declaração.

---

### Módulo 4 — Funrural

Funrural é a contribuição previdenciária do produtor rural: 1,5% sobre
a receita bruta de cada venda (ou 1,2% + 0,1% RAT se optar pelo CNPJ).

**Problemas mais comuns:**
- Produtor paga Funrural via cooperativa mas não sabe o total acumulado
- Produtor pessoa física que deveria ser segurado especial (família, < R$500k/ano)
  às vezes paga Funrural desnecessariamente
- Créditos de Funrural por pagamento indevido: muitos produtores têm créditos
  que nunca solicitaram

**O que automatiza:**
```
Calcula Funrural sobre cada NF de venda emitida
  ↓
Verifica: produtor se qualifica como segurado especial?
  (atividade em regime familiar, área < 4 módulos fiscais, < R$500k/ano)
  → Se sim: alerta que pode não precisar pagar Funrural
  → Se não: emite guia de recolhimento automaticamente
  ↓
Monitora créditos acumulados (casos de recolhimento indevido)
  → Se há crédito: inicia processo de compensação ou restituição
```

---

### Módulo 5 — IRPF Rural

O produtor rural pessoa física declara sua atividade no quadro de Atividade Rural
do IRPF. É o módulo mais complexo — e onde mais dinheiro é perdido.

**As regras específicas da atividade rural:**
- Resultado positivo (lucro) é tributável progressivamente
- Resultado negativo (prejuízo) pode ser compensado nos próximos 4 anos
- Investimentos em terra, benfeitorias, máquinas são dedutíveis
- Subvenções e incentivos do governo são tributáveis

**O que automatiza:**
```
Consolida o Livro Caixa do ano
  ↓
Calcula o resultado da atividade rural (receita - despesa)
  ↓
Aplica compensações de prejuízos de anos anteriores
  ↓
Simula: vale manter como PF ou migrar para PJ (empresa rural)?
  → PF: alíquota progressiva de até 27,5%
  → PJ Simples/Lucro Presumido: pode ser 6-15% dependendo do caso
  ↓
Preenche o quadro de Atividade Rural na declaração de IRPF
  e exporta para o programa da Receita Federal
```

---

### Módulo 6 — CAR + Regularização

Importado diretamente do produto CAR Rural — aqui é a espinha dorsal
que conecta os outros módulos:

```
CAR define: área total, APP, Reserva Legal, uso do solo
  ↓ alimenta
ITR: GU calculado com base nas áreas do CAR
  ↓ alimenta
Crédito Rural: CAR em dia = acesso a PRONAF/PRONAMP
  ↓ monitora
Alertas: "Seu CAR está em análise há X meses — isso pode bloquear seu crédito"
```

---

### Módulo 7 — Painel de Crédito Rural

O crédito rural (PRONAF, PRONAMP, ABC, Custeio, Investimento) exige uma
pilha de documentos que o produtor sempre deixa vencer ou não tem em mãos
quando precisa. Resultado: perde a safra do crédito subsidiado e vai para
o crédito caro.

**O que faz:**
```
Dashboard com semáforo de cada documento necessário:
  → CAR: ✅ válido / ⚠️ em análise / ❌ irregular
  → DAP/CAF (agricultor familiar): ✅ válida / ⚠️ vence em X meses
  → Certidão negativa Receita Federal: ✅ / ❌ vencida
  → Certidão negativa trabalhista: ✅ / ❌
  → ITR em dia: ✅ / ❌ DARF pendente
  → Funrural em dia: ✅ / ❌
  → Matrícula do imóvel atualizada: ✅ / ⚠️ verificar

Alerta 90 dias antes de qualquer documento vencer
Gera automaticamente: certidões negativas, DARF de regularização
Conecta com banco via Open Finance: vê o extrato rural separado
```

---

## Arquitetura de Integração

```
                    ┌─────────────────────────────┐
                    │      AGROBACK PLATFORM       │
                    └─────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
    ┌─────────┐         ┌──────────┐         ┌──────────┐
    │ RECEITAS│         │ IMPOSTOS │         │ CRÉDITO  │
    │         │         │          │         │          │
    │ NF-e    │         │ ITR auto │         │ Painel   │
    │ Produtor│         │ Funrural │         │ Docs     │
    │ Open    │         │ IRPF     │         │ CAR      │
    │ Finance │         │ Rural    │         │ DAP/CAF  │
    └─────────┘         └──────────┘         └──────────┘
         │                    │                    │
         └────────────────────▼────────────────────┘
                         ┌──────────┐
                         │ LIVRO    │
                         │ CAIXA    │
                         │ (centro) │
                         └──────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
         Receita          Banco do        Cooperativa
         Federal          Brasil Open     (extrato)
         (IRPF/ITR)       Finance
```

---

## Quem É o Cliente

**Perfil primário: Produtor médio**
- 100-2.000 hectares
- Soja, milho, gado, ou combinação
- Fatura R$300k-5M/ano
- Tem contador mas sabe que ele não é especialista em agro
- Perde crédito todo ano por documentação irregular
- Paga mais ITR do que deveria

**Perfil secundário: Pequeno produtor / agricultor familiar**
- Até 4 módulos fiscais
- Fatura até R$500k/ano
- Pode ser segurado especial — não sabe
- Usa cooperativa como intermediário para tudo
- Preço sensível — precisa de solução barata

**Perfil terciário: Contador rural (B2B)**
- Contador generalista em cidade do interior que atende 30-50 produtores
- Quer uma ferramenta para organizar seus clientes
- Hoje usa Excel + sistema genérico de contabilidade
- Pagaria R$500-2.000/mês por uma plataforma que acelere seu trabalho

---

## Modelo de Receita

| Plano | Para quem | Preço |
|-------|-----------|-------|
| Família | Até 4 módulos fiscais | R$49/mês |
| Produtor | 100-500 ha | R$149/mês |
| Fazenda | 500-2.000 ha | R$299/mês |
| Grande | 2.000+ ha | R$499/mês |
| Contador Pro | Gerencia até 20 clientes | R$799/mês |
| Cooperativa | Gerencia toda a base de sócios | Sob consulta |

**Receitas adicionais:**
- ITR: cobrar R$99 pela declaração anual além da assinatura (upsell pontual)
- CAR: R$399-999 por regularização (produto standalone que vira módulo)
- Crédito: comissão de indicação para bancos parceiros (R$200-500 por crédito aprovado)

**LTV típico:**
- O produtor rural não troca de contador fácil — churn histórico de contabilidade rural é < 5%/ano
- Assinatura de R$149/mês × 12 meses × 10 anos = R$17.880 de LTV sem upsell

---

## Distribuição — O Diferencial

Software para produtor rural não se vende pela internet. Se vende pelo canal certo.

**Canal 1: Cooperativas (maior prioridade)**
COMIGO, Cooperativa dos Cafeicultores, Coopego, Primavera Cooperativa em GO.
A cooperativa já tem:
- Relacionamento de confiança com cada sócio
- Estrutura de assistência técnica que visita as propriedades
- Interesse em ter os dados fiscais dos sócios organizados (para análise de crédito)
Modelo: cooperativa licencia a plataforma e oferece como benefício ao sócio.
Preço: R$2.000-10.000/mês para a cooperativa (ela distribui gratuitamente para os sócios).

**Canal 2: Contadores rurais**
Cada cidade do interior de GO tem 2-5 contadores que atendem produtores rurais.
Eles querem uma ferramenta — hoje usam Excel e Domínio/Totvs genérico.
Modelo: B2B2C — contador usa para gerir seus clientes, clientes ficam na plataforma.

**Canal 3: Banco do Brasil / Sicoob / Sicredi**
Gerentes de crédito rural no BB indicam a plataforma quando o produtor vai pedir
financiamento e não tem documentação em dia.
"Para liberar seu PRONAF, precisa regularizar o CAR e o ITR. Usa o AgroBack."

**Canal 4: Revenda de insumos**
O agrônomo da revenda que vende semente e adubo visita cada produtor.
Ele já é o consultor de confiança. Adicionar a recomendação da plataforma é natural.

---

## Por Que GO é o Mercado de Entrada

```
400.000 propriedades rurais
Cooperativas fortes (COMIGO é referência nacional)
Infraestrutura de NF-e Produtor Rural já existe
Goiânia: hub de agronegócio com contadores, advogados, bancos rurais
BR-060 e BR-153: corredor logístico do agro nacional passando por GO
Integração natural com CAR Rural (produto que já mapeamos para GO)
```

---

## Nome e Posicionamento

**Candidatos:**

| Nome | Lógica |
|------|--------|
| **Campo Certo** | Campo (rural) + Certo (correto, justo) — simples, direto |
| **TerraFisco** | Terra (rural) + Fisco (fiscal) — técnico, B2B |
| **Safra Contábil** | Safra (harvest) + contábil — descritivo demais |
| **Raíz** | Raiz de tudo, profundidade, rural — poético mas pode confundir |
| **CampoDoc** | Campo + documentação — funcional, sem personalidade |
| **Grão** | Minimalista, mas genérico |

**Recomendação: Campo Certo**

É o nome que um produtor rural de Jataí-GO entende na primeira vez.
Não precisa de explicação. Resolve o problema embutido no nome:
fazer tudo certo no campo.

> *"Campo Certo. O back-office do produtor rural."*

---

## O Insight Mais Importante

A maioria dos softwares para agro quer ser a ferramenta do dia a dia do produtor
no campo — mapa de solo, app de safra, rastreamento de máquina.

Campo Certo não compete com isso.

Campo Certo é o que acontece quando o produtor vende a safra e precisa
declarar o imposto. Quando o banco pede o CAR e está irregular. Quando o
contador manda a nota e o produtor não entende por que pagou R$4.000 de ITR.

É a plataforma que ninguém construiu porque é chata demais —
e por isso é a mais necessária.
