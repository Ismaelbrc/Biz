# Assina — Imobiliária Digital

Aluguel 100% online: anúncio, crédito, garantia, vistoria, contrato e
gestão — sem papel, sem fiador, sem intermediário presencial.

---

## O Problema — Dois Lados da Mesma Dor

### Do lado do inquilino

```
Processo atual para alugar um apartamento em Goiânia:

Semana 1:
  → Liga para 5 imobiliárias
  → Agende 3 visitas (corretora só pode na quarta às 14h)
  → Cancela 1 por conflito de agenda

Semana 2:
  → Escolhe o apartamento
  → Lista de documentos: RG, CPF, comprovante de renda dos últimos
    3 meses, holerites, declaração de IR, e o pior:
  → Precisa de FIADOR — alguém que tenha imóvel quitado no mesmo estado
    e que aceite co-assinar o contrato de 30 meses

Semana 3:
  → Entrega a documentação em papel, em envelope, pessoalmente
  → Aguarda "análise de crédito" (3-5 dias úteis)
  → Resultado: REPROVADO porque o fiador mora no Tocantins

Semana 4:
  → Começa tudo de novo com outra opção
  → Ou aceita pagar 3 meses de caução (R$6.000) bloqueados
  → Ou paga seguro fiança (que a imobiliária indica — com comissão)

Semana 5:
  → Assina contrato de 15 páginas que ninguém lê
  → Vistoria presencial de 2h com a corretora
  → Recebe as chaves

Total: 5 semanas, 8 deslocamentos, R$600-1.200 em taxas diversas
```

### Do lado do proprietário

```
Proprietário tem 2 apartamentos no Setor Bueno para alugar.

O que ele enfrenta:
  → 2 imobiliárias com exclusividade que brigam entre si
  → 1 imóvel parado há 3 meses "em divulgação"
  → Não sabe quantas pessoas viram o anúncio, quantas visitaram
  → Recebe a conta do aluguel no dia 15 (o inquilino pagou no dia 5 — a imobiliária ficou com os 10 dias de float)
  → Imobiliária cobra 10% de administração + 1 mês de aluguel no início
  → Quando o inquilino sai: disputa sobre a vistoria
    "A parede já estava assim antes" vs "O buraco foi você que fez"
  → Não existe vistoria fotográfica — é um laudo em papel assinado a
    mão que ninguém encontra 2 anos depois

Ele gerencia tudo por WhatsApp pessoal com a corretora.
Não tem painel, não tem histórico, não tem transparência.
```

---

## O Concorrente Que Define o Mercado

**QuintoAndar** fez isso primeiro e bem. É um unicórnio avaliado em
R$20B+ que provou que o mercado existe e que o consumidor quer digital.

O que o QuintoAndar faz bem:
- Sem fiador — garantia própria da plataforma
- Contrato digital + assinatura eletrônica
- Pagamento por PIX/boleto automático
- Presença em SP, RJ, BH, Curitiba, Porto Alegre

**Onde o QuintoAndar não é o dono do mercado:**

```
1. GEOGRAFICAMENTE:
   Goiânia e DF: presente, mas não dominante. O mercado local ainda
   é de imobiliárias tradicionais com práticas de 1995.
   Cidades menores (Anápolis, Aparecida de Goiânia, Luziânia): ausente.

2. IMÓVEL COMERCIAL:
   QuintoAndar é residencial. Salas comerciais, conjuntos, galpões
   pequenos e lojas em GO + DF têm zero opção digital.

3. GESTÃO PARA PEQUENO PROPRIETÁRIO:
   O "dono de 1-5 imóveis" que autogerencia. Não quer pagar 10% de
   administração mas precisa de ferramenta para cobrar, comunicar,
   registrar vistoria, calcular reajuste.
   QuintoAndar não tem produto para esse perfil.

4. IMÓVEL RURAL / CHÁCARAS:
   Goiás tem enorme mercado de chácara, sítio e imóvel rural de lazer.
   Completamente ignorado por plataformas digitais.
```

**Estratégia:** não competir de frente com QuintoAndar em São Paulo.
Dominar GO + DF + cidades satélite. Depois expansão natural.

---

## O Produto — 6 Módulos

