# Critica independente — Google Search, *Reunion* (2013)

## Escopo e regra de honestidade

Foram auditados:

- `research/films/2013_GOOGLE_REUNION_TECHNICAL_PASS.md`;
- `research/review-packs/reunion/instrumented_review_notes.md`;
- `research/review-packs/reunion/transcript_reviewed.md`;
- `research/review-packs/reunion/acquisition_notes.md`;
- `research/review-packs/reunion/review_manifest.json`;
- `research/review-packs/reunion/scene_candidates.csv`;
- 27/27 folhas densas, 4/4 folhas de candidatos, waveform e relatorio EBU;
- as nove fontes atomicas ligadas na technical pass.

Esta critica nao declara playback continuo nem escuta. A inspecao das folhas nao
autoriza inferir microtiming, movimento realizado, continuidade de movimento,
performance vocal ou experiencia de mix.

## Veredito

**NAO PROMOVER. MANTER GATES 4, 5 E 6 PARCIAIS. REABRIR GATE 8. GATE 9 FICA
REALIZADO COMO CRITICA, MAS NAO FECHADO ATE DISPOSICAO DOS P0/P1. BLOQUEAR
INGESTAO NO ATLAS.**

O pack e materialmente consistente: hash, duracao, contagens e origem convergem;
424 frames densos formam 27 folhas, 50 candidatos formam quatro folhas e o CSV
contem 50 linhas de dados. A versao e corretamente limitada ao upload oficial de
3:32, sem fingir que o primeiro corte ou os quatro filmes irmaos foram adquiridos.

O bloqueio decorre de cinco problemas prioritarios:

1. observacao visual ainda incorpora dialogo, relato historico e funcao;
2. UI encenada e descrita em alguns trechos como produto que de fato localiza ou
   altera a acao;
3. a ficha textual atribui emocao a fala que nao foi ouvida;
4. a estrutura especifica continua sob conflito de anterioridade com *Respect*;
5. a ausencia de consulta bilateral/historica impede usar o caso como precedente
   positivo de representacao segura da Particao.

## Estado dos gates

| Gate | Veredito independente | Razao |
|---:|---|---|
| 1 | **cumprido para a copia** | upload oficial, duracao e hash fechados; mezzanine, primeiro corte e obras irmas permanecem fora do escopo |
| 2 | **cumprido** | 27/27 folhas densas; 424 amostras a 0,5 s |
| 3 | **cumprido como inspecao** | 4/4 folhas e 50/50 candidatos; nao sao EDL |
| 4 | **parcial** | 2 fps nao resolvem inserts sub-0,5 s, flashes, transicoes, estabilidade ou movimento realizado |
| 5 | **parcial** | faixa humana inglesa lida, mas e traducao; sem roteiro, escuta, QA hindi/urdu e com um claim de performance indevido |
| 6 | **parcial** | mapa declarativo, waveform e EBU nao substituem cue sheet ou escuta; relatorio de `silencedetect` nao foi preservado no pack |
| 7 | **cumprido pela impossibilidade declarada** | CSV preservado e contagem final de planos recusada |
| 8 | **nao cumprido** | ha vazamentos entre observado, legenda, funcao narrativa e causalidade de produto |
| 9 | **critica realizada; fechamento pendente** | esta critica exige disposicao e reauditoria antes do Atlas |
| 10 | **cumprido como limite** | os documentos recusam movimento, mix e microtiming, embora claims locais ainda precisem de correcao |

O estado global deve permanecer
`LEITURA_TECNICA_INSTRUMENTADA_PARCIAL + REVIEW_PACK_BUILT_NOT_WATCHED`.

## Achados P0

### P0.1 — observado, legenda e inferencia continuam fundidos

`instrumented_review_notes.md:44` coloca `dialogo` na coluna
`OBSERVADO_NO_ARTEFATO`. Em `:47`, `neta confirma lembranca` e `Baldev relata
Particao` tambem aparecem como observacao, embora dependam da faixa textual. Em
`:89-90`, `planos mais estaveis` aparece sob `Observado nas amostras`, mas
estabilidade e movimento nao podem ser auditados a 2 fps.

