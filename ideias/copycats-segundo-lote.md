# Segundo Lote: 10 Copycats para o Brasil

Critério: modelo provado fora, dor real e específica do Brasil, automação viável.
Nenhuma ideia repete o que já está no portfólio.

---

## 1. Inventário e Herança Automatizado
**Copycat de:** Trust & Will (EUA), Farewill (UK)

Fazer inventário no Brasil leva em média 2-4 anos e custa R$5.000-30.000 em honorários.
Desde 2007 o inventário consensual pode ser feito em cartório — extrajudicial, muito mais rápido —
mas menos de 20% dos casos usam essa via porque ninguém guia o processo.

**O que automatiza:**
- Questionário mapeia o patrimônio e a composição familiar
- IA determina se o caso é extrajudicial (cartório) ou judicial (inventário tem menor de idade, herdeiro ausente, conflito)
- Gera todos os documentos: formal de partilha, declaração de bens, ITCMD, Sobrepartilha
- Coordena com cartório via e-Notariado
- Para casos judiciais: referral para advogado parceiro com split de honorário

**Modelo de receita:**
- Extrajudicial: R$1.500-3.500 fixo (vs. R$10.000-30.000 com advogado)
- Judicial (referral): 20-30% do honorário do advogado parceiro

**Mercado:** 1,4M mortes/ano no Brasil. A maioria com algum patrimônio (imóvel, veículo, poupança).
Apenas ~30% dos inventários são feitos formalmente — o restante fica em situação irregular por anos.

**Conexão com portfólio:** pipeline natural do produto de Imóvel Regular —
quem regulariza imóvel muitas vezes descobre que está no nome de falecido.

---

## 2. Divórcio Extrajudicial Automatizado
**Copycat de:** Hello Divorce (EUA), Wevorce (EUA), Agreed (UK)

Divórcio consensual sem filhos menores pode ser feito em cartório desde 2007.
Não precisa de advogado, não precisa de juiz. Mas quase ninguém sabe disso —
e quando sabe, não sabe como fazer os documentos nem qual cartório procurar.

**O que automatiza:**
- Questionário determina se o casal é elegível para divórcio extrajudicial
- Calcula partilha de bens (regime de casamento + patrimônio declarado)
- Gera escritura de divórcio, partilha e eventuais acordos de alimentos (quando não há menores)
- Agenda o cartório via e-Notariado
- Para casos com menores ou conflito: encaminha para advogado parceiro

**Modelo de receita:**
- Divórcio extrajudicial: R$599-999 fixo
- Com partilha de imóvel: R$1.299 (inclui coordenação com cartório de imóveis)
- Referral judicial: split com advogado

**Mercado:** 350.000+ divórcios/ano no Brasil. Maioria consensual.
Hello Divorce (EUA) chegou a US$10M ARR em 4 anos com modelo similar.

**Diferencial:** o cartório cobra as custas (em média R$800-2.000), mas ninguém
cobra por organizar o processo — essa é a lacuna.

---

## 3. Seguro Desemprego Automatizado
**Copycat de:** Candidly (EUA), Steady (EUA)

7-9 milhões de requerimentos de seguro desemprego por ano no Brasil.
Processo feito no aplicativo Carteira de Trabalho Digital — mas cheio de erros:
prazo errado (tem que esperar 6 meses entre requerimentos), documentação faltando,
CAGED não baixado pela empresa a tempo, habilitação negada por erro do sistema.

**O que automatiza:**
- Verifica elegibilidade antes de o trabalhador perder o prazo
- Preenche o requerimento automaticamente com dados da CTPS digital
- Monitora o status diariamente (negado? Por quê? Como resolver?)
- Se negado indevidamente: gera recurso com fundamentação correta
- Alerta sobre prazo de saques das parcelas (muitas pessoas perdem por esquecer)

**Modelo de receita:**
- R$39 fixo por requerimento (o benefício vale R$1.500-2.300/mês por até 5 parcelas)
- R$99 se incluir monitoramento + recurso em caso de negativa

**Mercado:** 7M requerimentos × R$39 = R$273M/ano de receita potencial.
CAC baixo: trabalhador demitido busca ativamente — Google Ads de intenção funciona.

---

## 4. Baixa de Empresa Automatizada
**Copycat de:** Stripe Atlas (incorporação), Clerky (EUA), Capbase

O oposto do "abrir empresa": fechar. Ninguém fez isso bem no Brasil.
Abrir empresa hoje tem Contabilizei, Abertura Simples, dezenas de concorrentes.
Fechar leva 6 meses a 2 anos, envolve Receita Federal + Junta Comercial + prefeitura +
estado, e a maioria dos contadores cobra igual ou mais que para abrir.

Brasil tem 4M+ empresas inativas que o dono não sabe como fechar —
acumulando multas, obrigações acessórias e dívidas invisíveis.

