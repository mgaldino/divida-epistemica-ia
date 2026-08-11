# Tradução integral para o português

- Fonte utilizada: https://x.com/a16z/status/2086845184785203468
- Modelo local de tradução: `context-review:mlx-community/Qwen3-8B-4bit`
- Regra editorial: tradução integral; sem resumo e sem preenchimento de lacunas.

## 00:00:00–00:05:00

[00:00:00–00:00:04] **Alejandro:** Estou investindo mais hoje em tokens do que em profissionais do conhecimento.

[00:00:04–00:00:06] **Alejandro:** Podemos construir agentes super-humanos.

[00:00:07–00:00:09] **Alejandro:** Isto significa que por todas as dimensões que importam,

[00:00:09–00:00:13] **Alejandro:** Nossos agentes superariam o melhor humano que já contratamos.

[00:00:13–00:00:16] **Host:** As empresas mais ambiciosas que ouvem isso decidirão seguir o exemplo,

[00:00:16–00:00:20] **Host:** Ou seja, vocês decidiram construir um agente por cliente.

[00:00:21–00:00:26] **Alejandro:** Todos os dias, entre 100 e 200.000 agentes são instanciados.

[00:00:26–00:00:29] **Alejandro:** especificamente para este cliente com sua própria máquina virtual.

[00:00:29–00:00:33] **Host:** Há muitas pessoas preocupadas com como as organizações do futuro vão ser.

[00:00:33–00:00:36] **Host:** e o papel que os seres humanos vão desempenhar.

[00:00:36–00:00:40] **Alejandro:** Se você nunca enfrentou o medo — se nunca o sentiu —, então ainda não tentou usar IA.

[00:00:40–00:00:44] **Alejandro:** Nós lançamos um programa dentro do Kavak chamado Academia Jedi.

[00:00:44–00:00:49] **Alejandro:** Do CEO aos engenheiros de IA e aos mecânicos, treinamos todos.

[00:00:49–00:00:53] **Alejandro:** E, após seis semanas, lançam agentes de ponta para a produção.

[00:00:53–00:00:57] **Host:** Que conselho você tem para futuros fundadores ou fundadores de primeira viagem que podem estar ouvindo?

[00:00:57–00:00:59] **Alejandro:** O que funciona agora é...

[00:00:59–00:01:04] **Host:** Bem-vindos de volta ao podcast da a16z.

[00:01:05–00:01:07] **Host:** Hoje temos Ale Maza, chefe de IA da Kavak.

[00:01:07–00:01:11] **Host:** Hoje vamos discutir a transformação que Ale liderou na Kavak

[00:01:11–00:01:13] **Host:** para torná-la uma empresa nativa de IA.

[00:01:13–00:01:15] **Host:** Obrigado, Ale, por estar conosco hoje.

[00:01:15–00:01:16] **Alejandro:** Obrigado pelo convite.

[00:01:16–00:01:20] **Host:** Antes de começar na Kavak, dirigia uma empresa chamada Opi Analytics.

[00:01:21–00:01:21] **Alejandro:** Isso mesmo.

[00:01:22–00:01:26] **Host:** E você estava muito envolvido com IA antes do ChatGPT.

[00:01:26–00:01:28] **Host:** Você quer nos contar um pouco sobre essa trajetória?

[00:01:28–00:01:29] **Alejandro:** Sim, sim, claro.

[00:01:29–00:01:31] **Alejandro:** Chamávamos de aprendizado de máquina naquela época.

[00:01:31–00:01:33] **Alejandro:** Era uma família diferente de algoritmos.

[00:01:33–00:01:41] **Alejandro:** E fundamos uma empresa com a visão muito ambiciosa de que novos modelos de aprendizado de máquina

[00:01:41–00:01:45] **Alejandro:** Seriam tão poderosas que poderiam resolver qualquer problema complexo.

[00:01:46–00:01:47] **Alejandro:** Isso foi antes dos Transformers, certo?

[00:01:47–00:01:49] **Alejandro:** Isso foi como em 2013.

[00:01:50–00:01:51] **Alejandro:** Então começamos a construir a empresa desse modo.

[00:01:51–00:01:57] **Alejandro:** E acho que estávamos 10 anos à frente do tempo, mas construímos uma grande empresa.

[00:01:57–00:02:05] **Alejandro:** Servimos como 1.400, 500 empresas em torno de algoritmos de risco, logística, previsão e marketing.

[00:02:05–00:02:18] **Alejandro:** Mas realmente o poder dos Transformers e depois o momento do ChatGPT quando ele chegou torna as coisas muito claras.

[00:02:18–00:02:29] **Alejandro:** que agora poderíamos construir uma empresa completamente nova e uma forma de construir empresas.

[00:02:29–00:02:33] **Alejandro:** E nos juntamos à Kavak e ao Carlos para construir isso.

[00:02:33–00:02:34] **Host:** Incrível.

[00:02:34–00:02:34] **Host:** Tudo certo.

[00:02:34–00:02:39] **Host:** Vamos passar a maior parte deste podcast falando exatamente sobre como você identificou o Kavak.

[00:02:39–00:02:43] **Host:** Mas talvez apenas para começar, o que o Kavak faz e qual é o seu papel lá?

[00:02:43–00:02:47] **Alejandro:** Kavak começou como um mercado de carros usados.

[00:02:47–00:02:53] **Alejandro:** Então compramos carros, os recondicionamos e depois os vendemos e financiamos.

[00:02:53–00:03:02] **Alejandro:** Mas, para fazer isso, também tivemos de construir uma fintech, uma empresa de logística, algo como a Carfax e...

[00:03:02–00:03:06] **Alejandro:** Basicamente, toda a infraestrutura para que isso funcione não existia no LATAM.

[00:03:06–00:03:10] **Alejandro:** Tivemos que construir tudo verticalmente para servir os nossos clientes da maneira certa.

[00:03:11–00:03:14] **Host:** Vou começar dando uma visão de como é a arquitetura.

[00:03:14–00:03:17] **Host:** Então um consumidor entra e diz: "Quero vender o meu carro".

[00:03:17–00:03:19] **Host:** Com quantos agentes esse consumidor interage?

[00:03:19–00:03:20] **Host:** Como é a estrutura de orquestração?

[00:03:20–00:03:22] **Host:** Diz-nos como você desenha isso.

[00:03:22–00:03:22] **Alejandro:** Sim.

[00:03:22–00:03:27] **Alejandro:** Então apostamos a empresa na transformação para uma empresa gerida por agentes.

[00:03:27–00:03:37] **Alejandro:** As perguntas que nos fazemos são: como construiríamos o Kavak em 2035 com inteligência de nível Fable 10 ou GPT-10?

[00:03:37–00:03:43] **Alejandro:** Na verdade, essa empresa parece muito diferente daquilo que construímos ou do que tínhamos naquela época.