### Módulo 1 — Cadastro e Anúncio

**Para o proprietário em 15 minutos:**

```
App guia o cadastro:
  1. Fotos guiadas: "Tire uma foto da sala" → app valida qualidade
     (luminosidade, ângulo, resolução) antes de aceitar
  2. Dados básicos: endereço, metragem, número de quartos
  3. Vídeo de 60 segundos: "Faça um tour do apartamento em 1 minuto"
  4. Valor sugerido pelo algoritmo:
     "Imóveis similares no Setor Bueno estão indo por R$2.100-2.400.
      Sugerimos R$2.200 para sair em 15 dias."
  5. Publicado.

Diferencial de anúncio:
  → Tour virtual automático a partir do vídeo de 60s (stitching por IA)
  → Planta baixa gerada por IA a partir das fotos
  → Score de completude: "Adicionar 2 fotos aumenta em 40% o interesse"
```

**Para o inquilino:**

```
Busca inteligente:
  → Filtros padrão: bairro, metragem, valor
  → Filtros únicos:
    "Aceita cachorro?" / "Tem vaga coberta?" / "Perto de qual escola?"
    "Pode home office?" (internet incluída, mesa, silêncio)

Agendamento de visita:
  → Visita presencial: agenda disponível do proprietário/gestor, sem
    intermediário
  → Visita virtual: tour em vídeo + chamada ao vivo pelo app com
    o proprietário (para quem está em outra cidade)

Favoritos inteligentes:
  → "3 pessoas favoritaram esse imóvel ontem"
  → Notificação quando imóvel desejado baixa de preço
  → "Imóvel disponível em 15 dias — reserve com prioridade"
```

---

### Módulo 2 — Análise de Crédito Digital

**O fim do fiador:**

```
Análise automática em menos de 24h:

DADOS SOLICITADOS AO INQUILINO:
  → CPF (base para toda a análise)
  → Autorização de consulta Open Finance (acesso ao extrato bancário)
  → Comprovante de renda (foto do holerite ou extrato)

O QUE A PLATAFORMA CONSULTA:
  → Serasa/SPC: histórico de inadimplência
  → SCR BACEN: operações de crédito ativas, histórico bancário
  → Open Finance: renda média dos últimos 6 meses (banco a banco)
  → CADIN: dívidas com governo federal
  → CNPJ (se autônomo/MEI): situação fiscal

SCORE PROPRIETÁRIO:
  → Modelo de risco calibrado para o mercado de GO + DF
  → Não é apenas "aprovado/reprovado" — é um score de 0-1000
  → "Score 820: aprovado para imóvel até R$2.500/mês sem garantia adicional"
  → "Score 640: aprovado com caução de 1 mês adicional"
  → "Score 420: indicar seguro fiança"

TEMPO: análise concluída em 2-4 horas (vs. 3-5 dias da imobiliária)
```

**Garantias disponíveis:**

```
1. GARANTIA ASSINA (premium):
   Plataforma assume o risco de inadimplência do inquilino.
   Proprietário recebe todo mês, independente de o inquilino pagar.
   Custo: 0,5% do valor mensal do aluguel cobrado ao proprietário.
   (QuintoAndar faz isso — é o modelo que deu certo)

2. SEGURO FIANÇA DIGITAL:
   Integração com Porto Seguro, Liberty, Tokio Marine.
   Contratado pelo app em 5 minutos. Sem fiador físico.
   Custo: 1-1,5 mês/ano (pago pelo inquilino, parcelado na parcela mensal).

3. CAUÇÃO PIX:
   Inquilino deposita via PIX. Valor fica em conta segregada.
   Devolvido automaticamente no término do contrato se não houver danos.
   Sem o dinheiro "perdido" no caixa da imobiliária.
```

---

### Módulo 3 — Vistoria Digital

**O maior gerador de conflito no mercado imobiliário — eliminado.**

