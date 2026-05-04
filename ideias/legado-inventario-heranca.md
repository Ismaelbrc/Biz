# Legado — Plataforma de Inventário e Herança

Dois produtos integrados: cofre digital de patrimônio (pré-morte)
e inventário automatizado (pós-morte).

---

## O Problema Real

O inventário é o processo jurídico mais evitado, mais caro e mais demorado
que uma família média vai enfrentar. E quase ninguém se prepara para ele.

```
O que acontece quando alguém morre sem planejamento:

Semana 1:
  "Onde estão os documentos do apartamento?"
  "Ele tinha conta em qual banco? Quantas contas?"
  "E as ações na corretora? Ele tinha, né?"
  "O FGTS — quem tem direito?"

Meses 1-3:
  Família peregrina por bancos, cartórios, DETRAN, Receita Federal
  Tentando descobrir o que o falecido tinha

Meses 3-12:
  Contratar advogado (2-6% do valor do espólio)
  Reunir 40-80 documentos de fontes diferentes
  Calcular e pagar ITCMD (4-8% do patrimônio, dependendo do estado)
  Agendar e ir ao cartório (inventário extrajudicial)
  Ou: esperar anos na fila do tribunal (inventário judicial)

Anos 1-4+:
  Transferir cada bem para o nome dos herdeiros
  DETRAN, cartório de imóveis, cada banco, cada corretora

Custo total: R$15.000-80.000
Tempo: 2-4 anos para a maioria dos casos
```

**O dado que define a oportunidade:**
Desde 2007, qualquer inventário com herdeiros maiores, em acordo,
sem menor e sem testamento contestado pode ser feito em cartório
em 30-90 dias. Menos de 20% dos inventários usam essa via.
O restante vai para o judiciário — não por necessidade, mas por desconhecimento.

---

## Dois Produtos: Cofre + Inventário

```
PRÉ-MORTE                          PÓS-MORTE
─────────────────────────────────────────────────────
COFRE DIGITAL                      INVENTÁRIO ASSISTIDO
(produto de recorrência)           (produto de ticket alto)

Organiza o patrimônio              Executa o inventário
em vida para os herdeiros          quando a morte ocorre

Receita: R$29/mês                  Receita: R$1.999-4.999
Mercado: qualquer adulto           Mercado: famílias com inventário aberto
com patrimônio                     (1,4M mortes/ano)

LTV: R$3.480 (10 anos)            One-time de alto valor
```

---

## Produto 1: Cofre Digital

**O que é:**
Vault digital onde a pessoa registra toda a sua vida financeira
para que os herdeiros encontrem tudo no momento da morte.

**Por que existe:**
A maioria das pessoas não deixa mapa do seu patrimônio.
Os herdeiros descobrem as contas bancárias pela fatura do cartão.
Descobrem o imóvel pelo IPTU que chega pelo correio.
As ações na corretora? Muitas ficam esquecidas para sempre.

```
O que o cofre registra:

PATRIMÔNIO
  Imóveis: endereço + matrícula + cartório + valor estimado
  Veículos: placa + RENAVAM + financiamento pendente?
  Contas bancárias: banco + agência + conta + tipo
  Investimentos: corretora + tipo + valor aproximado
  Previdência privada: PGBL/VGBL + seguradora + beneficiários
  Seguros de vida: seguradora + número da apólice + beneficiários
  Participação em empresas: CNPJ + % + qual cartório tem o contrato social
  Imóveis rurais: matrícula + cartório + CAR + tamanho

DÍVIDAS
  Financiamentos: banco + saldo devedor + prazo + bem vinculado
  Cartões de crédito: limites e saldos aproximados
  Outros: consórcio ativo, empréstimos pessoais

DOCUMENTOS DIGITAIS
  Certidão de nascimento, casamento, divórcio
  Escrituras de imóveis
  CRLV de veículos
  Contratos de investimento
  Apólices de seguro
  Testamento (se tiver)

INFORMAÇÕES PRÁTICAS
  Contato do contador, advogado, corretor de seguros
  Senhas (vault criptografado separado)
  Instruções: "se algo acontecer comigo, contate X primeiro"
  Localização de documentos físicos importantes
```

