# Honda Accord — *Cog*: revisao instrumentada

## Veredito de estado

- Estado maximo autorizado nesta passagem: `LEITURA_TECNICA_INSTRUMENTADA_PARCIAL + REVIEW_PACK_BUILT_NOT_WATCHED`.
- Nao autorizar: `REVISAO_AV_INSTRUMENTADA`, `VISTO_1X` ou `ANALISE_PROFUNDA`.
- Motivo: todas as amostras densas, candidatos e quatro janelas de microevento foram inspecionados; versao, creditos, processo e estrutura estao cruzados. Nao houve reproducao continua critica nem escuta humana; a costura entre as duas tomadas nao foi localizada em frame com evidencia suficiente. Critica independente e reauditoria foram incorporadas com veredito de nao promocao.

## Identidade da copia arquivistica de pesquisa

| Campo | Valor |
|---|---|
| Origem | copia arquivistica de premiacao apontada pelo registro do One Club; nao e master de exibicao original |
| URL de origem | `https://d2z00kf51ll94q.cloudfront.net/archive/2004/media/04079A_a_XLarge.mov` |
| Arquivo | `honda_cog_oneclub.mov` |
| SHA-256 | `cb57a3ece332729e780b008e26acf00121402eddc16dc75dc57829eda7d6d4c2` |
| Tamanho | 130.473.813 bytes |
| Duracao medida | 120,587254 s |
| Video | H.264 Main, 720x405, 29,97 fps, progressive, ~8,36 Mb/s |
| Audio | AAC LC, stereo, 48 kHz, ~290 kb/s |
| Timecode do arquivo | `01:00:00;00` |
| Duracao historica | Honda: 120 s; HAT: 00:02:01 |
| Watermark | One Club no canto inferior direito; pertence ao recipiente arquivistico, nao ao master de exibicao |

A copia e adequada para estrutura, geometria, cor macro e eventos. Nao autoriza inferir negativo/sensor, lente, filtro, stop, textura fina, foco critico ou intencao de grade.

## Artefatos realmente inspecionados

- 16/16 contact sheets densos, 241 amostras a cada 0,5 s.
- 1/1 contact sheet com 2 candidatos algoritmicos.
- Waveform integral, EBU R128, metadata, manifesto e CSV.
- ASR `large-v3` e transcricao textual da shots.
- Quatro mosaicos auditaveis a 4 fps, preservados em `microevent_contact_sheets/`:
  - 00:00–00:18, mecanismo inicial;
  - 00:53–01:05, janela do silencioso/ponto de costura declarado;
  - 01:13–01:30, janela, agua, limpadores, parabrisa e vidros;
  - 01:44–01:58, carro completo, banner e corte de marca.
- 27 beats de analise audiovisual externa, integralmente normalizados em `external_ai_scene_analysis.md`.
- Fontes atomicas Guardian, One Club, HAT, Honda Engine Room e shots.

## Gate `REVISAO_AV_INSTRUMENTADA`

| # | Exigencia | Estado | Evidencia/limite |
|---:|---|---|---|
| 1 | versao, duracao e hash | cumprido | copia arquivistica One Club + SHA + Honda/HAT |
| 2 | todos os densos | cumprido | 16/16; 241 amostras |
| 3 | todos os candidatos | cumprido | 2/2; detector nao e EDL |
| 4 | inserts, flashes, transicoes e movimento | parcial | quatro janelas 4 fps preservadas; sem playback continuo |
| 5 | fala corrigida | cumprido textualmente | shots + ASR; sem escuta humana |
| 6 | mapa de som por beats | parcial | 27 beats externos + waveform/EBU; sem escuta critica |
| 7 | EDL manual ou impossibilidade | cumprido pela declaracao | forma percebida continua; corte certo para end frame em 01:57,451; costura invisivel sem frame confirmado |
| 8 | observacao/declaracao/inferencia | cumprido | secoes rotuladas |
| 9 | critica independente | cumprido apos disposicao | `research/reviews/2026-08-10_HONDA_COG_INDEPENDENT_CRITIQUE.md`; P0/P1 incorporados, sem promocao |
| 10 | limites de movimento/som | cumprido | secao final |

## Observacao visual: mapa temporal