Na technical pass, `:45` diz que resultados surgem `quando alteram a proxima
acao`, e `:48` diz que cor/locacao `diferenciam espacos` dentro de `Decisoes
observaveis`. Mudanca de acao e diferenciacao funcional sao leituras, nao pixels.

**Correcao exigida:**

- observado: pessoas, objetos, UI legivel, sucessao de espacos, matizes e
  enquadramentos nas amostras;
- fonte/legenda: memoria, nomes, Particao, parentesco e demais conteudo verbal;
- inferencia/teste: confirmacao, mudanca de estado, ponte geografica, separacao
  funcional por cor e estabilidade de camera.

Gate 8 nao pode fechar enquanto essas classes continuarem misturadas.

### P0.2 — produto visto nao e comportamento de produto validado

As folhas mostram interfaces Google, consultas digitadas e telas de resultado.
Elas nao demonstram que as buscas foram realizadas ao vivo, que os resultados
eram completos ou precisos, que a interface nao foi composta, nem que Search
causou contato, visto, viagem ou reencontro.

`instrumented_review_notes.md:193-194` chama de observado que Search aparece em
consultas que `localizam pistas e atualizam logistica`. A technical pass `:45`
diz que os resultados aparecem quando alteram a acao. Ambas as formulacoes
atribuem eficacia narrativa ao produto dentro da camada observacional.

**Correcao exigida:** separar literalmente tres classes:

1. `UI_DE_GOOGLE_SEARCH_VISIVEL_NA_ENCENACAO`;
2. `FONTE_DECLARA_INTEGRACAO_DE_FUNCOES_DE_SEARCH`;
3. `COMPORTAMENTO_AO_VIVO_ACURACIA_E_CAUSALIDADE_NAO_VALIDADOS`.

O fluxo seguro e `pessoa formula consulta -> tela encenada apresenta resultado
-> pessoa interpreta -> outro humano/instituicao confirma ou executa`. Pesquisa
de requisitos nao e candidatura, aprovacao de visto, compra de passagem nem
autorizacao de viagem.

### P0.3 — transcricao atribui performance sem escuta

`transcript_reviewed.md:19` registra `repeticao emocionada dos nomes`, apesar de
`:6` dizer que o audio nao foi ouvido e `:31-32` recusar conclusao sobre
paralinguagem e microperformance. `Emocionada` e claim de performance, nao
conteudo textual.

No mapa sonoro, `instrumented_review_notes.md:180`, `:182` e `:186` dizem
`nenhuma fala na faixa inglesa`. O que foi verificado foi ausencia de fala
**localizada pela legenda inglesa** nesses intervalos; sem escuta, nao se pode
afirmar ausencia de fala no audio. Em `:179`, `texto de memoria apenas` tambem
deve ser `texto de memoria localizado pela legenda`, para nao soar como mapa de
presenca sonora.

**Correcao exigida:** remover o adverbio de performance e trocar todas as
ausencias por `nenhuma fala localizada pela faixa de legenda inglesa`. Hindi,
urdu, pronuncia, pausa, choro, timbre e hierarquia do mix continuam abertos.

Gate 5 permanece parcial mesmo depois dessa correcao.

### P0.4 — conflito com *Respect* bloqueia a estrutura especifica

A fonte do Register documenta uma alegacao atribuida ao autor de *Respect*
(2012) e paralelos narrativos gerais. Ela nao prova copia, acesso, infracao ou
inocencia. O corpus nao contem a obra anterior, comparacao integral, roteiro
datado, resposta conclusiva ou parecer juridico.

Logo, a prudencia escrita em `instrumented_review_notes.md:203-210` esta correta,
mas precisa governar a disposicao do Atlas: `MEMORY_TO_SEARCHABLE_TOKENS` nao
pode ser promovido **a partir deste caso** enquanto conservar o pacote
Particao + amigo perdido + descendente investigador + busca digital + reencontro.

