# Cadbury Dairy Milk — *Gorilla*: revisao instrumentada

## Veredito de estado

- Estado maximo autorizado nesta passagem: `LEITURA_TECNICA_INSTRUMENTADA_PARCIAL + REVIEW_PACK_BUILT_NOT_WATCHED`.
- Nao autorizar: `REVISAO_AV_INSTRUMENTADA`, `VISTO_1X` ou `ANALISE_PROFUNDA`.
- Motivo: imagem foi examinada densamente e em janelas de microevento, mas nao houve reproducao critica continua; o mapa auditivo depende de waveform/EBU e de uma analise audiovisual externa, nao de escuta direta. A critica independente existe e manteve o estado parcial; a incorporacao ainda requer reauditoria.

## Identidade da copia

| Campo | Valor |
|---|---|
| Origem da copia | upload publico de terceiro no YouTube |
| URL | https://www.youtube.com/watch?v=7S13-q_aprc |
| Arquivo de trabalho | `cadbury_gorilla.mp4` |
| SHA-256 | `1e63ec9a45a8807157ea2af51d42a0ea13588d8dd20095cb1a4142007584169c` |
| Duracao medida | 91,579501 s |
| Video | H.264, 320x240, 4:3, 30 fps, ~149 kb/s |
| Audio | AAC LC, stereo, 44,1 kHz, ~128 kb/s |
| Master historico | 90 s, confirmado pelo History of Advertising Trust |
| Anomalia de copia | marca `DIVX` em ~01:30,6; cauda nao criativa |

Esta copia serve para pesquisa de estrutura. Nao serve para julgar textura fina, foco, latitude, grano, qualidade de pele/fur, nitidez de lente ou intencao de grade.

## Artefatos realmente inspecionados

- 12/12 contact sheets densos, totalizando 183 amostras a cada 0,5 s.
- 1/1 contact sheet com 7 candidatos algoritmicos a mudanca visual.
- Frames individuais da transicao performance–packshot.
- Cinco mosaicos adicionais a 4 fps em 00:14–00:18, 00:22–00:34, 00:43–00:47, 00:58–01:18 e 01:23–01:27, preservados em `microevent_contact_sheets/` com a janela no nome do arquivo.
- Waveform integral.
- EBU R128 integral.
- Metadata/streams, manifesto, CSV de candidatos e ASR automatico.
- 13 cenas de analise audiovisual externa, normalizadas em `external_ai_scene_analysis.md`.
- Fontes atomicas D&AD, Guardian, British Arrows e HAT.

## Gate `REVISAO_AV_INSTRUMENTADA`

| # | Exigencia | Estado | Evidencia/limite |
|---:|---|---|---|
| 1 | versao, duracao e hash | cumprido para a copia; master nao autorizado | hash/metadata locais + HAT 90 s |
| 2 | todos os densos | cumprido | 12/12 sheets, 183 amostras |
| 3 | todos os candidatos | cumprido | 7/7 candidatos; detector nao e EDL |
| 4 | inserts, flashes, transicoes e movimento | parcial | janelas a 4 fps inspecionadas; microtiming continuo continua inacessivel |
| 5 | fala/transcricao | `PARCIAL_NADA_IDENTIFICADO_NOS_ARTEFATOS_SEM_ESCUTA` | ausência não certificada; letra automática rejeitada |
| 6 | mapa de som por beats | parcial | waveform/EBU + analise externa; sem escuta critica |
| 7 | EDL manual ou declaracao de impossibilidade | cumprido pela declaracao | nao ha contagem exata confiavel nesta copia; abaixo ha mapa de regimes, nao EDL |
| 8 | separar observacao, declaracao e inferencia | cumprido | secoes rotuladas |
| 9 | critica independente | cumprido | `research/reviews/2026-08-10_CADBURY_GORILLA_INDEPENDENT_CRITIQUE.md`; veredito sem promocao |
| 10 | limites de movimento/som | cumprido | secao final |

## Observacao visual: mapa temporal

Tempos sao aproximados e descrevem esta copia de 91,58 s. A cauda de terceiro nao pertence ao master historico.

