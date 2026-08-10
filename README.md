# Metodologia de IA nas Ciências Humanas

Materiais da apresentação **“Quando a IA faz a análise, quem responde pelo método?”**, preparada para um workshop sobre uso de inteligência artificial em pesquisa nas Ciências Humanas.

**Autor:** Manoel Galdino  
**Data da apresentação:** 7 de agosto de 2026  
**Duração prevista:** 15 minutos  
**Público principal:** pós-graduandos em Ciências Humanas, especialmente da FFLCH/USP

## Ideia central

A inteligência artificial é uma nova camada de abstração. Ela pode ampliar a capacidade do pesquisador de explicar, calcular, cruzar dados, produzir gráficos e explorar alternativas. O ganho é real, mas toda abstração também pode esconder decisões relevantes.

O princípio orientador do projeto é:

> **Delegue a implementação, não a autoria da cadeia inferencial.**

Aqui, **dívida epistêmica** designa o acúmulo de decisões substantivas que permanecem incorporadas ao artefato, mas deixam de ser compreendidas, justificadas e assumidas pelo pesquisador. O termo circula na engenharia de software e na manufatura (Cunningham 1992; Sculley et al. 2015; Ionescu et al. 2019); o que este projeto acrescenta é sua aplicação à cadeia inferencial da pesquisa empírica em ciências sociais.

A dívida técnica cobra do produto. A dívida epistêmica cobra da capacidade do pesquisador de defender a decisão — e a garantia, no limite, é a reputação científica.

Uma decisão exige deliberação explícita quando uma alternativa razoável puder mudar:

- o objeto medido;
- a população ou o denominador;
- a operacionalização de uma variável;
- o estimando ou o modelo;
- as hipóteses relevantes;
- o contraste estimado; ou
- a interpretação e a força da conclusão.

O critério não é evitar a IA. É preservar a autodireção intelectual e a capacidade de defender as decisões que dão significado à análise.

## Defesa metodológica sem cola

O protocolo recomendado para etapas críticas de um projeto é:

1. pedir à IA um Q&A adversarial sobre a análise;
2. não pedir imediatamente as respostas para as perguntas que o pesquisador não sabe responder;
3. transformar cada pergunta sem resposta em uma pendência de investigação;
4. reconstruir a proveniência e comparar alternativas razoáveis;
5. deliberar, registrar e assumir a decisão, mesmo que ela coincida com a sugestão inicial da IA;
6. manter a conclusão provisória enquanto decisões críticas ainda não tiverem sido investigadas e assumidas.

O fluxo resumido é:

```text
IA implementa → IA questiona → pesquisador investiga → pesquisador decide
```

Reprodução computacional, logs e reimplementação independente são salvaguardas importantes, mas respondem a perguntas diferentes. Reproduzir o que foi executado não garante que o construto foi bem medido nem que o pesquisador consegue defender por que aquela decisão é sua.

## Caso central

O caso da apresentação é uma análise de pontos ideais e a escolha de âncoras. A sequência importa:

- **Fevereiro.** A IA escreveu o código de estimação. Cada escolha foi interrogada enquanto era feita, e o procedimento foi compreendido na ocasião.
- **Agosto.** A IA escreveu a apresentação e interpretou os resultados. O texto afirmava mais do que o desenho autorizava.
- **Então.** A desconfiança levou à checagem — e, no mesmo movimento, à descoberta de que a razão da escolha das âncoras já não era reconstruível.

O episódio expôs **duas dívidas de origens diferentes**:

1. **a que a delegação criou:** uma interpretação que afirmava além do que o desenho sustenta, entregue pronta e bem escrita;
2. **a que o tempo criou:** a perda de proveniência da escolha das âncoras, tão antiga quanto a pesquisa e independente do uso de IA.

O que as une é a mesma condição: o resultado existia, e a defesa não. A mesma pergunta adversarial expôs as duas, levando à reconstrução do procedimento, à exploração de âncoras alternativas e à apresentação dos resultados como provisórios.