[00:03:44–00:03:52] **Alejandro:** Então, quando um cliente entra agora mesmo, um agente será criado especificamente para esse cliente com sua própria máquina virtual.

[00:03:52–00:04:01] **Alejandro:** Vai lembrar anos de interação desses clientes com Kavak, o que eles visitaram na página web ou uma chamada que eles tiveram há dois anos.

[00:04:01–00:04:14] **Alejandro:** Então, o agente guarda tudo na memória, formula uma estratégia e define a meta de longo prazo de maximizar o valor desse cliente ao longo do relacionamento, fazendo o que for necessário para deixá-lo satisfeito.

[00:04:14–00:04:20] **Alejandro:** E convertê-los em, como, todos os nossos diferentes produtos, como, ao longo do tempo.

[00:04:21–00:04:31] **Alejandro:** E essa é uma arquitetura completamente nova e inovadora em escala, acho que, porque as pessoas ainda estão construindo sistemas multiagente com especialistas.

[00:04:31–00:04:44] **Alejandro:** E percebemos que apostar em agentes de longa duração com objetivos difíceis, não apenas fluxos de trabalho, poderia maximizar a satisfação dos nossos clientes e, obviamente, o seu valor ao longo da vida.

[00:04:44–00:04:45] **Host:** Fantástico.

[00:04:45–00:04:45] **Host:** Certo.

[00:04:45–00:04:47] **Host:** Vamos entrar nos detalhes disso.

[00:04:47–00:04:53] **Host:** Mas, em contraste com muitas empresas que dizem “queremos nos tornar agênticas” e testam alguns fluxos de trabalho...

[00:04:53–00:04:58] **Host:** Vocês adotaram uma abordagem radical — tipo, precisávamos fazer isso funcionar.

[00:04:58–00:04:59] **Host:** Você teve que reduzir drasticamente.

## 00:05:00–00:10:00

[00:05:00–00:05:02] **Host:** Não funcionou durante um ano.

[00:05:02–00:05:02] **Host:** Certo.

[00:05:03–00:05:07] **Host:** Você quer explicar isso? Obviamente, foi preciso ajustar muitas coisas para fazê-lo funcionar.

[00:05:07–00:05:12] **Host:** Descreva a estrutura de orquestração naquela época, quais modelos vocês usavam e os detalhes específicos.

[00:05:12–00:05:16] **Alejandro:** Então havia, tipo, três decisões principais que tínhamos de tomar.

[00:05:17–00:05:23] **Alejandro:** O primeiro, e é aí que eu acho que muitas empresas estão presas agora, é o primeiro instinto é, ok,

[00:05:23–00:05:24] **Alejandro:** Vamos adotar a IA.

[00:05:25–00:05:31] **Alejandro:** E você basicamente deixa sua estrutura como está e dá o ChatGPT ou o Claude para sua equipe.

[00:05:31–00:05:33] **Alejandro:** E então não há eficiência.

[00:05:33–00:05:36] **Alejandro:** Seus clientes têm os mesmos problemas e nada acontece, né?

[00:05:36–00:05:43] **Alejandro:** Então, precisa redesenhar toda a sua empresa em torno dos agentes e das capacidades futuras.

[00:05:43–00:05:52] **Alejandro:** Isso significa reconstruir a maioria das APIs e os sistemas para que os agentes consigam usar tudo isso na execução das tarefas.

[00:05:52–00:05:57] **Alejandro:** Depois, é preciso começar a gerar dados e ciclos de feedback para ajustar esses agentes.

[00:05:57–00:06:01] **Alejandro:** A única maneira de fazê-los funcionar é se você os ensina.

[00:06:01–00:06:02] **Alejandro:** Como ensiná-los?

[00:06:02–00:06:04] **Alejandro:** Você os coloca em operação.

[00:06:04–00:06:05] **Alejandro:** Você os coloca diante dos clientes.

[00:06:06–00:06:06] **Alejandro:** Você obtém esses dados.

[00:06:06–00:06:07] **Alejandro:** Você recebe essas avaliações.

[00:06:07–00:06:11] **Alejandro:** E depois você treina seus agentes.

[00:06:12–00:06:17] **Alejandro:** E essa é a segunda aposta que fizemos, que poderíamos construir agentes superhumanos.

[00:06:17–00:06:24] **Alejandro:** Isso significa que por todas as dimensões que importam, como conversão, valor ao longo da vida, experiência do cliente,

[00:06:24–00:06:29] **Alejandro:** Nossos agentes superariam o melhor humano que já contratamos.

[00:06:29–00:06:30] **Alejandro:** E nós os colocamos diante dos problemas mais difíceis.

[00:06:30–00:06:37] **Alejandro:** E, por fim, você começa a mudar como mede o sucesso da empresa.

[00:06:37–00:06:39] **Alejandro:** A Kavak era uma empresa transacional.

[00:06:40–00:06:46] **Alejandro:** Costumávamos medir quantos carros comprávamos e vendíamos e quantos freios — quantas pastilhas de freio — precisávamos comprar.

[00:06:46–00:06:59] **Alejandro:** E passamos para uma empresa relacional, onde hoje eu tenho 10 milhões de clientes em minha base de dados e eu tenho agentes atribuídos à maioria deles com a tarefa de maximizar o valor ao longo da vida.

[00:06:59–00:07:05] **Alejandro:** Agora, estamos vendendo carros e empréstimos pessoais e itens de muito alto valor.

[00:07:05–00:07:15] **Alejandro:** Só ativar 1% dessa base de clientes representa centenas de milhões de dólares, se fizermos isso da maneira certa.

[00:07:15–00:07:21] **Alejandro:** Foi uma aposta que fez sentido para nós por causa do setor, do alto valor das transações e porque, no fim das contas,

[00:07:22–00:07:27] **Alejandro:** Os clientes precisam construir confiança com a empresa porque estão comprando um carro usado.

[00:07:27–00:07:34] **Alejandro:** E a maneira de construir a confiança é conhecê-los e planejar e nutrir uma relação de longo prazo.

[00:07:35–00:07:37] **Host:** Ale, eu só queria aprofundar um ponto.

[00:07:37–00:07:39] **Host:** Sabe, evals em vez de demonstrações de agentes.

[00:07:40–00:07:40] **Host:** Sim.

[00:07:40–00:07:47] **Host:** Provavelmente você recebe muitas propostas de agentes e, sabe, nunca foi tão fácil construir coisas.

[00:07:47–00:07:51] **Host:** Mas uma das perguntas é, como vocês vão avaliar isso?

[00:07:51–00:07:56] **Host:** Porque nem todos os testam em 90% das interações com os clientes para ver se estão realmente funcionando.

[00:07:56–00:08:04] **Host:** E acredito que cerca de 98% das interações, ou algo assim, agora são conduzidas por agentes.

[00:08:04–00:08:04] **Alejandro:** Sim, totalmente.

