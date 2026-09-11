# Apple — *The Greatest*: revisao instrumentada

## Veredito de estado

- Estado maximo nesta passagem:
  `LEITURA_TECNICA_INSTRUMENTADA_PARCIAL + REVIEW_PACK_BUILT_NOT_WATCHED`.
- Nao autorizar: `REVISAO_AV_INSTRUMENTADA`, `VISTO_1X` ou
  `ANALISE_PROFUNDA`.
- Motivo: 17/17 folhas densas, 5/5 folhas de candidatos, 37 mosaicos a 4 fps,
  waveform, EBU e transcricao oficial foram inspecionados; nao houve playback
  critico continuo nem escuta humana. A critica independente foi incorporada
  sem promover o estado.

## Identidade da copia

| Campo | Valor |
|---|---|
| Hospedeiro | British Arrows, registro oficial de premiacao |
| No audiovisual | Vimeo `807865978` |
| Arquivo | `the_greatest_british_arrows.mp4` |
| SHA-256 | `bd4aa73b9820a19b1f5d51c640c8592775a45810c041b1e94a72dc727c9f2b56` |
| Duracao | 132,608 s |
| Video | H.264 High, 1920x1080, 23,976 fps |
| Audio | AAC-LC, stereo, 48 kHz |
| Qualificador | copia arquivistica British Arrows; nao master oficial Apple fechado |

## Artefatos inspecionados

- 265 amostras densas a cada 0,5 s em 17 folhas.
- 80 candidatos algoritmicos em 5 folhas; nao sao 80 planos confirmados.
- 37 folhas de microeventos a 4 fps, cobrindo toda a copia em nove janelas:
  - 00:00–00:16, casa, Siri, persianas e comandos de voz;
  - 00:16–00:23, espelho, rosto e gestos manuais entre adulta e bebe;
  - 00:23–00:40, gestos manuais, AssistiveTouch, Detection Mode e maquiagem;
  - 00:40–00:44, maquiagem e transicao para o corredor escolar;
  - 00:44–01:03, Logic/Zoom, Speak Screen, Maps e foto por Voice Control;
  - 01:03–01:13, Door Detection e tela preta;
  - 01:13–01:26, cheer, direcao, festa, bebe, Sound Recognition e palco;
  - 01:26–02:08, montagem coletiva, retornos, interfaces e consequencias;
  - 02:08–02:12, gestos manuais finais e logo.
- Waveform, EBU R128 e `silencedetect`.
- Transcricao descritiva oficial Apple e legenda automatica de plataforma.
- Seis fontes atomicas ligadas: British Arrows, D&AD, One Club, Apple
  Education, Apple The Greatest e Apple Newsroom 2022.

## Gate `REVISAO_AV_INSTRUMENTADA`

| # | Exigencia | Estado | Evidencia/limite |
|---:|---|---|---|
| 1 | versao, duracao e hash | cumprido para a copia | arvore de versoes preserva o master Apple como aberto |
| 2 | todos os densos | cumprido | 17/17; 265 amostras |
| 3 | todos os candidatos | cumprido | 5/5; 80 candidatos |
| 4 | inserts, flashes, transicoes e movimento | parcial | nove janelas/37 folhas cobrem toda a copia a 4 fps; movimento realizado e microtiming ainda exigem playback |
| 5 | fala corrigida | parcial forte | transcricao oficial Apple cruzada; performance, letra e idioma efetivo do audio nao ouvidos |
| 6 | mapa de som por beats | parcial forte | fonte oficial + waveform/EBU/silencedetect; sem escuta |
| 7 | EDL manual ou impossibilidade | cumprido pela declaracao | detector e mapa de regimes, nao contagem exata de planos |
| 8 | observacao/declaracao/inferencia | cumprido apos disposicao | mapa refeito em tres campos; V3 independente fechou os residuos sem promover os gates perceptivos |
| 9 | critica independente | cumprido apos disposicao | parecer inicial, V2 adversarial e fechamento V3 em `research/reviews/`; estado global preservado |
| 10 | limites de movimento/som | cumprido | secao final |

## Regra epistemologica

