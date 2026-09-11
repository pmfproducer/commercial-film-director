# Motor de decisões de direção de fotografia

## Finalidade

Esta referência transforma intenção de direção em decisões executáveis de
fotografia. Ela não é um catálogo de estilos nem uma lista de equipamentos.

Uma passagem de DP só está pronta quando entrega, em três escalas:

1. **sistema do filme** — ponto de vista, evolução visual, regras e proibições;
2. **sistema de captura/geração** — formato, óptica, movimento, dinâmica, luz,
   exposição, cor e testes;
3. **decisão por plano** — composição, posição, lente, foco, trajetória, tempo,
   luz, exposição, continuidade, execução e fallback.

Se a saída couber em “35 mm anamórfica, golden hour, dolly-out, 24 fps, A24”,
a direção de fotografia ainda não foi feita.

## Contrato do DP

Para cada recomendação, registrar:

```text
DECISÃO
FUNÇÃO DRAMÁTICA/COMERCIAL
EFEITO PERCEPTIVO PRETENDIDO
MECANISMO FÍSICO OU VISUAL
COMO EXECUTAR
COMO TESTAR
CONTRAINDICAÇÃO/SINAL DE FALHA
ALTERNATIVA MAIS SIMPLES
STATUS: PROPOSTO | TESTAR | CONFIRMADO | N/A
```

Não esconder incerteza com adjetivo. Se sensor, lente, locação, distância,
orçamento ou modelo não foram confirmados, especificar o comportamento requerido
e o teste que fecha a escolha.

## Ordem real da decisão

```text
beat e mudança
→ relação do espectador com sujeito/produto/mundo
→ blocking, geografia e duração da ação
→ posição física, altura, distância, eixo e composição
→ comportamento da câmera: imóvel ou trajetória
→ campo de visão, perspectiva e profundidade/foco
→ formato/sensor e família óptica capazes de executar
→ dinâmica temporal, shutter e motion blur
→ luz motivadora, exposição, materiais e continuidade
→ filtro, textura, show LUT e pipeline de cor
→ suporte/rig, foco, monitoramento, dados e VFX
→ teste, fallback e contraindicação
```

Não comece pelo equipamento. Também não termine em abstração: depois de definir o
comportamento, proponha pacote e parâmetros quando a rota for captação real.

## Cinco eixos explícitos

Use estes cinco eixos como controles obrigatórios. Eles podem lembrar seletores de
interface, mas não funcionam como presets.

### 1. Câmera e movimento

Escolha primeiro o **comportamento**:

- imóvel/testemunhar;
- pan/tilt/reframe;
- push/pull;
- tracking lateral/frontal/traseiro;
- arco/orbit parcial;
- elevação/descida;
- handheld/ombro/Easyrig;
- Steadicam/gimbal;
- crane/jib/Technocrane;
- drone/cable/vehicle/body rig;
- macro/probe/motion control;
- trajetória impossível por IA/VFX.

Para cada `CAM-MOV-ID`, preencher:

```text
FUNÇÃO: revelar, aproximar, abandonar, acompanhar, oprimir, liberar, transferir,
        recontextualizar, conectar escalas ou materializar transformação
START FRAME: posição, altura, distância, eixo, composição e oclusões
GATILHO: ação, fala, som ou informação que inicia o movimento
PATH: eixo e geometria da trajetória; relação com blocking e parallax
CURVA: duração, velocidade, aceleração, easing e estabilidade
EVENTO: o que muda durante o percurso
STOP/HOLD: ponto final, duração de parada e motivo do corte
EXECUÇÃO: suporte/rig, operador, repetibilidade, foco e segurança
FALHA: flutuação genérica, antecipação da revelação, perda de geografia etc.
FALLBACK: corte, lock-off, dolly curto, V2V, motion reference etc.
```

“Orbit 360°” não é decisão. Declare por que o espectador precisa circundar o
sujeito, o que cada fração revela e por que 360° é melhor que 60°, 120° ou corte.

### 2. Perspectiva, formato e óptica

Decida em duas camadas.

**Camada perceptiva** — obrigatória em qualquer rota:

- proximidade física da câmera;
- relação de escala entre primeiro plano, sujeito e fundo;
- campo horizontal/vertical necessário;
- distorção ou compressão desejada;
- profundidade legível versus isolamento;
- comportamento nas bordas;
- transição de foco, breathing e close focus;
- contraste, flare, veiling glare, bokeh e focus roll-off;
- sobrevivência a 16:9, 9:16, 1:1 e cutdowns.

**Camada técnica** — obrigatória quando captação/equipamento estiverem definidos:

