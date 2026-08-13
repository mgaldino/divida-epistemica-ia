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
\end{center}

<!-- Fala: Conte o episódio sem começar pela tecnologia. O gancho é a vulnerabilidade do pesquisador: algo estava no paper, mas já não estava disponível para defesa. -->

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
\vspace{0.35cm}
\Large A especificação pede “estime a dimensão”.

\vspace{0.4cm}
\large A IA precisa preencher lacunas - e preenche bem:

\vspace{0.35cm}
\begin{tabular}{c@{\quad}c@{\quad}c}
  \textbf{o que medir} & \textbf{quem conta} & {\color{orange}\textbf{o que concluir}} \\
  \small objeto & \small população/denominador & {\color{orange}\small interpretação e força do claim}
\end{tabular}

\vspace{0.55cm}
\textbf{O código pode estar correto e a afirmação não se sustentar.}

\vspace{0.3cm}
\normalsize Os juros vencem quando alguém pergunta “por quê?”.
\end{center}

\sourcecite{A “fronteira” da IA é irregular: a assistência melhora algumas tarefas e piora outras, e o usuário nem sempre sabe previamente quais são quais. Dell’Acqua et al. (2026), DOI 10.1287/orsc.2025.21838.}

<!-- Fala: A terceira coluna é a do meu caso. As duas primeiras são riscos reais, mas o que aconteceu comigo foi na camada da interpretação. -->

## Por que essa dívida é difícil de detectar

\begin{columns}[T,onlytextwidth]
\column{0.31\textwidth}
\centering
{\color{orange}\Large\textbf{Camada}}

\vspace{0.2cm}
\normalsize O passivo vive na inferência. Reproduzir o código não chega lá.

\column{0.31\textwidth}
\centering
{\color{orange}\Large\textbf{Fluência}}

\vspace{0.2cm}
\normalsize O erro vem bem escrito. O atrito que dispararia a desconfiança desaparece.

\column{0.31\textwidth}
\centering
{\color{orange}\Large\textbf{Efeito Halo}}

\vspace{0.2cm}
\normalsize Verifiquei o código que gerou o número. Por isso não reli com o mesmo rigor o que foi dito sobre o número.
\end{columns}

\vspace{0.45cm}
\begin{center}
\normalsize Risco para a autoria: um output de qualidade não garante que a compreensão que o sustenta continue disponível.

\vspace{0.25cm}
\large A garantia dessa dívida é a sua reputação.
\end{center}

\sourcecite{Movimento análogo ao de Sculley et al. (2015): a dívida de sistemas de ML é difícil de detectar porque existe no nível do sistema, e os remédios de nível de código não a alcançam - aqui o mecanismo é cognitivo, não técnico. Sobre o efeito halo e a inconsciência de sua influência sobre o julgamento: Thorndike (1920), DOI 10.1037/h0071663; Nisbett e Wilson (1977), DOI 10.1037/0022-3514.35.4.250.}

<!-- Fala: Este slide explica por que reprodução não basta - e por que o protocolo do final tem o formato que tem. Se houver tempo, cite a crise de replicação na psicologia: gente sem ilícito legal, reprecificada a zero quando o campo alcançou. -->

## Dívida epistêmica

\begin{center}
\vspace{0.5cm}
{\color{orange}\Huge\textbf{Dívida epistêmica}}

\vspace{0.45cm}
\Large decisões \textit{substantivas} - que mudam objeto, medida ou inferência -

\vspace{0.15cm}
\Large incorporadas ao artefato e não mais assumidas pelo autor.

\vspace{0.6cm}
\normalsize A dívida técnica cobra do produto. Esta cobra da sua capacidade de defender a decisão.
\end{center}

\sourcecite{O termo circula na engenharia de software e na manufatura (Cunningham 1992; Sculley et al. 2015; Ionescu et al. 2019, DOI 10.1007/978-3-030-20040-4\_8). Aplico-o aqui à cadeia inferencial da pesquisa empírica em ciências sociais.}

