# Farol — Agência Digital Automatizada

Encontra negócios sem presença digital. Cria o site antes de ser contratada.
Manda o mockup pronto. O cliente vê, aprova e em 48h está no ar.
Todo o fluxo automatizado — sem reunião, sem proposta, sem espera.

---

## O Conceito

A venda tradicional de site funciona assim:
reunião de briefing → proposta de 10 páginas → aprovação → desenvolvimento
→ rodadas de ajuste → lançamento. 30-60 dias. R$3.000-10.000.

O cliente nunca contratou porque o processo era longo demais,
caro demais, e ele não sabia se o resultado ia ser bom.

A Farol inverte:

```
JEITO TRADICIONAL:            JEITO FAROL:

Reunião                       Bot encontra o negócio
  ↓                             ↓
Briefing                      IA cria o site
  ↓                             ↓
Proposta                      WhatsApp entrega o mockup
  ↓                             ↓
Aprovação                     Cliente aprova
  ↓                             ↓
Desenvolvimento               48h: site no ar
  ↓
Ajustes
  ↓
Lançamento

30-60 dias                    3-5 dias
R$3.000+                      R$697 + R$97/mês
Sem certeza do resultado      O cliente já viu como fica
```

O produto não é o site. É a ausência de fricção.

---

## O Mercado

```
Brasil: 20M+ PMEs ativas
Com site funcional e profissional: estimativa de 25% (~5M)
Sem site ou com site que "envergonha": ~15M negócios

Em Goiânia:
  → 180.000+ CNPJs ativos (JUCESP-GO)
  → Estimativa de 60-70% sem site ou com site inadequado
  → 100.000+ negócios como mercado endereçável só na capital

Setores com menor adoção digital e maior dor visível:
  → Clínicas e consultórios odontológicos e médicos
  → Oficinas mecânicas
  → Salões de beleza e barbearias
  → Restaurantes e lanchonetes
  → Escritórios de contabilidade e advocacia
  → Lojas de materiais de construção
  → Academias e estúdios de pilates / crossfit
  → Farmácias de manipulação
  → Óticas
  → Autoescolas
```

---

## O Fluxo Automatizado — Ponta a Ponta

```
ETAPA 1: PROSPECÇÃO AUTOMÁTICA
  Bot Google → encontra negócios sem site ou com site ruim
  ↓

ETAPA 2: GERAÇÃO DO SITE
  IA pega dados públicos do negócio → cria o site completo
  ↓

ETAPA 3: OUTREACH
  WhatsApp automático → manda o mockup pronto para o dono
  ↓

ETAPA 4: CONVERSÃO
  Cliente aprova → paga → site vai ao ar em 48h
  ↓

ETAPA 5: RETENÇÃO
  Assinatura mensal → hospedagem + manutenção + atualizações
```

Nenhuma dessas etapas tem intervenção humana no fluxo padrão.
Humano só entra em edge cases: cliente pede algo fora do padrão,
disputa de cobrança, negócio com necessidade especial.

---

## ETAPA 1 — Prospecção Automática

### Encontrar negócios sem site

```python
# Pipeline de prospecção via Google Places API

def prospectar_sem_site(cidade: str, categoria: str, limite: int = 500):
    resultados = []

    # Busca negócios na categoria + cidade
    lugares = google_places.search(
        query=f"{categoria} em {cidade}",
        location=COORDENADAS[cidade],
        radius=30000,  # 30km
        limit=limite
    )

    for lugar in lugares:
        detalhes = google_places.get_details(lugar.place_id)

        # Sem site cadastrado = alvo primário
        if not detalhes.website:
            resultados.append({
                "nome": detalhes.name,
                "telefone": detalhes.phone,
                "endereco": detalhes.address,
                "categoria": categoria,
                "fotos": detalhes.photos[:5],
                "avaliacao": detalhes.rating,
                "reviews": detalhes.reviews[:3],
                "horario": detalhes.opening_hours,
                "google_maps_url": detalhes.url,
                "alvo": "sem_site"
            })

        # Tem site? Verifica a qualidade
        elif detalhes.website:
            score = avaliar_qualidade_site(detalhes.website)
            if score < 40:  # Site ruim
                resultados.append({ ..., "alvo": "site_ruim", "score": score })

    return resultados

def avaliar_qualidade_site(url: str) -> int:
    score = 100

    checks = {
        "mobile_friendly":  verificar_mobile(url),      # -25 se não
        "ssl":              url.startswith("https"),     # -20 se não
        "velocidade":       medir_lcp(url) < 3.0,       # -20 se não
        "tem_telefone":     extrair_telefone(url),       # -10 se não
        "atualizado":       verificar_data_copyright(url) >= 2022,  # -15 se não
        "tem_conteudo":     contar_palavras(url) > 200,  # -10 se não
    }

    for check, passou in checks.items():
        if not passou:
            score -= PENALIDADES[check]

    return max(0, score)
```