- sensor/formato e crop/de-squeeze;
- família de lentes e cobertura;
- focal/focais por função, nunca isoladas;
- distância câmera-sujeito e distância de foco;
- T-stop de trabalho e profundidade resultante;
- verificação de profundidade de campo quando duas ou mais camadas precisam ficar
  legíveis; calcular/medir com sensor, focal, distância de foco, abertura e círculo
  de confusão apropriado, depois confirmar na projeção/tela de destino;
- spherical/anamorphic e squeeze;
- macro/diopter/close-focus quando aplicável;
- filtro e densidade;
- limite de peso, mecânica, montagem e foco;
- alternativa de pacote e teste comparativo.

Não escreva `85 mm f/1.2` como sinônimo de retrato. Sem sensor, distância,
blocking, foco, luz e formato de entrega, isso é um rótulo. Em cinema, distinguir
F-stop geométrico de T-stop/transmissão quando especificar exposição.

### 3. Luz, exposição e materiais

Para cada `LIGHT-STATE-ID`, registrar:

```text
MOTIVAÇÃO: fonte diegética, natural, gráfica ou expressionista e sua regra
GEOGRAFIA: direção/altura/azimute; relação com blocking e câmera
QUALIDADE: tamanho aparente, distância, dureza, wrap, edge e falloff
CONTROLE: fill, negative fill, flags, grids, spill, haze e reflexos
VALORES: prioridade de pele/produto/fundo; contraste em stops ou teste equivalente
COR: CCT/tint relativo, mistura, practicals e cores de tensão
EXPOSIÇÃO: âncora, proteção de highlights, sombras aceitáveis e latitude para pós
MATERIAIS: pele, metal, vidro, líquido, tecido, tela, rótulo, embalagem e logo
CONTINUIDADE: estado por beat, direção, intensidade, atmosfera e mudanças permitidas
EXECUÇÃO: método/fixtures apenas depois da intenção; energia, flicker, rig e segurança
FALLBACK: clima, locação, potência, espaço, reflexo ou impossibilidade de rig
```

Não usar `golden hour volumetric`, `dark noir` ou `soft cinematic light` como
especificação final. Traduzir em posição solar/fonte, janela temporal, direção,
qualidade, contraste, cor, haze, exposição, continuidade e plano de contingência.

### 4. Dinâmica temporal

Para cada `TIME-STATE-ID`, decidir:

- timebase/master de entrega;
- fps de captura/geração;
- velocidade final e conform;
- shutter angle/tempo e motion blur;
- ação real que cabe na duração;
- rampas e ponto/motivo da mudança;
- flicker, rolling shutter, sync, strobe e tela;
- handles e continuidade com planos vizinhos;
- áudio síncrono ou desenho posterior;
- teste de movimento real ou no modelo-alvo.

`120 fps` não significa automaticamente impacto. Alta velocidade pode diluir
energia, exigir mais luz, expor arte/VFX e destruir timing cômico. `24 fps` não
produz cinema sozinho. Time-lapse/hyperlapse deve comprimir uma transformação que
o público precisa perceber.

### 5. Look e acabamento

Não selecionar um rótulo como `blockbuster`, `A24`, `cyberpunk` ou `high fashion`
sem decompor:

- faixa de valores e curva de contraste;
- densidade de cor e saturação relativa;
- prioridade de pele e cor de marca/produto;
- matiz de highlights, mids e shadows;
- roll-off, toe e black floor;
- textura, nitidez, diffusion, halation, grain e noise;
- materiais, arte e fontes que criam o look antes do grade;
- show LUT/look transform, monitoramento e transform de saída;
- integração real/IA/VFX e trims por plataforma.

Use `LOOK-ID` e descreva fenômenos observáveis. Nome de filme, produtora ou
movimento cultural pode ser referência de conversa, nunca parâmetro suficiente.

## Pacote de câmera e captura real

Quando houver filmagem, o DP entrega `DP-SYS-ID` com:

- requisito de latitude, highlight roll-off, pele e reprodução de produto;
- câmera/sensor candidatos e motivo;
- resolução, codec, bit depth, gamut/log e aspect ratio;
- base ISO/exposure index proposto;
- timebase, fps e shutter por estado;
- white balance/tint e política de mudança;
- ND/IRND, polarizador, diffusion e efeitos;
- pacote óptico principal + alternativa;
- suporte/rig, foco, wireless, monitoramento e show LUT;
- charts, metadata, VFX plates, lens grids/distortion e tracking;
- mídia, energia, dados, checksum e handoff de cor;
- dependências de locação, equipe, agenda, custo e segurança;
- testes que confirmam ou derrubam o pacote.

Equipamento sem vínculo com plano é lista de compras. Requisito sem proposta de
execução também é incompleto.

## Fotografia em IA e híbrido

Separe três coisas:

1. **intenção perceptiva** — vale para qualquer modelo;
2. **controle disponível** — reference image, first/last, motion reference, V2V,
   white model, camera control, keyframes, LoRA/adapter etc.;