Tempos descrevem o arquivo One Club de 120,587 s. Eles sao marcos de beat, nao contagem de planos.

| Tempo aproximado | Observacao | Informacao nova | Funcao narrativa/comercial |
|---|---|---|---|
| 00:00–00:05 | engrenagens pequenas rolam sobre viga; as amostras mostram reenquadramento para a direita | componentes reconheciveis iniciam a cadeia | abrir com causalidade, nao com carro pronto |
| 00:05–00:17 | tubos, camshaft/mola e painel transferem impulso; parafusos deslizam | tamanho, peso e eixo mudam | demonstrar variedade sob uma regra unica |
| 00:17–00:30 | bateria/fio, bloco, radiador e rodas levam a acao ao alto | a cadeia usa gravidade, tracao e rampa | renovar risco sem cortar para outra cobertura |
| 00:30–00:46 | bancos, manual, vidro, esferas, cabecote e ventilador | materiais macios, papel, vidro e ar entram | transformar catalogo de pecas em coreografia de propriedades |
| 00:46–00:55 | esfera atravessa trilho vertical; componente cilindrico e liberado | causalidade deixa o piso e volta a ele | produzir variacao espacial mantendo legibilidade |
| 00:55–01:05 | cilindro/silencioso cruza; secao frontal e pneu assumem o movimento | fonte situa a emenda nesta passagem; janela e plausivel, mas mecanismo/frame nao foram provados | proteger a experiencia de sistema unico |
| 01:05–01:15 | pneu aciona bielas; porta, macaneta e vidro entram | componentes agora demonstram funcao reconhecivel do carro | aproximar mecanismo abstrato de atributo de produto |
| 01:15–01:25 | agua ativa lavador; limpadores movem o parabrisa | sensor/feature solicitado pelo cliente vira causa, nao insert explicativo | integrar selling point a dramatizacao |
| 01:25–01:35 | parabrisa aciona paineis de vidro; painel/cluster acende | a cadeia sobe, reflete e chega a eletronica | escalar delicadeza antes do payoff; relacao musical depende de escuta |
| 01:35–01:45 | mola atravessa mesa/alto-falantes; mecanismo gira chave | a analise externa situa aumento musical; imagem mostra ignicao | preparar passagem de pecas para carro vivo; som permanece hipotese corroborativa |
| 01:45–01:50 | Accord completo desce da rampa; tampa traseira fecha | todo finalmente emerge das partes | payoff de produto sem interromper a regra causal |
| 01:50–01:55 | carro para; banner `ACCORD` desce; locucao | nome e promessa chegam depois da prova | converter engenho em proposicao de marca |
| 01:55–01:57,451 | carro e banner permanecem | resultado e sustentado | permitir leitura/atribuicao |
| 01:57,451–fim | corte para fundo branco e Honda | assinatura corporativa | fechar marca e plataforma |

## Plano, corte e continuidade

### Observacao

- Do primeiro mecanismo ate o carro final, a imagem mantem direcao dominante da esquerda para a direita.
- As amostras e o processo publicado sugerem reenquadramentos orientados a frente causal, deixando componentes resolvidos e tornando o proximo receptor legivel; nao e reconstrucao de movimento continuo.
- O detector de diferenca visual encontrou apenas o inicio e o corte do end frame em `01:57,451`.
- A costura publicada entre duas tomadas nao aparece como candidato algoritmico.
- O end frame e um corte editorial inequivoco; os 27 segmentos externos sao beats semanticos, nao 27 shots.

### Intencao/processo declarado

- Guardian: o estudio necessario para uma unica tomada seria caro demais; foram usadas duas tomadas, unidas quando escapamento/silencioso atravessa o piso.
- Guardian: camera executava uma danca complexa para cima/baixo num track e falhas de camera podiam invalidar a tentativa.
- Honda: resultado final e composto por duas tomadas costuradas; execucao foi filmada em tempo real.
- shots chama a aparencia de `one long take`; isso descreve a experiencia, nao a captacao literal.

### Inferencia operacional

