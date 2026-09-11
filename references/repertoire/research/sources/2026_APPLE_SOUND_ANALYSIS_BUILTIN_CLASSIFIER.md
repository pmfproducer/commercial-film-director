# Apple Sound Analysis — classificador embutido para arquivos

## Identidade

- `source_id`: `SRC-2026-APPLE-SOUND-ANALYSIS-BUILTIN`
- Organização: Apple Developer Documentation.
- Tipo: documentação técnica primária de framework.
- Recursos:
  - https://developer.apple.com/documentation/soundanalysis
  - https://developer.apple.com/documentation/soundanalysis/snaudiofileanalyzer
  - https://developer.apple.com/documentation/soundanalysis/snclassifysoundrequest
  - https://developer.apple.com/documentation/soundanalysis/classifying-sounds-in-an-audio-file
- Acesso/verificação: 2026-08-11.

## Autoridade, viés e limite

- Autoridade alta para API, modelo embutido e comportamento declarado do framework Apple.
- Viés de plataforma: a documentação não é benchmark independente de acurácia e não cobre portabilidade fora de macOS/iOS.
- O modelo embutido é probabilístico. Um label/confidence não equivale a escuta humana, source separation, cue sheet, sync confirmado ou intenção de sound design.
- A lista de classes e a implementação podem depender da versão do sistema operacional; preservar identificador, contagem de labels e output bruto por execução.

## Alegações atômicas declaradas pela fonte

1. `SNAudioFileAnalyzer` executa requests de análise sobre arquivo de áudio e produz resultados temporais.
2. `SNClassifySoundRequest` pode usar o classificador embutido identificado por `SNClassifierIdentifier.version1` ou um modelo Core ML customizado.
3. O request expõe `knownClassifications`, `overlapFactor` e a duração de janela suportada.
4. `SNClassificationResult` retorna classificações ranqueadas para um intervalo de tempo.
5. A documentação descreve o classificador embutido como capaz de identificar mais de 300 sons; no ambiente auditado, `knownClassifications.count` retornou 303.

## Inferência operacional do projeto

O framework pode reduzir a lacuna do Gate 6 ao gerar candidatos temporais para fala, música, ambiente, efeito e silêncio-classifier. Ele não fecha sozinho o gate: o mapa precisa cruzar transcript, `silencedetect`, créditos/fontes e escuta humana documentada para claims perceptivos.

## Aplicação

- Script bruto: `research/scripts/sound_event_map.swift`.
- Compositor auditável: `research/scripts/build_sound_evidence.py`.
- Estado obrigatório do output: `MACHINE_SOUND_EVIDENCE_NOT_HUMAN_LISTENING`.
- Guardar output bruto, parâmetros, hash do áudio, versão do classificador e limitações junto ao mapa resumido.

## Não autoriza

- dizer que o filme foi ouvido ou assistido;
- nomear instrumentos/ambientes/efeitos como fato apenas pelo ML;
- declarar silêncio percebido a partir de limiar digital;
- inferir função emocional, espacialidade, timbre, perspectiva ou mix;
- promover `REVISAO_AV_INSTRUMENTADA` sem cumprir os demais gates e o contraditório.
