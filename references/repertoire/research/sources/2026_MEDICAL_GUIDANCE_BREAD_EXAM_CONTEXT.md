# Fonte atomica — contexto medico atual para reuso de *The Bread Exam*

## Objetivo

Registrar a divergencia entre a orientacao territorial da LBCF/Libano e guidelines internacionais consultados em 2026-08-11. Este arquivo nao presta aconselhamento individual nem decide qual protocolo deve vigorar em uma nova campanha.

## Fontes primarias e institucionais

1. Lebanese Breast Cancer Foundation, `Detection & Diagnosis / Testing`: https://lbcfoundation.org/Testing.aspx
2. Ministerio da Saude Publica do Libano, campanha nacional 2023: https://www.moph.gov.lb/en/Pages/0/71170/national-breast-cancer-awareness-campaign-2023
3. Ministerio da Saude Publica do Libano, algoritmos clinicos 2023: https://moph.gov.lb/userfiles/files/HealthCareSystem/PHC/Algorithms_230809_final-eng.pdf
4. World Health Organization, fact sheet `Breast cancer`, atualizada 2026-07-03: https://www.who.int/news-room/fact-sheets/detail/breast-cancer
5. American College of Obstetricians and Gynecologists, `Should I still be doing monthly self-exams of my breasts?`, revisado 2025-12: https://www.acog.org/womens-health/experts-and-stories/ask-acog/monthly-self-exams-of-breasts
6. ACOG, Practice Bulletin `Breast Cancer Risk Assessment and Screening in Average-Risk Women`: https://www.acog.org/clinical/clinical-guidance/practice-bulletin/articles/2017/07/breast-cancer-risk-assessment-and-screening-in-average-risk-women
7. American Cancer Society, FAQ das diretrizes de rastreamento: https://www.cancer.org/cancer/types/breast-cancer/frequently-asked-questions-about-the-american-cancer-society-new-breast-cancer-screening-guideline.html

## O que cada jurisdicao declara

| ID | Fonte | Declaracao relevante | Limite |
|---|---|---|---|
| BREAD-MED-01 | LBCF | Recomenda BSE mensal para mulheres acima de 20 anos, por volta do setimo dia apos inicio do ciclo, com metodos circular/checkers e avaliacao de mamilo. | pagina nao exibe data de revisao nem gradacao de evidencia; terminologia binaria |
| BREAD-MED-02 | MOPH Libano 2023 | A campanha nacional inclui material de autoexame e recomendacoes de rastreamento. | a pagina indice nao permite inferir que o filme de 2020 seja a tecnica oficial vigente |
| BREAD-MED-03 | MOPH algoritmos 2023 | Para risco medio, apresenta mamografia anual a partir dos 40 enquanto a mulher estiver em boa saude. | algoritmo nao valida cada gesto do filme |
| BREAD-MED-04 | WHO 2026 | Separa early diagnosis (reconhecer sinais, procurar avaliacao e ter referral) de screening; lista mudancas/lump/thickening, pele, mamilo e secrecao e orienta procurar cuidado. | nao oferece aval ao autoexame mensal sistematico mostrado |
| BREAD-MED-05 | ACOG 2025 | Para risco medio, nao recomenda autoexames mensais sistematicos; privilegia breast self-awareness e comunicacao de mudancas. | guidance dos EUA, nao automaticamente lei clinica do Libano |
| BREAD-MED-06 | ACOG bulletin | Diferencia autoexame repetitivo de self-awareness e cita falta de beneficio e risco de falsos positivos para risco medio. | nao cobre todas as pessoas de alto risco ou contextos de baixa infraestrutura |
| BREAD-MED-07 | ACS | Diz que evidencia nao mostra reducao de mortes por autoexame regular e que ele nao substitui mamografia; incentiva perceber/reportar mudancas. | guideline dos EUA |

## Disposicao

`JURISDICTIONAL_GUIDANCE_CONFLICT — HUMAN_MEDICAL_REVIEW_REQUIRED`

- O filme observado ensina rotina mensal sistematica e menciona forma, cor, tamanho, areas endurecidas, movimento circular/linear e secrecao. Isso se alinha a pagina atual da LBCF, mas diverge do enquadramento ACOG/ACS para pessoas de risco medio.
- Nao se deve concluir que a campanha era “medicamente errada” em 2020 nem que permanece apropriada para qualquer territorio em 2026. A decisao depende de autoridade clinica local, populacao, risco, acesso a mamografia, infraestrutura de referral e evidencia atual.
- O mecanismo nunca deve ser apresentado como diagnostico, prevencao ou substituto de consulta/rastreamento. Um achado requer avaliacao clinica; ausencia de achado palpavel nao exclui cancer.
- A promessa implicita “save a life” e alegacoes de eficacia precisam ser redigidas com cuidado e sustentadas separadamente.

## Requisitos para qualquer adaptacao

1. medical owner nomeado, credencial verificada e aprovacao datada;
2. territorio e guideline declarados, com data de expiracao/revisao;
3. separacao entre awareness, early diagnosis e screening;
4. linguagem de escalada para sinais/mudancas e acesso a servico local;
5. texto explicito de que a atividade nao substitui mamografia, avaliacao ou plano individual;
6. inclusao de pessoas sem menstruacao, pos-menopausa, gestantes/lactantes, homens, pessoas trans e nao binarias quando pertinente ao territorio;
7. teste de compreensao para verificar se a metafora ensina o limite, nao apenas o gesto;
8. revisao de ansiedade, falso positivo, falsa tranquilizacao e barreiras de acesso.

## Registro atomico

```yaml
id: SRC-BREAD-MEDICAL-GUIDANCE-2026
obra: The Bread Exam
estado: JURISDICTIONAL_GUIDANCE_CONFLICT
fontes_territoriais: [LBCF, Lebanon_MOPH]
fontes_internacionais: [WHO, ACOG, ACS]
uso_permitido: contexto_de_risco_e_governanca
uso_proibido: recomendacao_clinica_automatica
medical_human_gate: required
```