<!-- Fala: Credite o termo. Dizer que ele já existe demonstra domínio da literatura e não custa nada - o que é seu é a aplicação à cadeia inferencial. Verificar as três referências antes de apresentar. -->

## O caso: o que aconteceu comigo

\begin{center}
\vspace{0.35cm}
\large
\begin{tabular}{r@{\quad}l}
{\color{teal}\textbf{Fevereiro}} & A IA escreve o código de estimação. \\
 & \small Eu interroguei cada escolha. Eu entendi o que estava sendo feito. \\[0.4cm]
{\color{orange}\textbf{Agosto}} & A IA escreve a apresentação - e \textbf{interpreta} os resultados. \\
 & \small O texto afirmava mais do que o desenho autorizava. \\[0.4cm]
{\color{orange}\textbf{Então}} & Eu desconfiei e fui checar. \\
 & \small E descobri que também não sabia mais por que escolhi aquelas âncoras.
\end{tabular}
\end{center}

\sourcecite{A literatura de pontos ideais trata identificação e interpretação como problemas distintos: Poole e Rosenthal (1985); Clinton, Jackman e Rivers (2004); Morucci et al. (2025), DOI 10.1017/S000305542400039X.}

<!-- Fala: Clímax. Se a plateia for pouco quantitativa, abra com uma linha: “pontos ideais estimam posições a partir de votações; as âncoras fixam o significado da dimensão”. Delimitar você mesmo o papel da IA desarma a objeção de que isso é só esquecimento comum. -->

## Duas dívidas, origens diferentes

\begin{columns}[T,onlytextwidth]
\column{0.46\textwidth}
{\color{orange}\Large\textbf{A IA criou}}

\vspace{0.25cm}
\normalsize A interpretação afirmava além do que o desenho sustenta.

\vspace{0.2cm}
\small Nasce da delegação. Chega pronta e bem escrita.

\column{0.46\textwidth}
{\color{teal}\Large\textbf{O tempo criou}}

\vspace{0.25cm}
\normalsize Eu não reconstruía mais por que aquelas âncoras.

\vspace{0.2cm}
\small Nasce do esquecimento. É tão antiga quanto a pesquisa.
\end{columns}

\vspace{0.6cm}
\begin{center}
\large O que as une: \textbf{o resultado existia e a defesa não.}

\vspace{0.2cm}
\normalsize A mesma pergunta adversarial expôs as duas.
\end{center}

\sourcecite{Um ajuste latente não garante significado substantivo: Morucci et al. (2025); Adcock e Collier (2001), DOI 10.1017/S0003055401003100.}

<!-- Fala: Conceder que metade do problema é pré-IA torna a outra metade mais crível. E generaliza a recomendação: quem não usa IA também tem a dívida do tempo. -->

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
\large Nenhuma dessas salvaguardas visita a camada onde a minha dívida estava.
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
\item Peça um Q\&A adversarial - em sessão separada da análise.
\item Não peça imediatamente as respostas.
\item Transforme cada pergunta sem resposta em pendência.
\item Reconstrua a proveniência e compare alternativas.
\item Delibere, registre e assuma a decisão.
\end{enumerate}
\end{center}

\sourcecite{A lógica é próxima das intervenções de “forçamento cognitivo”, que reduziram sobredelegação em decisões assistidas por IA: Buçinca, Malaya e Gajos (2021), DOI 10.1145/3449287. A separação entre sessões é uma escolha de desenho deste protocolo.}

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

## Fechamento

\begin{center}
\vspace{0.3cm}
{\color{teal}\Huge\textbf{Seu paper não precisa ser feito sem IA.}}

\vspace{0.3cm}
{\color{orange}\Huge\textbf{Precisa continuar sendo defendível por você.}}

\end{center}

<!-- Fala: Termine voltando à confissão inicial. O beat do meio é a fala comendo a própria ração: o risco que estou denunciando quase passou por estes slides. -->

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