| Tempo | Observacao | Informacao nova | Funcao narrativa/comercial |
|---|---|---|---|
| 00:00–00:06,5 | campo roxo; entra assinatura `a GLASS and a HALF FULL PRODUCTION` | existe um mundo de marca antes de existir produto | preparar codigo cromatico e tom de apresentacao |
| ~00:06,5–00:17,7 | detalhes extremos de pelo, testa, olhos e nariz; identidade emerge aos poucos | a criatura e reconhecida por fragmentos | curiosidade sem explicar; obrigar atencao ao microgesto |
| ~00:17,7–00:23,5 | close frontal mais legivel; fundo roxo | o absurdo e apresentado com solenidade | estabilizar personagem e recusar punchline imediata |
| ~00:23,5–00:30,7 | retorno a detalhe extremo de nariz/olhos; abertura gradual do olhar | respiracao e concentracao tornam-se acao | transformar espera em performance, nao em vazio |
| ~00:30,7–00:44,5 | close/medium close sustentado; cabeca e olhar mudam lentamente | intencao parece existir antes de sabermos qual | acumular antecipacao e credibilidade comportamental |
| ~00:44,5–00:59,5 | enquadramento se abre gradualmente; caixas, torso e bateria entram na geografia | o espaco e reclassificado como estudio de ensaio | revelacao espacial substitui exposicao verbal |
| ~00:59,5–01:04 | primeiro regime de performance vigorosa; cortes entre angulos proximos e conjunto | a espera encontra sua descarga | sincronizar virada visual com virada musical |
| ~01:04–01:09 | plano amplo da bateria e do estudio | corpo, instrumento e contato ficam simultaneamente legiveis | sustentar plausibilidade visual da performance, nao provar audio ao vivo |
| ~01:09–01:12,3 | retorno a enquadramentos mais proximos e gestos amplos | energia e expressao ocupam o quadro | intensificar sem acrescentar historia nova |
| ~01:12,3–01:24,5 | plano amplo/medio amplo sustentado ate os golpes finais | performance chega ao fecho | deixar o prazer completar-se antes da assinatura |
| ~01:24,5–01:27 | dissolve do estudio para campo roxo e embalagem; identidade do pack torna-se legivel | fonte da experiencia e finalmente nomeada | atribuir a sensacao a Dairy Milk |
| ~01:27–01:30,5 | packshot roxo com `A glass and a half full of joy` | plataforma verbal fecha a promessa | converter descarga musical em territorio de marca |
| ~01:30,6–01:31,6 | watermark `DIVX` | interferencia de distribuicao | excluir da obra |

## Regimes de plano e montagem

### Contencao

**Observacao:** antes de ~59,5 s, a montagem usa poucos regimes, detalhes extremos e um desenvolvimento muito lento de escala. Tres mudancas fortes aparecem aproximadamente em 17,7, 23,5 e 30,7 s; depois ha uma passagem longa que abre o espaco.

**Inferencia:** a funcao nao e ostentar lente macro. Fragmentar e depois recompor adia a resposta para duas perguntas — `o que e?` e `o que vai fazer?`. Cada ampliacao de contexto paga uma parte da curiosidade sem liberar o payoff.

**Limite:** nao ha EDL exata. Compressao, movimento da criatura e mudanca gradual de enquadramento confundem o detector; 44,5 s pode ser alteracao dentro do mesmo plano.

### Descarga

**Observacao:** em ~59,5 s, a acao muda de regime. Entre ~59,5 e 72,3 s, ha alternancia mais rapida entre proximidade e plano amplo; depois o conjunto volta a sustentar a performance ate o dissolve.

**Inferencia:** o aumento de frequencia de corte acompanha a liberacao, mas o filme ainda preserva planos amplos suficientes para provar a acao. Cortar apenas em detalhes destruiria a credibilidade da performance.

**Hipotese rejeitada:** `quanto mais rapido o corte, maior a energia`. Aqui a energia nasce primeiro do acontecimento e da musica; a montagem redistribui ponto de vista. Sem a espera anterior, os mesmos cortes teriam menos efeito.

## Camera e composicao

### Observacao

- O inicio privilegia extreme close-ups de olhos, testa, nariz e textura do pelo.
- O fundo roxo elimina geografia externa e torna a criatura uma presenca grafica.
- O enquadramento frontal e o eixo do olhar evitam a codificacao imediata de sketch.
- A abertura progressiva do quadro revela caixas, paredes, cortina e bateria.
- Na performance, planos proximos registram rosto/bracos e planos amplos preservam instrumento e ambiente.

