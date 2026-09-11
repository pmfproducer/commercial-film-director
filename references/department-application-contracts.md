# Contratos de aplicação por departamento

## Regra central

Conhecimento de área só entra no filme quando modifica uma decisão, um artefato e
um handoff. Cada departamento trabalha pelo mesmo contrato:

```text
RECEBE — decisões e materiais a montante
PERGUNTA — problema que a área precisa resolver
DECIDE — escolhas sob sua responsabilidade
APLICA — onde isso aparece no filme e nos planos
REGISTRA — arquivo/IDs/estados que preservam a decisão
ENTREGA — o que a próxima área recebe
TESTA — evidência que confirma ou derruba a solução
REPROVA — falha que impede o handoff
```

Não produzir parecer isolado. Atualizar o documento canônico da fase e os IDs
consumidos pelos departamentos seguintes.

## 1. Estratégia e pesquisa

### Recebe

Briefing, fatos da marca/produto, público, contexto, mandatories, evidências,
restrições, formato, veiculação e materiais atuais.

### Decide e aplica

- problema de comunicação que o filme resolve;
- comportamento/percepção a mudar;
- tensão humana específica;
- proposição legítima e prova filmável;
- papel causal/probatório da marca;
- critério observável de sucesso;
- fatos, hipóteses, perguntas decisórias e claims proibidos.

### Registra e entrega

Preenche `01_BRIEF_ESTRATEGICO.md`, `00_SOURCE_MANIFEST.md` e decisões no estado.
Entrega à criação um contrato que permite dizer sim/não a uma ideia.

### Testa/reprova

Reprovar se o “insight” é tema abstrato, se a prova depende de locução para existir,
se qualquer marca cabe ou se hipótese virou fato.

## 2. Direção criativa

### Recebe

Contrato do briefing, tensão, proposição, prova e limites.

### Decide e aplica

- mecanismo filmável da ideia;
- dispositivo de narrativa/demonstração/documento/coreografia/comédia/mundo;
- imagem ou acontecimento memorável;
- função do produto/marca na causalidade;
- uso AI-native essencial, quando houver;
- rota recomendada, trade-offs e proibições.

### Registra e entrega

Preenche `02_ROTAS_E_DIRECAO.md` e `00_DIRECTION_LOCK.md`. Entrega ao roteiro uma
direção escolhida, não um moodboard de opções.

### Testa/reprova

Retirar IA, marca e imagem central separadamente. Reprovar se o filme continua
igual sem elas, se a rota é apenas estética ou se o diretor não recomenda uma.

## 3. Roteiro

### Recebe

Direção travada, público, duração, formatos, produto, mandatories e proibições.

### Decide e aplica

- protagonista/portador do POV, desejo, obstáculo e mudança;
- beats com estado de entrada, ação, gatilho, virada e saída;
- ordem de informação e progressão/escalada;
- prova/papel do produto;
- fala, texto, offscreen e silêncio;
- end state, assinatura e arquitetura dos cutdowns.

### Registra e entrega

Entrega primeiro uma versão isolada em `departments/script/`. Após revisão e
aceite do diretor, integra `03_ROTEIRO_LITERARIO.md` com cabeçalho de cena,
ação, personagem, diálogo e silêncio. Somente então deriva `03_ROTEIRO_AV.md`
com `BEAT ID`, duração, vídeo, áudio, texto, função e transição. Entrega ao
diretor ações dirigíveis, não apenas copy.

### Testa/reprova

Remover cada beat e verificar perda. Ler em tempo real. Reprovar beat cuja entrada
e saída são iguais, ação descrita como emoção abstrata ou produto intercambiável.
Se o diretor pedir `MORE_RESEARCH` ou `REVISE`, não sobrescrever a versão anterior;
abrir nova rodada vinculada.

## 4. Direção de cena, casting e performance

### Recebe

Roteiro, tese do diretor, arco, mundo preliminar, produto/props e restrições.

### Decide e aplica

- ponto de vista e subtexto por beat;
- casting por comportamento, corpo, voz, timing e relação;
- objetivo, obstáculo, ação jogável e mudança de tática;
- posições, trajetórias, distâncias, eyelines, oclusões e contato;
- performance de mãos/prop/produto, respiração, olhar e ritmo;
- o que câmera, som e corte percebem ou não percebem;
- source performance/motion reference quando IA não sustenta atuação por texto.

### Registra e entrega

Preenche `04_MAPA_CENA_PERFORMANCE.md` e o tratamento. Entrega ground plan,
blocking e estados para fotografia, arte, som, storyboard e continuidade.

### Testa/reprova

