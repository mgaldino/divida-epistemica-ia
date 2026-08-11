# Revisão da transcrição

Data: 11 de agosto de 2026

## Evidência de fonte

O post oficial da a16z identifica os participantes como Alejandro Maza, Angela
Strange e Gabriel Vasquez. A transcrição introduz o convidado oralmente como
“Ale Massa”; a grafia nominal adotada nos rótulos segue a fonte oficial:
`Alejandro` (a grafia completa na fonte é Alejandro Maza).

## Correção do encerramento

O primeiro passe do Whisper gerou três microsegmentos adicionais entre
`00:36:16.170` e `00:36:16.410`. Dois continham “Thank you very much, Ale.” e
um repetia “Thanks for having me.”. As durações de 0,12 s, 0,04 s e 0,08 s eram
fisicamente incompatíveis com o texto.

Um recorte independente de seis segundos (`00:36:12–00:36:18`) foi
retranscrito localmente com timestamps por palavra, com e sem
`condition_on_previous_text`. Ambos os passes retornaram somente:

- `00:36:13.420–00:36:15.220`: “Amazing. Ale, thank you for joining us.”
- `00:36:15.220–00:36:16.220`: “Thank you. Thanks for having me.”

Os três microsegmentos espúrios foram removidos do arquivo revisado
`segmentos_whisper.json`. O resultado bruto original foi preservado em
`segmentos_whisper_raw.json`.

## Limite da identificação de falantes

As fontes confirmam os três participantes, mas não oferecem diarização. O
arquivo `speakers.tsv` usa `Alejandro` e o rótulo coletivo `Host` somente onde
o papel é sustentado pelo conteúdo e pela estrutura da entrevista. Angela e
Gabriel não são distinguidos individualmente sem evidência acústica suficiente;
suas intervenções recebem apenas o rótulo coletivo `Host`.

## Tradução

Os 425 segmentos revisados em inglês foram traduzidos em correspondência 1:1,
sem alterar os intervalos. NLLB-200 e Unicamp EN–PT T5 produziram rascunhos
independentes; Qwen3-8B 4-bit revisou cada segmento localmente contra o inglês e
fez um segundo passe com contexto vizinho. Uma leitura comparativa identificou
calques, termos técnicos e alguns vazamentos do contexto; 124 correções foram
registradas com justificativa em `translation_corrections.tsv` e aplicadas de
modo reproduzível a `segmentos_traducao_final.json`.

A validação confirmou ausência de segmentos vazios, alinhamento integral e
preservação dos números, aceitando a equivalência correta “20th century” ↔
“século XX”. O segundo passe acústico também sustentou correções no inglês
revisado, entre elas `a16z`, `Ale Maza`, `evals`, `Fields Medal-level`, `Now`
em vez de `Natalie` e `queue` em vez de `cue`. O primeiro passe do Whisper
permanece intocado em `segmentos_whisper_raw.json`.
