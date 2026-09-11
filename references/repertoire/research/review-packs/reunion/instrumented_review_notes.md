# Google Search — *Reunion*: revisao instrumentada

## Veredito de estado

- Estado maximo: `LEITURA_TECNICA_INSTRUMENTADA_PARCIAL + REVIEW_PACK_BUILT_NOT_WATCHED`.
- Nao autorizar `REVISAO_AV_INSTRUMENTADA`, `VISTO_1X` ou `ANALISE_PROFUNDA`.
- Foram inspecionadas 27/27 folhas densas a 2 fps, 4/4 folhas de candidatos,
  waveform, EBU R128, legenda humana inglesa e nove fontes atomicas.
- Nao houve playback critico continuo nem escuta.

## Identidade da copia

| Campo | Valor |
|---|---|
| Origem | upload oficial Google India, YouTube `gHGDN9-oFJE` |
| Duracao | 212,014 s |
| SHA-256 | `4b7b2186679dd251fab413921b5a1eb0883dd4f3129e522474f4d37b69dc9239` |
| Video | AV1 Main, 1920x1080, 25 fps, BT.709 |
| Audio | Opus stereo, 48 kHz |
| Qualificador | derivado oficial de plataforma; nao mezzanine original |

## Gate `REVISAO_AV_INSTRUMENTADA`

| # | Exigencia | Estado | Evidencia/limite |
|---:|---|---|---|
| 1 | versao, duracao e hash | cumprido para a copia | cortes anteriores e filmes irmaos nao adquiridos |
| 2 | todos os densos | cumprido | 27/27; 424 amostras |
| 3 | todos os candidatos | cumprido como inspecao | 4/4 folhas; 50 candidatos a 0,28 nao sao EDL |
| 4 | inserts, flashes, transicoes e movimento | parcial | 2 fps pode omitir inserts menores que 0,5 s e nao audita movimento |
| 5 | fala corrigida | parcial forte | legenda humana inglesa integralmente lida; sem roteiro, escuta e QA das outras linguas |
| 6 | mapa de som por beats | parcial | waveform, EBU, texto e `silencedetect_-35dB_0.3s.txt`; sem escuta ou cue sheet |
| 7 | EDL manual ou impossibilidade | cumprido pela declaracao | candidatos preservados; contagem final de planos desconhecida |
| 8 | observacao/declaracao/inferencia | cumprido apos fechamento V4 | classes, causalidade e reconhecimento inferido separados da legenda/observacao |
| 9 | critica independente | cumprido apos fechamento V4 | disposicao encerrada; quatro candidatos de governanca liberados sem promocao perceptiva |
| 10 | limites de movimento/som | cumprido | secoes especificas |

## Mapa temporal epistemico

Tempos sao aproximados e nao constituem EDL.

| Tempo | `OBSERVADO_NO_ARTEFATO` | `FONTE_DECLARA` | `INFERENCIA/TESTE` |
|---|---|---|---|
| 00:00–00:03,5 | aereas urbanas e edificio com cupula/minaretes | a retrospectiva diz que imagens reais de Lahore foram obtidas de um DP local | imagem real de local nao prova autoridade cultural; identidade visual da cidade depende de fonte |
| 00:03,5–00:32 | fotografia, diario, homem idoso, mulher mais jovem e interior/balcao | legenda localiza parentesco, memoria de Yusuf, parque, pipas e doces | objetos concretos podem funcionar como pistas pesquisaveis; efeito e causalidade nao medidos |
| 00:32–01:06 | mulher mais jovem usa laptop; inserts mostram Google Search, mapa/imagens, portao, doce e loja | legenda localiza a personagem como neta; cliente/criacao dizem querer Search dentro da historia sem interrompe-la | cada consulta parece reduzir uma incerteza e orientar a proxima acao; fluidez precisa de playback/teste |
| 01:06–01:21 | cidade/loja, telefone e alternancia de espacos | fonte retrospectiva diz que placas de Lahore vieram de DP local | montagem cria ponte geografica aparente; continuidade, ritmo e som nao auditados |
| 01:21–02:18 | alternancia de espacos, telefone e rostos/corpos em reacao aparente | legenda humana cobre apresentacao, doces, mudanca e saudade/Particao | a ligacao pode funcionar como confirmacao humana; Search nao foi validado como causa do contato |
| 02:18–02:33 | pessoa jovem, bagagem e inserts com texto de requisitos de visto/clima | governo indiano documenta excecao relevante para nacionais paquistaneses em 2013 | a UI encenada apresenta informacao; comportamento ao vivo, acuracia, candidatura, espera, aprovacao e risco nao foram validados |
| 02:33–02:55 | taxi/viagem; inserts com texto de clima/status de voo; preparacao da casa | campanha diz integrar funcoes de Search | telas podem marcar logistica na montagem; causalidade e eficacia do produto nao foram validadas |
| 02:55–03:23 | porta, pessoas frente a frente, aproximacao e abraco | legenda localiza falas na porta e repeticao de nomes | surpresa, reconhecimento e culminancia sao interpretacoes; timing exige playback |
| 03:23–03:28 | logo Google em campo claro | upload identifica marca Google Search | marca reivindica papel de mediadora; nao valida reconciliação politica ou efeito social |
| 03:28–fim | epilogo exterior sob chuva com os mais jovens | fonte contemporanea descreve quatro filmes posteriores da campanha | epilogo sugere continuidade, mas relacao e funcao sonora nao foram auditadas |

