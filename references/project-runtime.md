# Runtime do projeto de filme

## Princípio

Conhecimento cinematográfico orienta decisões; este runtime controla a execução.
No modo projeto, nenhum turno começa escolhendo livremente "o que parece útil". O
agente localiza o estado do filme, lê as decisões já travadas e executa a próxima
fase permitida.

O arquivo `00_PROJECT_STATE.json` é a fonte de verdade operacional. Os documentos
Markdown são a fonte de verdade criativa e técnica. Se conversa e arquivos
divergirem, registrar a mudança nos arquivos antes de continuar.

`00_SALA_DE_DIRECAO.md` é o histórico legível das rodadas. Pareceres vivem em
`departments/`; briefs, hashes e revisões vivem em `collaboration/`. Leia
`multiagent-director-room.md` antes de abrir a primeira rodada.

## Modos

### `PROJECT` — padrão

Usar quando houver briefing, ideia, campanha, filme, roteiro, tratamento,
decupagem, storyboard, assets, prompts de planos, montagem ou produção. Criar ou
retomar um pacote de projeto. Entregar arquivos preenchidos, não apenas uma
resposta no chat.

### `ONE_OFF`

Usar somente quando o usuário pedir explicitamente algo avulso: uma opinião, uma
análise de referência, uma crítica isolada, um prompt único ou uma explicação sem
vínculo com um filme em andamento. Não criar pacote por iniciativa própria.

Se o pedido puder pertencer a um filme e o usuário não disser que é avulso, usar
`PROJECT`.

## Boot obrigatório de cada sessão

1. Procurar `00_PROJECT_STATE.json` no diretório atual e até três níveis abaixo.
2. Se houver um único projeto compatível, executar `status`, ler o estado, o
   `00_DIRECTION_LOCK.md` e os documentos da fase atual e anterior.
3. Se houver mais de um, selecionar pelo nome citado ou pelo arquivo/material
   anexado. Perguntar apenas se a escolha alterar materialmente o trabalho.
4. Se não houver projeto e o pedido for `PROJECT`, inicializar o pacote antes de
   desenvolver a solução.
5. Nunca reiniciar briefing, conceito ou linguagem já travados sem registrar uma
   revisão.

## Fases e dependências

| Ordem | Fase | Documentos obrigatórios | Pode iniciar quando |
|---|---|---|---|
| 01 | `BRIEF_STRATEGY` | `01_BRIEF_ESTRATEGICO.md` | projeto inicializado |
| 02 | `CREATIVE_DIRECTION` | `02_ROTAS_E_DIRECAO.md`, atualização de `00_DIRECTION_LOCK.md` | fase 01 completa |
| 03 | `SCRIPT` | `03_ROTEIRO_LITERARIO.md`, depois `03_ROTEIRO_AV.md` | fase 02 completa e uma direção registrada |
| 04 | `DIRECTOR_TREATMENT` | `04_TRATAMENTO_DIRECAO.md`, `04_MAPA_CENA_PERFORMANCE.md` | fase 03 completa |
| 05 | `VISUAL_SOUND_SYSTEM` | `05_DIRECAO_FOTOGRAFIA.md`, `05_DIRECAO_ARTE.md`, `05_ARQUITETURA_MONTAGEM_SOM.md`, `05_BIBLIA_VISUAL_SONORA.md` | fase 04 completa |
| 06 | `DECOUPAGE` | `06_ROTEIRO_TECNICO.md`, depois `06_SHOT_LIST.md` | fase 05 completa |
| 07 | `ASSETS_CONTINUITY` | `07_ASSET_BIBLE.md`, `07_ASSET_MANIFEST.json` | fase 06 completa |
| 08 | `STORYBOARD_PREVIS` | `08_STORYBOARD_PREVIS.md` | fase 07 completa |
| 09 | `AI_EXECUTION_PLAN` | `09_PLANO_PRODUCAO_HIBRIDA.md`, `09_PLANO_GERACAO_IA.md` | fase 08 completa |
| 10 | `SHOT_PACKETS` | `10_SHOT_PACKETS_PROMPTS.md` | fase 09 completa e modelos/modos confirmados ou marcados como hipótese |
| 11 | `POST_DELIVERY` | `11_MONTAGEM_SOM_POS.md` | fase 10 completa |
| 12 | `QA_VERSIONS` | `12_QA_MASTER_VERSOES.md` | fase 11 completa |

