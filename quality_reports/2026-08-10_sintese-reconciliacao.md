# Síntese-reconciliação das três revisões + discussão com o autor

**Data:** 2026-08-10
**Alvo:** `2026-08-07_apresentacao_metodologia_ia.Rmd`
**Função:** consolidar o estado *após* a discussão com o autor, que resolveu duas das críticas das revisões. Os relatórios datados (`devils-advocate`, `edmans-contribution`, `theory-framing`) permanecem como snapshots; este arquivo registra o que mudou depois deles.

---

## 1. Crítica da metáfora "dívida" — RETRATADA

**O que as revisões diziam:** dívida técnica é canonicamente um trade-off *consciente*, logo "dívida epistêmica" desencaixaria de um fenômeno silencioso.

**Por que caiu:** o próprio Sculley et al. (2015) falsifica a premissa, no parágrafo introdutório citado pelo autor:
> "there are often sound strategic reasons to take on technical debt... **Hidden debt is dangerous because it compounds silently.**"

"Often", não "always". E o débito *oculto/silencioso* é tratado como a categoria perigosa — ou seja, origem não-consciente é **nativa** ao conceito de dívida técnica (entanglement, undeclared consumers, data dependencies acumulam por acreção, não por decisão deliberada). A propriedade definidora não é "você a contraiu de olhos abertos"; é "precisa ser servida e se compõe quer você olhe ou não".

**Consequência:** a metáfora está *bem escolhida*. A frase de qualificação que a theory-framing havia sugerido ("ao contrário da dívida técnica, um empréstimo deliberado...") constrói um **contraste falso** e foi **descartada**. Substituição correta — cita Sculley a favor e realoca a novidade:

> *"Como toda dívida — Sculley e coautores já avisavam que 'hidden debt is dangerous because it compounds silently' —, a dívida epistêmica se compõe no escuro. O que a torna epistêmica é onde ela mora: não no código, mas na sua capacidade de reconstruir e defender a decisão."*

**Realocação do passivo (a originalidade real):**
- Dívida técnica (mesmo oculta): custo no **artefato**; serviço = refatorar; credor = manutenibilidade. Impessoal.
- Dívida epistêmica: custo na relação artefato ↔ **entendimento do autor**; serviço = reconstruir e reassumir a decisão; credor = capacidade futura de defendê-la. Pessoal e temporal.
Isto converge com a ponte "dívida epistêmica × validade de construto" (theory-framing §3a).

**Extensão do autor (incorporar como *stake* da fala):** o credor da dívida epistêmica é a **reputação científica**; o evento de *default* é o **escrutínio** (peer review, replicação, pós-publicação). O equity mapeia melhor que o bond: a cobrança chega de uma vez, sem data marcada (wipeout), como na reprecificação de uma ação a zero. A **crise de replicação na psicologia** é o caso-limite: pesquisadores sem ilícito legal, reprecificados a zero quando o campo alcançou práticas "unearned". Hoje o custo na fala está abstrato ("defensibilidade"); trocar por "a garantia é a sua carreira" é mais visceral para a plateia de pós.

---

## 2. Descasamento mecanismo ↔ caso (crítica nº 1 do devils-advocate) — RESOLVIDA, com reescrita do slide

**O que o autor esclareceu sobre o caso real (ponto ideal / âncoras):**
1. **Fevereiro:** a IA escreveu o código de estimação; o autor **interrogou cada escolha enquanto era feita** e entendeu na hora. Delegação bem feita. → O mecanismo (B) "a IA escolheu minhas âncoras em silêncio" **NÃO é o caso** e não deve ser alegado.
2. **Depois:** a IA produziu **o PPT e a interpretação** dos resultados. A interpretação **afirmava mais do que os dados permitiam** (overclaim). O autor desconfiou, checou, e pegou.

**Mecanismo verdadeiro = (C):** a IA como **narradora/intérprete que superafirma**, não como analista silenciosa. O perigo materializou-se na **camada de exposição/interpretação**, e a fluência do texto tornou fácil quase aceitar.

**Reescrita exigida:**
- Slide "Onde a abstração começa a cobrar juros": das três colunas (`o que medir | quem conta | o que concluir`), **só a terceira** ("o que concluir / interpretação") corresponde ao caso do autor. Repesar o slide para a **camada de interpretação/inferência**. As colunas "o que medir / quem conta" descrevem um mecanismo que não ocorreu neste caso.
- Slides do caso (7, 8): reenquadrar de "a IA decidiu minha análise" para "a IA **narrou** minha análise e disse mais do que ela sustenta; eu quase assinei embaixo".
- Isto amarra o caso a **validade/inferência** (overclaim = afirmar além do que o desenho autoriza), reforçando a ponte com validade de construto.

**O loop completo e verdadeiro (usar como espinha da fala):**
> IA gera a dívida na interpretação → a desconfiança do pesquisador a expõe → ele checa → corrige → apresenta como provisório.