### Volume esperado por rodada

```
Goiânia — clínicas odontológicas:
  → Google retorna ~2.000 resultados
  → Sem site: ~800 (40%)
  → Site ruim (score < 40): ~400 (20%)
  → Total de alvos: ~1.200 por categoria × cidade

Rodada completa (10 categorias × Goiânia):
  → ~12.000 alvos qualificados
  → Com telefone disponível para WhatsApp: ~70% = 8.400
```

---

## ETAPA 2 — Geração Automática do Site

```
DADOS DE ENTRADA (todos públicos — sem pedir nada ao cliente):
  → Nome do negócio (Google Places)
  → Endereço e CEP (Google Places)
  → Telefone (Google Places)
  → Horário de funcionamento (Google Places)
  → Fotos (Google Places Photos API)
  → Avaliação e reviews selecionados (Google Places)
  → Categoria do negócio (Google Places)

PROCESSO DE GERAÇÃO:

  1. Seleção de template por categoria:
     odontologia → template_clinica_dental
     mecânica    → template_oficina_mecanica
     beleza      → template_salao_beleza
     (30+ templates, cada um com layout específico para o setor)

  2. Claude API gera o conteúdo:
     → Headline principal: "Seu sorriso é a nossa missão"
     → Sobre: "O Consultório Sorriso Perfeito atende em Goiânia
       há X anos, oferecendo..."
     → Lista de serviços (inferida pela categoria + reviews)
     → Call to action: "Agende sua consulta pelo WhatsApp"

  3. População automática do template:
     → Nome, endereço, telefone, horário
     → Fotos do Google Places (as melhores por score de qualidade)
     → Reviews reais do Google (os mais completos e positivos)
     → Mapa do Google Maps embutido

  4. Otimizações automáticas:
     → Mobile-first (responsivo por padrão)
     → SSL ativo
     → Meta title e description gerados por IA
     → Schema markup (SEO local — LocalBusiness)
     → Velocidade < 2s (template otimizado)

  5. Preview URL gerada:
     → preview.farol.app/clinica-sorriso-perfeito-goiania
     → URL única por negócio, válida por 30 dias
     → Rastreia: visualizações, tempo na página, cliques no CTA
```

---

## ETAPA 3 — Outreach via WhatsApp

```
MENSAGEM ENVIADA PARA O DONO DO NEGÓCIO:

[Número do WhatsApp Farol → número do negócio no Google]

"Oi! Sou do Farol 👋

Montei uma versão do site da *[Nome do Negócio]* pra você ver
como ficaria online:

🔗 preview.farol.app/nome-do-negocio

Usei as fotos e informações que já estão no Google.
Em 48h coloco no ar — do jeito que está ou com ajustes.

Se não gostar: não tem problema, sem custo.
Se gostar: R$697 pra lançar + R$97/mês pra manter."

───────────────────────────────

FOLLOW-UP (3 dias sem resposta):

"Oi! Você chegou a ver o site que montei pra [Nome]?
Só quero garantir que chegou:
🔗 preview.farol.app/nome-do-negocio"

───────────────────────────────

FOLLOW-UP 2 (7 dias sem resposta):

"Última vez que escrevo 😄
O preview da [Nome] fica disponível por mais 23 dias.
Se quiser ver: preview.farol.app/nome-do-negocio
Se não rolar agora, sem problema! Fica com o link."

───────────────────────────────

RESPOSTA AUTOMATIZADA PARA "quanto custa?":

"Simples assim:
📌 R$697 para criar e lançar (domínio incluído)
📌 R$97/mês para manter no ar (hospedagem + atualizações)

Se quiser ajustar qualquer coisa antes de lançar — nome,
fotos, textos — é só me falar aqui. A gente muda."

RESPOSTA PARA "quero mudar o texto do sobre":

→ Bot coleta as alterações pelo WhatsApp
→ IA edita o site automaticamente
→ Preview atualizado em minutos
→ "Pronto! Dá uma olhada: preview.farol.app/nome"
```

