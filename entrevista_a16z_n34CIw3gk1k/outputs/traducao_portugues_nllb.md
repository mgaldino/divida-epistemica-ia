# Tradução integral para o português

- Fonte utilizada: https://x.com/a16z/status/2086845184785203468
- Modelo local de tradução: `facebook/nllb-200-distilled-600M`
- Regra editorial: tradução integral; sem resumo e sem preenchimento de lacunas.

## 00:00:00–00:05:00

[00:00:00–00:00:04] **Speaker não identificado:** Hoje estou a investir mais em tokens do que em trabalhadores do conhecimento.

[00:00:04–00:00:06] **Speaker não identificado:** Podemos construir agentes sobre-humanos.

[00:00:07–00:00:09] **Speaker não identificado:** Isto significa que por todas as dimensões que importam,

[00:00:09–00:00:13] **Speaker não identificado:** Os nossos agentes superariam o melhor humano que já contratámos.

[00:00:13–00:00:16] **Speaker não identificado:** As empresas mais ambiciosas que ouvem isto decidirão seguir o exemplo.

[00:00:16–00:00:20] **Speaker não identificado:** que é que decidiu construir um agente por cliente.

[00:00:21–00:00:26] **Speaker não identificado:** Todos os dias, entre 100 e 200 mil agentes recebem instantâneos.

[00:00:26–00:00:29] **Speaker não identificado:** especificamente para este cliente com a sua própria máquina virtual.

[00:00:29–00:00:33] **Speaker não identificado:** Há muitas pessoas preocupadas com como as organizações do futuro vão ser.

[00:00:33–00:00:36] **Speaker não identificado:** e o papel que os seres humanos vão desempenhar.

[00:00:36–00:00:40] **Speaker não identificado:** Se você não enfrentou medo antes, não o sentiu, então não tentou a IA.

[00:00:40–00:00:44] **Speaker não identificado:** Lançámos um programa dentro do Kavak chamado Academia Jedi.

[00:00:44–00:00:49] **Speaker não identificado:** Do CEO aos engenheiros de IA aos mecânicos, treinamos todos.

[00:00:49–00:00:53] **Speaker não identificado:** E depois de seis semanas, lançam agentes de última geração na produção.

[00:00:53–00:00:57] **Speaker não identificado:** Que conselho tem para futuros fundadores ou fundadores pela primeira vez que podem estar a ouvir?

[00:00:57–00:00:59] **Speaker não identificado:** O que funciona agora é...

[00:00:59–00:01:04] **Speaker não identificado:** Bem-vindo ao podcast da ACC.

[00:01:05–00:01:07] **Speaker não identificado:** Hoje, temos o Ale Massa, o chefe da IA na Kavak.

[00:01:07–00:01:11] **Speaker não identificado:** Hoje vamos discutir a transformação que Ale levou dentro de Kavak.

[00:01:11–00:01:13] **Speaker não identificado:** transformar-se numa empresa nativa de IA.

[00:01:13–00:01:15] **Speaker não identificado:** Obrigado, Ale, por estar connosco hoje.

[00:01:15–00:01:16] **Speaker não identificado:** Obrigado por me teres convidado.

[00:01:16–00:01:20] **Speaker não identificado:** Antes de começar na Kavak, dirigia uma empresa chamada Opi Analytics.

[00:01:21–00:01:21] **Speaker não identificado:** - É isso mesmo.

[00:01:22–00:01:26] **Speaker não identificado:** E você estava muito interessado em IA antes do ChatGPT.

[00:01:26–00:01:28] **Speaker não identificado:** Queres contar-nos um pouco sobre essa viagem?

[00:01:28–00:01:29] **Speaker não identificado:** Sim, sim, claro.

[00:01:29–00:01:31] **Speaker não identificado:** Chamávamos-lhe aprendizado automático naquela época.

[00:01:31–00:01:33] **Speaker não identificado:** Era uma família diferente de algoritmos.

[00:01:33–00:01:41] **Speaker não identificado:** E nós fundamos uma empresa com uma visão muito ambiciosa que os novos modelos de aprendizado de máquina

[00:01:41–00:01:45] **Speaker não identificado:** seriam tão poderosas que poderiam resolver qualquer problema complexo.

[00:01:46–00:01:47] **Speaker não identificado:** Isto foi antes dos Transformers, certo?

[00:01:47–00:01:49] **Speaker não identificado:** Isto foi como em 2013.

[00:01:50–00:01:51] **Speaker não identificado:** Então começámos a construir a empresa dessa forma.

[00:01:51–00:01:57] **Speaker não identificado:** E acho que estávamos 10 anos à frente do tempo, mas construímos uma grande empresa.

[00:01:57–00:02:05] **Speaker não identificado:** Servimos cerca de 1.400, 500 empresas como algoritmos de risco, logística, previsão, marketing.

[00:02:05–00:02:18] **Speaker não identificado:** Mas realmente o poder do que os Transformers e depois o momento do ChatGPT quando chegou tornam as coisas muito claras

[00:02:18–00:02:29] **Speaker não identificado:** que agora poderíamos construir uma empresa completamente nova e forma de construir empresas.

[00:02:29–00:02:33] **Speaker não identificado:** Juntámos-nos a Kavak e ao Carlos para construí-lo.

[00:02:33–00:02:34] **Speaker não identificado:** É incrível.

[00:02:34–00:02:34] **Speaker não identificado:** Está bem. Está bem.

[00:02:34–00:02:39] **Speaker não identificado:** Vamos passar a maior parte deste podcast a falar exatamente sobre como identificou o Kavak.

[00:02:39–00:02:43] **Speaker não identificado:** Mas talvez apenas para começar, o que faz o Kavak e qual é o seu papel lá?

[00:02:43–00:02:47] **Speaker não identificado:** Kavak começou como um mercado de carros usados.

[00:02:47–00:02:53] **Speaker não identificado:** Então compramos carros, reformamos-os, e depois vendemos-os e financiamo-los.

[00:02:53–00:03:02] **Speaker não identificado:** Mas para fazer isso, também tivemos que construir uma FinTech e uma empresa de logística e o Carfax e como

[00:03:02–00:03:06] **Speaker não identificado:** Basicamente, toda a infraestrutura para isto funcionar não existia em LATAM.

[00:03:06–00:03:10] **Speaker não identificado:** Então tivemos que construir tudo verticalmente para podermos servir os nossos clientes da maneira certa.

[00:03:11–00:03:14] **Speaker não identificado:** Vou começar com o enquadramento do que a arquitetura parece.

[00:03:14–00:03:17] **Speaker não identificado:** Um consumidor entra e diz: "Quero vender o meu carro".

[00:03:17–00:03:19] **Speaker não identificado:** Como, quantos agentes tocam?

[00:03:19–00:03:20] **Speaker não identificado:** Como é que o cinto parece?

[00:03:20–00:03:22] **Speaker não identificado:** Diz-nos como desenhas isto.

[00:03:22–00:03:22] **Speaker não identificado:** - Sim, sim.

[00:03:22–00:03:27] **Speaker não identificado:** Então apostamos que a empresa se transformará numa empresa dirigida por agentes.

[00:03:27–00:03:37] **Speaker não identificado:** As perguntas que nos fazemos são: como construiríamos o Kavak em 2035 com inteligência de nível Fable 10 ou GPT-10?

[00:03:37–00:03:43] **Speaker não identificado:** Na verdade, essa empresa parece muito diferente daquilo que construímos ou do que tínhamos naquela época.

