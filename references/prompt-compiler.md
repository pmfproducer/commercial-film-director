# Compilador de prompts por modo

## Princípio

Prompt não inventa o plano. Ele compila uma decisão já resolvida em instruções que o modelo aceita.

Os blocos abaixo são **schemas intermediários**, não texto para colar cegamente.
Antes da entrega, traduza o schema para o dialeto, campos, aliases e controles da
combinação `MODEL + SURFACE + MODE` verificada. Omita qualquer campo que o modo
não aceite; não mande cabeçalhos de áudio para um motor silencioso, `@Image1` para
uma interface sem aliases ou negative prompt para um modo que não o suporte.

Mantenha duas camadas:

- `MASTER DIRECTION CONTRACT`: intenção, subtexto, POV, beats, blocking, performance, som, continuidade e estado final;
- `EXECUTION PROMPT`: somente os controles que o modelo, modo e superfície escolhidos entendem de forma útil.

O contrato pode ser rico e o prompt curto. Não sacrifique a direção para imitar uma fórmula universal nem despeje o contrato inteiro num modo que pede simplicidade.

## Contrato mínimo antes da compilação

Compile somente quando conseguir preencher, por decisão aprovada ou hipótese
declarada:

```text
dramatic function
entry state → visible change → exit state
subject/action/performance
camera relationship and temporal behavior
critical continuity invariants
approved or intentionally absent references
sound role
model + surface + mode
```

Se o usuário pedir um prompt sem isso, reconstrua o contrato mínimo na própria
resposta com suposições curtas; não transforme a lacuna em questionário nem use o
prompt para decidir silenciosamente o filme.

Ordem geral:

```text
MODE/TASK
→ OUTPUT
→ REFERENCE CONTRACTS
→ SUBJECT/OBJECT/ENVIRONMENT
→ ACTION/PERFORMANCE/BLOCKING
→ CAMERA/COMPOSITION/TIME
→ LIGHT/MATERIAL/COLOR
→ AUDIO
→ PRESERVE/CHANGE
→ SPECIFIC AVOIDS
→ END STATE
```

Dentro de um plano: sujeito → ação observável → câmera/quadro → ambiente/luz/material → som → estado final.

Antes de compilar `camera`, a direção já deve ter resolvido posição inicial e
final, altura, eixo, campo, gatilho, trajetória, velocidade/aceleração, evento
revelado e parada. Nome de lente/câmera só entra se o motor demonstrar resposta
útil; comportamento observável e referências são controles mais fortes.

## Text-to-image

```text
GOAL / USE
SUBJECT AND IDENTITY
PRODUCT OR PROP GEOMETRY
POSE / PHYSICAL ACTION / EXPRESSION
ENVIRONMENT AND SPATIAL RELATIONSHIPS
COMPOSITION / POV / CAMERA POSITION / PERSPECTIVE
OPTICAL BEHAVIOR / DEPTH
LIGHT SOURCE / DIRECTION / QUALITY / CONTRAST
PALETTE / MATERIALS / TEXTURE
ATMOSPHERE
TEXT-SAFE COMPOSITION; exact text only when supported and validated, otherwise POST
OUTPUT / ASPECT RATIO
CONSTRAINTS / EXCLUSIONS IN MODEL-APPROPRIATE FORM
```

Descreva propriedades observáveis, não uma salada de nomes de câmeras/diretores.

## Multi-reference image

O exemplo abaixo é semântico. A quantidade e a sintaxe de referências precisam
ser recompiladas para o limite real do modelo. `guides ... only` expressa o
papel solicitado; o modelo ainda pode vazar atributos entre imagens, por isso o
resultado exige teste de separação.

```text
REFERENCE CONTRACT
- @Image1 guides facial identity only.
- @Image2 guides wardrobe only.
- @Image3 guides approved product geometry and visible brand reference only; exact label/text remains a validation or post task unless the selected mode proves fidelity.
- @Image4 guides location architecture only.
- @Image5 guides lighting and color treatment only.

SCENE
[observable scene]

PRESERVE
[identity, geometry, logo, spatial relations]

ROLE BOUNDARIES
Facial identity remains guided by @Image1; wardrobe by @Image2; product
geometry by @Image3; architecture by @Image4; lighting by @Image5. Preserve
these responsibilities without blending their unrelated attributes.
```

O bloco `ROLE BOUNDARIES` já formula papéis positivos. Se a superfície não
aceitar restrições, mantenha somente essas atribuições e valide vazamento por
iteração; não cole o schema literalmente.

## Image editing / inpainting

```text
Using the provided base image, change only [target/region]
from [current state] to [desired state].

Integrate the change with the existing perspective, scale, lighting,
shadows, reflections, depth of field and material response.

Preserve and validate every non-target area:
[invariants].
```

Para rosto, produto e branding, também descreva os detalhes que precisam sobreviver. “Preserve” é uma intenção de controle, não promessa de pixel invariável; se fidelidade absoluta não for suportada, planeje comp/pós.

## Text-to-video

