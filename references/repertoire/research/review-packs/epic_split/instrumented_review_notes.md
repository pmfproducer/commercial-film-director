# Volvo Trucks — *The Epic Split*: revisao instrumentada

## Veredito de estado

- Estado maximo: `LEITURA_TECNICA_INSTRUMENTADA_PARCIAL + REVIEW_PACK_BUILT_NOT_WATCHED`.
- Nao autorizar `REVISAO_AV_INSTRUMENTADA`, `VISTO_1X` ou `ANALISE_PROFUNDA`.
- Motivo: 20/20 folhas densas a 4 fps, waveform, EBU, legenda humana e seis
  fontes foram inspecionados; nao houve playback critico continuo nem escuta.

## Identidade da copia

| Campo | Valor |
|---|---|
| Origem | upload oficial Volvo Trucks, YouTube `M7FIvfx5J10` |
| Duracao | 76,720 s |
| SHA-256 | `1347b93aed1b019981b278895c6085f73a7f2535e861a624fcd9d07243bfc0ba` |
| Video | AV1 Main, 1920x1080, 25 fps, BT.709 |
| Audio | Opus stereo, 48 kHz; stream mede 76,694 s |
| Qualificador | derivado oficial de plataforma; nao mezzanine original |

## Artefatos inspecionados

- 307 amostras a cada 0,25 s em 20 folhas, cobrindo 00:00–01:16,5.
- Detector de mudanca a 0,28 gerou zero candidatos; isso nao prova ausencia de
  corte, costura ou limpeza digital.
- Waveform integral, EBU R128 e `silencedetect`.
- Legenda humana inglesa do upload oficial.
- Fontes: copia oficial, motorista, tecnologia Volvo, diretor/ADA, campanha da
  agencia e creditos Vimeo.

## Gate `REVISAO_AV_INSTRUMENTADA`

| # | Exigencia | Estado | Evidencia/limite |
|---:|---|---|---|
| 1 | versao, duracao e hash | cumprido para a copia | mezzanine original aberto |
| 2 | todos os densos | cumprido | 20/20; 307 amostras |
| 3 | todos os candidatos | cumprido por ausencia declarada | zero a threshold 0,28; algoritmo nao e EDL |
| 4 | inserts, flashes, transicoes e movimento | parcial | cobertura 4 fps integral; movimento realizado e costuras sao centrais e exigem playback |
| 5 | fala corrigida | parcial | resumo temporal de legenda humana; transcricao integral, performance e musica nao auditadas |
| 6 | mapa de som por beats | parcial | waveform/EBU/texto; sem escuta de voz, musica, motores ou mix |
| 7 | EDL manual ou impossibilidade | cumprido pela declaracao | uma composicao aparente mais cartelas; sem contagem de planos final |
| 8 | observacao/declaracao/inferencia | cumprido apos fechamento V3 | comparabilidade, cor, one-take, demo e efeitos mantidos em classes limitadas |
| 9 | critica independente | cumprido apos fechamento V3 | parecer e reauditorias V2/V3 em `research/reviews/`; estado perceptivo permanece parcial |
| 10 | limites de movimento/som | cumprido | secoes especificas |

## Mapa temporal epistemico

Tempos sao aproximados; nao constituem EDL.

| Tempo | `OBSERVADO_NO_ARTEFATO` | `FONTE_DECLARA` | `INFERENCIA/TESTE` |
|---|---|---|---|
| 00:00–00:09,2 | rosto central, olhos fechados, camisa azul, superficies douradas e sol baixo | legenda localiza a fala autobiografica desde 00:03,3 | reter informacao espacial pode transformar revelacao em pergunta; efeito de audiencia nao medido |
| 00:09,25–00:17,7 | olhos abrem; escala e recorte variam pouco | legenda continua a construcao da persona | olhar para a camera pode marcar passagem de memoria para desafio; depende de performance nao ouvida |
| 00:17,75–00:31,9 | campo se amplia progressivamente; laterais de dois caminhoes, corpo e depois frentes tornam-se visiveis | legenda anuncia corpo/pernas e o split | a revelacao visual responde a fala sem corte detectado; mecanismo de camera ou pos desconhecido |
| 00:32–00:47,7 | caminhoes se afastam lateralmente; pernas passam de abertura moderada ao split; figura permanece central | motorista relata uma linha externa como limite de seguranca e oito dias de ensaio | uma unica variavel visual — distancia — carrega risco, produto e progressao dramatica; nao e teste independente |
| 00:48–00:59,4 | separacao reduz gradualmente; figura e veiculos diminuem no quadro; sol permanece no eixo lateral | Volvo descreve manutencao de distancia e separacao em marcha a re | retorno fecha a acao e prepara atribuicao; direcao exata dos veiculos/camera exige playback |
| 00:59,5–01:08,5 | cartela de produto sobre caminhoes; distancia continua a mudar nas amostras | cartela e Volvo nomeiam estabilidade/precisao do Dynamic Steering | a marca nomeia a tese depois da demonstracao encenada; legibilidade temporal nao testada |
| 01:08,75–01:12,5 | cartela some; imagem escurece ate preto | nenhuma fonte primaria explica o timing do fade | descompressao antes do aviso; funcao sonora desconhecida |
| 01:12,75–fim | cartela branca em preto informa profissionais e area fechada | legenda oficial confirma o aviso | safety e parte da comunicacao, mas cartela tardia nao substitui projeto seguro |