- **OBSERVADO:** forma, gesto, interface ou medicao presente nos artefatos.
- **FONTE DECLARA:** texto atribuido a Apple, D&AD ou arquivo de premio.
- **INFERENCIA:** funcao narrativa plausivel apoiada por mais de um sinal.
- **PROTOTIPO:** regra para testar em outro filme, ainda nao universal.
- **LACUNA:** evidencia atual nao autoriza a afirmacao.

## Mapa de regimes narrativos

Tempos sao aproximados e nao representam EDL.

| Tempo | `OBSERVADO_NO_ARTEFATO` | `FONTE_DECLARA` | `INFERENCIA/TESTE` |
|---|---|---|---|
| 00:00–00:10 | quarto escuro; pessoa; persianas mudam de estado; luminosidade aparente aumenta | Apple descreve comando a Siri/HomePod, Weather e abertura das persianas | testar se iniciar por tarefa torna a feature causal; nao chamar luz de natural nem resultado de eficacia comprovada |
| 00:10–00:24 | iPhone, espelho, rosto e gestos manuais entre adulta e bebe | Apple identifica comandos, resposta falada e troca em ASL | a ordem pode instalar agencia antes do catalogo; recepcao nao medida |
| 00:24–00:39 | pe aciona tela; interface muda; maquiagem; texto `A red jacket` | Apple nomeia AssistiveTouch e Detection Mode/Image Descriptions/VoiceOver | cadeia visual sustenta demonstracao encenada; eficacia, latencia e disponibilidade nao testadas |
| 00:41–01:03 | Logic, texto, Maps, Camera, gesto facial e fotografia aparecem em amostras | Apple nomeia Zoom, Speak Screen, Maps e Voice Control | produto e tarefa sao associados; legibilidade temporal e confiabilidade permanecem abertas |
| 01:03–01:13 | corredor, bengala, telefone; imagem preta ~01:06,8–01:10,3; retorno a porta | Apple descreve Door Detection e declara que o video vai ao preto | retirada de imagem e `PROTOTIPO_DE_ALTO_RISCO`; nao equivale a cegueira nem comprova experiencia acessivel |
| 01:13–01:24 | celebracao, carro, festa, bebe, alerta visual, palco; quase-silencio medido | Apple descreve choro, silencio, Sound Recognition e piano | possivel virada de cuidado/performance depende de escuta e teste de acesso |
| 01:24–02:08 | montagem recombina pessoas, tarefas, telas, trabalho, estudo, direcao, mobilidade e prazer | Apple descreve retornos e a sequencia de acoes | testar pessoa por pessoa se memoria, agencia e valor dramatico sobrevivem a compressao; quantidade nao prova justica |
| 02:08–fim | gestos manuais entre adulta e bebe; logo Apple | Apple identifica a troca como ASL e fornece o conteudo da frase final em sua transcricao | rima relacional e atribuicao corporativa sao leituras; logo tambem pode capturar experiencias como patrimonio de marca |

## Conceito, roteiro e escolha de planos

### Fonte declara

- A D&AD afirma que o elenco compartilhou experiencias antes da escrita e teve
  papel central na concepcao, criacao e musica. Isso e relato de inscricao, nao
  auditoria de poder, consentimento ou autoria individual.
- A Apple identifica os recursos e publica a transcricao descritiva integral.

### Observado

- Muitos blocos permitem reconstruir uma cadeia visual: **pessoa/tarefa -> gesto ou comando ->
  interface legivel -> consequencia no mundo**.
- O produto aparece dentro da atividade e nao como packshot isolado; o fecho usa
  apenas o logo.
- Rosto, corpo/gesto, tela e resultado recebem escalas diferentes.
- A copia passa ao preto no bloco de Door Detection, fato tambem declarado na
  transcricao Apple.

### Inferencia operacional

Um plano de produto entra quando cumpre ao menos uma funcao:

1. estabelece quem quer fazer o que;
2. mostra a barreira de interacao sem transformar a pessoa em problema;
3. torna o input legivel — voz, pe, gesto, expressao, toque ou ambiente;
4. confirma o estado da interface;
5. mostra o resultado pratico, criativo ou afetivo;
6. devolve o quadro a pessoa depois da demonstracao encenada;
7. conecta o caso individual a uma tese coletiva;
8. atribui a marca.

