# Levi's — *Drugstore Male / Female*: reauditoria V2 de fechamento

## Estado e limite

**Estado:** `V2_REAUDIT_COMPLETE_GATE_8_CLOSED_DOCUMENTALLY_GATE_9_COMPLETE_GATES_1_4_5_6_PARTIAL`.

Esta reauditoria verifica somente a incorporação documental das seis correções
exigidas pela crítica independente anterior. Foram relidos a ficha técnica, as
notas instrumentadas Male/Female, as notas de aquisição, a revisão textual do
ASR Male, o novo manifest Boy e as fontes atômicas diretamente afetadas. O
arquivo Boy apontado pelo manifest foi conferido por metadata, tamanho e
SHA-256.

Não houve reprodução contínua, visionamento, audição humana, comparação
perceptiva entre Boy e Male, EDL manual nem inspeção audiovisual do item HAT de
60 s. O fechamento abaixo não promove o estado perceptivo da família.

## Reauditoria das seis correções

| # | Correção exigida | Evidência V2 | Juízo |
|---:|---|---|---|
| 1 | Reconciliar aquisição, manifest, hash e duração do Partizan Boy; atualizar a fonte | `drugstore_boy/lineage_manifest.json` registra asset Wiredrive `3354696`, caminho local, 17.656.458 bytes, 91,680 s e SHA-256 completo `7dd269c7680560a369925e34f083c4e692e4bc1bf6d8d9508a593abdc82633c7`. Conferência independente do arquivo local retornou exatamente o mesmo tamanho, hash e duração, além de H.264 640×480/25 fps e AAC 48 kHz/2 canais. A fonte Partizan agora declara mídia adquirida para lineage, fornece os mesmos dados e nega pack, playback, escuta e equivalência. Ficha e acquisition notes repetem o estado limitado. | `PASS` |
| 2 | Usar a nomenclatura exata de câmera por fonte | Ficha e notas Male dizem British Arrows `Lighting camera` e HAT `Cameraman`. Não resta `Director of Photography/Lighting Camera` nem “fotografia/lighting camera” nos documentos reauditados. As fontes atômicas preservam os mesmos campos e recusam ampliá-los para autoria integral. | `PASS` |
| 3 | Manter aberto o conflito 1993 / 1994–1995 / 1995 | Ficha e notas Male/Female qualificam `1995` como ano de arquivo/prêmio, registram 1993 na retrospectiva e 1994–1995 no HAT e deixam o lançamento original em conflito. As fontes conservam a proveniência de cada data. | `PASS` |
| 4 | Incluir safeguarding infantil na governança sexual-health | Ficha e ambos os packs registram figuras de aparência infantil sem inferir idade e exigem safeguarding, autorização de responsável, assentimento e welfare; Male acrescenta briefing específico sobre prop/subtexto e privacy. O candidato 6 reformulado inclui explicitamente `ADULT_STATUS_MINOR_SAFEGUARDING`. | `PASS` |
| 5 | Isolar o overrun do ASR Male do objeto audiovisual | Notas Male e `transcript_reviewed.md` registram `[BLANK_AUDIO]` de 90,000 a 98,460 s, além dos 90,517333 s do arquivo, como `overrun/padding` do ASR, não conteúdo, silêncio certificado ou extensão temporal do filme. | `PASS` |
| 6 | Isolar o HAT 60 s `Colour` da aparência dos derivados D&AD | Ficha e acquisition notes tratam o HAT 60 s `Colour` como classificação exclusiva daquele registro, separada da aparência monocromática/de baixa saturação dos derivados D&AD e sem convertê-la em equivalência, erro ou prova de grade. | `PASS` |

**Resultado:** `6/6 CORRECTIONS INCORPORATED`.

## Testes de regressão

| Área | Resultado da busca adversarial |
|---|---|
| Identidade e lineage | Male, Female, Boy e HAT 60 s continuam nós separados. A aquisição Boy não é convertida em identidade com Male, master canônico, integridade de corte ou análise do conteúdo. |
| Câmera, movimento e POV | A ficha não infere câmera, lente, rig, movimento contínuo, direção de olhar ou POV subjetivo contínuo. As notas mantêm a hipótese de restrição de informação dependente de playback/EDL e audiência. |
| Produto e claims | Watch pocket permanece possível dispositivo de plot, não efeito de memória demonstrado. `1873`, `The Original Jean`, originalidade, adequação do bolso, superioridade e venda continuam sem validação. |
| Segurança, álcool e targeting | O material não introduz álcool nem targeting como fato. Sexualidade, idade, consentimento, dignidade, privacy, veículo, ferrovia e locações permanecem gates humanos/documentais; ausência de documentos não é convertida em acusação sobre a produção histórica. |
| Autenticidade e representação | Títulos de fonte não viram identidade inferida. A variante Female não é tratada como simples troca de rótulo nem como prova automática de empoderamento, equivalência ou recepção. |
| Som | ASR, silêncio medido, EBU e crédito musical permanecem evidências distintas; nenhum deles vira escuta, cue sheet, conteúdo ou função narrativa. |
| Cor | `Colour` do HAT não contamina a descrição qualificada dos derivados D&AD, e a aparência destes não invalida o campo arquivístico HAT. |

