# Critica independente — Volvo Trucks, *The Epic Split* (2013)

## Escopo e regra de honestidade

Esta e uma auditoria adversarial dos artefatos disponiveis. Nao e declaracao de
visionamento continuo nem de escuta humana. Foram inspecionados:

- `research/methods/INSTRUMENTED_AV_REVIEW.md`;
- aquisicao, manifesto, metadados e CSV de candidatos;
- 20/20 folhas densas, com 307 amostras a cada 0,25 s;
- waveform integral, relatorio EBU R128 e resultado de `silencedetect`;
- `transcript_reviewed.md` e a legenda humana inglesa que ele resume;
- `research/review-packs/epic_split/instrumented_review_notes.md`;
- `research/films/2013_VOLVO_EPIC_SPLIT_TECHNICAL_PASS.md`;
- seis fichas atomicas ligadas: upload Volvo, entrevista do motorista, claim
  tecnico Volvo, entrevista de Andreas Nilsson, case Forsman & Bodenfors e
  creditos Vimeo/Littlemachine.

Os quadros sustentam composicao, variacao aproximada de escala e distancia,
presenca de cartelas, paleta aparente e sucessao de estados. Eles nao sustentam
aceleracao, trajetoria continua, velocidade, estabilizacao, natureza do movimento
de camera, ausencia de costura, microtiming, performance vocal, separacao de
fontes sonoras ou hierarquia do mix.

## Veredito

**NAO PROMOVER.** O estado correto permanece
`LEITURA_TECNICA_INSTRUMENTADA_PARCIAL + REVIEW_PACK_BUILT_NOT_WATCHED`.

O pack e forte para identidade da copia de plataforma, macrocomposicao,
progressao espacial amostrada, texto corporativo, creditos essenciais e relatos
de metodo. E insuficiente justamente para as duas promessas que tornam o caso
sedutor: continuidade de uma unica tomada e demonstracao causal da precisao do
sistema.

O filme pode ser estudado como `DEMONSTRACAO_DE_PRODUTO_ENCENADA` e como exemplo
de converter uma variavel reivindicada pela marca em variavel dramatica. Nao pode
ser usado como prova independente de steering, seguranca, superioridade,
`one-take`, ausencia de VFX ou eficacia comercial.

Esta critica cumpre a existencia do gate 9. O gate so fecha depois de a ficha
dispor os P0/P1 abaixo. Gates 4, 5, 6 e 8 permanecem parciais.

## Auditoria de versao

- A identidade fechada pertence ao derivado atual do upload oficial YouTube
  `M7FIvfx5J10`: 76,720 s, 5.343.760 bytes e SHA-256
  `1347b93aed1b019981b278895c6085f73a7f2535e861a624fcd9d07243bfc0ba`.
- O video mede 76,720 s; o audio, 76,694 s. A diferenca de cauda deve permanecer
  registrada.
- O arquivo e AV1/Opus produzido pela plataforma. Nao e mezzanine de 2013 e nao
  prova fidelidade de grade, compressao, mix ou cartelas ao master original.
- A pagina Vimeo/Littlemachine ancora quatro creditos, mas nao fecha versao,
  duracao ou master canonico.
- A legenda humana foi adquirida separadamente; os metadados do MP4 nao registram
  stream de captions ou descriptions.

Conclusao: gate 1 esta cumprido apenas para esta copia derivada identificada.

## Auditoria dos gates 4, 5, 6, 8 e 9

| Gate | Parecer independente | Fundamentacao |
|---:|---|---|
| 4 | **parcial, nao parcial forte** | 4 fps cobre a copia e mostra mudanca progressiva; o movimento continuo e a possivel costura sao o proprio argumento do filme. Sem playback, revisao de movimento e auditoria de seam/VFX, o requisito manual do protocolo nao foi cumprido |
| 5 | **parcial** | ha tempos e resumo confiavel derivados de legenda humana do upload oficial, mas `transcript_reviewed.md` deliberadamente nao preserva uma transcricao integral corrigida; performance e audio nao foram conferidos |
| 6 | **parcial** | waveform, EBU e ausencia de silencio tecnico no threshold escolhido nao distinguem, beat a beat, fala, musica, motores, ambiente, efeitos e silencio perceptivo |
| 8 | **parcial ate correcao** | o mapa central separa classes, mas a secao `Observado` ainda atribui efeitos de comparabilidade a simetria/repeticao e outras sinteses circulam sem rotulo local de inferencia |
| 9 | **cumprido quanto a existencia** | este parecer e a critica independente; disposicao na ficha e reauditoria ainda sao necessarias |