- **Camera como testemunha causal:** as amostras e o processo sugerem reenquadramento orientado ao elo ativo. Sem playback, nao afirmar simultaneidade universal, chegada no instante ideal ou microtiming.
- **Continuidade como experiencia de sistema:** a mise-en-scene reduz elipses perceptiveis e fabrica uma causalidade quase ininterrupta. Costura e pos coexistem com essa experiencia; ela nao e auditoria forense nem prova que nenhum elo foi ocultado.
- **Direcao lateral como gramatica:** eixo constante reduz custo cognitivo. A complexidade fica nos acontecimentos, nao na orientacao espacial.
- **Janela plausivel de costura:** a passagem do silencioso, continuidade lateral e geometria repetivel entre 00:53–01:05 podem mascarar/matchear a emenda. O objeto nao encobre inequivocamente todo o quadro; tecnica, mascara e frame exatos nao foram provados.

### Hipotese rejeitada

`Plano-sequencia e automaticamente mais imersivo.` Aqui a continuidade funciona porque a acao e causal, espacialmente legivel e renovada. Uma tomada longa de cobertura passiva nao produziria a mesma prova.

## Composicao e fotografia

### Observacao

- Ambiente arquitetonico branco/verde-ciano, lambris e piso de madeira clara formam uma base repetivel.
- Componentes pretos, metalicos e de vidro ganham contraste contra o fundo; fios/bateria/jacks introduzem pequenos acentos vermelhos.
- A composicao frequentemente reserva espaco a direita para a proxima consequencia.
- Escala de plano muda dentro do acompanhamento: detalhe suficiente para pequenas transferencias; campo mais amplo para pneus, paineis, rampas e carro completo.
- O carro final e o primeiro objeto que ocupa a composicao como produto inteiro, nao fragmento funcional.

### Intencao declarada relevante

- Bardou-Jacquet relata que a cadeia desenhada precisou mudar por diferencas de escala, peso, velocidade e limite de refoco da camera.
- Honda descreve a aparencia como bela e precisa, ligada a engenharia.

### Inferencia

- Fundo neutro nao significa ausencia de arte: ele cria uma `folha de prova` onde deslocamentos minimos e falhas ficam legiveis.
- Nesta copia, a dominante fria produz uma leitura possivel de laboratorio e contrasta com madeira/metal. Tags de cor inconsistentes e encode arquivistico impedem atribuir essa leitura a uma decisao de grade ou afirmar que foi escolhida para se separar da publicidade de estrada.
- Espaco negativo a frente do movimento e informacao operacional: mostra para onde olhar e onde a proxima relacao precisa acontecer.
- Variar escala pela necessidade de ler o elo e mais util que impor uma cobertura fixa de wide/medium/close.

### O que nao sabemos

- Camera, lente, focal, stop, filtro, negativo/sensor, stock, cabeca, dolly/track exatos, esquema de luz e decisao de grade.
- `David Ungaro` esta confirmado em camera/lighting, mas credito nao autoriza reconstruir equipamento.
- O master arquivistico tem tagging de cor inconsistente (`smpte170m`/`bt709`); nao usar metadata de entrega como intencao de captacao.

## Direcao de arte, props e engenharia

### Fatos de processo

- A agencia desenhou uma cadeia teorica antes da producao; quase todas as ligacoes mudaram na pratica.
- Honda liberou £100 mil e dois carros como gate de viabilidade antes do budget integral.
- Meses de testes envolveram engenheiros, artistas, escultores e designer.
- Pedidos tardios do cliente, como limpadores automaticos ao detectar agua, foram incorporados.
- Temperatura, vento e pequenas variacoes podiam alterar o resultado; cada tentativa exigia reset.

### Leitura

- Props nao sao decoracao: cada item tem massa, atrito, centro de gravidade, tolerancia, curso e estado anterior/seguinte.
- A arte precisa desenhar simultaneamente beleza, causalidade e resetabilidade.
- O `storyboard` adequado para esse tipo de filme nao e apenas quadro bonito; precisa de mapa de estados, transferencia de energia, tolerancia e plano de recuperacao.
- Teste de viabilidade e etapa criativa. O prototipo descobre o roteiro fisico que o papel nao consegue prever.

## Som e musica

### Medicao local

- Loudness integrado: `-23,8 LUFS`.
- Loudness range: `17,4 LU`.
- True peak: `-6,5 dBFS`.
- O waveform mostra ataques separados por grande parte da cadeia e aumento sustentado de densidade no ultimo quarto; nao identifica sozinho a origem de cada evento.

