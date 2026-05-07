# CotAI — Cotação de Suprimentos 100% pelo WhatsApp

O comprador fala o que precisa. O fornecedor responde guiado pelo bot.
O mapa de cotação chega no WhatsApp de quem pediu. Nada sai do WhatsApp.

---

## O Problema

Todo negócio compra suprimentos. E toda compra começa da mesma forma:

```
Gerente da clínica manda mensagem no WhatsApp para 5 distribuidoras:
  "Oi, tudo bem? Preciso de luva descartável M, avental e máscara.
   Pode me passar o preço?"

Distribuidora 1: responde em 4h com tabela em PDF ilegível
Distribuidora 2: "pode mandar a lista completa?" (não leu a mensagem)
Distribuidora 3: responde só da luva, esquece os outros itens
Distribuidora 4: não responde
Distribuidora 5: liga às 18h quando o gerente já foi embora

Gerente compila tudo em uma planilha às 19h para comparar.
Descobre que comparou luvas de marcas diferentes.
Começa de novo.

Tempo total: 4-6 horas por cotação.
Frequência: 2-4 vezes por mês.
Custo real: 8-16 horas/mês de uma pessoa qualificada perdidas em cotação.
```

O problema não é só o comprador. O fornecedor também sofre:

```
Representante da distribuidora recebe 30 pedidos de cotação por dia —
cada um em um WhatsApp diferente, com formatos diferentes, com itens
diferentes pedidos de formas diferentes. Não consegue responder tudo.
Prioriza os clientes grandes. O cliente médio fica sem cotação.
```

**O CotAI resolve os dois lados no mesmo canal que os dois já usam.**

---

## O Conceito Central

Não é um portal. Não é um app. Não é um sistema para aprender.

É um número de WhatsApp que entende o que você precisa comprar e
que já sabe falar com os fornecedores certos do jeito certo.

```
Para o comprador: fala como fala com qualquer pessoa no WhatsApp
Para o fornecedor: responde uma pergunta de cada vez, no próprio WhatsApp
Para os dois: nada para instalar, nada para aprender, nada para abrir no computador
```

---

## O Fluxo Completo — Tudo no WhatsApp

### LADO DO COMPRADOR

```
──────────────────────────────────────────────
COMPRADOR → COTAI
──────────────────────────────────────────────

[Comprador manda mensagem para o número do CotAI]

Comprador:
  "Preciso cotar para obra de reforma:
   50 sacos de cimento CP II 50kg
   20 barras de ferro 3/8" 12m
   10 latas de tinta Suvinil branca 18L
   Entrega em Goiânia Setor Bueno. Preciso até sexta."

CotAI:
  "Entendi! Vou confirmar o pedido antes de cotar:

   📦 Cimento CP II 50kg — 50 sacos
   📦 Ferro CA-50 3/8" (9,5mm) 12m — 20 barras
   📦 Tinta Suvinil Branco Neve 18L — 10 latas

   🏠 Entrega: Setor Bueno, Goiânia-GO
   📅 Prazo: até sexta-feira (09/05)

   Precisa de nota fiscal?"

Comprador:
  "Sim"

CotAI:
  "Condição de pagamento preferida?"

Comprador:
  "30 dias, mas aceito à vista"

CotAI:
  "Perfeito! Estou consultando os fornecedores agora.
   Você recebe o mapa de cotação aqui mesmo em até 3 horas. ✅"

[3 horas depois]

CotAI:
  "📊 Mapa de cotação pronto!

   Pedido: cimento + ferro + tinta
   Fornecedores consultados: 4

   🥇 Melhor preço total:
      MixConstrução — R$3.847 | 30 dias | Entrega: 2 dias úteis

   ⚡ Entrega mais rápida:
      Casa do Construtor — R$4.120 | À vista | Entrega: amanhã

   📄 Mapa completo com todos os itens e preços segue abaixo:"

   [PDF enviado]

   "Quer que eu feche com algum fornecedor? É só me dizer qual."
```

---

### LADO DO FORNECEDOR — O Formato via WhatsApp

O fornecedor não preenche formulário. Não acessa portal.
O CotAI faz as perguntas certas, uma de cada vez.

