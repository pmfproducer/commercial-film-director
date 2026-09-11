# Dollar Shave Club — *Our Blades Are F***ing Great*: revisao instrumentada

## Veredito de estado

- Estado maximo: `LEITURA_TECNICA_INSTRUMENTADA_PARCIAL + REVIEW_PACK_BUILT_NOT_WATCHED`.
- Nao autorizar `REVISAO_AV_INSTRUMENTADA`, `VISTO_1X` ou `ANALISE_PROFUNDA`.
- Motivo: 24/24 folhas densas a 4 fps, 1/1 folha de candidatos, waveform, EBU,
  legenda automatica e seis fontes foram inspecionados; nao houve playback
  critico continuo, escuta nem transcricao humana. A critica independente V1 e
  a reauditoria V2 foram realizadas; a disposicao V2 ainda exige os ajustes
  semanticos registrados ao fim desta ficha.

## Identidade da copia

| Campo | Valor |
|---|---|
| Origem | upload oficial Dollar Shave Club, YouTube `ZUG9qYTJMsI` |
| Duracao | 93,114 s |
| SHA-256 | `b13ab47ad250393763084b327e3876db5e571fa01c6922e63c52309e6310a337` |
| Video | AV1 Main, 1920x1080, 24000/1001 fps, BT.709 |
| Audio | Opus stereo, 48 kHz |
| Qualificador | derivado oficial de plataforma; nao mezzanine original |

## Artefatos inspecionados

- 372 amostras a cada 0,25 s em 24 folhas, cobrindo a copia inteira.
- Sete candidatos algoritmicos a threshold 0,28 em uma folha; nao sao EDL.
- Waveform integral, EBU R128 e `silencedetect` preservado.
- Legenda automatica inglesa, integralmente lida e resumida.
- Fontes: upload oficial; entrevista de processo com Aniello/Dubin; entrevista
  de producao com Dubin; pagina SpotCast; premio Digiday; perfil de metodo Inc.

## Gate `REVISAO_AV_INSTRUMENTADA`

| # | Exigencia | Estado | Evidencia/limite |
|---:|---|---|---|
| 1 | versao, duracao e hash | cumprido para a copia | mezzanine original aberto |
| 2 | todos os densos | cumprido | 24/24; 372 amostras |
| 3 | todos os candidatos | cumprido | 1/1 folha; 7 candidatos algoritmicos |
| 4 | inserts, flashes, transicoes e movimento | parcial | 4 fps integral; movimento, whip, continuidade e microcortes exigem playback/microamostragem |
| 5 | fala corrigida | parcial | legenda automatica resumida; texto exato, censura, performance e letra abertos |
| 6 | mapa de som por beats | parcial | waveform/EBU/legenda; sem escuta ou cue sheet |
| 7 | EDL manual ou impossibilidade | cumprido pela declaracao | detector nao permite contagem exata |
| 8 | observacao/declaracao/inferencia | cumprido apos disposicao V4 | galpao/operacao, papeis, safety e provenance separados; ultimo residuo de identidade removido |
| 9 | critica independente | cumprido apos disposicao V4 | tres candidatos de governanca liberados; estado perceptivo permanece parcial |
| 10 | limites de movimento/som | cumprido | secoes explicitas |

## Mapa temporal epistemico

Tempos sao aproximados e nao constituem EDL.