```text
[SUBJECT] begins in [INITIAL OBSERVABLE STATE] in [ENVIRONMENT].

When [VISIBLE TRIGGER], the subject [ORDERED ACTION/PERFORMANCE]
and ends in [END STATE].

If sound triggers the beat:
[OFFSCREEN / ONSCREEN EVENT] → [perceived response and timing].

The environment responds through [PHYSICAL CONSEQUENCE].

Camera:
[position/framing, one primary behavior, trajectory, speed, stop]

Lighting/material behavior:
[observable behavior]

Audio:
- Dialogue:
- Performance:
- Ambience:
- SFX:
- Music:

End frame:
[useful editorial state]
```

Inclua o bloco de áudio somente em modo com áudio nativo. Em motor silencioso,
compile o mesmo arco como plano de som separado. Para clipe curto, mantenha uma
ação dominante e um movimento principal; ações sequenciais só entram quando a
duração e o modelo demonstram suportá-las.

## Start-frame image-to-video

Neste modo, a imagem é o frame inicial. Ela fixa o estado de partida de sujeito,
composição, luz, cor e estilo; dirija principalmente o tempo:

```text
The camera [one principal behavior]
as the subject [one principal action].

[If performance matters: initial state → perceived trigger → observable change → final state.]

[secondary environmental motion and physical consequence]

The movement begins [initial speed/state],
accelerates/decelerates [behavior],
and ends with [specific end state and hold].
```

Não redescreva tudo nem introduza atributos incompatíveis com o frame.

## Reference-to-video / ingredients

Não confunda com start-frame I2V. Aqui a imagem pode guiar identidade, produto,
ambiente ou estilo sem ser literalmente o primeiro frame.

```text
REFERENCE ROLES
@CHAR_A guides identity only.
@PRODUCT_A guides product geometry/material only.
@ENV_A guides location architecture only.

SCENE AND STARTING COMPOSITION
[what the first visible shot must contain]

ACTION / PERFORMANCE / CAMERA / END STATE
[temporal direction]

DO NOT TRANSFER
[attributes that must not leak between references]
```

Quando o modo aceitar apenas referências de um único sujeito/produto, não use o
limite máximo para montar elenco, figurino, ambiente e style board numa mesma
chamada.

## First/last frame

```text
FIRST FRAME
[already fixed state]

TRANSITION MECHANISM
A single continuous [physical / semantic / camera] transformation
connects the first frame to the last.

TEMPORAL PROGRESSION
Beginning:
Middle:
End:

LAST FRAME
Use the supplied final composition as the target state, settle into it and hold.
```

Os dois frames não dirigem o meio. Declare movimento, transformação, passagem do tempo, escala, oclusão ou match mechanism.
Valide se os estados são geometricamente alcançáveis, se a direção de luz pode
mudar de modo coerente e se a duração comporta o percurso. O prompt não garante
por si só uma chegada pixel-perfect.

First/last controla estados de fronteira; não é, por si só, ferramenta de
identidade, diálogo, contato entre personagens ou preservação de produto durante
o percurso. Para esses riscos, acrescente refs/element binding quando disponíveis
ou use passes/composição.

## Video-to-video transformation

O source oferece timing, corpo, blocking e câmera como referência. Descreva o estado visual final e valide o que o modo realmente preservou:

```text
Transform the source footage into [target world/look/material].
Preserve [camera movement, timing, body motion, gaze, product position].
Change [environment, material, wardrobe or character treatment].
The final footage should look like [observable end state].
```

`Preserve` é um alvo. No QA, teste separadamente timing, câmera, corpo, expressão,
produto e background; o nível de aderência que protege um deles pode impedir a
transformação de outro.

## Camera/motion reference

Este modo não é sinônimo de V2V. A referência pode transferir somente trajetória,
ritmo, velocidade ou caráter de câmera, sem preservar conteúdo, duração ou
blocking completos.

```text
CAMERA REFERENCE
@[VIDEO] guides [path / pan / tilt / zoom / handheld character / timing] only.

GENERATED SCENE
[subject, action, environment and starting composition]

CAMERA APPLICATION
Apply the referenced camera behavior to [specific relationship with subject].
Ignore identity, wardrobe, location, color and audio from the reference.
```

Se a superfície oferecer `composition reference` separada, declare-a em outro
contrato; composição/layout não deve ser inferido de uma referência destinada
apenas à câmera.

## Video editing

```text
[CHANGE VERB] [target] to [specific state].

Match the existing perspective, camera motion, lighting, shadows,
reflections, depth and temporal behavior.

Preserve [all non-target elements].
```

Faça uma transformação principal por iteração e valide regiões não alvo. Em
editores que aceitam keyframes, use o frame aprovado para ancorar a mudança; a
frase de preservação não garante isolamento temporal ou pixel-perfect.

## Extensão

```text
Continue directly from the visual and audio state of @[SOURCE].

Preserve:
[identity, wardrobe, product, location, light, lens behavior,
camera inertia, ambient sound, music rhythm]

Continue the existing action:
[trajectory]

Introduce one new beat:
[next action]

End with:
[next useful editorial state]
```