Não foi encontrada regressão que reabra uma das seis correções. O caminho Boy
fica em `/tmp`, portanto sua preservação durável continua sendo uma questão de
custódia técnica; no snapshot reauditado, porém, o objeto existe e confere com o
manifest. Isso não altera o juízo de lineage nem impede o fechamento documental
específico do Gate 8.

## Gate 8

**Decisão:** `CLOSED_DOCUMENTALLY_FOR_THIS_PACK`.

As afirmações corrigidas agora distinguem de modo consistente:

- o que foi medido no objeto local;
- o que as fontes publicam com sua nomenclatura e data próprias;
- o que as folhas amostradas permitem observar;
- o que continua hipótese dependente de playback, EDL, escuta, comparação ou
  pesquisa de audiência.

Este fechamento é documental e limitado ao corpus atual. Não declara master
canônico, equivalência Boy/Male/HAT, linguagem audiovisual Boy, cor do master,
movimento, POV percebido, desenho sonoro, direitos, safety histórico, recepção
ou causalidade comercial.

## Gate 9 e disposição individual

Gate 9 permanece `COMPLETE_FOR_THIS_PACK`, sem mudança de disposição:

| # | Disposição V2 | Limite preservado |
|---:|---|---|
| 1 | `HOLD` | POV/informação exige playback, EDL, mapa de informação e teste de audiência. |
| 2 | `REFORMULATED_AND_APPROVED` | Plot device exige plant/recall/payoff observáveis e claim review separado. |
| 3 | `REFORMULATED_AND_APPROVED` | Variante de papel/persona exige lineage, execução e revisão de representação próprias. |
| 4 | `PROMOTABLE` | Superfície de época não prova história ou pesquisa. |
| 5 | `PROMOTABLE` | Título/página de prêmio não prova equivalência de versão. |
| 6 | `REFORMULATED_AND_APPROVED` | Prop de saúde sexual exige status adulto, safeguarding de menor, consentimento, precisão, contexto, dignidade, privacy e não coerção. |
| 7 | `REFORMULATED_AND_APPROVED` | História/originalidade no endline exige substanciação claim a claim e fronteira da copy figurativa. |
| 8 | `PROMOTABLE` | ASR `MUSIC` não é sound map. |

Placar preservado: **4/5/8 promovíveis; 2/3/6/7 reformulados e aprovados; 1
hold; nenhum rejeitado**. “Promovível” qualifica a formulação do princípio; não
prova execução perceptiva nem autoriza mutação automática do Atlas.

## Gates que não sobem

| Gate | Estado após V2 | Motivo |
|---|---|---|
| Gate 1 — lineage | `PARTIAL_NOT_CLOSED` | O nó Boy agora tem objeto e manifest verificáveis, mas não existe master canônico nem comparação frame/audio que resolva Male/Boy/HAT; a data original também segue em conflito. |
| Gate 4 — movimento, montagem e POV | `PARTIAL` | Amostragem não mede movimento contínuo, eyeline, duração exata de planos, montagem, withholding ou efeito do reveal. |
| Gate 5 — fala/texto auditivo | `PARTIAL` | ASR não foi confirmado por audição humana; `[BLANK_AUDIO]` foi corretamente rebaixado a overrun do sistema. |
| Gate 6 — som por beats | `PARTIAL` | Não há escuta crítica, cue sheet nem mapa sonoro por beat; EBU, waveform, silêncio e créditos não substituem essas evidências. |

O estado global permanece `LEITURA_TECNICA_INSTRUMENTADA_PARCIAL`. Fechar Gate
8 não fecha Gate 1 e não promove Gates 4/5/6.

## Veredito estrito

**Gate 8:** `CLOSED_DOCUMENTALLY_FOR_THIS_PACK — SIX_OF_SIX_CORRECTIONS_VERIFIED`.

**Gate 9:** `COMPLETE — 4/5/8 PROMOTABLE; 2/3/6/7 REFORMULATED_AND_APPROVED; 1 HOLD`.

**Gates 1/4/5/6:** `REMAIN_PARTIAL`.

**Estado final:** `V2_DOCUMENTARY_CLOSURE_ONLY_NO_PLAYBACK_NO_LISTENING_NO_PERCEPTUAL_PROMOTION_NO_ATLAS_MUTATION`.
