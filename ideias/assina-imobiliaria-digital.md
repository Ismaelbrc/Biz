# Assina — Back-office do Proprietário Direto

Contrato digital, vistoria com IA e controle de pagamento para quem
aluga sem imobiliária. Sem marketplace, sem corretora, sem burocracia.

---

## O Proprietário Direto

No Brasil existem dois tipos de proprietário que aluga imóvel:

**Tipo A — usa imobiliária:**
Paga 10% ao mês + 1 mês de aluguel na locação.
Recebe o repasse no dia 15 mesmo que o inquilino pagou no dia 5.
Não tem visibilidade de nada. Mas não precisa se preocupar.

**Tipo B — autogerencia (proprietário direto):**
Anuncia no OLX, Zap Imóveis ou por indicação de conhecido.
Não paga comissão — fica com 100% do aluguel.
Em troca: gerencia tudo sozinho. E gerencia muito mal.

```
Como o proprietário direto funciona hoje:

Contrato:
  → Baixa um modelo do Google
  → Imprime, assina à mão, tira xerox, guarda na gaveta
  → 2 anos depois não encontra quando precisa

Vistoria:
  → A maioria não faz nenhuma vistoria documentada
  → Alguns tiram fotos soltas no WhatsApp
  → Ninguém tem laudo formal — disputa garantida na saída

Cobrança:
  → Lembra do vencimento na memória
  → Manda mensagem no WhatsApp: "oi, o aluguel venceu"
  → Controle em planilha desatualizada ou no caderno
  → Reajuste anual: esquece ou aplica valor errado

Resultado:
  → Perde dinheiro no reajuste esquecido
  → Perde caução em disputa de vistoria sem documentação
  → Perde tempo gerenciando por WhatsApp pessoal
  → Não sabe quanto recebeu no ano para declarar no IR
```

**Esse é o cliente do Assina.**

Não é um marketplace. Não compete com QuintoAndar.
É uma ferramenta para o proprietário que já tem o inquilino —
e precisa fazer o restante direito, sem imobiliária, sem papel.

---

## Tamanho do Mercado

```
Brasil:
  → 14M+ imóveis alugados (IBGE)
  → ~40% são gerenciados diretamente pelo proprietário (sem imobiliária)
  → = 5,6M proprietários diretos no Brasil

Goiás + DF:
  → ~600.000 imóveis alugados
  → ~240.000 proprietários diretos (estimativa)
  → Ticket médio GO: R$1.500/mês | DF: R$2.200/mês

OLX em Goiânia (referência de volume):
  → 8.000-12.000 anúncios ativos de proprietário direto
  → Esse volume representa o funil natural de aquisição

Quem é esse proprietário:
  → Tem 1-3 imóveis (apartamento, casa, sala comercial)
  → Comprou como investimento ou herdou
  → Renda do aluguel é complemento — não é a renda principal
  → Não quer pagar imobiliária mas também não quer dor de cabeça
  → Faixa etária: 40-65 anos (tem o imóvel, nem sempre tem o digital)
```

---

## O Produto — 3 Módulos

### Módulo 1 — Contrato Digital

**O problema:** contrato baixado do Google não tem valor jurídico adequado,
não está atualizado com a Lei do Inquilinato (Lei 8.245/91 + reformas),
e ninguém encontra quando precisa.

```
FLUXO DO PROPRIETÁRIO:

  1. Cadastra o imóvel (endereço, tipo, valor do aluguel, prazo)
  2. Cadastra o inquilino (nome, CPF, endereço atual)
  3. Escolhe as cláusulas opcionais:
       → Aceita pet? (com cláusula de responsabilidade específica)
       → Permite reforma? (com cláusula de aprovação prévia)
       → Sublocação? (padrão: proibida)
       → Garantia: caução, seguro fiança, fiador ou sem garantia
       → Índice de reajuste: IPCA ou IGP-M
  4. Plataforma gera o contrato em segundos
  5. Ambos recebem o link de assinatura por WhatsApp ou e-mail
  6. Assinam pelo celular (sem certificado ICP — válido pela Lei 14.063/2020)
  7. Contrato armazenado na plataforma — acessível sempre

O QUE O CONTRATO INCLUI AUTOMATICAMENTE:
  → Cláusula de reajuste com índice e data de aniversário
  → Multa por rescisão antecipada proporcional (conforme STJ)
  → Responsabilidades de manutenção (pequenos reparos × estrutural)
  → Cláusula de vistoria (referencia o laudo gerado no Módulo 2)
  → Prazo para devolução da caução após saída
  → Foro: comarca do imóvel

LINGUAGEM SIMPLES:
  → Cada cláusula tem uma versão "em português" ao lado do texto jurídico
  → "O que significa isso?" — explica em uma frase o que cada trecho protege
```