## P0 — bloqueios de promocao

### P0.1 — Continuidade aparente nao e `one-take` final provado

As 307 amostras mostram uma composicao visualmente continua entre a abertura e o
fade, e o detector nao encontrou candidatos acima de 0,28. Isso nao detecta
costura invisivel, cleanup, morph, speed ramp, estabilizacao, remocao de rig ou
outro VFX. Um threshold unico, especialmente diante de mudanca gradual, nao e
EDL nem auditoria forense.

O motorista declara que a execucao com Van Damme ocorreu em uma tomada. Essa
fonte tem autoridade para a experiencia dele, nao para certificar o arquivo final
sem edicao. O diretor usa `tomada` ao relatar o teste de musica; tambem nao publica
um breakdown de pos.

Correcao obrigatoria: usar `COMPOSICAO_APARENTEMENTE_CONTINUA_EM_AMOSTRAS` e
`UMA_TOMADA_COM_O_PERFORMER_SEGUNDO_O_MOTORISTA`. Recusar `one-take`,
`plano-sequencia`, `sem cortes` ou `feito integralmente em camera` como fatos ate
playback e fonte primaria de montagem/VFX/cleanup.

### P0.2 — Demonstracao encenada nao valida o claim corporativo

A distancia lateral entre os caminhoes muda e o corpo transforma essa distancia
em medida visual. A cartela diz que o teste foi montado para demonstrar
estabilidade e precisao do Volvo Dynamic Steering. O press release da propria
Volvo associa o sistema a autocentralizacao e estabilidade em marcha a re.

Isso nao isola contribuicoes do sistema, motoristas, pista, marcas no solo,
ensaio, velocidade, camera, rig ou pos-producao. Nao ha telemetria, protocolo,
controle, comparador, tolerancia, repeticao publicada ou teste independente.

Correcao obrigatoria: manter tres classes separadas — `CLAIM_DA_VOLVO`,
`DEMONSTRACAO_ENCENADA_OBSERVAVEL` e `VALIDACAO_INDEPENDENTE_AUSENTE`. A palavra
`teste` presente na cartela e no nome da serie nao muda essa classificacao.

### P0.3 — O stunt nao pode virar instrucao operacional nem prova de seguranca

Oito dias de ensaio sem o performer, linha externa usada como limite e uma area
fechada sao sinais positivos de preparacao. A cartela final e comunicacao ao
publico, nao safety case.

Faltam rig, redundancia contra queda, ponto de ancoragem, velocidade, distancia,
vento limite, medical, resgate, comunicacao, criterio de abort, autoridade de
stop, responsabilidade dos dois motoristas, coordenador creditado, risk
assessment e disposicao de VFX. Nenhuma inferencia a partir de frames resolve
essas lacunas.

Correcao obrigatoria: nenhum principio derivado deste caso pode recomendar
exposicao humana. `SPECTACLE_NEEDS_HUMAN_MEASURE` deve aceitar objetivo,
consequencia, escala ou proxy sem corpo em risco. Todo projeto novo exige desenho
por profissionais qualificados e uma alternativa sem pessoa exposta.

### P0.4 — Gates perceptivos e estado global permanecem abertos

Cobertura a 4 fps nao substitui movimento; legenda nao substitui transcricao
integral nem escuta; waveform nao e mapa perceptivo de som. A critica
independente nao supre esses gates. Nao autorizar `REVISAO_AV_INSTRUMENTADA`,
`VISTO_1X` ou `ANALISE_PROFUNDA`.

## P1 — correcoes obrigatorias antes do Atlas

### P1.1 — Gate 8 ainda tem vazamento de efeito dentro de observacao

`instrumented_review_notes.md:129-130`, sob `Observado`, diz que simetria e
repeticao material fazem pequenas mudancas de distancia ficarem comparaveis.
Simetria, repeticao, linhas e variacao de distancia sao observaveis; tornar a
mudanca comparavel e uma funcao inferida.

Correcao: mover o efeito para `INFERENCIA/TESTE` e formular o dado bruto como
`composicao aproximadamente simetrica, formas repetidas e linhas da pista
permanecem presentes nas amostras`. Gate 8 fica parcial ate a reclassificacao.

### P1.2 — Gate 5 exige transcricao, nao apenas resumo

