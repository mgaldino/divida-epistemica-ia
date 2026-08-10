# Parecer de Contribution (Framework Edmans)

**Alvo:** Apresentação "Quando a IA faz a análise, quem responde pelo método?" (`2026-08-07_apresentacao_metodologia_ia.Rmd`)
**Data:** 2026-08-10
**Nota de calibração:** O alvo é uma *fala conceitual de 15 min*, não um paper empírico. A rubrica Edmans foi adaptada — as dimensões "novidade", "importância", "generalizabilidade" e "trade-offs" transferem-se bem; "adequação ao escopo do journal" e "hipóteses direcionais testáveis" foram reinterpretadas para o registro de intervenção conceitual. O padrão aplicado é: *esta fala faria a plateia atualizar crenças de forma significativa, ou é senso comum reembalado?*

## Score: 6.5/10

(Leitura: contribuição **sólida como intervenção pedagógica**, mas com um núcleo conceitual cujo grau de originalidade está **superestimado pela embalagem** e subdemonstrado pelo caso. Para uma fala de workshop — cujo padrão é mais baixo que top journal — isto é bom. Como alegação de *conceito novo*, é frágil.)

## Resumo da contribuição alegada

A fala propõe três coisas: (1) um **conceito** — "dívida epistêmica", o acúmulo de decisões substantivas incorporadas ao artefato de pesquisa mas não compreendidas/assumidas pelo autor; (2) um **protocolo** — "defesa metodológica sem cola" (Q&A adversarial com IA em que o objeto do teste é o pesquisador, não o código); (3) um **slogan operacional** — "delegue a implementação, não a autoria da cadeia inferencial". A alegação implícita é que a IA, como camada de abstração em linguagem natural, gera essa dívida ao completar decisões silenciosamente.

## Avaliação por dimensão

### Novidade [Fraca-a-Adequada]

Aqui está o ponto sensível. Avaliando peça por peça:

- **O conceito "dívida epistêmica"**: o *fenômeno* que ele nomeia — não entender/não conseguir defender as próprias escolhas metodológicas — é bem conhecido sob outros rótulos: validade de construto (Adcock & Collier 2001, que a própria fala cita), *researcher degrees of freedom* / *garden of forking paths* (Gelman & Loken; Simmons et al. 2011), *cognitive offloading* (Risko & Gilbert 2016, citado). Em engenharia de ML existe o quase-homônimo "Hidden Technical Debt in Machine Learning Systems" (Sculley et al. 2015). O leitor informado **não atualiza muito** a crença de que "você deve entender suas escolhas". O que é genuinamente novo é o **recorte**: juntar sob um só nome riscos que a literatura estuda separadamente, e ligá-los especificamente à interface de linguagem natural. Isso é uma contribuição de *síntese/nomeação*, não de descoberta — e a fala é honesta sobre isso ("formulação autoral, apoiada em literaturas adjacentes"). O problema é que uma contribuição de nomeação só se sustenta se o nome **fizer trabalho conceitual** que os nomes antigos não fazem. Ver Trade-offs abaixo: a metáfora "dívida" pode não fazer.

- **O protocolo "defesa sem cola"**: mais forte em novidade do que o conceito. A inversão "peça perguntas, não respostas; o objeto do teste é o pesquisador" é uma operacionalização não-óbvia e acionável. É a peça que mais faz a plateia atualizar ("nunca pensei em usar a IA como arguidora em vez de executora").

- **O slogan "delegue a implementação, não a autoria"**: retoricamente forte, conceitualmente é uma reformulação da distinção clássica autonomia intelectual vs. dependência epistêmica (Carter 2020, citado). Novidade baixa, valor pedagógico alto.

**Veredicto de novidade:** o *protocolo* carrega a novidade; o *conceito* é síntese reetiquetada; o *slogan* é embalagem de uma ideia antiga. A fala apresenta os três com o mesmo peso de originalidade, o que superestima o conjunto.

### Importância [Adequada-a-Forte]

O problema é *first-order* e no momento certo: uso de IA em pesquisa está explodindo, e a maioria das intervenções ou é tecnofóbica ("não use") ou tecno-otimista ingênua. Esta fala ocupa um espaço do meio raro e útil: pró-uso, mas com uma condição de guarda operacionalizável. Um pós-graduando **mudaria comportamento** com base nisso (adotaria o Q&A adversarial). Isso é mais do que a maioria das falas de método consegue. A distinção `reproduzir ≠ validar ≠ defender` sozinha vale a fala — é uma correção de rumo importante contra a crença de que auditoria mecânica = validade.

### Adequação ao escopo [Adequada, com ressalva de calibração]

Para o público declarado (pós de Humanas, FFLCH/USP, baixa familiaridade metodológica): a *tese* encaixa perfeitamente, mas o *caso* (pontos ideais / âncoras) é vocabulário quantitativo que desencaixa da audiência majoritariamente qualitativa. É como escrever para *IO* mas dar o exemplo central em notação de *Econometrica*. A contribuição está no escopo certo; a *ilustração* está no escopo errado.