---

### Módulo 2 — Vistoria Digital

**O maior gerador de conflito entre proprietário e inquilino — resolvido.**

```
PROBLEMA ATUAL:
  Na entrada: fotos no WhatsApp + talvez um papel assinado
  Na saída: "isso já estava assim" vs "você que fez isso"
  Resultado: disputa, JEC, caução perdida ou retida indevidamente

VISTORIA DE ENTRADA — guiada pelo app:

  App abre o checklist por cômodo:
    Sala de estar:
      → "Fotografe a parede norte" (com guia de enquadramento)
      → "Fotografe a parede sul"
      → "Fotografe o piso"
      → "Fotografe a janela (aberta e fechada)"
      → "Fotografe o interruptor e tomadas"

  Para cada cômodo: 8-15 fotos + 1 vídeo de 30 segundos
  Total: ~100 fotos + 6-8 vídeos por imóvel padrão
  Tempo: 30-45 minutos

  IA analisa cada foto:
    → Detecta e cataloga imperfeições pré-existentes:
      "Arranhão no piso da cozinha (11cm, direção nordeste)"
      "Mancha na parede do quarto (área ~0,3m², cor bege)"
      "Furos de parafuso na parede da sala (3 furos, 8mm)"
    → Classifica: cosmético / funcional / estrutural

  Laudo gerado automaticamente:
    → PDF com todas as fotos organizadas por cômodo
    → Lista de imperfeições pré-existentes com foto e descrição
    → Hash SHA-256 do documento (imutável — qualquer alteração detectável)
    → Timestamp e geolocalização de cada foto

  Ambos assinam o laudo digitalmente.
  Armazenado na plataforma por 10 anos (prazo prescricional).

VISTORIA DE SAÍDA — comparação automática:

  Mesmo app, mesma sequência de fotos
    ↓
  IA compara entrada vs. saída por ângulo:

  RESULTADO AUTOMÁTICO:
  ┌────────────────────────────────────────────────────────┐
  │ COMPARATIVO VISTORIA — AP. 302, SETOR BUENO            │
  ├────────────────────────────────────────────────────────┤
  │ ✅ Sem alteração: piso sala, janelas, banheiro social   │
  │                                                         │
  │ ⚠️  Pré-existente (sem alteração): arranhão piso cozinha│
  │                                                         │
  │ ❌ Novo dano detectado:                                  │
  │    → Furo na parede do quarto: ~3cm (não existia)       │
  │      Reparo estimado: R$40-80                           │
  │    → Mancha no teto do banheiro: possível umidade       │
  │      Reparo estimado: R$150-300 (investigar causa)      │
  │                                                         │
  │ Sugestão de retenção de caução: R$190-380               │
  │ Caução disponível: R$4.500                              │
  │ Devolução sugerida: R$4.120-4.310                       │
  └────────────────────────────────────────────────────────┘

  Proprietário aprova, ajusta ou contesta com justificativa.
  Inquilino tem 5 dias para contestar com contra-evidência.
  Após prazo: devolução automática via PIX.
```

---

### Módulo 3 — Controle de Pagamento

**O WhatsApp deixa de ser ferramenta de cobrança.**

