# Fotografia: câmera, lente, luz, movimento e cor

## Cadeia causal

```text
beat dramático
→ relação do espectador com a cena
→ geografia e blocking preliminar
→ posições inicial/final, altura, distância e eixo da câmera
→ perspectiva, campo e composição
→ formato, óptica, foco, profundidade e shutter
→ blocking refinado e trajetória/imobilidade
→ luz, exposição, filtros e resposta de materiais
→ suporte/rig e execução
→ pipeline de cor e acabamento
```

Não comece por uma câmera famosa ou por “35 mm cinematográfica”.

Essa cadeia possui loops. Blocking vem antes da câmera como prioridade
dramática; posição, campo, bordas, foco, trajetória, arte e luz voltam ao ensaio
e refinam marcas. Um plano-conceito pode restringir blocking, mas ainda precisa
servir ação, performance e POV. Se a solução técnica obriga a trocar a intenção,
suba de nível e torne a mudança explícita.

## Posição e composição

Decida:

- alinhamento com o POV;
- distância emocional;
- tamanho relativo entre personagem, produto e mundo;
- altura e poder;
- frontalidade ou observação lateral;
- primeiro, segundo e terceiro planos;
- espaço negativo;
- simetria, desequilíbrio, linhas e massas;
- informação incluída/excluída;
- estado inicial e final da composição.

## Lente e perspectiva

Separe os mecanismos:

- a posição física da câmera determina perspectiva e proporção espacial;
- focal + área capturada do sensor determinam o campo de visão daquela posição;
- ao manter o mesmo tamanho de sujeito com outra focal, a câmera costuma mudar
  de posição; essa mudança, não o número em milímetros sozinho, altera rosto,
  fundo e parallax;
- zoom muda campo sem deslocar a câmera; dolly muda posição e perspectiva;
- formato, abertura, focal, distância de foco e critério de nitidez participam
  da profundidade de campo.

Considere em conjunto:

- focal e tamanho de sensor;
- distância câmera-sujeito;
- ângulo de visão;
- proporção aparente entre planos;
- distorção geométrica e facial;
- profundidade de campo e distância de foco;
- abertura e transmissão;
- contraste/microcontraste;
- flare, ghosting e veiling glare;
- bokeh e queda de foco;
- breathing;
- consistência entre lentes.

Escolha nesta ordem: posição/perspectiva → campo → profundidade/foco →
comportamento óptico → cobertura/mecânica/transmissão. Teste rosto, produto,
bordas, fontes especulares, rack focus, movimento e look de exibição.

Mecanismos expressivos comuns:

- câmera próxima + campo amplo: presença, corpo, espaço expandido, possível distorção;
- câmera distante + tele: observação, compressão, isolamento, grafismo;
- foco profundo: relações simultâneas e mundo legível;
- foco raso: seleção, intimidade, fragilidade ou ocultação;
- óptica limpa: precisão e material;
- óptica degradada/difundida: memória, pele, atmosfera ou instabilidade — apenas quando serve ao filme.

Anamórfico não é sinônimo de cinema. Avalie magnificação, squeeze, breathing,
flare, bokeh, focus roll-off, close focus, composição e sobrevivência aos
recortes. Em IA, “anamorphic cinematic” tende a convocar clichês; prefira um
look key e fenômenos observáveis quando eles realmente importarem.

## Câmera e formato por comportamento

Formule requisitos antes de citar equipamento:

- latitude e highlight roll-off necessários;
- textura e reprodução de pele/produto;
- rolling/global shutter e tipo de movimento;
- sensibilidade e nível de luz;
- sensor/formato e ópticas desejadas;
- frame rate e motion cadence;
- shutter/tempo de exposição e motion blur;
- tamanho, peso e geometria do rig;
- metadata/VFX/tracking;
- resolução, crop e entregas;
- pipeline de cor.

Para geração com IA, traduza esses requisitos em comportamento observável. Nome de câmera/lente pode ser referência secundária, nunca a decisão principal.

“Imagem escura” não significa subexpor sem desenho. Declare a âncora de exposição
(pele, label, céu, metal, chama ou tela), o que pode cair em sombra, o que não
pode clipar e a margem necessária para VFX/color/HDR.

## Filtros

- ND/IRND: controla exposição/abertura e contaminação infravermelha;
- polarizador: reflexos, céu e saturação, com efeitos dependentes de ângulo;
- diffusion: blooming/halation, contraste, resolução aparente e pele;
- grads: distribuição de exposição;
- efeitos especiais: apenas quando testados no sistema inteiro.

