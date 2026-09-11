# {{PROJECT_NAME}} — índice do projeto

- Projeto ID: `{{PROJECT_ID}}`
- Cliente/marca: {{CLIENT}}
- Criado em: {{DATE}}
- Estado canônico: `00_PROJECT_STATE.json`
- Direção vigente: `00_DIRECTION_LOCK.md`

## Regra de retomada

Antes de qualquer trabalho, executar o status do runtime e ler a trava de direção,
o documento da fase anterior e o documento da fase atual. Não escolher uma nova
direção apenas porque uma sessão nova começou.

## Cadeia de documentos

1. `01_BRIEF_ESTRATEGICO.md`
2. `02_ROTAS_E_DIRECAO.md`
3. `03_ROTEIRO_LITERARIO.md`
4. `03_ROTEIRO_AV.md`
5. `04_TRATAMENTO_DIRECAO.md` + `04_MAPA_CENA_PERFORMANCE.md`
6. `05_DIRECAO_FOTOGRAFIA.md` + `05_DIRECAO_ARTE.md` + `05_ARQUITETURA_MONTAGEM_SOM.md`
7. `05_BIBLIA_VISUAL_SONORA.md` — consolidação entre departamentos
8. `06_ROTEIRO_TECNICO.md`
9. `06_SHOT_LIST.md`
10. `07_ASSET_BIBLE.md` + `07_ASSET_MANIFEST.json`
11. `08_STORYBOARD_PREVIS.md`
12. `09_PLANO_PRODUCAO_HIBRIDA.md` + `09_PLANO_GERACAO_IA.md`
13. `10_SHOT_PACKETS_PROMPTS.md`
14. `11_MONTAGEM_SOM_POS.md`
15. `12_QA_MASTER_VERSOES.md`

As rodadas e pareceres ficam em `00_SALA_DE_DIRECAO.md`, `collaboration/` e
`departments/`. Aceite do diretor não equivale a aprovação humana.

## Pastas

- `collaboration/`: briefs, hashes, ciclos, handoffs e revisões do diretor.
- `departments/`: pareceres isolados dos especialistas; não são documentos canônicos.
- `research/`: pesquisa motivada por decisão, nunca depósito genérico.
- `references/`: referências recebidas e mapa do que extrair/não copiar.
- `assets/`: masters aprovados de personagem, produto, prop, ambiente, figurino e look.
- `storyboard/`: frames rough, execution boards, overheads e animatic.
- `generations/`: outputs identificados por `PLAN ID` e tentativa.
- `audio/`: voz, música, ambientes, foley e efeitos.
- `outputs/`: cortes, masters e versões de entrega.