| Tempo | `OBSERVADO_NO_ARTEFATO` | `FONTE_DECLARA` | `INFERENCIA/TESTE` |
|---|---|---|---|
| 00:00–00:09,25 | homem/porta-voz aparente sentado diante de mesa; parede de pequenos produtos/objetos; enquadramento muda para ele em pe | upload/fontes identificam Michael Dubin como performer e fundador; legenda localiza apresentacao, assinatura, entrega e preco | rosto do porta-voz pode reduzir distancia, mas efeito e brand trust nao foram medidos |
| 00:09,25–00:17,75 | homem/porta-voz aparente muda de posicao em espaco de aparencia industrial; plano se amplia; cartaz vermelho com a frase central aparece | fontes identificam Dubin e atribuem a Aniello/Dubin a frase e o metodo mensagem-antes-de-gags | movimento pelo espaco pode transformar pitch em visita; persistencia e timing exigem playback |
| 00:17,75–00:23,5 | pano/objeto laranja cruza ou envolve a figura; produto aparece na mao | legenda enumera componentes do barbeador | gag e detalhe podem dividir atencao; testar recordacao de feature e oferta |
| 00:23,5–00:32 | crianca aparente, pessoa sentada, creme/espuma e raquete/bola aparecem em profundidade | legenda inclui claim de crianca, preco de concorrentes e referencia a Federer | `MINOR_IS_NOT_PRODUCT_SAFETY_EVIDENCE`; safeguarding, guardian, release e compreensao nao validados |
| 00:32–00:44,75 | homem/porta-voz aparente junto a empilhadeira; fala direta; fundo industrial e retrato | fontes identificam o performer como Dubin; legenda satiriza recursos de barbeadores e inclui piada sobre poliomielite | pausa espacial pode priorizar argumento verbal; dano/capacitismo e claim comparativo exigem revisao |
| 00:44,75–00:54,5 | novo trecho de espaco industrial; mulher em uniforme azul, caixas/objetos, objeto longo de aparencia laminada e mudanca rapida de campo aparecem | legenda pede parar de pagar por tecnologia e nomeia a mulher como Alejandra dentro do discurso de envio | aparente corte pode dividir tese de produto e operacao; material/fio/coreografia, papel, consentimento e safety nao validados |
| 00:54,5–00:57,5 | figura em fantasia de urso ocupa o quadro; o homem/porta-voz aparente nao aparece em parte das amostras | legenda tem lacuna e depois retoma venda/empregos | gag sem porta-voz pode pontuar estrutura, mas funcao sonora e removibilidade nao foram testadas |
| 00:57,5–01:07,75 | homem/porta-voz aparente e mulher em uniforme azul aparecem em pequeno veiculo com rodas; caixas/pallets; depois o homem aparece entre pilhas | fontes identificam o performer como Dubin; legenda fala de empregos e nomeia Alejandra | deslocamento/operacao exigem playback; `WORKER_ROLE_CONSENT_COMPENSATION_AND_RELEASE_NOT_VALIDATED` |
| 01:07,75–01:22,0 | homem/porta-voz aparente avanca entre caixas; bandeira dos EUA, fantasia, dinheiro/confete e luz magenta/vermelha entram | fontes identificam o performer como Dubin; legenda retoma economia, dominio e festa | acumulacao pode converter promessa em celebracao; simbolos nacionais e dinheiro nao provam impacto economico |
| 01:22,0–fim | preto; pergunta em tipografia branca; logo, dominio e tagline em cartelas | descricao oficial identifica marca; legenda marca musica | cartelas concentram atribuicao/CTA; legibilidade, duracao e musica exigem playback/teste |

## Problema, estrategia e arquitetura

### Fonte declara

- Dubin formula o problema como preco alto, deslocamento, esquecimento e friccao
  para comprar laminas em lojas.
- Aniello relata reducao de um roteiro de quatro paginas ate restar mensagem
  essencial; as piadas foram escritas sobre esse esqueleto.
- Dubin descreve o video como historia engraçada com proposito, nao somente
  conteudo engraçado.
- O filme serviu simultaneamente a lancamento, captacao e compartilhamento; isso
  e contexto declarado, nao causalidade comprovada.

### Observado nas amostras

- A oferta e apresentada por um homem/porta-voz aparente antes da circulacao
  por um espaco de aparencia industrial. Upload e fontes, nao os quadros,
  identificam Michael Dubin como performer e fundador.
- Produto, cartaz, caixas, mulher em uniforme azul, maquinario, props, bandeira,
  dinheiro/confete e cartelas finais aparecem em sucessao.