Use apenas quando o modo aceitar o tipo de source fornecido; alguns extensores
continuam somente clips gerados pelo próprio modelo. Preserve áudio no prompt
apenas quando a extensão audiovisual estiver documentada. Caso contrário,
estenda/reconstrua ambience, SFX, música e diálogo na pós. Extensão reduz a quebra
no splice, mas pode acumular drift de identidade, geometria, luz e ritmo; compare
o novo `exit state` com o continuity ledger.

## Performance transfer / lip-sync

```text
PERFORMANCE SOURCE
- actor video is intended to guide timing, gaze, expression, breath, mouth, hands and body

CHARACTER SOURCE
- character reference is intended to guide identity, anatomy/material and wardrobe

TRANSFER
Target the emotional progression and spoken timing from the approved performance.
Adapt the motion anatomically to the target character.
```

Use somente quando o modelo/modo suportar os controles declarados. Valide olhos, boca, mãos, timing, corpo e identidade; “performance transfer” não garante cópia exata. Use consent e autorização para pessoa real, imagem e voz.

Separe o contrato conforme o input:

- `character image`: pode permitir transferência de face, fala, gesto e corpo,
  dependendo do modo;
- `character video`: normalmente preserva a câmera/ambiente/movimento corporal do
  vídeo e aplica principalmente face, expressão e fala;
- `lip-sync only`: controla boca/tempo de fala e não deve ser vendido como
  transferência de atuação corporal.

No Act-Two atual, um character input é processado por geração. Cenas com vários
falantes exigem passes individuais e composição; grave performances com timing de
resposta já resolvido e evite sobreposição de fala se o speaker mapping do motor
não tiver sido testado.

## Áudio nativo

```text
DIALOGUE
CHAR_A, [delivery, volume, intention]:
"Texto exato."

PERFORMANCE
[speed, breath, pauses, effort]

AMBIENCE
[space, distance, reflections]

SYNCED SFX
[event → sound consequence]

MUSIC
[function, tempo, instrumentation, curve, entrance/exit]

MIX PRIORITY
[foreground / midground / background]
```

Não dependa do mix unido quando a produção precisa de controle: preserve plano para stem/substituição de diálogo, atmosfera, SFX e música.

O bloco é um brief sonoro, não promessa de stems, mix, loudness, fonema perfeito
ou sincronismo frame-exato. Mapeie cada fala a um personagem inequívoco, descreva
os eventos em ordem e retire `MUSIC` quando o modelo/superfície não documentar
controle musical útil.

## Storyboard/reference-controlled multimodal

```text
OVERALL OUTPUT
duration, aspect, language, number of beats/shots

REFERENCE ROLES
@Image / @Video / @Audio = one explicit responsibility each

CONTINUITY CONTRACT
identity, wardrobe, product, geography, screen direction, light, audio motif

BEAT 1 [time range only if supported]
action + camera + sound + exit state

BEAT 2
...

PRESERVE / CHANGE / DO NOT TRANSFER
END STATE
```

Use timestamps só em modelos/modos que respondem a controle temporal. Não finja precisão.

## Negativos

Alguns modelos respondem melhor apenas a instruções positivas; outros possuem campo de negative prompt ou aceitam restrições explícitas. Verifique a superfície. Runway Gen-4/4.5, por exemplo, recomenda formulação positiva e pode interpretar “no/don't” de forma imprevisível.

Primeiro formule invariantes positivos:

- preserve the approved facial identity throughout;
- retain the approved product silhouette, proportions and label placement for validation;
- keep the approved grip and hand anatomy throughout the action;
- preserve left-to-right screen direction;
- keep the established light direction and exposure stable;
- keep every background character separate and consistent;
- keep the camera locked after the final landing.

Só quando o modo aceitar negativos, acrescente prevenções específicas como
`no identity blending` ou `no product-label deformation`.

Evite listas universais gigantes. Elas competem com a ação principal.

## Complexidade e vários personagens

- Nomeie por posição ou alias inequívoco e atribua uma ação a cada sujeito.
- Atribua cada fala ao alias correto e declare quem escuta/reage; valide speaker
  mapping antes de produzir todas as cenas.
- Declare parceiro, eyeline, contato e resposta; não peça “eles interagem naturalmente”.
- Uma ação dominante e um movimento principal de câmera por beat, salvo coreografia controlada por vídeo.
- Se identidade, fala, contato físico, prop e câmera disputam o mesmo plano, use
  element/reference binding, motion/performance references, passes separados ou
  composição. First/last só ajuda quando o problema real são os estados de
  fronteira.
- Teste primeiro o beat de maior risco. Divida o plano quando o modelo não sustentar a causalidade; não transforme falha de capacidade em prompt enciclopédico.

## Critérios de prompt pronto

- um modo/tarefa claro;
- modelo, superfície e modo não foram confundidos;
- cada referência tem função;
- ação e câmera são fisicamente legíveis;
- há progressão, não só aparência;
- estado final é útil para montagem;
- invariantes e variáveis não se contradizem;
- áudio, se pedido, tem eventos e prioridade;
- branding/texto crítico possui plano de validação/pós;
- nenhuma frase tenta corrigir uma decisão criativa inexistente.