## Estrategia e arquitetura narrativa

### Fonte declara

- O brief era mostrar o poder da tecnologia e sua diferenca na vida real.
- A criacao queria inserir funcoes de Search sem interromper a historia.
- A equipe descreve uma narrativa longa seguida por quatro filmes mais
  funcionais, e um primeiro corte perto de cinco minutos reduzido a tres.
- A audiencia da inscricao era a populacao online indiana, majoritariamente
  abaixo de 35 anos; isso e target declarado, nao recepcao comprovada.

### Observado nos quadros

- Fotografia/diario, pessoas em dialogo aparente, laptop, telefone, bagagem,
  interfaces, viagem, porta, abraco, logo e epilogo aparecem nessa sucessao.
- A UI visivel mostra consultas/resultados associados a lugar, portao, comida,
  comercio, visto, clima e voo; autenticidade e funcionamento nao foram testados.
- O logo surge depois do reencontro principal, seguido por epilogo.

### Inferencia operacional

- A legenda/fontes permitem testar uma arquitetura que nao seja `tecnologia faz
  milagre`, mas
  `memoria concreta -> consulta -> confirmacao humana -> coordenacao ->
  encontro`. Cada elo deve sobreviver ao teste de causalidade.
- Produto pode servir como camada de coordenacao entre pessoas e instituicoes;
  isso e hipotese narrativa, nao eficacia observada. Se o
  roteiro omite autorizacao, custo, espera ou falha, deve marcar a elipse.
- Como prototipo, longa duracao pode ser defendida por mudancas irreversiveis —
  lembrar, localizar, confirmar, decidir, viajar, reconhecer — e nao pelo
  prestigio de parecer cinema.

## Direcao, decupagem e camera

### Observado nas amostras

- O prologo alterna escala urbana, fotografia/diario e pessoas em aparente
  dialogo; estabilidade e movimento exigem playback.
- Inserts de interface ocupam quadro suficiente para tornar texto e resultado
  identificaveis em amostras selecionadas.
- Telefonemas usam alternancia de espacos e closeups/corpos; perto do final,
  pessoas antes mostradas em espacos diferentes aparecem no mesmo espaco.
- Na sequencia final, pessoas aparecem primeiro a distancia, depois se aproximam
  e se abracam. Separacao, culminancia e reconhecimento sao inferencias.

### Prototipos transferiveis

1. **Memoria pode gerar tokens de acao.** Prototipo abstrato bloqueado neste
   caso ate comparacao com *Respect*; nao copiar o pacote narrativo especifico.
2. **Tela so entra se mudar o proximo ato.** Prototipo a testar: UI visivel nao
   comprova comportamento do produto, acuracia ou causalidade.
3. **Separe informacao de confirmacao.** Resultado de busca sugere; telefonema,
   pessoa, documento ou evento confirma.
4. **Teste co-presenca tardia como hipotese de culminancia.** Se a separacao e
   a premissa, compare uma versao que adia o mesmo espaco com outra que nao o
   faz; os quadros amostrados nao provam payoff nem funcao narrativa.
5. **Nao apague friccao institucional.** Pesquisa pode iniciar um processo; nao
   substitui visto, credito, cuidado clinico, consentimento ou acesso.

### Limites

- Amostras nao autorizam nomear dolly, handheld, slider, lente, filtro, stop,
  velocidade, estabilizacao ou movimento persistente.
- `Closeup`, `campo amplo` e `insert` descrevem aparencia das amostras, nao EDL.
- Camera, lentes, luz, rig e metodologia de continuidade nao foram publicados.

## Fotografia, luz, cor e arte

### Observado

- Interiores de loja apresentam verdes e tons quentes; ambientes de Delhi e
  interfaces frequentemente apresentam neutros/cinza/azulados nas amostras.
- Fotografia/diario, doces, telefone, bagagem, telas, portao e chuva visual sao
  objetos/espacos recorrentes nas amostras.
- Cenarios e matizes variam entre os espacos; funcao de diferenciacao e
  intencao de paleta permanecem inferencia.

### Inferencia/prototipo