**Acesso de emergência:**
```
O titular define quem pode pedir acesso em caso de morte.

Processo de desbloqueio:
  → Herdeiro apresenta certidão de óbito
  → Plataforma verifica via API do RCPN (Registro Civil)
  → Envia notificação para todos os outros herdeiros cadastrados
  → Após 72h sem contestação: libera acesso ao cofre
  → Herdeiros veem o mapa completo do patrimônio

Sem esse cofre: meses de peregrinação por instituições
Com esse cofre: 72h para ter visão completa do patrimônio
```

**Modelo de receita:**
- R$29/mês por titular
- R$249/ano (desconto de 28%)
- Gratuito para maiores de 70 anos com patrimônio declarado acima de R$200k
  (aquisição: eles indicam os filhos que pagam a assinatura)

---

## Produto 2: Inventário Assistido

### Fase 1 — Diagnóstico (gratuito)

```
5 perguntas que definem o caminho:
  1. Há herdeiros menores de 18 anos? (judicial obrigatório se sim)
  2. Todos os herdeiros estão em acordo? (judicial se não)
  3. Há testamento? (judicial se testamento contestado)
  4. O falecido tinha dívidas que podem superar o patrimônio? (alerta)
  5. Há imóvel rural acima de determinado valor? (ITCMD progressivo)

Resultado:
  → Extrajudicial (cartório): caminho A — mais rápido e barato
  → Judicial obrigatório: caminho B — referral para advogado
  → Caso complexo: avaliação com especialista
```

### Fase 2 — Descoberta de Ativos

**O maior problema dos inventários é não saber o que existe.**
A plataforma automatiza a busca em todas as fontes:

```
BUSCA AUTOMÁTICA (via CPF do falecido):

Receita Federal:
  → Última declaração de IR (lista todos os bens declarados)
  → CNPJ vinculados (era sócio de alguma empresa?)
  → Pendências fiscais que vão para o espólio

DETRAN:
  → Veículos registrados no CPF
  → Licenciamento em dia? Débitos de multa?
  → Financiamento ativo? (bem não pode ser transferido com financiamento)

Cartório de Imóveis (via CNJ e-Notariado):
  → Imóveis registrados no CPF
  → Ônus reais (hipoteca, penhora, usufruto)
  → Qual cartório tem a matrícula

INCRA / SNCR:
  → Imóveis rurais registrados

SISBACEN (Banco Central):
  → Lista de instituições financeiras onde o CPF tem relacionamento
  → (Não mostra saldo — abre o caminho para cada banco)

CEF (via Gov.br API):
  → FGTS: saldo a ser recebido pelos herdeiros
  → PIS/PASEP: saldo esquecido

INSS:
  → O falecido recebia benefício? (dependentes têm direito a pensão por morte)
  → Quem são os dependentes cadastrados?

B3 (via Receita Federal):
  → Investimentos declarados em renda variável
  → Custódia de ações e fundos

Seguradoras (via SUSEP):
  → Apólices de seguro de vida (beneficiários recebem fora do inventário)
  → Previdência privada (PGBL/VGBL: pode ou não entrar no inventário)
```

**Output da fase de descoberta:**
```
RELATÓRIO DE ATIVOS DO ESPÓLIO
─────────────────────────────────────────────────
BENS IDENTIFICADOS:
  Apartamento Rua X, Goiânia     R$ 380.000
  Veículo Toyota Corolla 2019    R$  68.000
  Conta BB Agência 1234          R$  23.400 (estimado)
  Ações XP Investimentos         R$  41.200 (último IR)
  FGTS                           R$  12.800
  
TOTAL ESTIMADO DO ESPÓLIO:       R$ 525.400

ITCMD ESTIMADO (GO, 4%):         R$  21.016
CUSTAS DE CARTÓRIO (estimado):   R$   3.200
HONORÁRIOS PLATAFORMA:           R$   3.500

ATENÇÃO:
  → Veículo tem financiamento ativo (R$18.000)
  → Apartamento tem IPTU em atraso (consultar prefeitura)
  → INSS: o falecido pode ter dependente com direito a pensão
─────────────────────────────────────────────────
```