### Intencao declarada por fontes

- Juan Cabral descreveu a ideia como uma tentativa de levar a marca ao coracao, nao ao raciocinio explicativo.
- Fontes de processo dizem que a cena foi tratada com seriedade documental para o absurdo nao virar piada descartavel.
- O perfil/entrevista da shots descreve editorialmente os primeiros 60 s como close/concentracao seguidos de abertura e bateria; `research/sources/2013_SHOTS_JUAN_CABRAL_AD_ICON.md` registra que isso e simplificacao, nao EDL.

### Inferencia operacional

- **Escala como revelacao:** decidir o tamanho de plano pelo quanto de contexto o publico pode receber agora, nao por uma tabela de cobertura.
- **Frontalidade como contrato tonal:** quando a premissa e absurda, composicao solene pode pedir que o espectador a aceite antes de rir.
- **Plano amplo como prova visual limitada:** depois de vender concentracao por detalhes, mostrar corpo+instrumento sustenta plausibilidade corporal. Nao prova que o audio final foi captado ao vivo.

### O que nao sabemos

- Camera, lente, focal, filtro, stop, suporte, velocidade real de obturador e estrategia de foco.
- Se existe speed ramp ou handheld deliberado. A analise externa sugeriu ambos; a amostragem nao confirma.
- Se o pullback e uma tomada unica, composicao de movimentos ou sucessao de planos sutis.

## Fotografia, luz e cor

### Observacao

- Roxo domina fundo inicial e end frame; uma faixa amarela fina atravessa parte da parede do estudio.
- Pelo preto e pele cinza recebem highlights que separam testa, nariz e bochechas do fundo.
- O inicio e mais fechado/escuro; o estudio revelado inclui brancos, cinzas, verde de cortina, preto de caixas e reflexos cromados da bateria.
- O packshot retira a variedade do estudio e volta a um campo roxo quase total.

### Inferencia

- O roxo funciona como continuidade de marca: prepara atribuicao muito antes do logotipo.
- Highlights na criatura nao servem so a `beleza`; tornam microgestos legiveis durante uma espera longa.
- A passagem de rosto escuro/texturizado para metais brilhantes torna a bateria visualmente explosiva sem trocar a familia cromatica do fundo.
- O retorno ao roxo puro no packshot fecha um arco cromatico: codigo -> mundo -> codigo+produto.

### Limite

Nao inferir grade, temperatura de fonte, contraste de captacao ou escolha de camera a partir de um arquivo 320x240 fortemente comprimido. `Roxo de marca` e observavel; `por que tal camera/cor foi escolhida` so e declaravel parcialmente.

## Performance, casting e criatura

### Fatos de fonte

- Garon Michael e o performer creditado pelo HAT.
- A criatura e pratica: traje/animatronica com operadores, segundo D&AD e Guardian.
- Michael precisou aprender bateria.
- O calor do traje limitava a duracao de tomadas e exigia resfriamento/hidratacao.

### Observacao

- Antes da bateria, acao e composta de piscadas, respiracao/expansao do nariz, olhos fechados, mudancas de olhar, giro lento e extensao do pescoco.
- A performance evita aceno ao espectador, sorriso explicativo ou gag corporal antecipada.
- Durante a descarga, bracos, torso e cabeca ocupam amplitudes maiores; a batera oferece resistencia e contato visiveis.

### Inferencia

- O casting precisava combinar presenca dentro do traje, controle de microgesto e capacidade de tornar a bateria plausivel.
- Treinar o performer protegeu a legibilidade corporal do plano amplo: sem coordenacao plausivel, a montagem teria de esconder a acao em fragmentos. Isso nao demonstra autoria do audio final.
- A limitacao termica deveria afetar ordem de planos, duracao de take, ensaio fora do traje e cobertura de seguranca.

## Som e musica

### Medicao local

- Loudness integrado: `-21,5 LUFS`.
- Loudness range: `14,1 LU`.
- True peak: `-6,8 dBFS`.
- Entre 00:06,5 e 00:59,5, amostras momentary locais variam aproximadamente de `-42,2` a `-19,4 LUFS`; entre 00:59,5 e 01:24,5, variam de `-30,2` a `-16,6 LUFS`. Os intervalos mostram dinamica, nao estabilidade; inicio e cauda incluem valores ainda mais baixos.
- A energia cai rapidamente por volta de 01:28–01:30.

