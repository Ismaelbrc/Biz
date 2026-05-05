# Terceiro Lote: 10 Ideias — Direito e Desburocratização

Critério: dores reais do brasileiro, modelo de receita claro,
automação viável, não repete o que já está no portfólio.

---

## 1. Revisional de Financiamento
**Copycat de:** DoNotPay (EUA), várias fintechs de contestação de crédito

Brazil tem 60M+ operações de crédito ativas. Financiamentos de carro,
moto e imóvel frequentemente têm: IOF calculado errado, juros acima do
limite legal, seguros embutidos não solicitados, capitalização indevida
(anatocismo). O cliente assina sem entender — e paga mais anos pagando
um valor que não deveria.

**O que automatiza:**
- Usuário envia o contrato (foto ou PDF)
- IA extrai: taxa de juros, CET (Custo Efetivo Total), IOF cobrado, seguros
- Compara com: taxa máxima legal para a modalidade + tabela do BACEN
- Se houver irregularidade: calcula o valor cobrado a mais
- Gera petição para revisão judicial + executa via JEC (até R$20k) ou
  ação revisional em vara cível

**Modelo de receita:** success fee de 20-30% do valor recuperado
**Ticket típico:** R$2.000-15.000 por caso
**Mercado:** 60M contratos × taxa de irregularidade estimada de 15% = 9M casos potenciais

---

## 2. Plano de Saúde — Negativa de Cobertura
**Copycat de:** Appeal Health (EUA), Rightway (EUA)

Plano de saúde recusa cobrir cirurgia, exame, medicamento ou internação.
A ANS tem um Rol de Procedimentos que obriga os planos a cobrir — mas
os planos negam mesmo assim contando que o paciente não vai brigar.
Após decisão do STJ (2022), planos devem cobrir inclusive tratamentos
fora do Rol se houver indicação médica.

**O que automatiza:**
- Usuário descreve o procedimento negado + envia a negativa por escrito
- IA verifica: está no Rol da ANS? Há jurisprudência favorável?
- Gera: notificação extrajudicial ao plano (48h para resposta)
- Se não responder: peticiona na ANS + JEC simultaneamente
- Para casos urgentes (risco de vida): petição de tutela de urgência
  com prazo de 24h para cumprimento

**Modelo de receita:**
- Assinatura: R$29/mês (monitoramento + contestação ilimitada)
- Success fee para casos judiciais: 25% do valor do tratamento coberto

**Mercado:** 50M+ beneficiários de plano de saúde no Brasil.
Taxa de negativa estimada: 1 em cada 5 beneficiários por ano.

---

## 3. Calculadora de Rescisão — Direitos Trabalhistas
**Copycat de:** Gusto (EUA), Rippling — mas do lado do trabalhador

Trabalhador demitido recebe os valores na conta sem entender se está
correto. A maioria não sabe calcular: saldo de salário, aviso prévio
(proporcional ao tempo de serviço), 13º proporcional, férias + 1/3,
multa de 40% do FGTS, FGTS do mês de rescisão.

Empresas erram (ou fraudam) esses cálculos — especialmente em:
- Aviso prévio indenizado proporcional (1 dia por ano de serviço após o 1º)
- Férias vencidas em dobro quando não gozadas no período correto
- FGTS de empresas que declararam menos que o real

**O que automatiza:**
- Trabalhador informa: data de admissão, demissão, salário, tipo de rescisão
- Plataforma calcula o valor correto de cada verba rescisória
- Compara com o TRCT (Termo de Rescisão) assinado
- Se houver diferença > R$200: orienta sobre como cobrar
- Gera reclamação trabalhista simplificada para o CEJUSC (pré-judicial)
- Para valores > R$20k: referral para advogado trabalhista parceiro

**Modelo de receita:**
- Calculadora gratuita (aquisição)
- Recurso via CEJUSC: R$149 fixo
- Referral trabalhista: 25% do honorário do advogado

**Mercado:** 9M demissões formais por ano no Brasil.
Estimativa: 30% com alguma irregularidade no cálculo.

---

## 4. Consignado Indevido — INSS dos Idosos
**Copycat de:** sem equivalente direto — problema exclusivamente brasileiro

Fraude sistêmica: idosos têm empréstimos consignados descontados
diretamente do benefício do INSS sem ter contratado, ou foram induzidos
a contratar sem entender. O desconto some no extrato — muitos não percebem
por meses ou anos.

BACEN e INSS têm processos para contestar mas são complexos e lentos.

**O que automatiza:**
- Idoso (ou familiar) conecta o extrato do INSS via Gov.br
- IA identifica descontos de consignado: banco, valor, data de início
- Verifica se o contrato foi firmado dentro das regras (limites de idade,
  percentual máximo, banco autorizado pelo INSS)
- Se irregular: gera reclamação ao BACEN + INSS + boletim de ocorrência
  (se fraude) + ação de repetição de indébito no JEC