Um close de tela que nao muda a compreensao de input, estado ou resultado e
redundante. Um plano emocional que apaga a funcao pode virar inspiracao vaga.

## Decupagem, camera e montagem

### Observado nos quadros

- A abertura alterna enquadramentos de ambiente/quarto, aproximacao da pessoa e
  detalhe funcional do dispositivo.
- Interfaces sao legiveis em amostras selecionadas para reconhecer mudancas de estado:
  atalho de AssistiveTouch, descricao do paleto, tracks ampliadas, texto lido,
  Camera, Door Detection e alerta de choro.
- Planos mais abertos preservam corpo, equipamento e ambiente; detalhes mostram
  input e feedback.
- O segundo minuto recombina pessoas ja apresentadas; se isso reduz a necessidade
  de reapresentar cada mecanismo e uma hipotese, nao um efeito comprovado.

### Prototipos

- `PROTOTIPO_PENDENTE_DE_PLAYBACK` — movimento de camera so se justifica se
  acompanhar um input, revelar um estado, preservar orientacao ou transferir
  atencao entre pessoa e resultado.
- **Cobertura causal minima:** contexto -> input -> interface -> consequencia ->
  reacao. Nem todo caso exige cinco planos; exige cinco informacoes legiveis.
- **Reuso por memoria:** depois de ensinar uma relacao pessoa/recurso, a montagem
  pode abreviar o retorno. Antes disso, compressao vira confusao.
- `PROTOTIPO_DE_ALTO_RISCO` — preto ou quase-silencio podem deslocar modalidade,
  mas tambem podem simplificar deficiencia para educar o publico sem deficiencia.
  Exigem versoes acessiveis e avaliacao disability-led; tela preta nao equivale
  a cegueira.

### Limites

- Nao afirmar travelling, pan, tilt, handheld, estabilizacao, velocidade,
  continuidade de movimento, match cut ou suporte sem playback.
- Nao inferir lente, sensor, camera, filtro, stop ou distancia focal por
  profundidade aparente.

## Fotografia, luz, cor e arte

### Observado

- Abertura domestica usa sombras quentes; a luminosidade aparentemente motivada
  pela janela aumenta quando as persianas abrem. A origem da luz e desconhecida.
- Maquiagem e casa usam pessego/rosa e luz suave; corredor/palco usa ambar,
  vermelho e preto; estudio musical usa verde/ciano; festa usa magenta/verde.
- O paleto vermelho e legivel no Detection Mode e reaparece vestido no palco;
  a continuidade semantica e inferencia, nao intencao publicada.
- Algumas amostras selecionadas exibem texto ou estado de interface reconhecivel
  ao lado de pele, gesto ou ambiente; isso nao estabelece legibilidade temporal
  durante o playback nem para diferentes condicoes de exibicao.

### Inferencia/prototipo

- Cor funciona melhor quando amarra objeto, pessoa e consequencia — o vermelho
  do paleto nao e apenas paleta, e informacao detectada e identidade de palco.
- Luz pode mudar por verbo narrativo: persianas abrem, ambiente se torna
  utilizavel. Uma mudanca luminosa sem acao ou informacao seria decoracao.
- Diferenciar mundos por cor ajuda a reconhecer personagens na montagem
  coletiva, mas o efeito na audiencia nao foi medido.

### Lacunas

- Nenhuma fonte publica camera, lentes, filtros, stops, LUT, contraste, diagrama
  de luz ou breakdown practical/VFX por plano.
- A copia de premio nao prova intencao de grade nem fidelidade ao master Apple.

## Performance, casting, representacao e acesso

- O processo declarado de experiencias do elenco antes do roteiro e uma pista
  forte de metodo, mas nao prova consulta suficiente, compensacao, poder de veto
  ou consenso entre pessoas com deficiencia.
- A decupagem mostra trabalho, cuidado, estudo, prazer, estilo e criacao. A
  variedade e observavel; dizer que ela evita reducao a diagnostico e uma
  avaliacao representacional, nao prova de recepcao inclusiva.