```
PROBLEMA ATUAL:
  Entrada: corretora faz laudo em papel com 200 itens.
  Saída, 2 anos depois: ninguém encontra o laudo.
  Inquilino jura que a marca na parede "já estava assim".
  Proprietário retém caução inteira.
  Processo no JEC.

SOLUÇÃO:

VISTORIA DE ENTRADA:
  → App guia o inquilino cômodo por cômodo:
    "Agora fotografe a parede norte da sala de perto"
    "Fotografe o estado do piso da cozinha"
    "Filme a janela abrindo e fechando"
  → 80-120 fotos/vídeos com timestamp + geolocalização imutáveis
  → IA detecta e cataloga automaticamente:
    - Arranhões / manchas / furos na parede
    - Estado do piso (madeira, porcelanato, carpete)
    - Condição de torneiras, chuveiros, janelas, portas
    - Equipamentos (ar condicionado, fogão embutido, etc.)
  → Laudo gerado automaticamente: "7 itens com imperfeição pré-existente
    documentados." Com fotos, coordenadas e timestamp.
  → Ambas as partes assinam o laudo digitalmente.
  → Imutável — armazenado em blockchain light (hash do documento em cadeia).

VISTORIA DE SAÍDA:
  → Mesmo app, mesmos ângulos, mesma sequência de fotos
  → IA compara automaticamente entrada vs. saída:
    "Parede da sala: novo furo de 2cm detectado (não presente na entrada)"
    "Arranhão no piso da cozinha: pré-existente, sem alteração"
    "Ar condicionado: funcionando na entrada, não testado na saída — agendar teste"
  → Relatório de diferenças com sugestão de valor de reparo:
    "Repintura do quarto (12m²): R$280-420 pela tabela de mercado Goiânia"
  → Proprietário aprova ou contesta com evidências
  → Caução devolvida ou retida proporcional — automaticamente via PIX

RESULTADO:
  → Zero disputa subjetiva — o laudo fotográfico é irrefutável
  → Zero papel — tudo digital, tudo armazenado
  → Prazo de contestação: 5 dias úteis após o relatório — depois, automático
```

---

### Módulo 4 — Contrato Digital

```
GERAÇÃO AUTOMÁTICA:
  → Dados do imóvel + dados das partes + garantia escolhida
  → Contrato gerado em segundos com:
    - Índice de reajuste (IPCA ou IGP-M — escolha do proprietário)
    - Prazo (12, 24, 30 meses)
    - Cláusulas sobre animais, reformas, sublocação
    - Multa por rescisão antecipada (calculada automaticamente)
    - Responsabilidades de manutenção (baseadas no Código Civil)

LINGUAGEM SIMPLES:
  → Versão "humana" do contrato: cada cláusula tem um resumo
    em linguagem simples ao lado do texto jurídico
  → "O que significa isso? A multa por sair antes do prazo é de
    3 aluguéis, reduzindo proporcionalmente a cada mês cumprido."

ASSINATURA DIGITAL:
  → ZapSign ou DocuSign — válido juridicamente (Lei 14.063/2020)
  → Assinatura por SMS/WhatsApp — sem precisar de certificado ICP-Brasil
  → Registro automático no e-Notariado para contratos acima de R$3.000/mês
    (opcional — recomendado para imóveis de alto valor)

ARMAZENAMENTO:
  → Contrato armazenado para sempre na plataforma
  → Acessível 24/7 pelo app — "qual é o vencimento do meu contrato?"
  → Alertas automáticos: 90 dias antes do vencimento
    "Seu contrato vence em 90 dias. Renovar? Encerrar? Negociar?"
```

---

### Módulo 5 — Gestão do Aluguel (para o proprietário)

**O produto que as imobiliárias deveriam ter e não têm:**

