# Bloqueios conhecidos de maturidade

## `P1_GATE_G_FREE_TEXT_INGESTION`

- **Data:** 2026-08-11.
- **Estado:** mitigação de intake coberta por regressão; Gate G ainda aberto.
- **Severidade:** P1; impede `tested` e `production` dos 19 contratos.
- **Escopo:** intake conversacional/Markdown no forward-test PMF.

### Evidência observada

1. No briefing congelado **IA Schools**, `route_agents` em modo consultivo/treatment retornou `BLOCKING_INTAKE` e afirmou faltar `objective`, embora o texto explicitasse o problema e a mudança pretendida.
2. No briefing congelado **Banco de Leite**, o runtime afirmou faltar `audience`, `brand/offer` e `duration/channel`, embora o Markdown contivesse essas informações.

### Leitura controlada

- O resultado demonstra que a ingestão lexical atual não interpreta de forma robusta briefings naturais que seriam fornecidos à skill conversacional.
- Ele não demonstra que os contratos falharam por conteúdo de direção, fotografia ou produção; os testes foram bloqueados antes desse ponto.
- Um `project_state` estruturado pode permitir testes do fluxo interno, mas não fecha este defeito de entrada e não pode ser usado como recibo substituto do Gate G.

### Mitigação observada no estado atual

- `test_real_ia_schools_markdown_keeps_only_unresolved_audience_missing` agora confirma que o texto resolve objetivo, marca/oferta e entrega; somente audiência permanece ausente, como o próprio brief determina.
- `test_real_banco_leite_markdown_supplies_all_four_intake_dimensions` agora confirma as quatro dimensões e preserva os escalonamentos clínico e de exposição corporal.
- A suíte completa passou com essas regressões. Isso fecha a reprodução lexical original no nível de intake, mas ainda não é um forward-test integral, não compara CONTROL e SYSTEM e não emite recibo de melhoria cega.

### Condição de fechamento

- manter as regressões do parser fora desta camada de ownership;
- completar, sem editar os briefs congelados, IA Schools e Banco de Leite em `free_text_markdown`, fornecendo apenas a audiência realmente ausente de IA Schools por intake humano rastreável;
- confirmar que nenhuma informação explícita é marcada como ausente;
- preservar os outputs e hashes;
- então executar as comparações cegas e emitir os recibos PMF por contrato.

Nenhuma promoção foi realizada em resposta a estes testes.

## `P1_GATE_G_V12_STRUCTURAL_REGRESSIONS`

- **Data:** 2026-08-11.
- **Estado:** falha V12 confirmada; contratos endurecidos para nova rodada prospectiva.
- **Severidade:** P1; impede `tested` e `production` até nova evidência cega e forward-tests da versão exata.
- **Escopo:** `strategy.brand@0.3.0`, `creative.direction@0.3.0`, `production.executive@0.3.0` e `critique.independent@0.3.0`.

### Evidência observada

1. Gate G V12 terminou em `FAIL`, com `0/4 SUPERIOR` e quatro projetos `UNSAFE_OR_REGRESSIVE`.
2. Hotel, trânsito e cooktop não reconciliaram orçamento, recursos especializados, cronograma e contingência em um ledger de viabilidade auditável.
3. Doação de órgãos não apresentou três mecanismos criativos concorrentes nem perguntas decisórias explícitas, e introduziu um claim externo sem evidência auditável.
4. Os quatro candidatos chegaram ao seal sem referências criativas completas; a revisão pré-seal não bloqueou essas lacunas.

### Mitigação estrutural implementada

- `production.executive@0.3.0` exige `Feasibility Ledger` reconciliado ao teto e distingue alocação de planejamento de cotação real.
- `creative.direction@0.3.0` exige `Route Set` com pelo menos três mecanismos distintos e `Reference Cards` completos antes da convergência.
- `strategy.brand@0.3.0`, `creative.direction@0.3.0` e `critique.independent@0.3.0` exigem `Decision Questions` com decisão afetada, owner e deadline.
- Claims externos dependem de `Evidence Registry`; referências criativas dependem de provenance, mecanismo limitado, contracaso e `do_not_copy`.
- `critique.independent@0.3.0` executa cold review pré-seal nos 12 eixos e três contagens do Gate G e veta claims evitáveis, gaps ocultos, referência ausente e recurso fora de budget/timeline.

### Condição de fechamento

- ~~exercer os quatro contratos `0.3.0` em fixtures adversariais~~ — fechado em
  2026-08-15 por execução cega e pontuação independente: 24/24
  `PASS_BEHAVIORAL`, seis casos distintos por contrato;
