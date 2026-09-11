# Levi's *Drugstore Male* — revisão textual do áudio

Estado: `ASR_HYPOTHESIS_NOT_HUMAN_HEARD`.

O Whisper small retornou apenas três segmentos `[MUSIC]` e um `[BLANK_AUDIO]`.
Isso não prova ausência de fala, ambiente, efeitos, letra ou conteúdo musical.
Não houve audição humana nem cue sheet.

O `[BLANK_AUDIO]` automático vai de 90,000 a 98,460 s, além da duração do
arquivo (90,517333 s). É classificado como overrun/padding do ASR, não conteúdo,
silêncio certificado ou extensão temporal do objeto.

O detector de silêncio a −42 dB por 0,5 s mediu silêncio de `87.111187` a
`90.517313`, duração `3.406125` s. EBU R128 mediu −19,3 LUFS integrados, LRA
14,8 LU e true peak −4,0 dBFS. Essas medidas descrevem energia do arquivo, não
conteúdo ou função narrativa.

Texto visível amostrado no end frame, a confirmar por source/brand record:

> Watch pocket created in 1873. Abused ever since. Levi's 501. The Original Jean.

O texto visível é `VISIBLE_TEXT`, não transcrição de áudio nem claim validado.
`1873`, `The Original Jean` e qualquer implicação histórica exigem
substanciação da marca/arquivo antes de reutilização.