---

## ETAPA 4 — Conversão e Lançamento

```
APROVAÇÃO:
  Cliente: "Gostei! Quero esse."

  Bot: "Ótimo! 🎉 Pra lançar:

  1️⃣ Me confirma o e-mail para cadastro
  2️⃣ Já tem domínio? (tipo seusite.com.br)
     Se não: a gente registra por R$40/ano incluso

  Pagamento: [link Asaas — PIX ou cartão parcelado]"

APÓS PAGAMENTO CONFIRMADO:
  → Domínio registrado automaticamente (API Registro.br)
  → DNS configurado automaticamente
  → Site publicado no domínio do cliente
  → SSL ativo em minutos (Let's Encrypt)
  → Google My Business linkado
  → E-mail de confirmação com login do painel

  Bot: "Site no ar! 🚀
  Acesse: seusite.com.br
  Painel de edições: painel.farol.app
  Qualquer atualização: é só me mandar aqui no WhatsApp."

PRAZO REAL DE LANÇAMENTO:
  → Negócio sem domínio: 24-48h (propagação de DNS)
  → Negócio com domínio existente: 4-8h
```

---

## ETAPA 5 — Retenção e Manutenção

```
O QUE INCLUI O R$97/MÊS:

Técnico (invisível para o cliente):
  → Hospedagem em servidor dedicado (sem lentidão)
  → SSL renovado automaticamente
  → Backups diários automáticos
  → Monitoramento de uptime (alerta se site cair)
  → Atualizações de segurança automáticas

Atendimento (via WhatsApp):
  → Até 2 atualizações de conteúdo por mês
    ("muda o telefone" / "adiciona esse novo serviço" / "tira essa foto")
  → Resposta em até 4h úteis

ATUALIZAÇÕES VIA WHATSAPP:

  Cliente: "Muda meu telefone para (62) 99999-1234"
  Bot coleta → IA edita → "Pronto! Já está atualizado no site."

  Cliente: [envia foto nova]
  Bot: "Qual página colocar essa foto? (início / sobre / serviços)"
  Cliente: "início"
  Bot: "✅ Foto adicionada na página inicial."

RELATÓRIO MENSAL AUTOMÁTICO:
  → Visitas ao site no mês
  → De onde vieram (Google, WhatsApp, direto)
  → Quantos cliques no botão de WhatsApp (CTA principal)
  → Posição no Google para "[negócio] + [cidade]"
  Enviado no WhatsApp todo dia 1º.

ADD-ONS (receita extra):
  → Google Meu Negócio configurado e otimizado: R$297 único
  → WhatsApp Business profissional configurado: R$197 único
  → Fotos profissionais (parceiro fotógrafo GO + DF): R$397
  → Loja virtual básica (até 20 produtos): R$997 + R$49/mês extra
  → Link de agendamento online (Calendly-like): R$147/mês
```

---

## Arquitetura Técnica

```
PROSPECÇÃO
  → Google Places API (prospecção de alvos)
  → Playwright (verificação de qualidade de sites existentes)
  → Google PageSpeed API (score de velocidade)
  → Banco de alvos: PostgreSQL com status do pipeline
    (prospectado → site gerado → outreach → respondeu → converteu → ativo)

GERAÇÃO DE SITES
  → Templates: Next.js estático (30+ templates por setor)
  → Geração de conteúdo: Claude API (claude-opus-4-7)
  → Fotos: Google Places Photos API + otimização (sharp)
  → Preview hosting: Vercel ou Cloudflare Pages (grátis por preview)
  → Build: geração de arquivo estático por negócio → deploy em 30s

OUTREACH
  → WhatsApp Business API: Z-API (BR, custo menor) ou Twilio
  → Rastreamento de preview: pixel de abertura + evento de clique
  → Máquina de estados de follow-up (BullMQ com delays)
  → Rate limiting: máximo 100 mensagens/hora por número (evitar ban)

CONVERSÃO
  → Pagamento: Asaas (PIX + cartão)
  → Domínio: Registro.br API (automático)
  → DNS: Cloudflare API (propagação rápida)
  → SSL: Let's Encrypt via Certbot (automático)

MANUTENÇÃO
  → Painel do cliente: Next.js (edições simples de conteúdo)
  → Edições via WhatsApp: bot coleta → Claude edita HTML/conteúdo
    → deploy automático
  → Monitoramento de uptime: Better Uptime (alerta + histórico)
  → Analytics: Plausible (leve, sem cookie banner, LGPD ok)

STACK CENTRAL
  → Backend: Node.js (Fastify) + PostgreSQL
  → Sites gerados: Next.js estático (performance + SEO)
  → IA: Claude API (geração de conteúdo + edições via WhatsApp)
  → Deploy de sites: Cloudflare Pages (grátis, rápido, global)
  → Infra Farol: Railway (backend + banco)
```