```
COBRANÇA AUTOMÁTICA:
  → Boleto ou PIX gerado automaticamente todo mês
  → Vencimento configurável (dia 5, 10 ou 15 — escolha do inquilino)
  → Reajuste anual aplicado automaticamente com notificação 30 dias antes:
    "Em 30 dias o aluguel passa de R$2.200 para R$2.312 (IPCA +5,1%)"
  → Recebimento direto na conta do proprietário — sem float da imobiliária

PAINEL DO PROPRIETÁRIO:
  ┌─────────────────────────────────────────────────┐
  │ SEUS IMÓVEIS — JULHO 2026                       │
  ├─────────────────────────────────────────────────┤
  │ Ap. 502, R. 84, Setor Bueno                     │
  │   Inquilino: Carlos Mendes                       │
  │   Aluguel: R$2.200 — PAGO ✅ (02/07)            │
  │   Contrato: vence em 14 meses                   │
  │   Último contato: 12 dias atrás                  │
  │                                                  │
  │ Ap. 301, R. Goiás, Jardim Goiás                 │
  │   Inquilino: Ana Rodrigues                       │
  │   Aluguel: R$1.800 — VENCIDO ⚠️ (5 dias)       │
  │   Notificação enviada automaticamente            │
  │   Próximo passo: [Enviar cobrança] [Negociar]   │
  └─────────────────────────────────────────────────┘

COMUNICAÇÃO CENTRALIZADA:
  → Chat dentro do app — sem WhatsApp pessoal
  → Histórico completo de todas as mensagens
  → Solicitações de manutenção com foto + triagem automática:
    "Torneira pingando — responsabilidade do locatário (uso indevido)
     ou do locador (desgaste natural)?" → IA sugere com base no CC

MANUTENÇÃO INTELIGENTE:
  → Triagem automática pelo Código Civil:
    Locatário: pequenos reparos de uso diário
    Locador: estrutural, elétrico, hidráulico, telhado
  → Marketplace de prestadores de serviço parceiros (encanador, eletricista)
  → Orçamento em 24h — pagamento via app
  → Comprovante digital armazenado no histórico do imóvel
```

---

### Módulo 6 — Rescisão Digital

```
FLUXO QUANDO INQUILINO QUER SAIR:

  Inquilino clica "Encerrar contrato" no app
    ↓
  Plataforma calcula multa rescisória:
    "Você cumpriu 18 dos 30 meses. Multa proporcional: R$1.467.
     (Multa de 3 aluguéis × 40% restante do contrato)"
    ↓
  Agendamento de vistoria de saída (presencial ou guiada pelo app)
    ↓
  Comparativo automático entrada vs. saída
    ↓
  Cálculo final:
    Caução retida: R$4.400
    (-) Multa rescisória: R$1.467
    (-) Reparo parede (furo novo): R$180
    (=) Devolução ao inquilino: R$2.753 via PIX em 10 dias úteis
    ↓
  Ambas as partes confirmam → PIX automático
  Ambas deixam avaliação mútua (proprietário avalia inquilino, viceversa)

BANCO DE DADOS DE HISTÓRICO:
  → Inquilino com bom histórico tem acesso a imóveis premium
    sem caução: "Você tem 3 aluguéis anteriores com nota 4.8+.
    Aprovado sem depósito."
  → Proprietário com histórico de conflitos gerados é sinalizado
```

---

## Segmento Diferenciador — Imóvel Comercial GO + DF

**O buraco que ninguém está preenchendo:**

```
QuintoAndar: residencial apenas
Imobiliárias tradicionais: processo ainda mais burocrático para comercial
Resultado: sala comercial de R$2.500/mês em Goiânia ainda é alugada
com contrato em papel, fiador pessoa jurídica e processo de 45 dias

Mercado comercial em GO + DF:
  → 80.000+ salas e conjuntos comerciais ativos
  → Ticket médio: R$2.500-8.000/mês
  → Contrato de 24-60 meses (LTV muito maior)
  → Proprietário geralmente PJ (mais sofisticado, mais receptivo a digital)
  → Corretores comerciais = pouquíssima concorrência digital

Diferenças de produto para comercial:
  → CNPJ do locatário (análise fiscal + receita federal)
  → Contrato IPCA com opção de reajuste por área construída (INCC)
  → Vistoria com laudo para fins contábeis (ativação/baixa de ativo)
  → Nota fiscal automática do aluguel (integração com Omie/Conta Azul)
  → Cláusula de benfeitorias (quem paga o ar condicionado novo?)
```

---

## Modelo de Receita

### Para o proprietário (B2B2C)

| Serviço | Modelo | Valor |
|---------|--------|-------|
| Anúncio | Gratuito | R$0 |
| Taxa de locação (quando fecha) | One-time | 1 mês de aluguel |
| Administração mensal | Recorrente | 8%/mês do aluguel |
| Garantia Assina (prop. recebe sempre) | Add-on | 0,5%/mês do aluguel |
| Vistoria premium (laudo para obra) | One-time | R$149 |

