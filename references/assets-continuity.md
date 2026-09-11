# Assets, sheets e continuidade

## Princípio

Asset existe para congelar uma decisão criativa, reduzir uma ambiguidade relevante ou preservar continuidade. Não crie pranchas por hábito.

## Ordem de construção adaptativa

```text
identidade
→ figurino, produto e props
→ ambiente e geografia
→ estilo, luz e material
→ execution storyboard
→ performance/execution keyframes
→ motion/performance references
→ áudio
→ pacote por plano
```

Um `rough story board` pode e deve existir antes dos masters para testar ação, POV, blocking e montagem. A ordem acima descreve consolidação dos **inputs finais**, não uma espera burocrática para começar a pensar o filme.

Não interprete a seta como checklist fixo. Priorize o primeiro risco irreversível
do plano: às vezes é identidade, mas pode ser geografia, produto, performance,
câmera ou transformação. Construa apenas as famílias das quais decisões a jusante
realmente dependem.

## Famílias e IDs

- `CHR` personagem/identidade;
- `PERF` performance/pose/expression;
- `WDR` figurino/HMU;
- `PRD` produto;
- `PRP` prop;
- `ENV` ambiente/local;
- `LGT` luz/look/color key;
- `BRD` storyboard;
- `MOT` movimento/performance/camera reference;
- `AUD` voz, música, atmosfera ou timing;
- `SEQ` sequência;
- `SHOT` plano.

Exemplo: `AURA_SEQ02_SH040_FIRST_v004`.

Mantenha figurino/HMU independente da identidade: `WDR_<CHAR>_<LOOK>_<STATE>_vNN`. Isso permite trocar estado, duplicata ou look sem criar outra pessoa canônica.

Estados: `WIP → REVIEW → APPROVED → SUPERSEDED`.

## Character package

Registre:

- função dramática;
- âncoras imutáveis de identidade;
- silhueta, proporções e escala;
- geometria facial e marcas;
- cabelo, pele e textura;
- postura, centro de gravidade e gestual;
- figurino-base;
- elementos variáveis e invariantes.

Vistas possíveis: full body frontal, perfil, três quartos, costas, close neutro, detalhes críticos e escala. Use base neutra para identidade e keyframe contextual para pele, cabelo, figurino, luz e expressão no filme.

Character sheet é um bom documento humano. Quando houver slots, imagens separadas e nomeadas podem reduzir a leitura de múltiplos personagens dentro de uma prancha.

Isso é uma heurística de produção, não garantia do modelo. Teste a mesma identidade
no ângulo, distância, expressão e luz que o plano exige. Uma vista gerada a partir
de outra só se torna master depois de aprovada; derivadas não substituem
silenciosamente a fonte canônica.

### Vários personagens

- um alias e um identity master independentes por personagem;
- silhueta, figurino, cabelo e paleta distinguíveis quando a cena é complexa;
- um contextual group board para posição, escala, eyelines e relação;
- contrato separado para cada voz/performance;
- não use uma foto de grupo como única fonte de identidade individual;
- faça teste de troca de fala, fusão facial, migração de figurino e troca de lugar.

## Performance package

Separe aparência de atuação:

```text
objetivo, obstáculo e ação jogável
parceiro/alvo e relação
estado corporal inicial
gatilho percebido
ação, olhar, respiração, mãos e prop
mudança gradual e resposta do parceiro
estado/pose final
expressões somente nas intensidades usadas pelo roteiro
invariantes e variáveis permitidas
```

Corpo e relação espacial carregam o beat antes da microexpressão. Para atuação complexa, use vídeo performado, motion/performance reference ou keyframes; prompt textual sozinho é controle fraco. Não peça a uma única prancha que seja simultaneamente identity master, expression range, storyboard, frame de luz e motion reference.

## Product package