### Generalizabilidade [Limitada pela evidência, ampla pela lógica]

A lógica do argumento generaliza bem (qualquer campo com decisões substantivas delegáveis). Mas a *evidência* é N=1 autobiográfico, e — crítico — o único caso instancia o mecanismo *benéfico* da IA (ela revelou a lacuna), não o mecanismo *danoso* que a tese alega (IA completa em silêncio). A generalização "a IA gera dívida epistêmica" está sustentada por asserção, não por exemplo. Isto rebaixa o score: a contribuição *conceitual* mais forte (IA como geradora do risco) é justamente a menos evidenciada.

### Trade-offs [Parcial — e aqui está a fraqueza conceitual mais séria]

A metáfora "dívida" carrega um trade-off implícito que a fala não examina: *technical debt* é canonicamente um empréstimo **consciente e deliberado** ("entrego agora, refatoro depois"). O fenômeno que a fala descreve é o oposto — decisões completadas **silenciosamente, sem consciência**. Uma dívida que você não sabe que contraiu não é bem uma dívida; é um passivo oculto. A fala usa o slide "onde a abstração começa a cobrar juros" para explorar a metáfora, mas os "juros" fazem trabalho retórico, não conceitual. Ou seja: a peça que deveria justificar a *nomeação nova* (a metáfora fazer trabalho que os rótulos antigos não fazem) é justamente onde ela range. Um crítico atento vira isso contra o conceito.

### Hipóteses / mecanismo [Presente mas com elo faltando]

Há um mecanismo teórico explícito (abstração em linguagem natural → completação silenciosa de decisões substantivas → dívida). É direcional e claro. O problema não é ausência de mecanismo, é que o **caso não fecha o mecanismo**: no episódio, o humano escolheu as âncoras e esqueceu; a IA perguntou. O mecanismo anunciado (IA completa) e o mecanismo demonstrado (humano esquece, IA audita) não coincidem.

## Veredicto geral sobre contribution

Como **intervenção de workshop**, a contribuição é suficiente e acima da média: aborda um problema first-order, propõe uma prática acionável e não-óbvia (o protocolo), e entrega pelo menos uma distinção conceitual limpa e correta (`reproduzir ≠ validar ≠ defender`). **Isso justifica a fala.** Como **alegação de contribuição conceitual original** ("dívida epistêmica" como conceito novo), é frágil por dois motivos convergentes: (1) o fenômeno é reetiquetagem de construtos existentes, e a metáfora escolhida (dívida) *desencaixa* do fenômeno silencioso que descreve — então a nomeação não faz trabalho conceitual novo que justifique o rótulo; (2) o mecanismo distintivo (IA *gera* o risco) não é demonstrado pelo único caso, que na verdade mostra a IA *mitigando* o risco.

**Principal ponto fraco:** a fala vende três contribuições com peso igual, mas só uma (o protocolo) tem novidade robusta. O conceito precisa ou de uma justificativa de por que "dívida" é a metáfora certa, ou de um reposicionamento honesto como *síntese/nomeação útil* (não descoberta).

## Sugestões construtivas

1. **Rebaixe a alegação sobre o conceito e eleve a do protocolo.** Apresente "dívida epistêmica" explicitamente como *síntese que reúne riscos dispersos* (o que a fala já quase faz) e deixe o protocolo "defesa sem cola" carregar o peso da originalidade. Isso alinha a alegação à força real de cada peça.

2. **Defenda ou troque a metáfora.** Ou (a) acrescente uma frase que salve "dívida" — p.ex. distinguir *dívida técnica consciente* de *dívida epistêmica involuntária*, tornando o involuntário a novidade; ou (b) considere um rótulo que encaixe no fenômeno silencioso (passivo/opacidade epistêmica). A `theory-framing` está avaliando isso em paralelo.

3. **Feche o mecanismo com um segundo micro-exemplo.** Um caso de 20 segundos em que a IA de fato completa um default substantivo sem avisar (tratamento de NA, denominador, baseline, priori). Sem isso, a tese "IA gera dívida" fica sem instância.

4. **Cite o análogo direto para blindar a novidade.** Sculley et al. (2015), "Hidden Technical Debt in ML Systems", é o parente próximo. Citá-lo e diferenciar-se dele (lá é dívida de *sistema*; aqui é de *autoria inferencial*) fortalece a contribuição em vez de enfraquecê-la — mostra que você conhece o vizinho e sabe o que acrescenta.

5. **Troque a ilustração central para a plateia certa.** Um exemplo de escolha interpretativa (recorte de corpus, categoria de codificação) alcança o público de Humanas melhor que âncoras de pontos ideais, sem perder a força do argumento.
