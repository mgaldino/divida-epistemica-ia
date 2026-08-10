# Entrevista integral — workshop Metodologia de IA nas Ciências Humanas

**Data:** 7 de agosto de 2026

[Voltar à síntese](2026-08-07_sintese_entrevista_workshop_metodologia_ia.md)

> Transcrição integral das falas da entrevista, desde o briefing que acionou a skill Interview Me até a síntese final. Mensagens de sistema, chamadas de ferramentas e saídas técnicas foram omitidas; atualizações conversacionais de trabalho foram preservadas.

## Turno 1 — Manoel Galdino

Então, eu tenho algumas ideias que ainda estão um pouco desorganizadas, e eu preciso encaixar no tempo que eu tenho de fala, né? Então, eu vou querer que você use a skill de Interview Me. Interview Me. Então, quais são as minhas ideias? E a skill vai me ajudar a organizar e fechar melhor o escopo da prestação, e aí depois a gente fazer a apresentação. Então, quais são as minhas ideias? Então, eu tenho algumas ideias. Primeira ideia é a ideia de abstração, falar de abstração, né? Então, o que a inteligência artificial faz na pesquisa é permitir que a gente possa abstrair algumas coisas. E toda abstração, ela significa simplificar, deixar de olhar para coisas concretas para olhar para coisas mais high level. Então, têm boas abstrações e abstrações ruins. A boa abstração é aquela que abstrai das coisas, dos detalhes, e das coisas que não são tão relevantes para você se concentrar nas coisas mais importantes. E a abstração ruim, ela deixa as coisas relevantes de lado, e aquilo te atrapalha, porque você precisava pensar naquelas coisas relevantes, né? Então, eu tenho uma série de analogias para fazer sobre abstração, falando, por exemplo, de usar assembly, né, linguagem de máquina, quando a gente começa a programar em linguagem de programação de mais alto nível, a gente perde coisas, tem sempre perda, inclusive para boas práticas de programação, ao não saber disso, né? Mas a gente abstrai. Ou mesmo quando a gente sai... Espera um pouquinho, vá. Martim, vá. Só um parêntese aqui. Martim, vá. Vá. Nossa, que coisa chata, Martim, pelo amor de Deus. Vá. Então, voltando aqui, fechado o parêntese. Estava falando com o meu filho. Então, esse exemplo do linguagem de programação de máquina, né, pode até falar, sei lá, linguagem de programação de um nível não tão alto como C, C++, tem ponteiro, um monte de coisa, que normalmente você ganha várias coisas ao olhar para isso, né? Mas gasta muita energia. Então, você cria frameworks, por exemplo, né, em linguagem de programação tipo PHP, etc., né? C Sharp, blá blá blá. Então, esses frameworks, eles abstraem, permitem a gente abstrair e você programar coisas, né? Teorias, modelos, são todas abstrações. Então, a forma que eu queria convidar as primeiras pessoas a pensar é, para além da questão ética de usar IA, pensar em termos de o que é bom que a gente possa abstrair, que vai tornar nossas pesquisas melhores, nós melhores pesquisadores, e o que é ruim, né? Que a gente não deveria abstrair, tá? Esse é o ponto mais geral. E aí, na minha fala, eu vou falar sobre uso de métodos estatísticos mais de fronteira, né, não coisas básicas, com IA, tá? Então, eu quero falar sobre quais são as boas práticas. E aí eu tenho algumas ideias. Então, primeiro é explicar a diferença entre reproducibilidade e replicação, tá? E depois explicar, falar, ó, quando você fizer usar IA para fazer o código para você, análise de dados para você, você vai precisar garantir tanto a reproducibilidade quanto a replicação, tá? E explicar, lógico, por que a gente se preocupa na ciência com reproducibilidade e replicação, né? Porque não é uma tarefa individual, é uma tarefa coletiva. E é pra... Martim, para de barulho. E é para pensar, desculpa, outro parêntese aqui com meu filho. E é para pensar a IA também um pouco nessa lógica. Então, subagentes ou agentes independentes, eles formam um certo empreendimento coletivo. E você precisa pensar dessa forma. Então, você não deve confiar na resposta individual de um agente ou de um subagente, mas na resposta coletiva, que seja reproduzida por outros agentes e replicada por outros agentes, né? Então, essa é a lógica geral. E aí mostrar como as implicações dessas práticas com exemplos concretos de como isso acontece.