```
CONFIGURAÇÃO (uma vez só):
  → Dia de vencimento: 5, 10 ou 15
  → Forma de pagamento: PIX fixo ou boleto
  → Tolerância: dias de carência antes de notificar atraso
  → Multa por atraso: 2% + 0,033%/dia (padrão Lei do Inquilinato)

CICLO MENSAL AUTOMÁTICO:

  Dia -3 (3 dias antes do vencimento):
    → WhatsApp pro inquilino: "Olá! Seu aluguel de setembro vence
      em 3 dias — R$2.200. PIX: [chave] ou Boleto: [link]"

  Dia 0 (vencimento):
    → Se PIX recebido: confirma para proprietário + registra
    → Se não recebido: notificação pro proprietário

  Dia +3 (3 dias após):
    → WhatsApp pro inquilino com multa calculada:
      "Seu aluguel venceu há 3 dias. Valor atualizado: R$2.266
       (R$2.200 + 2% multa + 3 dias de mora)"

  Dia +10:
    → Notificação mais firme
    → Proprietário recebe: "Considerar notificação formal?"
      → Botão: [Gerar notificação extrajudicial] — integração com Bismarck

PAINEL DO PROPRIETÁRIO:
  ┌──────────────────────────────────────────────────────┐
  │ MEUS IMÓVEIS — SETEMBRO 2026                         │
  ├──────────────────────────────────────────────────────┤
  │ Ap. 302 Setor Bueno — Ana Rodrigues                  │
  │   Aluguel: R$2.200 | ✅ PAGO (03/09)                │
  │   Contrato: vence em 8 meses (mai/2027)              │
  │   Reajuste: +5,2% IPCA em dezembro → R$2.314         │
  │                                                      │
  │ Casa Jardim Goiás — Carlos e Marta Santos            │
  │   Aluguel: R$1.800 | ⚠️ VENCIDO há 5 dias           │
  │   Notificação enviada em 08/09 — sem resposta        │
  │   [Gerar notificação formal] [Ligar agora]           │
  │                                                      │
  │ Sala 405 Centro — Papelaria Exemplo LTDA             │
  │   Aluguel: R$3.500 | ✅ PAGO (05/09)                │
  │   Contrato: vence em 14 meses (nov/2027)             │
  └──────────────────────────────────────────────────────┘

REAJUSTE AUTOMÁTICO:
  → 60 dias antes do aniversário do contrato:
    "Em 60 dias o contrato faz 12 meses. Reajuste previsto:
     +5,2% IPCA (acumulado set/25-ago/26). Novo valor: R$2.314."
  → Proprietário confirma (ou ajusta)
  → Plataforma gera aditivo contratual para assinatura de ambas as partes
  → Cobrança atualiza automaticamente a partir do mês correto

RELATÓRIO ANUAL:
  → Janeiro: "Aqui está o resumo do seu aluguel em 2025 para o IR:"
    Renda total recebida: R$26.400
    Meses pagos em dia: 10 | Com atraso: 2 | Inadimplência: 0
    Comprovante para DIRPF pronto para download
```

---

## Modelo de Receita

### Freemium — a entrada gratuita

```
PLANO FREE (sempre gratuito):
  → 1 imóvel
  → Contrato digital ilimitado
  → Controle de pagamento básico (registro manual)
  → Vistoria: upload livre de fotos (sem análise de IA)
  → Histórico de 12 meses

Objetivo: o proprietário entra de graça, resolve o problema do contrato,
e descobre que quer mais. A vistoria com IA é o que converte.
```

### Planos pagos

| Plano | Preço | Para quem |
|-------|-------|-----------|
| **Solo** | R$29/mês | Até 3 imóveis — vistoria com IA, cobrança automática, reajuste automático |
| **Investidor** | R$59/mês | Até 10 imóveis — tudo do Solo + relatório IR + histórico ilimitado |
| **Gestor** | R$129/mês | Ilimitado — para quem gerencia imóveis de terceiros (despachante, gestor independente) |

### Pay-per-use (alternativa para quem não quer assinar)

| Serviço | Valor |
|---------|-------|
| Gerar contrato | R$39 por contrato |
| Vistoria de entrada com laudo IA | R$49 |
| Vistoria de saída com comparativo | R$49 |
| Aditivo de reajuste | R$19 |
| Notificação extrajudicial de inadimplência | R$59 |

### Unit economics

```
CAC estimado (SEO + OLX orgânico): R$80-150
Conversão free → pago: 25% (estimativa conservadora)
ARPU pago: R$29-59/mês
Churn estimado: 3-5%/mês (proprietário cancela quando imóvel fica vago)
LTV médio: R$29 × (1/0,04) = R$725

Breakeven por cliente pago: ~3 meses de assinatura
```

---

## Distribuição

### Canal 1 — OLX e Zap Imóveis (SEO + anúncios)

O proprietário direto anuncia no OLX. Esse é o momento de maior dor:
acabou de achar o inquilino e agora precisa fazer o contrato.