**Correcao exigida:** manter o principio como prototipo abstrato, adquirir e
analisar *Respect*, construir matriz de elementos comuns/especificos, registrar
transformacao e obter revisao juridica humana antes de reutilizar a estrutura.
Nao rotular nenhuma das obras como plagio ou prova de inocencia com o corpus
atual.

### P0.5 — trauma historico e friccao institucional nao estao validados

O pack registra historia familiar do diretor, imagens de Lahore fornecidas por
DP local e ausencia de evidencia de historiador, sobreviventes, consultores de
ambos os paises ou avaliacao de dano. Isso e um registro honesto de ausencia,
nao consulta demonstrada nem consenso.

A fonte oficial de visto tem escopo estreito, mas confirma que nacionais
paquistaneses permaneciam excecao a uma flexibilizacao em fevereiro de 2013. As
folhas passam de uma busca por requisitos a preparacao/viagem sem mostrar
candidatura, prazo, aprovacao, custo, elegibilidade ou risco. A elipse pode ser
dramaticamente funcional, mas nao pode ser ensinada como representacao segura de
acesso institucional.

**Correcao exigida:** classificar o caso como
`REPRESENTACAO_HISTORICA_E_SEGURANCA_CULTURAL_NAO_VALIDADAS`. Ele pode sustentar
uma regra de governanca — consulta, contestacao e friccao sao gates — mas nao um
precedente positivo de como representar a Particao, India, Paquistao, religiao,
nacionalidade ou processo de visto.

## Achados P1

### P1.1 — claims de camera excedem as folhas

As amostras sustentam campo amplo aparente, closeups aparentes, inserts, eixos de
olhar e alternancia de espacos. Nao sustentam `planos mais estaveis`, dolly,
handheld, velocidade, suavidade, foco puxado ou continuidade de movimento.

**Correcao:** retirar `mais estaveis`; manter enquadramentos aparentes e dizer que
qualidade/mecanica do movimento requer playback.

### P1.2 — cor, props e arte misturam recorrencia com funcao

As folhas sustentam verdes/quentes na loja, neutros/cinza/azulados em outras
amostras e recorrencia de fotografia, diario, doces, telefone, bagagem, telas,
portao e chuva visual. `Funcionam`, `ancora`, `confirma` e `anuncia` sao funcoes
analiticas.

**Correcao:** em `instrumented_review_notes.md:124-135`, deixar recorrencia e
matiz sob observado; mover funcao de prop, separacao espacial e efeito cromatico
para `inferencia/prototipo`. Nao atribuir pais, religiao ou cultura a paletas.

### P1.3 — mapa sonoro e medicao precisam de proveniencia mais estrita

O relatorio EBU preservado sustenta -9,2 LUFS integrado, LRA 10,8 LU e true peak
+1,4 dBFS. O pack trata corretamente o true peak como alerta da copia derivada,
nao diagnostico audivel nem target de entrega.

Entretanto, nao ha arquivo de saida de `silencedetect` no pack ou no manifesto.
Os timecodes podem estar corretos, mas nao sao auditaveis por outro revisor a
partir dos artefatos listados.

**Correcao:** preservar comando, versao, threshold, duracao minima e saida bruta
do `silencedetect`, ou rebaixar os timecodes a `medicao declarada nas notas`.
Gate 6 continua parcial; waveform nao identifica voz, musica, ambiente ou efeito.

### P1.4 — longa duracao e mudanca de estado ainda sao prototipos

`instrumented_review_notes.md:157-158` chama de observavel uma estrutura de oito
mudancas de estado. Os eventos e sua ordem aparecem nas folhas/legenda, mas
`estado`, irreversibilidade, removibilidade e tempo merecido sao analise. O relato
de corte de quase cinco para tres minutos prova negociacao editorial, nao que
3:32 seja otimo.