## Turno 2 — Codex — atualização de trabalho

Vou usar a skill **Interview Me** para transformar essas ideias em uma tese, um escopo compatível com o tempo e uma sequência de exemplos — sem começar os slides antes de fecharmos o argumento. Primeiro vou seguir o protocolo da entrevista; em seguida começamos pelas decisões que mais mudam a apresentação.

## Turno 3 — Codex

Já aparece um eixo promissor: **IA como tecnologia de abstração**, cuja qualidade depende de quais detalhes ela retira do pesquisador; na análise estatística avançada, isso exige mecanismos coletivos de verificação. Voltaremos depois à distinção importante entre reprodução por outro agente, implementação independente e replicação científica — elas não são automaticamente equivalentes.

Primeira pergunta: **qual é o tempo líquido máximo da sua fala, sem contar eventual debate?**

## Turno 4 — Manoel Galdino

15mim

## Turno 5 — Codex

Com 15 minutos, caberá **um argumento central e um exemplo forte**; não uma exposição abrangente sobre métodos de fronteira.

Se a plateia recordar apenas uma frase da sua apresentação no dia seguinte, **qual frase você gostaria que fosse?**

## Turno 6 — Manoel Galdino

nao sei ainda, tenho muitas duvidas

## Turno 7 — Codex

Então não vamos forçar a frase ainda; vamos chegar a ela pelo problema.

**Qual é o erro que mais o incomoda quando alguém usa IA para fazer uma análise estatística avançada?** Pense no caso concreto que faria você dizer: “essa pessoa abstraiu justamente aquilo que não poderia ter abstraído”.

## Turno 8 — Manoel Galdino

