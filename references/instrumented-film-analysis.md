# Análise integral e instrumentada de filme

## Quando usar

Use apenas para responder uma pergunta curricular ou criativa concreta, por exemplo:

- como o blocking justifica o movimento?
- quando o filme corta e por quê?
- como arte, luz e grade constroem a paleta?
- como o som cria espaço ou subjetividade fora do quadro?
- como produto/marca entra na causalidade?
- que possibilidade AI-native seria impossível em produção convencional?

Não “audite os melhores filmes” em bloco. Selecione obra e categoria de craft pela pergunta.

## Fonte e escopo

- obtenha legalmente a melhor versão disponível;
- registre versão, duração, fps, aspecto, resolução, codec e áudio;
- confirme se é filme integral, cutdown, case film, reupload ou versão sem som original;
- não confunda créditos do case, da campanha e da peça;
- registre lacunas e não invente.

## Pacote mínimo

1. `ffprobe` de vídeo e áudio;
2. extração de áudio sem perda desnecessária;
3. detecção de cortes como hipótese inicial;
4. contact sheets e frames antes/depois de cortes;
5. frames amostrados em intervalos para planos longos;
6. transcrição com timestamps e identificação de idioma;
7. waveform, loudness e espectrograma quando a pergunta envolve som;
8. revisão integral sincronizada de imagem + som;
9. shot table corrigida por observação humana;
10. evidências com timecodes.

Detecção automática de corte falha em dissolves, flashes, whip pans, motion blur, strobe e transformação contínua. Corrija manualmente.

## Shot table

```text
SHOT-ID
TC IN / OUT / DURAÇÃO
BEAT E FUNÇÃO
AÇÃO / PERFORMANCE / BLOCKING
COMPOSIÇÃO / POV / GEOGRAFIA
CÂMERA / MOVIMENTO / PERSPECTIVA
LUZ / COR / ARTE / FIGURINO / PROP
ENTRADA / SAÍDA / MOTIVAÇÃO DO CORTE
DIÁLOGO / AMBIÊNCIA / SFX / MÚSICA / SILÊNCIO
PAPEL DA MARCA/PRODUTO
EVIDÊNCIA OBSERVÁVEL
INFERÊNCIA E GRAU DE CERTEZA
```

## Separar observação de inferência

- Observação: “a câmera se aproxima após o olhar mudar”.
- Inferência: “o movimento parece converter reconhecimento interno em aproximação do público”.
- Não verificado: lente exata, câmera, filtro ou intenção declarada sem fonte de produção.

Não determine focal ou equipamento exato apenas por aparência. Descreva perspectiva/comportamento e procure fonte técnica quando isso for relevante.

## Leitura de som

Mapeie:

- ponto de escuta;
- voz e respiração;
- room tone/ambiente;
- foley e efeitos sincronizados;
- som fora do quadro;
- motivos e repetições;
- entradas/saídas musicais;
- pontes sonoras;
- silêncio e dinâmica;
- relação evento sonoro → corte/movimento/transformação.

Waveform/espectrograma apoiam a escuta; não interpretam dramaturgia sozinhos.

## Extração de princípio transferível

Para cada resposta:

```text
PERGUNTA
EVIDÊNCIA COM TIMECODE
MECANISMO
EFEITO NO PÚBLICO
DEPENDÊNCIAS ENTRE ÁREAS
PRINCÍPIO TRANSFERÍVEL
CONDIÇÕES EM QUE NÃO FUNCIONARIA
EXERCÍCIO/TESTE
POSSÍVEL TRADUÇÃO PARA IA
```

O resultado desejado não é “este filme usa câmera fluida”. É algo aplicável, como: “o movimento começa depois da mudança de pensamento e termina quando a nova relação espacial se completa; sem esse beat, seria ornamentação”.

## Saída honesta

Declare:

- o que foi visto/ouvido integralmente;
- o que veio de fonte oficial/entrevista/crédito;
- o que é inferência;
- o que não foi verificado;
- qual pergunta foi respondida e qual permaneceu aberta.