**O que automatiza:**
- Diagnóstico: tem débito? Empregado ativo? Livros fiscais em dia?
- Mapa de pendências antes de iniciar o processo (evita surpresas)
- Geração de todas as certidões negativas necessárias
- Declaração de inatividade (DCTF, ECF, ECD)
- Protocolo na Receita, Junta e prefeitura em sequência correta
- Monitoramento até conclusão final

**Modelo de receita:**
- Empresa sem débito: R$299-499 fixo
- Empresa com pendências: R$699-1.200 (inclui orientação de regularização antes da baixa)

**Mercado:** 1,5M+ empresas abertas/ano. Taxa histórica de mortalidade indica mercado
constante de 800k-1M fechamentos/ano. Maioria faz de forma incorreta ou não faz.

---

## 5. CAR e Regularização Ambiental Rural
**Copycat de:** sem equivalente direto — oportunidade sem modelo internacional claro

CAR (Cadastro Ambiental Rural) é obrigatório para todo imóvel rural no Brasil desde 2012.
Sem CAR: produtor não acessa crédito rural, não vende para tradings, não regulariza imóvel.

Mais de 30% dos imóveis rurais ainda têm CAR irregular ou desatualizado.
Em Goiás — onde já temos foco — o agronegócio é o maior setor da economia.

**O que automatiza:**
- Upload da matrícula do imóvel
- IA processa imagem de satélite (Google Earth Engine API) e identifica:
  - Área total, APP (Área de Preservação Permanente), Reserva Legal
  - Sobreposição com áreas protegidas
  - Passivo ambiental estimado
- Gera o shapefile para registro no SICAR (sistema nacional do CAR)
- Instrui sobre Programa de Regularização Ambiental (PRA) se houver passivo
- Para imóveis com embargo IBAMA: diagnóstico + referral para advogado ambiental

**Modelo de receita:**
- CAR simples (imóvel < 4 módulos fiscais): R$399
- CAR complexo + PRA: R$999-2.500
- Monitoramento anual (SICAR exige atualização): R$199/ano

**Mercado em GO:** 400.000+ imóveis rurais cadastrados, ~120.000 com pendências.
Distribuição: cooperativas agropecuárias, sindicatos rurais, revendas de insumo.

---

## 6. Consórcio Inteligente
**Copycat de:** sem equivalente direto — consórcio é produto exclusivamente brasileiro

R$500B+ em consórcios ativos no Brasil. 10M+ consorciados.
Ninguém criou uma ferramenta de gestão inteligente para esse produto.

Dores reais do consorciado hoje:
- Não sabe se vale mais lancer (dar lance) ou esperar ser contemplado
- Não entende quando sair vendendo sua cota no mercado secundário
- Não sabe como usar a carta de crédito da forma mais eficiente
- Administradoras cobram taxas que o consorciado não entende

**O que automatiza:**
- Conecta com a administradora (scraping ou manual) para monitorar saldo e assembleias
- Simula: "se der um lance de R$X hoje, qual a probabilidade de ser contemplado?"
- Monitora o mercado secundário de cotas — quando vender, quando comprar
- Calcula o custo real do consórcio vs. financiamento vs. poupança (muita gente descobre que fez escolha errada)
- Para quem quer sair: conecta com compradores de cota via marketplace integrado

**Modelo de receita:**
- Assinatura: R$29/mês por cota monitorada
- Marketplace de cotas: 2% da transação

**Por que agora:** Banco Central abriu dados de consórcio via Open Finance em 2023 —
pela primeira vez é possível acessar dados de saldo e histórico programaticamente.

---

## 7. IPTU Inteligente — Contestação de Tributos Municipais
**Copycat de:** Ownwell (EUA — property tax appeals), Kukun (EUA)

IPTU é calculado com base no valor venal do imóvel definido pela prefeitura.
Esse cálculo frequentemente superestima a área, usa categoria errada,
ou não considera depreciação. Em São Paulo, 30%+ dos recursos de IPTU são deferidos.

**O que automatiza:**
- Usuário informa o IPTU (carnê ou código de barras)
- Plataforma acessa o cálculo da prefeitura via API/scraping
- Compara com: metragem real, uso atual, estado de conservação, imóveis comparáveis
- Se há discrepância > 15%: gera impugnação administrativa automática
- Monitora o processo e alerta sobre prazos

**Além do IPTU:**
- ISS indevido para profissionais autônomos e pequenas empresas
- Taxa de lixo e iluminação pública cobradas irregularmente
- ITBI superfaturado em transações imobiliárias

**Modelo de receita:**
- Success fee: 30% da redução obtida (só cobra se ganhar)
- Assinatura monitoramento: R$49/ano por imóvel

**Mercado:** 70M imóveis urbanos no Brasil, a maioria pagando IPTU.
Ownwell (EUA) virou unicórnio contestando property tax em escala.

---

## 8. Saúde Ocupacional + eSocial para PMEs
**Copycat de:** Rippling (EUA), Gusto (EUA) — mas foco em compliance de saúde ocupacional