- Calcula: valor total descontado indevidamente = valor a recuperar

**Modelo de receita:** success fee de 25% do valor recuperado
**Ticket médio:** R$3.000-12.000 (meses de desconto indevido acumulados)
**Mercado:** estimativa de 3-5M idosos com algum consignado irregular

---

## 5. Alvará de Funcionamento Automatizado
**Copycat de:** Clerky (EUA), Harbor Compliance (EUA)

Todo negócio físico precisa de alvará de funcionamento da prefeitura.
O processo é diferente em cada município. Em Goiânia: CMEI, CEIC,
consulta de viabilidade, AVCB (corpo de bombeiros), licença sanitária se aplicável.

Pequenos empreendedores passam 3-6 meses nesse processo por falta
de orientação — muitas vezes abrem sem alvará e recebem autuação.

**O que automatiza:**
- Usuário informa: município, endereço, atividade (CNAE)
- Plataforma mapeia: quais licenças são necessárias, em qual ordem,
  quais documentos, qual o custo de cada taxa
- Gera: formulários pré-preenchidos para cada órgão
- Agenda: vistorias do corpo de bombeiros e vigilância sanitária onde aplicável
- Monitora: status de cada etapa
- Alerta: 60 dias antes de cada renovação anual

**Modelo de receita:**
- Alvará simples (comércio/serviço de baixo risco): R$349
- Alvará complexo (alimentação, saúde, educação): R$699
- Renovação anual monitorada: R$149/ano

**Mercado:** 3M+ novos CNPJs abertos por ano + 15M+ estabelecimentos
com alvará que precisam renovar anualmente.
**Foco GO + DF:** integração com Prefeitura de Goiânia e SEEC-DF desde o dia 1.

---

## 6. Portabilidade de Crédito Automatizada
**Copycat de:** Credible (EUA), LendingTree (EUA)

Todo brasileiro com empréstimo tem o direito de transferir para outro banco
com taxa menor (portabilidade de crédito — Resolução BACEN 4.292/2013).
Pouquíssimos exercem esse direito porque o processo é burocrático e
as instituições criam fricção para dificultar.

**O que automatiza:**
- Usuário informa: banco atual, tipo de crédito, saldo devedor, taxa atual
- Plataforma consulta: melhores taxas disponíveis via Open Finance
- Simula: economia total se migrar para o banco X
- Inicia a portabilidade: protocola o pedido no banco atual (que tem prazo
  legal de 5 dias para responder)
- Monitora: se banco dificultar → aciona reclamação no BACEN

**Modelo de receita:**
- Comissão do banco recebedor: R$150-500 por portabilidade concluída
- Flat fee do usuário: R$49 (opcional — para quem quer o serviço gerenciado)

**Mercado:** R$5 trilhões em crédito ativo no Brasil. 1% de taxa a menos
em um financiamento de R$50k = R$10.000 de economia. Proposta de valor clara.

---

## 7. Recurso em Concurso Público
**Copycat de:** sem equivalente direto

8M+ inscrições em concursos públicos por ano no Brasil. Cada edital
gera centenas de recursos de candidatos eliminados: questão mal formulada,
gabarito errado, irregularidade na banca, critério de desempate ilegal.

A maioria dos candidatos não recorre por não saber como ou por falta de
tempo. Os que recorrem, recorrem mal (sem fundamentação jurídica).

**O que automatiza:**
- Candidato informa: qual questão/fase contestar + motivo
- IA consulta: legislação de referência, jurisprudência de bancas similares,
  decisões de TCE/TCU que anularam questões parecidas
- Gera: recurso administrativo completo com fundamentação
- Se banca mantiver: gera mandado de segurança simplificado
  (MS é o remédio jurídico correto para atos de banca)
- Referral para advogado administrativista parceiro para MS

**Modelo de receita:**
- Recurso administrativo: R$39 por recurso
- Mandado de segurança (referral): 20% do honorário do advogado
- Assinatura para candidatos em múltiplos concursos: R$49/mês

**Mercado:** 8M inscrições × 10% com motivo de recurso × R$39 = R$31M/ano
só no recurso administrativo. MS é ticket alto (R$1.500-5.000).

---

## 8. DPVAT / SPVAT — Indenização de Acidente de Trânsito
**Copycat de:** Snapsheet (EUA), ClaimLogik (Austrália)

O seguro obrigatório DPVAT (agora SPVAT) cobre: morte, invalidez permanente
e despesas médicas em acidentes de trânsito. Valor: até R$13.500 por vítima.

Problema: vítimas não sabem que têm direito, não sabem como reclamar,
ou tiveram o pedido negado indevidamente pela seguradora.

**O que automatiza:**
- Vítima ou familiar responde: tipo de acidente, lesão, documentação
- IA verifica: há direito ao DPVAT? Qual valor estimado?
- Gera: requerimento completo para a seguradora + documentação necessária
- Se negado: recurso com jurisprudência + JEC para cobrar na justiça
- Para invalidez permanente: calcula percentual correto com base na tabela