### Fase 3 — Coleta de Documentos

**O checklist inteligente:**
```
Não é uma lista genérica — é personalizada para este espólio específico.

DOCUMENTOS DO FALECIDO:
  ✅ Certidão de óbito (obtida)
  ✅ CPF e RG (obtidos)
  ⬜ Certidão de casamento (pendente)
  ⬜ Escritura do apartamento (pendente — qual cartório tem?)

DOCUMENTOS DOS HERDEIROS:
  ✅ RG e CPF de todos (obtidos)
  ⬜ Certidão de nascimento dos filhos (pendente)

CERTIDÕES NEGATIVAS:
  ⬜ CND Receita Federal
  ⬜ CND Estadual (SEFAZ-GO)
  ⬜ CND Municipal (Prefeitura Goiânia)
  ⬜ CND Trabalhista (TST)

POR BEM:
  Apartamento:
    ⬜ Matrícula atualizada (cartório de imóveis)
    ⬜ Certidão de ônus reais
    ⬜ Declaração de valor venal (Prefeitura)
    ⬜ Certidão negativa de IPTU
  
  Veículo:
    ⬜ CRLV atual
    ⬜ Certidão de quitação do financiamento (banco)
    ⬜ ATPV assinado
```

**Para cada documento pendente:**
- Instrução de como obter (onde ir, o que levar, custo)
- Link para o sistema online quando existir
- Geração automática de carta/ofício quando a instituição exigir solicitação formal
- Upload e armazenamento seguro quando obtido

### Fase 4 — Cálculo e Planejamento do ITCMD

**ITCMD = o imposto que mais surpreende os herdeiros.**

```
Goiás: 4% sobre o valor total do espólio
DF: 4% sobre o valor total do espólio
São Paulo: 4% (mas há projetos de lei para aumentar para 8%)
Bahia: progressivo até 8%
```

**O que a plataforma calcula:**
```
Cenário A — partilha igualitária:
  Espólio: R$525.400
  ITCMD: R$21.016 (4% de R$525.400)
  Cada herdeiro paga: R$7.005 (3 filhos)

Cenário B — otimização por tipo de bem:
  Imóvel vai para herdeiro A (residente em GO, isenção parcial?)
  Veículo vai para herdeiro B (menor valor, menor imposto)
  Investimentos liquidados, saldo dividido igualitariamente
  ITCMD total: R$19.840 (R$1.176 de economia com planejamento)

Isenções aplicáveis:
  → GO: imóvel único de valor até R$100.000 pode ter isenção
  → Verificar se algum herdeiro é cônjuge (regime de comunhão)
  → FGTS e seguro de vida: entram ou não entram no ITCMD?
    (depende do estado — em GO, seguro de vida pago a beneficiário
    não integra o espólio e não paga ITCMD)
```

**Geração automática da DARE (guia de pagamento do ITCMD):**
```
Calcula o valor correto para cada herdeiro por cada bem
Gera o DARE no padrão da SEFAZ-GO ou SEFAZ-DF
Acompanha o prazo (ITCMD deve ser pago antes da lavratura da escritura)
```

### Fase 5 — Minuta da Escritura

**O trabalho mais caro do advogado — e o mais automatizável:**

```
A plataforma gera a minuta completa da escritura de inventário e partilha:

  → Qualificação completa de todos os herdeiros
  → Descrição jurídica de cada bem (matrícula, RENAVAM, CNPJ etc.)
  → Declaração de inexistência de outros bens/dívidas
  → Partilha detalhada (quem recebe o quê)
  → Cálculo do ITCMD pago
  → Referência às certidões negativas

Advogado parceiro recebe a minuta pronta:
  → Revisa (1-2h de trabalho vs. 8-10h para elaborar do zero)
  → Assina digitalmente (obrigatório mesmo no extrajudicial)
  → Honorário reduzido: R$1.500-2.500 (vs. R$8.000-25.000 tradicional)

A plataforma agenda o cartório via e-Notariado.
```