**Correcao:** mover as oito mudancas para inferencia de estrutura e manter
`LONG_FORM_EARNS_TIME_BY_IRREVERSIBLE_STATE_CHANGE` como prototipo ate playback,
EDL manual e teste real de remocao ou comparacao de versoes.

### P1.5 — creditos sao uteis, mas insuficientes para atribuir decisoes

Cliente, agencia, produtora e direcao convergem entre fontes. Sukesh Kumar Nayak
e ligado a escrita; Tassaduq Hussain e `Prashant` vem de portifolio participante,
com nome do colorista incompleto. O DP de Lahore permanece sem nome/escopo.

Faltam, entre outros, montagem, musica, som, producao de arte, casting, VFX,
equipe de camera, pesquisa cultural, consultoria historica e cadeia criativa
completa. A propria technical pass reconhece a parcialidade.

**Correcao:** manter `CREDITOS_PARCIAIS_VERIFICADOS`; nenhuma escolha de lente,
luz, cor, montagem, som, casting ou representacao pode ser atribuida a uma pessoa
apenas pelo cargo publicado.

### P1.6 — UI, dados reais e clearance nao foram auditados

As folhas exibem resultados, mapas, nomes de comercio, contato, companhia/voo e
interfaces de 2013. O corpus nao registra se cada resultado era ao vivo ou
composto, nem clearance, consentimento do comercio, autorizacao de marcas
terceiras ou acuracia dos dados.

**Correcao:** nao reutilizar telefones, enderecos, resultados, mapas ou dados
identificaveis como template; em nova producao, usar dados licenciados/ficticios,
revisao legal e produto atual. A tela do filme nao e documentacao atual do
Google Search nem orientacao migratoria.

### P1.7 — audiencia, viralidade, premio e versoes estao corretamente limitados

Nao foi encontrado vazamento bloqueante aqui. O pack distingue target declarado
de recepcao, premio de consenso e views de impacto social. Tambem distingue os
quatro filmes posteriores de cutdowns comprovados e nao finge ter comparado o
primeiro corte.

**Manter:** numeros promocionais sem dataset/metodo nao podem sustentar eficacia,
universalidade, reconciliacao politica, ausencia de dano ou causalidade desta
obra.

## Triangulacao das fontes

| Fonte | Uso seguro | Nao autoriza |
|---|---|---|
| upload oficial Google India | identidade, pagina, duracao de plataforma, faixas | autoria tecnica, traducao validada, causalidade de produto |
| Economic Times 2013 | brief, campanha, declaracoes atribuidas | integracao percebida como fluida, impacto India-Paquistao |
| retrospectiva ETBrandEquity 2023 | processo lembrado, primeiro corte, placas de Lahore | memoria infalivel, consulta cultural, safety case |
| perfil Amit Sharma 2014 | metodo declarado e perguntas de producao | excesso de diaria/budget como virtude transferivel |
| shots/Sukesh Nayak | autoria ligada e filosofia declarada | viralidade como universalidade ou eficacia |
| Vimeo de portifolio | creditos parciais de craft | master, escopo exclusivo, autoria de cada decisao |
| Kyoorius | cliente, marca, agencia, target de inscricao | pesquisa de recepcao, consenso ou aprovacao cultural |
| Register | existencia e teor da alegacao sobre *Respect* | veredito de plagio ou inocencia |
| MHA India | excecao especifica declarada em fevereiro de 2013 | regra completa do itinerario ficcional ou regra atual |

## Disposicao para o Atlas

### Candidatos epistemicamente seguros, apos correcao e reauditoria

1. `PRODUCT_AS_COORDINATION_LAYER_NOT_MIRACLE` — pessoas, produto e instituicoes
   devem permanecer elos separados; nao atribuir ao produto a acao humana ou
   autorizacao institucional.
2. `HISTORICAL_TRAUMA_REQUIRES_AUTHORITY_AND_FRICTION` — promover apenas como
   regra de governanca, nao como elogio ao tratamento deste filme.