- Cor pode separar estado, horario ou familia, mas nunca codificar pais,
  religiao ou cultura sem pesquisa, teste e direcao de arte responsavel.
- Props podem carregar evidencia ou acao: testar se fotografia, doce e bagagem
  mudam compreensao/decisao; recorrencia visual sozinha nao prova funcao.
- Locacao real aumenta especificidade geografica; nao concede voz historica,
  consentimento comunitario ou autenticidade total.

## Performance, casting e representacao

- Os quadros mostram homens em espacos separados antes e co-presentes perto do
  final, com mudancas de posicao e abraco. Reacao, reconhecimento, dependencia
  dramatica, microperformance, pausa e voz permanecem inferencia ou nao auditados.
- A fonte retrospectiva atribui escolhas de casting e uma dinamica de set, mas
  anedota nao e protocolo universal de direcao de atores.
- Nao inferir religiao, nacionalidade, parentesco real ou experiencia da
  Particao pela aparencia dos interpretes.
- Trauma historico exige consulta, direito de contestacao e revisao cultural.
  Historia familiar do diretor e locacao real sao sinais, nao autoridade total.
- A agencia/arquivo nao documentam historiador, sobreviventes, consultor de
  ambos os paises ou avaliacao de dano. Essa ausencia deve permanecer visivel.

## Montagem e duracao

- O detector gerou 50 candidatos, concentrados sobretudo no primeiro minuto e
  em mudancas de espaco/reacao; nao e contagem de planos.
- Como inferencia de estrutura, a sucessao pode ser descrita por oito estados:
  memoria, busca, localizacao, contato, confirmacao, viagem, reconhecimento e
  epilogo. Irreversibilidade e removibilidade nao foram testadas.
- O relato de corte de quase cinco para tres minutos sustenta removibilidade
  como problema real, nao prova que o master e otimo nem que 3:32 e inevitavel.
- Teste de corte: remover um beat e perguntar qual informacao, decisao ou
  consequencia deixa de existir. Atmosfera pode permanecer, mas deve ter funcao
  explicitada e comparada com versao curta.

## Som e musica

- EBU R128: -9,2 LUFS integrado, LRA 10,8 LU e true peak +1,4 dBFS.
- O true peak positivo e um alerta tecnico desta copia derivada; nao diagnostica
  audivelmente clipping sem inspecao adicional e nao define target de entrega.
- `silencedetect` a -35 dB por 0,3 s encontrou apenas 00:00,001–00:01,145958 e
  03:30,990042–03:32,014; comando, versao e eventos foram preservados em
  `silencedetect_-35dB_0.3s.txt`.
- A faixa humana localiza dialogos, mas nao confirma presenca/ausencia, nivel ou
  funcao de musica, ambiente, telefone, chuva, porta ou efeitos.

### Mapa sonoro declarativo, sem escuta

| Beat | Fala localizada | Musica | Ambiente/efeito | Silencio medido | Estado |
|---|---|---|---|---|---|
| 00:00–00:32 | texto de memoria localizado pela legenda em 00:04–00:32 | nao confirmado por beat | nao confirmado | 00:00,001–00:01,146 | presenca sonora alem da legenda desconhecida |
| 00:32–01:10 | nenhuma fala localizada pela faixa inglesa | nao confirmado | UI/ambiente nao confirmados | nenhum | funcao sonora desconhecida |
| 01:10–01:37 | dialogo de telefone localizado | nao confirmado | telefone nao confirmado por escuta | nenhum | hierarquia de mix aberta |
| 01:37–02:07 | nenhuma fala localizada pela faixa inglesa | nao confirmado | nao confirmado | nenhum | funcao sonora desconhecida |
| 02:07–02:17 | fala de Particao/saudade localizada | nao confirmado | nao confirmado | nenhum | alto risco de performance/traducao |
| 02:17–02:55 | pedido ao taxi em 02:46–02:47 | nao confirmado | viagem/UI nao confirmadas | nenhum | transicao logistica nao auditada |
| 02:55–03:22 | falas na porta e repeticao de nomes localizadas pela legenda | nao confirmado | porta/choro/ambiente nao confirmados | nenhum | clímax sonoro nao auditado |
| 03:22–fim | nenhuma fala localizada pela faixa inglesa | nao confirmado | chuva/epilogo nao confirmados | 03:30,990–fim | encerramento desconhecido |

Nenhuma linha autoriza afirmar score ascendente, silencio dramatico, som de
chuva, ringtone, choro, contraponto, sincronismo ou efeito emocional.

## Produto, claim e causalidade

- `UI_DE_GOOGLE_SEARCH_VISIVEL_NA_ENCENACAO`: interfaces, consultas e resultados
  aparecem nas amostras; nao se verificou execucao ao vivo ou composicao.
