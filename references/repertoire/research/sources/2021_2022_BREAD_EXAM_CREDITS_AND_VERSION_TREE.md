# Fonte atomica — arvore de versoes e conflitos de creditos de *The Bread Exam*

## Fontes cruzadas

1. Gerety Awards, ficha 2021: https://www.geretyawards.com/winners/2021/entry/69103/the-bread-exam-spinneys-supermarkets-lebanese-breast-cancer-foundation
2. The One Show, ficha 2022: https://www.oneclub.org/awards/theoneshow/-award/44803/the-bread-exam/
3. D&AD, arquivo 2022: https://www.dandad.org/work/d-ad-awards-archive/the-bread-exam
4. Portfolio de Sonia Presne: https://soniapresne.com/projects/bread-exam/
5. Feed profissional Packshotmag/Satellite my Love, 2021-06-28: https://www.packshotmag.com/live-feeds/un-grand-prix-pour-satellite-my-love-et-mccann/
6. YouTube McCann Paris, 2021-01-15: https://www.youtube.com/watch?v=QyMKMzbOpiw
7. YouTube McCann Worldgroup, 2021-05-07: https://www.youtube.com/watch?v=Oc1a-Srld7E
8. YouTube McCann Paris, 2021-06-29: https://www.youtube.com/watch?v=D3q5nUbWQRQ

## Autoridade e vies

- Gerety, One Show e D&AD sao arquivos profissionais de premio: fortes para o que a inscricao creditou, mas nao independentes da submissao da campanha.
- O portfolio de Sonia Presne e fonte participante e pode misturar autoria de filme, fotografia e extensoes impressas.
- O feed Packshotmag foi publicado por Satellite my Love e confirma parceria/premiacao, nao uma ficha tecnica integral.
- Os endpoints dos tres uploads McCann sao primarios para identidade, data, duracao e estado desses nos; nao provam que sejam cortes de campanha exibidos ao publico.

## Arvore de versoes observada em metadata

| No | Publicador | Data endpoint | Duracao endpoint | Estado em 2026-08-11 | Classe |
|---|---|---:|---:|---|---|
| `0CfhuJJg4rA` | AUBMC | 2020-10-06 | 103 s | publico | no institucional AUBMC mais antigo localizado e revisado; master/titularidade/equivalencia nao provados |
| `QyMKMzbOpiw` | McCann Paris | 2021-01-15 | 115 s | publico | case study curto |
| `Oc1a-Srld7E` | McCann Worldgroup | 2021-05-07 | 135 s | unlisted | case film |
| `D3q5nUbWQRQ` | McCann Paris | 2021-06-29 | 135 s | publico | case film posterior/sibling do no anterior |

- A Gerety lista arquivos de `2m14s` e `1m43s`; isto reforca a existencia de pelo menos uma peca e um case film, mas nao resolve qual e master nem substitui hashing entre siblings.
- O Vimeo `568419946` embutido no feed da Satellite my Love nao foi adquirido: o endpoint exigiu autenticacao e sua equivalencia com um dos casos de 135 s permanece `UNRESOLVED`.

## Creditos convergentes

| Funcao | Credito convergente / fonte |
|---|---|
| Agencia | McCann Paris; tambem aparecem McCann Health London, FP7 McCann Dubai e McCann Worldgroup Germany nas extensoes globais — Gerety/One Show/D&AD |
| Cliente/parceiros | Lebanese Breast Cancer Foundation, Spinneys/Spinneys Flour, AUB Medical Center; Slow Food Beirut tambem aparece no One Show |
| Producao | Satellite my Love, Octopus, Craft Germany — One Show; Gerety identifica Satellite my Love e Octopus |
| Direcao de arte | Sonia Presne, Flora Sagnes e Sakeena Amjad no One Show; Gerety lista Presne e Sagnes |
| Direcao criativa | Cedric Astrella, Sebastien Boutebel, Guy Lewis, Mateo Fernandez e Guy Swimer em combinacoes diferentes por nivel/fonte |
| Fotografia | Malek Hosni — One Show |
| Som | Olivier Vehert (sound engineer), Claire Paillot e Isabelle Crechet (sound producers) — One Show |
| Musica | Le Trio Joubran / Randana Label — Gerety |

## Conflito de autoria audiovisual — nao resolver por maioria

- Gerety credita **Danielle Rizkallah** como `Film Director`.
- One Show credita **Danielle Rizhalla** como `Director` e **Malek Hosni** como `Director of Photography`. A grafia `Rizhalla` parece inconsistente, mas nao deve ser corrigida silenciosamente.
- O portfolio de Sonia Presne credita **Malek Hosni** como `Director and Photographer`.
- A entrevista da Spinneys chama Danielle Rizkallah de `Campaign Director`, categoria que pode ou nao corresponder a direcao do filme.
- Disposicao: `AUTHORSHIP_ROLE_SPLIT_UNRESOLVED`. Hipoteses plausiveis incluem creditos diferentes entre filme, foto/print e extensoes, ou erro de portfolio/award. Nenhuma e promovida a fato sem call sheet, ficha da produtora ou confirmacao direta.

## Alegacoes atomicas

| ID | Tipo | Alegacao | Pode sustentar | Nao pode sustentar |
|---|---|---|---|---|
| BREAD-CRED-01 | FONTE_PROFISSIONAL | Gerety registra release 2020-10-06, 1m44 e dois arquivos (1m43 e 2m14). | separacao entre peca e case film segundo a fonte | master, titularidade ou equivalencia de frames sem hashes |
| BREAD-CRED-02 | FONTE_PROFISSIONAL | One Show separa Danielle como diretora e Malek como DP. | papel inscrito naquela ficha | autoria final incontroversa |
| BREAD-CRED-03 | FONTE_PARTICIPANTE | Presne chama Malek de diretor e fotografo. | existencia do conflito documental | co-direcao ou substituicao de Danielle |
| BREAD-CRED-04 | METADATA_PRIMARIA | Tres case studies McCann medem 115, 135 e 135 s. | arvore de nos | conteudo ou identidade quadro a quadro |
| BREAD-CRED-05 | FONTE_PARTICIPANTE | Satellite my Love reportou 11 Lions e um Grand Prix em 2021. | recepcao reportada | qualidade, eficacia ou independencia dos resultados |

## Registro atomico

```yaml
id: SRC-BREAD-CREDITS-VERSIONS-2021-2022
obra: The Bread Exam
nos: [AUBMC_103s, McCannParis_115s, McCannWorldgroup_135s, McCannParis_135s]
conflito_autoria: AUTHORSHIP_ROLE_SPLIT_UNRESOLVED
fontes: [Gerety, One_Show, DandAD, Sonia_Presne, Packshotmag, YouTube_McCann]
forca_evidencia: B_para_creditos_A_para_metadata_de_cada_no
```
