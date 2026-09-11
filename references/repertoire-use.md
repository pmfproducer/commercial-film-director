# Repertório que participa da criação

## Função

A pessoa chega com uma ideia. A direção desenvolve o filme com especialistas que
usam conhecimento da profissão e referências estudadas para propor e discutir
soluções. História, performance, fotografia, arte, montagem e som devem mudar o
filme de maneira concreta. Boards, referências de quadro, previs e testes tornam
as decisões visuais inspecionáveis nas etapas já previstas.

O repertório é textual e portátil. A instalação não exige vídeos, áudios ou
contact sheets. O arquivo original pode ser consultado para um novo estudo
audiovisual quando isso resolver uma pergunta real.

Não condicionar o trabalho a rever todo o acervo. Complete lacunas por estudo
dirigido: entrevistas, making-ofs, tratamentos e fontes da especialidade podem
explicar escolhas; examinar cenas específicas esclarece movimento, ritmo e som.
Preserve a distinção entre declaração de processo, observação e interpretação.
Guarde a síntese textual e a referência; downloads de mídia não são requisito
para a memória operacional. Uma nova fonte pode informar a proposta sem promover
o estado de visionamento da obra inteira.

## Acervo recuperado

`repertoire/manifest.json` registra cópias, fontes, hashes e correções de caminho.
O snapshot inclui 107 registros de precedentes, 19 contratos de especialidades,
mapa de 17 áreas curriculares, fichas de filmes, fontes e perfis profissionais.
Não confundir essas contagens com experiência validada.

O estado recuperado registra 24 leituras técnicas instrumentadas parciais, zero
visionamentos integrais e zero análises profundas. O mapa curricular traz
competências e fontes; carga horária não foi extraída nesse mapa. Os contratos permanecem
provisórios. Consultar textos não altera esses rótulos.

## Uso na sala de direção

Formule o problema expressivo em linguagem concreta: acompanhar a causa de uma
transformação, por exemplo, ou construir uma revelação por montagem. O roteiro e
as restrições do filme delimitam essa questão.

`assign-task` prepara automaticamente um arquivo de repertório para cada área e
o inclui no brief e nas entradas verificadas da rodada. O especialista deve:

1. Ler seu contrato e as seções curriculares pertinentes.
2. Examinar candidatos criativos e contracasos separadamente. A ordem de busca
   sugere leitura; não decide a direção.
3. Abrir as fichas que sustentam a proposta, distinguindo observação parcial,
   declaração de um profissional, inferência e hipótese nova.
4. Explicar o mecanismo transferido, a adaptação ao filme, uma alternativa e a
   escolha que depende de outra área. Rejeitar referências que não sirvam ao brief.
5. Na revisão cruzada, responder à proposta da outra área e registrar o que
   mudou. O diretor integra decisões que sustentem a mesma intenção.

Uma leitura parcial pode sugerir uma hipótese criativa a testar no novo filme.
Isso não autoriza alegar efeito medido no público, visionamento integral ou
identificação de equipamento sem fonte. Cautelas documentais não substituem a
proposta de cenas, ações, imagem, montagem e som.

## Consulta direta pela direção

```bash
python3 scripts/prepare_repertoire.py --role DIRECTOR --query "problema criativo do filme" --output /pasta/do/projeto/references/direction-repertoire.json
```

Também aceita DP, EDITOR, PRODUCTION_DESIGNER, SOUND_DESIGNER e os demais papéis
da sala. `--check` verifica os arquivos do snapshot e caminhos de evidência.
`scripts/search_precedents.py` preserva o mecanismo anterior de busca do Atlas.

O retorno separa referências para criação, restrições/contracasos e pistas de
leitura em filmes e profissionais. Uma lacuna de busca não impede inventar:
impede apresentar a invenção como conhecimento comprovado da referência.

## Memória de decisão no projeto

Preserve nos pareceres e no registro da direção o que altera o filme:
referência consultada → mecanismo → proposta → discussão → decisão → teste ou
condição de revisão. Essa memória pertence ao projeto e não promove
automaticamente uma hipótese para o acervo compartilhado.

## Exemplo de aplicação

`../examples/REMENDA.md` e `../examples/REMENDA_ROUGHBOARD.html` mostram o
encadeamento de uma ideia, propostas, conflito e revisão visual. São um caso
demonstrativo; não replicar sua gag, paleta, duração ou gramática como padrão
para outros filmes.

## Limite da recuperação

A recuperação restabelece acesso e participação do estudo nos briefs. Ela não
conclui o visionamento pendente, não substitui formação humana e não comprova
que qualquer filme resultante será bom. Essa qualidade deve ser examinada no
roteiro, na encenação, nos materiais visuais e na montagem produzida.
