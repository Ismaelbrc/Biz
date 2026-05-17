# Pipeline de Capítulo — Winds of Wycaro

Este comando orquestra o ciclo completo: escrita → quatro agentes em paralelo → Carol aplica correções → capítulo finalizado e commitado.

**Uso**: `/capitulo [número] — [título] — [brief completo com POV, contexto, o que acontece, tom, egg a plantar]`

---

## FASE 1 — ESCRITA

Escreva o capítulo seguindo `escritor.md` na íntegra.

Antes de escrever, executar o checklist duplo:

**Checklist de egg:**
- [ ] Qual egg plantar neste capítulo? (consultar coluna "Plantar em" no tracker)
- [ ] O egg parece detalhe de mundo, não setup?
- [ ] Violando regra inviolável? (cor dos olhos, pesadelo, canção)
- [ ] Já há egg na cena planejada? (um por cena)

**Checklist de escrita:**
- [ ] POV correto?
- [ ] Prosa sensorial (slipsand, vento, calor, bourbon)?
- [ ] Raban mostrado, não descrito?
- [ ] Monólogo interno tecido na ação?
- [ ] Capítulo termina em momento emocional irresolvido?
- [ ] Competência de Lucasia intacta?
- [ ] Metalinguagem de série ausente? ("L1/L2/L3/L4" → âncora temporal concreta)
- [ ] Frequência de "não ia examinar" controlada? (máx. 2/livro, mínimo 10 caps de intervalo)
- [ ] Nenhum parágrafo pós-resolução emocional explicando o que a cena já disse?

Alvo: 2500–3500 palavras.

---

## FASE 2 — QUATRO AGENTES EM PARALELO (imediato após escrita)

Assim que o capítulo estiver escrito, acionar os quatro agentes **simultaneamente** — não esperar um terminar para iniciar o próximo.

| Agente | Skill | Foco principal |
|--------|-------|----------------|
| Mara Dunwyn | `/fa-apaixonada` | Impacto emocional, slow burn, imersão |
| Prof. Aldric Verne | `/critico-literario` | Prosa, estrutura, qualidade literária |
| Dex Carval | `/roteirista` | Lógica, continuidade, timeline, ortografia, eggs |
| Carol Sturka | `/carol-revisao` | Lie, Raban, voz, tiques de escrita, estrutura da série |

Cada agente recebe o texto completo do capítulo recém-escrito.

---

## FASE 3 — CAROL LÊ OS QUATRO RELATÓRIOS

Carol lê todos os relatórios e decide o que aplicar. Sem reescrita de cenas inteiras. Sem mudança de estrutura. Princípio: cortes e ajustes pontuais.

### Aceitar sem hesitar
- Erros ortográficos, de concordância, de pontuação
- Contradições de timeline/continuidade com evidência clara em texto anterior
- Tiques de escrita identificados (clusters de fórmula, metalinguagem de série)
- Parágrafos pós-resolução que explicam o que a cena já mostrou

### Avaliar antes de aceitar
- Sugestões de prosa que alteram a voz — verificar se a voz de Lucasia se mantém
- Cortes em cenas de tensão romântica — verificar se o ritmo de slow burn não é afetado
- Adições de personagem secundário — verificar se serve à cena ou à estrutura maior
- Qualquer mudança que envolva egg plantado ou a ser plantado

### Rejeitar por padrão
- Sugestões que suavizam a competência de Lucasia para o romance
- Mudanças que revelam informação de egg antes do payoff planejado
- Acelerações de tensão romántica fora do ritmo calculado
- Qualquer modificação no Livro 1 (protegido — nunca tocar)

---

## FASE 4 — FINALIZAÇÃO

Após aplicar todas as correções:

1. Verificar regras invioláveis: cor dos olhos, pesadelo, canção, número 25
2. Commit descritivo: `Cap. [N] — [Título]: escrito + revisão quadrupla aplicada`
3. Push para `claude/pluribus-series-research-ze4GE`

O capítulo só está finalizado após o push.

---

**Prompt do usuário**: $ARGUMENTS