A "defesa sem cola" aparece funcionando *antes* de ter sido formalizada.

**Dogfooding — LIBERADO pelo autor.** Beat sugerido:
> *"Estes slides tiveram uma versão em que a IA interpretou meus próprios resultados e disse mais do que eu podia provar. Eu só peguei porque desconfiei e voltei a checar. É disso que eu vim falar."*

---

## 3. Correções que permanecem das revisões (não afetadas pela discussão)

- **P1 obrigatório (theory-framing §2):** remover "Formulação autoral" do slide 6. O termo "epistemic debt" já existe (Ionescu et al. 2019, manufatura; Sculley et al. 2015, "hidden technical debt" em ML; literatura de SE/GenAI de 2026). Reivindicar a **aplicação à cadeia inferencial da pesquisa empírica em ciências sociais + a ponte com validade de construto**, que é território desocupado.
  - ⚠️ **Verificar antes de citar:** Ionescu (2019) e Sculley (2015) são checáveis. As referências de **2026** (arXiv/vixra) vieram de WebSearch de subagente e podem ter IDs/títulos alucinados — confirmar uma a uma antes de colocar em slide. A conclusão "o termo já existe" se sustenta só com 2019 + 2015.
- **Acessibilidade do caso (devils-advocate §Escopo 1):** o vocabulário de pontos ideais é opaco para a plateia majoritariamente qualitativa. Dar 20s de contexto **ou** ancorar o overclaim num exemplo interpretativo mais universal. (Menos urgente agora que o foco migrou para a *interpretação*, que é legível sem entender estimação de ponto ideal.)
- **Economia (devils-advocate §Economia; theory-framing P4):** considerar fundir "O que muda na prática?" com o fechamento, e/ou "O ganho é real" com "cobrar juros".
- **Cite Sculley (2015)** no slide da abstração/juros — dá lastro e mostra domínio do vizinho.

---

## 3b. O movimento Sculley: *por que* a dívida epistêmica é mais difícil de detectar

Sculley et al. (2015), na intro, não só nomeiam a dívida — argumentam que a dívida técnica de ML é **mais difícil de detectar que o usual** e dão a razão estrutural:
> "This debt may be difficult to detect because it exists at the **system level rather than the code level**... Typical methods for paying down code level technical debt are **not sufficient**..."

A fala deve fazer o **mesmo movimento um nível acima**: argumentar por que a dívida epistêmica da IA é mais difícil de detectar, com mecanismo explícito. Três razões:

1. **Nível inferencial, não computacional.** O código pode estar correto e reproduzível; o passivo mora na distância entre o que o código computou e o que a prosa afirma que significa. Os remédios padrão (reproduzir, re-rodar, auditar logs) operam no nível do código e **não alcançam** esse nível. → Este é o *mecanismo* que o slide `reproduzir ≠ validar ≠ defender` hoje só *afirma*. Análogo direto de "code-level remedies not sufficient".
2. **A fluência desarma o alarme.** Dívida tradicional se anuncia por atrito (bug, build quebrado, número feio). A saída da IA é fluente e plausível justamente onde erra; o sinal de desconfiança é suprimido pela boa redação. Análogo de "subtly corrupted... difficult to detect".
3. **Confiança ganhada numa camada mascara a não-ganhada na outra.** O autor interrogou a estimação (fevereiro) e a entendeu — confiança legítima. Esse halo reduz o escrutínio da interpretação autorada pela IA depois; a fronteira "verifiquei a estimação" vs. "não verifiquei a narração" se apaga porque ambos vieram no mesmo artefato fluente. Análogo de "boundaries subtly corrupted or invalidated".

**Payoff:** fecha o arco e **justifica o protocolo** — se os remédios padrão não alcançam a dívida inferencial, é preciso um instrumento mirado nessa camada (o Q&A adversarial / defesa sem cola). O movimento Sculley explica *por que a terapia é do formato certo*.

**Caveat de overclaim (obrigatório, dado o tema da fala):** é **analogia, não identidade**. Sculley = mecanismo técnico (dados corrompem fronteiras de código). Aqui = mecanismo cognitivo/retórico (fluência, halo). Reivindicar o **paralelo estrutural** ("mais difícil de detectar por razão estrutural, não por descuido"), **não** "mesma razão".

---

## 4. O que sobrevive intacto (não mexer)

`reproduzir ≠ validar ≠ defender` (núcleo); o protocolo Q&A adversarial ("o objeto do teste é o pesquisador"); a abertura por confissão; a escada de abstração; o slide 4 (desarma leitura anti-IA); o reconhecimento explícito do caráter provisório; o limiar "delegue a implementação, não a autoria da cadeia inferencial".

**Score Edmans (contribuição):** 6.5/10 como snapshot — mas as resoluções acima (metáfora bem ancorada, caso realinhado ao mecanismo verdadeiro, claim de autoria corrigido para a ponte com validade de construto) elevam a defensibilidade da contribuição acima do que o snapshot registrou.