```
──────────────────────────────────────────────
COTAI → FORNECEDOR (mensagem de abertura)
──────────────────────────────────────────────

CotAI [para MixConstrução]:
  "Oi! Sou o CotAI — sistema de cotação da Reformas Silva Ltda.
   Temos um pedido para você cotar. São 3 itens. Pode me ajudar? (sim/não)"

MixConstrução:
  "sim"

──────────────────────────────────────────────
COTAI conduz item por item
──────────────────────────────────────────────

CotAI:
  "Ótimo! Vamos lá.

   📦 ITEM 1 de 3:
   Cimento CP II 50kg — 200 sacos
   Entrega: Setor Bueno, Goiânia | Prazo necessário: até 09/05

   Qual o preço por saco?"

MixConstrução:
  "38,50"

CotAI:
  "✅ R$38,50/saco anotado.
   Tem estoque de 200 sacos disponível?"

MixConstrução:
  "sim, temos 300"

CotAI:
  "✅ Estoque confirmado.
   Em quantos dias úteis entrega no Setor Bueno?"

MixConstrução:
  "2 dias"

CotAI:
  "✅ 2 dias úteis.
   Aceita pagamento em 30 dias?"

MixConstrução:
  "sim"

CotAI:
  "✅ Perfeito!

   ─────────────────────────
   📦 ITEM 2 de 3:
   Ferro CA-50 3/8" (9,5mm) 12m — 20 barras
   Qual o preço por barra?"

MixConstrução:
  "47,00"

CotAI:
  "✅ R$47,00/barra.
   Tem as 20 barras disponíveis?"

MixConstrução:
  "tem"

CotAI:
  "✅ Mesmo prazo de 2 dias para o ferro?"

MixConstrução:
  "sim"

CotAI:
  "✅

   ─────────────────────────
   📦 ITEM 3 de 3:
   Tinta Suvinil Branco Neve 18L — 10 latas
   Qual o preço por lata?"

MixConstrução:
  "a suvinil eu não tenho, trabalho com Coral"

CotAI:
  "Entendido. Tem Coral Branco Neve 18L no mesmo padrão?
   (se sim, passo o preço como alternativa de marca)"

MixConstrução:
  "sim, 95 reais a lata"

CotAI:
  "✅ Coral Branco Neve 18L — R$95,00/lata como alternativa.

   ─────────────────────────
   📋 RESUMO DA SUA COTAÇÃO:

   Cimento CP II 50kg × 200: R$7.700 (R$38,50/un)
   Ferro CA-50 3/8" × 20:    R$940 (R$47,00/un)
   Coral Branco Neve × 10:   R$950 (R$95,00/un)
   ──────────────────────────
   Total estimado:            R$9.590
   Prazo entrega:             2 dias úteis
   Pagamento:                 30 dias
   NF:                        [Emite NF? sim/não]"

MixConstrução:
  "sim emite"

CotAI:
  "✅ Tudo anotado! Sua cotação foi registrada.
   Se você for selecionado, a gente te avisa aqui mesmo. 🤝"
```

---

### A Inteligência do Bot no Fluxo do Fornecedor

```
SITUAÇÕES QUE O BOT TRATA AUTOMATICAMENTE:

1. Fornecedor não tem o produto:
   "Não tenho cimento CP II"
   → Bot: "Tem CP III ou CPB como alternativa?"
   → Registra como "alternativa de produto"

2. Fornecedor manda preço ambíguo:
   "38 e meio"
   → Bot confirma: "R$38,50, correto?"

3. Fornecedor manda tabela em PDF ou imagem:
   → Claude Vision extrai os preços automaticamente
   → Bot confirma cada valor extraído antes de registrar

4. Fornecedor não responde em 2 horas:
   → Lembrete automático: "Oi! Ainda consegue me cotar os itens?"

5. Fornecedor responde parcialmente e some:
   → Após 1h: "Ficou faltando o item 2 e 3. Consegue completar?"
   → Após 3h: registra só o que foi cotado (parcial)

6. Fornecedor manda áudio:
   → Transcrição automática (WhatsApp já tem, ou Whisper API)
   → Extração dos valores do áudio

7. Fornecedor negocia no chat:
   "Se o pedido for acima de 300 sacos eu faço por 37"
   → Registra condição: "preço condicional ao volume"
   → Aparece no mapa como nota para o comprador
```

---

## O Mapa de Cotação — Entregue no WhatsApp