Essa dívida é difícil de detectar por três razões: ela vive na camada da inferência, onde a reprodução do código não chega; o erro chega bem escrito, suprimindo o atrito que dispararia a desconfiança; e a confiança legitimamente ganha ao verificar a estimação reduz o escrutínio da interpretação, porque ambas vêm no mesmo artefato. O movimento é análogo ao de Sculley et al. (2015) — a dívida de sistemas de ML é difícil de detectar porque existe no nível do sistema, e os remédios de nível de código não a alcançam — com a diferença de que aqui o mecanismo é cognitivo, não técnico.

## Materiais do projeto

| Material | Função |
|---|---|
| [`2026-08-07_apresentacao_metodologia_ia.pdf`](2026-08-07_apresentacao_metodologia_ia.pdf) | Apresentação final em PDF |
| [`2026-08-07_apresentacao_metodologia_ia.Rmd`](2026-08-07_apresentacao_metodologia_ia.Rmd) | Fonte editável e reproduzível dos slides |
| [`2026-08-07_apresentacao_metodologia_ia.tex`](2026-08-07_apresentacao_metodologia_ia.tex) | Fonte LaTeX preservada pela compilação |
| [`2026-08-07_apresentacao_metodologia_ia.knit.md`](2026-08-07_apresentacao_metodologia_ia.knit.md) | Markdown intermediário gerado pelo R Markdown |
| [`2026-08-07_sintese_entrevista_workshop_metodologia_ia.md`](2026-08-07_sintese_entrevista_workshop_metodologia_ia.md) | Síntese do argumento, do público e do escopo |
| [`2026-08-07_entrevista_integral_workshop_metodologia_ia.md`](2026-08-07_entrevista_integral_workshop_metodologia_ia.md) | Transcrição integral da entrevista de preparação |
| [`2026-08-07_revisao_literatura_entrevista_metodologia_ia.md`](2026-08-07_revisao_literatura_entrevista_metodologia_ia.md) | Revisão exploratória e referências de apoio |
| [`tmp/pdfs/2026-08-07_apresentacao/`](tmp/pdfs/2026-08-07_apresentacao/) | PNGs renderizados dos slides para inspeção visual |

## Reprodução

A apresentação foi escrita em R Markdown e compilada como Beamer, usando XeLaTeX. A partir da raiz do projeto, com R, `rmarkdown` e uma instalação TeX disponível:

```bash
Rscript -e 'rmarkdown::render("2026-08-07_apresentacao_metodologia_ia.Rmd", clean = FALSE)'
```

O argumento `clean = FALSE` preserva os artefatos intermediários, incluindo o `.tex`. Para uma inspeção textual simples do PDF:

```bash
pdftotext -layout 2026-08-07_apresentacao_metodologia_ia.pdf /tmp/apresentacao_metodologia_ia.txt
```

Os PNGs em `tmp/pdfs/` são artefatos de inspeção visual da versão renderizada. Eles não substituem o PDF nem o arquivo-fonte `.Rmd`.

## Escopo e limites

- A apresentação é uma intervenção conceitual curta, não um catálogo de métodos estatísticos.
- “Dívida epistêmica” é um termo já em uso na engenharia de software e na manufatura. A contribuição deste projeto é a aplicação à cadeia inferencial da pesquisa empírica, não a cunhagem do termo. As referências que sustentam essa atribuição devem ser lidas antes da apresentação final.
- O caso ilustra o mecanismo na camada da interpretação. A alegação de que a IA completa silenciosamente decisões de mensuração e de população é um risco plausível, não um episódio documentado neste projeto.
- A revisão de literatura incluída no projeto é exploratória, não sistemática nem exaustiva.
- O caso das âncoras é um exemplo metodológico e autobiográfico; o repositório não pretende reproduzir a análise de pontos ideais.
- A defesa metodológica sem cola é uma recomendação prática derivada do argumento e de literatura sobre descarregamento cognitivo, automação, autonomia intelectual, validade e pesquisa assistida por IA. Sua eficácia como protocolo de formação ainda requer avaliação.

## Referências de entrada

As referências completas estão em [`2026-08-07_revisao_literatura_entrevista_metodologia_ia.md`](2026-08-07_revisao_literatura_entrevista_metodologia_ia.md). Entre as referências diretamente mobilizadas na apresentação estão Risko e Gilbert (2016), Carter (2020), Buçinca, Malaya e Gajos (2021), Messeri e Crockett (2024), Morucci et al. (2025) e Abdurahman et al. (2025).