[00:03:44–00:03:52] **Speaker não identificado:** Então, quando um cliente entra agora mesmo, um agente será criado especificamente para esse cliente com sua própria máquina virtual.

[00:03:52–00:04:01] **Speaker não identificado:** Ele vai lembrar anos de interação desses clientes com Kavak, o que eles visitaram na página web ou uma chamada que eles tiveram há dois anos.

[00:04:01–00:04:14] **Speaker não identificado:** Então, lembre-se de tudo como na memória, invente uma estratégia e estabeleça um objetivo a longo prazo para maximizar o valor de vida deste cliente e fazer o que for preciso para fazer o cliente feliz.

[00:04:14–00:04:20] **Speaker não identificado:** E transformá-los em, tipo, todos os nossos diferentes produtos, tipo, ao longo do tempo.

[00:04:21–00:04:31] **Speaker não identificado:** E esta é uma arquitetura completamente nova e inovadora em escala, acho eu, porque, tipo, as pessoas ainda estão a construir um sistema multi-agente com especialistas.

[00:04:31–00:04:44] **Speaker não identificado:** E percebemos apostar que agentes de longa duração com objetivos difíceis, não apenas fluxos de trabalho, poderiam maximizar a satisfação dos nossos clientes e, obviamente, o seu valor ao longo da vida.

[00:04:44–00:04:45] **Speaker não identificado:** É fantástico.

[00:04:45–00:04:45] **Speaker não identificado:** Está bem. Está bem.

[00:04:45–00:04:47] **Speaker não identificado:** Então vamos saltar para as nuances disso.

[00:04:47–00:04:53] **Speaker não identificado:** Mas talvez contra muitas empresas que dizem: "Queremos ser agentes" e tentam alguns fluxos de trabalho.

[00:04:53–00:04:58] **Speaker não identificado:** Vocês fizeram o arranque, tivemos de fazer isto funcionar.

[00:04:58–00:04:59] **Speaker não identificado:** Tinhas de reduzir drasticamente o tamanho.

## 00:05:00–00:10:00

[00:05:00–00:05:02] **Speaker não identificado:** Não funcionou por um ano.

[00:05:02–00:05:02] **Speaker não identificado:** - Sim, sim.

[00:05:03–00:05:07] **Speaker não identificado:** Então, você quer falar, obviamente, você teve que sintonizar muitas coisas para fazer isso funcionar.

[00:05:07–00:05:12] **Speaker não identificado:** Descreva o arame naquela altura e quais modelos usava e especificamente.

[00:05:12–00:05:16] **Speaker não identificado:** Então, havia, tipo, três decisões principais que tínhamos de tomar.

[00:05:17–00:05:23] **Speaker não identificado:** O primeiro, e é aqui que eu acho que muitas empresas estão presas agora, é o primeiro instinto é, ok,

[00:05:23–00:05:24] **Speaker não identificado:** Vamos adotar a IA.

[00:05:25–00:05:31] **Speaker não identificado:** E basicamente deixas a tua estrutura como está e dás o ChatGPT ou o Claude à tua equipa.

[00:05:31–00:05:33] **Speaker não identificado:** E não há eficiências.

[00:05:33–00:05:36] **Speaker não identificado:** Os teus clientes têm os mesmos problemas e nada acontece, certo?

[00:05:36–00:05:43] **Speaker não identificado:** Então, precisa de redesenhar toda a sua empresa em torno dos agentes e das capacidades futuras.

[00:05:43–00:05:52] **Speaker não identificado:** Isto significa reconstruir a maior parte das suas APIs, reconstruir o sistema para que os agentes possam usá-las para executá-las.

[00:05:52–00:05:57] **Speaker não identificado:** Então, você precisa começar a gerar os dados e os circuitos de feedback para ajustar estes agentes.

[00:05:57–00:06:01] **Speaker não identificado:** A única maneira de fazê-los funcionar é ensiná-los.

[00:06:01–00:06:02] **Speaker não identificado:** Como é que os ensina?

[00:06:02–00:06:04] **Speaker não identificado:** Põe-as ao ar livre.

[00:06:04–00:06:05] **Speaker não identificado:** Põe-as à frente dos clientes.

[00:06:06–00:06:06] **Speaker não identificado:** Consegues os dados.

[00:06:06–00:06:07] **Speaker não identificado:** Consegues essas avaliações.

[00:06:07–00:06:11] **Speaker não identificado:** E depois treinas os teus agentes.

[00:06:12–00:06:17] **Speaker não identificado:** E esta é a segunda aposta que fizemos, que poderíamos construir agentes sobre-humanos.

[00:06:17–00:06:24] **Speaker não identificado:** Isto significa que por todas as dimensões que importam, como conversão, valor ao longo da vida, experiência do cliente,

[00:06:24–00:06:29] **Speaker não identificado:** Os nossos agentes superariam o melhor humano que já contratámos.

[00:06:29–00:06:30] **Speaker não identificado:** E colocamo-los na frente dos problemas mais difíceis.

[00:06:30–00:06:37] **Speaker não identificado:** E, finalmente, começamos a mudar a forma como medimos o sucesso da empresa.

[00:06:37–00:06:39] **Speaker não identificado:** A Kavak era uma empresa de transações.

[00:06:40–00:06:46] **Speaker não identificado:** Costumávamos medir quantos carros comprámos, quantos carros vendemos, quantos travões precisávamos, as almofadas de travões que precisávamos comprar.

[00:06:46–00:06:59] **Speaker não identificado:** E mudámos para uma empresa de relações onde agora tenho 10 milhões de clientes na minha base de dados e tenho agentes atribuídos à maioria deles com a tarefa de maximizar o seu valor ao longo da vida.

[00:06:59–00:07:05] **Speaker não identificado:** Agora, estamos a vender carros e empréstimos pessoais e itens muito caros.

[00:07:05–00:07:15] **Speaker não identificado:** Assim, apenas ativando 1% desta base de clientes, é como centenas de milhões de dólares se o fizermos da maneira certa.

[00:07:15–00:07:21] **Speaker não identificado:** Então é uma aposta que faz sentido para nós por causa da nossa indústria, por causa do bilhete, e porque no final do dia,

[00:07:22–00:07:27] **Speaker não identificado:** Os clientes precisam construir confiança com uma empresa porque estão a comprar um carro usado.

[00:07:27–00:07:34] **Speaker não identificado:** E a maneira de construir confiança é conhecê-los e planejar e cultivar um relacionamento a longo prazo.

[00:07:35–00:07:37] **Speaker não identificado:** Ale, só queria clicar duas vezes numa coisa.

[00:07:37–00:07:39] **Speaker não identificado:** Sabes, o mal sobre as demonstrações de agentes.

[00:07:40–00:07:40] **Speaker não identificado:** - Sim, sim, sim.

[00:07:40–00:07:47] **Speaker não identificado:** Provavelmente recebes muitos agentes e, sabes, nunca foi mais fácil construir coisas como antes.

[00:07:47–00:07:51] **Speaker não identificado:** Mas uma das perguntas é, como vocês vão avaliar isto?

[00:07:51–00:07:56] **Speaker não identificado:** Porque nem todos os testam em 90% das interações com os clientes para ver se funcionam.

[00:07:56–00:08:04] **Speaker não identificado:** E, vocês sabem, eu acredito que cerca de 98% das interações ou algo assim são agora manuseadas por agentes.

[00:08:04–00:08:04] **Speaker não identificado:** Sim, absolutamente.

