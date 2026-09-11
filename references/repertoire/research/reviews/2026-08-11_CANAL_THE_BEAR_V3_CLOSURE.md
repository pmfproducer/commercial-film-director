# Canal+ — *The Bear*: fechamento V3

## Veredito

**Estado:** `V3_CLOSURE_COMPLETE_GATE_8_CLOSED_GATE_9_COMPLETE_THREE_CANDIDATES_AUTHORIZED_FOR_ATLAS_CONSIDERATION_NOT_AUTOMATIC_INGESTION`.

A V3 verificou somente os residuos documentais da V2. Nao houve novo playback,
audicao, aquisicao, EDL ou elevacao perceptiva.

As tres correcoes finais foram incorporadas:

1. a fonte BETC antiga agora registra Bonkers/Vimeo como no nominal de 78 s e
   nao conserva sibling/registro de 75 s;
2. pass e pack agora possuem matrizes explicitas de acessibilidade, mantendo
   cada item nao testado como gap;
3. o candidato 6 foi renomeado no pack para
   `DIGITAL_REPLACEMENT_DOES_NOT_CLOSE_PERFORMER_CREDIT_CONSENT_COMPENSATION_USAGE_AND_AUTHORSHIP_LEDGER`.

**Gate 8:** `CLOSED_DOCUMENTALLY_FOR_THIS_PASS`.

**Gate 9:** `COMPLETE_FOR_THIS_PACK`.

Isso nao transforma a obra em `VISTO_1X`, `REVISAO_AV_INSTRUMENTADA` ou
`ANALISE_PROFUNDA` e nao fecha versionamento global, movimento, fala ou som.

## 1. Lineage Bonkers

`research/sources/2011_BETC_YOUTUBE_CANAL_THE_BEAR_MEDIA.md` agora e coerente
com a nova fonte Bonkers:

- BETC: plataforma 78 s; container 78,437007 s; copia hasheada;
- shots: no profissional `01:18`, nao adquirido/comparado;
- Bonkers/Vimeo `48446219`: oEmbed 78 s, nao adquirido/comparado;
- campo isolado `75`: nao usado como duracao;
- One Show `Under :90`: categoria, nao duracao.

Nao restaram ocorrencias focais de sibling 75 s, comparacao 75/78 ou registro
Bonkers 75. Convergencia nominal em 78 s nao prova equivalencia material.

**Resultado:** residuo P0 `CLOSED`; Gate 1 permanece `PARTIAL_NOT_CLOSED`.

## 2. Matriz de acessibilidade

Pass e pack agora registram, sem alegar conformidade:

| Campo | Estado preservado |
|---|---|
| idioma/traducao | frances/ingles candidatos, sem validacao humana |
| captions/SDH | texto queimado parcial; stream sem flag; nao equivale a captions completas |
| audio description | stream sem flag; campanha inteira nao auditada; AD nao adquirida |
| legibilidade | contraste, tamanho, safe area, mobile e tempo nao testados |
| photosensitivity | fogo/explosao/movimento aparentes; frequencia/risco nao medidos |
| profanity/classificacao | frase somente no ASR; mercado/horario/alternativa abertos |
| reveal multimodal | compreensao sem som, com captions e com AD nao testada |

As matrizes distinguem ausencia de evidencia nesta copia de falha historica da
campanha. Nao elevam fala, som, acessibilidade global ou estado perceptivo.

**Resultado:** residuo P1 `CLOSED_DOCUMENTALLY`.

## 3. Candidato 6

O pack substituiu o identificador juridicamente amplo
`PERFORMANCE_REFERENCE_RIGHTS_SURVIVE_DIGITAL_REPLACEMENT` por:

`DIGITAL_REPLACEMENT_DOES_NOT_CLOSE_PERFORMER_CREDIT_CONSENT_COMPENSATION_USAGE_AND_AUTHORSHIP_LEDGER`.

A nova formulacao descreve um ledger de governanca ainda aberto, sem prometer
direito juridico universal. Jurisdicao e contrato continuam obrigatorios para
qualquer afirmacao legal especifica.