- `FONTE_DECLARA_INTEGRACAO_DE_FUNCOES_DE_SEARCH`: a campanha queria mostrar
  Search como ferramenta util na vida.
- `COMPORTAMENTO_AO_VIVO_ACURACIA_E_CAUSALIDADE_NAO_VALIDADOS`: pessoas
  formulam, interpretam, ligam, decidem, viajam e recebem; regras
  de visto e transporte continuam externas ao produto.
- Recusar `Search reuniu dois paises`, `Search aprovou a viagem` ou `a campanha
  reconciliou India e Paquistao`. Sao extrapolacoes politicas/causais.

## Originalidade, direitos e anterioridade

- Ha alegacao publica secundaria de semelhanca com o curta paquistanes
  *Respect* (2012).
- A fonte documenta a alegacao, nao prova copia ou inocencia. Nao ha resposta
  conclusiva, roteiro datado ou parecer juridico neste corpus.
- Antes de usar a estrutura como referencia: buscar/analisar a obra anterior,
  mapear elementos comuns/especificos, registrar transformacao e submeter a
  revisao juridica humana. Nao copiar Particao, amigo perdido, descendente que
  busca e reencontro digital como pacote narrativo.

## Principios candidatos para Atlas, ainda bloqueados

1. `MEMORY_TO_SEARCHABLE_TOKENS` — prototipo abstrato bloqueado pela
   anterioridade; nunca reutilizar o pacote Particao + amigo + descendente +
   busca + reencontro a partir deste caso.
2. `PRODUCT_AS_COORDINATION_LAYER_NOT_MIRACLE` — mapear pessoas, produto e
   instituicoes como elos separados.
3. `SEARCH_UI_ONLY_WHEN_STATE_CHANGES` — prototipo; funcao/causalidade e economia
   de montagem ainda nao testadas.
4. `HISTORICAL_TRAUMA_REQUIRES_AUTHORITY_AND_FRICTION` — consulta, contestacao,
   direitos e friccao real sao gates, nao acabamento.
5. `LONG_FORM_EARNS_TIME_BY_IRREVERSIBLE_STATE_CHANGE` — prototipo pendente de
   playback, EDL, comparacao de versoes e teste de remocao.
6. `ACTUAL_LOCATION_IS_NOT_CULTURAL_AUTHORITY` — placa real prova lugar
   capturado, nao valida representacao.
7. `VIRAL_RESPONSE_IS_NOT_CONSENSUS` — views/comentarios nao provam acordo,
   impacto social ou ausencia de dano.

Recusar: query como aprovacao institucional, produto como reconciliador
politico, cidade real como autoridade cultural, emocao da equipe como audiencia,
viralidade como consenso e originalidade sem busca de anterioridade.

## Pendencias antes de qualquer promocao

- critica independente e disposicao;
- playback continuo com imagem e som ou manutencao explicita dos gates 4/6;
- revisao humana de hindi/urdu e contexto historico dos dialogos;
- mapa de direitos/originalidade com *Respect* e resposta dos autores;
- fonte primaria de creditos completos e DP de Lahore;
- evidencia de consulta cultural/historica ou registro honesto de ausencia.
- clearance/acuracia para UI, telefones, enderecos, comercio, mapas, voo e dados
  identificaveis; em novo projeto usar dados licenciados/ficticios e revisao legal.

## Disposicao da critica independente

- `P0.1–P0.3`: aceitos; observado, legenda e inferencia foram separados, UI foi
  classificada como encenacao sem eficacia validada e claims de performance/
  ausencia de fala foram removidos.
- `P0.4`: aceito; estrutura especifica permanece bloqueada ate aquisicao e
  comparacao integral de *Respect*, transformacao documentada e revisao juridica.
- `P0.5`: aceito; estado `REPRESENTACAO_HISTORICA_E_SEGURANCA_CULTURAL_NAO_VALIDADAS`.
  O caso ensina governanca, nao um modelo positivo da Particao ou do visto.
- `P1.1–P1.2`: aceitos; estabilidade saiu do observado e cor/props viraram
  inferencias/testes.
- `P1.3`: aceito; artefato bruto de `silencedetect` foi preservado, sem promover
  gate 6.
- `P1.4`: aceito; longa duracao e estados irreversiveis sao prototipos.
- `P1.5`: aceito; creditos permanecem parciais e cargo nao atribui decisao.
- `P1.6`: aceito; UI/dados exigem clearance, acuracia e revisao legal.
- `P1.7`: mantido; audiencia, premio, viralidade e versoes seguem limitados.
- Candidatos seguros somente apos reauditoria: itens 2, 4, 6 e 7. Itens 1, 3,
  5 e todos os efeitos formais permanecem prototipos.
- Gates 4/5/6 e estado global permanecem parciais; gates 8/9 aguardam
  reauditoria desta disposicao.