3. **vocabulário do modelo** — só usar depois de confirmar surface/mode/versão.

Em IA, preferir:

```text
posição e distância aparentes
→ perspectiva/campo e profundidade
→ composição inicial/final
→ trajetória, velocidade, inércia e parada
→ fonte, direção, qualidade, contraste e material
→ motion cadence/blur observável
→ look por fenômenos
```

Milímetros, marca de câmera, lente vintage ou T-stop podem ser úteis para gerar
associação estética, mas não garantem física nem comportamento óptico. Quando o
modelo não expõe esses controles, registrar como `equivalente perceptivo`, não
como dado técnico de captura.

Para movimento complexo, decidir qual input carrega cada controle:

- frame inicial: composição/identidade/estado;
- frame final: chegada;
- motion reference: path/timing/easing;
- white/clay pass: geografia/blocking/câmera;
- V2V: performance e câmera preservadas;
- look key: luz/material/cor;
- plates/masks: produto, rosto, mãos, texto e logo.

## Card obrigatório por plano

Cada `PLAN ID` recebe:

```text
FUNÇÃO / BEAT / EFEITO NO PÚBLICO
POV E DISTÂNCIA EMOCIONAL
BLOCKING: ENTRY → TRIGGER → MID → EXIT
START/MID/END FRAME + INFORMAÇÃO NAS BORDAS
POSIÇÃO: ALTURA / DISTÂNCIA / EIXO / ORIENTAÇÃO
PERSPECTIVA/CAMPO/FORMATO
LENTE: FAMÍLIA / FOCAL / T-STOP / FOCO / DOF / FILTRO / COMPORTAMENTO
MOVIMENTO: CAM-MOV-ID / PATH / SPEED / ACCEL / STOP / HOLD / RIG
DINÂMICA: TIME-STATE-ID / FPS / SHUTTER / BLUR / RAMP / HANDLES
LUZ: LIGHT-STATE-ID / FONTE / DIREÇÃO / TAMANHO / CONTRASTE / COR / MATERIAL
EXPOSIÇÃO: ÂNCORA / PROTEGER / PODE CAIR / MARGEM DE PÓS
LOOK: LOOK-ID / TEXTURA / COLOR PIPELINE
EXECUÇÃO: REAL / IA / VFX / HÍBRIDO + INPUTS/CONTROLES
CONTINUIDADE COM PLANO ANTERIOR/SEGUINTE
TESTE / SINAL DE FALHA / FALLBACK / CONTRAINDICAÇÃO
```

Se o plano for gerado, campos físicos podem usar equivalentes perceptivos, mas
não podem desaparecer. Se for filmado, parâmetros técnicos precisam ser
confirmados ou marcados `PROPOSTO/TESTAR`.

## Testes que fecham decisões

O plano de testes deve alterar uma variável por vez e dizer qual escolha será
feita a partir do resultado:

- três posições reais com campo equivalente;
- duas famílias de lente em rosto/produto/bordas/flare/foco;
- T-stops e distância de foco na ação real;
- clean versus filtros/densidades;
- luz/material/exposição com pele, produto, label, vidro, metal e tela;
- movimento em duração real, com aceleração, parada, foco e rig;
- fps/shutter sob a ação, practicals e telas;
- show LUT, cor de marca, pele, highlight e roundtrip VFX/color;
- first/last, motion reference ou V2V no modelo-alvo;
- plano montado entre vizinhos e com som.

Teste que não muda uma decisão é demonstração, não teste.

## Veto de qualidade

Reprovar a passagem de fotografia se ocorrer qualquer um:

- preset ou adjetivo substitui mecanismo;
- câmera/lente famosas aparecem sem requisito ou teste;
- focal sem sensor/formato e posição/distância quando captação real;
- plano principal exige simultaneamente primeiro plano próximo e fundo legível,
  mas a profundidade de campo prevista não cobre ambos e nenhuma estratégia de
  foco, stop, distância, split-field, composição ou redesign foi escolhida;
- movimento sem start, gatilho, trajetória, evento, stop e hold;
- fps sem timebase, shutter, ação e consequência de luz;
- luz sem fonte, geografia, contraste, exposição e material;
- grade prometida para corrigir captação sem informação;
- plano gerado cita equipamento como se fosse metadata real;
- técnica não muda percepção, narrativa, produto ou montagem;
- nenhuma alternativa simples ou contraindicação foi considerada.

## Critério de pronto

A fotografia está pronta quando outra equipe consegue:

- entender o ponto de vista sem o DP explicar oralmente;
- testar e escolher pacote sem adivinhar intenção;
- montar rig, luz, foco e exposição por plano;
- traduzir o mesmo plano para IA sem perder perspectiva, dinâmica ou luz;
- identificar o que é proposta, o que foi testado e o que está confirmado;
- reconhecer imediatamente quando um output trai a direção.