Teste filtro + lente + sensor + pele + produto + fontes especulares + exposição. Um filtro não produz efeito fixo em qualquer combinação.

Em difusão, separe três fenômenos: halation, redução de contraste/veiling e
redução de detalhe fino. Look de IA deve reproduzir fenômenos consistentes, não
apenas citar a marca do filtro. Polarizador pode remover reflexos que desenham o
produto e variar em pans/ângulos amplos.

## Luz

Defina:

- fonte motivadora e plausibilidade do mundo;
- direção;
- tamanho/qualidade;
- distância e falloff;
- relação key/fill/negative fill;
- contraste e faixa de valores;
- cor relativa;
- practicals e elementos visíveis;
- separação de pele, produto e fundo;
- comportamento de materiais, reflexos, transparência e atmosfera;
- progressão ao longo dos beats.

Qualidade dura/suave depende sobretudo do tamanho aparente da fonte, não da
intensidade. Fonte suave continua precisando de direção e contenção: spill pode
achatar o fundo e destruir a hierarquia. Luz motivada pode ser impossível ou
expressionista, desde que sua regra produza direção, queda, sombra, reflexão e
mudança coerentes.

Luz pode ser naturalista, expressionista, gráfica, beauty ou orientada a produto. A escolha deve expressar uma situação e não um preset.

Para prompts, descreva fonte observável, direção, qualidade, contraste, resposta de material e prioridade. “Cinematic lighting” não informa nada.

## Movimento e imobilidade

Todo movimento precisa de:

```text
motivo
ponto inicial
ponto final
trajetória
velocidade
aceleração/desaceleração
estabilidade
relação com ação/blocking
informação revelada ou relação transformada
momento de parada
```

Desenhe-o como `start frame → gatilho → aceleração/trajetória → evento interno
→ desaceleração → end frame/hold`. Se nada muda no percurso, compare com um
corte entre os estados.

Funções possíveis:

- seguir/perseguir;
- aproximar para reconhecer uma mudança;
- afastar para contextualizar ou abandonar;
- revelar por paralaxe/oclusão;
- transferir atenção;
- reconfigurar poder entre corpos;
- materializar vertigem, liberdade, ameaça ou controle;
- conectar escalas/mundos;
- executar uma transformação causal impossível.

Ferramentas têm comportamentos, não emoções fixas:

- dolly/trilho: trajetória precisa e paralaxe controlada;
- slider: deslocamento curto;
- gimbal: mobilidade fluida com risco de flutuação genérica;
- Steadicam: presença humana estabilizada;
- handheld: resposta corporal e microvariação;
- crane/jib: mudança de altura e relação espacial;
- drone: deslocamento aéreo/escala;
- motion control: repetição, composição e VFX;
- lock-off: atenção ao que muda dentro do quadro.

## Movimentos e IA

Não peça três movimentos incompatíveis num plano curto. Defina um comportamento principal e, quando necessário, use:

- video reference para trajetória real;
- white/clay model para blocking e câmera;
- first/last frames para composição extrema;
- V2V para preservar timing/corpo/câmera;
- keyframes intermediários quando o modelo aceita;
- plano dividido quando a causalidade excede a capacidade do motor.

Câmera fisicamente impossível ainda precisa de motivação, inércia legível e ponto de chegada.

Separe controles generativos:

- execution/start frame: composição, identidade e estado inicial;
- last frame: estado de chegada, não o caminho;
- white/clay model: geografia, blocking, pose, trajetória e câmera;
- motion reference: path, timing e curva de aceleração, não identidade/look;
- look key: luz, contraste, material e cor, não geografia;
- V2V: preservar performance/câmera já válidas enquanto muda mundo/material;
- references: um papel e limites de transferência por asset.

Para I2V, o frame já fixa aparência; o prompt deve dirigir ação, câmera,
ambiente e progressão temporal. Para T2V, descreva também mundo/composição.
First/last frames precisam ser geometricamente alcançáveis e ter tempo para a
transição. Não peça simultaneamente layout, identidades, coreografia complexa,
look e câmera virtuosa somente por texto.

## Plano-sequência e corte

O plano-sequência é justificado por continuidade, performance, transformação ou relação espacial. Se a ideia exige colisão de pontos de vista, compressão, elipse ou controle preciso de informação, corte pode ser mais forte.