### Para o inquilino (B2C)

| Serviço | Modelo | Valor |
|---------|--------|-------|
| Busca e candidatura | Gratuito | R$0 |
| Análise de crédito expressa (2h) | One-time | R$49 |
| Seguro fiança digital | Comissão da seguradora | 1,2 mês/ano |

### Unit economics por contrato

```
Aluguel médio GO + DF: R$2.000/mês
Contrato médio: 24 meses

Taxa de locação:        R$2.000 (mês 0)
Administração 24 meses: R$2.000 × 8% × 24 = R$3.840
Garantia Assina:        R$2.000 × 0,5% × 24 = R$240
Comissão seguro fiança: R$280 (estimativa)

LTV por contrato:       R$6.360

CAC estimado (via corretor parceiro ou digital): R$400-800
Margem bruta por contrato: ~R$5.600
```

### Projeção

```
Ano 1 (GO + DF, foco residencial):
  Contratos fechados:  50/mês → 600 no ano
  Contratos ativos:    300 em média (com churns e renovações)
  Receita de locação:  600 × R$2.000 = R$1,2M
  Receita de adm:      300 × R$2.000 × 8% = R$480k
  Total Ano 1:         ~R$1,7M

Ano 2 (expansão + comercial):
  Contratos residenciais: 150/mês
  Contratos comerciais:   20/mês (ticket 3x maior)
  Total Ano 2:            ~R$5-7M
```

---

## Vistoria com IA — O Diferencial Técnico

```python
# Pipeline de análise comparativa de vistoria

class VistoriaAnalyzer:

    def comparar_vistorias(self, fotos_entrada: list, fotos_saida: list):
        resultados = []

        for angulo in ANGULOS_PADRAO:
            foto_antes = self.encontrar_foto(fotos_entrada, angulo)
            foto_depois = self.encontrar_foto(fotos_saida, angulo)

            # Alinhamento de perspectiva (homografia)
            foto_alinhada = self.alinhar_perspectiva(foto_antes, foto_depois)

            # Detecção de diferenças via diff de features
            diferencas = self.detectar_diferencas(foto_alinhada, foto_depois)

            # Claude Vision classifica cada diferença
            for diff in diferencas:
                classificacao = claude.analyze_image(
                    imagem=diff.crop,
                    prompt="""
                    Classifique esta diferença encontrada em uma vistoria de imóvel:
                    1. Tipo: arranhão / furo / mancha / quebrado / faltando / desgaste_normal
                    2. Causa provável: uso_indevido / acidente / desgaste_natural / reforma
                    3. Responsabilidade: locatário / locador / inconclusivo
                    4. Urgência de reparo: imediato / pode_aguardar / cosmético
                    5. Custo estimado de reparo em Goiânia: R$X-Y
                    """
                )
                resultados.append({
                    "angulo": angulo,
                    "diferenca": diff,
                    "classificacao": classificacao,
                    "foto_antes": foto_antes.url,
                    "foto_depois": foto_depois.url
                })

        return self.gerar_laudo(resultados)

    def gerar_laudo(self, resultados):
        # Agrupa por responsabilidade
        responsabilidade_locatario = [r for r in resultados
                                      if r["classificacao"]["responsabilidade"] == "locatário"]
        total_reparo = sum(r["classificacao"]["custo_medio"] for r in responsabilidade_locatario)

        return {
            "data": datetime.now(),
            "hash_documento": self.gerar_hash(resultados),  # imutável
            "itens_locatario": responsabilidade_locatario,
            "itens_desgaste_normal": [...],
            "total_retencao_caution_sugerida": total_reparo,
            "laudo_pdf": self.render_pdf(resultados)
        }
```

---

## Distribuição

### Canal 1 — Corretores parceiros (não concorrentes)

A estratégia não é eliminar o corretor — é torná-lo mais produtivo.

```
Proposta para o corretor CRECI-GO:
  → Usa a plataforma Assina para seus clientes
  → Não precisa de imobiliária para trabalhar — trabalha independente
  → Recebe comissão igual (1 mês de aluguel) mas entrega mais rápido
  → Acesso a ferramentas que a imobiliária nunca deu: análise de crédito
    automática, vistoria digital, contrato gerado, cobrança automatizada
  → "Você fecha 3x mais contratos porque o processo é 3x mais rápido"

Meta: 100 corretores parceiros em Goiânia + DF no primeiro ano
Efeito: esses 100 corretores já têm carteira de proprietários
```

