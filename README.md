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

Aqui, **dívida epistêmica** é uma formulação autoral e provisória para o acúmulo de decisões substantivas que permanecem incorporadas ao artefato, mas deixam de ser compreendidas, justificadas e assumidas pelo pesquisador.

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

O caso da apresentação é uma análise de pontos ideais e a escolha de âncoras. Em um Q&A simulado pela IA, surgiu a pergunta:

> “As âncoras foram definidas teoricamente antes dos resultados ou escolhidas porque produziam uma dimensão substantivamente conveniente?”

A pergunta revelou três problemas possíveis:

1. **proveniência:** não era possível reconstruir claramente por que as âncoras tinham sido escolhidas;
2. **construto:** não estava claro se a dimensão latente correspondia ao conceito teórico de interesse;
3. **autoria:** o resultado existia, mas a defesa metodológica ainda não estava disponível.

O episódio não certificou automaticamente a análise. Ele transformou uma lacuna invisível em uma pendência explícita, levando à reconstrução do procedimento, à exploração de âncoras alternativas e à apresentação dos resultados como provisórios.

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
- “Dívida epistêmica” é apresentada como uma síntese autoral de literaturas adjacentes, não como um conceito já consolidado por uma única tradição.
- A revisão de literatura incluída no projeto é exploratória, não sistemática nem exaustiva.
- O caso das âncoras é um exemplo metodológico e autobiográfico; o repositório não pretende reproduzir a análise de pontos ideais.
- A defesa metodológica sem cola é uma recomendação prática derivada do argumento e de literatura sobre descarregamento cognitivo, automação, autonomia intelectual, validade e pesquisa assistida por IA. Sua eficácia como protocolo de formação ainda requer avaliação.

## Referências de entrada

As referências completas estão em [`2026-08-07_revisao_literatura_entrevista_metodologia_ia.md`](2026-08-07_revisao_literatura_entrevista_metodologia_ia.md). Entre as referências diretamente mobilizadas na apresentação estão Risko e Gilbert (2016), Carter (2020), Buçinca, Malaya e Gajos (2021), Messeri e Crockett (2024), Morucci et al. (2025) e Abdurahman et al. (2025).