[00:08:05–00:08:13] **Alejandro:** Para dar uma ideia da escala, 96% de todas as interações são conduzidas por agentes.

[00:08:14–00:08:16] **Alejandro:** Então, não há humanos lá.

[00:08:17–00:08:21] **Alejandro:** Como 95% de todas as transações são totalmente manipuladas pelos agentes.

[00:08:21–00:08:25] **Alejandro:** Obviamente, você encontra uma pessoa quando retira o carro: há alguém fisicamente presente para entregar as chaves.

[00:08:25–00:08:31] **Alejandro:** Mas o restante da experiência da viagem é gerenciado por um agente.

[00:08:31–00:08:38] **Alejandro:** Todos os dias, entre 100.000 e 200.000 agentes são instanciados.

[00:08:38–00:08:39] **Alejandro:** Eles acordam.

[00:08:39–00:08:44] **Alejandro:** Trabalham ora por três minutos, ora por oito horas, ora por três dias.

[00:08:44–00:08:49] **Alejandro:** Eles, assim, colocam um despertador para a próxima tarefa e voltam a dormir.

[00:08:49–00:08:52] **Alejandro:** A escala disso é apenas incrível.

[00:08:53–00:08:53] **Alejandro:** E está funcionando.

[00:08:53–00:08:57] **Alejandro:** Como é que você consegue fazer isso funcionar em escala?

[00:08:58–00:09:01] **Alejandro:** E a resposta que você mencionou são as evals.

[00:09:01–00:09:04] **Alejandro:** Gosto de me mover extremamente rápido.

[00:09:05–00:09:08] **Alejandro:** Mas para se mover rápido, tem que ter freios, né?

[00:09:08–00:09:08] **Alejandro:** Imagine um carro.

[00:09:10–00:09:13] **Alejandro:** Você só pisa no acelerador quando tem os freios certos.

[00:09:14–00:09:15] **Alejandro:** E a IA é extremamente poderosa.

[00:09:15–00:09:22] **Alejandro:** E eu vi muitas empresas cometerem esse erro porque tentam ir devagar porque não têm os freios certos.

[00:09:22–00:09:24] **Alejandro:** Então eu pensei nisso de outra forma.

[00:09:24–00:09:25] **Alejandro:** Quão rápido podemos avançar?

[00:09:26–00:09:28] **Alejandro:** Bem, depende da qualidade das nossas avaliações.

[00:09:28–00:09:43] **Alejandro:** Uma boa regra é que gastamos aproximadamente a mesma quantidade de tempo, tempo de engenharia, tokens e dinheiro na construção das avaliações que na construção dos agentes.

[00:09:43–00:09:48] **Alejandro:** É assim que você melhora cada vez mais, sem tratar as evals como algo secundário.

[00:09:48–00:09:49] **Alejandro:** Então, o que medimos?

[00:09:50–00:09:53] **Alejandro:** Em primeiro lugar, os resultados do negócio.

[00:09:53–00:09:56] **Alejandro:** Se o meu cliente estiver feliz, ele comprará um carro.

[00:09:56–00:09:59] **Alejandro:** Eles vão ter o empréstimo aprovado.

[00:09:59–00:10:01] **Alejandro:** Eles vão vender um carro para nós.

## 00:10:00–00:15:00

[00:10:01–00:10:03] **Alejandro:** E esse é o primeiro cheque.

[00:10:03–00:10:05] **Alejandro:** Como, converteu?

[00:10:05–00:10:07] **Alejandro:** E é aí que a maioria das coisas quebra.

[00:10:07–00:10:20] **Alejandro:** Vejo empresas medindo o número de chamadas ou minutos durante a chamada ou alguns KPIs superficiais que lhe dão alguma informação, mas que não funcionam mesmo.

[00:10:20–00:10:30] **Alejandro:** O importante é saber se esse cliente converteu, se isso gera valor para ele e se ele fica satisfeito em voltar a interagir conosco depois de algum tempo.

[00:10:30–00:10:41] **Alejandro:** E, uma vez conectadas essas avaliações, é apenas otimizar a arquitetura agente certa e dar aos agentes habilidades para escalar isso e atender a milhões de clientes.

[00:10:43–00:10:43] **Host:** É realmente, realmente incrível.

[00:10:43–00:11:02] **Host:** Relacionado a isso: você cria as evals certas e sabe que funciona, mas algumas empresas ainda têm certa aversão ao risco de colocar os agentes diante dos clientes e deixá-los executar as tarefas de maior impacto — que, no seu caso, seriam as vendas.

[00:11:02–00:11:04] **Host:** Seus agentes realmente vendem aos clientes?

[00:11:04–00:11:05] **Alejandro:** Sim.

[00:11:05–00:11:08] **Alejandro:** Nunca construímos agentes de suporte nem de atendimento ao cliente.

[00:11:09–00:11:11] **Alejandro:** Construímos agentes de vendas.

[00:11:11–00:11:15] **Alejandro:** É extremamente difícil vender um carro na América Latina.

[00:11:16–00:11:18] **Alejandro:** Então imagine alguém querendo comprar um carro.

[00:11:19–00:11:22] **Alejandro:** Eles podem escolher, tipo, entre, tipo, 20.000 SKUs.

[00:11:22–00:11:29] **Alejandro:** Depois precisam escolher o financiamento e passar pelo processo de financiamento, seguro e cobertura.

[00:11:29–00:11:32] **Alejandro:** E provavelmente estão trocando o carro deles.

[00:11:32–00:11:34] **Alejandro:** Então precisamos cotar esse carro.

[00:11:34–00:11:48] **Alejandro:** É um processo que, quando feito por uma pessoa — ou como a Kavak fazia em 2020 e 2021 —, exige ser extremamente bom em 15 coisas diferentes e ter 15 especialistas, em 15 equipes diferentes.

[00:11:48–00:12:00] **Alejandro:** Normalmente, a pessoa falava com o especialista em financiamento, o consultor de automóveis, o especialista em compras e o especialista em seguros; juntos, eles montavam um pacote e vendiam o carro.

[00:12:00–00:12:03] **Alejandro:** E isso é extremamente difícil de fazer.

[00:12:03–00:12:19] **Alejandro:** Mas, como, a primeira coisa que fizemos foi, ok, conseguir um agente para ser melhor do que o especialista em cada uma dessas coisas e depois juntá-lo e ter, como, um mega especialista que é um especialista em seguros, financiamento, et cetera.

[00:12:19–00:12:22] **Alejandro:** E é esse megaespecialista que colocamos diante do cliente.

[00:12:22–00:12:24] **Alejandro:** Então a experiência para o cliente é incrível.

[00:12:24–00:12:31] **Alejandro:** Triplicamos o NPS e a pontuação de satisfação do cliente colocando o agente em frente ao cliente.

[00:12:32–00:12:37] **Alejandro:** E, no início, converteu 50% mais do que a nossa equipe humana.