Campanha de intenção:
- "como fazer contrato de aluguel sem imobiliária"
- "modelo de contrato de aluguel válido"
- "vistoria de imóvel como fazer"
- "como cobrar aluguel sem imobiliária"

CPC baixo (nicho específico), intenção altíssima.
Ferramenta gratuita de contrato = conversão alta.

### Canal 2 — Grupos de Facebook e WhatsApp de investidores em imóveis

Existem centenas de grupos ativos de "proprietários de imóveis" e
"investidores em imóveis" em Goiânia e Brasília. Discussões recorrentes:
"qual modelo de contrato vocês usam?", "como fazer vistoria?",
"inquilino não pagou — o que faço?"

Cada discussão dessas é uma oportunidade de aparecer com a solução.
Presença orgânica nesses grupos = aquisição de custo zero.

### Canal 3 — YouTube sobre investimento em imóveis

Criadores com foco em renda passiva via aluguel: Thiago Concer,
Gustavo Cerbasi, Rafael Seabra. Conteúdo de "como alugar sem imobiliária"
tem audiência massiva. Parceria = acesso direto ao público exato.

### Canal 4 — Contadores e despachantes

O contador do proprietário sabe que tem cliente com imóvel alugado.
O despachante que ajudou a comprar sabe que o imóvel vai ser alugado.

Parceria: comissão de R$20-30 por cliente ativado.
Plataforma que o contador recomenda = credibilidade instantânea.

### Canal 5 — Portaria e síndicos

Síndico do prédio sabe quais unidades estão para alugar e quais
proprietários gerenciam diretamente. Canal de baixo volume mas
de alta confiança (recomendação pessoal dentro do condomínio).

---

## Arquitetura Técnica

```
STACK (simples e enxuto para MVP)

Frontend:
  → Web: Next.js (proprietário acessa principalmente pelo desktop)
  → Mobile: React Native (inquilino usa principalmente pelo celular
    — especialmente para a vistoria)

Backend:
  → Node.js + PostgreSQL (Supabase para MVP)
  → Armazenamento de fotos: Cloudflare R2 (barato, sem egress)

INTEGRAÇÕES ESSENCIAIS
  → Assinatura digital: ZapSign API (R$1-3 por documento)
  → WhatsApp: Z-API ou Twilio (notificações automáticas)
  → PIX/Boleto: Asaas (R$1,99 por boleto, PIX com QR fixo gratuito)
  → Geração de PDF: Puppeteer (server-side, templates HTML)

VISTORIA COM IA
  → Upload de fotos: Cloudflare R2 + CDN
  → Análise individual de foto: Claude API Vision
    (detecta danos, classifica tipo e severidade)
  → Comparação entrada/saída:
    → Alinhamento: OpenCV em Python (microserviço)
    → Análise de diferenças: Claude Vision (compara par de fotos)
  → Geração do laudo: HTML → Puppeteer → PDF
  → Hash imutável: SHA-256 do PDF armazenado junto ao documento

CUSTO DE OPERAÇÃO (por vistoria):
  → 100 fotos × análise Claude Vision: ~R$1,50
  → Comparação 100 pares: ~R$3,00
  → Geração do laudo: R$0,05
  → Armazenamento (por 10 anos): R$0,30
  → Total custo por vistoria: ~R$5

  Com cobrança de R$49 por vistoria: margem bruta de ~R$44
```

---

## Roadmap

### Mês 1 — Validação zero-código
```
→ Landing page simples: "Faça seu contrato de aluguel sem imobiliária"
→ Formulário de dados → gera PDF via template → envia para assinatura (ZapSign)
→ Sem app, sem código complexo — Typeform + Zapier + ZapSign + Make
→ Cobrar R$39 por contrato via PIX manual
→ Meta: 30 contratos pagos em 30 dias
→ Validação: pessoas pagam pelo contrato digital?
```

### Mês 2 — MVP da vistoria
```
→ App mobile básico (React Native) com checklist de vistoria
→ Upload guiado de fotos por cômodo
→ Laudo gerado em PDF (ainda sem IA de comparação — apenas organização)
→ Cobrar R$49 por vistoria
→ Meta: 20 vistorias realizadas
→ Validação: proprietário conclui a vistoria sozinho?
```