### Canal 2 — Proprietário direto (FSBO — For Sale By Owner)

Proprietário que anuncia no OLX, Viva Real, Zap Imóveis sem imobiliária.
Há 40.000+ anúncios de proprietário direto em GO + DF nessas plataformas.

Proposta:
- "Você anunciou sozinho. Nós cuidamos do resto: crédito, contrato, cobrança."
- Ferramenta gratuita de gestão para proprietário que já tem inquilino
  (isca para entrar no ecossistema)
- Campanhas no Zap Imóveis e Viva Real segmentando anúncios de proprietário

### Canal 3 — Construtoras e incorporadoras locais

GO tem mercado imobiliário forte: Goiânia é uma das cidades que mais
constrói por habitante no Brasil. Construtoras como Emplavi, OAS, Planeta
têm carteiras de investidores (pessoas que compram apartamento para alugar).

Proposta B2B:
- Plataforma de gestão de aluguel para a carteira de investidores da construtora
- Construtora entrega o apartamento + entrega o inquilino (via Assina)
- White label opcional para construtoras maiores

### Canal 4 — Síndicos e administradoras de condomínio

Síndico conhece todos os proprietários que estão alugando no prédio.
Administradoras de condomínio (Lello, BRZ, Apolar) têm acesso à carteira inteira.

Parceria:
- Administradora recomenda o Assina para proprietários da sua carteira
- Comissão de R$200 por contrato ativado

---

## Arquitetura Técnica

```
FRONTEND
  → App mobile: React Native (iOS + Android)
  → Web app: Next.js (para proprietários e corretores)
  → Tour virtual: integração com Matterport API ou Zillow 3D Home

BACKEND
  → Node.js (Fastify) + PostgreSQL
  → Filas: Bull (Redis) para processos assíncronos (análise de crédito, OCR)

INTEGRAÇÕES CRÍTICAS
  → Crédito: Serasa API + Open Finance (Belvo ou Pluggy)
  → Assinatura digital: ZapSign API
  → Pagamentos: Asaas (boleto + PIX recorrente + split de pagamento)
  → WhatsApp: Twilio / Z-API (notificações de vencimento, vistoria, contrato)
  → Imóvel: Zap Imóveis API + Viva Real API (distribuição automática de anúncio)
  → Seguros: Porto Seguro API + Tokio Marine (seguro fiança)

VISTORIA COM IA
  → Upload de fotos: AWS S3 + CloudFront
  → Alinhamento de imagem: OpenCV (Python microservice)
  → Análise comparativa: Claude API Vision (claude-opus-4-7)
  → Geração do laudo: LaTeX → PDF serverless (AWS Lambda)
  → Hash imutável do laudo: SHA-256 + timestamp carimbado

ARMAZENAMENTO
  → Fotos de vistoria: armazenadas por 10 anos (prazo prescricional)
  → Contratos: armazenados para sempre com hash de integridade
  → Dados sensíveis: criptografia em repouso (AES-256)

STACK AUXILIAR
  → Monitoramento: Datadog
  → Email transacional: Resend
  → Filas: BullMQ
  → Feature flags: Unleash (self-hosted)
```

---

## Roadmap

### Fase 1 — Mês 1-2: Validação manual em Goiânia
```
→ Fechar 10 contratos manualmente usando a plataforma mínima
  (formulários + WhatsApp + ZapSign + Asaas)
→ Validar: taxa de conversão de anúncio para visita, de visita para contrato
→ Testar o processo de vistoria fotográfica em 10 saídas
→ Confirmar LTV real (não projetado)
→ Recrutar 10 corretores parceiros
→ NÃO construir software — validar o negócio primeiro
```

### Fase 2 — Mês 3-4: MVP digital
```
→ Landing page + cadastro de imóvel (proprietário)
→ Análise de crédito automatizada (Serasa + Open Finance)
→ Contrato gerado + ZapSign integrado
→ Cobrança automática (Asaas)
→ Vistoria guiada pelo app (fotos com checklist — ainda sem IA de comparação)
→ Meta: 30 contratos/mês
```