[00:08:05–00:08:13] **Speaker não identificado:** Então, para lhe dar uma ideia da escala, como 96% de todas as interações são manuseadas por agentes.

[00:08:14–00:08:16] **Speaker não identificado:** Então, não há humanos lá.

[00:08:17–00:08:21] **Speaker não identificado:** Como 95% de todas as transações são totalmente manuseadas por agentes.

[00:08:21–00:08:25] **Speaker não identificado:** Obviamente, conhece-se um ser humano quando pega no carro, como se alguém estivesse lá para lhe dar as chaves.

[00:08:25–00:08:31] **Speaker não identificado:** Mas o resto da experiência da viagem é manuseado por um agente.

[00:08:31–00:08:38] **Speaker não identificado:** Todos os dias, entre 100.000 e 200.000 agentes recebem instantâneo num dia.

[00:08:38–00:08:39] **Speaker não identificado:** Eles acordam.

[00:08:39–00:08:44] **Speaker não identificado:** Às vezes trabalham por três minutos, às vezes por oito horas, às vezes por três dias.

[00:08:44–00:08:49] **Speaker não identificado:** E eles, como, definir um despertador para a sua próxima tarefa e voltar a dormir.

[00:08:49–00:08:52] **Speaker não identificado:** A escala disto é incrível.

[00:08:53–00:08:53] **Speaker não identificado:** E está a funcionar.

[00:08:53–00:08:57] **Speaker não identificado:** Como é que consegues que isto funcione em escala?

[00:08:58–00:09:01] **Speaker não identificado:** E a resposta que mencionou é avaliações.

[00:09:01–00:09:04] **Speaker não identificado:** Gosto de me mover extremamente rápido.

[00:09:05–00:09:08] **Speaker não identificado:** Mas para te moveres depressa, precisas de frenos, certo?

[00:09:08–00:09:08] **Speaker não identificado:** Imagina um carro.

[00:09:10–00:09:13] **Speaker não identificado:** Você vai bater no gás só se você tem os freios certos.

[00:09:14–00:09:15] **Speaker não identificado:** E a IA é super poderosa.

[00:09:15–00:09:22] **Speaker não identificado:** E eu vi muitas empresas cometerem esse erro porque tentam ir devagar porque não têm os freios certos.

[00:09:22–00:09:24] **Speaker não identificado:** Então pensei no contrário.

[00:09:24–00:09:25] **Speaker não identificado:** Como, a que velocidade podemos ir?

[00:09:26–00:09:28] **Speaker não identificado:** Bem, depende da qualidade das nossas avaliações.

[00:09:28–00:09:43] **Speaker não identificado:** Uma boa regra é que gastamos aproximadamente a mesma quantidade de tempo, tempo de engenharia, tokens e dinheiro na construção das avaliações que na construção dos agentes.

[00:09:43–00:09:48] **Speaker não identificado:** E é assim que se torna melhor e melhor e melhor, não deixando as avaliações como uma reflexão posterior.

[00:09:48–00:09:49] **Speaker não identificado:** Então, o que medimos?

[00:09:50–00:09:53] **Speaker não identificado:** Primeiro e acima de tudo, os resultados para o negócio.

[00:09:53–00:09:56] **Speaker não identificado:** Se o meu cliente estiver feliz, comprará um carro.

[00:09:56–00:09:59] **Speaker não identificado:** Eles vão ter o empréstimo aprovado.

[00:09:59–00:10:01] **Speaker não identificado:** Venderão-nos um carro.

## 00:10:00–00:15:00

[00:10:01–00:10:03] **Speaker não identificado:** E esse é o primeiro cheque.

[00:10:03–00:10:05] **Speaker não identificado:** Como, converteu-se?

[00:10:05–00:10:07] **Speaker não identificado:** E é aí que a maioria das coisas quebra.

[00:10:07–00:10:20] **Speaker não identificado:** Vejo empresas a medir o número de chamadas ou minutos durante a chamada ou alguns KPIs superficiais que lhe dão alguma informação, mas isso não funciona.

[00:10:20–00:10:30] **Speaker não identificado:** Como, o importante é se este cliente se converteu, está a trazer valor ao cliente, e o cliente está feliz em voltar a envolver-se conosco depois de um tempo?

[00:10:30–00:10:41] **Speaker não identificado:** E uma vez que você tem essas avaliações conectadas, então é apenas otimizar a arquitetura agencial certa e dar aos agentes habilidades para escalar isso e atender a milhões de clientes.

[00:10:43–00:10:43] **Speaker não identificado:** É realmente, realmente incrível.

[00:10:43–00:11:02] **Speaker não identificado:** E, você sabe, relacionado a isso é, tipo, ok, então você cria as avaliações certas, você sabe, está funcionando, você sabe, algumas pessoas, algumas empresas ainda se sentem um pouco arriscado e colocá-los na frente dos clientes e ser capaz de executar as tarefas de maior alavancagem, que em seu caso seria vender.

[00:11:02–00:11:04] **Speaker não identificado:** Os seus agentes vendem mesmo a clientes?

[00:11:04–00:11:05] **Speaker não identificado:** - Sim, sim, sim.

[00:11:05–00:11:08] **Speaker não identificado:** Então, nunca construímos um serviço de apoio ao cliente ou agentes de atendimento ao cliente.

[00:11:09–00:11:11] **Speaker não identificado:** Construímos agentes de vendas.

[00:11:11–00:11:15] **Speaker não identificado:** É extremamente difícil vender um carro na América Latina.

[00:11:16–00:11:18] **Speaker não identificado:** Então imagine alguém querendo comprar um carro.

[00:11:19–00:11:22] **Speaker não identificado:** Eles podem escolher, tipo, entre, tipo, 20.000 SKUs.

[00:11:22–00:11:29] **Speaker não identificado:** Depois precisam escolher o financiamento e passar pelo processo de financiamento, seguro e cobertura.

[00:11:29–00:11:32] **Speaker não identificado:** E provavelmente estão a trocar o carro deles.

[00:11:32–00:11:34] **Speaker não identificado:** Então, precisamos de citar esse carro.

[00:11:34–00:11:48] **Speaker não identificado:** Então é um processo que, se alguém o fizer ou como o Kaivak fez em 2020, 2021, era preciso ser extremamente bom em 15 coisas diferentes e ter 15 especialistas diferentes em 15 equipes diferentes.

[00:11:48–00:12:00] **Speaker não identificado:** E normalmente a pessoa falava com o especialista em finanças, o especialista em consultoria de automóveis, o especialista em compras, o especialista em seguros, e eles construíram um pacote e compraram um carro.

[00:12:00–00:12:03] **Speaker não identificado:** E isso é extremamente difícil de fazer.

[00:12:03–00:12:19] **Speaker não identificado:** Mas, como, a primeira coisa que fizemos foi, ok, podemos conseguir um agente para ser melhor do que o especialista em cada uma dessas coisas e depois juntá-lo e ter, como, um mega especialista que é um especialista em seguros, financiamento, etc.

[00:12:19–00:12:22] **Speaker não identificado:** E é o que colocamos na frente do cliente.

[00:12:22–00:12:24] **Speaker não identificado:** Então a experiência para o cliente é incrível.

[00:12:24–00:12:31] **Speaker não identificado:** triplicamos o NPS e a satisfação do cliente colocando o agente na frente do cliente.

[00:12:32–00:12:37] **Speaker não identificado:** E, no início, converteu 50% mais do que a nossa equipa humana.