## Conceito e estrategia

### Fonte declara

- A agencia queria ampliar alcance B2B para compradores e influenciadores com
  testes extremos de atributos relevantes, distribuidos por YouTube e PR.
- Nilsson queria deslocar a serie de um registro documental para algo emocional
  e poetico, descrito por ele como haicai visual.
- A Volvo associa a acao a estabilidade e precisao do Dynamic Steering.

### Observado

- Pessoa, caminhoes, estrada, sol e cartelas compoem quase todo o campo visual.
- A tese tecnica aparece em texto apenas depois da acao principal.
- O split e reversivel: abre ate um maximo e depois reduz enquanto a escala se
  torna mais ampla.

### Inferencia operacional

- O stunt nao e assunto paralelo: sua variavel dramatica observavel e a distancia
  lateral, que a marca reivindica controlar em marcha a re. A relacao e
  retorica/encenada, nao validacao tecnica.
- A celebridade cria uma medida corporal intuitiva da separacao, mas tambem pode
  capturar mais memoria que o sistema; brand linkage precisa ser testado.
- O filme oferece `DEMONSTRACAO_DE_PRODUTO_ENCENADA`, nao prova independente de
  eficacia, seguranca, superioridade ou causalidade comercial.
- Classes obrigatorias: `CLAIM_DA_VOLVO`, `DEMONSTRACAO_ENCENADA_OBSERVAVEL` e
  `VALIDACAO_INDEPENDENTE_AUSENTE`. O nome "test" da serie nao funde as tres.

## Direcao, decupagem e camera

### Observado em amostras

- Abertura central e simetrica, primeiro estreita e depois progressivamente
  ampla; a pessoa permanece no eixo entre massas semelhantes.
- Estrada e caminhoes fornecem linhas convergentes; o sol baixo permanece no
  lado esquerdo do quadro.
- A distancia entre os caminhoes abre e volta a reduzir sem corte detectado.
- A cartela de produto preserva a imagem da acao como fundo; a de seguranca
  recebe quadro preto separado.

### Decisoes transferiveis como prototipo

1. **Escolha uma variavel visual ligada ao claim.** Direcao, distancia,
   deformacao, tempo ou peso podem mudar na encenacao; isso comunica a
   propriedade reivindicada, mas nao a valida.
2. **Atrase a explicacao, nao a causalidade.** A acao pode vir antes da cartela
   se o que muda ja estiver conectado ao atributo que sera nomeado.
3. **Revelacao deve liberar informacao.** Cada ampliacao de campo precisa revelar
   corpo, maquina, risco ou escala; movimento sem nova informacao e decoracao.
4. **Plano aparente longo exige coreografia de producao.** Blocking, veiculos,
   camera, tempo de luz, performance, rig, seguranca e contingencia formam uma
   decisao unica; nenhum departamento resolve sozinho.

### Limites

- Amostras indicam mudanca progressiva de escala, nao autorizam nomear dolly,
  zoom, crane, rig, estabilizacao, velocidade ou costura.
- O rótulo permitido e `COMPOSICAO_APARENTEMENTE_CONTINUA_EM_AMOSTRAS` junto de
  `UMA_TOMADA_COM_O_PERFORMER_SEGUNDO_O_MOTORISTA`. Zero candidatos e o relato
  nao provam arquivo final sem cortes invisiveis, cleanup ou VFX.
- Camera, lente, filtros, stop e suporte nao foram publicados nas fontes lidas.

## Fotografia, luz, cor e arte

### Observado

- Paleta dominante: ouro/bege dos caminhoes e ambiente, azul/ciano da camisa,
  vinho/escuro das frentes e cinza da pista.