Ensaiar a mesma cena com câmera fixa, ator fixo e coreografia conjunta. Reprovar
nota “mais natural/intenso”, microexpressão sem ação, eyeline impossível ou
blocking desenhado só para movimentar câmera.

## 5. Direção de fotografia

### Recebe

Tese, roteiro, mapa de performance/blocking, mundo/arte preliminar, produto,
formatos, rotas real/IA/VFX e limitações de produção.

### Decide e aplica

- relação do espectador e evolução visual;
- posição, altura, distância, eixo e composição;
- formato/sensor, perspectiva, família de lentes, foco e filtros;
- movimento/imobilidade com trajetória e rig;
- timebase, fps, shutter e motion blur;
- fonte, geografia, qualidade, contraste, cor e exposição;
- resposta de pele, produto, material e atmosfera;
- show look, monitoramento, captura, dados, VFX e testes;
- equivalentes perceptivos e controles quando o plano é gerado.

### Registra e entrega

Preenche `05_DIRECAO_FOTOGRAFIA.md` e IDs `DP-SYS`, `CAM-MOV`, `LIGHT-STATE`,
`TIME-STATE` e `LOOK`. Entrega cards ao storyboard, câmera/grip/gaffer, IA, VFX,
editorial e color.

### Testa/reprova

Aplicar `references/cinematography-decision-engine.md`. Reprovar preset, focal sem
contexto, movimento decorativo, luz sem exposição/material ou gear list sem plano.

## 6. Production design, props, figurino e HMU

### Recebe

Tese, roteiro, performance/blocking, fotografia preliminar, produto e exigências
de fidelidade/VFX/IA.

### Decide e aplica

- tese do mundo e regra espacial/material;
- found/adapted/built/miniature/3D/generative/hybrid;
- arquitetura, circulação, zonas de poder e ação;
- materiais, set dressing, cor e resposta à luz;
- props operacionais/narrativos/sonoros/hero e seus estados;
- produto, escala, orientação, contato, label/logo e pós;
- silhueta, figurino, cabelo, maquiagem, desgaste e duplicatas;
- o que precisa existir fisicamente para performance, contato, luz e som.

### Registra e entrega

Preenche `05_DIRECAO_ARTE.md`, define `ENV/PRD/PRP/WDR` e alimenta
`07_ASSET_BIBLE.md`/manifesto. Entrega geografia e estados a fotografia,
continuidade, storyboard, produção, VFX e IA.

### Testa/reprova

Testar blocking real, ação do prop, leitura do produto, tecidos/materiais sob a luz
e continuidade de estados. Reprovar paleta sem matéria, cenário sem ação, prop
decorativo ou produto sem fidelidade e pós.

## 7. Montagem

### Recebe

Roteiro, beats, direção, performance, decupagem, duração, formatos e som.

### Decide e aplica

- ordem das descobertas e diferença entre o que público/personagem sabem;
- tratamento do tempo, compressão, elipse, repetição e respiro;
- condição de corte ou continuidade por beat;
- must-have, performance choice, POV pivot, geography, bridge, compression,
  brand proof e utility;
- handles, transições, cutdowns e end frame;
- cobertura necessária antes de filmar/gerar.

### Registra e entrega

Preenche a seção editorial de `05_ARQUITETURA_MONTAGEM_SOM.md`, exige função na
decupagem e finaliza em `11_MONTAGEM_SOM_POS.md`. Entrega ao diretor/DP/storyboard
as operações que cada plano precisa habilitar.

### Testa/reprova

Montar animatic no tempo real, mudo e com som. Reprovar cobertura “wide/medium/
close” protocolar, B-roll “para dinamismo”, corte só na batida ou duração sem handles.

## 8. Sound design, voz e música

### Recebe

POV, beats, performance, mundo/material, montagem, produto, diálogo e duração.

### Decide e aplica

- ponto de escuta e distância sonora;
- eventos on/offscreen, prelap, ataque, corpo e cauda;
- production sound, respiração, Foley, ambientes, SFX e silêncio;
- motivo sonoro do produto/marca;
- função da música antes de gênero: condução, contraponto, ritual, memória etc.;
- entrada/saída, hit points, densidade, timbre, stems e direitos;
- o que precisa ser gravado, criado, sintetizado, licenciado ou reconstruído.

### Registra e entrega

Preenche `05_ARQUITETURA_MONTAGEM_SOM.md`, sound events/cues na decupagem e cue
sheet em `11_MONTAGEM_SOM_POS.md`. Entrega áudio ao animatic, geração e mix.

### Testa/reprova