```
[Mensagem texto no WhatsApp — resumo executivo]

CotAI para Reformas Silva Ltda:

📊 MAPA DE COTAÇÃO — 07/05/2026
Pedido: Cimento + Ferro + Tinta
Fornecedores: 4 consultados | 3 responderam

─────────────────────────────────
🥇 MELHOR PREÇO TOTAL (um fornecedor):
   MixConstrução
   Cimento: R$7.700 | Ferro: R$940 | Tinta (Coral): R$950
   Total: R$9.590 | 30 dias | Entrega: 2 dias úteis

⚡ ENTREGA MAIS RÁPIDA:
   Casa do Construtor
   Total: R$10.120 | À vista | Entrega: amanhã

💰 MENOR PREÇO (dividindo o pedido):
   Construfort (cimento R$7.580) +
   Ferrodist (ferro R$870) +
   Tintas GO (tinta Suvinil R$980)
   Total: R$9.430 — economia de R$160 vs. MixConstrução
   ⚠️ 3 fornecedores = 3 entregas + 3 NFs

─────────────────────────────────
💡 RECOMENDAÇÃO:
MixConstrução. Prazo dentro do pedido (sexta), 30 dias,
uma entrega só. A economia de R$160 na opção dividida
não compensa a complexidade operacional para uma reforma.

Quer que eu envie o pedido para a MixConstrução? (sim/não)

📄 PDF completo com todos os preços item a item: [arquivo]

[PDF é enviado automaticamente junto com a mensagem]
```

---

## Arquitetura Técnica — WhatsApp First

```
NÚMERO CENTRAL DO COTAI
  → Empresa cadastrada recebe o número via WhatsApp
  → Cada empresa tem um "código" de identificação automático
    (não precisa de login — o número do celular é o identificador)

COMPRADOR LADO:

  WhatsApp do comprador → Webhook → Node.js
    ↓
  Claude API:
    → Extrai itens, quantidades, especificações, prazo, local
    → Identifica ambiguidades ("tinta branca" → qual marca? qual acabamento?)
    → Faz perguntas de clarificação se necessário
    → Normaliza: "ferro 3/8" → CA-50 9,5mm
    ↓
  Matching de fornecedores:
    → Banco de dados: fornecedor × categoria × região × histórico de resposta
    → Seleciona os 3-5 mais relevantes
    ↓
  Dispara RFQ para cada fornecedor via WhatsApp Business API

FORNECEDOR LADO:

  WhatsApp do fornecedor → Webhook → Motor de estado
    ↓
  Estado da conversa armazenado por fornecedor × cotação:
    "MixConstrução está no item 2 de 3 da cotação #4521"
    → Cada resposta avança o estado
    → Bot sabe exatamente qual pergunta fazer a seguir
    ↓
  Claude API parseia cada resposta:
    → Extrai valor numérico mesmo de texto informal
    → Detecta alternativas de produto, condições especiais
    → Confirma ambiguidades antes de registrar
    ↓
  Se resposta for PDF ou imagem:
    → Claude Vision extrai dados
    → Bot confirma os valores extraídos

GERAÇÃO DO MAPA:

  Após todos os fornecedores responderem (ou timeout de 3h):
    → Motor de comparação: preço × prazo × condição × NF
    → Algoritmo de recomendação
    → Geração do PDF (Puppeteer + HTML template)
    → Envio: mensagem texto resumo + PDF via WhatsApp

STACK:
  → Runtime: Node.js (TypeScript)
  → Banco: PostgreSQL + Redis (estados das conversas)
  → IA: Claude API (claude-opus-4-7 — extração + parsing + recomendação)
  → WhatsApp: Z-API (menor custo para MVP em BR) ou Twilio
  → PDF: Puppeteer
  → Fila: BullMQ (processamento assíncrono de cotações)
  → Infra: Railway (deploy simples, sem overhead)
```

---

## Motor de Estado das Conversas

