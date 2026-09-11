# Sala de direção multiagente

## Princípio

Um filme não é produzido por um único cérebro preenchendo departamentos em
sequência. O diretor-orquestrador formula a pergunta, convoca especialistas,
recebe propostas independentes, promove confronto produtivo, devolve revisão e
só então integra a decisão no documento canônico.

Quando colaboração/subagentes estiver disponível, use especialistas temporários
reais. Quando não estiver, execute passes separados e registre
`ROLE_SIMULATION`; nunca apresente uma simulação como equipe real.

Nenhum especialista edita diretamente o documento canônico da raiz. Cada área
entrega um parecer versionado em `departments/<area>/`. O diretor aceita, rejeita
ou devolve. Somente material `ACCEPTED_BY_DIRECTOR` é integrado.

## Papéis canônicos

- `DIRECTOR`: unidade, conflitos, devoluções e decisão final interna.
- `RESEARCHER`: fatos, contexto, tensões, referências, riscos e lacunas.
- `CREATIVE_DIRECTOR`: mecanismos de conceito e papel causal da marca.
- `SCREENWRITER`: estrutura, cenas, ação, personagens, fala e silêncio.
- `PERFORMANCE_DIRECTOR`: casting, objetivo, ação jogável, subtexto e blocking.
- `DP`: câmera, perspectiva, óptica, movimento, luz, exposição e look.
- `PRODUCTION_DESIGNER`: espaço, cenografia, materiais, props, figurino e HMU.
- `EDITOR`: informação, duração, cobertura, corte, elipse e versões.
- `SOUND_DESIGNER`: ponto de escuta, voz, Foley, SFX, silêncio e música.
- `CONTINUITY_SUPERVISOR`: identidade, geografia, eixo e estados.
- `STORYBOARD_ARTIST`: rough boards, overhead, previs e animatic.
- `PRODUCER_AD`: produzibilidade, ordem operacional, equipe, agenda e risco.
- `VFX_AI_SUPERVISOR`: assets, VFX, rotas IA, testes e fallbacks.
- `POST_QA`: conform, cor, som, versões e controle de qualidade.
- `CRITIC`: passagem adversarial independente; não corrige o próprio parecer.

## Ciclo obrigatório

Antes da proposta, cada especialista lê o pacote de repertório que `assign-task`
anexa ao seu brief: contrato profissional, seções curriculares e referências
recuperadas para a questão. Abra as fontes relevantes e preserve seus níveis de
evidência. O diretor consulta seu próprio repertório quando formular a questão.
O uso completo está em `repertoire-use.md`.

No parecer, ligar referência → mecanismo → adaptação proposta → dependência ou
conflito com outra área. Na discussão, explicitar o que mudou e por quê. Uma
referência pouco pertinente deve ser rejeitada; uma hipótese nova pode ser
testada sem fingir que foi observada num filme anterior. O repertório alimenta
imaginação e decisão, não obriga copiar linguagem nem substitui a criação por
um relatório de cautelas.

```text
DIRECTOR abre a pergunta e declara o que deve ser preservado
→ especialistas recebem brief e hashes das entradas
→ cada especialista entrega proposta isolada
→ DIRECTOR compara função, mecanismo, execução, risco e teste
→ ACCEPT: integra e fecha a rodada
→ REVISE: devolve ao mesmo papel com motivo observável
→ MORE_RESEARCH: volta ao pesquisador antes de reescrever
→ CROSS_DEPARTMENT_REVIEW: abre conflito entre áreas afetadas
→ REJECT: descarta a proposta, preservando o histórico
```

Estados: `OPEN → DISPATCHED → SUBMITTED → DIRECTOR_REVIEW →
ACCEPTED_BY_DIRECTOR` ou `REVISION_REQUIRED`.

`ACCEPTED_BY_DIRECTOR` é decisão interna de desenvolvimento. Não equivale a
`APPROVED`, que exige manifestação humana explícita.

`REVISE` e `REJECT` podem encerrar a rodada assim que ao menos um parecer
submetido demonstra o problema; não é necessário esperar trabalho sem utilidade.
As tarefas ainda pendentes ficam `CANCELLED_BY_DIRECTOR`, e as entregas já feitas
permanecem no histórico. Comunique a devolução aos agentes que ainda trabalham
e abra uma sucessora. Uma submissão tardia não reabre a rodada encerrada.
`ACCEPT` continua exigindo todos os pareceres e papéis obrigatórios.

## Salas por etapa

### História — `STORY_LOCK`

1. O usuário conta a ideia.
2. O diretor formula o problema do filme.
3. Pesquisador e criação devolvem evidências, tensão e mecanismos.
4. Roteirista escreve o roteiro literário.
5. Crítico tenta remover clichê, locução explicativa e marca-adesivo.
6. O diretor aceita, pede nova pesquisa ou reescrita.
7. Só após `STORY_LOCK` o roteiro audiovisual é derivado.

### Encenação — `DIRECTOR_TREATMENT_LOCK`

Direção de performance transforma texto em objetivo, ação, subtexto, blocking e
geografia. O diretor testa e fecha a cena antes de pedir que a câmera a resolva.

### Imagem e tempo — `VISUAL_SYSTEM_LOCK`

DP, arte, montagem e som trabalham separadamente. Depois revisam conflitos reais:
câmera versus blocking, material versus luz, cobertura versus duração, música
versus ponto de vista. O diretor reconcilia e registra a solução comum.

### Pacote técnico — `TECHNICAL_PACK_LOCK`

Roteiro técnico nasce do filme fechado em ordem narrativa. Shot list deriva dele
em ordem operacional. Storyboard/previs testa geografia, timing e som. Nenhum dos
três pode inventar uma nova direção.

### Plano de produção — `PRODUCTION_PLAN_LOCK`

Produção, VFX/IA e continuidade validam recursos, riscos, direitos, segurança,
assets, testes baratos e fallbacks. Pós e QA encerram o ciclo sem reescrever a
ideia para esconder falha de produção.

Esse lock aceita somente o plano documental. `READY_TO_SHOOT` exige aprovação
humana, recursos, direitos, safety e testes executados; a skill nunca o infere.
Da mesma forma, `QA_DOCUMENT_LOCK` aceita o dossiê de QA, não um master. Somente
evidência de mídia permite `PASS_MASTER`.

## Brief de especialista

Cada assignment deve declarar:

- pergunta que a área resolve;
- arquivos e hashes recebidos;
- decisões que deve preservar;
- liberdade real para propor;
- mudanças proibidas;
- artefato esperado;
- teste de aceite;
- ator real: `TEMP_SUBAGENT` ou `ROLE_SIMULATION`.
- provenance pinado: path, versão e SHA-256 do runtime. O especialista reporta os
  três valores no `submit-task`; mismatch é bloqueio, não aviso.

## Revisão do diretor

O diretor não escolhe por gosto abstrato. Registra:

- proposta aceita ou devolvida;
- efeito narrativo, emocional e comercial;
- mecanismo que sustenta a decisão;
- conflito resolvido e perda aceita;
- documento canônico que será atualizado;
- condição que obriga reabrir a rodada.

## Regra de concisão

A sala registra decisões, divergências e revisões que mudam o filme. Não arquiva
conversa vazia, elogio, brainstorm descartável ou repetição de briefing.