[00:12:37–00:12:43] **Speaker não identificado:** E agora está a converter sobre isso, tipo, 2,1x mais.

[00:12:44–00:12:45] **Speaker não identificado:** Então é uma empresa completamente diferente.

[00:12:45–00:12:46] **Speaker não identificado:** Então os teus agentes são melhores vendedores.

[00:12:47–00:12:47] **Speaker não identificado:** Muito melhor.

[00:12:47–00:12:59] **Speaker não identificado:** E percebem isto, certo, porque são especialistas, e são infinitamente pacientes, e conhecem toda a vossa história, e podem planear a longo prazo, e nunca se cansam.

[00:12:59–00:13:09] **Speaker não identificado:** Então, se cometerem um erro, aprendem, e no dia seguinte, não só eles, mas os outros 200.000 agentes aprenderão com esse erro.

[00:13:09–00:13:16] **Speaker não identificado:** Este é o ciclo de feedback que envolvemos, e que está a mostrar o crescimento, os resultados e a satisfação dos nossos clientes.

[00:13:16–00:13:25] **Speaker não identificado:** Uma das duas coisas muito interessantes que penso sobre o Kavak é que acho que o mundo se tornou confortável com a IA que pode fazer serviço ao cliente.

[00:13:25–00:13:26] **Speaker não identificado:** Ainda é muito difícil fazer bem.

[00:13:26–00:13:34] **Speaker não identificado:** Mas, como disse Gabe, ainda há uma visão de que os clientes não vão querer comprar coisas caras da IA, e você está provando que eles estão errados.

[00:13:34–00:13:35] **Speaker não identificado:** - Sim, sim, sim.

[00:13:35–00:13:42] **Speaker não identificado:** A próxima camada disso é que, bem, você não vai realmente ser capaz de fazer serviços financeiros regulamentados de ponta a ponta com IA.

[00:13:42–00:13:51] **Speaker não identificado:** Mas se você passar pelo que está a fazer, está a subscrever um cliente magro ou sem arquivo, a preços corretos, a fazer serviço.

[00:13:51–00:14:04] **Speaker não identificado:** Então talvez falem sobre como escreveram as avaliações para se sentirem confortáveis com isso, e então versus, eu não sei, ir a uma filial bancária ou até mesmo a uma fintech, como é que essa experiência é muito melhor?

[00:14:04–00:14:18] **Speaker não identificado:** O primeiro produto financeiro que lançámos foi um empréstimo de carro, e normalmente no México e em alguns mercados emergentes, leva dois meses ou mais para obter um empréstimo de carro aprovado.

[00:14:18–00:14:29] **Speaker não identificado:** Normalmente aprovamos em menos de três minutos, o que é muito legal, porque temos todos estes dados sobre o cliente e o carro.

[00:14:30–00:14:45] **Speaker não identificado:** E se o cliente não puder pagar mais o carro, devolver-nos-á, e podemos dar-lhe um carro mais barato, e depois pagam uma quantia menor a cada mês, e gostam de sair da água, o que é incrível sobre a integração vertical do negócio.

[00:14:45–00:14:54] **Speaker não identificado:** Mas depois, quando começámos a lançar outros produtos financeiros, percebemos que esta é uma decisão muito importante para o cliente, certo?

[00:14:54–00:15:08] **Speaker não identificado:** Normalmente levam de três a quatro meses para decidirem comprar um carro e obter um empréstimo ou um empréstimo pessoal, como um grande empréstimo pessoal que também fazemos.

## 00:15:00–00:20:00

[00:15:08–00:15:22] **Speaker não identificado:** Então, se você conhecer o seu cliente durante este processo e facilitar o processo para eles, então apenas as suas métricas de conversão e retenção começam a passar pelo telhado.

[00:15:22–00:15:49] **Speaker não identificado:** Não é apenas a transação, é entender cada cliente pessoalmente e fazê-los converter quando estiverem prontos com uma personalização muito profunda da taxa de juros, do risco, do valor máximo do empréstimo de uma forma que faz sentido para o portfólio como um todo, obviamente, mas que é otimizado para o nível de risco e provavelmente as outras ofertas que o cliente está a receber.

[00:15:49–00:15:55] **Speaker não identificado:** E então talvez nos dê apenas para ser, você sabe, avaliações são sempre um tópico muito quente, você meio que liderou com isso.

[00:15:55–00:16:06] **Speaker não identificado:** Qual é um exemplo de talvez uma área difícil de projetar para avaliações ou uma onde você teve que gastar uma quantidade extra de tempo com apenas dado o fato de que, como, há dinheiro real PII em risco?

[00:16:06–00:16:06] **Speaker não identificado:** - Sim, sim.

[00:16:06–00:16:06] **Speaker não identificado:** - Sim, sim, sim.

[00:16:06–00:16:23] **Speaker não identificado:** Então, quando decidimos redesenhar a empresa em torno da IA, você fez a pergunta, OK, será que a IA vai ser capaz de fazer este trabalho, como mesmo o trabalho do CEO ou trabalhos onde a liderança está?

[00:16:23–00:16:25] **Speaker não identificado:** E a resposta, honestamente, é provavelmente sim.

[00:16:25–00:16:28] **Speaker não identificado:** Como em 2035 com uma taxa de melhoria, será capaz de fazer.

[00:16:28–00:16:30] **Speaker não identificado:** Então nós dissemos, ok, vamos tentar agora.

[00:16:31–00:16:34] **Speaker não identificado:** Vamos tentar construir um CEO de IA.

[00:16:35–00:16:38] **Speaker não identificado:** Então, arranjamos uma cidade no México.

[00:16:38–00:16:39] **Speaker não identificado:** É a Cuernavaca.

[00:16:39–00:16:44] **Speaker não identificado:** E colocamos como um agente numa das nossas armaduras como CEO.

[00:16:45–00:16:49] **Speaker não identificado:** E começa a aprender e começa a tomar decisões e a avaliar essas decisões.

[00:16:50–00:16:53] **Speaker não identificado:** E só está a funcionar há seis semanas.

[00:16:53–00:16:58] **Speaker não identificado:** O objetivo do primeiro mês era dobrar os lucros de Cuernavaca.

[00:16:58–00:17:09] **Speaker não identificado:** Não alcançou, mas foi 1,5x, como 50% mais lucros só administrando a cidade, o que é loucura, certo?

[00:17:09–00:17:10] **Speaker não identificado:** É incrível.

[00:17:10–00:17:12] **Speaker não identificado:** E é o CEO.

[00:17:12–00:17:16] **Speaker não identificado:** Como as pessoas diziam, era o último trabalho que a IA devia ter feito.

[00:17:16–00:17:18] **Speaker não identificado:** E não, não é mesmo.

[00:17:18–00:17:20] **Speaker não identificado:** E como é que isto aconteceu?

[00:17:20–00:17:40] **Speaker não identificado:** E é como uma pessoa muito inteligente, como campos, níveis de metais, inteligente, como entrar em cada número, cada cliente, fazer a previsão perfeita e micro-gerenciar todas as coisas que precisam ser executadas todos os dias para chegar a um plano.

[00:17:40–00:17:52] **Speaker não identificado:** Então ele literalmente vai enviar mensagens a todos os trabalhadores físicos em Cuernavaca com os seus planos para o dia e pedir-lhes para enviar notas de voz para saber o seu progresso.

[00:17:53–00:17:55] **Speaker não identificado:** Assim, a satisfação do cliente cresceu.