- Sol baixo visivel cria contorno e flare aparente em amostras; origem e controle
  da luz sobre o rosto nao foram publicados.
- A camisa tem matiz azul/ciano enquanto caminhoes e ambiente sao
  predominantemente ouro/bege; o efeito de separacao e uma hipotese abaixo.
- Composicao aproximadamente simetrica, formas repetidas e linhas da pista
  permanecem presentes nas amostras.

### Inferencia/prototipo

- Cor pode funcionar como separacao funcional: humano frio contra maquina e
  amanhecer quentes; separar melhor o performer e um efeito a testar. Intencao
  de wardrobe/grade nao publicada.
- Luz baixa tem dupla funcao potencial: janela de irrepetibilidade e escala
  emocional. A fonte do motorista confirma amanhecer, nao o esquema de luz.
- Linhas da pista e repeticao de forma podem tornar variacoes espaciais mais
  comparaveis; testar contra uma versao sem referencias, pois o efeito nao foi
  medido.

## Performance, stunt, safety e producao

- Olhos fechados, abertura dos olhos, bracos cruzados e relativa imobilidade
  sao observaveis nas amostras; ritmo, tensao e microexpressao exigem playback.
- O motorista relata oito dias de ensaio sem Van Damme e uma linha de limite.
- A tomada com o performer ocorreu em janela curta de amanhecer segundo o
  participante; isso nao torna pressao de horario uma virtude por si so.
- A cartela final e `DISCLOSURE_AO_PUBLICO` sobre profissionais e area fechada;
  nao e `EVIDENCIA_DE_PRODUCAO_SEGURA`.
- Faltam: rig, protecao contra queda, medical, autoridade de stop, vento limite,
  velocidades, comunicacao, plano de resgate e disposicao de VFX/cleanup.
- Regra: nunca converter este precedente em instrucao operacional de stunt. Um
  coordenador qualificado, seguranca, veiculos e autoridade local sao humanos
  obrigatorios; uma versao sem pessoa exposta deve existir como alternativa.
- Objetivo, consequencia, objeto ou proxy podem fornecer medida humana sem
  colocar um corpo em risco.

## Montagem e ritmo

- A estrutura visual observada comprime-se em quatro regimes: identidade,
  revelacao, expansao/reducao do split e atribuicao/safety.
- O detector nao encontrou candidatos acima de 0,28. Nas amostras, a mudanca
  interna ao quadro torna a progressao legivel; a frequencia de corte do arquivo
  final permanece desconhecida, e zero candidatos nao prova ausencia de cortes.
- Nao chamar de plano-sequencia, one-take ou feito em camera; usar apenas o
  rotulo de composicao aparentemente continua definido acima.
- O retorno parcial dos caminhoes evita que o clímax termine apenas no maximo;
  a acao ganha fechamento antes da cartela. Esta e leitura, nao intencao publicada.

## Som e musica

- A legenda oficial localiza fala em 00:03,3–00:30,4 e cartelas em 01:01,2–01:07,6
  e 01:12,9–01:16,0.
- Nilsson declara ter testado a musica de Enya sobre a tomada no local e mantido
  a escolha apos reacao da equipe. O estado e
  `LICENCIAMENTO_NEGOCIADO_SEGUNDO_O_DIRETOR`, nao licenca auditada.
- EBU: -12,4 LUFS integrado, LRA 5,1 LU, true peak -2,0 dBFS.
- `silencedetect` a -35 dB por 0,3 s nao encontrou intervalo; isso nao significa
  ausencia perceptiva de pausa, nem identifica voz, musica, motores ou ambiente.
- `PROTOTIPO_PENDENTE_DE_ESCUTA`: musica deve ampliar a dimensao humana sem
  mascarar tensao mecanica, fala, aviso ou identidade do produto; sem stems e
  escuta nao ha conclusao de mix.

### Mapa sonoro por beats sem escuta

| Beat | Fala declarada | Musica declarada | Motor/ambiente | Efeito | Silencio tecnico medido | Funcao inferida |
|---|---|---|---|---|---|---|
| 00:00–00:03,2 | nao localizada em legenda | presenca geral na copia declarada; limite do beat nao confirmado | nao confirmado | nao confirmado | nenhum a -35 dB/0,3 s | entrada musical possivel; nao avaliar sem escuta |
| 00:03,3–00:30,4 | fala de Van Damme localizada | presenca geral na copia declarada; limite do beat nao confirmado | nao confirmado | nao confirmado | nenhum | fala prepara persona e feito; hierarquia do mix aberta |
| 00:30,5–00:59,4 | nenhuma fala localizada | presenca geral na copia declarada; limite do beat nao confirmado | nao confirmado | nao confirmado | nenhum | musica pode carregar progressao; efeito nao auditado |
| 00:59,5–01:08,5 | cartela, nao fala | presenca geral na copia declarada; limite do beat nao confirmado | nao confirmado | nao confirmado | nenhum | atribuicao visual; continuidade musical aberta |
| 01:08,75–fim | aviso em cartela, nao fala | nao confirmado por beat | nao confirmado | nao confirmado | nenhum | funcao sonora do fade/aviso desconhecida |