### Fase 6 — Transferência dos Bens

**Depois da escritura lavrada: cada bem precisa ser transferido individualmente.**

```
IMÓVEL:
  → Gera requerimento para o cartório de imóveis
  → Calcula custo de registro da transferência
  → Acompanha até o novo registro em nome dos herdeiros

VEÍCULO:
  → Gera ATPV (Autorização de Transferência de Propriedade do Veículo)
  → Orienta sobre o processo no DETRAN GO/DF
  → Integração com Contesto (DoNotPay) para quitar multas pendentes antes da transferência

CONTAS BANCÁRIAS:
  → Gera ofício personalizado para cada banco
  → Instrução de como cada banco processa o desbloqueio
  → Cada banco tem seu processo (BB, CEF, Itaú, Bradesco, Nubank)

INVESTIMENTOS:
  → Instrução específica para cada corretora/gestora
  → XP, BTG, Clear, Rico, Tesouro Direto — cada um diferente

FGTS:
  → Requerimento à CEF com toda a documentação
  → Prazo legal: 30 dias após protocolo
```

---

## Inventário Judicial — O Referral

Quando o caso não é elegível para extrajudicial:
```
Plataforma faz:
  → Levantamento completo de ativos (igual ao extrajudicial)
  → Organização de toda a documentação
  → Resumo do caso para o advogado (economiza 3-5h de reunião inicial)
  → Cálculo de ITCMD

Referral para advogado de inventário parceiro:
  → Plataforma entrega o caso já instruído
  → Advogado cobra honorários menores (trabalho inicial já feito)
  → Split: 25% para a plataforma do honorário total
  → Honorário típico de inventário judicial: R$8.000-30.000
  → Receita da plataforma: R$2.000-7.500 por referral
```

---

## Foco em GO — Inventário Rural

**O maior case específico para Goiás:**

Fazendas sendo transferidas entre gerações. Produtor rural morre
sem sucessão planejada — família brigando por fazenda de R$3-8M
por anos enquanto a propriedade se deprecia e a safra é perdida.

```
Especificidades do inventário rural em GO:

CAR: precisa estar regularizado antes da transferência
  → Integração com o produto CAR Rural do portfólio

ITR: declarações dos últimos 5 anos precisam estar em dia
  → Integração com Campo Certo

Valor da fazenda: ITCMD calculado sobre valor de mercado
  → Para R$5M de fazenda: R$200k de ITCMD (4%)
  → Planejamento pode reduzir via doação em vida com usufruto

INCRA: imóvel rural precisa de certificação
  → Georreferenciamento (se não tiver)
  → Atualização no SNCR

Módulos fiscais: determina se é pequena propriedade
  → Afeta ITCMD (isenções para propriedade familiar em alguns estados)

Contrato de arrendamento vigente: herdeiros assumem
  → Precisa ser renegociado ou mantido

Dívidas rurais: financiamentos no BB Agro, BNDES
  → Bens vinculados não podem ser partilhados com dívida ativa
  → Processo de quitação ou assunção de dívida pelos herdeiros
```

**Produto específico: Sucessão Rural**
```
Para fazendeiros que querem planejar a sucessão em vida:

Doação com usufruto:
  → Doa a fazenda aos filhos em vida
  → Mantém o usufruto (usa e colhe os frutos até morrer)
  → Paga ITCMD agora (menor porque valor da fazenda é menor + usufruto deduz)
  → Herdeiros recebem a propriedade sem inventário na morte

Holding familiar rural:
  → Transfere a fazenda para uma empresa (holdings são comuns no agro)
  → Quotas da empresa são mais fáceis de dividir
  → Evita o processo de inventário do imóvel

Testamento rural:
  → Muito raro em GO mas extremamente recomendável para fazendas
  → Plataforma gera o testamento e orienta sobre cartório de notas
```