Uma solicitação de "pacote completo" autoriza percorrer as fases em sequência,
criando todos os documentos em estado `TRABALHO`. Não autoriza gastar créditos,
publicar, contratar, licenciar ou marcar aprovação humana.

## Estados de fase

- `PENDING`: ainda não iniciada.
- `IN_PROGRESS`: documentos criados e sendo preenchidos.
- `COMPLETE_DRAFT`: conteúdo utilizável e criticado; pode alimentar a próxima
  fase sob premissas registradas.
- `APPROVED`: aprovação humana explícita registrada.
- `REVISE`: mudança anterior invalidou esta fase; revisar antes de avançar.

O comando `complete` recusa arquivos com marcadores `<<PREENCHER>>`. Não declarar
uma fase concluída se o validador falhar.

Também recusa a fase sem uma rodada `ACCEPTED_BY_DIRECTOR`, sem entregas de todos
os papéis obrigatórios, com parecer alterado após revisão ou quando o diretor usa
o mesmo `actor_id` de um especialista. Aceite do diretor é gate interno; não abre
gate humano nem marca `APPROVED`.

## Ciclos de colaboração

```bash
python3 scripts/project_runtime.py open-cycle --project-dir ... --phase ... \
  --question "problema que o diretor precisa resolver" \
  --must-preserve "trava e decisões a montante"

python3 scripts/project_runtime.py assign-task --project-dir ... \
  --cycle CYCLE-... --role DP --actor-type TEMP_SUBAGENT --actor-id ... \
  --problem "..." --may-propose "..." --prohibited-changes "..." \
  --deliverable "departments/.../parecer.md" --acceptance-test "..."

python3 scripts/project_runtime.py submit-task --project-dir ... \
  --task TASK-001 --file departments/.../parecer.md --dissent-or-risk "..." \
  --runtime-path /caminho/pinado/project_runtime.py \
  --runtime-version VERSAO_DO_BRIEF \
  --runtime-sha256 HASH_DO_BRIEF

python3 scripts/project_runtime.py director-review --project-dir ... \
  --cycle CYCLE-... --actor-id ROOT_DIRECTOR --verdict ACCEPT \
  --reason "..." --integration-target "documentos canônicos"
```

Vereditos: `ACCEPT`, `REVISE`, `MORE_RESEARCH`,
`CROSS_DEPARTMENT_REVIEW` e `REJECT`. Toda devolução gera nova rodada ligada à
anterior; o histórico não é apagado.

`REVISE` e `REJECT` podem encerrar a rodada assim que ao menos um parecer
submetido demonstra o problema; não é necessário esperar trabalho sem utilidade.
As tarefas ainda pendentes ficam `CANCELLED_BY_DIRECTOR`, e as entregas já feitas
permanecem no histórico. Comunique a devolução aos agentes que ainda trabalham
e abra uma sucessora. Uma submissão tardia não reabre a rodada encerrada.
`ACCEPT` continua exigindo todos os pareceres e papéis obrigatórios.

O caminho de `--file` pode ser absoluto ou relativo à raiz de `--project-dir`;
ele não depende da pasta atual do terminal. A entrega deve estar dentro do projeto.

Cada brief contém path, versão e SHA-256 do runtime que abriu a assignment. O
`submit-task` exige que o especialista reporte exatamente esses valores. Isso
impede que uma instalação antiga valide a candidata silenciosamente.

Ao concluir, o runtime registra SHA-256 de cada documento. `validate` compara o
arquivo atual com esse hash. Qualquer edição posterior em fase concluída invalida
o projeto até executar `revise-from` a partir da primeira fase alterada, propagar
a mudança e concluir novamente. Não “corrigir rapidinho” um artefato canônico sem
change control.

Na fase 06, `validate` também executa lint semântico mínimo: igualdade dos `PLAN
ID` entre roteiro técnico e shot list, duração por plano, soma contra duração
alvo, handles quantificados e unicidade de `CAM-MOV ID`. Movimento realmente
contínuo em mais de um plano exige `SHARED_CONTINUOUS` explícito.
A coluna `Duração física` do técnico representa o trecho útil na montagem,
igual a `Duração útil` na shot list; handles ficam separados. Por exemplo,
5 s úteis com 2 s antes e 2 s depois exigem tomada mínima de 9 s, mas entram
como 5 s na soma da duração do filme.

