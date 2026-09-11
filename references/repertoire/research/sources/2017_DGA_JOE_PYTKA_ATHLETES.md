# Fonte atomica — Joe Pytka sobre dirigir atletas

## Identidade

- Ledger de origem: `#9`.
- URL: https://www.dga.org/craft/dgaq/issues/1704-fall-2017/pitching-balls-pitching-product
- Publicacao: DGA Quarterly, Fall 2017.
- Autora: T. L. Stanley.
- Pessoas/obras centrais: Joe Pytka, Bo Jackson, Michael Jordan, Ken Griffey Jr.; Nike e outras campanhas esportivas.
- Tipo: reportagem profissional com entrevistas diretas a quatro diretores.
- Acesso integral: 2026-08-10.
- Forca para ingestao: `A` para falas atribuidas; `B` para a moldura editorial e anedotas sem cruzamento.

## Autoridade, vies e escopo

- A DGA tem autoridade profissional e Pytka tem experiencia direta com os atletas e obras citadas.
- A reportagem confronta a experiencia de Pytka com Bryan Buckley, Brian Beletic e Max Malkin, mas nao e uma norma de seguranca nem um estudo de performance.
- O texto celebra campanhas esportivas conhecidas e pode privilegiar anedotas memoraveis. O episodio de Bo Jackson e retrospectivo e nao deve ser convertido em recomendacao de conduta.

## Declaracoes e fatos reportados

| ID | Tipo | Alegacao parafraseada | Responsavel/fonte | Pode sustentar | Nao pode sustentar |
|---|---|---|---|---|---|
| PYTKA-DGA17-01 | DECLARACAO_DIRETA | Para obter o plano desejado, Pytka pediu que Bo Jackson corresse diretamente contra a camera; o impacto derrubou o diretor e quebrou a lente. | Joe Pytka | o resultado visual desejado alterou a instrucao fisica e gerou risco/dano real | que confronto ou dano sejam aceitaveis, necessarios ou replicaveis |
| PYTKA-DGA17-02 | DECLARACAO_DIRETA | Pytka aconselha seguranca sobre o resultado desejado e ausencia de hesitacao diante do atleta. | Joe Pytka | filosofia pessoal de comunicacao/autoridade | eficacia universal, etica ou seguranca do metodo |
| PYTKA-DGA17-03 | DECLARACAO_DIRETA | Segundo Pytka, atletas nao gostam de surpresa, preferem seu elemento e temem parecer ridiculos. | Joe Pytka | preocupacoes recorrentes percebidas por ele | perfil psicologico universal de todo atleta |
| PYTKA-DGA17-04 | RELATO_EDITORIAL + DECLARACAO | Como o tempo com atletas costuma ser curto, Pytka relata mudar rapidamente quando algo nao funciona. | artigo + Joe Pytka | preparacao precisa incluir alternativas executaveis | que improviso substitua ensaio, testes ou autorizacao |
| PYTKA-DGA17-05 | DECLARACAO_DIRETA | Pytka recusou uma segunda queda de Ken Griffey Jr. depois de uma captura bem-sucedida por preocupacao com lesao. | Joe Pytka | seguranca pode encerrar cobertura mesmo sob pedido da agencia | protocolo formal de risco ou que a primeira tentativa fosse isenta de perigo |
| PYTKA-DGA17-06 | DECLARACAO_DIRETA | Um contrato de endosso impediu colocar um atleta da NBA em determinada limousine num anuncio do McDonald's. | Joe Pytka | conflitos de marca podem alterar arte, props e encenacao | termos contratuais completos ou regra aplicavel a todo atleta |

## Citacao curta

> “You’re always worried about somebody getting hurt.”

Uso: registra a prioridade declarada no caso Griffey. Ela nao apaga o risco de outros relatos da mesma fonte.

## Observacoes da leitura

- A fonte mostra tensao interna no proprio metodo relatado: Pytka celebra o impacto de Bo Jackson, mas tambem descreve recusa de repeticao por seguranca com Griffey.
- Os demais diretores acrescentam mecanismos que nao devem ser atribuidos a Pytka: blocking fisico primeiro, especialista do esporte, stunt performers, musica no set e ensaios informais.
- Tempo, seguranca, imagem publica, contratos de exclusividade e entourage aparecem como restricoes diferentes; nao devem ser fundidas numa unica explicacao de “dificuldade com celebridade”.

## Inferencias separadas

- **Inferencia candidata:** dirigir atleta exige desenhar a acao ao redor de competencia real, risco permitido, tempo disponivel e limites de patrocinio.
- **Inferencia candidata:** o plano B precisa preservar a funcao do plano sem depender de repetir uma acao perigosa.
- **Contra-alerta:** firmeza nao e permissao para intimidacao. O relato de impacto evidencia um risco, nao uma tecnica recomendada.

## Aplicabilidade operacional

- Antes do storyboard final, criar uma matriz `acao / risco / substituto / angulo seguro / limite de repeticoes / conflito de marca`.
- Definir o resultado observavel do plano em vez de depender de uma ordem vaga de performance.
- Planejar doubles, coreografia e angulos como alternativas de seguranca, com especialista e equipe de stunt quando aplicavel.

## Registro atomico

```yaml
id: SRC-PYTKA-DGA-2017-ATHLETES
pessoa: Joe Pytka
papel: diretor
obras: [Nike Bo Knows, Nike I Got It, campanhas esportivas]
etapas: [casting, ensaio, blocking, seguranca, captacao]
restricoes: [tempo_de_atleta, risco_fisico, contratos_de_marca, imagem_publica]
fato: "a DGA publica declaracoes diretas e relatos atribuidos a Pytka"
citacao_curta: "You're always worried about somebody getting hurt."
inferencia: "o plano deve ser redesenhavel sem transferir risco desnecessario ao atleta"
fonte_url: "https://www.dga.org/craft/dgaq/issues/1704-fall-2017/pitching-balls-pitching-product"
tipo_fonte: "reportagem profissional com entrevistas diretas"
forca_evidencia: A
necessita_validacao_cruzada: true
```