---

## Modelo de Receita Completo

| Produto | Preço | Quando |
|---------|-------|--------|
| Cofre Digital | R$29/mês | Recorrente |
| Inventário Extrajudicial | R$2.499 fixo | One-time |
| Inventário Judicial (referral) | 25% do honorário | Por caso |
| Sucessão Rural | R$1.499 | One-time + assinatura |
| ITCMD Optimization | R$499 | Upsell para espólios > R$500k |

**Projeção por funil:**
```
Brasil: 1,4M mortes/ano
GO + DF: ~70.000 mortes/ano
Com patrimônio relevante (>R$100k): ~35.000 famílias/ano em GO+DF
Conversão de 5%: 1.750 inventários/ano
Ticket médio: R$2.499 (extrajudicial) + R$800 de upsells
Receita inventários: R$5,8M/ano (GO+DF em maturidade)

Cofre Digital:
  50.000 assinantes × R$29/mês = R$1,45M/mês
```

---

## Risco Jurídico — Como Estruturar

**Advocacia é obrigatória no inventário extrajudicial:**
A lei exige que um advogado assine a escritura — não pode ser a plataforma.

**Estrutura correta:**
```
Plataforma (Legado):
  → Faz tudo que é tecnologia: descoberta de ativos, checklist,
    coleta de documentos, cálculo de ITCMD, geração de minuta

Advogado parceiro:
  → Revisa a minuta (1-2h de trabalho)
  → Assina digitalmente
  → Comparece ao cartório (ou assina remotamente via e-Notariado)
  → Cobra honorário fixo acordado com a plataforma: R$1.500-2.500
    (vs. R$8.000-25.000 que cobraria se fizesse tudo do zero)

Cartório:
  → Lavra a escritura
  → Cobra as custas tabeladas (R$1.500-3.500 dependendo do estado/valor)

Usuário paga:
  → Plataforma: R$2.499
  → Advogado parceiro: R$1.500-2.500
  → Cartório: R$1.500-3.500
  → ITCMD: 4% do espólio
  Total: muito abaixo dos R$15.000-50.000 do processo tradicional
```

---

## Distribuição

**Canal 1: O Cofre como Aquisição**
Quem assina o Cofre em vida converte automaticamente para o Inventário
quando a morte ocorre — sem CAC adicional.

**Canal 2: Google (intenção de dor aguda)**
"Como fazer inventário em Goiás"
"Documentos para inventário"
"Quanto custa inventário"
Intenção claríssima, altíssimo valor de conversão.

**Canal 3: Cartórios de Notas como Parceiros**
O cartório já recebe a família no momento da morte.
Parceria: cartório indica a plataforma, recebe R$200-300 por conversão.

**Canal 4: Advogados de Família (rede de parceiros)**
Advogados que não são especializados em inventário indicam a plataforma
e recebem indicação reversa para os casos que a plataforma não consegue
resolver (judiciais complexos).

**Canal 5: Seguradoras e Previdência Privada**
Quando o seguro de vida é pago, a seguradora poderia indicar a plataforma
para ajudar a família com o inventário dos demais bens.

---

## Nome e Posicionamento

**Nome: Legado**

Legado é o que ficamos após partir. É o que os pais constroem para os filhos.
É uma palavra com peso emocional positivo — não evoca morte, evoca continuidade.
Simples de pronunciar, fácil de lembrar, domínio provável disponível.

Alternativas: **Partilha** (muito técnico) / **Herança** (genérico) /
**Espólio** (muito frio) / **Sucessão** (muito corporativo)

**Posicionamento:**
> *"Você passou a vida construindo.
> O Legado garante que chegue para quem você ama."*

Dois ângulos:
- Para quem planeja em vida (Cofre): paz de espírito
- Para herdeiros após a morte: clareza e agilidade no momento mais difícil