- função narrativa;
- geometria, proporções e dimensões;
- frente, verso, laterais, topo/base e três quartos hero;
- logo/grafismos/orientação;
- material, reflexão, transparência e translucidez;
- forma de segurar/usar;
- escala na mão/no cenário;
- estados: fechado, aberto, ativado, gasto, molhado etc.;
- danos/deformações proibidas;
- plano de pós para branding e texto crítico.

Classifique fidelidade: `A_EXACT` para logo, label, claim, UI e texto; `B_CONTINUOUS` para geometria/material/estado; `C_INTERPRETIVE` para detalhe não crítico. Classe A usa fonte oficial e plano de composição/validação, não promessa de geração.

## Prop package

- função narrativa e ação que dispara;
- forma, material, escala, peso e som;
- forma de segurar/operar e pontos de contato;
- orientação/posição/quantidade por plano;
- referência isolada de identidade e referência contextual de uso;
- duplicatas e versões de dano;
- grafo de estados: `ST01 → evento → ST02 → evento → ST03`;
- continuidade com mãos, eyelines, screen direction, som e cortes.

Estado pertence à narrativa; versão pertence ao arquivo:

```text
PRP_GLASS_A__ST01_EMPTY_CLEAN__v01
PRP_GLASS_A__ST02_HALF_FULL_WET__v03_SELECT
```

## Environment package

- função emocional;
- geografia, floor plan e escala;
- entradas, saídas e áreas de ação;
- marcos recorrentes;
- materiais e história do espaço;
- fontes práticas e estados de luz;
- hora, clima, atmosfera;
- caminhos de personagem e câmera;
- vistas master/reverse/axis left/axis right;
- elementos imutáveis e variáveis.

## Wardrobe/HMU

- função dramática e fase narrativa;
- silhueta e leitura à distância;
- camadas e ordem;
- frente, perfil, costas e detalhes;
- tecido, queda e resposta a movimento/luz;
- cabelo, pele e maquiagem;
- acessórios;
- som produzido e interação com produto/props;
- estados seco/molhado, limpo/sujo, íntegro/danificado;
- duplicatas para ação/stunt;
- continuidade por beat;
- elementos que não podem migrar entre personagens.

## Look/luz/material

Não defina estilo por adjetivos. Registre:

- fonte e direção da luz;
- qualidade/falloff/contraste;
- faixa de valores e prioridade de pele/produto;
- dominantes e cor de tensão;
- comportamento de highlight/sombra;
- textura de pele e material;
- profundidade e queda de foco;
- flare, distorção, grão e halation;
- color transform/acabamento pretendido.

Crie look keys nas condições que podem quebrar a continuidade: pele, produto,
highlight especular, sombra profunda, estados de luz distintos, VFX/IA e saída
SDR/HDR quando relevante. Uma referência de look controla aparência; não deve
transferir identidade, figurino, geografia ou composição conflitante.

## Storyboard e execution keyframes

Não use a mesma imagem sem declarar qual função ela desempenha:

- `story keyframe`: intenção e ápice dramático; pode ser inexequível;
- `look keyframe`: luz, material, cor e acabamento;
- `execution keyframe`: composição e conteúdo preparados para um modo gerativo;
- `first frame`: estado literal de entrada quando o modo o usa assim;
- `last frame`: estado literal de saída;
- `reference image`: guia sem obrigação de ser frame de fronteira.

Um painel pode cumprir mais de uma função somente depois de teste. Preserve os
metadados de quadro fora da imagem: SHOT-ID, duração, entry/exit, lente/perspectiva,
som, refs e versão.

## Motion, câmera e performance references

Separe o que cada vídeo deve transferir:

```text
MOT_CAMERA = trajetória, pan/tilt/zoom, velocidade, aceleração, parada
MOT_BLOCKING = caminhos, marcas, contato e relações espaciais
MOT_PERFORMANCE = olhar, respiração, face, mãos, corpo, fala e timing
MOT_EDIT = duração e ritmo de cortes
```