---

## Modelo de Receita

```
SETUP (one-time):        R$697 por site lançado
  Inclui: criação, domínio 1 ano, lançamento, configuração

MENSAL (recorrente):     R$97/mês por site ativo
  Inclui: hospedagem, SSL, manutenção, 2 atualizações, relatório

ADD-ONS:                 R$147-997 por serviço adicional
```

### Unit economics

```
CAC: R$0 (outreach automático — custo é só o tempo de máquina)
  → Custo real por lead prospectado: R$0,30 (API Google + IA)
  → Custo real por outreach: R$0,05 (WhatsApp)
  → Custo total por cliente convertido (8% de conversão): R$4,20

Setup: R$697
Margem do setup: ~R$580 (custo: domínio R$40 + infra R$77)

Mensal: R$97
Custo mensal por cliente: R$12-18 (hospedagem + WhatsApp + IA)
Margem mensal: ~R$80

Churn estimado: 3%/mês
LTV: R$697 + (R$80 × 33 meses) = R$3.337

Payback: menos de 1 mês
```

### Projeção de escala

```
Rodada mensal de prospecção:
  → 8.000 WhatsApps enviados (Goiânia, 10 categorias)
  → Taxa de resposta: 15% = 1.200 respostas
  → Taxa de conversão dos que respondem: 12% = 144 novos clientes/mês

Receita mensal Ano 1 (acumulada):
  → Mês 3: 432 clientes × R$97 = R$41.904/mês recorrente
  → Mês 6: 864 clientes × R$97 = R$83.808/mês recorrente
  → Mês 12: 1.728 clientes × R$97 = R$167.616/mês recorrente
    + setup fees (144/mês × R$697) = R$100.368/mês
  → Total Mês 12: ~R$268.000/mês → R$3,2M/ano

(Com churn de 3%: base real ~1.400 clientes no mês 12)
```

---

## Por Que Funciona

```
1. VOCÊ JÁ VÊ COMO VAI FICAR
   Nenhuma agência faz isso. Você sempre assina sem saber o resultado.
   A Farol inverte: você vê primeiro, decide depois.
   Eliminação de risco = eliminação da principal objeção.

2. CAC PRÓXIMO DE ZERO
   Prospecção automatizada via Google + WhatsApp automático.
   Não tem vendedor, não tem reunião, não tem proposta.
   O único custo de aquisição é o custo de API — centavos por cliente.

3. TICKET ACESSÍVEL PARA QUEM NUNCA TEVE SITE
   R$697 é o que o cliente paga sabendo o que vai receber.
   R$97/mês é menos que um plano de celular.
   A decisão é fácil porque o risco é baixo e o resultado é visível.

4. MANUTENÇÃO VIA WHATSAPP É IMPOSSÍVEL DE CHURNAR
   "Muda meu telefone" → feito em minutos.
   O cliente nunca cancela porque nunca precisa fazer nada.
   A fricção de cancelar é maior que a fricção de manter.

5. O MODELO ESCALA SEM CUSTO FIXO RELEVANTE
   Cada novo cliente custa R$4 para adquirir e R$15 para atender.
   1.000 clientes = R$97.000/mês com R$15.000 de custo variável.
   Não tem escritório, não tem equipe de vendas, não tem reunião.
```

---

## Roadmap