- A frase central aparece visualmente cedo; o dominio/logo retornam no final.

### Inferencia operacional

- O artefato mostra apenas `WAREHOUSE_IMAGERY`: galpao aparente, caixas,
  pallets, mesas e maquinario. Dubin declara que era o armazem original de
  fulfillment; propriedade, data, operacao durante o take, estoque, emprego,
  capacidade e pedidos ficam em
  `OPERATIONAL_STATUS_CAPACITY_AND_FULFILLMENT_NOT_VALIDATED`.
- A estrutura candidata alterna `claim verbal -> gag visual -> proximo claim`.
  Cada gag precisa passar teste de compreensao: reforca, contrasta, pontua ou
  apenas compete com a oferta?
- `CEO em quadro` e casting de risco: funciona apenas se autoridade de marca,
  performance, disponibilidade, representacao e continuidade forem melhores que
  uma alternativa; fundador nao e regra.

## Direcao, decupagem e camera

### Observado em amostras

- Abertura usa composicao relativamente fixa em mesa; depois a escala e o fundo
  mudam enquanto o homem/porta-voz aparente ocupa frequentemente centro/proximo
  do centro. Fontes externas, nao os quadros, o identificam como Dubin.
- Gags aparecem tanto junto dele quanto em profundidade ou apos ele sair do
  quadro.
- Ha mudanca forte entre ~00:44,75 e ~00:45 e entrada de cartela em ~01:22;
  sete candidatos nao fecham a contagem real de cortes.
- As amostras sugerem acompanhamento pelo corredor e mudanca rapida perto da
  lamina/urso; nao autorizam nomear dolly, steadicam, handheld, whip pan ou take
  continuo.

### Prototipos transferiveis

1. **Ancore a oferta antes do primeiro desvio.** O espectador deve conseguir
   reconstruir produto, preco/mecanismo e proxima acao antes de receber gags.
2. **Escreva humor sobre o esqueleto da mensagem.** Para cada gag, registre
   claim associado, ganho de memoria, risco de distracao e versao sem gag.
3. **Use profundidade como segunda pista, nao segunda historia.** Acao de fundo
   precisa continuar legivel sem sequestrar fala, produto ou seguranca.
4. **Movimento deve comprar evidencia.** Cada mudanca de posicao precisa revelar
   produto, operacao, personagem ou consequencia; aparencia de energia nao basta.
5. **Quebre o fluxo quando a tese mudar.** Um corte ou pausa pode separar valor,
   operacao e CTA; a obra nao prova qual foi a intencao de cada transicao.

### Limites

- Nenhuma fonte lida publica camera, lente, suporte, filtro, stop, rig, foco,
  operador ou metodologia de continuidade.
- Quatro quadros por segundo nao fecham velocidade, aceleracao, estabilidade,
  microtiming, eixo, raccord, foco ou existencia de costuras.

## Fotografia, luz, cor e arte

### Observado

- Espaco de aparencia industrial fornece fluorescentes aparentes, caixas,
  pallets, empilhadeira, corredores e variedade de objetos.
- A base visual e relativamente neutra/quente; laranja e vermelho/magenta
  aparecem em props, cartaz e sequencia final.
- Figurino principal e camisa clara com gravata escura; cartelas finais usam
  preto, branco e vermelho.

### Inferencia/prototipo

- Espaco industrial declarado pelo participante como armazem original pode
  unificar arte e argumento, mas imagem nao valida operacao. Ruido visual,
  marcas, safety e continuidade de objetos exigem controle proprio.
- Cor de acento pode sinalizar gag, claim ou fase; intencao de paleta e grade
  nao foram publicadas e efeito precisa de teste.
- Aparencia simples nao prova ausencia de iluminacao, arte, ensaio ou pos. O
  relato de baixo caixa nao deve virar estetica de descuido.

## Performance, casting e comedia