### Evidencia externa/declarada

- A analise externa descreve clicks, rolagens, impactos, motor, agua, limpadores, vidro, eletronica e musica por 27 beats.
- Tony Davidson declarou que som era importante para expressar `warm engineering`.
- Guardian: Garrison Keillor foi escolhido pela entonacao; a musica visava audiencia mais jovem associada ao Accord.
- shots sustenta o texto final.

### Inferencia

- O som converte microcausalidade visual em materia: peso e material podem ser percebidos mesmo quando a peca e pequena no quadro.
- A analise externa situa aumento/entrada musical perto do payoff, depois de uma longa sequencia descrita como mecanica; sem escuta humana, ordem, predominancia e credibilidade sonora permanecem hipotese corroborativa.
- Locucao resume a experiencia que o filme acabou de demonstrar; se viesse antes, transformaria a cadeia em ilustracao de uma frase.

### Limites

- Sem escuta humana, nao afirmar que cada efeito e captado ao vivo, recriado em foley, sincronizado sample-accurate ou espacializado de modo especifico.
- A analise externa pode identificar incorretamente pecas e sons.
- Medicao de energia nao substitui mix map por stems.

## Produto, estrategia e autoria

### Declarado

- O conceito havia sido rejeitado para Civic e voltou no brief do Accord.
- Honda aprovou a ideia porque reconheceu um problema de engenharia.
- A retrospectiva da marca liga mostrar o carro por dentro a reforcar capacidade de engenharia.
- O full-length de dois minutos teve exibicao premium limitada e depois formatos menores.

### Observado

- Depois do breve lead-in, componentes do carro dominam grande parte do corpo do filme; aparatos externos tambem participam, e o carro completo surge apenas perto de ~01:45.
- Features entram como comportamentos dentro da cadeia, nao como texto sobreposto.
- Nome/modelo e marca chegam depois da prova.

### Inferencia critica

- `Produto tardio` e insuficiente: o carro inteiro surge tarde, enquanto componentes reconheciveis, metaforas materiais e aparatos dividem o corpo do filme. Presenca de peca nao equivale a demonstracao funcional.
- A forma ganha especificidade por usar componentes reconheciveis do Accord, mas precisa separar tres camadas: **demonstracao funcional** (por exemplo, limpadores/sensor), **metafora material** (pecas usadas por peso, forma ou rolamento) e **aparato de producao** (rampas, fios, suportes, agua e estruturas). Trocar o packshot nao remove essa materialidade, mas o filme nao valida literalmente desempenho ou confiabilidade do automovel.
- Mesmo assim, Rube Goldberg e uma forma historica anterior ao filme. Ownership vem da integracao produto-mecanismo-mensagem, nao da alegacao de inventar a cadeia.

## Decisoes reconstruidas

### 1. Fazer o produto contar a historia por suas partes

- `WHAT`: desmontar o Accord e transformar componentes em cadeia causal.
- `WHY_DECLARADO`: Honda reconheceu um problema de engenharia; mostrar o carro por dentro reforcava capacidade de engenharia.
- `EFFECT_OBSERVADO`: componentes reconheciveis ocupam grande parte do filme; algumas features demonstram funcao, muitas pecas operam como metafora material e rampas/fios/suportes como aparato.
- `ALTERNATIVE`: beauty shots do carro pronto, locucao de features ou tabela de atributos.
- `WHY_NOT`: afirmaria engenharia em vez de faze-la acontecer.
- `PRINCIPLE`: quando a promessa e sistemica, classificar cada beat como demonstracao funcional, metafora material ou aparato; somente a primeira pode sustentar prova de funcao.

### 2. Usar continuidade para tornar dependencia visivel

- `WHAT`: acompanhamento lateral percebido como um unico fluxo, com costura invisivel entre duas tomadas.
- `WHY_DECLARADO`: uma unica locacao longa seria proibitiva; o principio deveria continuar parecendo executavel como um sistema.
- `EFFECT_OBSERVADO`: o espectador recebe uma experiencia altamente legivel de transferencia causal, embora costura e pos impeçam trata-la como auditoria forense.
- `ALTERNATIVE`: cobertura multiangulo e montagem de highlights.
- `WHY_NOT`: facilitaria a producao, mas abriria espaco para saltos causais e reduziria a tensao de `vai funcionar?`.
- `PRINCIPLE`: continuidade e uma decisao narrativa quando a promessa depende de reduzir elipses perceptiveis e sustentar experiencia de sistema; mediacoes precisam permanecer explicitas.