[00:12:37–00:12:43] **Alejandro:** Agora, a taxa de conversão é 2,1 vezes maior.

[00:12:44–00:12:45] **Alejandro:** Então é uma empresa completamente diferente.

[00:12:45–00:12:46] **Alejandro:** Então seus agentes são melhores vendedores.

[00:12:47–00:12:47] **Alejandro:** Muito melhor.

[00:12:47–00:12:59] **Alejandro:** E você consegue isso, né, porque são especialistas, e são infinitamente pacientes, e conhecem toda a sua história, e podem planejar a longo prazo, e nunca se cansam.

[00:12:59–00:13:09] **Alejandro:** Então, e se cometerem um erro, aprendem, e no dia seguinte, não só eles, mas os outros 200.000 agentes estarão aprendendo com esse erro.

[00:13:09–00:13:16] **Alejandro:** Esse é o ciclo de feedback que colocamos em prática, e seus efeitos aparecem no crescimento, nos resultados e na satisfação dos clientes.

[00:13:16–00:13:25] **Host:** Uma — na verdade, duas — das coisas muito interessantes sobre a Kavak é que o mundo já se acostumou à ideia de que a IA pode fazer atendimento ao cliente.

[00:13:25–00:13:26] **Host:** Ainda é muito difícil fazer bem.

[00:13:26–00:13:34] **Host:** Mas, sabe, como Gabe disse, ainda há uma visão de que, bem, os clientes não vão querer comprar coisas caras da IA, e você está provando que eles estão errados.

[00:13:34–00:13:35] **Alejandro:** Sim.

[00:13:35–00:13:42] **Host:** A próxima camada disso é que, bem, você não vai realmente ser capaz de fazer serviços financeiros regulamentados de ponta a ponta com IA.

[00:13:42–00:13:51] **Host:** Mas, ao examinar o que vocês fazem, vemos análise de crédito para clientes com histórico escasso ou inexistente, precificação correta e gestão do empréstimo.

[00:13:51–00:14:04] **Host:** Então talvez fale como você escreveu as avaliações para se sentir confortável com isso, e então versus, eu não sei, ir a uma filial bancária ou até mesmo a uma fintech, como essa experiência é muito melhor?

[00:14:04–00:14:18] **Alejandro:** O primeiro produto financeiro que lançamos foi um empréstimo de carro, e normalmente no México e em alguns mercados emergentes, leva dois meses ou mais para obter um empréstimo de carro aprovado.

[00:14:18–00:14:29] **Alejandro:** Normalmente aprovamos em menos de três minutos, o que é bastante legal, porque temos todos esses dados sobre o cliente e o carro.

[00:14:30–00:14:45] **Alejandro:** E, se o cliente não puder mais pagar pelo carro, ele o devolve; podemos oferecer um carro mais barato, com prestação mensal menor, e ajudá-lo a sair do sufoco. Isso é o incrível da integração vertical do negócio.

[00:14:45–00:14:54] **Alejandro:** Mas, assim, quando começamos a lançar outros produtos financeiros, percebemos que essa é uma decisão muito importante para o cliente, né?

[00:14:54–00:15:08] **Alejandro:** Normalmente levam de três a quatro meses para decidirem comprar um carro e obter um empréstimo ou um empréstimo pessoal, como um grande empréstimo pessoal que também oferecemos.

## 00:15:00–00:20:00

[00:15:08–00:15:22] **Alejandro:** Então, se você conhecer o seu cliente durante este processo e facilitar o processo para eles, então suas métricas de conversão e retenção começam a subir muito.

[00:15:22–00:15:49] **Alejandro:** Não é apenas a transação, é entender cada cliente pessoalmente e convertê-los quando estiverem prontos com uma personalização muito profunda da taxa de juros, do risco, do valor máximo do empréstimo, de uma forma que faz sentido para o portfólio como um todo, obviamente, mas que é otimizada para o nível de risco e provavelmente as outras ofertas que o cliente está recebendo.

[00:15:49–00:15:55] **Host:** E então talvez nos dê apenas para ser, você sabe, as avaliações são sempre um tópico muito quente, você meio que levou isso à frente.

[00:15:55–00:16:06] **Host:** Qual seria um exemplo de área em que é difícil desenhar evals, ou em que foi preciso investir tempo extra, dado que há dinheiro real e informações de identificação pessoal em risco?

[00:16:06–00:16:06] **Host:** Certo.

[00:16:06–00:16:06] **Alejandro:** Sim.

[00:16:06–00:16:23] **Alejandro:** Então, quando decidimos redesenhar a empresa em torno da IA, você perguntou se a IA vai conseguir fazer esse trabalho, até mesmo o de CEO ou cargos que envolvem liderança?

[00:16:23–00:16:25] **Alejandro:** E a resposta, honestamente, é provavelmente sim.

[00:16:25–00:16:28] **Alejandro:** Em 2035, nesse ritmo de melhoria, ela provavelmente será capaz de fazê-lo.

[00:16:28–00:16:30] **Alejandro:** Então nós dissemos, ok, vamos tentar agora.

[00:16:31–00:16:34] **Alejandro:** Vamos tentar criar um CEO de IA.

[00:16:35–00:16:38] **Alejandro:** Então, criamos uma cidade no México.

[00:16:38–00:16:39] **Alejandro:** É Cuernavaca.

[00:16:39–00:16:44] **Alejandro:** E colocamos um agente numa das nossas armaduras como CEO.

[00:16:45–00:16:49] **Alejandro:** E começa a aprender e começa a tomar decisões e a avaliar essas decisões.

[00:16:50–00:16:53] **Alejandro:** E só está rodando há seis semanas.

[00:16:53–00:16:58] **Alejandro:** O objetivo do primeiro mês foi duplicar os lucros de Cuernavaca.

[00:16:58–00:17:09] **Alejandro:** Não chegou a isso, mas foi 1,5 vez, como 50% mais lucros só administrando a cidade, o que é louco, certo?

[00:17:09–00:17:10] **Alejandro:** É incrível.

[00:17:10–00:17:12] **Alejandro:** E é o CEO.

[00:17:12–00:17:16] **Alejandro:** Como as pessoas diziam, era o último trabalho que a IA deveria ter feito.

[00:17:16–00:17:18] **Alejandro:** E não, não é mesmo.

[00:17:18–00:17:20] **Alejandro:** E como isso aconteceu?

[00:17:20–00:17:40] **Alejandro:** É como uma pessoa extremamente inteligente — no nível de uma Medalha Fields — examinando cada número e cada cliente, fazendo a previsão perfeita e microgerenciando tudo o que precisa ser executado diariamente para cumprir um plano.

[00:17:40–00:17:52] **Alejandro:** Então ele literalmente envia mensagens a todos os trabalhadores físicos em Cuernavaca com seus planos para o dia e pede que enviem notas de voz para informar o progresso.

[00:17:53–00:17:55] **Alejandro:** Assim, a satisfação dos clientes cresceu.