- Um homem/porta-voz aparente aparece falando para a camera e se deslocando por
  ambientes; fontes o identificam como Dubin. Entrega,
  pausas e timing nao foram ouvidos/reproduzidos.
- A fonte associa sua formacao de improvisacao a escuta, contraste e decisao
  rapida; isso e metodo declarado, nao eficacia demonstrada.
- Mulher em uniforme azul, crianca aparente, pessoa sentada, pessoa na area do
  operador, duas pessoas em pequeno veiculo com rodas e performer em fantasia
  aparecem; identidade, papeis, movimento, releases, compensacao e condicoes de
  trabalho nao foram publicados. A legenda nomeia a mulher como Alejandra.
- `Deadpan`, autocritica e subversao de linguagem de marca sao intencoes
  declaradas/leituras a testar, nao licenca para humilhar trabalhador, crianca,
  pessoa com deficiencia ou doenca.
- Estados formais: `DISABILITY_REPRESENTATION_REVIEW_NOT_PERFORMED`,
  `MINOR_IS_NOT_PRODUCT_SAFETY_EVIDENCE` e
  `WORKER_ROLE_CONSENT_COMPENSATION_AND_RELEASE_NOT_VALIDATED`.
- Recusa formal: nunca extrair polio, deficiencia, avo ou corpo como marcador de
  atraso/inferioridade; memoria ou premio nao compensam desumanizacao. Humor que
  usa doenca, mobilidade, corpo ou tecnologia assistiva exige revisao liderada
  por pessoas com deficiencia.
- Recusa formal: crianca nao substancia suavidade/seguranca; Alejandra,
  desemprego, sorriso aparente ou participacao nao provam emprego, consentimento,
  compensacao, equidade ou dignidade.

## Producao, budget e safety

- Dubin declara cerca de US$ 4.500 e aproximadamente oito horas no local que
  chama de armazem original em Gardena. Classificacao:
  `PARTICIPANT_REPORTED_APPROXIMATE_CASH_OUTLAY_NOT_AUDITED`.
- O relato nao estabelece se favores, salarios de mercado, equipamento, pos,
  musica, seguro, direitos, oportunidade ou infraestrutura do armazem estavam
  incluidos; composicao e custos in-kind permanecem desconhecidos.
- Estados formais: `SAFETY_CASE_NOT_ACQUIRED_OR_VALIDATED`,
  `CHILD_SAFEGUARDING_GUARDIAN_RELEASE_NOT_VALIDATED`,
  `FORKLIFT_OPERATOR_LOCKOUT_AND_EXCLUSION_ZONE_NOT_VALIDATED`,
  `BLADED_OBJECT_MATERIAL_EDGE_CHOREOGRAPHY_NOT_VALIDATED` e
  `WHEELED_PROP_AND_STACKED_LOAD_SAFETY_NOT_VALIDATED`.
- Empilhadeira, pessoa na area do operador, objeto longo de aparencia laminada,
  crianca aparente, pequeno veiculo com rodas, cargas e coreografia multipessoa
  exigem coordenacao, zona de exclusao, operador habilitado, material seguro,
  guardian/release, autoridade de stop e alternativa. Nao se afirma que
  maquinario estava ativo, que o veiculo se movia ou que o objeto tinha fio.
- Nunca converter o precedente em instrucao de arma, maquinario ou trabalho com
  crianca. `Parece barato` nao autoriza reduzir safety.

## Montagem e removibilidade

- Sete candidatos concentram-se em ~00:09,38, 00:17,89, 00:32,03, 00:44,88,
  00:57,39, 01:07,94 e 01:22,04; sao diferencas visuais, nao EDL.
- O metodo publicado oferece teste forte: mensagem essencial primeiro e
  remocao do que nao tiver razao/ponto. A ficha nao presume que cada frame final
  passa nesse teste.