### 3. Prototipar antes de comprometer a producao

- `WHAT`: gate de £100 mil/dois carros antes do budget de £1 milhao.
- `WHY_DECLARADO`: provar viabilidade teorica e pratica.
- `EFFECT_DECLARADO`: quase todas as ligacoes desenhadas foram redesenhadas por escala, foco e fisica.
- `ALTERNATIVE`: aprovar storyboard como se fosse especificacao final.
- `WHY_NOT`: papel nao modelava tolerancias reais.
- `PRINCIPLE`: para filmes de mecanismo, previs e storyboard devem produzir hipoteses testaveis; prototipo governa a versao final.

### 4. Integrar pedido de feature ao mecanismo

- `WHAT`: agua ativa limpadores, que movem o parabrisa e continuam a cadeia.
- `WHY_DECLARADO`: Honda pediu features especificas perto da producao.
- `EFFECT_OBSERVADO`: selling point e causa dramatica, nao interrupcao.
- `ALTERNATIVE`: insert separado ou super explicativo.
- `WHY_NOT`: quebraria o contrato de causalidade.
- `PRINCIPLE`: uma exigencia de produto ganha forca quando altera a historia; se apenas pausa o filme, ainda nao foi integrada.

### 5. Aquecer a engenharia pelo som

- `WHAT_DECLARADO/EXTERNO`: buscar assinaturas de material para `warm engineering`; fontes situam musica/voz no payoff, mas esta revisao nao ouviu a entrada nem o mix.
- `WHY_DECLARADO`: comunicar `warm engineering`; voz pela entonacao e musica para rejuvenescer associacao.
- `EFFECT_INFERIDO`: a precisao nao fica clinica; o sistema tem ritmo, peso e humor.
- `ALTERNATIVE`: trilha epica continua ou desenho sonoro esteril.
- `RISK`: sem escuta/stems, a construcao fina permanece hipotese.
- `PRINCIPLE`: som de produto pode carregar personalidade de marca, nao apenas realismo.

## O que nao copiar

- cadeia Rube Goldberg como superficie reconhecivel;
- `plano-sequencia` como trofeu sem necessidade causal;
- pecas aleatorias que nao pertencem ao produto;
- promessa `sem CGI` quando ha costura/cleanup;
- features empurradas como inserts depois da ideia;
- fundo branco chamado de `premium` sem funcao de legibilidade;
- centenas de tentativas como romantizacao de falta de previs;
- equipamento ou lente inventados a partir de credito de DP.

## Perguntas transferiveis para a skill

1. Qual parte da promessa e demonstracao funcional, qual e metafora material e qual depende de aparato de producao?
2. O publico precisa ver cada elo causal ou so o resultado? Por que?
3. Onde a camera precisa estar para conter causa e efeito no mesmo campo de compreensao?
4. Que espacamento, massa, atrito e tempo de reset cada beat exige?
5. Que parte do storyboard e hipotese e qual ja foi prototipada?
6. Uma costura invisivel protege qual promessa narrativa?
7. A feature do cliente muda a historia ou apenas interrompe para ser mostrada?
8. Se o packshot for trocado, o mecanismo ainda pertence especificamente a este produto?
9. O desenho sonoro comunica material, peso e personalidade de marca?
10. Qual e o stop rule de tentativas, budget e seguranca?

## Limites finais

- Nao houve playback critico continuo com imagem e som.
- Movimento persistente, aceleracao, focus pulls, microtiming e sincronismo fino nao podem ser julgados integralmente.
- A costura entre as tomadas esta declarada, mas o frame exato nao foi provado.
- O mapa de som usa IA externa, waveform e fontes; nao escuta humana.
- Camera/lentes/stock/suporte nao foram publicados nas fontes recuperadas.
- Numeros de tentativas e dias divergem; manter atribuicoes separadas.
- O master tem watermark do arquivo One Club.
- A critica independente foi concluida e incorporada com veredito de **nao promocao**; gates 4 e 6 continuam parciais.