- Riscos a testar: catalogo de recursos substituir personagem; tecnologia
  individual apagar barreiras sistemicas; musica heroica recolocar a narrativa
  de superacao; marca se apropriar de experiencia vivida; recursos ou pessoas
  parecerem intercambiaveis na montagem.
- Requisitos para projeto novo: consultoria remunerada antes do roteiro,
  autoridade documentada, acessibilidade de set, safety, consentimento por uso,
  versoes com AD/legendas/Libras quando aplicavel e critica independente.

## Som e musica

- A transcricao Apple declara uma faixa baseada em Muhammad Ali, comandos,
  VoiceOver, Speak Screen, Maps, obturadores, silencio, alerta e piano.
- A D&AD atribui ao elenco participacao musical agregada; nao publica cadeia de
  autoria, gravacao ou mix.
- O quase-silencio medido em 01:18,619–01:21,165 coincide com a retirada
  declarada antes do alerta de choro. A funcao dramatica continua inferencia sem
  escuta.
- `PROTOTIPO_PENDENTE_DE_ESCUTA`: cada recurso precisa de espaco audivel e
  prioridade no mix; se a trilha mascarar feedback funcional, a cadeia de
  demonstracao encenada pode deixar de ser compreensivel.

## Principios transferiveis provisoriamente consolidados

1. Comece pela autonomia desejada; apresente a tecnologia quando ela entra na
   causalidade da acao.
2. Nomeie uma interface somente por tela legivel ou fonte primaria.
3. Cubra input, estado e consequencia encenada; close de produto sem mudanca informacional e
   ornamento.
4. Depois de tornar legivel a demonstracao encenada da funcao, devolva o plano
   a pessoa e ao que ela realizou.
5. Use detalhe para mecanismo e plano aberto para agencia/contexto; um nao
   substitui o outro.
6. Experiencia vivida pode informar o roteiro antes de ele fechar, mas o projeto
   deve registrar contribuicao, mudanca, credito, consentimento, compensacao e
   autoridade; participacao agregada nao e consenso nem coautoria provada.
7. Cor e arte devem carregar informacao ou verbo, nao apenas assinatura.
8. Retirar imagem ou som e prototipo de alto risco, nunca atalho de empatia;
   exige versoes acessiveis e teste disability-led.
9. Montagem coletiva so funciona depois que cada pessoa/mecanismo ganhou memoria
   suficiente.
10. Representacao numerosa nao equivale a representacao justa; a critica precisa
    testar quem decide, quem se beneficia e quais barreiras o filme apaga.

## Pendencias antes de qualquer promocao

- playback critico com imagem e som ou manutencao explicita dos gates 4/6 como
  parciais;
- comparacao com a versao Apple padrao e audiodescrita se voltarem a estar
  disponiveis;
- confirmacao humana de movimento, microtiming e mix.

## Disposicao da critica independente

- `P0.1`: aceito; gates 4/5/6 permanecem parciais e nenhum estado foi promovido.
- `P0.2`: aceito; `product proof` foi substituido por
  `DEMONSTRACAO_DE_PRODUTO_ENCENADA` e os limites de eficacia foram explicitados.
- `P0.3`: aceito; processo participativo de premio nao e validacao cultural,
  consenso ou etica concluida.
- `P0.4`: aceito; a copia British Arrows nao e chamada de experiencia acessivel;
  versao AD e legendas confiaveis continuam nao adquiridas.
- `P1.1`: corrigido no mapa de tres campos acima.
- `P1.2`: 14 novas folhas cobrem 00:16–00:23, 00:40–00:44 e 01:26–02:08;
  gate 4 ainda e parcial porque amostragem a 4 fps nao e playback.
- `P1.3–P1.11`: linguagem de legibilidade, camera, luz, cor, som, autoria,
  supercrip, tela preta, barreiras e compressao coletiva foi rebaixada ou
  transformada em pergunta/prototipo com salvaguarda.
- O estado segue parcial; a reauditoria pode fechar somente a disposicao/gate 9,
  nao os gates perceptivos.
- A V3 independente fechou gates 8 e 9; gates 4/5/6 e o estado global continuam
  parciais.
