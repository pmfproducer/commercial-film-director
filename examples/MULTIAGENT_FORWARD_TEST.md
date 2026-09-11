# Protocolo de forward-test multiagente

Use ao alterar runtime, fases, papéis, gates ou entregáveis. O teste deve ocorrer
em workspace isolado e nunca usar como resposta-alvo a solução imaginada pelo
autor da alteração.

## Cenário mínimo

1. Usuário chega somente com uma ideia incompleta.
2. Diretor abre sala e convoca pesquisador/criação/roteiro.
3. Primeira versão recebe `REVISE` ou `MORE_RESEARCH` por falha real.
4. Nova rodada responde à crítica e chega a `STORY_LOCK`.
5. DP, arte, montagem e som entregam propostas independentes.
6. Um conflito entre departamentos é identificado e resolvido pelo diretor.
7. Roteiro técnico, shot list e storyboard preservam IDs e decisões.
8. Produção/IA declara custos, riscos, testes e fallbacks sem gastar créditos.
9. Pós e QA distinguem plano de execução de master realmente produzido.
10. O validador recusa autoaprovação, parecer alterado e avanço sem rodada aceita.

## Rubrica — 100 pontos

| Dimensão | Pontos | Evidência exigida |
|---|---:|---|
| Multiagência real | 25 | actor_ids distintos, briefs, pareceres e hashes |
| Iteração e direção | 20 | devolução real, nova rodada e decisão fundamentada |
| Qualidade criativa | 15 | ideia causal, específica e com papel legítimo da marca |
| Aplicação departamental | 15 | câmera, arte, montagem e som mudam o filme e são executáveis |
| Rastreabilidade/entregáveis | 15 | literário→AV; técnico→shot list; IDs e change control íntegros |
| Honestidade produção/QA | 10 | distingue planejado, testado, produzido e aprovado |

Nota mínima para instalar: **90/100**, sem zero em nenhuma dimensão.

## Reprovações automáticas

- um único ator registrado como vários especialistas reais;
- roteiro AV criado no lugar do roteiro literário narrativo;
- especialista editando documento canônico e aprovando o próprio trabalho;
- fase seguinte aberta após parecer `REVISE` ou `MORE_RESEARCH` sem sucessora;
- roteiro técnico e shot list fundidos;
- storyboard bonito que contradiz blocking, lente, luz, duração ou som;
- QA declara master, teste ou aprovação inexistente;
- `VALID` obtido apenas pela substituição mecânica de placeholders.