## Cor

Cor começa em roteiro, locação, set, pigmentos, materiais, pele, figurino, fontes, exposição, lente e filtro. O grade consolida e separa; não ressuscita decisões contraditórias.

Defina:

- progressão por beat;
- faixa de valores;
- contraste e densidade;
- dominantes e cores de tensão;
- prioridade de pele/produto;
- comportamento de highlights e sombras;
- saturação relativa;
- color management/show transform;
- integração com VFX e versões.

Separe o pipeline:

```text
superfície/material + espectro da luz
→ exposição/filtro/óptica/sensor
→ input transform/normalização
→ look transform de produção
→ balance e continuidade por plano
→ grade criativo e integração VFX/IA
→ output transform por display
→ trim pass e QC
```

Look transform é modificação sistemática e portátil; não substitui grade por
plano. Guarde look keys com pele, produto, highlight, sombra, VFX/IA e saídas
SDR/HDR quando relevantes.

## Testes mínimos

- perspectiva: três posições físicas e campos de visão, com blocking real;
- óptica: rosto/produto/bordas, T-stops, close focus, rack/breathing, flare e pan;
- luz/material: duro/suave, fill/negative fill, mixed color, vidro/metal/líquido/
  tecido/tela/rótulo e exposição acima/abaixo;
- filtros: clean + densidades em close/wide, pele, produto, practicals e movimento;
- movimento: duração real, trajetória, parallax, aceleração, parada e handoff;
- IA: trocar uma variável por rodada; testar posição → trajetória → ação → look
  → modo → duração, mantendo as demais fixas;
- first/last no modelo-alvo: geografia, identidade, direção de luz e chegada;
- cor/VFX: chart, pele, cor de marca, transforms, roundtrip e trims;
- montagem: plano entre vizinhos e com som, não still isolado.

## Card de fotografia por plano

```text
FUNÇÃO / BEAT / EFEITO NO PÚBLICO
POV E DISTÂNCIA EMOCIONAL
BLOCKING + ENTRY/TRIGGER/MID/EXIT
POSIÇÃO/ALTURA/EIXO + COMPOSIÇÃO START/END
CAMPO/FORMATO/ÓPTICA/FOCO/PROFUNDIDADE/SHUTTER
MOVIMENTO: MOTIVO/PATH/SPEED/ACCEL/STOP/HOLD
LUZ: FONTE/DIREÇÃO/TAMANHO/CONTRASTE/COR/MATERIAL
ÂNCORA DE EXPOSIÇÃO + FILTRO
COR/LOOK/TRANSFORMS/TRIMS
CONTROLE IA: MODE/ASSETS/PRESERVE/CHANGE
ALTERNATIVA / TESTE / SINAL DE FALHA
```

Se a saída for apenas “50 mm, dolly-in, soft cinematic light, teal and orange,
ARRI look”, a decisão fotográfica ainda não existe.

## Fontes-base

- [AFI Cinematography Curriculum](https://conservatory.afi.com/cinematography-curriculum/) — análise dramática, perspectiva, composição, lente, cor, exposição, blocking, testes e pós.
- [Kodak Essential Reference Guide for Filmmakers](https://www.kodak.com/content/products-brochures/Film/kodak-essential-reference-guide-for-filmmakers.pdf) — óptica, T-stop, foco, profundidade, exposição e filtros.
- [ARRI Lighting Handbook](https://www.arri.com/resource/blob/83996/409091c612f371b0c68b41d9dcb636db/arri-lighting-handbook-english-data.pdf) — hard/soft, tamanho aparente, spill, intensidade e cor.
- [ASC Shot Craft: Camera Movement](https://theasc.com/articles/shot-craft-camera-movement) — roteiro/intenção antes de suporte e assinaturas das ferramentas.
- [Panavision Five Pillars of Anamorphic](https://www.panavision.com/highlights/highlights-detail/the-five-pillars-of-anamorphic) — atributos anamórficos a testar.
- [Tiffen Diffusion Guide](https://tiffen.com/pages/diffusion-guide) — halation, contraste, resolução e densidades.
- [ACES Look Transforms](https://docs.acescentral.com/system-components/look-transforms/) — lugar e limite do look no color management.
- [Runway I2V Prompting Guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide), [Veo](https://deepmind.google/models/veo/), [Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) e [Firefly Motion Reference](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/match-camera-motion-to-reference-video.html) — controles generativos atuais.
