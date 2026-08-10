# Devil's Advocate Report

**Alvo:** Apresentação "Quando a IA faz a análise, quem responde pelo método?" (`2026-08-07_apresentacao_metodologia_ia.Rmd`)
**Data:** 2026-08-10
**Formato:** fala conceitual de 15 min, público de pós-graduandos em Ciências Humanas (FFLCH/USP), baixa familiaridade com métodos.

---

## Vulnerabilidade principal

O caso central (âncoras em pontos ideais) não instancia o mecanismo que a fala anuncia. A fala afirma o dano *"a IA completa silenciosamente decisões substantivas"* (slide "Onde a abstração começa a cobrar juros"). Mas no episódio real **quem escolheu as âncoras foi o autor**, e a IA aparece como **a auditora que revelou a lacuna** (via Q&A adversarial). Ou seja: a evidência exibida é um caso de uso *benéfico* da IA, apresentado sob uma moldura de *risco* da IA. Um metodologista na plateia derruba o clímax com uma frase: "isso não é dívida gerada pela IA — é a IA te salvando de uma escolha sua mal documentada, e o problema das âncoras é pré-IA (identificação/rotação em pontos ideais)."

---

## Ataques por dimensão

### Lógica interna

1. **Descasamento mecanismo ↔ evidência (o ataque decisivo).**
   - A cadeia argumentativa da fala é: *abstração esconde decisões → IA, por ser abstração de linguagem natural, completa decisões substantivas em silêncio → isso gera dívida epistêmica → exemplo: as âncoras*. Mas o exemplo não fecha o silogismo: no caso, a decisão substantiva (escolha de âncoras) foi **humana e consciente na origem**; o que se perdeu foi a *proveniência na memória*, não a *autoria para a IA*. A IA não "completou" nada — ela **perguntou**. O elo "IA completa silenciosamente" fica **asserido mas não demonstrado**.
   - **Severidade**: Alta.
   - **Como o autor poderia responder**: (a) reposicionar o caso honestamente como "a IA como audiência crítica que expôs *minha própria* dívida" — mas isso enfraquece a moldura de que a IA *gera* o risco; ou (b) acrescentar um segundo micro-exemplo onde a IA de fato completa um default substantivo (tratamento de NA, denominador, priori, escolha de baseline) sem avisar. A opção (b) é a que salva o silogismo.

2. **A fala oscila entre continuidade e ruptura, e usa as duas conforme conveniente.**
   - Slide "nova camada de abstração": a IA é *o próximo degrau* de uma escada contínua (máquina → programação → linguagem natural). Isso é um argumento de **continuidade**.
   - Slides de alarme ("cobrar juros", "particularmente poderosa e perigosa" na síntese): a IA é **categoricamente diferente**. Isso é **ruptura**.
   - As duas teses não são incompatíveis, mas a fala nunca as reconcilia. Se é só mais um degrau, por que o pânico? Se é ruptura, a metáfora da escada (que sugere continuidade suave) mina o alarme.
   - **Severidade**: Média.
   - **Como o autor poderia responder**: nomear explicitamente o que muda *em tipo* — não o fato de abstrair, mas a **fluência plausível** da saída, que rebaixa o escrutínio (automação/viés de confirmação; "ilusão de entendimento" de Messeri-Crockett). Aí escada e alarme convivem: é o mesmo degrau, mas o primeiro cuja saída *parece* raciocínio.

3. **O protocolo pressupõe a virtude cuja escassez ele diagnostica.**
   - Passo 2 da "defesa sem cola": *"não peça imediatamente as respostas"*. Mas a fala inteira argumenta que as pessoas sobredelegam **porque é sem atrito**. Se o atrito zero é a causa da dívida, apelar para a força de vontade individual ("não peça") é prescrever abstinência a quem tem o vício ao alcance da mão. O protocolo depende do autocontrole que ele mesmo diz estar em falta.
   - **Severidade**: Média.
   - **Como o autor poderia responder**: enquadrar o passo 2 como **andaime externo** (cognitive forcing, Buçinca et al. — que a fala já cita), não como disciplina interna. Ex.: registrar a pergunta como *pendência versionada* antes de qualquer resposta; transformar em item de checklist do projeto. Move o mecanismo de "querer resistir" para "estrutura que força a pausa".

### Mecanismo causal