nao sei o que mais incomoda, mas eis os principais: 1. os agentes tomam decisoes metodologicas silenciosas (exemplo: definir que o eleitorado relevante é de 18 a 70 anos (voto obrigatorio), ou 16+, ou 18+. Cada decisao dessa muda a variavel calculada e isso pode ser silencioso e responder a perguntas diferentes. Na tentativa de abstrair a implementacao, a pessoa abstraiu uma decisão substantiva importante. 2. o agente comete um erro qualquer e, sem saber como foi feita a implementacao do método, nao percebe. Aí as conclusoes estão erradas e nao sabe. 3. a pessoa delega toda a analise e nao se apropria do conhecimento.

## Turno 9 — Codex

Os três problemas parecem compartilhar algo mais profundo: **perda de controle epistêmico pelo pesquisador**.

Mas precisamos decidir a arquitetura do argumento: **você os vê como três riscos paralelos ou como uma cadeia — o pesquisador delega sem se apropriar, decisões substantivas ficam invisíveis e, por isso, erros deixam de ser percebidos?**

## Turno 10 — Manoel Galdino

é o que falei, toda abstração tem custos, sempre se perde alguma coisa, sempre tem perda de controle epistêmico. programar em C pode gerar um bug que a pessoa que faz em assembly nao comete. E assim pro diante. Tem que falar do trade-off, nao só dos custos

## Turno 11 — Codex

Perfeito — eu havia achatado seu argumento ao enfatizar apenas o risco. A analogia com C e assembly diz algo mais interessante: **não devemos evitar a abstração; devemos escolher conscientemente seu nível e criar salvaguardas para os controles que perdemos**. A IA aumenta capacidade, mas muda onde os erros e as decisões substantivas podem se esconder.

No caso específico dos métodos estatísticos de fronteira, **qual é o principal ganho proporcionado pela IA que, para você, justifica aceitar esse custo de perda de controle?**

## Turno 12 — Manoel Galdino

nao sei traduzir em palavras direito, além do óbvio, que é o ganho de produtividade. Quero ajuda justamente nisso. Dê uma olhada nos logs das muitas sessoes de uso do codex aqui no meu computador ao longo dos ultimos meses, nos vários projetos que rodei para ver se você consegue me ajuda nisso.

## Turno 13 — Codex — atualização de trabalho

Vou fazer uma leitura transversal e somente de consulta: inventariar as sessões dos últimos meses, separar uma amostra por projeto e tipo de trabalho, e então voltar aos logs completos para identificar capacidades que a IA acrescentou além de velocidade. O produto será uma tipologia baseada em episódios reais — incluindo custos e limites — que usaremos para retomar a entrevista. Isso deve levar alguns minutos; não vou alterar projetos nem os próprios logs.

## Turno 14 — Codex — atualização de trabalho

O inventário confirma que há material suficiente para uma leitura séria: são 3.146 sessões desde março, com forte concentração entre maio e julho. Vou evitar uma falsa “análise de tudo”: primeiro vou mapear projetos e tipos de tarefa; depois examinarei em profundidade episódios contrastantes — análise causal, modelagem formal, coleta/auditoria de dados, redação e revisão — para separar ganho de produtividade de ganho propriamente epistêmico.

## Turno 15 — Codex — atualização de trabalho

Já aparece uma distinção útil. Nos registros, a IA não apenas executa tarefas mais depressa: ela permite construir **redundância deliberada** — outra implementação, outro revisor, outro enquadramento — e converter escolhas que poderiam permanecer tácitas em artefatos auditáveis. Agora estou testando essa leitura contra casos em que o sistema também falhou: substituição silenciosa de método, validação apenas aparente e conclusões que mudaram quando se congelaram amostra, denominadores ou tratamento.

## Turno 16 — Codex

Sim. Examinei um inventário de **3.146 sessões, cerca de 3 GB**, e li episódios completos de sete fluxos de pesquisa. Não é uma amostra representativa para estimar frequências; é evidência qualitativa de capacidades e falhas recorrentes.

O ganho além da produtividade pode ser formulado como **ampliação da largura de banda epistêmica do pesquisador**. Há quatro manifestações:

- **Expansão da fronteira do factível:** não apenas fazer mais rápido, mas realizar tarefas que normalmente seriam abandonadas — auditar 29,9 milhões de registros, extrair e validar milhares de textos, executar milhares de casos-limite de um modelo formal.
- **Redundância epistêmica:** manter implementações independentes, linguagens diferentes e revisores adversariais. No DETRAN, R e Python convergiram quando painel e especificação foram igualados; a divergência inicial revelou escolhas de amostra e desenho, não apenas bugs.
- **Externalização das decisões:** estimando, população relevante, denominadores, codificação, versões e critérios de parada podem ser transformados em artefatos inspecionáveis. A IA pode ajudar a tornar explícito o que antes ficaria apenas na cabeça do pesquisador.
- **Aprendizagem por confronto:** nos logs, suas objeções sobre estoque de tratados, elegibilidade e convenção de aceitação na igualdade corrigiram análises que já pareciam tecnicamente sofisticadas. O diálogo permitiu compreender e melhorar o método; a delegação integral teria escondido o problema.

Isso sugere uma frase provisória:

> **A IA não apenas acelera a pesquisa; ela amplia quantos caminhos o pesquisador consegue explorar e verificar. Mas essa ampliação só produz conhecimento melhor quando as decisões substantivas permanecem visíveis e contestáveis.**

A analogia com linguagens de programação fica ainda melhor assim: uma linguagem de alto nível abstrai instruções de máquina, mas oferece tipos, testes, depuradores e maneiras de inspecionar o que ocorreu. **O agente é uma abstração mais perigosa porque não esconde apenas implementação: quando a especificação está incompleta, ele também a completa tomando decisões metodológicas.**

Há também uma correção para retomarmos depois: outro agente trabalhando com os mesmos dados não produz necessariamente uma **replicação científica**. Pode produzir reprodução computacional, reimplementação independente ou análise de robustez; replicação, em sentido mais estrito, costuma exigir nova evidência. Essa distinção pode fortalecer sua apresentação.

Minha próxima pergunta é: **qual desses ganhos mais corresponde à experiência que você quer transmitir — tornar pesquisas antes inviáveis factíveis, criar verificação independente ou aprender por meio do confronto com o agente?**

<oai-mem-citation>
<citation_entries>
MEMORY.md:145-153|note=[DETRAN scale independent R Python analysis and identification limits]
MEMORY.md:159-160|note=[hidden panel and specification choices behind apparent disagreement]
MEMORY.md:218-221|note=[formal verification success and later protocol quarantine]
MEMORY.md:230-230|note=[passing checks did not validate a changed theoretical object]
MEMORY.md:1637-1646|note=[checkpointed corpus scaling and auditable batch workflow]
MEMORY.md:1649-1652|note=[model comparison and protected output design]
</citation_entries>
<rollout_ids>
019fd898-d672-7270-8553-a9dd76d56bdc
019fc9d1-e576-7801-8406-e2020eb1ad16
019fce7d-77e4-77e3-aed9-fb1d0d80d9e1
019ec1ee-ef9e-7983-bb03-a31a7fed01a0
019eccfb-5580-7983-8e10-e97845598efb
019f4723-4378-7c01-be6e-4df1cfa292c7
</rollout_ids>
</oai-mem-citation>

## Turno 17 — Manoel Galdino

A que eu mais quero destacar é aprender por meio do confronto com o agente. Isso é um ótimo insight.

## Turno 18 — Codex

Isso resolve uma tensão central da apresentação: **a IA pode tanto produzir alienação quanto apropriação do conhecimento**. A diferença está no modo de uso.

- Na delegação integral, o pesquisador recebe uma conclusão.
- No confronto, recebe uma proposta que precisa interrogar, contestar e reformular.
- Esse processo pode fazê-lo compreender decisões metodológicas melhor do que compreenderia apenas escrevendo código rotineiro.

A IA deixa de ser “oráculo” e passa a funcionar como **interlocutor metodológico contestável**.

Qual episódio concreto de sua experiência melhor mostra você contestando o agente e, com isso, passando a compreender melhor o problema metodológico?

## Turno 19 — Manoel Galdino

acho que o da apresentacao da ABCP sobre pontos ideais é um bom exemplo. Inclusive eu mesmo pedi pora IA fazer simulado comigo de Q&A nesse espírito e as perguntas que eu nao sabia responder eram abstrações que tinahm sido ruins e eu precisava em apropriar. Aliás seria bom talvez ter até uma skill ou hook pra isso, mas é assunto pra outra hora.

## Turno 20 — Codex

Esse exemplo é excelente porque mostra um ciclo completo:

**IA implementa → IA simula uma audiência crítica → as perguntas revelam abstrações ruins → o pesquisador volta ao método e se apropria das decisões.**

Portanto, o confronto não precisa ocorrer apenas durante a programação. Ele pode ser criado deliberadamente depois, colocando o pesquisador na posição de **defender pessoalmente cada escolha que delegou**. A ideia da skill/hook fica anotada conceitualmente para retomarmos em outro momento.

Na simulação da apresentação da ABCP, **qual pergunta que você não soube responder revelou de maneira mais clara que havia abstraído algo importante demais?**

## Turno 21 — Manoel Galdino

Foi sobre as âncoras. Eu nao lembrava quais âncoras havia escolhido (tinha mexido há vários meses no paper), mas mais importante, eu fiquei na dúvida se eu tinha identificado corretamente com as âncoras a dimensão altente de meu interesse de pesquisa. A pergunta foi essa: "As âncoras foram definidas teoricamente antes de observar os resultados ou escolhidas porque produziam uma dimensão substantivamente conveniente?"

## Turno 22 — Codex

Essa pergunta é quase perfeita para a apresentação porque revelou duas perdas distintas:

1. **Perda de memória/proveniência:** você já não conseguia reconstruir por que aquelas âncoras tinham sido escolhidas.
2. **Perda de controle sobre a validade do construto:** mesmo que o código estivesse correto e reproduzível, você não sabia se a dimensão latente estimada correspondia ao conceito teórico pretendido.

Ou seja, a falha não estava na execução estatística. Estava na ligação **teoria → decisão de mensuração → interpretação**. A simulação de Q&A transformou uma abstração invisível em uma pergunta que você precisava ser capaz de defender.

Depois que essa pergunta apareceu, **o que você fez concretamente para recuperar o controle sobre a escolha das âncoras e a interpretação da dimensão latente?**

## Turno 23 — Manoel Galdino

Eu fui investigar, por mei oda Ia, o que tinha sido feito, como tinha sido feito e explorar ancoras alternativas para ter certeza de que estava fazendo o certo. Ainda estu trabalhando nisso. Apresentei os resultados como provisórios.

## Turno 24 — Codex

Isso torna o exemplo mais forte, não mais fraco. O confronto com a IA não “certificou” automaticamente o resultado; ele revelou que a certificação ainda não existia. O ganho epistêmico foi:

**resultado aparentemente concluído → pergunta que você não consegue defender → reconstrução da proveniência → exploração de alternativas → conclusão rebaixada para provisória.**

Há aprendizado, revisão metodológica e melhor calibração da afirmação. A boa abstração não exige conhecer cada linha do código, mas exige conseguir explicar e defender as decisões que conectam teoria, mensuração e interpretação.

Se você transformasse esse episódio em **uma regra prática** para quem usa IA em métodos estatísticos avançados, qual seria essa regra antes de apresentar ou publicar um resultado?

## Turno 25 — Manoel Galdino

Ah, nao sei dizer. Nao pode ser: faça um Q&A em etapas importantes de um projeto, em que você nao pode simplesmente pedir à IA a cola das respostas que nao sabe, mas precisarar investigar como cas coisas foram feitas e o pq, de modo a se apropriar do conhecimento por trás das decisões.

## Turno 26 — Codex

Pode — e é uma regra muito boa. Eu a chamaria de **defesa metodológica sem cola**:

> Em etapas críticas, peça à IA que faça um Q&A adversarial sobre sua análise. Não solicite imediatamente as respostas que desconhece. Cada pergunta que você não consegue responder se torna uma pendência de investigação; o resultado permanece provisório até que você consiga justificar a decisão com suas próprias palavras.

Isso é diferente de pedir a outro agente que revise o código. Aqui, **o objeto do teste é o pesquisador**: a IA verifica se ele se apropriou do conhecimento que delegou.

Para fecharmos o escopo dos 15 minutos: você quer que essa **defesa sem cola** seja a recomendação central da apresentação, ou um mecanismo entre outros, ao lado de reprodução e verificação independente?

## Turno 27 — Manoel Galdino

MAs é necesário mais que "o resultado permanece provisório até que você consiga justificar a decisão com suas próprias palavras.". Você precisa entender e tomar decisões em conjunto com a IA nesses pontos críticos, ainda que delegue implementação das decisões. Você pode pedir um gráfico, uma explicacao estatística, cruzamenrtos adicionais, mas a decisão tem que ser sua, nem que seja para ser a mesma que játinha sido tomada. Quando vc decide é mais empoderador do que quando apenas entende e é capaz de explicar. Esse é o threshold que recomendo para a abstração não gerar mais custos que benefício, o que os programadores chamam de dívida, aqui seria dívida epistêmica, talvez.

## Turno 28 — Codex

Exato. **Compreender depois não basta; é preciso recuperar a autoria da decisão.** A IA pode calcular alternativas, produzir gráficos, explicar consequências e implementar a escolha, mas o pesquisador precisa deliberar e decidir — inclusive quando termina ratificando a opção inicialmente sugerida pelo agente.

A formulação pode ser:

> **Delegue a implementação, não a autoria da cadeia inferencial.**

E “dívida epistêmica” descreve bem o mecanismo: ela se acumula quando decisões metodológicas são tomadas sem que o pesquisador as perceba, avalie e assuma. Como na dívida técnica, o custo aparece depois — ao interpretar um resultado, responder a uma crítica, modificar o modelo ou descobrir que várias etapas dependiam de uma escolha que ninguém consegue defender.

Para transformar isso em um critério operacional: **quais decisões de uma análise estatística você considera substantivas demais para serem tomadas silenciosamente pela IA?**

## Turno 29 — Manoel Galdino

difícil dizer, sao muitas. mas escolha de denominadores, modelos a serem usados, qual o estimando, como operacionalizar variável...

## Turno 30 — Codex

Não precisamos enumerar todas. Podemos formular um teste geral:

> **Uma decisão exige deliberação do pesquisador quando alternativas razoáveis mudariam o objeto medido, a população analisada, o contraste estimado ou a força da conclusão.**

Isso abrange:

- denominador → sobre quem vale a proporção;
- operacionalização → o que a variável representa;
- estimando → qual pergunta está sendo respondida;
- modelo → quais comparações e pressupostos sustentam a inferência.

Detalhes de implementação podem ser abstraídos quando diferentes escolhas tecnicamente corretas preservam essas propriedades substantivas.

Esse teste captura adequadamente, para você, a fronteira entre o que pode ser delegado e o que precisa ser decidido conjuntamente com a IA?

## Turno 31 — Manoel Galdino

acho que ainda nao, mas podemos seguir assim por enquanto e depois refinamos.

## Turno 32 — Codex

Perfeito. Vamos tratá-lo como **critério provisório**, sem forçar uma definição fechada de dívida epistêmica antes de testá-la contra os exemplos.

Agora precisamos calibrar os 15 minutos: **quem você espera que seja o público predominante da apresentação?**

## Turno 33 — Manoel Galdino

pós-graduandos de ciências humanas, maioria da FFLCH.

## Turno 34 — Codex

Isso favorece uma apresentação conceitual, com um caso concreto e pouca linguagem técnica. “Estimando”, “âncoras” e “reprodução” precisarão ser traduzidos, não apenas mencionados.

Quanto contato você imagina que esse público tenha com **programação e métodos estatísticos avançados**?

## Turno 35 — Manoel Galdino

acho que métodos é baixa, programação alguma, já que estao interessados em IA. Ao nível do R.

## Turno 36 — Codex

Então a analogia pode funcionar melhor dentro do próprio R:

> Ao usar `lm()`, ninguém precisa programar álgebra matricial ou decomposição QR. Essa é uma abstração produtiva. Mas `lm()` não deveria decidir silenciosamente qual é a população, o desfecho, a especificação ou a interpretação causal.

A IA acrescenta uma camada que também pode preencher essas decisões substantivas. É aí que surge a dívida epistêmica. Isso comunica o argumento sem gastar tempo explicando assembly, C e frameworks.

Você aceitaria usar **o R e `lm()` como analogia principal de abstração**, deixando assembly apenas como menção rápida ou eliminando-o?

## Turno 37 — Manoel Galdino

acho que é mais fácil falar em programar em linguagem de máquina e com linguagem natural, que até quem nao programa entender, do que falar em LM e ágebra matricial ou decomposição QR. Mas posso dar os dois exemplos, para atingir um público mais amplo.

## Turno 38 — Codex

Concordo. Podemos usá-los em sequência, sem desenvolver duas aulas:

1. **Linguagem de máquina → linguagens de programação → linguagem natural:** apresenta a escada de abstração de forma universal.
2. **R e funções estatísticas:** mostra que pesquisadores já aceitam abstrações produtivas; a novidade da IA é que ela também pode abstrair decisões metodológicas.

Com apenas 15 minutos, porém, precisamos definir a posição de reprodução e replicação: **você quer mantê-las como um segundo pilar da fala ou tratá-las como salvaguardas subordinadas ao argumento principal sobre confronto, decisão e dívida epistêmica?**

## Turno 39 — Manoel Galdino

subordinas

## Turno 40 — Codex

Ótimo. Então o núcleo fica:

**abstração → risco de dívida epistêmica → confronto com a IA → retomada da decisão pelo pesquisador.**

Reprodução, reimplementação independente e Q&A entram como mecanismos para detectar a dívida, não como temas autônomos.

Além do caso das âncoras nos pontos ideais, **você considera indispensável apresentar outro exemplo concreto de método estatístico avançado?**

## Turno 41 — Manoel Galdino

nao

## Turno 42 — Codex

Isso fecha bem o escopo: **um conceito, um caso e uma recomendação prática**. O título menciona métodos de fronteira, mas o caso de pontos ideais já concretiza isso sem transformar a fala em catálogo de técnicas.

Ao final dos 15 minutos, você quer que o público saia principalmente **mais disposto a usar IA**, **mais cauteloso ao delegar**, ou **decidido a incorporar uma defesa metodológica sem cola em seus projetos**?

## Turno 43 — Manoel Galdino

mais disposto a usar IA e disposto a incorporar uma defesa metodológica sem cola em seus projetos

## Turno 44 — Codex

## Síntese da entrevista

**Objetivo da fala:** fazer pós-graduandos em Ciências Humanas saírem mais dispostos a usar IA e preparados para incorporar uma defesa metodológica sem cola em seus projetos.

**Tese central:** a IA é uma nova camada de abstração. Ela amplia o que o pesquisador consegue fazer, mas pode gerar **dívida epistêmica** quando toma decisões substantivas das quais o pesquisador não se apropria.

**Threshold provisório da boa abstração:** o pesquisador pode delegar a implementação, mas não a autoria da cadeia inferencial. A IA pode explicar, calcular, produzir gráficos e explorar alternativas; a decisão metodológica precisa ser deliberada e assumida pelo pesquisador.

**Caso central:** na preparação da apresentação da ABCP sobre pontos ideais, o Q&A simulado perguntou:

> “As âncoras foram definidas teoricamente antes de observar os resultados ou escolhidas porque produziam uma dimensão substantivamente conveniente?”

Você não conseguia reconstruir a escolha nem garantir que a dimensão latente correspondia ao conceito teórico. Isso levou a uma nova investigação com IA, à exploração de âncoras alternativas e à apresentação dos resultados como provisórios.

**Recomendação prática — defesa metodológica sem cola:**

1. Em marcos críticos, peça à IA um Q&A adversarial.
2. Não peça imediatamente a resposta das perguntas que não souber responder.
3. Transforme cada lacuna em uma investigação.
4. Use a IA para reconstruir a proveniência, comparar alternativas e visualizar consequências.
5. Tome pessoalmente a decisão metodológica, ainda que ratifique a escolha anterior.
6. Mantenha o resultado como provisório enquanto essa decisão não estiver resolvida.

**Papel subordinado das demais salvaguardas:** reprodução computacional, reimplementação independente e revisão por outros agentes ajudam a detectar erros e escolhas ocultas, mas não substituem a apropriação e a decisão do pesquisador.

**Escopo dos 15 minutos:** um conceito, um caso e uma prática. Sem catálogo de métodos e sem segundo estudo de caso.

Uma última decisão narrativa: você prefere abrir com **“descobri que não sabia defender uma decisão do meu próprio paper”** ou com a escada **linguagem de máquina → linguagem de programação → linguagem natural**?