**Modelo de receita:**
- Requerimento: R$99 fixo
- Success fee se houver recurso: 20% do valor recebido
- Ticket médio de invalidez permanente: R$4.000-13.500

**Mercado:** 400.000+ acidentes com vítimas por ano no Brasil.
Taxa de não reivindicação estimada: 40%.

---

## 9. LGPD — Direitos de Dados Automatizados
**Copycat de:** Mine (Israel/EUA), Jumbo Privacy (EUA)

A LGPD (Lei Geral de Proteção de Dados) deu ao brasileiro 8 direitos
sobre seus dados: acesso, correção, exclusão, portabilidade, entre outros.
Mas exercer esses direitos ainda é manual e desconhecido pela maioria.

Casos práticos:
- Dados vazados em breach de banco ou varejista
- CPF sendo usado por outra pessoa (fraude de identidade)
- Empresa recusando contratar porque dados de dívida antiga apareceram
- Dados de saúde vendidos a seguradoras sem autorização

**O que automatiza:**
- Usuário conecta e-mail + CPF
- Plataforma identifica: com quem seus dados estão, quais empresas
  têm seus dados cadastrados, histórico de compartilhamento
- Gera: pedidos de acesso a dados para cada empresa identificada
- Gera: pedido de exclusão onde o usuário não quer mais ter dados
- Se empresa descumprir: gera reclamação à ANPD + JEC

**Modelo de receita:**
- Assinatura: R$19/mês (monitoramento contínuo + pedidos ilimitados)
- Para empresas (B2B): auditoria de LGPD compliance R$499-2.000

**Mercado:** 100M+ usuários de internet no Brasil. Vazamentos de dados
são mensais. Awareness está crescendo rapidamente.

---

## 10. Regularização Fiscal de Empresa — PERT e Parcelamentos
**Copycat de:** TaxRise (EUA), Optima Tax Relief (EUA)

Estima-se que 4M+ empresas brasileiras tenham débitos com a Receita
Federal, FGTS (CEF), ou estados/municípios. Muitos donos nem sabem o
tamanho real da dívida. Periodicamente o governo abre PERTs
(Programas Especiais de Regularização Tributária) com descontos de
multa e juros de até 100%.

**O que automatiza:**
- CNPJ do usuário → plataforma consulta: Receita Federal, FGTS, PGFN, Sefaz estadual
- Consolida: visão completa do passivo fiscal da empresa
- Simula: qual programa de parcelamento é melhor (PERT, Simples em atraso,
  parcelamento ordinário) — para cada programa, calcula desconto e parcela
- Gera: pedido de adesão ao programa com todos os anexos
- Monitora: comprovantes de pagamento mensais para não perder o parcelamento

**Modelo de receita:**
- Diagnóstico gratuito (aquisição)
- Adesão ao parcelamento: R$499 fixo + 5% de economia gerada no 1º ano
- Monitoramento mensal: R$99/mês enquanto o parcelamento estiver ativo

**Mercado:** 4M+ empresas com débito × ticket médio de R$499 = R$2B de mercado endereçável.
A cada novo PERT aberto pelo governo: onda de demanda concentrada.

---

## Mapa de Encaixe no Bismarck

```
BISMARCK
│
├── [já mapeados]
│   ├── Contesto (multas + cobranças)
│   ├── Amparo (INSS)
│   ├── Aravo (dívidas)
│   ├── Legado (inventário)
│   └── Concilia (família)
│
└── [novos candidatos]
    ├── Alta prioridade (mercado + automação + ticket)
    │   ├── Revisional de Financiamento
    │   ├── Plano de Saúde
    │   └── Rescisão Trabalhista
    │
    ├── Média prioridade
    │   ├── Consignado Indevido (conecta ao Amparo)
    │   ├── Alvará de Funcionamento (conecta ao MEI Auto)
    │   └── Portabilidade de Crédito (conecta ao Aravo)
    │
    └── Oportunidades pontuais
        ├── Recurso de Concurso (sazonal, alto volume)
        ├── DPVAT / SPVAT (conecta ao Contesto)
        ├── LGPD (conecta ao Aravo)
        └── PERT Fiscal (conecta ao MEI Auto)
```

## Os Três que Eu Priorizaria

**Revisional de Financiamento** — 60M contratos, ticket alto,
success fee natural, jurisprudência consolidada.

**Plano de Saúde** — todo brasileiro com plano já foi negado uma vez.
Alta indignação = alta conversão. Decisão do STJ (2022) cria fundamento sólido.

**Rescisão Trabalhista** — 9M demissões por ano, calculadora gratuita
como aquisição, enorme volume potencial, conecta naturalmente ao
público do Contesto e do Amparo.