[00:17:56–00:17:57] **Speaker não identificado:** Temos um inventário melhor.

[00:17:58–00:18:03] **Speaker não identificado:** Nós rotamos melhor, melhor penetração do financiamento, como cada KPI começou a melhorar.

[00:18:03–00:18:06] **Speaker não identificado:** Então é super fixe e super emocionante.

[00:18:06–00:18:15] **Speaker não identificado:** Agora, quais são os empregos onde pensamos que ainda somos como treinamento e contratação de humanos?

[00:18:15–00:18:17] **Speaker não identificado:** Estes estão relacionados ao mundo físico.

[00:18:17–00:18:24] **Speaker não identificado:** Então, quando falamos de mecânica, Cuernavaca tem por aí, eu acho que no México, cerca de 800 mecânicos.

[00:18:24–00:18:29] **Speaker não identificado:** Há muita destreza e sentidos que são muito difíceis de substituir.

[00:18:30–00:18:33] **Speaker não identificado:** Então, também construímos estes agentes com o mesmo arame que está a escalar.

[00:18:34–00:18:37] **Speaker não identificado:** E os mecânicos têm o ajudante.

[00:18:37–00:18:48] **Speaker não identificado:** Estava a dizer-vos antes, é como no filme Ratatouille, como o rato que é um chef a colaborar com um ser humano.

[00:18:48–00:18:49] **Speaker não identificado:** É assim.

[00:18:49–00:18:50] **Speaker não identificado:** Então é um ajudante.

[00:18:50–00:18:51] **Speaker não identificado:** Chamamos-lhe El Maic.

[00:18:52–00:18:59] **Speaker não identificado:** E diz-lhes como inspecionar um carro e dá-lhes dicas e mostra-lhes como fazê-lo.

[00:18:59–00:19:07] **Speaker não identificado:** E a qualidade das inspeções, outra vez, passou pelo telhado, estamos a inspecionar mais rápido, estamos a reparar mais rápido, é mais barato.

[00:19:07–00:19:11] **Speaker não identificado:** Mas o mais importante, estamos a entregar carros de melhor qualidade.

[00:19:13–00:19:19] **Speaker não identificado:** As garantias diminuíram cerca de 20, 26% desde o lançamento.

[00:19:19–00:19:22] **Speaker não identificado:** E a satisfação do cliente, novamente, subiu.

[00:19:23–00:19:24] **Speaker não identificado:** Então é sobre isto.

[00:19:24–00:19:36] **Speaker não identificado:** Como desenhaste a tua organização a partir do zero com uma superinteligência abundante que é barata e vais construí-la?

[00:19:37–00:19:51] **Speaker não identificado:** Natalie, isto é uma boa continuação para um tópico chave neste momento no Vale do Silício, onde, sabes, há muitas pessoas preocupadas com como as organizações do futuro vão parecer e o papel que os seres humanos vão desempenhar.

[00:19:51–00:19:51] **Speaker não identificado:** - Sim, sim, sim.

[00:19:51–00:19:53] **Speaker não identificado:** E acho que tocaste um pouco nisso.

[00:19:53–00:19:57] **Speaker não identificado:** Gostaríamos de saber como pensam sobre isso.

[00:19:57–00:19:57] **Speaker não identificado:** - Sim, sim, sim.

[00:19:58–00:20:00] **Speaker não identificado:** E as organizações.

## 00:20:00–00:25:00

[00:20:00–00:20:00] **Speaker não identificado:** - Sim, sim, sim.

[00:20:01–00:20:01] **Speaker não identificado:** Absolutamente.

[00:20:01–00:20:06] **Speaker não identificado:** Então, tomámos essa pergunta muito a sério há três anos.

[00:20:06–00:20:11] **Speaker não identificado:** E a verdade é que o trabalho de todos mudará.

[00:20:12–00:20:21] **Speaker não identificado:** O que estávamos a fazer há uns anos provavelmente será melhor feito por um agente de IA.

[00:20:22–00:20:22] **Speaker não identificado:** Não é verdade?

[00:20:22–00:20:23] **Speaker não identificado:** Então, o que significa isso?

[00:20:23–00:20:25] **Speaker não identificado:** Precisamos de treinar todos.

[00:20:26–00:20:36] **Speaker não identificado:** Então, lançámos um programa dentro do Kavak que se chama Academia Jedi onde qualquer pessoa do Kavak, como o CEO para, sim.

[00:20:36–00:20:36] **Speaker não identificado:** E é fantástico.

[00:20:37–00:20:43] **Speaker não identificado:** Como o CEO para gostar de engenheiros de IA para mecânicos, como ir à academia.

[00:20:43–00:20:49] **Speaker não identificado:** É super difícil, como eu, eu, eu, eu, eu, como conduzido, como conduzido para mim mesmo.

[00:20:49–00:20:50] **Speaker não identificado:** Tu desenhaste o programa.

[00:20:50–00:20:51] **Speaker não identificado:** Eu desenhei o programa.

[00:20:51–00:20:52] **Speaker não identificado:** Mas constantemente.

[00:20:52–00:20:53] **Speaker não identificado:** Constantemente.

[00:20:53–00:20:57] **Speaker não identificado:** Porque precisas de atualizar o programa porque tudo está a mudar tão rápido.

[00:20:57–00:21:04] **Speaker não identificado:** E não podes mandar estas pessoas para Stanford para aprenderem isto, porque é algo novo.

[00:21:04–00:21:04] **Speaker não identificado:** Não é verdade?

[00:21:05–00:21:07] **Speaker não identificado:** Então nós treinamos todos.

[00:21:07–00:21:14] **Speaker não identificado:** E depois de seis semanas, lançam agentes de última geração, agentes de IA para a produção.

[00:21:14–00:21:21] **Speaker não identificado:** E são mecânicos e financiadores e engenheiros, como qualquer um pode fazê-lo.

[00:21:21–00:21:27] **Speaker não identificado:** E o que isso gerou é que talvez esta pessoa não se torne um engenheiro de IA.

[00:21:27–00:21:32] **Speaker não identificado:** Alguns têm, mas sabem como colaborar com esta nova tecnologia.

[00:21:32–00:21:32] **Speaker não identificado:** Não é verdade?

[00:21:32–00:21:36] **Speaker não identificado:** Então, a forma como olhamos para isto foi, rapazes, não há como voltar atrás.

[00:21:36–00:21:38] **Speaker não identificado:** Como se este fosse o caminho do Kavak.

[00:21:38–00:21:40] **Speaker não identificado:** É assim que a empresa vai parecer.

[00:21:40–00:21:46] **Speaker não identificado:** Estas são as mudanças para a equipa de engenharia, a equipa de finanças, a equipa de produtos.

[00:21:46–00:21:48] **Speaker não identificado:** Isto é o que vai mudar.

[00:21:49–00:21:56] **Speaker não identificado:** Você tem a escolha de gostar de treinar e, e obter as habilidades para se apresentar nesta nova realidade, neste novo mundo.

[00:21:58–00:22:01] **Speaker não identificado:** Ou talvez deixes o Kavak se não for para ti, mas é assim que vamos.

[00:22:02–00:22:03] **Speaker não identificado:** E somos óptimos.

[00:22:04–00:22:07] **Speaker não identificado:** Como nós, nós, fortalecemos a cultura e estávamos super empolgados.

[00:22:08–00:22:12] **Speaker não identificado:** E as pessoas realmente sabem como construir esses sistemas agentes.