O arquivo `transcript_reviewed.md` registra que o texto e resumo sem reproducao
integral da fala. Isso e util para estrutura e direito autoral, mas nao permite
auditar palavra, pausa textual, omissao, sobreposicao ou correspondencia completa
com a legenda humana.

Correcao: preservar internamente uma transcricao corrigida integral com fonte,
idioma e timecodes, mantendo no corpus publico apenas o resumo quando necessario.
Sem isso, gate 5 permanece parcial; sem escuta, performance continua aberta mesmo
depois do fechamento textual.

### P1.3 — Gate 6 ainda nao e mapa de som por beats

Os valores `-12,4 LUFS`, `5,1 LU LRA` e `-2,0 dBFS` true peak sao validos para a
copia. O waveform mostra energia ao longo do arquivo e o `silencedetect` a
-35 dB/0,3 s nao encontrou intervalo. Nenhum desses artefatos identifica fontes.

Correcao: criar tabela por beat com colunas separadas `FALA_DECLARADA`,
`MUSICA_DECLARADA`, `MOTOR/AMBIENTE_NAO_CONFIRMADO`, `EFEITO_NAO_CONFIRMADO`,
`SILENCIO_TECNICO_MEDIDO` e `FUNCAO_INFERIDA`. Ate escuta, nao afirmar que motores
estao audiveis, que musica mascara/revela mecanica, que ha contraponto ou que o
fade produz descompressao sonora.

### P1.4 — Mudanca de escala nao identifica camera nem movimento realizado

Os quadros mostram Van Damme e caminhoes diminuindo no quadro e mais estrada
entrando no campo. Nao identificam dolly, zoom, crane, camera vehicle, rig,
estabilizacao, velocidade, direcao relativa ou combinacao com pos. O movimento
lateral dos caminhoes e a marcha a re sao apoiados por fontes, mas sua qualidade
continua nao percebida.

Manter `REVEAL_SPENDS_INFORMATION` como prototipo de decupagem, nao aprendizado
demonstrado sobre equipamento ou tecnica de camera.

### P1.5 — Cor e luz sustentam contraste aparente, nao intencao ou fidelidade

As amostras sustentam azul/ciano no figurino, ouro/bege nos caminhoes/ambiente,
frentes escuras, pista cinza, sol baixo, contorno e flare aparente. Nao sustentam
LUT, wardrobe intent, temperatura, fonte sobre o rosto, filtros, exposicao,
continuidade em master ou decisao exclusiva da fotografia.

`humano frio contra maquina quente` pode permanecer prototipo. `a cor separa o
performer` e `o fundo torna precisao comparavel` devem ser tratados como funcao a
testar, nao efeito comprovado.

### P1.6 — Creditos essenciais nao autorizam autoria total

Vimeo/Littlemachine sustenta Andreas Nilsson, Ed Wild, Peter Brandt e Folke Film.
Forsman & Bodenfors e sustentada por case/entrevista. O conjunto nao fecha
criacao individual, segundo motorista, coordenacao de stunt, rig, camera/grip,
arte, wardrobe, cor, VFX, som, musica, cliente ou safety.

Correcao: preservar `CREDITOS_PARCIAIS_VERIFICADOS`; nao atribuir movimento,
paleta, costura, mix ou safety a uma pessoa apenas pelo cargo. Perfis de autores
e principios departamentais exigem ficha completa e fonte qualificada.

### P1.7 — Licenciamento musical foi declarado, nao auditado

Nilsson declara que testou musica de Enya sobre a tomada no local e que houve
negociacao posterior de licenca. Isso sustenta metodo e existencia declarada de
negociacao. Nao publica documento de licenca, faixa/titulo na ficha atomica,
autores, master/publishing, fee, territorio, prazo, midias, aprovacoes ou creditos
contratuais.

Correcao: usar `LICENCIAMENTO_NEGOCIADO_SEGUNDO_O_DIRETOR`, nao `LICENCA
VERIFICADA`. Como principio, musica temporaria com potencial de permanencia gera
gate juridico antes de travar montagem; reacao de equipe nao autoriza compra nem
prevê recepcao.

### P1.8 — A cartela de safety e tardia e limitada

A cartela entre aproximadamente 01:12,75 e o fim e legivel nas amostras e informa
profissionais/area fechada. Ela aparece depois do stunt, nao demonstra prevencao,
nao desencoraja toda imitacao e nao substitui comunicacao apropriada ao canal.