```typescript
// Estado de uma cotação por fornecedor
interface ConversaFornecedor {
  cotacaoId: string
  fornecedorId: string
  whatsapp: string
  itens: ItemRFQ[]
  itemAtual: number
  respostas: RespostaItem[]
  estado: 'aguardando_aceite' | 'cotando' | 'completo' | 'recusado' | 'timeout'
  ultimaMensagem: Date
}

// Máquina de estados do bot para fornecedor
async function processarRespostaFornecedor(
  mensagem: string,
  conversa: ConversaFornecedor
): Promise<MensagemBot> {

  switch (conversa.estado) {

    case 'aguardando_aceite':
      const aceite = await claude.classify(mensagem, ['sim', 'não', 'ambíguo'])
      if (aceite === 'sim') {
        conversa.estado = 'cotando'
        return perguntarItem(conversa.itens[0])
      }
      if (aceite === 'não') {
        conversa.estado = 'recusado'
        return { texto: "Tudo bem! Se mudar de ideia é só falar. 👍" }
      }
      return { texto: "Pode confirmar? Consegue me ajudar com essa cotação? (sim/não)" }

    case 'cotando':
      const item = conversa.itens[conversa.itemAtual]
      const campo = proximoCampoNaoPreenchido(conversa.respostas, item)

      // Extrai o valor do campo atual da mensagem em linguagem natural
      const valor = await claude.extract({
        mensagem,
        campo,        // 'preco_unitario' | 'prazo_dias' | 'condicao' | 'estoque' | 'emite_nf'
        item,
        contexto: conversa.respostas
      })

      if (valor.ambiguo) {
        return { texto: valor.perguntaEsclarecedora }
      }

      // Registra a resposta
      conversa.respostas.push({ campo, valor: valor.extraido, itemId: item.id })

      // Verifica se o item está completo
      if (itemCompleto(conversa.respostas, item)) {
        conversa.itemAtual++

        if (conversa.itemAtual >= conversa.itens.length) {
          // Todos os itens cotados
          conversa.estado = 'completo'
          return gerarResumoParaFornecedor(conversa)
        }

        // Próximo item
        return perguntarItem(conversa.itens[conversa.itemAtual])
      }

      // Mais campos do mesmo item
      return perguntarCampo(campo, item)
  }
}

// O que perguntar por campo
function perguntarCampo(campo: string, item: ItemRFQ): MensagemBot {
  const perguntas = {
    preco_unitario: `Qual o preço por ${item.unidade}?`,
    prazo_dias:     `Em quantos dias úteis entrega?`,
    condicao:       `Aceita pagamento em 30 dias?`,
    estoque:        `Tem as ${item.quantidade} ${item.unidade} disponíveis?`,
    emite_nf:       `Emite nota fiscal?`
  }
  return { texto: perguntas[campo] }
}
```

---

## Modelo de Receita

### Para o comprador

| Plano | Preço | Limite |
|-------|-------|--------|
| **Starter** | R$199/mês | 10 cotações/mês |
| **Pro** | R$399/mês | 30 cotações/mês, itens ilimitados |
| **Enterprise** | R$899/mês | Ilimitado, múltiplos usuários via WhatsApp |
| **Avulso** | R$29/cotação | Sem assinatura |

### Para o fornecedor

O fornecedor **não paga para responder** — ele recebe leads qualificados gratuitamente.
Isso é o que cria o incentivo para responder.

Monetização futura do fornecedor:
- **Destaque na listagem:** R$99/mês para aparecer primeiro no matching
- **Analytics:** R$149/mês para ver win rate, perda de preço por produto, histórico

### Unit economics

```
CAC comprador (outbound B2B + associações): R$400
ARPU médio: R$299/mês
Churn: 5%/mês
LTV: R$5.980

Custo por cotação (Claude API + WhatsApp + infra): ~R$3-8
Margem por cotação: alta (custo fixo de assinatura, custo variável baixo)
```

---

## Roadmap

### Semana 1-4 — Validação zero-código
```
→ Número de WhatsApp do CotAI ativo (Z-API básico)
→ Comprador manda pedido → analista humano extrai manualmente (com Claude)
→ Analista envia mensagens para fornecedores no WhatsApp (manualmente)
→ Registra respostas em planilha
→ Gera mapa em Google Sheets, envia PDF
→ Cobra R$29 por cotação via PIX
→ Meta: 20 cotações em 30 dias
→ Valida: comprador paga? Fornecedor responde? Em quanto tempo?
```

### Mês 2 — Automação do lado do comprador
```
→ Bot WhatsApp extrai pedido automaticamente (Claude API)
→ Faz perguntas de clarificação automaticamente
→ Disparo de RFQ para fornecedores ainda semi-manual
→ Meta: 50 cotações/mês com 1 operador
```

### Mês 3 — Automação do lado do fornecedor
```
→ Bot conduz o fornecedor item por item (máquina de estados)
→ Parsing automático de respostas (Claude API)
→ Follow-up automático para não-respondentes
→ Geração de PDF e entrega automática
→ Meta: 100 cotações/mês sem operador para 90% dos casos
```