[00:22:12–00:22:19] **Speaker não identificado:** E se olharmos para o Kavak agora, qualquer processo, é realmente uma colaboração de agentes e humanos.

[00:22:19–00:22:23] **Speaker não identificado:** E, às vezes, como agentes, são os chefes ou, dos humanos.

[00:22:23–00:22:25] **Speaker não identificado:** E, às vezes, os seres humanos desenham os agentes.

[00:22:25–00:22:29] **Speaker não identificado:** Mas acho que conseguimos realmente construir isto e mudar isto.

[00:22:30–00:22:38] **Speaker não identificado:** E é através desta ideia que precisamos de aprender todos os dias e as coisas continuarão a mudar.

[00:22:38–00:22:46] **Speaker não identificado:** E a única maneira de continuarmos relevantes é melhorar as nossas habilidades a cada mês ou a cada dois meses.

[00:22:46–00:22:50] **Speaker não identificado:** Mas tens, ou tens, milhares de pessoas.

[00:22:51–00:22:53] **Speaker não identificado:** Agora os agentes fazem a maioria das coisas.

[00:22:53–00:22:53] **Speaker não identificado:** - Sim, sim, sim.

[00:22:53–00:22:56] **Speaker não identificado:** Então, qual é a estrutura orgânica do Kavak?

[00:22:57–00:22:59] **Speaker não identificado:** Como, o conceito de gerenciamento médio já existe?

[00:22:59–00:23:00] **Speaker não identificado:** Como é que parece o teu órgão?

[00:23:00–00:23:00] **Speaker não identificado:** - Sim, sim.

[00:23:01–00:23:06] **Speaker não identificado:** Assim, a forma como parece agora são equipes muito planas, equipes muito antigas, super empoderadas.

[00:23:06–00:23:13] **Speaker não identificado:** Se olharmos para uma equipa, temos engenharia, IA, como operações, como tudo.

[00:23:13–00:23:21] **Speaker não identificado:** E eles estão a construir os agentes, a trabalhar para os agentes, ou a estar no mundo físico na frente do cliente.

[00:23:22–00:23:24] **Speaker não identificado:** A maior parte da nossa organização parece assim.

[00:23:24–00:23:36] **Speaker não identificado:** Então, é realmente construído em torno da ideia de como as organizações serão no futuro e em torno da IA e realmente aproveitando esta nova tecnologia.

[00:23:36–00:23:43] **Speaker não identificado:** Obviamente, isso exigia muita reformulação porque em 2023 ou 2022, ninguém estava a construir agentes.

[00:23:43–00:23:47] **Speaker não identificado:** Ninguém estava a ajudar agentes ou a receber ordens de agentes.

[00:23:47–00:23:56] **Speaker não identificado:** E a forma como atendemos ao mundo físico ou aos clientes era diferente de quando um agente nos diz o que fazer ou nos ajuda a melhorar o nosso trabalho.

[00:23:56–00:23:57] **Speaker não identificado:** - Sim, sim, sim.

[00:23:57–00:24:01] **Speaker não identificado:** E é uma estrutura completamente diferente do que tínhamos há apenas dois anos.

[00:24:01–00:24:01] **Speaker não identificado:** - Sim, sim, sim.

[00:24:01–00:24:05] **Speaker não identificado:** Explique, já falámos sobre isto antes, como é trabalhar para os agentes.

[00:24:05–00:24:07] **Speaker não identificado:** Acho que a forma como descreveu foi um sistema de agentes.

[00:24:08–00:24:11] **Speaker não identificado:** E às vezes, quando falha, é como, oh, isso é jogado para uma espécie de sinal humano.

[00:24:11–00:24:11] **Speaker não identificado:** - Sim, sim.

[00:24:11–00:24:12] **Speaker não identificado:** Mas depois isso está perdido.

[00:24:13–00:24:14] **Speaker não identificado:** E como é que conseguiste juntar isso?

[00:24:14–00:24:22] **Speaker não identificado:** Então, como o, o, vemos humanos nos circuitos e, e, e a maioria desses sistemas agentes em produção agora, como sistemas agentes em grande escala.

[00:24:22–00:24:33] **Speaker não identificado:** Normalmente, se um agente atinge uma parede ou não consegue atuar mais, vai enviar o caso ou o cliente para um suporte de nível dois e esquecer.

[00:24:34–00:24:37] **Speaker não identificado:** Isso não funciona porque não fechamos os circuitos.

[00:24:37–00:24:41] **Speaker não identificado:** Então, não gera os dados para treinar o agente a fazer isso melhor.

[00:24:41–00:24:46] **Speaker não identificado:** O que funciona agora é que temos um agente obcecado por cada um dos clientes, como milhões disto.

[00:24:46–00:24:55] **Speaker não identificado:** Eles têm acesso a cada API, a cada habilidade, e nós temos agentes a construir esses seres humanos, a construir essas habilidades para eles.

[00:24:55–00:25:02] **Speaker não identificado:** E depois, se um agente bater numa parede ou cancelar algo, chama esta API dizendo, preciso de ajuda.

## 00:25:00–00:30:00

[00:25:02–00:25:05] **Speaker não identificado:** E por outro lado, não é um agente nem um software.

[00:25:06–00:25:08] **Speaker não identificado:** É um ser humano a ajudá-los.

[00:25:08–00:25:14] **Speaker não identificado:** Mas se você mapear isto em um gráfico org, são realmente equipes humanas que têm um agente.

[00:25:14–00:25:15] **Speaker não identificado:** Estou a obter melhores resultados.

[00:25:15–00:25:16] **Speaker não identificado:** Está super claro.

[00:25:16–00:25:18] **Speaker não identificado:** Como, faz sentido.

[00:25:18–00:25:19] **Speaker não identificado:** Na verdade, é uma sequência perfeita.

[00:25:19–00:25:24] **Speaker não identificado:** E sei que tens muitos líderes em instituições maiores a chegar até ti.

[00:25:24–00:25:25] **Speaker não identificado:** Então, talvez isso lhe economize muitas chamadas telefónicas.

[00:25:25–00:25:31] **Speaker não identificado:** Mas acho que racionalmente, muitos líderes de empresas intuitivamente entendem isso.

[00:25:31–00:25:37] **Speaker não identificado:** Ainda é muito difícil implementar a IA através da sua organização.

[00:25:37–00:25:38] **Speaker não identificado:** Os modelos são bons o suficiente.

[00:25:38–00:25:39] **Speaker não identificado:** Tu sabes disso.

[00:25:39–00:25:40] **Speaker não identificado:** É um problema org.

[00:25:40–00:25:41] **Speaker não identificado:** É um problema psicológico.

[00:25:41–00:25:43] **Speaker não identificado:** Como, que conselhos tens ou o que viste?

[00:25:43–00:25:45] **Speaker não identificado:** Acho que são duas coisas.

[00:25:45–00:25:49] **Speaker não identificado:** A primeira é que tem que ser de cima para baixo por causa disto.

[00:25:50–00:26:04] **Speaker não identificado:** Por exemplo, se conseguirmos a adoção, não vai a lado nenhum, porque é difícil gerar esse gosto ou estratégia para as pessoas chegarem ao fundo, decidirem o que construir e o que não, e chegarem a algo que funcione para a empresa.

[00:26:04–00:26:12] **Speaker não identificado:** Portanto, a transformação tem de ser de cima para baixo, e os líderes têm de adotar, e os líderes têm de ter um plano muito claro sobre o que construir.