1. **Mecanismo alternativo mais simples explica o caso: esquecimento comum, sem IA.**
   - O episódio das âncoras é explicável por *researcher degrees of freedom* + memória falha + documentação ausente — um problema tão velho quanto a pesquisa quantitativa. A IA é **incidental** ao dano (só o revelou). A fala atribui à IA um papel causal (gerar dívida) que o caso não sustenta.
   - **Severidade**: Alta (é o outro lado da vulnerabilidade principal).
   - **Como o autor poderia responder**: conceder que o *fenômeno* é antigo, mas argumentar que a IA muda a **taxa de acumulação** (mais decisões delegadas por unidade de tempo, com menos atrito de reflexão) e a **detectabilidade** (a fluência mascara a lacuna). O dano não é novo em espécie; é novo em escala e em disfarce.

2. **Direção do efeito da IA é ambígua na própria fala.**
   - A IA aparece como *geradora* de dívida (abstração que esconde) e como *redutora* de dívida (Q&A que expõe). A fala celebra as duas, mas não diz **quando** ela faz uma coisa e quando faz a outra. Sem essa condição de contorno, a recomendação "use IA para se auto-auditar" flutua sobre a mesma ferramenta acusada de causar o problema.
   - **Severidade**: Média.
   - **Como o autor poderia responder**: explicitar a assimetria — a IA gera dívida no modo *gerador/completador* (você pede um produto e aceita) e a reduz no modo *adversarial/interrogador* (você pede perguntas, não respostas). A tese fica: **mude o modo de uso, não a quantidade de uso.** Isso é, na verdade, o coração da fala e merece estar explícito.

### Evidência empírica

1. **N = 1, autobiográfico, sem contrafactual.**
   - Um episódio pessoal. Não há como saber se (a) o protocolo teria pego a lacuna que a introspecção não pegou, nem (b) se sem IA o autor teria falhado igual. É ilustração, não evidência. A própria fala/README admite: *"eficácia como protocolo de formação ainda requer avaliação."*
   - **Severidade**: Baixa (para uma fala conceitual de 15 min, N=1 é aceitável — mas vira munição se alguém tratar a recomendação como *estabelecida*).
   - **Como o autor poderia responder**: manter o registro **explicitamente provisório** (a fala já faz isso) e não deixar a recomendação soar como protocolo validado. Uma frase de humildade epistêmica blinda.

2. **A única evidência de eficácia citada (Buçinca et al. 2021, cognitive forcing) apoia a *lógica geral*, não *este* protocolo.**
   - Cognitive forcing reduziu sobredelegação em decisões assistidas — mas em tarefas de decisão pontual, não em desenho metodológico de pesquisa. A transferência é plausível, não demonstrada.
   - **Severidade**: Baixa.
   - **Como o autor poderia responder**: citar como *analogia motivadora*, com o verbo certo ("a lógica é próxima de", que a fala já usa). Ok como está; só não superinterpretar em Q&A.

### Escopo e generalização

1. **O caso é o ponto menos acessível para a plateia declarada.**
   - Público de baixa familiaridade metodológica, e o clímax roda sobre *pontos ideais, dimensão latente, âncoras, identificação, construto*. A peça que deveria concretizar é a mais opaca. Risco real: o argumento geral (bom) sobrevive, mas o clímax (o caso) passa por cima de metade da sala.
   - **Severidade**: Alta (é falha de *entrega*, não de lógica — mas numa fala de 15 min, entrega é tudo).
   - **Como o autor poderia responder**: 20 segundos de "o que é estimar pontos ideais" com uma imagem única; **ou** trocar o caso por um exemplo universalmente legível (escolha de denominador; uma regra de codificação em análise qualitativa/documental — mais próximo do repertório de Humanas) e deixar as âncoras como menção de uma linha.

2. **A prescrição é calibrada para pesquisa quantitativa; a plateia é majoritariamente qualitativa/humanística.**
   - "Objeto, denominador, operacionalização, estimando, interpretação" — metade desse vocabulário é de tradição quantitativa. Para um pós de Filosofia, Letras ou História, "estimando" e "denominador" não são as decisões críticas dele. O critério de "decisão substantiva" precisa de tradução para escolhas *interpretativas* (recorte de corpus, categoria de análise, seleção de fontes, enquadramento teórico).
   - **Severidade**: Média.
   - **Como o autor poderia responder**: generalizar o critério para "qualquer escolha em que uma alternativa razoável mudaria o que você conclui" e ancorá-lo em pelo menos um exemplo não-quantitativo.

### Contra-argumentos na literatura