### Fase 3 — Mês 5-6: Automação da vistoria
```
→ Motor de comparação de fotos entrada/saída (IA)
→ Laudo automático com sugestão de retenção de caução
→ Dashboard completo do proprietário
→ Módulo de manutenção com marketplace de prestadores
→ Meta: 60 contratos/mês
```

### Fase 4 — Mês 7-12: Expansão e comercial
```
→ Imóvel comercial (adaptações de contrato + análise CNPJ)
→ Expansão para Brasília (DF tem mercado distinto: superquadras, fungíveis)
→ Produto para construtoras (white label B2B)
→ Meta: 150 contratos/mês
```

---

## Brasília — Mercado Específico

Brasília tem particularidades que poucos entendem:

```
SUPERQUADRAS:
  Blocos da Asa Norte e Asa Sul têm conceito de "fungibilidade":
  apartamento 303 sul, bloco H, apto 201 é intercambiável com
  qualquer outro 201 da superquadra. Os contratos seguem essa lógica.

SETORES HABITACIONAIS:
  Lago Norte, Lago Sul, Park Way, Jardim Botânico, Águas Claras,
  Taguatinga, Ceilândia — cada setor tem mercado e ticket distintos.
  Produto precisa conhecer essa geografia.

IMÓVEL FUNCIONAL:
  Servidores federais têm imóvel funcional (GRPU). Esse mercado
  é completamente separado — mas quando saem do funcional, aluam
  no mercado privado. Canal interessante.

CIDADES SATÉLITE:
  Valparaíso de Goiás, Luziânia, Novo Gama, Águas Lindas —
  do lado de Goiás, mas com inquilinos que trabalham em Brasília.
  Ticket de R$800-1.400. Volume enorme. Zero plataforma digital.
  Assina pode dominar esse mercado sem concorrente.
```

---

## Riscos e Mitigações

### Risco 1 — QuintoAndar entra pesado em Goiânia

**Probabilidade:** média. QuintoAndar já está em Goiânia mas não é dominante.
**Resposta:** velocidade. Dominar os corretores locais antes que o QA chegue
com orçamento de marketing. Corretor com carteira ≠ facilmente substituível.
**Diferenciador sustentável:** imóvel comercial e cidades satélite — QA nunca vai lá.

### Risco 2 — Adoção digital em mercado conservador

**Risco:** proprietários goianienses são acostumados com imobiliária presencial.
**Mitigação:** o corretor parceiro faz a ponte. Proprietário não precisa aprender
o app — o corretor usa por ele. O proprietário só acessa o painel depois de
já ter o contrato ativo.

### Risco 3 — Inadimplência e risco de crédito (se oferecer garantia)

**Risco:** se a plataforma assumir o risco de inadimplência, um spike de
inadimplência queima o caixa.
**Mitigação:** fase 1 SEM garantia própria — apenas seguro fiança de seguradora.
Garantia Assina (risco próprio) só depois de ter 12+ meses de dados de crédito
do mercado local para calibrar o modelo.

### Risco 4 — Regulação de corretagem

**Risco:** CRECI-GO pode questionar a plataforma por exercer atividade
de corretagem sem credenciamento.
**Mitigação:** modelo de marketplace + corretores parceiros credenciados.
A plataforma é tecnologia. Os corretores são credenciados CRECI.
Modelo idêntico ao QuintoAndar (que tem parceria com CRECI).

### Risco 5 — Contestação de laudo de vistoria

**Risco:** proprietário ou inquilino contesta o laudo de IA na justiça.
**Mitigação:** laudo sempre apresentado como "assistência" — ambas as partes
assinam concordando. Há prazo de contestação de 5 dias antes de ser finalizado.
Para disputas maiores: perito convencional como árbitro (plataforma tem lista).

---

## Nome e Posicionamento

### Nome: Assina

**Duplo significado perfeito:**
- Assinar um contrato: o ato central do produto
- Assinar um plano (subscription): o modelo de negócio

**Sonoridade:** As-si-na. 3 sílabas. Verbo de ação.
Em português: "vai lá e assina" — energia de facilidade, de conclusão.