Nenhuma linha autoriza afirmar motores audiveis, contraponto, mascaramento,
sincronismo, espacialidade ou pausa perceptiva.

## Principios candidatos para Atlas, ainda sem promocao

1. `CLAIMED_PRODUCT_VARIABLE_AS_DRAMATIC_VARIABLE` — propriedade reivindicada
   pela marca pode virar mudanca visual mensuravel na encenacao; isso nao valida
   a propriedade.
2. `REVEAL_SPENDS_INFORMATION` — cada mudanca de escala precisa liberar uma nova
   informacao narrativa, produtiva ou de risco.
3. `STAGED_DEMONSTRATION_IS_NOT_VALIDATION` — claim da marca, demonstracao
   encenada e teste independente sao tres classes distintas.
4. `SPECTACLE_NEEDS_HUMAN_MEANING` — escala extraordinaria precisa de objetivo,
   consequencia ou proxy humano; nao requer corpo exposto. Testar brand linkage,
   compreensao do mecanismo e reconhecimento do trabalho invisivel.
5. `SINGLE_ACTION_REQUIRES_MULTI_DEPARTMENT_CHOREOGRAPHY` — aparente simplicidade
   visual desloca complexidade para ensaio, safety, camera, luz e contingencia.
6. `CREW_REACTION_IS_NOT_AUDIENCE_EVIDENCE` — emocao no set pode orientar teste
   de montagem, nunca validar recepcao.

Os itens 1, 3, 5 e 6 podem ser candidatos apos reauditoria. Os itens 2 e 4,
contraste cromatico, cartela tardia, continuidade aparente e preservacao em
cutdowns permanecem prototipos. Recusar: one-take inferido, stunt como teste
independente, disclosure como prova de safety, negociacao musical como licenca
auditada e numeros de case como causalidade comercial.

## Pendencias antes de qualquer promocao

- critica independente e disposicao;
- playback continuo com imagem e som ou manutencao explicita dos gates 4/6;
- fonte primaria de stunt/rig/VFX/cleanup;
- ficha de creditos ampliada e eventual conflito de versao.

## Disposicao da critica independente

- `P0.1`: aceito; continuidade aparente e tomada com performer foram separadas.
- `P0.2`: aceito; claim, demonstracao encenada e validacao ausente sao classes.
- `P0.3`: aceito; nenhum principio autoriza stunt e alternativa sem exposicao e
  obrigatoria.
- `P0.4`: aceito; gates 4/5/6 e estado global permanecem parciais.
- `P1.1`: corrigido; dado bruto de simetria/repeticao foi separado do efeito.
- `P1.2`: aceito como limite; resumo nao e transcricao e gate 5 segue parcial.
- `P1.3`: mapa declarativo corrigido; a presenca musical e geral e nenhum limite
  de beat foi confirmado. Sem escuta, gate 6 segue parcial.
- `P1.4–P1.5`: montagem, camera, movimento, cor e luz foram mantidos como
  amostra/hipotese; frequencia de corte final permanece desconhecida.
- `P1.6`: creditos continuam parciais e cargo nao atribui decisao total.
- `P1.7`: negociacao musical relatada nao e documento de licenca.
- `P1.8`: disclosure ao publico nao e safety case.
- `P1.9`: significado humano inclui brand linkage e trabalho invisivel; corpo
  exposto nao e requisito.
- `P1.10`: distribuicao/resultados permanecem declaracoes de case sem causalidade.
- A V2 encontrou residuos em P1.1, P1.3, P1.4 e na classificacao Atlas. Eles
  foram corrigidos acima; Gate 9 aguarda a reauditoria V3 desta disposicao, e
  nenhum Atlas sera ingerido antes dela.
- A V3 confirmou o fechamento literal e semantico desses quatro residuos.
  Gates 8 e 9 estao cumpridos apos disposicao; os itens 1, 3, 5 e 6 podem ser
  considerados pelo Atlas dentro dos limites registrados. Gates 4/5/6 e o
  estado global permanecem parciais.