[00:26:12–00:26:14] **Speaker não identificado:** Já vi tantas empresas.

[00:26:14–00:26:16] **Speaker não identificado:** É como se estivéssemos a fazer um hackathon.

[00:26:16–00:26:18] **Speaker não identificado:** As pessoas estão a pensar em casos de uso.

[00:26:18–00:26:20] **Speaker não identificado:** Estamos a patrocinar alguns destes casos de uso.

[00:26:20–00:26:21] **Speaker não identificado:** - Isso não funciona.

[00:26:21–00:26:30] **Speaker não identificado:** É como, ter muito claro como será a empresa daqui a três ou cinco anos, e depois começar a construir isso.

[00:26:30–00:26:34] **Speaker não identificado:** E sejam muito verticais a guiar as suas tropas para isso.

[00:26:35–00:26:42] **Speaker não identificado:** Um exército não funciona se todos tiverem ideias sobre estratégia e tática e vão ao campo de batalha e fazem o que quiserem.

[00:26:42–00:26:45] **Speaker não identificado:** Precisas de uma estratégia muito clara, e é isso que precisamos agora.

[00:26:46–00:26:47] **Speaker não identificado:** Está numa fase de transformação.

[00:26:48–00:26:53] **Speaker não identificado:** A segunda é que você precisa medir o que realmente importa, e são avaliações, mas também são as avaliações certas.

[00:26:54–00:27:00] **Speaker não identificado:** Vejo muitas empresas gastando agora enormes quantias, e dizem, está bem, eu tenho adoção.

[00:27:00–00:27:04] **Speaker não identificado:** Estou a gastar centenas de milhões de dólares em tokens agora.

[00:27:04–00:27:05] **Speaker não identificado:** Que tal isso?

[00:27:06–00:27:07] **Speaker não identificado:** Há qualidade nos tokens.

[00:27:07–00:27:10] **Speaker não identificado:** Então eu tenho uma estrutura aqui que também é útil.

[00:27:11–00:27:21] **Speaker não identificado:** Como, tokens de nível três, os mais valiosos, são estes agentes onde você pode obter o ROI de cada token específico.

[00:27:21–00:27:22] **Speaker não identificado:** E posso fazer isso agora.

[00:27:22–00:27:23] **Speaker não identificado:** Isso é ótima notícia para mim.

[00:27:24–00:27:32] **Speaker não identificado:** Porque estou a crescer, e porque sei o ROI de cada token, porque vai para os agentes que estão a executar o trabalho da organização, certo?

[00:27:32–00:27:33] **Speaker não identificado:** Estes são os melhores tokens.

[00:27:33–00:27:38] **Speaker não identificado:** Tokens de nível dois são coisas que você pode medir indiretamente.

[00:27:38–00:27:40] **Speaker não identificado:** Vejo desenvolvedores na base de código?

[00:27:41–00:27:45] **Speaker não identificado:** E posso avaliar o valor desses tokens, pelo menos indiretamente, e depois empurrá-los para produções.

[00:27:46–00:27:53] **Speaker não identificado:** O primeiro nível, quando a maioria das empresas estão, é que as pessoas estão apenas a usar código plug ou chat GPT ou cowork ou o que quer que seja.

[00:27:53–00:27:54] **Speaker não identificado:** O que aconteceu com eles?

[00:27:54–00:27:55] **Speaker não identificado:** - Não faço ideia.

[00:27:56–00:27:57] **Speaker não identificado:** Então não se trata apenas de adoção.

[00:27:57–00:28:08] **Speaker não identificado:** Trata-se de ter uma visão muito clara e depois medir que cada token que você gasta lhe traz esses benefícios e apenas iterar, iterar, iterar a partir daí.

[00:28:08–00:28:22] **Speaker não identificado:** E nós tocámos sobre isso um pouco, mas acho que vale a pena mergulhar, pois talvez as empresas mais ambiciosas que ouvem isto decidam seguir o exemplo, que é que você decidiu construir um agente por cliente versus por tarefa.

[00:28:22–00:28:29] **Speaker não identificado:** E depois descobri ao longo do caminho que cada um desses agentes precisa de sua própria máquina micro-virtual.

[00:28:29–00:28:33] **Speaker não identificado:** Então, talvez nos acompanhe nessas decisões, naquela arquitetura.

[00:28:33–00:28:51] **Speaker não identificado:** E acho que estamos a ver estes resultados agora, mas era uma aposta muito arriscada porque as pessoas costumam passar de fluxos de trabalho, como se eu pudesse aconselhar a todos, não construir fluxos de trabalho agentes, para gráficos ou funções ou objetivos.

[00:28:51–00:28:57] **Speaker não identificado:** E construímos isso, que estes são sistemas multi-agentes que podem executar uma função inteira para um objetivo complexo.

[00:28:58–00:29:04] **Speaker não identificado:** Como aqueles que eu disse que para vender um carro, você precisa fazer financiamento, compras, como recomendações, etc.

[00:29:05–00:29:11] **Speaker não identificado:** E tínhamos milhares, dezenas de milhares destes agentes a trabalhar em escala, a gerir o negócio em dezembro.

[00:29:11–00:29:18] **Speaker não identificado:** Mas depois o Opus 4.5 saiu e percebi que este não é mais o paradigma certo.

[00:29:19–00:29:30] **Speaker não identificado:** Como a inteligência agora não precisa como o gráfico e a grelha multi-agente trabalho e uso porque vai restringir este nível de inteligência.

[00:29:30–00:29:54] **Speaker não identificado:** Então decidimos destruir tudo o que tivemos construído durante dois anos que funcionou, que nos trouxe à rentabilidade, que nos trouxe um crescimento incrível e começarmos de novo com um arame que pensávamos ser robusto e escalável e aproveitar a auto-melhoria recorrente ou novos modelos, modelos mais inteligentes que saem a cada mês.

[00:29:54–00:30:08] **Speaker não identificado:** Assim, a forma como isto parece ser uma máquina virtual com um agente, com acesso à memória e avaliações e o CLI onde eles podem acessar todas as ferramentas e todas as API na minha empresa e o objetivo a longo prazo.

## 00:30:00–00:35:00

[00:30:09–00:30:17] **Speaker não identificado:** E apresento centenas de milhares destes todos os dias com metas a longo prazo, como maximizar o valor ao longo da vida.

[00:30:17–00:30:19] **Speaker não identificado:** A organização de auto-melhoria.

[00:30:19–00:30:19] **Speaker não identificado:** - É isso mesmo.

[00:30:19–00:30:20] **Speaker não identificado:** A organização de auto-melhoria.

[00:30:20–00:30:29] **Speaker não identificado:** E acho que as pessoas estão super obcecadas com o RSI agora, e isso vai melhorar os modelos.

[00:30:30–00:30:41] **Speaker não identificado:** Mas se olharmos desta forma, o valor econômico na humanidade nos últimos 4.000 anos foi fornecido por organizações, não por indivíduos.

[00:30:41–00:30:49] **Speaker não identificado:** Então, o que você quer auto-melhorar e envolver-se nesse ciclo é a organização que pode fornecer mais valor econômico, certo?

[00:30:49–00:31:13] **Speaker não identificado:** Esse é o ciclo em que penso que as empresas vão começar a concentrar-se, porque se conseguirmos que esse ciclo funcione e é uma organização que realmente se auto-melhora e aproveita os modelos mais recentes e a melhor inteligência que estamos a obter a cada dois dias, então atingimos o exponencial, não apenas na inteligência, mas no valor que podemos gerar como empresa.