**Domínio:** assina.com.br / assina.app — verificar disponibilidade.

**Alternativas:**

| Nome | Análise |
|------|---------|
| **Assina** ✅ | Duplo sentido forte, verbo de ação, limpo |
| Morada | Quente, residencial — mas sem energia de ação |
| Chave | Símbolo universal — mas genérico demais |
| Porta | Metáfora bonita — pouco distintivo |
| Imóvel.ia | Descritivo — não é marca |
| Loca | Verbo (locar) — mas "loca" tem conotação negativa em PT-BR |

### Tagline

> *"Anunciou, alugou. Do contrato à chave, tudo no app."*

Ou mais curta:
> *"Aluguel sem burocracia."*

(Simples. Direto. O produto inteiro em 3 palavras.)

### Posicionamento

```
Para o proprietário:
  "Chega de correr atrás de imobiliária, discutir vistoria e
   esperar o repasse. Você publica, aprova e recebe — no app."

Para o inquilino:
  "Sem fiador. Sem papel. Sem semanas esperando análise.
   Aprovou, assinou, entrou."

Para o corretor:
  "Sua carteira, suas ferramentas. Só que tudo digital.
   Você fecha 3 contratos no tempo em que fechava 1."
```

### Identidade visual (direcionamento)

```
Paleta:
  → Verde-escuro (#1B4332) + branco + detalhes dourados
  → Verde: crescimento, confiança, dinheiro
  → Dourado: premium, residência de valor
  → Não é a paleta de fintech (azul neon) — é imobiliário com tecnologia

Tipografia:
  → Título: sans-serif geométrica (Neue Montreal, Space Grotesk)
  → Texto: Inter — limpeza e legibilidade
  → Não usa serifa (não quer parecer cartório velho)

Símbolo:
  → Ideia: casa estilizada com caneta de assinar dentro, formando um ícone único
  → Ou: chave simplificada que é ao mesmo tempo uma assinatura cursiva
```

---

## Conexão com o Portfólio

```
Proprietário aluga pelo Assina
  ↓
Legado: "Seu imóvel está no inventário?
  Garanta que vai para quem você quer."
  ↓
Revis: "Você tem financiamento desse imóvel?
  Verifique se os juros estão corretos."
  ↓
Campo Certo: "Imóvel rural? Tem ITR em dia? CAR regularizado?"

Inquilino usa Assina
  ↓
Aravo: "Tem dívida que está impedindo a aprovação de crédito?
  Limpe o nome primeiro."
  ↓
Amparo: "Garante que seu INSS está em dia —
  seu comprovante de renda vai ficar mais forte."
  ↓
Revis: "Tem financiamento do carro? Confere se não te cobraram a mais."

O Assina é o produto com a maior sobreposição de público
com todos os outros do portfólio: proprietário e inquilino são
90% da população economicamente ativa brasileira.
```

---

## Resumo Executivo

**O produto:** imobiliária 100% digital para GO + DF. Anúncio, análise
de crédito, garantia sem fiador, vistoria fotográfica com IA, contrato
digital e gestão de aluguel — tudo pelo app.

**O cliente principal:** proprietário com 1-5 imóveis que está cansado
de pagar 10% para uma imobiliária e não ter controle. E o inquilino
que não tem fiador e não quer perder semanas no processo.

**Diferencial vs. QuintoAndar:** foco em GO + DF (mercado local não dominado),
imóvel comercial (ignorado por todas as plataformas digitais), cidades satélite
do DF (ticket baixo, volume enorme, zero concorrência digital), e corretor
parceiro como canal de distribuição (não tenta eliminar — usa).

**Modelo:** 1 mês de aluguel na locação + 8%/mês de administração.
LTV médio por contrato: R$6.360.

**Por que agora:** ZapSign tornou a assinatura digital acessível para PMEs.
Open Finance deu acesso a renda real sem burocracia. PIX tornou a cobrança
automática trivial. Claude API Vision tornou a vistoria inteligente viável.
A soma dessas quatro tecnologias é o produto — nenhuma delas existia antes de 2020.

**Nome:** Assina
**Tagline:** "Aluguel sem burocracia."