[00:17:56–00:17:57] **Alejandro:** Temos um inventário melhor.

[00:17:58–00:18:03] **Alejandro:** Nós rotamos melhor, melhor penetração de financiamento, como todos os KPIs começaram a melhorar.

[00:18:03–00:18:06] **Alejandro:** Então é super legal e super emocionante.

[00:18:06–00:18:15] **Alejandro:** Agora, quais são os empregos em que a gente acha que ainda é preciso treinar e contratar humanos?

[00:18:15–00:18:17] **Alejandro:** Estas estão relacionadas ao mundo físico.

[00:18:17–00:18:24] **Alejandro:** Então quando falamos de mecânica, Cuernavaca tem por aí, eu acho que no México, cerca de 800 mecânicos.

[00:18:24–00:18:29] **Alejandro:** Há muita destreza e sentidos que são muito difíceis de substituir.

[00:18:30–00:18:33] **Alejandro:** Então, também construímos esses agentes com o mesmo sistema que está escalando.

[00:18:34–00:18:37] **Alejandro:** E os mecânicos têm esse assistente.

[00:18:37–00:18:48] **Alejandro:** Estava dizendo a vocês antes, é como no filme Ratatouille, como o rato que é realmente um chef colaborando com um ser humano.

[00:18:48–00:18:49] **Alejandro:** É assim.

[00:18:49–00:18:50] **Alejandro:** Então é um ajudante.

[00:18:50–00:18:51] **Alejandro:** Nós o chamamos de El Mike.

[00:18:52–00:18:59] **Alejandro:** Ele lhes diz como inspecionar um carro, dá dicas e mostra como fazer.

[00:18:59–00:19:07] **Alejandro:** E a qualidade das inspeções, novamente, passou ao teto, estamos inspecionando mais rápido, estamos reparando mais rápido, é mais barato.

[00:19:07–00:19:11] **Alejandro:** Mas, mais importante, estamos entregando carros de maior qualidade.

[00:19:13–00:19:19] **Alejandro:** As garantias caíram cerca de 20 a 26% desde o lançamento.

[00:19:19–00:19:22] **Alejandro:** E a satisfação dos clientes, novamente, subiu.

[00:19:23–00:19:24] **Alejandro:** Então é isso.

[00:19:24–00:19:36] **Alejandro:** Como você desenharia sua organização do zero, com superinteligência abundante e barata, e simplesmente partiria para construí-la?

[00:19:37–00:19:51] **Host:** Agora, esta é uma boa transição para um tema central no Vale do Silício: muita gente está preocupada com a forma que terão as organizações do futuro e com o papel que os seres humanos desempenharão.

[00:19:51–00:19:51] **Host:** Sim.

[00:19:51–00:19:53] **Host:** E eu acho que você tocou um pouco nisso.

[00:19:53–00:19:57] **Host:** E então a gente adoraria ouvir, né, como vocês estão pensando nisso.

[00:19:57–00:19:57] **Host:** Sim.

[00:19:58–00:20:00] **Host:** E as organizações.

## 00:20:00–00:25:00

[00:20:00–00:20:00] **Host:** Sim.

[00:20:01–00:20:01] **Alejandro:** Com certeza.

[00:20:01–00:20:06] **Alejandro:** Então nós levamos essa questão muito a sério há três anos.

[00:20:06–00:20:11] **Alejandro:** E a verdade é que o trabalho de todos mudará.

[00:20:12–00:20:21] **Alejandro:** Então, e o que estávamos fazendo há alguns anos provavelmente será melhor feito por um agente de IA.

[00:20:22–00:20:22] **Alejandro:** Certo?

[00:20:22–00:20:23] **Alejandro:** Então, o que isso significa?

[00:20:23–00:20:25] **Alejandro:** Precisamos treinar todos.

[00:20:26–00:20:36] **Alejandro:** Então, lançamos um programa dentro do Kavak que se chama Academia Jedi onde qualquer pessoa do Kavak, como o CEO, para sim.

[00:20:36–00:20:36] **Alejandro:** E é fantástico.

[00:20:37–00:20:43] **Alejandro:** Como do CEO para engenheiros de IA até mecânicos, como ir à academia.

[00:20:43–00:20:49] **Alejandro:** É muito difícil. Eu mesmo conduzi o programa.

[00:20:49–00:20:50] **Host:** Você desenhou o programa.

[00:20:50–00:20:51] **Alejandro:** Eu desenhei o programa.

[00:20:51–00:20:52] **Alejandro:** Mas constantemente.

[00:20:52–00:20:53] **Host:** Constantemente.

[00:20:53–00:20:57] **Alejandro:** Porque você precisa estar atualizando o programa porque tudo está mudando tão rápido.

[00:20:57–00:21:04] **Alejandro:** E você não consegue mandar estas pessoas para fora, para o Stanford, para aprender isso, porque é uma coisa nova.

[00:21:04–00:21:04] **Alejandro:** Certo?

[00:21:05–00:21:07] **Alejandro:** Então treinamos a todos.

[00:21:07–00:21:14] **Alejandro:** E, após seis semanas, lançam agentes de última geração, agentes de IA para a produção.

[00:21:14–00:21:21] **Alejandro:** E são mecânicos e profissionais de finanças e engenheiros, como qualquer um pode fazê-lo.

[00:21:21–00:21:27] **Alejandro:** E o que isso gerou é que talvez esta pessoa não se torne um engenheiro de IA.

[00:21:27–00:21:32] **Alejandro:** Alguns têm, mas eles sabem colaborar com essa nova tecnologia.

[00:21:32–00:21:32] **Alejandro:** Certo?

[00:21:32–00:21:36] **Alejandro:** Então a forma como a gente olhou para isso foi, caras, lá, não há como voltar atrás.

[00:21:36–00:21:38] **Alejandro:** É nessa direção que a Kavak está avançando.

[00:21:38–00:21:40] **Alejandro:** Esta é a maneira como a empresa vai ficar.

[00:21:40–00:21:46] **Alejandro:** Estas são as mudanças para a equipe de engenharia, a equipe de finanças e a equipe de produtos.

[00:21:46–00:21:48] **Alejandro:** Assim, isso é o que vai mudar.

[00:21:49–00:21:56] **Alejandro:** Você tem a escolha de treinar e, e obter as habilidades para se destacar nesta nova realidade, neste novo mundo.

[00:21:58–00:22:01] **Alejandro:** Ou talvez deixe Kavak se isso não for para você, mas é assim que a gente está indo.

[00:22:02–00:22:03] **Alejandro:** E somos ótimos.

[00:22:04–00:22:07] **Alejandro:** Assim como nós, nós, fortalecemos a cultura e estávamos super empolgados.

[00:22:08–00:22:12] **Alejandro:** E as pessoas realmente sabem como construir esses sistemas agentes.