Toda empresa com funcionário CLT é obrigada a:
- ASO de admissão, periódico e demissão
- PCMSO (Programa de Controle Médico de Saúde Ocupacional)
- PGR (Programa de Gerenciamento de Riscos — substitui o PPRA)
- Registrar todos os eventos de saúde no eSocial (S-2220, S-2240)

Para uma empresa com 10 funcionários, isso gera 40-60 eventos no eSocial por ano.
A maioria das PMEs faz errado, paga multa na fiscalização ou paga caro para clínica
que faz tudo de forma manual e lenta.

**O que automatiza:**
- Calendário de ASOs com alertas (admissão, periódico vencendo, demissional)
- Rede de clínicas parceiras com agendamento automático
- Geração do PGR/PCMSO para atividades de baixo risco (padrão para a maioria das PMEs de comércio e serviço)
- Envio automático dos eventos S-2220 e S-2240 no eSocial via API
- Alerta antes de fiscalização (DRT programa em calendário público)

**Modelo de receita:**
- R$49/funcionário/mês (inclui ASOs ilimitados + envio eSocial)
- Para PME de 10 funcionários: R$490/mês
- Receita da clínica parceira: R$25-50 por consulta agendada pela plataforma

**Mercado:** 10M+ trabalhadores formais em empresas com até 50 funcionários.
Nenhum concorrente focou nessa camada — os players de RH (Gupy, Totvs, ADP) miram médias e grandes.

---

## 9. Pensão Alimentícia Automatizada
**Copycat de:** SupportPay (EUA), OurFamilyWizard (EUA)

15M+ famílias monoparentais no Brasil. Inadimplência de pensão alimentícia é
crônica — estima-se que 70% dos acordos judiciais não são cumpridos integralmente.
O processo de cobrar é humilhante, lento e revitimiza quem já foi prejudicado.

**O que automatiza:**
- Registro de pagamentos e não-pagamentos com evidência automática (timestamp + banco)
- Tracking de despesas extraordinárias (escola, médico, atividade) com solicitação formal ao co-genitor
- Régua automática de cobrança: lembrete → notificação formal → execução judicial assistida
- Geração de petição de prisão (devedor de alimentos pode ser preso — poucos sabem usar isso)
- Para casos de revisão de pensão: simulador de novo valor com base em renda atualizada

**Modelo de receita:**
- R$29/mês por família
- R$99 por petição judicial gerada
- Parceria com advogados de família para casos complexos

**Mercado:** 15M famílias × R$29 = R$435M/mês de receita potencial.
NPS naturalmente alto — resolver esse problema muda a vida de quem está no produto.

---

## 10. Imposto de Renda Plus — IR para Quem Tem Complexidade
**Copycat de:** TurboTax (EUA), TaxJar (EUA), Keeper Tax (EUA)

O IR do assalariado simples é resolvido. O problema é o IR de:
- Autônomos e freelancers (carnê-leão mensal, deduções de despesas)
- Investidores (renda variável, fundos, criptomoedas — cada um com regra diferente)
- Aluguéis (carnê-leão + deduções permitidas vs. não permitidas)
- Quem tem dependente com despesa médica alta
- Quem vendeu imóvel (ganho de capital, isenção por reinvestimento)

Esses perfis pagam R$300-1.500 para contador fazer algo que poderia ser automatizado.

**O que automatiza:**
- Integra com corretoras via Open Finance/API (B3 dados históricos, XP, Rico, etc.)
- Importa notas de corretagem e calcula DARFs de renda variável mensalmente
- Carnê-leão automático para autônomos: NF recebida → DARF calculado → pago via PIX
- Simula cenários: "vale declarar dependente pelo completo ou simplificado?"
- Cruza com Receita Federal (malha fina prevention) antes de enviar

**Modelo de receita:**
- Assinatura anual: R$149-299/ano
- IR básico (assalariado simples): grátis — aquisição
- IR complexo (investidor/autônomo): R$199-499/ano

**Mercado:** 40M declarações/ano. 8-10M no perfil "complexo" mal atendido.
TurboTax fatura US$3B/ano nos EUA. No Brasil o mercado é deserto acima do básico.

---

## Matriz de Prioridade — Segundo Lote

| Ideia | Mercado | Automação | Ticket | Entrada | Score |
|-------|---------|-----------|--------|---------|-------|
| Seguro Desemprego | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Baixo | Fácil | **1º** |
| IR Plus | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Médio | Fácil | **2º** |
| Baixa de Empresa | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Médio | Fácil | **3º** |
| Inventário e Herança | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Alto | Média | **4º** |
| CAR Rural (GO) | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Médio | Fácil | **5º** |
| IPTU Inteligente | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Médio | Média | **6º** |
| Divórcio Extrajudicial | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Médio | Média | **7º** |
| Consórcio Inteligente | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Baixo | Média | **8º** |
| Saúde Ocupacional PME | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Médio | Alta | **9º** |
| Pensão Alimentícia | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Baixo | Fácil | **10º** |