Ouvir sem imagem e assistir sem som. Reprovar “trilha inspiradora”, som adicionado
depois, música repetindo imagem, som/motivo que contradiz o estado físico ou evento
visual sem consequência sonora/material.

## 9. Storyboard, overhead, previs e animatic

### Recebe

Roteiro, direção, blocking, fotografia, arte, montagem, som, assets e duração.

### Decide e aplica

- painel rough versus execution;
- composição e estados entry/mid/exit;
- geografia, eixo, campo, câmera, luz e oclusões;
- necessidade de corte, keyframes e continuidade;
- timing real, áudio temporário e handles;
- overhead/white model/techvis quando texto não resolve espaço/rig.

### Registra e entrega

Preenche `08_STORYBOARD_PREVIS.md`, salva boards/overheads/animatic e preserva
`PLAN/FRAME/ASSET/DP` IDs. Entrega planos visuais testados à produção e execução.

### Testa/reprova

Reprovar painel bonito sem função, board incompatível com blocking/lente/luz,
rough tratado como master ou animatic que não testa duração e som.

## 10. Produção, AD, câmera/grip/DIT e gaffer

### Recebe

Decupagem, documentos de departamentos, boards, locações/assets, rotas por plano,
prazo, orçamento e requisitos de entrega.

### Decide e aplica

- ordem e agrupamento operacional sem perder IDs narrativos;
- recursos, equipe, agenda, dependências, resets e contingências;
- pacote de câmera, rig, foco, monitoramento, mídia, energia e dados;
- execução de luz, controle, potência, flicker, clima e continuidade;
- permissões, risco e aprovações humanas para rig/veículo/altura/água/energia;
- capture/stock/3D/VFX/IA/hybrid e fallback por plano.

### Registra e entrega

Preenche `09_PLANO_PRODUCAO_HIBRIDA.md` e `09_PLANO_GERACAO_IA.md`. Entrega
chamada, shot order, dependências, plates/data e testes para execução e pós.

### Testa/reprova

Reprovar recurso sem função, cronograma que ignora reset/luz/dados, rig não
verificado, plano sem fallback ou custo/segurança tratados como detalhe posterior.

## 11. Assets, VFX e IA

### Recebe

Plano dirigido, boards, estados, documentos de fotografia/arte/performance/som,
produto, modelo/surface/mode e fidelidade exigida.

### Decide e aplica

- master, variant, state e version;
- asset/ref e responsabilidade única;
- practical/in-camera/plate/2D/3D/VP/generative/hybrid;
- first/last, motion reference, performance source, V2V e comp;
- invariantes, variáveis, ponte causal e risco intermediário;
- plates, mattes, lens/light/color data e post branding;
- modelo, surface, mode, inputs, limite de tentativa e fallback.

### Registra e entrega

Preenche asset bible/manifesto, plano IA e shot packets. Mantém `ASSET/PLAN/FRAME`
IDs e logs. Entrega material validado à montagem, VFX, cor, som e QC.

### Testa/reprova

Testar primeiro o risco central. Reprovar referência sem função, output bonito sem
plano, identidade/produto/física quebrados, prompt decidindo cena ou modelo
escolhido por fama.

## 12. Color, finishing, branding e entrega

### Recebe

OCF/outputs, edit lock, show look, metadata, VFX, áudio, fontes oficiais, matrizes
de versão e especificações.

### Decide e aplica

- color management, look, balance e output transforms;
- match real/IA/VFX, pele, produto e cor de marca;
- grain, halation, denoise, sharpen, graphics, text/UI/captions;
- conform, mix, loudness quando especificado, codec, resolução e trims;
- QC narrativo, visual, sonoro, técnico e de versões.

### Registra e entrega

Preenche `11_MONTAGEM_SOM_POS.md` e `12_QA_MASTER_VERSOES.md`. Entrega masters
somente após gates humanos e técnicos.

### Testa/reprova

Reprovar LUT como solução total, texto gerado tratado como final, VFX sem roundtrip,
versão amputada, mix não verificada ou arquivo chamado FINAL antes da aprovação.

## Handoff mestre

Ao concluir uma fase, registrar:

```text
DECISÕES TRAVADAS
IDS/ESTADOS CRIADOS OU ALTERADOS
ARQUIVOS CANÔNICOS
HIPÓTESES/TESTES ABERTOS
O QUE A PRÓXIMA ÁREA DEVE PRESERVAR
O QUE ELA PODE PROPOR
CONDIÇÃO QUE OBRIGA VOLTAR UMA FASE
```

Isso é o que impede cada nova sessão ou departamento de inventar outro filme.