### Mês 4-6 — Qualidade e escala
```
→ Score de fornecedor: taxa de resposta, aderência ao preço cotado
→ Feedback loop: comprador avalia se o vencedor entregou no prazo e preço
→ Expansão de categorias (construção → saúde → alimentação)
→ Planos de assinatura lançados
→ Meta: 50 compradores pagantes, 300 fornecedores na rede
```

---

## Por Que Funciona no Brasil

```
1. WHATSAPP É A INFRAESTRUTURA DE NEGÓCIOS DAS PMEs BRASILEIRAS
   O comprador já cotou no WhatsApp. O fornecedor já respondeu no WhatsApp.
   O CotAI não muda o canal — organiza o que já acontece.

2. O FORNECEDOR TEM INCENTIVO PARA RESPONDER
   Hoje ele recebe pedidos de cotação no WhatsApp pessoal, sem organização.
   O CotAI chega com pedido qualificado, escopo claro, pronto para responder.
   Responder é mais fácil, não mais difícil.

3. A BARREIRA DE ENTRADA É ZERO
   Comprador: salva o número e manda mensagem.
   Fornecedor: responde quando o CotAI manda.
   Ninguém instala nada, acessa nenhum portal, aprende nenhum sistema.

4. O MODELO DE PERGUNTAS É NATURAL
   "Qual o preço?" → responde o preço.
   "Em quantos dias entrega?" → responde o prazo.
   É uma conversa. Brasileiro sabe ter conversa no WhatsApp.

5. NENHUM CONCORRENTE FAZ ISSO AQUI
   Mercado Eletrônico é para grandes empresas.
   Portais de cotação exigem cadastro e login.
   O CotAI é WhatsApp puro — é diferente de tudo que existe.
```

---

## Nome e Posicionamento

### Nome: CotAI

**CotAI** = Cota + AI. Limpo, direto, comunica o produto inteiro.
O "AI" sinaliza tecnologia sem precisar explicar.
Funciona como marca e como descrição ao mesmo tempo.

**Pronúncia:** "co-TA-ai" — natural em português.
"Manda pro CotAI" — funciona como verbo de encaminhamento.

**Domínio:** cotai.com.br / cotai.app

### Tagline

> *"Fala o que precisa. O CotAI cota."*

Para o fornecedor:
> *"Receba pedidos qualificados direto no WhatsApp. De graça."*

### Posicionamento

```
Para o comprador:
  "Você já cotou no WhatsApp. Só que você fazia o trabalho.
   Agora o CotAI faz."

Para o fornecedor:
  "Seus clientes cotam com você pelo WhatsApp. Agora de forma
   organizada, um item de cada vez, sem mensagem perdida."
```

---

## Conexão com o Portfólio

```
Construtora usa o CotAI para comprar material de obra
  ↓
Assina: "Você aluga imóvel para funcionários?
  Faça o contrato e a vistoria digital."
  ↓
Campo Certo: "Compra insumos do agro? Tem ITR e CAR em dia?"

Clínica usa o CotAI para cotar suprimentos médicos
  ↓
Bismarck: "Plano de saúde negou um procedimento do seu paciente?
  A gente contesta automaticamente."

O CotAI é o produto B2B mais fácil de combinar com os outros:
o cliente é a empresa, e toda empresa tem múltiplas dores.
```

---

## Resumo Executivo

**O produto:** agente de IA para cotação de suprimentos B2B 100%
pelo WhatsApp. Comprador fala o que precisa em linguagem natural.
Bot conduz cada fornecedor por um roteiro de perguntas no WhatsApp.
Mapa de cotação comparativo é gerado e devolvido automaticamente.

**Por que WhatsApp:** é onde comprador e fornecedor já estão.
Sem portal, sem app, sem login, sem formato para memorizar.
O fornecedor responde porque é mais fácil que o jeito atual.

**O cliente:** PMEs com compras recorrentes de suprimentos —
construtoras, clínicas, restaurantes. Foco inicial: GO + DF.

**O modelo:** assinatura R$199-399/mês para o comprador.
Fornecedor recebe leads qualificados de graça — isso é o que
constrói a rede e é o que diferencia o produto de qualquer concorrente.

**Nome:** CotAI
**Tagline:** "Fala o que precisa. O CotAI cota."
