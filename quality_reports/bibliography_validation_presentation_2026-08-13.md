# Validação bibliográfica da apresentação

**Arquivo principal:** `2026-08-07_apresentacao_metodologia_ia.Rmd`  
**Data da validação:** 13 de agosto de 2026

## Resumo

- O arquivo não usa `.bib` nem comandos formais `\cite{}`/`@chave`.
- As referências aparecem como citações manuais em `\sourcecite{}` e na lâmina final.
- A validação foi, portanto, feita pelo cruzamento manual das obras citadas com a revisão exploratória do projeto e com registros bibliográficos das editoras, periódicos, bases acadêmicas ou páginas dos autores.
- Obras únicas citadas na apresentação: **16**.
- Citações manuais sem correspondência bibliográfica identificada: **0**.
- DOIs confirmados para as obras que possuem DOI: **15**.
- Problemas de atribuição ou rastreabilidade corrigidos: **3**.

## Correções realizadas

1. A formulação “risco moral” foi substituída por uma formulação autoral mais precisa, porque a apresentação não usava uma fonte explícita para aquele mecanismo.
2. A frase que apresentava a separação entre sessões como prática corrente de workflows de agentes foi substituída por “uma escolha de desenho deste protocolo”; a afirmação anterior dependia de uma fonte comercial e não era necessária para o argumento.
3. A referência a Ionescu et al. (2019) passou a incluir o DOI `10.1007/978-3-030-20040-4_8`, tornando rastreável a fonte da aplicação de “dívida epistêmica” à manufatura inteligente.

## Obras citadas e status

| Obra citada | Status |
|---|---|
| Risko e Gilbert (2016) | OK; DOI confirmado |
| Carter (2020) | OK; DOI confirmado |
| Dell’Acqua et al. (2026) | OK; DOI confirmado |
| Sculley et al. (2015) | OK; registro NeurIPS confirmado |
| Thorndike (1920) | OK; DOI confirmado |
| Nisbett e Wilson (1977) | OK; DOI confirmado |
| Cunningham (1992) | OK; registro ACM confirmado |
| Ionescu, Schlund e Schmidbauer (2019) | OK; DOI confirmado |
| Poole e Rosenthal (1985) | OK; DOI confirmado |
| Clinton, Jackman e Rivers (2004) | OK; DOI confirmado |
| Morucci et al. (2025) | OK; DOI confirmado |
| Adcock e Collier (2001) | OK; DOI confirmado |
| Flanagin et al. (2024) | OK; DOI confirmado |
| Abdurahman et al. (2025) | OK; DOI confirmado |
| Buçinca, Malaya e Gajos (2021) | OK; DOI confirmado |
| Messeri e Crockett (2024) | OK; DOI confirmado; aparece na lâmina “Para aprofundar” |

## Limite da validação

Como não há arquivo `.bib`, não é possível reportar chaves órfãs ou entradas fantasma no sentido estrito da skill `validate-bib`. A apresentação usa referências impressas manualmente; a auditoria acima verifica a correspondência entre essas menções e obras bibliográficas identificáveis, sem converter o documento para um fluxo de citações automatizado.

## QA do artefato final

- PDF recompilado com XeLaTeX via `rmarkdown::render()`.
- `pdfinfo`: **15 páginas**, sem criptografia ou erro de estrutura reportado.
- `pdftotext`: confirmou as correções no texto final e a presença do DOI de Ionescu et al. (2019).
- As 15 páginas foram rasterizadas e inspecionadas visualmente; não foram observados cortes, sobreposições ou referências ilegíveis.
