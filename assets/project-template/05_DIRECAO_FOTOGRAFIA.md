# 05 — Direção de fotografia

- Projeto: `{{PROJECT_ID}}`
- Estado: TRABALHO
- Direção: `00_DIRECTION_LOCK.md`
- Performance/blocking: `04_MAPA_CENA_PERFORMANCE.md`
- Método: `references/cinematography-decision-engine.md`

## Contrato do DP

- O DP recebe: <<PREENCHER>>
- Pergunta visual que precisa resolver: <<PREENCHER>>
- Tese fotográfica em uma frase: <<PREENCHER>>
- Relação do espectador com sujeito/produto/mundo: <<PREENCHER>>
- Evolução visual do primeiro ao último beat: <<PREENCHER>>
- Decisões travadas nesta versão: <<PREENCHER>>

## Sistema mestre — `DP-SYS-001`

Para cada item marcar `PROPOSTO`, `TESTAR`, `CONFIRMADO` ou `N/A`.

### Formato e captura

- Rota: captação real / IA / VFX / híbrida: <<PREENCHER>>
- Requisitos de latitude, highlight roll-off, pele e produto: <<PREENCHER>>
- Sensor/formato/crop/de-squeeze propostos e motivo: <<PREENCHER>>
- Aspect ratios e proteção para versões: <<PREENCHER>>
- Resolução/codec/bit depth/gamut/log: <<PREENCHER>>
- Base ISO/EI e política de exposição: <<PREENCHER>>
- White balance/tint e mudanças permitidas: <<PREENCHER>>
- Monitoramento/show LUT/viewing pipeline: <<PREENCHER>>
- Metadata, charts, plates e dados para VFX/color: <<PREENCHER>>
- Pacote de câmera principal + alternativa: <<PREENCHER>>
- Dependências de equipe, locação, rig, custo e segurança: <<PREENCHER>>

### Estratégia de perspectiva e lentes — `LENS-SET-001`

- Posição/distância e relação espacial dominante: <<PREENCHER>>
- Campo de visão e formatos que precisam sobreviver: <<PREENCHER>>
- Família óptica principal e motivo: <<PREENCHER>>
- Sensor + focais por função: <<PREENCHER>>
- Distância câmera-sujeito e perspectiva desejada: <<PREENCHER>>
- T-stop de trabalho, foco, profundidade e close focus: <<PREENCHER>>
- Viabilidade de DOF/foco para camadas próximas e distantes — cálculo, app ou teste real: <<PREENCHER>>
- Contraste, flare, breathing, distorção, bokeh e roll-off: <<PREENCHER>>
- Spherical/anamorphic/squeeze quando aplicável: <<PREENCHER>>
- ND/IRND, polarizador, diffusion, grads e efeitos: <<PREENCHER>>
- O que rosto, mãos, produto, bordas e speculars precisam preservar: <<PREENCHER>>
- Alternativa mais simples e perda: <<PREENCHER>>
- Teste que confirma/derruba o pacote: <<PREENCHER>>

## Gramática de câmera e movimento

| CAM-MOV ID | Planos/beat | Função e efeito no público | Start frame/posição | Gatilho | Path/parallax e relação com blocking | Duração/velocidade/aceleração/easing | Evento revelado | Stop/hold | Suporte/rig/foco/repetibilidade | Sinal de falha | Fallback |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CAM-MOV-001 | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> |

### Imobilidade

- Quando a câmera deve permanecer imóvel e por quê: <<PREENCHER>>
- O que muda dentro do quadro: <<PREENCHER>>
- Por que lock-off é superior a movimento/corte: <<PREENCHER>>

## Dinâmica temporal

| TIME-STATE ID | Planos/beat | Timebase/master | FPS captura/geração | Shutter angle/tempo | Motion blur/cadência | Rampa/conform | Ação que cabe na duração | Flicker/sync/rolling shutter | Handles/áudio | Teste/falha |
|---|---|---:|---:|---|---|---|---|---|---|---|
| TIME-STATE-001 | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> |

## Estados de luz, exposição e materiais

| LIGHT-STATE ID | Beat/cena | Motivação/fonte | Direção/altura/azimute | Tamanho/qualidade/distância/falloff | Fill/negative/spill/haze | Contraste/valores | CCT/tint/cor relativa | Âncora de exposição/proteger/pode cair | Pele/produto/material/fundo | Practicals/execução/potência/flicker | Continuidade/fallback |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LIGHT-STATE-001 | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> |

## Look, textura e color pipeline — `LOOK-001`

- Faixa de valores, contraste e densidade: <<PREENCHER>>
- Saturação e cor de tensão por beat: <<PREENCHER>>
- Pele, produto e cor de marca: <<PREENCHER>>
- Highlights, mids, shadows, toe e black floor: <<PREENCHER>>
- Nitidez, diffusion, halation, grain e noise: <<PREENCHER>>
- Arte/materiais/luz que criam o look antes do grade: <<PREENCHER>>
- Input/look/output transforms e trims: <<PREENCHER>>
- Integração e matching real/IA/VFX: <<PREENCHER>>
- Anti-look e clichês proibidos: <<PREENCHER>>

## Tradução para IA/híbrido

- Equivalente perceptivo de posição/perspectiva/campo: <<PREENCHER>>
- Controle de trajetória/timing: prompt / motion ref / white model / V2V: <<PREENCHER>>
- Controle de luz/look/material: <<PREENCHER>>
- Campos técnicos que não devem ser fingidos como metadata real: <<PREENCHER>>
- O que plate/mask/comp precisa proteger: <<PREENCHER>>

## Plano de testes

| TEST ID | Decisão em disputa | Variável isolada | Setup/material | Critério observável | Resultado que escolhe A/B | Custo/ordem | Status |
|---|---|---|---|---|---|---|---|
| DP-TEST-001 | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | <<PREENCHER>> | PROPOSTO |

## Handoff e veto

- Câmera/grip/DIT recebem: <<PREENCHER>>
- Gaffer/elétrica recebem: <<PREENCHER>>
- Arte/VFX/IA recebem: <<PREENCHER>>
- Storyboard/editorial/color recebem: <<PREENCHER>>
- Contraindicações que obrigam voltar à direção: <<PREENCHER>>