[00:22:12–00:22:19] **Alejandro:** Hoje, qualquer processo da Kavak é realmente uma colaboração entre agentes e seres humanos.

[00:22:19–00:22:23] **Alejandro:** E, às vezes, os agentes são os chefes ou, de, dos humanos.

[00:22:23–00:22:25] **Alejandro:** E, por vezes, os seres humanos estão projetando os agentes.

[00:22:25–00:22:29] **Alejandro:** Mas eu acho que a gente conseguiu realmente construir isso e mudar isso.

[00:22:30–00:22:38] **Alejandro:** E é por meio dessa ideia que precisamos estar aprendendo todos os dias e as coisas continuarão a mudar.

[00:22:38–00:22:46] **Alejandro:** A única maneira de continuar relevante é atualizar suas habilidades todo mês ou a cada poucos meses.

[00:22:46–00:22:50] **Host:** Mas você tem, ou teve, sabe-se lá, milhares de pessoas.

[00:22:51–00:22:53] **Host:** Agora, os agentes fazem a maior parte das coisas.

[00:22:53–00:22:53] **Host:** Sim.

[00:22:53–00:22:56] **Host:** Então, qual é a estrutura organizacional do Kavak?

[00:22:57–00:22:59] **Host:** Assim, o conceito de gerenciamento médio ainda existe?

[00:22:59–00:23:00] **Host:** Como é a estrutura da sua organização?

[00:23:00–00:23:00] **Alejandro:** Certo.

[00:23:01–00:23:06] **Alejandro:** Agora temos equipes muito horizontais, muito sêniores e altamente empoderadas.

[00:23:06–00:23:13] **Alejandro:** Se você olhar para uma equipe, encontrará engenharia, IA, operações — tudo.

[00:23:13–00:23:21] **Alejandro:** Elas constroem os agentes, trabalham para os agentes ou atuam no mundo físico diante do cliente.

[00:23:22–00:23:24] **Alejandro:** É assim que funciona a maior parte da nossa organização.

[00:23:24–00:23:36] **Alejandro:** Então, é realmente construído em torno da ideia de como as organizações serão no futuro, em torno da IA e, de fato, aproveitando essa nova tecnologia.

[00:23:36–00:23:43] **Alejandro:** Evidentemente, isso exigia muita retrainamento porque em 2023 ou 2022, ninguém estava construindo agentes.

[00:23:43–00:23:47] **Alejandro:** Ninguém estava ajudando os agentes ou tomando ordens dos agentes.

[00:23:47–00:23:56] **Alejandro:** A maneira de atender ao mundo físico ou aos clientes era diferente de quando um agente lhe diz o que fazer ou o ajuda a melhorar seu trabalho.

[00:23:56–00:23:57] **Host:** Sim.

[00:23:57–00:24:01] **Alejandro:** E é uma estrutura completamente diferente da que tínhamos há apenas dois anos.

[00:24:01–00:24:01] **Host:** Sim.

[00:24:01–00:24:05] **Host:** Explique, já falamos sobre isso antes, como é trabalhar para os agentes.

[00:24:05–00:24:07] **Host:** Acho que você o descreveu como um sistema agêntico.

[00:24:08–00:24:11] **Host:** Às vezes, quando ele falha, o caso é encaminhado para uma fila de atendimento humano.

[00:24:11–00:24:11] **Host:** Certo.

[00:24:11–00:24:12] **Host:** Mas aí isso fica perdido.

[00:24:13–00:24:14] **Host:** E como você uniu isso?

[00:24:14–00:24:22] **Alejandro:** Então, como o, o, vemos humanos nos loops e, e, e a maioria desses sistemas agentes em produção agora, como sistemas agentes em grande escala.

[00:24:22–00:24:33] **Alejandro:** Normalmente, se um agente encontra um obstáculo ou não consegue mais prosseguir, envia o caso ou o cliente para o suporte de nível dois e se esquece dele.

[00:24:34–00:24:37] **Alejandro:** Isso não funciona porque os ciclos não se fecham.

[00:24:37–00:24:41] **Alejandro:** Então, você não gera os dados para treinar o agente a fazer isso melhor.

[00:24:41–00:24:46] **Alejandro:** O que funciona hoje é ter um agente obcecado por cada cliente — milhões desses agentes.

[00:24:46–00:24:55] **Alejandro:** Eles têm acesso a todas as APIs e habilidades, e temos seres humanos construindo essas habilidades para eles.

[00:24:55–00:25:02] **Alejandro:** Se um agente encontra um obstáculo ou precisa cancelar algo, chama uma API dizendo: “Preciso de ajuda”.

## 00:25:00–00:30:00

[00:25:02–00:25:05] **Alejandro:** E, por outro lado, não é um agente ou um software.

[00:25:06–00:25:08] **Alejandro:** É um ser humano que está ajudando.

[00:25:08–00:25:14] **Alejandro:** Se você representar isso num organograma, verá equipes humanas que têm um agente.

[00:25:14–00:25:15] **Alejandro:** Estou obtendo melhores resultados.

[00:25:15–00:25:16] **Host:** É super claro.

[00:25:16–00:25:18] **Host:** Assim, faz sentido.

[00:25:18–00:25:19] **Host:** Na verdade, essa é uma transição perfeita.

[00:25:19–00:25:24] **Host:** Sei que muitos líderes de instituições maiores entram em contato com você.

[00:25:24–00:25:25] **Host:** Então, talvez isso lhe evite muitos telefonemas.

[00:25:25–00:25:31] **Host:** Mas acho que, racionalmente, muitos líderes empresariais entendem isso de forma intuitiva.

[00:25:31–00:25:37] **Host:** Ainda é muito difícil implantar IA em toda a organização.

[00:25:37–00:25:38] **Host:** Os modelos são bons o suficiente.

[00:25:38–00:25:39] **Host:** Você sabe disso.

[00:25:39–00:25:40] **Host:** É um problema organizacional.

[00:25:40–00:25:41] **Host:** É um problema psicológico.

[00:25:41–00:25:43] **Host:** Que conselho você daria, ou o que tem observado?

[00:25:43–00:25:45] **Alejandro:** Acho que são duas coisas.

[00:25:45–00:25:49] **Alejandro:** A primeira é que tem que ser de cima para baixo por causa disso.

[00:25:50–00:26:04] **Alejandro:** Se você buscar apenas adoção, não chegará a lugar nenhum, porque é difícil criar esse discernimento ou estratégia para que as pessoas decidam, de baixo para cima, o que construir e cheguem a algo que funcione para a empresa.

[00:26:04–00:26:12] **Alejandro:** A transformação precisa ser conduzida de cima para baixo; os líderes precisam adotar a tecnologia e ter um plano muito claro do que construir.

[00:26:12–00:26:14] **Alejandro:** Já vi tantas empresas.

[00:26:14–00:26:16] **Alejandro:** É assim, ah, assim, a gente está fazendo um hackathon.

