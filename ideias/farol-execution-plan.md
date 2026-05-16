# Farol — Execution Plan

## Context

Build a zero-touch digital agency for Brazilian local businesses with no web
presence. The product finds businesses without sites via Google Places API,
generates a personalized site using the business's own public data (name,
photos, reviews, hours, address), and delivers the mockup via WhatsApp before
anyone is hired. The client sees the finished product before deciding. If they
approve: R$697 setup, site live in 48h, R$97/month ongoing.

Business thesis: "Seu negócio já existe. A gente coloca ele no mapa." The
conversion insight — showing the result before requesting payment — eliminates
the primary objection of traditional agency sales (you never know what you'll
get). CAC approaches zero because prospecting and outreach are automated.

Target market: 15M+ Brazilian businesses without a functional website.
GO + DF as launch market: 180k+ CNPJs active in Goiânia, estimated 60-70%
without a site or with a site that scores below 40/100 on mobile, SSL,
speed, and content completeness.

There is no direct Brazilian equivalent. Incumbents are traditional agencies
(R$3k-10k, 30-60 days, you don't see it until it's done), DIY builders
(Wix/Squarespace — requires skill and time the owner doesn't have), or
low-cost freelancers (slow, inconsistent, no maintenance).

---

## Weak Spots Identified

### Business Risks

**1. WhatsApp outreach gets the number banned**
WhatsApp aggressively bans numbers that send unsolicited messages at volume.
A ban kills the core acquisition channel overnight.

Fix: WhatsApp Business API via official provider (360dialog or Twilio) — not
unofficial tools (Z-API risks ban at scale). Rate-limit to 80 messages/hour
per number. Warm up each number over 14 days (start with 20/day, increase
10%/day). Monitor spam report rate via Meta Business Manager. Have 3 numbers
in rotation; if one gets restricted, others continue. Long-term: opt-in list
from SEO/landing pages converts better anyway.

**2. Legal gray area — generating a site using someone's brand without consent**
Creating and hosting a site with someone's business name before they hire you
could be argued as trademark misuse or unauthorized use of brand.

Fix: The preview is a proposal, not a live published site. robots.txt noindex
on all preview URLs. Preview page includes explicit header: "Este é um modelo
criado pela Farol como proposta. Não está publicado na internet." Site goes
live ONLY after explicit approval + payment. Legal precedent: design agencies
show mockups with client brand before contract — standard practice. Consult
OAB on terms of service language before launch.

**3. Google Places API photos have usage restrictions**
Google Places Photos API terms prohibit certain commercial uses of photos
(storing them, redistributing without attribution). Using them directly in
generated sites risks ToS violation.

Fix: Two-layer approach. Preview phase: photos served via Google CDN (Places
Photo API URL, not stored). After client approves: explicitly ask client to
provide 3-5 photos of their business for the final published site. Automates
preview, keeps legal compliance for live sites. Adds a human touchpoint that
improves quality anyway.

**4. Preview sites indexed before client approves**
If Google crawls preview.farol.app/business-name before the client approves,
the business appears online without consent — and with potential errors.

Fix: All preview URLs behind robots.txt Disallow. Every page has
`<meta name="robots" content="noindex, nofollow">`. Preview subdomain also
blocked via Cloudflare DNS from public Google indexing. Published sites
(post-payment) get SEO treatment — opposite of preview.

**5. Template exhaustion at scale — sites look identical**
With 5 templates per category, by client #50 in a neighborhood, the sites
start looking the same. Local businesses talk to each other.

Fix: Color palette, font pairing, and layout variant are parameterized and
assigned uniquely per business (hash of CNPJ → deterministic variant).
Claude generates unique copy per business (not templated text). Client can
request design changes before launch. At 300+ clients, introduce 2nd-gen
templates.

**6. Client churn when business closes or owner dies**
Brazilian small business mortality is high (~50% close in 5 years). Churn
from business closure is unrecoverable — different from churn from
dissatisfaction.

Fix: Underwrite this into unit economics (churn modeled at 5%/month, not 3%).
Offer annual plan at R$870/year (25% discount vs monthly) — reduces churn
from casual cancellation. Add value monthly: Google ranking report, visitor
count, WhatsApp button click-through rate. Makes cancellation feel like
giving up a working asset, not just canceling a subscription.

**7. Registro.br has no API for .com.br registration**
Registro.br, the Brazilian domain registrar, requires going through an
accredited registrar. There's no direct public API for programmatic
.com.br registration.

Fix: Use Cloudflare Registrar API for .com domains (full API, R$50/year,
instant). For .com.br: partner with a registrar that has API access
(Locaweb, HostGator BR, or UOL Host all have partner APIs). In MVP,
.com domains only — faster, cheaper, and most SMBs don't have a preference.
Offer .com.br as paid upgrade (R$60/year) via manual process until API
is established.

### Infrastructure Risks

**1. WhatsApp number banned mid-campaign**
Described above in business risks. Infrastructure mitigation:

Fix: Abstract WhatsApp sending behind a queue (BullMQ). Queue consumers are
swappable per number/provider. Number rotation logic: if provider returns
4xx/banned error, route to backup number. Monitor Meta Business Manager
API for quality rating degradation before ban happens.

**2. Preview site hosting costs at scale**
Each generated preview is a Next.js static site. At 10,000 previews/month,
Vercel free tier is exceeded immediately.

Fix: Previews are NOT deployed as separate Vercel projects. They are routes
on a single Next.js app: `/preview/[slug]` — data is fetched from Supabase
at request time (SSR). One Vercel project serves all previews. Cost: $20/mo
Vercel Pro handles 1M requests. Published (paid) client sites live on
Cloudflare Pages — free, unlimited sites, fast global CDN.

**3. Google Places API costs at prospecting scale**
Places API Details call (needed for phone, hours, photos) costs $17/1,000
requests. Prospecting 10,000 businesses/month = $170 in API costs.

Fix: Cache aggressively — store all Places API responses in Supabase. Re-use
cached data for 90 days before refreshing. Only fetch Details for businesses
that pass the "no website" filter from the cheaper Nearby Search ($0/1,000
for basic fields). Estimated real cost: $30-50/month at 10k prospects.

**4. Single failure point on domain + DNS at launch**
If Cloudflare Registrar API or DNS propagation fails post-payment, client
waits and loses trust immediately after paying.

Fix: Deploy client sites first to farol.app/clientname subdomain (instant,
no DNS wait). Send client this URL immediately after payment. Custom domain
setup runs in parallel, auto-switches when DNS propagates (usually 1-4h via
Cloudflare). Client has a working URL in under 10 minutes; custom domain is
a bonus that arrives later.

**5. LGPD on business owner data**
The prospecting pipeline stores business owner phone numbers, photos, and
potentially CPF (if CNPJ lookup includes owner data). This is personal data
under LGPD.

Fix: Store only publicly available data (from Google Maps, which the business
owner made public). Do not acquire owner CPF at any stage. Phone numbers
stored with explicit "business contact" classification, not "personal contact."
Opt-out link in every WhatsApp message: "Para não receber mais mensagens:
[link]." Opt-outs honored immediately. Privacy policy explicit about source
of data.

---

## Product Architecture

### Core Modules

| Module | What it does | Brazil-specific delta |
|--------|-------------|----------------------|
| **Prospect Engine** | Google Places API scans for businesses without sites or with low-quality sites; scores each lead | Google Maps dominance in BR = 95%+ of local businesses listed; rich data source |
| **Site Generator** | Claude API pulls business data + populates category-specific Next.js template; generates unique copy, layout variant, color scheme | Portuguese templates by sector; Google reviews in PT-BR; Brazilian phone format (WhatsApp button, not call) |
| **Preview Delivery** | Preview URL per business, tracked (opens, time on page, CTA clicks); WhatsApp message with link + follow-up sequence | WhatsApp-first (not email); BR open rates on WhatsApp ~90% vs email ~22% |
| **Conversion Flow** | Client approves via WhatsApp; Asaas generates PIX/boleto; post-payment: domain + DNS + deploy automated | PIX instant settlement; no credit card required; domain via Cloudflare API |
| **Client Dashboard** | Landlord-style portal: site analytics, visitor count, WhatsApp button clicks, Google ranking position | Plausible Analytics (LGPD compliant, no cookie banner required) |
| **Update Engine** | Client sends change request via WhatsApp; Claude edits content; auto-redeploys | WhatsApp-native: "muda meu telefone" → done in minutes; no login needed for updates |
| **Retention Layer** | Monthly report via WhatsApp: visitors, ranking, CTAs; proactive suggestions ("adicionar foto nova aumenta engajamento") | Report delivered where client lives (WhatsApp), not where they don't (email) |

### What NOT to Build (MVP)

- Tenant screening / credit analysis (wrong product)
- E-commerce / online store (Year 2 add-on only)
- Social media management (separate product — Postou)
- Blog / CMS for client to self-edit (complicates support; clients don't update blogs)
- Mobile app (PWA is sufficient; native app adds no value for this audience)
- Multi-language sites (Portuguese only, full stop)
- SEO campaigns / Google Ads management (separate service, different skill set)

---

## Tech Stack

### Core Infrastructure

```
Frontend (marketing site + client dashboard):
  Next.js 15 App Router + Tailwind CSS + shadcn/ui
  Deploy: Vercel (São Paulo region)

Generated client sites:
  Next.js 15 static export (getStaticProps from Supabase)
  Deploy: Cloudflare Pages (free tier, unlimited sites, global CDN)
  Build: GitHub Actions → Cloudflare Pages deploy hook per client

Backend / Database:
  Supabase (Postgres + Auth + Storage + Edge Functions)
  Region: South America (São Paulo)

Preview system:
  Single Next.js app, /preview/[slug] route (SSR from Supabase)
  No per-preview deployment needed

File storage:
  Cloudflare R2 (client-uploaded photos post-approval)
  Google Places Photo API URLs for preview phase (no storage needed)

Prospecting pipeline:
  Python script (runs on Railway cron, $5/mo)
  Google Places API → filter → Supabase → queue
```

### Service Layer (Buy, Don't Build)

```
WhatsApp:
  Primary: 360dialog ($49/mo + Meta pass-through)
    — Official BSP, required for Business API at scale
  Fallback: Twilio WhatsApp ($0.005/conversation + Meta)
  Message templates: pre-approved by Meta before launch

Payments:
  Primary: Asaas (PIX + boleto + recurring subscription)
    — Webhooks: PAYMENT_RECEIVED, PAYMENT_OVERDUE
  Backup: Efí (formerly Gerencianet) — same rails, second account
  Platform billing: Asaas Cobrança Recorrente (landlord's monthly R$97)

Domain registration:
  .com: Cloudflare Registrar API (~R$50/year, instant programmatic)
  .com.br: Locaweb Partner API (5-10 day manual process in MVP)

DNS:
  Cloudflare API (zone creation, A/CNAME records, instant propagation)

Email (transactional):
  Resend (3K free/mo, then $0.0005/email)
  Domain: noreply@farol.app

Analytics (client sites):
  Plausible Analytics self-hosted on Railway ($10/mo)
  LGPD compliant — no cookies, no personal data, no banner required

Site uptime monitoring:
  Better Uptime (free tier: 50 monitors)
  Alert on downtime → WhatsApp to client + internal Slack

AI content generation:
  Claude API claude-opus-4-7 (site copy, unique headlines, about section)
  Claude API claude-haiku-4-5 (WhatsApp update processing — cheaper)
  Prompt caching enabled on all Claude API calls (60% cost reduction)

Google APIs:
  Places API (Nearby Search + Place Details + Photos)
  PageSpeed Insights API (site quality scoring)
  My Business API (GMB management — Year 2 add-on)
```

### Automation Layer

```
Workflow engine:
  Trigger.dev (durable tasks — prospecting cron, follow-up sequences,
  monthly report generation, subscription billing retry)

Prospecting pipeline (Python, Railway cron):
  Runs weekly per category × city
  Google Places API → quality score → deduplicate → queue for generation

Site generation pipeline (Node.js, Trigger.dev):
  Dequeue prospect → fetch Places Details → select template →
  Claude API generates copy → build site → deploy preview →
  queue outreach message

Outreach sequence (Trigger.dev + 360dialog):
  Day 0: Initial WhatsApp with preview link
  Day 3: Follow-up if no response
  Day 7: Final message
  Day 30: Archive prospect (eligible for re-prospecting in 6 months)

Monthly client report (Trigger.dev, runs Day 1 each month):
  Fetch Plausible analytics → format report → WhatsApp to client

Internal ops (n8n self-hosted on Railway, $10/mo):
  New client onboarding sequence
  Failed payment retry notifications
  Churned client win-back campaign (D+3, D+7, D+30 after cancel)
```

### Database Schema

```sql
-- Core tables

CREATE TABLE prospects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  google_place_id TEXT UNIQUE NOT NULL,
  business_name TEXT NOT NULL,
  category TEXT NOT NULL,        -- 'odontologia', 'mecanica', 'beleza', etc.
  city TEXT NOT NULL,
  phone TEXT,
  address TEXT,
  rating NUMERIC(2,1),
  reviews_count INT,
  google_maps_url TEXT,
  website_url TEXT,              -- NULL = no site; filled = has site
  site_quality_score INT,        -- 0-100, NULL if no site
  has_whatsapp BOOLEAN,
  status TEXT DEFAULT 'queued',  -- queued | generating | preview_ready |
                                 -- outreach_sent | responded | converted |
                                 -- rejected | archived
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE generated_sites (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  prospect_id UUID REFERENCES prospects(id),
  template_id TEXT NOT NULL,     -- 'dental_v1', 'mecanica_v2', etc.
  color_variant TEXT NOT NULL,   -- deterministic from prospect hash
  preview_slug TEXT UNIQUE NOT NULL,
  preview_url TEXT NOT NULL,
  content JSONB NOT NULL,        -- Claude-generated: headline, about, services[], cta
  photos JSONB,                  -- Google Places photo references
  preview_views INT DEFAULT 0,
  preview_time_seconds INT DEFAULT 0,
  cta_clicks INT DEFAULT 0,
  published_url TEXT,            -- NULL until client pays
  cloudflare_pages_url TEXT,
  status TEXT DEFAULT 'preview', -- preview | approved | published | rejected
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE clients (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  prospect_id UUID REFERENCES prospects(id),
  site_id UUID REFERENCES generated_sites(id),
  business_name TEXT NOT NULL,
  owner_name TEXT,
  owner_phone TEXT NOT NULL,
  owner_email TEXT,
  cnpj TEXT,
  domain TEXT,                   -- registered domain
  asaas_customer_id TEXT,        -- for recurring billing
  plan TEXT DEFAULT 'standard',  -- standard (R$97/mo) | annual (R$870/yr)
  setup_paid_at TIMESTAMPTZ,
  subscription_status TEXT,      -- active | overdue | cancelled
  next_billing_date DATE,
  updates_remaining INT DEFAULT 2,  -- resets monthly
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE outreach_messages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  prospect_id UUID REFERENCES prospects(id),
  message_type TEXT NOT NULL,    -- 'initial' | 'followup_1' | 'followup_2'
  whatsapp_message_id TEXT,
  sent_at TIMESTAMPTZ,
  delivered_at TIMESTAMPTZ,
  read_at TIMESTAMPTZ,
  replied_at TIMESTAMPTZ,
  reply_text TEXT,
  reply_sentiment TEXT           -- positive | negative | question | ignore
);

CREATE TABLE update_requests (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID REFERENCES clients(id),
  request_text TEXT NOT NULL,    -- original WhatsApp message
  parsed_changes JSONB,          -- Claude-extracted change set
  status TEXT DEFAULT 'pending', -- pending | applied | rejected
  applied_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE subscriptions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  client_id UUID REFERENCES clients(id),
  amount_cents INT NOT NULL,
  due_date DATE NOT NULL,
  paid_at TIMESTAMPTZ,
  asaas_payment_id TEXT,
  method TEXT,                   -- pix | boleto
  status TEXT DEFAULT 'pending'  -- pending | paid | overdue | cancelled
);
```

---

## Business Model

### Pricing

| Tier | Price | What's included |
|------|-------|----------------|
| **Setup** | R$697 one-time | Site creation, domain registration (.com), SSL, deploy, Google Maps link |
| **Standard** | R$97/mês | Hosting, SSL auto-renewal, uptime monitoring, 2 content updates/month via WhatsApp, monthly analytics report |
| **Annual** | R$870/ano | Same as Standard; 25% discount vs monthly; domain renewal included |
| **Add-on: GMB** | R$297 único | Google Meu Negócio setup + optimization (photos, hours, Q&A, categories) |
| **Add-on: WhatsApp Business** | R$197 único | WhatsApp Business profile setup + green checkmark application |
| **Add-on: Fotos** | R$397 único | Professional photoshoot coordination (partnered photographer, GO+DF) |
| **Add-on: Loja** | R$997 + R$49/mês | Up to 30 products, PIX checkout, order by WhatsApp |

### Unit Economics

| Item | Cost per client/month |
|------|-----------------------|
| Cloudflare Pages hosting | R$0 (free tier) |
| Cloudflare R2 storage (photos) | R$1.50 |
| Plausible Analytics (shared) | R$0.80 |
| 360dialog WhatsApp (monthly report + update confirmations) | R$4.00 |
| Claude API (update processing, 2 updates/mo) | R$1.20 |
| Better Uptime monitoring | R$0.50 |
| Resend email | R$0.20 |
| Trigger.dev (report automation) | R$0.30 |
| Asaas transaction fee (R$2.50/boleto, PIX free) | R$1.25 |
| **Total COGS** | **~R$9.75/mo** |
| **Revenue (Standard)** | **R$97/mo** |
| **Gross Margin** | **~90%** |

Setup economics:
- Setup revenue: R$697
- Setup cost: domain R$50 + Claude generation R$8 + deploy R$2 + Asaas fee R$14
- Setup gross profit: R$623

CAC:
- Google Places API + Claude (prospect → preview): R$2.80/prospect
- 360dialog WhatsApp (3-message sequence): R$0.45/prospect
- Total cost per prospect: R$3.25
- Conversion rate (outreach → paying client): ~8%
- **CAC: R$3.25 / 0.08 = ~R$41**

LTV:
- Setup: R$623 profit
- Monthly: R$87.25 margin × (1/0.05 churn) = R$1,745
- **LTV: R$2,368**
- **LTV:CAC = 58x**

Break-even at 3 paying clients (covers all infrastructure at R$200/month).
Target: 500 clients active = R$48,500/month recurring + R$89,600/month setup fees (at 144 new clients/month).

### Revenue Mix Target (Year 1)

- 70% recurring subscriptions
- 20% setup fees (new clients)
- 10% add-ons (GMB, photos, WhatsApp Business)

---

## GTM Strategy

### Channel Priority

**1. WhatsApp Outreach (primary — pull, not push)**
Automated prospecting sends personalized preview to each business.
No need to explain what it is — they see their own site.
Conversion: 8% of outreach → paying client.
At 2,000 WhatsApps/week (within Meta limits): ~160 new clients/week.

**2. SEO (secondary — compound over time)**
High-intent keywords with zero competition at local level:
- "site para barbearia goiânia" (low volume, high intent, near-zero competition)
- "criar site para clínica odontológica" (~1.2K/mo)
- "quanto custa um site para salão de beleza" (~800/mo)
- "site simples para oficina mecânica" (~600/mo)
Build 20 landing pages targeting category × city. Free site audit tool
("teste se seu site está perdendo clientes") captures email + phone.

**3. Referral from existing clients**
Every happy client knows 5 other local business owners.
Referral incentive: R$100 credit on next month for each client referred.
WhatsApp script: "Gostou do site? Indica pra um amigo dono de negócio.
A gente faz o dele também — e te devolve R$100 na mensalidade."

**4. CDL / Sebrae / Associações Comerciais**
CDL-Goiânia and Sebrae-GO run workshops on digital presence for members.
Partner pitch: "Ofereça site gratuito por 30 dias para associados como
benefício da associação." Farol charges R$297 setup (discounted), client
pays R$97/month after trial. Association co-brands the product.

**5. YouTube + Instagram (brand building)**
Short-form content: "Seu negócio aparece no Google? Olha esse teste."
Show the before/after of a business with no site vs. with site.
Not primary acquisition — builds trust for outreach conversion.

### Sales Motion

No outbound sales team. No proposal. No meeting.
The WhatsApp message IS the pitch. The preview IS the demo.
Human only enters for: complex requests (e-commerce, custom design),
failed payment recovery, and client onboarding phone call (optional,
offered as premium for annual plan).

---

## Execution Constraints

- **Developer:** Claude Code (AI-assisted). All code written via Claude Code.
  Use Next.js + Supabase — strong priors in training data. Avoid exotic
  frameworks or custom build tooling.
- **Budget:** Infrastructure target < R$300/month in Year 0. Free tiers cover
  most costs until 50+ clients.
- **Timeline:** Phase 1 is manual — zero code needed. Ship a paying client
  in week 1 before writing a single line.
- **CNPJ blocker:** Asaas (for receiving client payments) and 360dialog
  (WhatsApp Business API) require CNPJ. Open in parallel — 5-15 business days.

---

## CNPJ Opening — Parallel Track (Do This Week 1)

1. **CNAE:** 6201-5/01 (Desenvolvimento de programas de computador) or
   7319-0/99 (Serviços de publicidade não especificados) — either works.
   If planning to bill design services: 7410-2/02 (Design gráfico).
2. **Regime:** Simples Nacional. MEI if solo + revenue <R$81k/year.
   ME (Microempresa) if expecting scale — higher limit, same simplicity.
3. **Open via:** Portal Redesim (gov.br) or contador online
   (Contabilizei/Agilize ~R$99/month — worth it for the first year).
4. **After CNPJ:** Open PJ bank account at Inter Empresas (free, API-friendly,
   PIX from day 1).
5. **Register on Asaas:** CNPJ + PJ bank account required. Approval: 1-3 days.
6. **Apply for 360dialog:** Meta Business verification required. Submit
   business documents. Approval: 5-10 business days. In parallel, use
   personal WhatsApp (manually) for first 20 outreach messages.
7. **Cloudflare Registrar:** No CNPJ required. Set up immediately.

---

## MVP Execution Roadmap

### Phase 1 — Manual Validation (Week 1-2): No Code

Goal: one paying client before writing a single line. Proves the concept.
Teaches the sales motion and conversion rate before automating it.

```
Day 1-3: Find 20 prospects manually
  → Open Google Maps in Goiânia
  → Search category: "barbearia goiânia", "clínica odontológica goiânia"
  → Filter: no website shown in the listing
  → Record: business name, phone (WhatsApp), address, category, 3 photos
  → Target: 20 businesses, 4 categories (barber, dental, mechanic, beauty)

Day 3-5: Build 3 mockup sites manually
  → Use Framer.com (free, generates shareable preview links)
  → One per category (barber, dental, mechanic)
  → Populate with the actual business data found above
  → Make it real: their name, their address, their Google photos, their reviews

Day 5-7: Send WhatsApp manually
  → Personal WhatsApp: "Oi [Nome]! Criei um site pra [Nome do Negócio].
    Fica à vontade pra dar uma olhada: [Framer link].
    Se gostar, posto no ar em 48h por R$697 + R$97/mês pra manter."
  → Send to 15-20 numbers
  → Track in a spreadsheet: sent / opened / replied / interested / paid

Day 7-14: Follow up, close first client
  → 3 days no response: "Oi! Você chegou a ver o site que criei pra você?"
  → Responded with interest: answer questions via WhatsApp
  → Close via PIX: send your personal PIX key, ask for R$697
  → After payment: publish the Framer site OR buy a domain + deploy
    manually on Vercel (30 minutes)

Deliverable: 1 paying client, R$697 in pocket, real conversion data
Learn: which category converted, what objections came up, how long it took
```

### Phase 2 — Automation of Site Generation (Days 15-45)

Goal: go from 1 site/day (manual) to 20 sites/day (automated).
Still sending outreach manually or semi-manually.

```
Week 3 (Days 15-21): Scaffold + Pipeline

  npx create-next-app@latest farol --typescript --tailwind --app
  shadcn/ui init

  Supabase project (South America — São Paulo):
  Tables: prospects, generated_sites, clients, outreach_messages

  Python prospecting script (runs locally, later Railway):
    import googlemaps
    client = googlemaps.Client(key=PLACES_API_KEY)

    def prospect_city(city, category, max_results=200):
        places = client.places(f"{category} em {city}")
        for place in places['results']:
            details = client.place(place['place_id'],
                fields=['name','formatted_phone_number','website',
                        'opening_hours','photos','rating','user_ratings_total',
                        'formatted_address'])
            if not details['result'].get('website'):
                # No website — save to Supabase
                upsert_prospect(details['result'])

  Run for: Goiânia × [barbearia, clínica odontológica, oficina mecânica,
  salão de beleza, academia, restaurante]
  Expected: 800-1200 prospects per run

Week 4 (Days 22-28): Templates + Content Generation

  Create 3 Next.js templates (one per top category):
  /templates/barbearia/page.tsx  — dark theme, masculine, WhatsApp CTA
  /templates/odonto/page.tsx     — clean, clinical, appointment CTA
  /templates/mecanica/page.tsx   — bold, industrial, service list

  Each template accepts props:
  {
    businessName, tagline, about, services: string[],
    phone, address, hours, rating, reviewCount,
    photos: string[],  // Google Places photo URLs
    colorVariant: 'A' | 'B' | 'C'  // deterministic from place_id hash
  }

  Claude API call for each prospect (prompt cached for cost):
  const content = await claude.messages.create({
    model: 'claude-opus-4-7',
    max_tokens: 800,
    system: `Você é um copywriter especialista em sites de negócios locais
             brasileiros. Escreva textos diretos, sem jargão, em português
             do Brasil informal. Nunca use: "soluções", "excelência",
             "compromisso com qualidade".`,
    messages: [{
      role: 'user',
      content: `Negócio: ${businessName}
                Categoria: ${category}
                Avaliação Google: ${rating} estrelas (${reviewCount} avaliações)
                Reviews reais: ${topReviews.join('\n')}
                Endereço: ${address}

                Gere:
                1. Tagline (máx 8 palavras, específica para o negócio)
                2. Texto "sobre nós" (2 frases, específico, não genérico)
                3. Lista de 4-6 serviços (baseado na categoria e reviews)
                4. CTA principal (ação específica, não "fale conosco")

                Formato JSON.`
    }]
  })

  Preview URL system:
  /preview/[slug] in Next.js — SSR from Supabase
  Slug: kebab-case of business name + city + 4 random chars
  Tracking pixel: increment preview_views on each load
  CTA click: POST /api/preview/[slug]/click → update cta_clicks

Week 5 (Days 29-35): Conversion Flow

  Post-approval WhatsApp response handling:
  Client says "gostei" or "quero" → trigger Asaas invoice via API:

  const customer = await asaas.customers.create({
    name: businessName,
    cpfCnpj: cnpj || cpf,
    mobilePhone: phone,
  })
  const charge = await asaas.charges.create({
    customer: customer.id,
    billingType: 'PIX',
    value: 697,
    dueDate: tomorrow,
    description: 'Site Farol — Setup'
  })
  // Send PIX QR code image to client via WhatsApp

  Post-payment webhook (/api/webhooks/asaas):
  PAYMENT_RECEIVED → trigger site launch pipeline

  Site launch pipeline (Trigger.dev):
  1. Fetch final site content from Supabase
  2. Create GitHub repo for client site (GitHub API)
  3. Push Next.js static build
  4. Connect to Cloudflare Pages (Cloudflare API)
  5. Register domain (Cloudflare Registrar API)
  6. Create DNS A record pointing to Cloudflare Pages
  7. Wait for SSL provisioning (Cloudflare auto SSL)
  8. Send WhatsApp to client: "🚀 Site no ar! seusite.com"
  9. Create Asaas recurring subscription: R$97/month, auto-charge

  Expected time from payment to site live: 15-30 minutes (domain + SSL async)
  Interim URL (instant): pages.farol.app/[client-slug]
```

### Phase 3 — Automated Outreach (Days 46-75)

Goal: remove human from prospecting and outreach entirely.
System runs weekly cycle: prospect → generate → deliver → follow up.

```
Week 7-8 (Days 46-60): WhatsApp Business API

  360dialog account active (CNPJ verified, Meta approved)
  Message templates submitted and approved:

  Template 1 (initial):
  "Oi {{1}}! Criei um site pro *{{2}}* pra você dar uma olhada 👇
  {{3}}
  Se gostar, posto no ar em 48h por R$697 + R$97/mês pra manter. Sem compromisso."

  Template 2 (follow-up day 3):
  "Oi {{1}}, você chegou a ver o site que fiz pro *{{2}}*?
  O link ainda tá aqui: {{3}}"

  Template 3 (final day 7):
  "Última mensagem 😊 O site do *{{1}}* fica disponível por mais 23 dias.
  Se quiser ver: {{2}}"

  Outreach automation (Trigger.dev):
  Every Sunday 08:00: run prospecting script for the week's target category
  Monday 09:00: generate sites for new prospects (max 200/day)
  Tuesday 10:00: send initial WhatsApp to prospects with preview ready
  Friday 10:00: send follow-up to day-3 non-responders
  Following Tuesday: send final message to day-7 non-responders

  Rate limiting:
  Max 80 messages/hour per number
  3 numbers in rotation (warm up each over 14 days before use)
  Monitor Meta quality score; pause if drops below 70/100

Week 9-10 (Days 61-75): Response Handling Automation

  Inbound WhatsApp webhook (360dialog → /api/whatsapp/inbound):
  Claude classifies message intent:
  'interested' → trigger Asaas invoice creation + send payment link
  'question' → Claude generates answer based on FAQ knowledge base
  'price_negotiation' → send: "O valor é R$697 + R$97/mês.
    Quer ver o site antes de decidir? [preview link]"
  'not_interested' → mark prospect as rejected, opt out
  'wants_changes' → "Claro! Me fala o que mudar que eu ajusto."
    → Claude modifies site content → redeploy preview → notify

  Deliverable: Full end-to-end automation. Prospect discovered on Sunday,
  preview delivered on Tuesday, payment received Thursday, site live Thursday.
  Zero human involvement for 90% of conversions.
```

### Phase 4 — Retention + Add-ons (Days 76-90)

```
Client dashboard (Next.js, authenticated):
  → Site analytics (Plausible embed)
  → Monthly visitor chart
  → WhatsApp button click count
  → Google position for "business name + city"
  → Update history

WhatsApp update flow:
  Client: "muda meu telefone para (62) 99999-1234"
  →  /api/whatsapp/inbound → Claude extracts change:
     { field: 'phone', value: '(62) 99999-1234' }
  → Update Supabase → trigger Cloudflare Pages redeploy
  → "✅ Telefone atualizado! Já está no site."
  → Decrement updates_remaining; if 0: "Você usou suas 2 atualizações
    do mês. Próximas: R$29 cada ou espera dia 1. O que prefere?"

Monthly report (Trigger.dev, Day 1):
  Fetch Plausible API → format message → send WhatsApp:
  "📊 Relatório do seu site — Outubro 2026

   Visitantes únicos: 847
   De onde vieram: Google 72% | WhatsApp 21% | Direto 7%
   Cliques no botão WhatsApp: 43
   Posição no Google para 'barbearia setor bueno': #4

   Dica do mês: adicionar horário de funcionamento atualizado
   pode melhorar seu ranking em 1-2 posições. Quer que a gente
   atualize? Conta aqui."

Add-on upsell (triggered by events):
  Client gets 20+ WhatsApp button clicks/month →
  "Você está recebendo bastante contato pelo site! Quer configurar
   um WhatsApp Business profissional com catálogo de serviços?
   R$197 uma vez. Responde 'sim' que explico."
```

---

## Infrastructure Setup Checklist

### Accounts to Create (ordered by dependency)

```
Week 1 (no CNPJ needed):
  □ Vercel account (São Paulo region)
  □ Supabase project (South America — São Paulo)
  □ Cloudflare account (R2 bucket + Pages + Registrar)
  □ GitHub account (for client site repos)
  □ Google Cloud Console (Places API key + billing)
  □ Anthropic account (Claude API key)
  □ Resend account (email domain verification)
  □ Plausible Analytics (self-hosted on Railway or cloud)
  □ Railway account (Python prospecting script + n8n)
  □ Trigger.dev account (workflow automation)
  □ Better Uptime account (uptime monitoring)

After CNPJ (parallel track, starts Week 1):
  □ Inter Empresas PJ bank account
  □ Asaas account (CNPJ + PJ account required)
  □ 360dialog account (Meta Business verification, 5-10 days)
  □ Locaweb partner account (for .com.br domains, if needed)
```

### Company Setup (Brazil)

```
  □ Abertura de CNPJ (CNAE: 7319-0/99 ou 6201-5/01)
  □ Conta bancária PJ — Inter Empresas (gratuita, API-friendly)
  □ Contrato social + nome fantasia "Farol Presença Digital"
  □ Advogado: revisar termos de uso (uso de dados públicos do Google,
    isenção de garantia sobre SEO, política de cancelamento)
  □ LGPD: Política de Privacidade + Termos de Serviço
  □ Registro de marca "Farol" no INPI (Classe 42 — serviços de software)
    Prazo: 18-36 meses, custo: R$355 por classe
```

---

## Competitive Positioning

| Feature | Agência tradicional | Freelancer | Wix/Squarespace | **Farol** |
|---------|---------------------|-----------|-----------------|-----------|
| Vê antes de pagar | ❌ | ❌ | ✅ (template) | ✅ (seu negócio) |
| Tempo até o ar | 30-60 dias | 15-30 dias | Imediato (DIY) | 48h |
| Preço setup | R$3.000-10.000 | R$500-2.000 | R$0 (DIY) | R$697 |
| Manutenção | R$300-800/mês | Avulso caótico | R$79/mês (inglês) | R$97/mês |
| Precisa saber mexer | ❌ | ❌ | ✅ (horas de trabalho) | ❌ |
| Atualizações | E-mail + espera | WhatsApp + espera | Você mesmo | WhatsApp instantâneo |
| Mobile-first | Depende | Depende | ✅ | ✅ por padrão |
| SEO local configurado | Raramente | Raramente | Manual | ✅ automático |
| Relatório mensal | ❌ | ❌ | ❌ | ✅ WhatsApp |
| CAC para o cliente | Zero (eles procuram) | Zero (indicação) | Zero (Google) | Zero (Farol vai até eles) |

**Wedge:** único produto no Brasil que entrega um site personalizado com os dados reais do negócio antes de pedir um centavo.

---

## Benchmark vs. Broadly (US Equivalent)

| Dimension | Broadly (US) | Farol (BR) |
|-----------|-------------|------------|
| Target | Local US SMBs | Local BR SMBs (GO + DF first) |
| Price | $299/mo (all-in) | R$97/mês + R$697 setup |
| Site generation | Template, client fills data | Automated from Google Places |
| Outreach | Inbound (client finds them) | Outbound (Farol finds client) |
| Mockup before hire | ❌ | ✅ — core differentiator |
| Reviews management | ✅ | Year 2 add-on |
| WhatsApp-native | ❌ | ✅ — primary channel |
| Chat widget | ✅ | WhatsApp button (better for BR) |
| Social media | ✅ (bundled) | Separate product (Postou) |
| CAC | ~$200 (inbound) | ~R$41 (automated outreach) |
| Gross margin | ~65% | ~90% |

Broadly weakness to exploit: passive acquisition model (waits for inbound).
Farol's automated outreach is structurally superior in a market where
the target client doesn't search for "website service" — they don't know
they need it until they see their own site ready to launch.

---

## Success Metrics

| Milestone | Timeline | Metric |
|-----------|----------|--------|
| First paying client | Week 2 | R$697 received (manual) |
| 10 paying clients | Month 1 | R$970/mês MRR |
| First automated site | Day 45 | Zero human touch end-to-end |
| 50 paying clients | Month 3 | R$4,850/mês MRR |
| Outreach fully automated | Day 75 | 200 WhatsApps/day without operator |
| 200 paying clients | Month 6 | R$19,400/mês MRR |
| 500 paying clients | Month 12 | R$48,500/mês MRR |
| Break-even | Month 2 | MRR > R$300/mês infra |
| Add-on revenue >10% | Month 6 | GMB + WhatsApp Business upsells converting |

---

## Critical Files to Create

```
/app
  /dashboard                  — Client management dashboard (landlord view)
  /preview/[slug]             — Public preview page (SSR, noindex)
  /admin                      — Internal: prospect pipeline, outreach status
  /api
    /webhooks
      /asaas                  — Payment events (RECEIVED, OVERDUE)
      /whatsapp               — Inbound messages from 360dialog
    /preview/[slug]/click     — Track CTA clicks on preview
    /sites/generate           — Trigger site generation for a prospect
    /sites/launch             — Trigger site launch post-payment

/components
  /templates
    /barbearia                — Barber shop Next.js template
    /odontologia              — Dental clinic template
    /mecanica                 — Auto mechanic template
    /beleza                   — Beauty salon template
    /academia                 — Gym / fitness template
  /preview                   — Preview wrapper (noindex, proposal header)
  /dashboard                 — Dashboard UI components

/lib
  /supabase                  — DB client + TypeScript types
  /google-places             — Places API client + caching layer
  /claude                    — Claude API client + prompt templates
  /asaas                     — Payment API client (charges, customers, webhooks)
  /cloudflare                — Pages API + Registrar API + R2 client
  /whatsapp                  — 360dialog client + message templates
  /plausible                 — Analytics API client

/scripts
  /prospect.py               — Google Places prospecting (Railway cron)
  /generate-batch.ts         — Batch site generation from prospect queue
  /seed-templates.ts         — Load template configs into Supabase

/triggers                    — Trigger.dev workflow definitions
  /weekly-prospecting.ts
  /outreach-sequence.ts
  /monthly-report.ts
  /subscription-billing.ts
  /site-launch-pipeline.ts

/supabase
  /migrations                — DB schema migrations
    /001_initial_schema.sql
  /functions                 — Edge functions (webhook processing)

/templates                   — Static template configs (JSON)
  barbearia.json
  odontologia.json
  mecanica.json
  beleza.json
  academia.json
```

---

## Verification Plan

End-to-end test before calling each Phase complete:

**Phase 1 (Manual):**
Open Google Maps → find business without site → build mockup in Framer →
send WhatsApp manually → receive reply → collect R$697 via PIX →
publish site manually → client confirms site is live.

**Phase 2 (Generation):**
Run prospecting script → check Supabase for new prospects →
trigger site generation → open preview URL → confirm business data is correct,
copy is unique (not generic), photos load, CTA works, page is noindexed →
simulate approval → confirm Asaas invoice created → confirm Cloudflare
Pages deployment triggered → confirm DNS record created → confirm site
resolves on custom domain.

**Phase 3 (Outreach):**
Trigger outreach sequence for a test prospect → confirm 360dialog sends
initial message → advance clock 3 days (Trigger.dev test mode) →
confirm follow-up sent → simulate positive reply → confirm Claude classifies
as 'interested' → confirm Asaas payment link sent → confirm payment
webhook triggers launch pipeline → site live in under 30 minutes.

**Phase 4 (Retention):**
Send "muda meu telefone para X" via WhatsApp → confirm Claude extracts
change → confirm Supabase updated → confirm Cloudflare Pages redeployed →
confirm new phone appears on live site → confirm WhatsApp confirmation sent.
Advance to Day 1 of month → confirm Plausible data fetched →
confirm report message sent via WhatsApp with correct metrics.
```

---