### Mês 3 — Controle de pagamento
```
→ Dashboard web básico do proprietário
→ Registro de pagamentos + notificação manual por WhatsApp
→ Boleto/PIX via Asaas integrado
→ Plano mensal: R$29/mês (converte os pay-per-use recorrentes)
→ Meta: 50 assinantes pagos
```

### Mês 4-6 — IA na vistoria + refinamento
```
→ Análise automática de fotos (Claude Vision)
→ Comparativo entrada/saída automatizado
→ Reajuste automático com geração de aditivo
→ Relatório anual para IR
→ Meta: 200 assinantes pagos
```

---

## Integração com o Portfólio Bismarck

O Assina tem dois momentos naturais de crossell:

**Quando o inquilino não paga:**
```
Painel mostra: "Aluguel vencido há 10 dias. O que fazer?"
  → [Gerar notificação extrajudicial] → Contesto / Bismarck
    "Geramos a notificação formal. Se não pagar em 3 dias,
     podemos entrar com ação de despejo automaticamente."
```

**Quando termina o contrato:**
```
→ Legado: "Esse imóvel está no seu inventário?
    Garanta que vai para quem você quer sem inventário judicial."
→ Revis: "Você tem financiamento desse imóvel?
    Verifique se os juros estão corretos."
```

**Quando o inquilino usa o app:**
```
→ Aravo: "Sua análise de crédito mostrou restrição no Serasa.
    Quer regularizar para facilitar futuros aluguéis?"
→ Amparo: "Você é MEI? Garante que seu INSS está em dia."
```

---

## Nome e Posicionamento

### Nome: Assina

O contrato é o ato central do produto. Assinar = concluir, formalizar,
dar validade. Em português tem energia de ação, de encerramento de um
processo que antes era burocrático e lento.

Também funciona como verbo de comando: "Vai lá, assina."

**Tagline:**

> *"Contrato, vistoria e cobrança — sem imobiliária, sem papel."*

### Posicionamento em uma frase

O Assina é para o proprietário que quer fazer tudo direito
sem precisar de ninguém para fazer por ele.

```
Para o proprietário que diz:
  "Não quero pagar 10% pra imobiliária"
  → Assina resolve: você não precisa

Para o proprietário que diz:
  "Mas eu não sei como fazer contrato certo"
  → Assina resolve: a plataforma faz por você

Para o proprietário que diz:
  "Tenho medo de briga na saída"
  → Assina resolve: o laudo fotográfico elimina a disputa

Para o proprietário que diz:
  "Odeio ficar cobrando no WhatsApp"
  → Assina resolve: o sistema cobra por você
```

### Tom de voz

```
Formal     ←——————————[•]————→    Informal
Técnico    ←———————[•]—————→     Acessível
Sério      ←————[•]——————————→   Bem-humorado
Distante   ←——————————[•]———→    Próximo
```

O Assina fala como um amigo que é advogado e contador ao mesmo tempo —
resolve o problema sem jargão, sem enrolação, sem te fazer sentir burro
por não saber fazer.

---

## Resumo Executivo

**O produto:** ferramenta de back-office para proprietário que aluga
sem imobiliária. Três problemas resolvidos: contrato sem advogado,
vistoria sem papel e disputa, cobrança sem WhatsApp pessoal.

**O cliente:** proprietário de 1-5 imóveis que autogerencia. Perfil:
40-65 anos, renda do aluguel como complemento, não quer pagar comissão
mas também não quer dor de cabeça. 5,6M no Brasil, ~240k em GO + DF.

**O modelo:**
- Gratuito: 1 imóvel (isca de aquisição)
- Pago: R$29-59/mês ou R$39-49 por serviço avulso

**Por que funciona:**
- O contrato digital é o problema imediato — e é fácil de resolver
- A vistoria com IA é o diferencial que ninguém mais oferece
- O proprietário direto está ativamente buscando solução (SEO de intenção alta)
- Custo de construção baixo — ZapSign + Asaas + Claude Vision = produto funcional

**Por que GO + DF primeiro:**
- Mercado familiar (conhecimento local)
- Sem concorrência direta focada nesses estados
- Corredor GO-DF = dois mercados com uma operação

**Nome:** Assina
**Tagline:** "Contrato, vistoria e cobrança — sem imobiliária, sem papel."