[00:26:16–00:26:18] **Alejandro:** As pessoas apresentam casos de uso.

[00:26:18–00:26:20] **Alejandro:** Estamos patrocinando alguns desses casos de uso.

[00:26:20–00:26:21] **Alejandro:** Isso não funciona.

[00:26:21–00:26:30] **Alejandro:** É assim, estar muito claro sobre o que a empresa vai parecer em três ou cinco anos, e depois começar a construir isso.

[00:26:30–00:26:34] **Alejandro:** E ser, assim, muito vertical no direcionamento de suas tropas para isso.

[00:26:35–00:26:42] **Alejandro:** Um exército não funciona se cada um cria suas próprias ideias de estratégia e tática, vai ao campo de batalha e faz o que quer.

[00:26:42–00:26:45] **Alejandro:** Você precisa de uma estratégia muito clara, e isso é o que a gente precisa agora.

[00:26:46–00:26:47] **Alejandro:** Está na fase de transformação.

[00:26:48–00:26:53] **Alejandro:** A segunda é que você precisa medir o que realmente importa, e são as avaliações, mas também são as avaliações certas.

[00:26:54–00:27:00] **Alejandro:** Vejo muitas empresas gastando agora enormes quantias, e dizem, está bem, eu tenho adoção.

[00:27:00–00:27:04] **Alejandro:** Estou gastando centenas de milhões de dólares em tokens agora.

[00:27:04–00:27:05] **Alejandro:** E quanto a isso?

[00:27:06–00:27:07] **Alejandro:** Há qualidade nos tokens.

[00:27:07–00:27:10] **Alejandro:** Então eu tenho uma estrutura aqui que também é útil.

[00:27:11–00:27:21] **Alejandro:** Os tokens de nível três, os mais valiosos, são os usados por agentes cujo retorno de cada token específico pode ser calculado.

[00:27:21–00:27:22] **Alejandro:** E eu posso fazer isso agora.

[00:27:22–00:27:23] **Alejandro:** Isso é ótima notícia para mim.

[00:27:24–00:27:32] **Alejandro:** Porque eu estou crescendo, e porque sei o ROI de cada token, porque vai para os agentes que estão executando o trabalho da organização, né?

[00:27:32–00:27:33] **Alejandro:** Estes são os melhores tokens.

[00:27:33–00:27:38] **Alejandro:** Tier dois tokens são coisas que você pode medir indiretamente.

[00:27:38–00:27:40] **Alejandro:** Você vê desenvolvedores na base de código?

[00:27:41–00:27:45] **Alejandro:** Posso avaliar o valor desses tokens, ao menos indiretamente, e então levar o resultado para produção.

[00:27:46–00:27:53] **Alejandro:** No nível um, onde está a maioria das empresas, as pessoas apenas usam Claude Code, ChatGPT, Cowork ou qualquer outra ferramenta.

[00:27:53–00:27:54] **Alejandro:** O que aconteceu com aqueles?

[00:27:54–00:27:55] **Alejandro:** Não tenho ideia.

[00:27:56–00:27:57] **Alejandro:** Então não se trata apenas de adoção.

[00:27:57–00:28:08] **Alejandro:** É realmente ter uma visão muito clara e então medir se cada token que você gasta está trazendo esses benefícios e apenas iterar, iterar, iterar a partir daí.

[00:28:08–00:28:22] **Host:** Já tocamos um pouco nisso, mas vale aprofundar: talvez as empresas mais ambiciosas que estão ouvindo decidam seguir o exemplo. Vocês optaram por construir um agente por cliente, em vez de por tarefa.

[00:28:22–00:28:29] **Host:** E depois descobri ao longo do caminho que cada um desses agentes precisa de sua própria máquina microvirtual.

[00:28:29–00:28:33] **Host:** Explique-nos essas decisões e essa arquitetura.

[00:28:33–00:28:51] **Alejandro:** Acho que estamos vendo os resultados agora, mas foi uma aposta muito arriscada. As pessoas geralmente passam de fluxos de trabalho — e eu aconselharia todos a não construir fluxos de trabalho agênticos — para grafos, funções ou objetivos.

[00:28:51–00:28:57] **Alejandro:** Nós apostamos em sistemas multiagentes capazes de executar uma função inteira em torno de objetivos complexos.

[00:28:58–00:29:04] **Alejandro:** Como no exemplo que mencionei: para vender um carro, é preciso cuidar de financiamento, compra, recomendações e assim por diante.

[00:29:05–00:29:11] **Alejandro:** Em dezembro, já tínhamos milhares — dezenas de milhares — desses agentes trabalhando em escala e operando o negócio.

[00:29:11–00:29:18] **Alejandro:** Mas aí o Opus 4.5 saiu e eu percebi que esse não é mais o paradigma certo.

[00:29:19–00:29:30] **Alejandro:** Agora, a inteligência não precisa do grafo, da malha multiagente nem da estrutura de orquestração, porque isso restringiria esse nível de inteligência.

[00:29:30–00:29:54] **Alejandro:** Decidimos destruir tudo o que havíamos construído por dois anos — que funcionava, nos tornara lucrativos e gerara crescimento extraordinário — e recomeçar com uma estrutura que julgávamos robusta e escalável, capaz de aproveitar o autoaperfeiçoamento recursivo e os modelos mais inteligentes lançados a cada mês.

[00:29:54–00:30:08] **Alejandro:** O resultado é uma máquina virtual com um agente que tem acesso à memória, às evals, à interface de linha de comando, a todas as ferramentas e APIs da empresa e a uma meta de longo prazo.

## 00:30:00–00:35:00

[00:30:09–00:30:17] **Alejandro:** E instancio centenas de milhares desses cada dia com metas de longo prazo, como maximizar o valor ao longo da vida.

[00:30:17–00:30:19] **Alejandro:** A organização de autoaperfeiçoamento.

[00:30:19–00:30:19] **Host:** Exatamente.

[00:30:19–00:30:20] **Alejandro:** A organização de autoaperfeiçoamento.

[00:30:20–00:30:29] **Alejandro:** E acho que as pessoas estão super obcecadas com o RSI agora, e isso vai melhorar os modelos.

[00:30:30–00:30:41] **Alejandro:** Mas se você olhar para isso, o valor econômico na humanidade nos últimos 4.000 anos tem sido entregue por organizações, não por indivíduos.

[00:30:41–00:30:49] **Alejandro:** Então, o que você quer se autoaperfeiçoar e se engajar nesse ciclo é a organização que pode gerar mais valor econômico, certo?

[00:30:49–00:31:13] **Alejandro:** Esse é o ciclo em que penso que as empresas vão começar a concentrar-se, porque se conseguir que esse ciclo funcione e é uma organização que está realmente se auto-aprimorando e aproveitando os modelos mais recentes e a melhor inteligência que estamos obtendo a cada dois dias agora, então você atinge o exponencial, não apenas na inteligência, mas no valor que pode gerar como empresa.