Para cada reference, registre source timecode, duração, FPS, proporção, câmera
estável/handheld, personagem(es), o que herdar e o que ignorar. Uma camera
reference não controla automaticamente blocking; um performance video não deve
transferir figurino, ambiente ou look; um V2V source pode transferir muito mais
estrutura que uma motion reference.

Quando filmar white model/plate:

- preserve começo e fim úteis ao corte;
- mantenha mãos/rosto no quadro se forem controles;
- use fundo simples quando extração/composição for provável;
- respeite escala, gravidade, contato e direção de tela do mundo final;
- grave handles e clean plate quando necessários.

## Áudio e voz

Separe por função quando o modo ou a pós precisarem de controle:

```text
AUD_DIALOGUE_<CHAR>
AUD_VOICE_ID_<CHAR>
AUD_AMBIENCE_<LOCATION>
AUD_SFX_<EVENT>
AUD_MUSIC_<CUE>
AUD_TIMING_<PERFORMANCE>
```

Registre idioma, texto aprovado, performer/consent, timing, sample rate, canais,
room tone, direitos e função. Uma faixa com voz, música e ambiente juntos não é
boa referência quando apenas um desses elementos deve ser herdado. Áudio nativo
pode servir a criação e sincronismo, mas não garante stems; preserve a rota de
reconstrução/mix quando o filme exigir controle editorial.

## Contrato de referência

Para qualquer ref operacional, declare o núcleo:

```yaml
id:
function: "o que deve guiar"
preserve: ["o que deve sobreviver"]
ignore: ["o que não deve transferir"]
status: "WIP | REVIEW | APPROVED | SUPERSEDED"
version:
```

Acrescente os campos abaixo quando houver arquivo externo, colaboração,
direitos/consentimento, reprodutibilidade, múltiplos consumidores ou necessidade
real de rastreamento:

```yaml
alias:
file:
beats: ["onde se aplica"]
model:
surface:
mode:
origin:
rights_status:
consent_status:
generator:
generator_inputs:
consumer: "human-canonical | model-input | post-only"
validation_test:
```

Não transforme exploração local ou rough board em cadastro completo. A quantidade
de metadata deve acompanhar o risco de uso, propagação e aprovação.

`function` registra o atributo que a referência **deve guiar**, não uma promessa de
isolamento interno do modelo. Não escreva apenas “use as imagens como referência”.
Declare: `@Image1 identidade`, `@Image2 figurino`, `@Image3 produto`, `@Image4
geografia`, `@Video1 câmera`, `@Audio1 ritmo`; depois teste vazamento de atributo.

## Continuidade por estado

```text
SHOT | personagem | performance | figurino/HMU | produto/prop | mão |
posição | eyeline | direção de tela | luz/clima | dano/sujeira |
estado da transformação | motivo sonoro | entry | exit
```

Não sobrescreva estados:

```text
CHR_MARA_STATE_A_CALM
CHR_MARA_STATE_B_ALERT
PRD_SERUM_STATE_A_SEALED
PRD_SERUM_STATE_B_OPEN_40PCT
ENV_TUNNEL_STATE_NIGHT_WET
```

Regra: `EXIT SHOT_03 = ENTRY SHOT_04`, salvo ruptura deliberada.

## QA de assets

- identidade reconhecível em ângulos relevantes;
- proporções e escala estáveis;
- produto/logo corretos;
- base neutra separada de look contextual;
- materiais e reflexos coerentes;
- não há contradição entre masters;
- vistas suficientes para o uso previsto;
- função, origem, direitos, versão e status registrados;
- referências não transferem atributos indesejados.
- o arquivo foi testado no modelo/superfície/modo consumidor, não apenas aprovado
  como imagem isolada;
- multi-character e áudio preservam speaker/identity mapping;
- first/last, reference image, V2V source, camera reference e performance source
  não foram tratados como controles equivalentes.