- Prototipo de paper edit: para cada unidade, marcar `CLAIM`, `GAG`, `PROVA
  ENCENADA`, `TRANSICAO`, `CTA` e `RISCO`; retirar a unidade e medir o que deixa
  de ser entendido ou lembrado.
- Longos trechos de aparente continuidade podem deslocar cortes para blocking e
  movimento; sem playback nao ha conclusao sobre ritmo, takes ou raccord.

## Som e musica

- EBU R128: -12,8 LUFS integrado, LRA 11,5 LU, true peak +1,3 dBFS.
- True peak positivo e alerta desta copia derivada, nao diagnostico audivel de
  clipping nem target de entrega.
- `silencedetect` a -35 dB/0,3 s encontrou 18 intervalos, sobretudo pausas
  curtas antes de 00:16,5; medicao nao identifica silencio perceptivo.
- A descricao oficial credita *Karate*, de Kennedy. Credito nao e cue sheet,
  licenca auditada ou prova de presenca por beat.
- A legenda automatica marca musica em ~01:17,6; letra e limites permanecem
  incertos. Voz, ambiente, props, rodas, maquinario e efeitos nao foram ouvidos.

### Mapa sonoro declarativo, sem escuta

| Beat | Fala localizada pela legenda automatica | Musica | Ambiente/efeito | Silencio medido | Estado |
|---|---|---|---|---|---|
| 00:00–00:17,75 | apresentacao/oferta/frase central | nao confirmada por beat | nao confirmado | dez intervalos curtos ate 00:16,43 | timing vocal nao auditado |
| 00:17,75–00:32 | features/crianca/preco/Federer | nao confirmada | props nao confirmados | 00:30,13–00:30,60 | claim e humor sem escuta |
| 00:32–00:44,75 | excesso de features/avo/polio | nao confirmada | nao confirmado | nenhum acima do threshold | entrega e dano abertos |
| 00:44,75–00:57,5 | tecnologia/compra/envio, com lacuna | nao confirmada | lamina/urso nao confirmados | quatro intervalos 00:47–00:56,67 | transicao/gag nao auditados |
| 00:57,5–01:07,75 | empregos/Alejandra/trocadilho | nao confirmada | pequeno veiculo/galpao nao confirmados | dois intervalos 01:05,63–01:07,25 | dialogo exato aberto |
| 01:07,75–01:17,6 | economia/dominio/festa | nao confirmada | dinheiro/confete nao confirmados | 01:15,74–01:16,05 | crescendo nao inferido |
| 01:17,6–fim | letra automatica de baixa confianca | faixa oficial creditada; presenca geral sugerida pela legenda | nao confirmado | nenhum acima do threshold | musica/CTA exigem escuta e rights |

## Produto, claims, legal e atribuicao

- `HISTORICAL_OFFER_COPY`: US$ 1/mes e entrega pertencem ao filme de 2012.
- `TERMS_SHIPPING_PLANS_ELIGIBILITY_NOT_ACQUIRED`.
- `PRODUCT_FEATURE_AND_QUALITY_CLAIMS_NOT_SUBSTANTIATED`.
- `CHILD_SMOOTHNESS_OR_SAFETY_CLAIM_NOT_SUBSTANTIATED`.
- `COMPETITOR_PRICE_AND_FEATURE_COMPARISON_NOT_SUBSTANTIATED`.
- `FEDERER_NAME_PERSONALITY_TRADEMARK_CLEARANCE_NOT_AUDITED`.
- `JOB_CREATION_QUANTITY_QUALITY_AND_CAUSALITY_NOT_VALIDATED`: imagem de mulher
  e galpao nao prova emprego novo, condicao, quantidade ou causalidade.
- `REPORTED_OUTCOMES_WITH_PR_PAID_SEARCH_OFFER_PRODUCT_TIMING_AND_SITE_CONFOUNDERS`:
  views, cadastros, premio, crash, captacao e crescimento sao resultados
  reportados sem experimento de incrementalidade ou contrafactual.