3. `ACTUAL_LOCATION_IS_NOT_CULTURAL_AUTHORITY` — imagem real comprova material de
   lugar, nao consulta, consentimento, representatividade ou autenticidade total.
4. `VIRAL_RESPONSE_IS_NOT_CONSENSUS` — views, comentarios e premio nao medem
   acordo, seguranca cultural ou impacto social.

Esses quatro candidatos ainda nao devem ser ingeridos antes da disposicao dos
P0/P1 e reauditoria de fechamento.

### Prototipos

1. `MEMORY_TO_SEARCHABLE_TOKENS` — manter abstrato e bloqueado pela anterioridade
   ate comparacao com *Respect*; nunca copiar o pacote narrativo especifico.
2. `SEARCH_UI_ONLY_WHEN_STATE_CHANGES` — a funcao e plausivel, mas mudanca causal
   e economia de montagem nao foram testadas; UI visivel nao e prova funcional.
3. `LONG_FORM_EARNS_TIME_BY_IRREVERSIBLE_STATE_CHANGE` — requer playback, EDL,
   removibilidade e comparacao de versoes.
4. Co-presenca reservada ao payoff, separacao cromatica, funcao de props, ponte
   geografica e timing do reconhecimento — todos dependem de teste/percepcao.

### Recusados

- `Search reuniu dois paises`, aprovou visto ou tornou a viagem possivel sozinho;
- UI encenada como prova de produto ao vivo, acuracia ou superioridade;
- a campanha como reconciliacao politica ou consenso India-Paquistao;
- locacao real ou historia familiar como autoridade cultural suficiente;
- o filme como modelo validado de representacao da Particao ou processo de visto;
- o pacote Particao + amigo perdido + descendente + busca + reencontro como
  estrutura livre de conflito de direitos;
- viralidade, comentario, premio ou emocao da equipe como eficacia/audiencia;
- estabilidade, movimento, ritmo, score, silencio dramatico, choro, ringtone,
  chuva audivel ou microperformance inferidos das folhas/waveform;
- credito de cargo como autoria exclusiva de uma decisao.

## Disposicao exigida

### P0

1. separar dialogo/Particao/confirmacao da coluna observacional;
2. separar UI visivel, intencao de campanha e validacao/causalidade ausente;
3. retirar `emocionada` da ficha textual e corrigir ausencias de fala para
   ausencia na legenda;
4. manter estrutura especifica bloqueada ate comparacao com *Respect*;
5. rotular representacao historica/seguranca cultural como nao validadas.

### P1

1. retirar estabilidade de camera das amostras;
2. mover funcao de cor/props/espaco para inferencia;
3. preservar ou rebaixar a evidencia de `silencedetect`;
4. manter longa duracao/mudancas irreversiveis como prototipo;
5. manter creditos parciais e ampliar cadeia antes de atribuicao;
6. adicionar gate de clearance/acuracia para UI e dados identificaveis;
7. preservar limites de audiencia, premio e versao ja corretos.

## Fechamento permitido e bloqueado

- Gate 4: **parcial, sem promocao**.
- Gate 5: **parcial, sem promocao**.
- Gate 6: **parcial, sem promocao**.
- Gate 8: **nao pode fechar** antes dos P0.1–P0.3 e P1.1–P1.4.
- Gate 9: **critica realizada, disposicao ainda aberta**.
- Atlas: **bloqueado** ate incorporacao e reauditoria.
- Estado global: **parcial e inalterado**.
- Veredito de promocao do filme: **nao promover** a
  `REVISAO_AV_INSTRUMENTADA`, `VISTO_1X` ou `ANALISE_PROFUNDA`.

O caso possui valor para ensinar causalidade distribuida, limites de autoridade
cultural e diferenca entre resposta viral e consenso. Esse valor so e seguro
quando o sistema aprende tambem o que a obra e o pack nao demonstram: produto
validado, visto aprovado por busca, consulta historica suficiente, originalidade
resolvida, desempenho ouvido ou montagem percebida em continuidade.
