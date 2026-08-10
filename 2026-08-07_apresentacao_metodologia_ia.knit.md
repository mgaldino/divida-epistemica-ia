---
title: "Quando a IA faz a análise, quem responde pelo método?"
subtitle: "Abstração, dívida epistêmica e defesa metodológica sem cola"
author: "Manoel Galdino"
date: "7 de agosto de 2026"
output:
  beamer_presentation:
    latex_engine: xelatex
    keep_tex: true
classoption: "aspectratio=169"
fontsize: 12pt
header-includes:
  - |
    \usepackage{lmodern}
    \definecolor{ink}{HTML}{1F2933}
    \definecolor{teal}{HTML}{0F766E}
    \definecolor{orange}{HTML}{D95D39}
    \definecolor{muted}{HTML}{667085}
    \setbeamercolor{normal text}{fg=ink,bg=white}
    \setbeamercolor{structure}{fg=teal}
    \setbeamercolor{frametitle}{fg=ink,bg=white}
    \setbeamercolor{title}{fg=ink}
    \setbeamercolor{subtitle}{fg=muted}
    \setbeamercolor{alerted text}{fg=orange}
    \setbeamercolor{block title}{fg=white,bg=teal}
    \setbeamercolor{block body}{fg=ink,bg=teal!6}
    \setbeamerfont{title}{series=\bfseries,size=\LARGE}
    \setbeamerfont{frametitle}{series=\bfseries,size=\Large}
    \setbeamertemplate{navigation symbols}{}
    \setbeamertemplate{headline}{}
    \setbeamertemplate{frametitle continuation}{}
    \setbeamertemplate{footline}{\hfill\scriptsize\color{muted}\insertframenumber\, / \,\inserttotalframenumber\hspace{0.35cm}\vspace{0.18cm}}
    \newcommand{\sourcecite}[1]{\vfill{\tiny\color{muted}#1}}
---

 
## A pergunta que eu não consegui responder

\begin{center}
\vspace{0.6cm}
{\color{orange}\Huge\textbf{Eu descobri que não sabia defender uma decisão do meu próprio paper.}}

\vspace{0.8cm}
\large Não era um erro de código. Era uma perda de autoria metodológica.
\end{center}

<!-- Fala: Conte o episódio sem começar pela tecnologia. O gancho é a vulnerabilidade do pesquisador: algo estava no paper, mas já não estava disponível para defesa. -->

## Antes de falar de IA, pense no seu método

\begin{center}
\vspace{0.6cm}
\Large\textbf{Qual foi a última decisão metodológica que você conseguiria reconstruir hoje - sem abrir o código?}

\vspace{0.9cm}
\normalsize O que você teria de explicar?

\vspace{0.25cm}
\begin{tabular}{c@{\qquad}c@{\qquad}c}
  objeto & medida & interpretação \\
  \color{teal}\rule{2.2cm}{1.2pt} & \color{teal}\rule{2.2cm}{1.2pt} & \color{teal}\rule{2.2cm}{1.2pt}
\end{tabular}
\end{center}

<!-- Fala: Faça uma pausa. A pergunta prepara a audiência para entender que o objeto do teste será o pesquisador, não apenas o produto computacional. -->

## A IA é uma nova camada de abstração

\begin{center}
\vspace{0.2cm}
\large
\texttt{linguagem de máquina}

\vspace{0.05cm}
{\color{teal}\large\downarrow}

\vspace{0.05cm}
\texttt{linguagem de programação}

\vspace{0.05cm}
{\color{teal}\large\downarrow}

\vspace{0.05cm}
\texttt{linguagem natural}

\vspace{0.05cm}
{\color{orange}\large\downarrow}

\vspace{0.05cm}
\textbf{delegação de trabalho intelectual}
\end{center}

\sourcecite{A ideia dialoga com cognição distribuída e descarregamento cognitivo: Risko e Gilbert (2016), DOI 10.1016/j.tics.2016.07.002.}

<!-- Fala: A abstração é boa: permite trabalhar em um nível mais alto. A pergunta não é se devemos abstrair, mas o que pode desaparecer quando subimos de nível. -->

## O ganho é real - e é por isso que o risco importa

\begin{columns}[T,onlytextwidth]
\column{0.48\textwidth}
\Large\textbf{A IA pode}

\vspace{0.25cm}
\begin{itemize}
\item explicar;
\item calcular;
\item cruzar dados;
\item gerar gráficos;
\item explorar alternativas.
\end{itemize}

\column{0.48\textwidth}
\Large\textbf{O pesquisador precisa}

\vspace{0.25cm}
\begin{itemize}
\item definir o objeto;
\item escolher a medida;
\item assumir as hipóteses;
\item interpretar o contraste;
\item defender a conclusão.
\end{itemize}
\end{columns}

\sourcecite{A dependência de ferramentas não é automaticamente perda de autonomia; o critério é preservar a autodireção intelectual. Carter (2020), DOI 10.1007/s11229-017-1549-y.}

<!-- Fala: Não é uma fala anti-IA. A delegação de implementação é justamente a parte produtiva. O limite aparece quando a ferramenta passa a completar decisões que mudam o significado da análise. -->

## Onde a abstração começa a cobrar juros

\begin{center}
\vspace{0.45cm}
\Large A especificação pede “estime a dimensão”.

\vspace{0.45cm}
\large A IA pode completar silenciosamente:

\vspace{0.35cm}
\begin{tabular}{c@{\quad}c@{\quad}c}
  \color{orange}\textbf{o que medir} & \color{orange}\textbf{quem conta} & \color{orange}\textbf{o que concluir} \\
  objeto & população/denominador & estimando/interpretação
\end{tabular}

\vspace{0.6cm}
\textbf{O código pode estar correto. A pergunta pode ter mudado.}
\end{center}

\sourcecite{A “fronteira” da IA é irregular: a assistência melhora algumas tarefas e piora outras, e o usuário nem sempre sabe previamente quais são quais. Dell’Acqua et al. (2026), DOI 10.1287/orsc.2025.21838.}

<!-- Fala: Dê um exemplo simples: trocar o denominador, uma variável ou uma âncora pode mudar a pergunta sem produzir nenhum erro de execução. -->

## Minha proposta: dívida epistêmica

\begin{center}
\vspace{0.6cm}
{\color{orange}\Huge\textbf{Dívida epistêmica}}

\vspace{0.45cm}
\Large decisões substantivas que ficaram incorporadas ao artefato,

\vspace{0.15cm}
\Large mas deixaram de estar compreendidas e assumidas pelo autor.

\vspace{0.65cm}
\normalsize\textit{Formulação autoral, apoiada em literaturas adjacentes.}
\end{center}

<!-- Fala: Diga explicitamente que você não está alegando que o termo já possui um campo consolidado. O valor da expressão é juntar riscos que a literatura costuma estudar separadamente. -->

## O caso: pontos ideais e as âncoras

\begin{center}
\vspace{0.25cm}
\large\textbf{“As âncoras foram definidas teoricamente antes dos resultados - ou porque produziam uma dimensão conveniente?”}

\vspace{0.7cm}
\begin{tabular}{c@{\qquad}c@{\qquad}c}
  \color{orange}\textbf{proveniência} & \color{orange}\textbf{mensuração} & \color{orange}\textbf{defesa} \\
  Por que escolhi? & O que a dimensão mede? & Consigo explicar?
\end{tabular}
\end{center}

\sourcecite{A literatura de pontos ideais trata identificação e interpretação como problemas distintos: Poole e Rosenthal (1985); Clinton, Jackman e Rivers (2004); Morucci et al. (2025), DOI 10.1017/S000305542400039X.}

<!-- Fala: Aqui está o clímax. A pergunta da IA não entregou uma resposta; ela revelou uma lacuna na memória e na validade do construto. -->

## O que exatamente foi perdido?

\begin{columns}[T,onlytextwidth]
\column{0.31\textwidth}
\centering
{\color{orange}\Huge 1}

\vspace{0.12cm}
\Large\textbf{Proveniência}

\vspace{0.18cm}
\normalsize Não reconstruía a razão da escolha.

\column{0.31\textwidth}
\centering
{\color{orange}\Huge 2}

\vspace{0.12cm}
\Large\textbf{Construto}

\vspace{0.18cm}
\normalsize Não estava claro o que a dimensão representava.

\column{0.31\textwidth}
\centering
{\color{orange}\Huge 3}

\vspace{0.12cm}
\Large\textbf{Autoria}

\vspace{0.18cm}
\normalsize O resultado existia; a defesa não.
\end{columns}

\sourcecite{Um ajuste latente não garante significado substantivo: Morucci et al. (2025); Adcock e Collier (2001), DOI 10.1017/S0003055401003100.}

<!-- Fala: Faça a distinção entre “não lembrar um detalhe de implementação” e “não conseguir justificar uma decisão que muda o construto”. -->

## Reprodução ajuda - mas não resolve tudo

\begin{center}
\vspace{0.35cm}
\Large
\textbf{Código e logs} \quad $\neq$ \quad \textbf{validade} \quad $\neq$ \quad \textbf{autoria}

\vspace{0.65cm}
\begin{columns}[T,onlytextwidth]
\column{0.31\textwidth}
\centering\textbf{Reproduzir}

\vspace{0.18cm}
\normalsize o que foi executado

\column{0.31\textwidth}
\centering\textbf{Validar}

\vspace{0.18cm}
\normalsize o que foi medido

\column{0.31\textwidth}
\centering\textbf{Defender}

\vspace{0.18cm}
\normalsize por que essa escolha é minha
\end{columns}

\vspace{0.55cm}
\large Salvaguardas são necessárias. Elas não substituem deliberação.
\end{center}

\sourcecite{Diretrizes recentes recomendam registrar ferramenta, versão, datas, prompts e procedimentos para permitir reprodução: Flanagin et al. (2024), DOI 10.1001/jama.2024.3471; Abdurahman et al. (2025), DOI 10.1177/25152459251325174.}

<!-- Fala: Esta é uma das mensagens que precisa ficar na memória: a auditoria mecânica responde a uma pergunta diferente da validação do construto. -->

## A defesa metodológica sem cola

\begin{center}
\vspace{0.2cm}
\large
\textbf{IA implementa} $\rightarrow$ \textbf{IA questiona} $\rightarrow$ \textbf{pesquisador investiga} $\rightarrow$ \textbf{pesquisador decide}

\vspace{0.35cm}
\small
\begin{enumerate}
\setlength{\itemsep}{2pt}
\item Peça um Q\&A adversarial.
\item Não peça imediatamente as respostas.
\item Transforme cada pergunta sem resposta em pendência.
\item Reconstrua a proveniência e compare alternativas.
\item Delibere, registre e assuma a decisão.
\end{enumerate}
\end{center}

\sourcecite{A lógica é próxima das intervenções de “forçamento cognitivo”, que reduziram sobredelegação em decisões assistidas por IA: Buçinca, Malaya e Gajos (2021), DOI 10.1145/3449287.}

<!-- Fala: A diferença não é pedir menos à IA. É pedir que ela atue também como audiência crítica, sem usurpar o momento de decisão. -->

## O meu limiar provisório

\begin{center}
\vspace{0.5cm}
{\color{teal}\Huge\textbf{Delegue a implementação,}}

\vspace{0.2cm}
{\color{orange}\Huge\textbf{não a autoria da cadeia inferencial.}}

\vspace{0.75cm}
\large Pause e delibere quando uma alternativa razoável puder mudar:

\vspace{0.2cm}
\normalsize objeto \quad | \quad denominador \quad | \quad operacionalização \quad | \quad estimando \quad | \quad interpretação
\end{center}

<!-- Fala: Este é o slide para repetir lentamente. A regra não exige que o pesquisador rejeite a sugestão da IA; exige que ele a examine e a faça sua, se decidir mantê-la. -->

## O que muda na prática?

\begin{center}
\vspace{0.35cm}
\begin{columns}[T,onlytextwidth]
\column{0.46\textwidth}
\Large\textbf{Antes de aceitar}

\vspace{0.2cm}
\normalsize “A IA sugeriu.”

\vspace{0.18cm}
\normalsize “O código roda.”

\vspace{0.18cm}
\normalsize “O resultado parece plausível.”

\column{0.46\textwidth}
\Large\textbf{Depois de aceitar}

\vspace{0.2cm}
\normalsize “Eu comparei alternativas e escolhi.”

\vspace{0.18cm}
\normalsize “O objeto e o estimando estão claros.”

\vspace{0.18cm}
\normalsize “Consigo responder à crítica.”
\end{columns}
\end{center}

\sourcecite{A literatura recente descreve riscos de ilusão de entendimento, opacidade de proveniência e confiança mal calibrada em pesquisa assistida por IA: Messeri e Crockett (2024); Gautam et al. (2026).}

<!-- Fala: Mostre que “assumir a decisão” não é uma performance de certeza. Uma decisão pode continuar provisória; o ponto é saber por que ela está provisória e o que falta investigar. -->

## Fechamento

\begin{center}
\vspace{0.75cm}
{\color{teal}\Huge\textbf{Seu paper não precisa ser feito sem IA.}}

\vspace{0.35cm}
{\color{orange}\Huge\textbf{Precisa continuar sendo defendível por você.}}

\vspace{0.8cm}
\large A pergunta final não é “a IA fez?”.

\vspace{0.15cm}
\large É: \textbf{“qual decisão eu assumi - e por quê?”}
\end{center}

<!-- Fala: Termine voltando à confissão inicial. Agora o problema não é ter usado IA; é ter deixado uma decisão crítica sem autor disponível para explicá-la. -->

## Para aprofundar

\small

\begin{itemize}
\item Risko e Gilbert (2016). “Cognitive Offloading.” \textit{Trends in Cognitive Sciences}. DOI: 10.1016/j.tics.2016.07.002.
\item Carter (2020). “Intellectual Autonomy, Epistemic Dependence and Cognitive Enhancement.” \textit{Synthese}. DOI: 10.1007/s11229-017-1549-y.
\item Messeri e Crockett (2024). “Artificial Intelligence and Illusions of Understanding in Scientific Research.” \textit{Nature}. DOI: 10.1038/s41586-024-07146-0.
\item Morucci et al. (2025). “Measurement That Matches Theory.” \textit{APSR}. DOI: 10.1017/S000305542400039X.
\item Abdurahman et al. (2025). “A Primer for Evaluating LLMs in Social-Science Research.” DOI: 10.1177/25152459251325174.
\end{itemize}

\vfill
\centering
\textcolor{muted}{A revisão exploratória completa e as referências estão no arquivo de apoio do projeto.}