[00:31:13–00:31:15] **Speaker não identificado:** Isso é muito emocionante.

[00:31:15–00:31:28] **Speaker não identificado:** Você mencionou que, por causa de todos os desafios na adoção da IA, viu a maior oportunidade na formação de novas empresas a trabalhar nesta nova maneira e, em seguida, perturbar os mercados.

[00:31:28–00:31:29] **Speaker não identificado:** Queres falar um pouco sobre isso?

[00:31:29–00:31:30] **Speaker não identificado:** - Sim, sim, sim.

[00:31:30–00:31:37] **Speaker não identificado:** Há um conceito na economia sobre destruição criativa de Joseph Schumpeter.

[00:31:38–00:31:56] **Speaker não identificado:** E o que diz é que a forma como a inovação atinge a economia não é através das empresas adotando a nova tecnologia, mas através das empresas mantendo-se como eram e os incumbentes com a nova tecnologia destruindo as velhas empresas.

[00:31:56–00:32:08] **Speaker não identificado:** Isto destrói valor a curto prazo na economia, mas a longo prazo, é melhor para todos porque estas novas empresas mais eficientes e eficazes fornecerão melhores produtos e serviços para a economia como um todo.

[00:32:08–00:32:13] **Speaker não identificado:** E isto aconteceu nas revoluções industriais passadas, e sempre aconteceu.

[00:32:13–00:32:23] **Speaker não identificado:** E é uma ótima oportunidade para os empreendedores e as pessoas de hoje porque é difícil adotar a IA profundamente.

[00:32:24–00:32:32] **Speaker não identificado:** É muito difícil para um CEO hoje em dia, especialmente de uma grande empresa ou empresa pública, ir e dizer, como se estivesse a apostar tudo na IA.

[00:32:32–00:32:44] **Speaker não identificado:** A empresa tem que olhar assim, vou destruir e reconstruir tudo o que tenho construído nos últimos 40 anos para se tornar uma empresa nativa de IA.

[00:32:45–00:32:48] **Speaker não identificado:** Quantos CEOs farão isso numa empresa em escala?

[00:32:48–00:33:03] **Speaker não identificado:** Assim, enquanto adotam, novas empresas podem ser formadas que são construídas em torno dos pontos fortes da IA e assumem e trazem novos produtos e serviços para as massas.

[00:33:04–00:33:06] **Speaker não identificado:** E isto já aconteceu antes.

[00:33:06–00:33:07] **Speaker não identificado:** Como se isto tivesse acontecido com a eletricidade.

[00:33:07–00:33:09] **Speaker não identificado:** Esta é uma história que sempre conto à minha equipa.

[00:33:10–00:33:18] **Speaker não identificado:** As tecnologias para a linha de produção da Ford foram desenvolvidas em 1879 e 1881.

[00:33:19–00:33:27] **Speaker não identificado:** Edison começou a comercializar eletricidade em Nova York e depois em Londres, e inventou um dinamo extremamente eficiente.

[00:33:27–00:33:34] **Speaker não identificado:** Podia ter construído a fábrica da Ford 40 anos antes da Ford.

[00:33:35–00:33:35] **Speaker não identificado:** A tecnologia estava lá.

[00:33:35–00:33:36] **Speaker não identificado:** Estava tudo lá.

[00:33:36–00:33:49] **Speaker não identificado:** Mas a forma como as pessoas adotaram a eletricidade e a dinâmica da Ford foi, ok, vou deixar a minha fábrica como quatro andares, poços e cintos, e apenas trocar o meu motor de carvão por um motor elétrico.

[00:33:49–00:33:52] **Speaker não identificado:** E isso lhe trará benefícios, sim, mas como uma eficiência de 6%.

[00:33:53–00:34:10] **Speaker não identificado:** O que precisava ser feito era destruir aquela fábrica, construí-la numa superfície plana, não no centro de Nova York, mas em Connecticut ou New Jersey, e redesenhar toda a sua fábrica em torno de pequenos dinamos e eletricidade.

[00:34:10–00:34:20] **Speaker não identificado:** E depois temos como a melhoria 3x na produtividade que alimentou os EUA durante o século 20.

[00:34:20–00:34:23] **Speaker não identificado:** E o mesmo aconteceu novamente com o computador, e o mesmo está acontecendo novamente hoje.

[00:34:23–00:34:29] **Speaker não identificado:** As pessoas querem adotá-lo, mas não estão dispostas a redesenhar toda a empresa, e adotam-no superficialmente.

[00:34:29–00:34:37] **Speaker não identificado:** E no final, isso lhe dará uma melhoria de 6% ou 10%, não uma melhoria de 10x.

[00:34:37–00:34:43] **Speaker não identificado:** E é como o dilema do inovador em escala industrial novamente.

[00:34:45–00:34:50] **Speaker não identificado:** Acho que acabaste de fazer um caso incrível para os futuros fundadores que é hora de construir.

[00:34:50–00:34:51] **Speaker não identificado:** É hora de construir.

[00:34:51–00:34:56] **Speaker não identificado:** E talvez um ótimo lugar para acabar seja, sabes, teres construído e expandido a tua própria empresa.

[00:34:56–00:34:58] **Speaker não identificado:** Agora tornaste o Kavak totalmente agente.

[00:34:59–00:35:03] **Speaker não identificado:** Como, que conselhos tens para futuros fundadores ou fundadores pela primeira vez que podem estar a ouvir?

## 00:35:00–00:40:00

[00:35:04–00:35:07] **Speaker não identificado:** Portanto, este é o momento mais emocionante da história humana.

[00:35:07–00:35:08] **Speaker não identificado:** Eu acredito nisso.

[00:35:08–00:35:11] **Speaker não identificado:** Estamos a viver no momento mais emocionante da história humana.

[00:35:11–00:35:29] **Speaker não identificado:** E é o momento mais emocionante para ser um fundador porque é a primeira vez que alguém tem acesso às ferramentas e inteligência mais poderosas do mundo, quase de graça ou por 20 dólares por mês.

[00:35:29–00:35:38] **Speaker não identificado:** Literalmente, a democratização das ferramentas para as pessoas construir nunca foi assim na história humana.

[00:35:38–00:35:45] **Speaker não identificado:** E há tantos problemas a serem resolvidos e uma nova realidade a ser construída em torno deste novo paradigma.

[00:35:46–00:35:49] **Speaker não identificado:** Então, digamos, apenas vá para lá, mas vá para lá profundamente.

[00:35:50–00:35:53] **Speaker não identificado:** Imagine como será o futuro da IA.

[00:35:54–00:35:57] **Speaker não identificado:** Nem sequer é um exponencial.

[00:35:57–00:36:04] **Speaker não identificado:** Basta mapear uma tendência que é linear se as coisas continuarem a melhorar, como, a IA continua a melhorar em escala linear.

[00:36:04–00:36:11] **Speaker não identificado:** E apenas construir para isso, e você vai vir com ideias maravilhosas que, como, trazer um monte de valor para o mundo.

[00:36:13–00:36:13] **Speaker não identificado:** É incrível.

[00:36:14–00:36:15] **Speaker não identificado:** Ale, obrigado por se juntar a nós.

[00:36:15–00:36:15] **Speaker não identificado:** - Não, obrigado.

[00:36:15–00:36:16] **Speaker não identificado:** Obrigado por me teres convidado.