- ~~exercer os quinze contratos `0.2.0` restantes em fixtures adversariais~~ —
  fechado em dois lotes prospectivos, executados sem contexto de pontuação e
  avaliados de forma independente: lote A 30/30 e lote B 60/60
  `PASS_BEHAVIORAL`. Com isso, os 19/19 contratos têm seis casos canônicos
  aprovados, sem alterar o `declared_status=provisional`;
- ~~executar nova comparação cega prospectiva para estratégia, direção criativa
  e produção executiva~~ — fechado pelo V27, com duas famílias causalmente
  atribuídas a cada um desses três contratos;
- demonstrar melhoria causal de `critique.independent@0.3.0`: o V27 recusou a
  atribuição porque a crítica só selou tratamentos já escritos; o ensaio causal
  V2 executou três fixtures e obteve `0/3` descritivo, mas a auditoria
  independente o invalidou por unblind antes do freeze global `9/9`; ele não
  gera recibo e não pode ser reparado sob o mesmo execution ID. O protocolo
  prospectivo V13 fechou a reauditoria como
  `PASS_READY_FOR_EXTERNAL_PROVISIONING`, mas ainda não foi provisionado nem
  executado e, portanto, não gera recibo de melhoria cega;
- ~~completar dois forward-tests PMF aprovados para os quatro contratos~~ —
  fechado: Banco de Leite + Estação Literária cobrem `critique.independent`, e
  Estação Literária + Festival Família, Música e Morango cobrem estratégia,
  direção criativa e produção executiva;
- emitir apenas os recibos restantes vinculados por hash à versão contratual
  exata;
- manter todos os contratos em `provisional` enquanto esses recibos não existirem.

O hardening já possui evidência adversarial completa para 19/19 contratos, mas
as comparações cegas, os forward-tests restantes e a causalidade da crítica
ainda bloqueiam maturidade `tested`; a evidência pós-V27
fica no ledger separado `contract-maturity-post-v27.json` para não reescrever o
checkpoint V13 ancorado. Nenhuma promoção foi realizada.

## `P1_REMAINING_V02_BLIND_AND_FORWARD_EVIDENCE`

- **Data:** 2026-08-15.
- **Estado:** protocolo cego V5 aprovado para provisionamento externo; nenhuma
  execução real.
- **Severidade:** P1; mantém quinze contratos em `provisional`.
- **Escopo:** contratos `0.2.0` fora do núcleo
  `strategy.brand`, `creative.direction`, `production.executive` e
  `critique.independent`.

### Evidência fechada

- 19/19 contratos possuem seis fixtures adversariais aprovadas;
- 19/19 possuem Gate F documental aprovado;
- o programa V5 cobre quinze contratos em duas famílias cada, com 30 trials,
  60 braços e 90 avaliações;
- o golden sintético V5 validou 2.151 artefatos e 740 receipts temporários;
- a auditoria independente V5 concluiu
  `PASS_READY_FOR_EXTERNAL_PROVISIONING`, sem P0/P1.
- o pacote administrativo conjunto foi congelado em
  `research/projects/contract-maturity/external-provisioning/`, com manifesto
  SHA-256
  `a20c651d6720dab46df99a54cdf5a8cc3d5a749d09e7cdb92f10aea448d8160d`;
- o pacote prende por hash os designs e pareceres V5/V13, publica runbook e
  decisões humanas, bloqueia chaves privadas e autorização de execução e passou
  14/14 testes próprios;
- a análise de providers confirmou rotas WORM + Ed25519 em AWS e GCP, mas
  nenhum produto isolado entrega o schema completo; o V5 ainda exige decidir
  entre um gateway único auditado e uma nova versão que separe model provider de
  receipt provider;
- a integração preservou V5 42/42, V13 57/57 e maturidade 20/20. O V5 foi
  reexecutado em dependências temporárias congeladas porque o Python padrão
  falhou corretamente sem `jsonschema` e `rfc8785`.

### Evidência ainda ausente

- owners, principals, chaves, custódia, WORM e trust anchors externos reais;
- candidatos CONTROL/SYSTEM reais e congelados;
- 90 avaliações cegas reais, unblind autorizado e atribuição por contrato;
- dois forward-tests PMF por família exigida para cada contrato;
- receipts de `blind_improvement`, `pmf_forward_test` e Gate H no ledger vivo.

### Próximo gate operacional

- preencher uma declaração externa real conforme
  `schemas/PROVISIONING_DECLARATION.schema.json`;
- nomear pelo menos nove principals V5, cinco owners humanos V13 e dezoito
  participants V13;
- aprovar custos, retenção, custódia e canal out-of-band;
- escolher provider compatível e provisionar dois backends V13 sem colocar
  segredo, chave privada ou trust root dentro do repositório;
- obter nova auditoria operacional antes de qualquer freeze ou execução.

O PASS de preflight prova apenas que o protocolo pode ser provisionado. Ele não
é resultado experimental, não altera `declared_status` e não autoriza instalação
da skill.