### Semana 1-2 — Validação manual
```
→ Prospectar 50 negócios manualmente (Google Maps)
→ Criar 10 mockups manualmente (Wix ou Framer — sem automação ainda)
→ Mandar pelo WhatsApp pessoal: "Montei um site pra você. Quer ver?"
→ Meta: 2-3 conversões em R$697
→ Aprende: qual categoria converte mais? Qual mensagem funciona?
→ Não constrói nada até validar que as pessoas pagam
```

### Semana 3-4 — Automação da geração de site
```
→ Template em Next.js para a categoria que mais converteu
→ Script que puxa dados do Google Places e popula o template
→ Claude API gera os textos automaticamente
→ Preview URL funcionando
→ Ainda envia manualmente pelo WhatsApp
→ Meta: gerar 1 site por hora de trabalho (vs. 1 por dia na semana anterior)
```

### Mês 2 — Automação do outreach
```
→ WhatsApp Business API conectado (Z-API)
→ Script de prospecção roda automaticamente
→ Outreach + follow-up automatizados
→ Humano só acompanha as respostas e fecha a venda
→ Meta: 500 WhatsApps/semana, 30 conversões/mês
```

### Mês 3 — Lançamento automático
```
→ Pagamento via Asaas integrado
→ Registro de domínio automático (Registro.br API)
→ Deploy automático após pagamento confirmado
→ Onboarding 100% via WhatsApp
→ Meta: do pagamento ao site no ar sem nenhuma ação humana
```

### Mês 4-6 — Retenção e expansão
```
→ Painel do cliente para edições simples
→ Relatório mensal automático via WhatsApp
→ Edições via WhatsApp (Claude edita o site pelo chat)
→ Expansão para Brasília e Anápolis
→ Novas categorias a cada 2 semanas
→ Meta: 500 clientes ativos, R$48.500/mês recorrente
```

---

## Nome e Posicionamento

### Nome: Farol

Farol ilumina o caminho. Para negócios no escuro digital,
o Farol aparece e mostra o caminho.

Dupla metáfora: encontra (a Farol encontra você) e guia
(a Farol te coloca no caminho digital).

**Tagline:**
> *"Seu negócio já existe. A gente coloca ele no mapa."*

Ou mais direto:
> *"Criamos seu site antes de você contratar a gente."*

### Tom de voz

```
Sem jargão de agência.
Sem "soluções disruptivas" ou "presença omnichannel".
Fala como o dono da barbearia entende.

"Fiz um site pra sua barbearia. Dá uma olhada."
"Não gostou? Muda o que quiser. Sem custo."
"Gostou? Em 48h tá no ar."

Direto. Concreto. Sem enrolação.
```

---

## Conexão com o Portfólio

```
Cliente da Farol (dono do negócio local)
  ↓
CotAI: "Você compra suprimentos pra seu negócio?
  A gente cota pra você pelo WhatsApp."
  ↓
Postou: "Quer que a gente cuide do Instagram também?
  Todo mês, automatizado."
  ↓
MEI Automatizado: "Seu DAS está em dia?
  A gente emite e paga por você."
  ↓
Assina: "Você aluga o imóvel do seu negócio?
  Faça o contrato digital."

O dono do negócio local é o cliente com maior sobreposição
de dores com o portfólio inteiro.
A Farol é a porta de entrada — o primeiro produto que ele encontra,
porque o produto vai até ele, não espera ele vir até o produto.
```

---

## Resumo Executivo

**O produto:** agência digital automatizada que encontra negócios sem
presença digital, cria o site antes de ser contratada, manda o mockup
pelo WhatsApp e lança em 48h após aprovação. Manutenção e atualizações
via WhatsApp pelo preço de um almoço por semana.

**O diferencial:** o cliente vê o resultado antes de pagar.
Nenhuma agência faz isso. Elimina a principal objeção de compra.

**O modelo:** R$697 setup + R$97/mês. CAC de R$4.
LTV de R$3.337. Margem bruta de ~85%.

**Por que escala:** prospecção via Google API + geração via IA +
outreach via WhatsApp = custo variável próximo de zero por cliente.
1.000 clientes não exigem 1.000 horas de trabalho — exigem o mesmo
número de servidores que 100 clientes.

**Nome:** Farol
**Tagline:** "Seu negócio já existe. A gente coloca ele no mapa."