Correcao: separar `DISCLOSURE_AO_PUBLICO` de `EVIDENCIA_DE_PRODUCAO_SEGURA`. Em
projetos novos, mensagem, timing, legibilidade, idioma e adequacao por canal sao
parte do plano, mas nunca o safety system.

### P1.9 — O corpo torna o claim intuitivo, mas pode eclipsar produto e trabalho

Van Damme oferece escala corporal e memoria cultural. Tambem pode concentrar
recordacao na celebridade e romantizar risco, enquanto motoristas, ensaio e
sistema ficam invisiveis. O pack nao contem brand-lift, recall por elemento,
recepcao de motoristas/compradores ou teste de compreensao do claim.

Correcao: `SPECTACLE_NEEDS_HUMAN_MEASURE` precisa incluir teste de brand linkage,
compreensao do mecanismo e reconhecimento do trabalho invisivel. Celebridade nao
e evidencia de clareza do produto.

### P1.10 — Estrategia e resultados pertencem ao case, nao ao artefato

Forsman & Bodenfors declara publico B2B ampliado, YouTube/PR, orcamento de midia
limitado e resultados. A propria ficha atomica registra ausencia de dataset,
metodologia, periodo, controle e atribuicao causal.

Correcao: estudar a distribuicao como sistema declarado; nao converter viralidade,
interesse, acao ou market share em efeito comprovado deste filme isolado.

## P2 — pesquisa e precisao adicionais

1. Adquirir, se autorizado, o mezzanine ou master de 2013 e comparar duracao,
   frames, cartelas, grade, compressao, audio e legendas com o derivado atual.
2. Realizar playback critico com imagem e som; fazer auditoria de continuidade em
   velocidade normal e quadro a quadro, com atencao a costuras, speed changes,
   estabilizacao, cleanup e fades.
3. Localizar breakdown primario de camera, rig, VFX/cleanup, montagem e stunt;
   identificar ambos os motoristas, coordenacao, autoridade de stop e contingencia.
4. Obter ficha completa de creditos em arquivo de premio, produtora ou agencia e
   reconciliar rotulos antes de criar perfis de pessoa.
5. Preservar transcricao integral corrigida e realizar escuta humana para voz,
   musica, motores, ambiente, efeitos, sincronismo e mix.
6. Verificar documentacao musical: faixa, autoria, master, publishing, escopo da
   licenca e creditos, sem publicar material protegido alem do necessario.
7. Buscar telemetria, protocolo de engenharia ou teste independente do Dynamic
   Steering; separar desempenho do sistema de execucao do stunt.
8. Adquirir cutdowns, bastidores, pecas tecnicas e adaptacoes de PR antes de
   afirmar que claim, safety e brand linkage sobrevivem por canal.
9. Buscar dados de recepcao com metodologia, incluindo compradores, motoristas e
   influenciadores, antes de atribuir resultado comercial ao filme.

## Auditoria por departamento

### Direcao e roteiro

**Sustentado:** a informacao visual e liberada progressivamente; a fala resumida
prepara identidade/corpo antes da abertura espacial; a cartela tecnica entra
depois da acao; Nilsson declara a ambicao emocional/poetica.

**Inferido:** que o atraso aumenta curiosidade, que o paralelo humano-tecnico
melhora compreensao e que a atribuicao tardia fortalece a marca. Esses efeitos
exigem teste de audiencia.

### Decupagem, camera e montagem

**Sustentado:** rosto/corpo, caminhoes, pista e cartelas mudam de proporcao e
presenca; distancia abre e reduz nas amostras; zero candidatos foram encontrados
no threshold declarado.

**Nao sustentado:** one-take final, plano-sequencia, tecnica de camera, direcao e
velocidade continuas, suporte, estabilizacao, ausencia de costura, limpeza ou VFX,
ritmo realizado e contagem exata de planos.

### Fotografia, cor e arte

**Sustentado:** paleta aparente azul/ouro/escuro/cinza, composicao aproximadamente
simetrica, linhas de pista, repeticao dos veiculos, sol baixo e flare/contorno
aparentes na copia de plataforma.

**Nao sustentado:** intencao cromatica, efeito emocional, camera, lente, filtro,
stop, luz sobre rosto, LUT, grade do master, practical/VFX ou autoria individual
de cada decisao.

### Som e musica

**Sustentado por fonte/medicao:** tempos da legenda, musica de Enya segundo fonte
de processo, negociacao de licenca segundo o diretor, waveform e valores EBU.

