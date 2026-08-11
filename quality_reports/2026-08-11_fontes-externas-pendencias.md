# Fontes externas lidas em 11 ago 2026 — o que entrou, o que ficou pendente

**Fontes:**
1. Kahn, M. E. (2026). *Will AI Improve Undergraduate Economics Education?* Working paper, USC, 11 ago 2026. 14.486 palavras. PDF baixado do Drive nesta sessão.
2. the9x.ai — *Agentic AI for Researchers Workshop* (The 9x Academic / Coded Thinking). Página comercial de curso, não fonte acadêmica.

---

## 1. O que entrou na v2.1

### Slide 12 — sessão separada para o Q&A adversarial

O item 1 do protocolo passou a ser: *"Peça um Q&A adversarial - em sessão separada da análise."*

**Origem:** the9x.ai lista, entre suas regras de verificação, *"never let the same session verify its own work"*.

**Por que importa:** o protocolo dizia "peça um Q&A adversarial" sem especificar onde. Se a mesma sessão que produziu a análise faz a arguição, ela carrega o mesmo contexto e os mesmos pontos cegos — a arguição vira teatro. Fecha um vazio operacional real.

**Atribuição:** creditada na `\sourcecite` como "regra prática corrente em workflows de agentes", sem citar o curso pelo nome. É prática de comunidade, não achado de alguém; e a fonte é página comercial, imprópria como citação acadêmica.

### Slide 7 — risco moral

Linha acrescentada abaixo das três colunas: *"Risco moral: quando o output de qualidade fica barato, ele deixa de sinalizar a compreensão que o sustenta."*

**⚠️ PENDÊNCIA OBRIGATÓRIA DE ATRIBUIÇÃO.** A formulação vem de Kahn (2026), introdução:

> *"AI creates a new form of moral hazard. When high-quality output can be generated with little effort, observable performance becomes a weaker signal of underlying understanding."*

O conceito de risco moral é padrão em economia (Arrow, Holmström) e pode ser usado sem citação. A **aplicação específica** a este fenômeno, não. A linha entrou sem citação porque o autor optou por não citar antes de ler o paper — decisão coerente com sua prática. **Se após a leitura a formulação for mantida, Kahn deve entrar na `\sourcecite` do slide 7.** Numa fala sobre autoria não-assumida, deixar isso implícito seria autocontraditório.

---

## 2. O que ficou pendente de decisão (adiado por escolha do autor)

### Corroboração externa do mecanismo — Kahn (2026), seção 14.5

Sobre cursos de capstone empírico com uso de assistentes de código:

> *"Regular check-ins revealed only weak correlation between the sophistication of the submitted paper and the student's actual comprehension of the econometric choices and economic interpretation."*

**Por que é a melhor corroboração disponível:** está no domínio exato da fala — escolhas econométricas e interpretação —, e descreve precisamente o descolamento entre qualidade do output e compreensão real que sustenta o conceito de dívida epistêmica.

**Caveat obrigatório se for usada:** relato docente, não estudo controlado. Kahn declara na introdução: *"many of my ideas are speculative and based on my own interactions with AI. I have not conducted a survey..."*

**Consequência de adiar:** a fragilidade de N=1 permanece sem endereçamento na v2.1. Aceitável — a fala apresenta o caso como ilustração autobiográfica, não como evidência.

Outra passagem útil, da seção 6 ("The Unstructured AI Experiment"):

> *"Apparent performance (grades, paper quality, exam scores) can improve even as underlying human capital accumulation declines for some students."*

---

## 3. Preparação para Q&A (não entra no deck)

### A objeção mais forte que a plateia pode fazer, agora em versão empírica

Kahn documenta **efeitos heterogêneos**: estudantes disciplinados usam IA como complemento/acelerador; os menos disciplinados, como substituto. E:

> *"AI may amplify differences in learning even when all students appear to be doing great."*

Isto é exatamente a crítica nº 4 do devil's advocate — *o protocolo pressupõe a virtude cuja escassez ele diagnostica*. Se quem sobredelega o faz porque é sem atrito, por que resistiria a pedir a resposta da pergunta difícil? A heterogeneidade de Kahn sugere que o protocolo pode ampliar a diferença entre quem já tem disciplina e quem não tem, em vez de fechá-la.

**Resposta preparada:** o passo 2 é **andaime externo**, não força de vontade — é a lógica de forçamento cognitivo (Buçinca et al. 2021), que a fala já cita. Por isso deve ser institucionalizado: pendência versionada, item de checklist do projeto, sessão separada obrigatória. Deixá-lo à disciplina individual é justamente o que não funciona. Conceder a heterogeneidade e reposicionar o protocolo como estrutura, não como virtude, é a resposta honesta.

---

## 4. O que foi descartado

- **Ben Golub / Refine Ink** (pareceres por ~US$30, Kahn §14.4). Convergência independente interessante na ideia de IA-como-parecerista, e o desenho pedagógico é bom (nota pelo modo como o aluno lida com o feedback; diário de progresso; prova oral). Mas o modelo pede **respostas** à IA, enquanto o protocolo daqui as **retém deliberadamente** — a distinção é o coração da "defesa sem cola". Explicá-la custaria tempo que 15 min não têm.
- **Seções 7–13 e 15–17 de Kahn** — desenho curricular de graduação, Hayek e predição, tributação sobre valor da terra, escada de apprenticeship. Irrelevantes para a fala.
- **the9x.ai como citação acadêmica.** Página comercial de curso. Serve como artefato de prática, nunca como fonte scholarly.
- **"Silent data decisions"**, listado pelo curso entre as falhas conhecidas de agentes. Sustenta o claim geral do slide 6 (a IA pode completar decisões de mensuração e população), mas o caso do autor não instancia isso, e a v2.0 já rebaixou essa alegação a risco plausível. Não muda nada.

---

## 5. Pendências do autor antes de apresentar

- [ ] Ler Kahn (2026) e decidir sobre a atribuição da linha de risco moral no slide 7 (**obrigatório**, ver §1).
- [ ] Decidir se a corroboração da §14.5 entra na `\sourcecite` do slide 7.
- [ ] Ler as referências já creditadas: Cunningham (1992), Sculley et al. (2015), Ionescu et al. (2019), Thorndike (1920), Nisbett e Wilson (1977) — e conferir os DOIs, escritos de memória.
- [ ] Se Kahn for citado, mover o PDF do scratchpad para o projeto.