**Resultado:** residuo P1 `CLOSED`.

## 4. Checagem de regressao

Nao reapareceram nos arquivos focais:

- sibling Bonkers 75 s;
- `montagem rapida` ou detector que `subconta cortes`;
- ausencia de marca/interface antes da endline;
- grito/profanity classificados como observacao visual;
- UI ficticia generalizada para todas as telas;
- material animal presumido no reference suit;
- sistema formal de mocap certificado.

Continuam corretamente presentes:

- `EDIT_PATTERN_UNKNOWN`;
- interface/wordmark Canal+ diegetico antes da endline;
- papeis lancados como observado e voz/profanity como ASR/inferencia;
- UI ficticia limitada ao escopo fxguide;
- material do suit e formal mocap nao validados;
- product proof, safety, animal, rights, recepcao e causalidade como gaps.

## 5. Gates apos V3

| Gate | Estado final desta passagem |
|---:|---|
| 1 — versao/duracao/hash | `PARTIAL_NOT_CLOSED` |
| 2 — densos | `COMPLETE` |
| 3 — candidatos | `COMPLETE_AS_INSPECTION_NOT_EDL` |
| 4 — movimento/transicoes | `PARTIAL` |
| 5 — fala | `PARTIAL` |
| 6 — som | `PARTIAL` |
| 7 — EDL/impossibilidade | `CLOSED_BY_DECLARED_IMPOSSIBILITY` |
| 8 — observado/declarado/inferido | `CLOSED_DOCUMENTALLY_FOR_THIS_PASS` |
| 9 — critica/disposicao | `COMPLETE_FOR_THIS_PACK` |
| 10 — limites | `COMPLETE_AS_LIMIT_STATEMENT` |

Estado global mantido: `LEITURA_TECNICA_INSTRUMENTADA_PARCIAL` e
`REVIEW_PACK_BUILT_NOT_WATCHED`.

## 6. Disposicao Atlas final

Somente os candidatos 6, 8 e 9 ficam autorizados **para consideracao** no
Atlas. Isso nao e ingestao automatica nem aprovacao sem contracaso.

| # | Candidato | Decisao V3 | Condicoes antes/depois da ingestao |
|---:|---|---|---|
| 6 | `DIGITAL_REPLACEMENT_DOES_NOT_CLOSE_PERFORMER_CREDIT_CONSENT_COMPENSATION_USAGE_AND_AUTHORSHIP_LEDGER` | `AUTHORIZED_FOR_ATLAS_CONSIDERATION` | provenance fxguide/Autodesk; qualificar performer nao identificado; jurisdicao/contrato; contracaso; nao chamar formal mocap |
| 8 | `META_PRODUCTION_NEEDS_DEPARTMENT_ACCURACY` | `AUTHORIZED_FOR_ATLAS_CONSIDERATION` | review pelos departamentos mostrados; provenance; screen/prop/rights ledger; safety; dignidade; contracaso |
| 9 | `ANIMAL_TROPHY_METAPHOR_REQUIRES_REPRESENTATION_REVIEW` | `AUTHORIZED_FOR_ATLAS_CONSIDERATION` | review por especie/mercado; welfare vivo separado; material do suit nao presumido; CG nao usado como aval etico; contracaso |

Permanecem fora de consideracao para card nesta passagem:

- 1, 3, 5 e 7: `REFORMULATE_AS_PROTOTYPE`;
- 2 e 4: `HOLD`.

Antes de inserir 6/8/9, o owner ainda deve aplicar schema Atlas, citar fontes
atomicas, explicitar limites, anexar contracaso e rodar validacao/regressao do
retrieval. A V3 nao autoriza promover os prototypes ou holds por proximidade
semantica.

## Conclusao

Gate 8 fecha no nivel documental desta passagem e Gate 9 permanece completo.
The Bear continua sendo uma leitura tecnica instrumentada parcial, nao uma obra
assistida/ouvida integralmente. Apenas 6, 8 e 9 podem seguir para consideracao
controlada no Atlas; nenhum outro candidato e liberado e nenhum gate
1/4/5/6/global foi elevado.