[00:31:13–00:31:15] **Alejandro:** Então isso é realmente emocionante.

[00:31:15–00:31:28] **Host:** Você mencionou que, diante de todos os desafios de adoção da IA, via a maior oportunidade na criação de novas empresas estruturadas dessa forma e capazes de transformar os mercados.

[00:31:28–00:31:29] **Host:** Você quer falar um pouco sobre isso?

[00:31:29–00:31:30] **Alejandro:** Sim.

[00:31:30–00:31:37] **Alejandro:** Existe na economia o conceito de destruição criativa, de Joseph Schumpeter.

[00:31:38–00:31:56] **Alejandro:** A ideia é que a inovação não chega à economia porque as empresas adotam a nova tecnologia, mas porque algumas permanecem como eram e outras, munidas da nova tecnologia, destroem as antigas.

[00:31:56–00:32:08] **Alejandro:** Isso destrói valor a curto prazo na economia, mas a longo prazo é melhor para todos, pois estas novas empresas mais eficientes e eficazes fornecerão melhores produtos e serviços para a economia como um todo.

[00:32:08–00:32:13] **Alejandro:** E isso aconteceu nas revoluções industriais passadas, e isso sempre aconteceu.

[00:32:13–00:32:23] **Alejandro:** E é uma grande oportunidade para os empreendedores e as pessoas de hoje, pois é difícil adotar a IA de forma profunda.

[00:32:24–00:32:32] **Alejandro:** É muito difícil para um CEO hoje em dia, especialmente de uma grande empresa ou empresa pública, ir e dizer, hey, como se estivesse apostando tudo na IA.

[00:32:32–00:32:44] **Alejandro:** A empresa precisa assumir essa forma: “Vou destruir e reconstruir tudo o que ergui nos últimos 40 anos para me tornar uma empresa nativa de IA”.

[00:32:45–00:32:48] **Alejandro:** Quantos CEOs fariam isso em uma empresa de grande porte?

[00:32:48–00:33:03] **Alejandro:** Enquanto elas adotam a tecnologia, podem surgir novas empresas construídas em torno dos pontos fortes da IA, assumir a dianteira e levar novos produtos e serviços às massas.

[00:33:04–00:33:06] **Alejandro:** E isso já aconteceu antes.

[00:33:06–00:33:07] **Alejandro:** Assim aconteceu com a eletricidade.

[00:33:07–00:33:09] **Alejandro:** Essa é uma história que sempre conto para a minha equipe.

[00:33:10–00:33:18] **Alejandro:** As tecnologias para a linha de produção da Ford foram desenvolvidas em 1879 e 1881.

[00:33:19–00:33:27] **Alejandro:** Edison começou a comercializar a eletricidade em Nova York e depois em Londres, e inventou um dinamo extremamente eficiente.

[00:33:27–00:33:34] **Alejandro:** Então você poderia ter construído a fábrica da Ford 40 anos antes da Ford.

[00:33:35–00:33:35] **Alejandro:** A tecnologia estava lá.

[00:33:35–00:33:36] **Alejandro:** Tudo estava lá.

[00:33:36–00:33:49] **Alejandro:** Mas a maneira como as pessoas adotaram a eletricidade e o dinamismo de Ford foi, né, eu vou deixar minha fábrica com quatro pisos, eixos e cintos, e só mudar meu motor de carvão para um motor elétrico.

[00:33:49–00:33:52] **Alejandro:** Isso trará benefícios, sim, mas algo como 6% de eficiência.

[00:33:53–00:34:10] **Alejandro:** O que precisava ser feito era destruir aquela fábrica, construí-la numa superfície plana, não no centro de Nova York, mas em Connecticut ou New Jersey, e redesenhar toda a sua fábrica em torno de pequenos dinamos e eletricidade.

[00:34:10–00:34:20] **Alejandro:** Então se obtém uma melhoria de produtividade de cerca de 3x, que impulsionou os Estados Unidos durante o século XX.

[00:34:20–00:34:23] **Alejandro:** E o mesmo aconteceu novamente com o computador, e o mesmo está acontecendo novamente hoje.

[00:34:23–00:34:29] **Alejandro:** As pessoas querem adotá-lo, mas não estão dispostas a redesenhar toda a empresa, e adotam-no apenas superficialmente.

[00:34:29–00:34:37] **Alejandro:** E no final, isso lhe dará uma melhoria de 6% ou 10%, não uma melhoria de 10x.

[00:34:37–00:34:43] **Alejandro:** E é como o dilema do inovador em escala industrial de novo.

[00:34:45–00:34:50] **Host:** Acho que você acabou de apresentar aos futuros fundadores um argumento incrível de que é hora de construir.

[00:34:50–00:34:51] **Host:** É hora de construir.

[00:34:51–00:34:56] **Host:** Talvez um bom ponto para encerrar seja este: você construiu e expandiu sua própria empresa.

[00:34:56–00:34:58] **Host:** Agora você transformou a Kavak numa empresa totalmente orientada por agentes.

[00:34:59–00:35:03] **Host:** Que conselho você daria aos futuros fundadores ou aos fundadores de primeira viagem que possam estar ouvindo?

## 00:35:00–00:40:00

[00:35:04–00:35:07] **Alejandro:** Portanto, este é o momento mais emocionante da história humana.

[00:35:07–00:35:08] **Alejandro:** Eu acredito nisso.

[00:35:08–00:35:11] **Alejandro:** Estamos vivendo no momento mais emocionante da história humana.

[00:35:11–00:35:29] **Alejandro:** E é o momento mais emocionante para ser um fundador, porque é a primeira vez que alguém tem acesso às ferramentas e inteligência mais poderosas do mundo, quase de graça ou por 20 dólares por mês.

[00:35:29–00:35:38] **Alejandro:** A democratização das ferramentas para as pessoas construírem nunca foi assim na história humana.

[00:35:38–00:35:45] **Alejandro:** E há tantos problemas a serem resolvidos e uma nova realidade a ser construída em torno desse novo paradigma.

[00:35:46–00:35:49] **Alejandro:** Eu diria: simplesmente vá em frente, mas vá fundo.

[00:35:50–00:35:53] **Alejandro:** Imagine como será o futuro em torno da IA.

[00:35:54–00:35:57] **Alejandro:** Nem é exponencial.

[00:35:57–00:36:04] **Alejandro:** Basta traçar uma tendência linear, supondo que a IA continue melhorando em ritmo linear.

[00:36:04–00:36:11] **Alejandro:** Construa para esse futuro e você terá ideias maravilhosas, capazes de gerar muito valor para o mundo.

[00:36:13–00:36:13] **Host:** Incrível.

[00:36:14–00:36:15] **Host:** Ale, obrigado por participar.

[00:36:15–00:36:15] **Alejandro:** Obrigado.

[00:36:15–00:36:16] **Alejandro:** Obrigado pelo convite.
