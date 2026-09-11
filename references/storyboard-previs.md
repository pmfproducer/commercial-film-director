# Storyboard, overhead, keyframes, animatic e pacote por plano

## Visual bible

Consolide apenas regras que precisam sobreviver entre planos:

- logline visual e arco emocional;
- POV/distância emocional;
- regra de realidade e ruptura;
- gramática de quadro, perspectiva e movimento;
- progressão de luz, contraste, cor e material;
- regras de mundo/arte/props/figurino;
- gramática de performance;
- montagem e som;
- regras AI-native;
- clichês proibidos.

## Research boards

### Realidade

Prova lugar, época, comportamento, processo, produto e material. Em cada card: fonte/direitos, o que prova, detalhe observável, decisão informada, o que não copiar.

### Linguagem

Cada frame deve produzir uma regra: “figura pequena contra arquitetura esmagadora”, não “gostei dessa foto”.

### Anti-referência

Registre soluções de categoria, performance, movimento, look e IA que tornariam o filme genérico.

## Storyboard

Use dois níveis quando necessário:

- `rough story board`: barato, pode vir antes de identities/look masters e testa causalidade, POV, blocking e corte;
- `execution board`: vem depois dos masters relevantes e fixa composição, estado, continuidade e inputs de geração.

Não espere todos os assets para pensar a sequência nem trate um rough board como referência visual aprovada.

No `rough story board`, registre apenas o necessário para testar a sequência:

```text
SEQ-SHOT-PANEL
beat/função e informação nova
ação e mudança de estado
POV/composição essencial
entrada/saída
duração aproximada e som relevante
relação com o painel anterior; CUT/NO CUT se ambíguo
```

No `execution board`, acrescente os controles que precisam sobreviver à geração,
captação ou montagem:

```text
SEQ-SHOT-PANEL
shot e panel — vários painéis podem pertencer ao mesmo plano
beat e função
informação nova
emoção
objetivo/tática e gatilho percebido
ação, expressão, eyeline e relação com parceiro/prop
foreground / midground / background
enquadramento e POV
estado/pose de entrada e saída
duração aproximada
som/fala
relação com o painel anterior
`CUT` ou `NO CUT` quando a relação puder ser ambígua
```

Se o painel não altera informação, emoção, ação, composição ou ritmo, provavelmente é redundante.

## Overhead/director's plan

Não confunda com storyboard. Mostre:

- planta e escala;
- geografia e arquitetura;
- posições/trajetórias de personagem e produto;
- câmera e campo de visão;
- eixo, eyelines e screen direction;
- trilho/crane/gimbal quando relevantes;
- distância/foco;
- fontes de luz;
- entradas, saídas e oclusões.

Para IA, overhead ou white/clay model pode controlar relações espaciais, pose, blocking e câmera. Desenhe primeiro a ação e as relações; adicione câmera/campo/luz depois, salvo quando o dispositivo do plano exigir desenvolvimento simultâneo.

## Shot list

Núcleo de qualquer plano:

```text
SHOT-ID / função / duração
entry → evento → exit
composição inicial/final e POV
ação/performance/blocking
câmera ou imobilidade
som e relação editorial
```

Acrescente somente quando afetarem execução ou continuidade:

```text
posição/altura/distância/eixo inicial e final
campo/formato/perspectiva/óptica/foco/profundidade
movimento: gatilho/path/velocidade/aceleração/parada/hold
movimento do sujeito e ambiente
luz: fonte/direção/tamanho/contraste/cor + arte/material/props
transição de entrada/saída
assets dependentes
modo de geração
risco e pós
```

Não crie colunas vazias para planos simples. Um lock-off de reação pode exigir
menos descrição que uma transformação contínua de produto.

## Keyframes

- `story keyframe`: ápice emocional;
- `look keyframe`: resultado de arte, luz, cor e material;
- `execution keyframe`: input direto de geração;
- `first frame`: estado corporal, composição, olhar, produto, luz e elementos móveis;
- `last frame`: mudança concluída, pose, câmera, continuidade e hold.

Entre first/last, defina caminho causal: o que transforma, por qual oclusão/movimento, trajetória, velocidade, aceleração e desaceleração.

## Animatic

Teste:

- duração real dos painéis e da ação;
- legibilidade da ideia;
- produto e marca pelo tempo necessário;
- fala/respiração;
- câmera;
- música, SFX, atmosfera e silêncio;
- pontos de corte e transições;
- handles;
- duração de versões.

Use imagens provisórias sem embelezamento. Animatic é instrumento de pensamento temporal.

## Pacote executável por plano

Núcleo do handoff: `SHOT-ID + intenção + duração + entry/event/exit + ação e
câmera + assets ativos com papel + modo/prompt + critérios de aprovação`.

O bloco abaixo é uma expansão condicional, não formulário obrigatório. Use
first/last, áudio detalhado, plates/dados, color pipeline, VFX/comp ou log somente
quando o plano e a rota escolhida realmente dependerem deles. Não duplique texto
que já está fixado por um asset aprovado: referencie `ID + versão` e registre apenas
sua manifestação naquele plano.

```text
SHOT-ID:
INTENÇÃO — o público sente/compreende...
ESPECIFICAÇÃO — duração, aspecto, resolução, fps, head/tail handles
ENTRY/EXIT STATE — performance, ENV, WDR/HMU, PRD e PRP

ASSETS APROVADOS
@character = identidade
@wardrobe = roupa/HMU
@product = geometria/branding
@environment = geografia/materiais
@look = luz/cor
@motion = câmera/performance
@audio = ritmo/voz/som

FIRST/LAST FRAME + versões
AÇÃO/PERFORMANCE/BLOCKING
CÂMERA/PROGRESSÃO TEMPORAL
SOM — entrada/prelap, ponto de escuta, evento e cauda
IMUTÁVEIS
VARIÁVEIS
CONTINUIDADE
MODO/MODELO E MOTIVO
PROMPT
ROTA DE CAPTURA/GERAÇÃO + PLATES/DADOS quando necessários
COLOR PIPELINE / LOOK REFERENCE
PLANO DE VFX/COMP/PÓS + BRANDING/TEXTO/UI
CRITÉRIOS DE APROVAÇÃO
LOG — modelo, modo, refs, seed/parâmetros, versão, observações
```

## Pipeline adaptativo

- produto simples: visual bible + product master + board + shot packets;
- personagem recorrente: acrescente identity, performance e wardrobe;
- mundo fantástico: environment, props, materials e look development;
- transformação complexa: first/last, overhead/white model e animatic;
- vários personagens: refs individuais, blocking e eyelines;
- sequência longa: continuity bible e versões por estado.

Acrescente controle onde há risco, recorrência ou intenção específica. Não transforme direção em repartição.