## Principios candidatos para Atlas, ainda sem promocao

1. `MESSAGE_BONES_BEFORE_COMEDY` — prototipo bloqueado: declaracao localizada em
   texto integral recuperado por indice, sem captura direta, roteiros ou paper edit.
2. `GAG_REQUIRES_CLAIM_AND_REMOVABILITY_RECORD` — cada gag precisa declarar
   claim, funcao, risco e alternativa sem gag; sintese a testar.
3. `WAREHOUSE_IMAGERY_IS_NOT_OPERATIONAL_OR_PRODUCT_PROOF` — candidato seguro:
   imagem de galpao e declaracao participante nao provam operacao, capacidade,
   emprego, qualidade, estoque ou fulfillment.
4. `LOW_CASH_COST_IS_NOT_REPLICABLE_PRODUCTION_COST` — o relato de caixa nao
   estabelece se talento, favores, infraestrutura, oportunidade e demais
   custos in-kind estavam incluidos; composicao e custo replicavel permanecem
   desconhecidos.
5. `FOUNDER_AS_CAST_IS_A_TEST_NOT_DEFAULT` — autoridade de marca precisa vencer
   alternativas em performance, risco, disponibilidade e representacao.
6. `COMEDY_TRAINING_IS_NOT_UNPLANNED_IMPROVISATION` — improvisacao profissional
   usa escuta, parceria e preparacao; nao autoriza set solto.

Itens 3, 4 e 6 foram liberados pela reauditoria V4 como candidatos seguros de
governanca. Itens 1, 2 e 5,
uso de profundidade, acentos cromaticos, fluxo pelo galpao e CTA tardio
permanecem prototipos. Recusar formalmente: polio/deficiencia/corpo como atraso;
crianca como prova de seguranca; Alejandra/desemprego/trabalhador como punchline
ou prova de emprego; objeto/maquinario/cargas como receita low-budget; galpao
como validacao; baixo caixa como desculpa de safety; outcome como causalidade.

## Pendencias

- critica independente e reauditorias V2, V3 e V4 realizadas; Gates 8/9
  fechados documentalmente sem promocao do estado audiovisual;
- playback continuo ou manutencao explicita de Gates 4/6 parciais;
- transcricao/roteiro humano e aquisicao do episodio SpotCast;
- ficha completa de producao, DP, arte, montagem, som, cor e rights;
- safety/insurance/release e verificacao historica de oferta/claims.

## Disposicao da critica independente

- `P0.1`: aceito; imagem de galpao, declaracao de Dubin e operacao nao validada
  foram separadas.
- `P0.2`: aceito; cinco estados formais de safety registrados sem acusar
  movimento, fio, acidente ou imprudencia nao observados.
- `P0.3`: aceito; capacitismo virou recusa de extracao e gate disability-led.
- `P0.4`: aceito; crianca e Alejandra nao sao prova de produto, emprego,
  consentimento, compensacao ou equidade.
- `P0.5`: aceito; Yahoo/Entrepreneur esta qualificado como texto integral
  recuperado via indice com direct open 429; claims de metodo permanecem
  declaracoes localizadas, nao auditoria integral. SpotCast segue nao ouvido.
- `P1.1–P1.6`: aceitos; cash outlay, claims, outcomes, EDL, timing/som e creditos
  receberam classes/limites explicitos.
- `P2.1–P2.6`: aceitos; identidades, objeto, veiculo, true peak e musica foram
  reescritos sem extrapolacao.
- A reauditoria V2 aceitou a maior parte da disposicao e encontrou quatro
  residuos: identidade em campos observados, composicao desconhecida do caixa,
  separacao entre valor e duracao e estado da critica. Estes residuos foram
  corrigidos nesta versao. Atlas 3 e 6 permanecem candidatos seguros; 4 so pode
  ser considerado apos verificacao desta nova redacao; 1, 2 e 5 seguem
  prototipos. Gates 4/5/6 e estado global permanecem parciais.