## Contrato de aplicação dos departamentos

Conhecimento consultado não conta como trabalho executado. Cada departamento deve
deixar no documento da fase a cadeia `recebe → decide → aplica → registra → entrega
→ testa`. Toda decisão técnica inclui sua função no filme, mecanismo, execução,
critério de aceite, contraindicação e fallback. O handoff usa IDs; palavras amplas
como “cinematográfico”, “premium”, “dinâmico” ou “luz dramática” não satisfazem o
contrato sem especificação observável.

Fotografia deve fechar o sistema do filme e o plano: posição e altura, relação
câmera-sujeito, formato/sensor ou tradução perceptiva para IA, focal/família óptica,
distância, abertura/foco, percurso do movimento, fps/shutter, desenho de luz,
exposição, materialidade e look, todos ligados à função e a um teste. Arte,
performance, montagem, som, produção, IA e finishing seguem contratos equivalentes
definidos em `references/department-application-contracts.md`.

## Trava de direção

`00_DIRECTION_LOCK.md` preserva o eixo do filme entre sessões. Após a fase 02,
deve conter:

- problema comercial e mudança desejada;
- tensão humana;
- ideia em uma frase;
- tese do diretor;
- mecanismo visual/temporal;
- papel da marca/produto;
- arco de performance;
- regras de mundo;
- regra de câmera;
- regra de luz/cor/arte;
- regra de montagem;
- regra sonora;
- uso impossível de IA e sua função;
- invariantes e proibições;
- rota recomendada e fonte da decisão.

Roteiro, fotografia, arte, planos, storyboard, assets, prompts e pós devem citar
como materializam essa trava. Uma ideia nova que a contradiga não é "melhoria
local": é mudança de direção e exige change control.

## Change control

Quando o usuário alterar uma decisão:

1. atualizar `00_DIRECTION_LOCK.md` e o estado;
2. registrar motivo e alcance em `revision_log`;
3. marcar `REVISE` todas as fases derivadas afetadas;
4. preservar `SCENE ID`, `PLAN ID`, `FRAME ID` e `ASSET ID` quando a função não
   mudou; criar novo ID quando a função mudou;
5. propagar a revisão antes de criar novos prompts ou outputs.

## IDs obrigatórios

- cenas: `SC-010`, `SC-020`;
- planos: `PL-010`, `PL-020`;
- quadros/estados: `FR-PL010-A`, `FR-PL010-B`;
- assets: `CHAR-001`, `PRP-001`, `ENV-001`, `WDR-001`, `PRD-001`, `LOOK-001`,
  `SFX-001`;
- versões de shot packet: `PL-010-v01`.

Os mesmos IDs atravessam roteiro técnico, shot list, storyboard, manifestos,
prompts, geração, montagem e QA.

## Pesquisa no runtime

Pesquisa não é uma fase autônoma. Só pesquisar para resolver uma decisão aberta
da fase atual. Registrar o resultado no documento correspondente com:

- pergunta que precisava ser resolvida;
- fonte ou referência;
- mecanismo observado;
- decisão tomada;
- o que não copiar;
- validade ou data quando a informação for volátil.

Não despejar pesquisa no entregável nem usar referências como substituto de
direção.

## Gates humanos reais

Pode avançar autonomamente em rascunhos reversíveis quando o usuário pediu o
filme completo. Parar antes de:

- gasto de créditos em volume;
- uso de imagem, voz, música, obra ou marca de terceiros sem autorização;
- claim legal, médico, financeiro ou técnico não confirmado;
- contratação, orçamento fechado, publicação ou envio ao cliente;
- marcação de qualquer fase como `APPROVED` ou `FINAL` sem aprovação explícita.

## Migração v1 → v2

Projetos legados devem usar `migrate --dry-run` e depois `migrate --apply`.
A migração cria backup do estado, preserva briefing/rota, restaura roteiro
literário e separa técnico/shot list. Não divide automaticamente arquivos antigos
nem sobrescreve conteúdo. Projetos narrativos retornam para `03_SCRIPT`.

## Regra de resposta

No modo projeto, a resposta no chat é apenas o resumo do que foi feito. O trabalho
principal precisa existir no pacote local. Sempre informar:

1. fase concluída ou em andamento;
2. arquivos criados ou atualizados;
3. decisão de direção preservada;
4. premissas abertas;
5. próxima fase ou gate real.