1. **Um cético do lado "reprodutibilidade resolve" tem resposta pronta.**
   - Alguém da tradição de *open science* dirá: "documente prompts, versões, seeds (Flanagin et al., que você cita) e a dívida some — é problema de higiene, não conceito novo." A fala se antecipa com o slide `reproduzir ≠ validar ≠ defender`, que é a defesa correta. Mas o slide precisa **martelar** que documentação registra *o que* foi feito, não *se você entende por quê* — senão o cético acha que a fala está reinventando a documentação.
   - **Severidade**: Baixa (a defesa existe; só precisa de ênfase).

2. **Ninguém da literatura de *automation bias* / HCI é mobilizado como possível discordante.**
   - A fala cita essa literatura como apoio, nunca como tensão. Um pesquisador de HCI poderia dizer que o problema não é "autoria" (conceito filosófico) mas *calibração de confiança* (conceito mensurável), e que "dívida epistêmica" é uma reembalagem humanística de algo já operacionalizado. Não é fatal, mas a fala não mostra ter ouvido essa objeção.
   - **Severidade**: Baixa.

### Economia do texto (13 slides de conteúdo)

- **Slide "O que muda na prática?" (Antes/Depois de aceitar)** repete, em forma de tabela, o que o slide "O meu limiar provisório" e o "Fechamento" já dizem. Três slides finais (limiar, o-que-muda, fechamento) fazem o mesmo trabalho retórico: "assuma a decisão". Em 15 min, isso é 2 min gastos reafirmando. **Cortar "O que muda na prática?" ou fundi-lo ao limiar.**
- **Slide "O ganho é real" (colunas A IA pode / o pesquisador precisa)** e **slide "Onde a abstração cobra juros"** têm sobreposição: ambos listam o que é delegável vs. o que é do pesquisador. Poderiam ser um só, liberando tempo para o segundo exemplo que o argumento precisa (ver Lógica #1).

---

## Ranking de vulnerabilidades

1. **Descasamento mecanismo ↔ caso** (Lógica #1 + Mecanismo #1) — *poderia derrubar o clímax*. A IA não gerou a dívida no exemplo; ela a revelou. Sem um segundo exemplo de IA-completando-em-silêncio, a tese central fica sem evidência do seu próprio mecanismo.
2. **Acessibilidade do caso para a plateia** (Escopo #1) — *enfraquece a entrega*. O clímax é ininteligível para metade da sala declarada.
3. **Continuidade vs. ruptura não reconciliadas** (Lógica #2) — *abre flanco em Q&A*. Resolve-se nomeando a fluência/ilusão de entendimento como o que muda em tipo.
4. **Protocolo depende da virtude que diagnostica como escassa** (Lógica #3) — *enfraquece a recomendação*. Resolve-se com andaime externo em vez de força de vontade.
5. **Calibração quantitativa para plateia qualitativa** (Escopo #2) — *reduz alcance*. Um exemplo interpretativo resolve.

---

## Recomendações de corte

- **Cortar ou fundir "O que muda na prática?" (Antes/Depois de aceitar).** Redundante com "limiar" + "fechamento". Economiza ~1,5 min para o segundo exemplo que o argumento exige.
- **Fundir "O ganho é real" e "Onde a abstração cobra juros"** em um slide (delegável vs. do-pesquisador + o que a IA pode completar em silêncio). Libera espaço e coloca o mecanismo do dano ao lado da lista, onde ele fica mais convincente.
- **Não cortar** o slide `reproduzir ≠ validar ≠ defender` — é o núcleo. Se algo, dar-lhe mais 20 segundos.

## O que sobrevive ao escrutínio

- **`reproduzir ≠ validar ≠ defender`** — distinção limpa, não-óbvia, correta. É a contribuição mais forte e resiste a qualquer ataque.
- **"Delegue a implementação, não a autoria da cadeia inferencial"** — bom slogan operacional; sobrevive desde que "autoria" seja definida (poder defender a escolha), o que a fala faz.
- **A abertura pela confissão** — retoricamente correta; vulnerabilidade pessoal ganha a plateia antes do conceito.
- **O reconhecimento explícito do caráter provisório** (README/escopo) — honestidade epistêmica que blinda contra o ataque de "N=1 vendido como protocolo validado".
- **A moldura "o objeto do teste é o pesquisador, não o código"** — reorientação genuína e produtiva do problema.

**Núcleo que resiste, em uma linha:** a *arquitetura conceitual* (reproduzir≠validar≠defender; delegar implementação, não autoria) é sólida e defensável; o que não resiste é a *ligação entre o caso escolhido e o mecanismo anunciado* — e essa é reparável com um segundo exemplo.