### Analise externa corroborada

- Introducao atmosferica/pulso no inicio.
- Entrada de voz cantada em torno de 00:18.
- Fill de bateria de alto impacto em torno de 00:59.
- Regime denso de bateria ate o packshot e fade final.

### Inferencia

- A faixa nao e `trilha de apoio`: e relogio estrutural. O publico que reconhece sua arquitetura antecipa uma virada antes de ve-la.
- O filme monta expectativa sobre um evento musical ja existente e faz a criatura parecer estar esperando o mesmo momento que o publico.
- A duracao de 90 s e funcional porque preserva a preparacao musical; um cutdown nao pode apenas remover 30 s sem redesenhar a promessa de atraso.

### Limites e risco

- Sem escuta critica, nao afirmar sincronismo fino de golpes, efeitos de sala, camadas de foley, panorama ou compressao criativa.
- O mecanismo depende parcialmente de reconhecimento cultural da faixa; audiencias que nao a conhecem ainda recebem contraste de energia, mas podem perder antecipacao especifica.
- Licenciamento, direitos territoriais e custo da musica fazem parte da ideia, nao de uma etapa administrativa tardia.

## Marca e produto

### Fatos declarados

- Brief: recuperar amor pela marca.
- Estrategia declarada: fazer a comunicacao proporcionar sensacao comparavel ao prazer do produto.
- Duas ideias mais centradas em chocolate foram apresentadas antes do caminho do gorila.
- A ausencia de consumo e produto dentro da narrativa foi defendida por agencia e cliente.

### Observacao

- Cor de marca aparece desde o primeiro segundo.
- Produto nao participa da acao.
- O pack fica legivel apenas nos segundos finais, depois da performance.
- A assinatura verbal traduz a experiencia para `joy`.

### Leitura critica

- O filme demonstra **efeito desejado da marca**, nao funcao fisica do chocolate.
- O end frame nao e um apendice qualquer: ele fecha uma promessa previamente codificada por roxo, plataforma e prazer. `Ownership antes do produto` e inferencia condicionada ao reconhecimento desses ativos, nao efeito universal observado.
- **Permutabilidade do sistema de marca:** baixa quando roxo, `glass and a half` e pack permanecem e sao reconhecidos pela audiencia.
- **Permutabilidade do mecanismo criativo:** alta/moderada se outra marca substituir o sistema e mantiver `espera + musica conhecida + performance absurda + packshot`. Logo, `produto tardio` nao e regra; exige arquitetura de atribuicao testada.

## Decisoes reconstruidas

### 1. Entregar a promessa como experiencia

- `WHAT`: substituir demonstracao de consumo por 90 s de antecipacao e descarga musical.
- `WHY_DECLARADO`: recuperar amor e fazer o publico sentir prazer.
- `EFFECT_INFERIDO/HIPOTESE_A_TESTAR`: a forma pode dramatizar um benefício
  emocional antes de nomeá-lo; compreensão e efeito não são observados nos frames.
- `ALTERNATIVE`: ideia com chocolate no centro.
- `WHY_NOT`: seria mais segura, mas menos capaz de renovar a relacao afetiva.
- `PRINCIPLE`: quando a promessa e sensorial, a forma pode ser a demonstracao — desde que atribuicao e contexto amarrem a experiencia ao produto.

### 2. Fazer o absurdo atuar serio

- `WHAT`: criatura pratica, comportamento concentrado, fundo simples e paciencia de enquadramento.
- `WHY_DECLARADO`: impedir que a premissa vire gag descartavel.
- `EFFECT_INFERIDO/HIPOTESE_A_TESTAR`: o hold pode convidar procura de intenção
  no rosto; atenção, expectativa e resposta do espectador não foram medidas.
- `ALTERNATIVE`: exagerar humor, reacao ou montagem desde o inicio.
- `WHY_NOT`: gastaria a surpresa antes da musica.
- `PRINCIPLE`: quanto mais impossivel a premissa, mais util pode ser uma direcao de performance disciplinada.

### 3. Usar duracao como mola