**Nao sustentado:** titulo/creditos musicais completos no pack, termos da licenca,
performance, motores/ambientes realmente audiveis, prioridade de voz, dinamica
percebida, contraponto, mascaramento, espacialidade e sincronismo.

### Produto, legal e claim

**Sustentado:** cartela e Volvo reivindicam estabilidade/precisao do Dynamic
Steering; a imagem mostra dois veiculos e distancia lateral variando.

**Nao sustentado:** causalidade tecnica isolada, eficacia, superioridade,
seguranca, tolerancia, repetibilidade, conformidade, telemetria ou resultado
comercial. A demonstracao pode comunicar um claim sem validá-lo.

### Producao, stunt e safety

**Sinal positivo declarado:** oito dias de ensaio sem Van Damme, linha visual de
limite, uma tomada com performer segundo motorista e area fechada/profissionais.

**Lacuna critica:** rig, redundancia, velocidade, vento, medical, resgate,
comunicacao, abort, autoridade, segundo motorista, coordenador, risk assessment e
pos-producao. Nao transformar aparente simplicidade em receita de risco.

## Disposicao exigida para o Atlas

### Podem permanecer candidatos, com reformulacao e escopo

1. `CLAIMED_PRODUCT_VARIABLE_AS_DRAMATIC_VARIABLE` — transforme uma propriedade
   reivindicada pela marca em mudanca visual mensuravel na encenacao; isso nao
   valida a propriedade.
2. `STAGED_DEMONSTRATION_IS_NOT_VALIDATION` — claim corporativo, artefato visivel
   e teste independente sao classes diferentes.
3. `CREW_REACTION_IS_NOT_AUDIENCE_EVIDENCE` — reacao no set pode gerar hipotese,
   nunca resultado de audiencia.
4. `SINGLE_ACTION_REQUIRES_MULTI_DEPARTMENT_CHOREOGRAPHY` — simplicidade aparente
   exige integracao de ensaio, camera, luz, veiculos, safety e contingencia; nao e
   autorizacao para stunt.

### Permanecem prototipos

- `REVEAL_SPENDS_INFORMATION` — cada mudanca aparente de escala deve liberar
  informacao; efeito e movimento realizado exigem playback.
- `SPECTACLE_NEEDS_HUMAN_MEANING` — extraordinario precisa de objetivo ou
  consequencia humana, nao necessariamente corpo exposto.
- contraste cromatico como separacao funcional entre pessoa, maquina e ambiente;
  intencao e efeito nao verificados.
- atraso da cartela de produto; testar compreensao, brand linkage e legibilidade.
- continuidade aparente como tensao; nunca pressupor one-take ou ausencia de pos.
- preservacao de claim e disclosure em cutdowns; nenhum corte foi adquirido.

### Devem ser recusados

- **RECUSAR:** `one-take` ou `feito em camera` inferido de zero candidatos.
- **RECUSAR:** stunt publicitario equivale a teste independente de produto.
- **RECUSAR:** cartela de safety prova que a producao foi segura.
- **RECUSAR:** ensaio e area fechada bastam para replicar exposicao humana.
- **RECUSAR:** a marca `provou` estabilidade, precisao ou superioridade.
- **RECUSAR:** reacao emocional da equipe valida audiencia ou mercado.
- **RECUSAR:** credito de diretor/DP/editor prova autoria exclusiva de forma,
  cor, movimento, costura ou som.
- **RECUSAR:** negociacao de licenca relatada equivale a documento juridico
  auditado.
- **RECUSAR:** numeros de case sem metodologia provam causalidade comercial.

## Condicoes para reauditoria e fechamento do gate 9

1. rebaixar gate 4 de `parcial forte` para `parcial` enquanto nao houver playback
   e auditoria de costura;
2. manter gates 5 e 6 parciais e registrar que resumo nao e transcricao integral;
3. mover o efeito de comparabilidade de `Observado` para `Inferencia/Teste` e
   reabrir gate 8 ate essa correcao;
4. substituir qualquer atalho de `one-take` por continuidade aparente + relato
   atribuido de uma tomada com performer;
5. manter claim, demonstracao encenada e validacao independente separados;
6. incorporar limites de safety, creditos, licenca musical e resultados de case;
7. dispor cada principio Atlas nas classes acima sem promover prototipos;
8. preservar o estado global parcial mesmo depois de fechar apenas o gate 9.