- `WHAT`: preservar aproximadamente 60 s de preparacao antes da bateria.
- `WHY_DECLARADO`: 90 s eram tratados como duracao ideal; a antecipacao e parte da experiencia.
- `EFFECT_INFERIDO/HIPOTESE_A_TESTAR`: a mudança amostrada de gesto/escala e a
  região sonora medida podem produzir liberação; timing, som percebido e efeito
  de audiência exigem playback, escuta e teste.
- `ALTERNATIVE`: chegar rapido ao gorila tocando.
- `WHY_NOT`: mostraria a ideia, mas removeria o percurso emocional que a faz funcionar.
- `PRINCIPLE`: atraso so e narrativo quando cada beat acumula expectativa, informacao ou tensao; demora vazia nao e suspense.

### 4. Provar performance em vez de esconder

- `WHAT`: treinar performer e incluir planos amplos do corpo+instrumento.
- `WHY_DECLARADO`: havia um traje pratico e um performer que precisava aprender bateria.
- `OBSERVADO_EM_AMOSTRAS`: corpo, instrumento e contato aparecem juntos em
  enquadramentos amplos. `INFERIDO`: isso pode aumentar plausibilidade visual.
  `NAO_DEMONSTRADO`: execução sonora ao vivo, credibilidade percebida ou efeito
  no público.
- `ALTERNATIVE`: detalhes, dublagem fragmentada ou criatura digital sem prova ampla.
- `WHY_NOT`: enfraqueceria a satisfacao do acontecimento.
- `PRINCIPLE`: quando o prazer depende de habilidade corporal, a decupagem precisa reservar um plano que a demonstre.

### 5. Fazer codigo de marca trabalhar antes do logo

- `WHAT`: roxo como ambiente inicial, fundo do estudio e campo final.
- `WHY_INFERIDO`: manter codificacao visual durante longa ausencia de pack.
- `EFFECT_INFERIDO`: para quem reconhece roxo e `glass and a half`, o produto parece emergir de um sistema ja atribuido; para audiencia fria, pode permanecer apenas `brand-coded` ate o pack.
- `ALTERNATIVE`: estudo neutro e packshot roxo apenas no final.
- `RISK`: cor isolada pode nao bastar em mercados onde nao e distintiva.
- `PRINCIPLE`: presenca de marca pode ser distribuida na forma, mas cada codigo precisa de teste de distintividade e contexto.

## O que nao copiar

- animal inesperado + musica famosa;
- 60 s de `nada` antes de um payoff;
- roxo como atalho para Cadbury;
- produto apenas no fim como sinal de sofisticacao;
- plano longo sem progressao interna;
- microgesto sem performer/rig capaz de sustenta-lo;
- uma unica pessoa acumulando autoria como regra de organizacao.

## Perguntas transferiveis para a skill

1. Qual sensacao do produto o filme pode realmente **fazer acontecer**, em vez de apenas afirmar?
2. O que cada segundo de atraso deposita na expectativa?
3. Qual informacao deve ser revelada por escala de plano e qual por corte?
4. Que plano prova a acao principal sem ajuda de montagem?
5. Que codigo de marca ja trabalha antes do packshot — e ele e distintivo para esta audiencia?
6. Se a musica for removida ou desconhecida, o arco ainda funciona?
7. Direitos, duracao e custo da musica tornam a ideia inviavel?
8. O absurdo esta sendo dirigido como verdade, como sketch ou como espetaculo? Por que?
9. A referencia esta sendo usada por seu mecanismo ou apenas por sua superficie reconhecivel?
10. Se o packshot for trocado por outra marca, o filme ainda parece pertencer ao cliente?

## Limites finais

- Nao houve playback critico continuo com imagem e som.
- Movimento persistente, aceleracao, microtiming de performance e continuidade entre golpes nao podem ser julgados integralmente.
- O mapa sonoro nao descreve espacialidade ou sincronismo fino.
- A copia e pequena, comprimida e contaminada por cauda de terceiro.
- Camera/lentes/luz nao foram publicadas nas fontes recuperadas.
- Relatos divergem sobre um ou dois dias de filmagem.
- Resultados de pesquisa e negocio sao declaracoes retrospectivas; nao isolam causalidade.
- A critica independente foi concluida com veredito de **nao promocao**; gates de som e movimento continuam parciais.
