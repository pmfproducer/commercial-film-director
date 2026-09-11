# Roteamento de modelos e modos

Snapshot verificado em 2026-08-28. Capacidades mudam: antes de comprometer produção, conferir documentação oficial e disponibilidade na conta/região.

Nunca trate o nome de uma família como prova de que um controle existe. Registre separadamente:

```text
MODEL = família e versão
SURFACE = app, API ou integração que será usada
MODE = T2V, start-frame I2V, reference-to-video, first/last, V2V, edit etc.
INPUTS = tipos, quantidades e duração realmente aceitos nesse modo
OUTPUT = duração, proporção, resolução, áudio e formato realmente expostos
```

Uma capacidade anunciada na página do modelo pode não estar disponível na API,
região, conta ou integração escolhida. Não compile sintaxe, aliases ou limites de
uma superfície para outra.

## Escolha por controle necessário

Não escolha “o melhor modelo”. Liste os controles do plano e procure o sistema que os aceita:

```text
duração
quantidade/tipo de referências
identidade/personagem/produto
first/last frame
motion/camera reference
V2V/edit/extension
multi-shot/storyboard
performance/lip-sync
áudio nativo
resolução/alpha/ProRes/EXR
consistência e custo de iteração
```

## Seedance 2.5

Use quando uma sequência precisa coordenar muitos assets multimodais, extensão,
referência criativa, câmera/movimento, edição e áudio. A documentação oficial
anuncia até 30 s, até 30 imagens, 10 vídeos e 10 áudios, além de white/clay model,
green-screen/reference editing e controles temporais. Esses números são limites
máximos anunciados, não recomendação para preencher todos os slots nem garantia de
que todos os controles sobreviverão juntos. Teste o beat de maior risco e reduza
referências/instruções quando identidade, contato, física ou causalidade competirem.

Fonte: [ByteDance Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5).

## Kling 3.0 / Omni

Use para multishot curto, cenas com personagens/objetos recorrentes, diálogo e
áudio associados, start/end frame e element binding. A família 3.0 anuncia até
15 s, áudio nativo, múltiplos planos, element reference e diálogo multilíngue; a
documentação do produto mostra que disponibilidade e combinações mudam entre
Video 3.0, 3.0 Omni e a superfície. Não presuma que start frame, end frame,
element binding, edição e áudio podem ser combinados no mesmo job sem conferir a
interface.

Fontes: [Kuaishou Kling 3.0](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be), [guia oficial Kling Video 3.0](https://app.klingai.com/cn/quickstart/klingai-video-3-model-user-guide), [Kling no Firefly](https://www.adobe.com/products/firefly/partner-models/kling-ai.html).

## Veo 3.1

Use para planos curtos de alta fidelidade com áudio nativo, reference images,
first/last frame e extensão quando o modo escolhido expuser esses controles. A
API atual descreve clipes de 8 s em 720p/1080p/4K, até três reference images e
extensão de vídeos Veo elegíveis. A página de produto demonstra também camera
controls, outpainting e object insertion, mas não presuma que demonstrações da
superfície Flow/DeepMind sejam parâmetros disponíveis na API ou em outra
integração.

Fontes: [Google AI Veo](https://ai.google.dev/gemini-api/docs/veo), [DeepMind Veo](https://deepmind.google/models/veo/).

## Runway

Trate como ecossistema modular:

- Gen-4.5: T2V e start-frame I2V de 2–10 s; no I2V, o texto deve
  principalmente dirigir movimento;
- Gen-4 Image References: até três imagens ativas para guiar personagem,
  ambiente, produto e composição; é controle de referência, não garantia de
  identidade ou geometria;
- Act-Two: driving performance + um character input por geração. Com character
  image pode transferir gesto/corpo; com character video, o vídeo conserva seu
  movimento corporal/câmera e o Act-Two dirige principalmente face/expressão.
  Diálogo com vários personagens exige passes e composição, salvo mudança
  oficialmente documentada;
- Aleph 2.0/Edit Studio: edição contextual dirigida de vídeo, com um alvo claro
  por iteração; `preserve everything else` é intenção a validar, não isolamento
  pixel-perfect;
- ProRes/PNG sequence dependem de plano, ferramenta e modo.

Use quando for melhor separar imagem, performance, movimento, edição e acabamento em passos controláveis.

Fontes: [Gen-4.5](https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5), [Image References](https://help.runwayml.com/hc/en-us/articles/40042718905875-Creating-with-Gen-4-Image-References), [Act-Two](https://help.runwayml.com/hc/en-us/articles/42311337895827-Performance-Capture-with-Act-Two), [Aleph](https://help.runwayml.com/hc/en-us/articles/52150503729171-Aleph-2-0-Prompting-Guide).

## Luma Ray V2V

Use motion-first: capture performance, câmera e blocking; transforme
mundo/look/material usando a estrutura temporal como base. Não confunda versões:
Ray 3.2 Modify é V2V, mantém a duração do source (até 20 s) e oferece até 64
keyframes, motion/structure e controles de personagem; Ray 3.14 possui outro
conjunto de modos e limites. No Ray 3.2, o prompt descreve o estado visual alvo,
não reescreve a coreografia que já está no source. Todos os elementos preservados
precisam ser verificados no resultado.

Fonte: [Luma Ray 3.2](https://lumalabs.ai/learning-center/articles/ray-3-2-introduction-and-core-concepts).

## Adobe Firefly/Premiere

Use para motion reference, composition reference, camera presets, first/last
frame, elementos para composição/alpha quando suportado, SFX dirigidos e
integração editorial/Generative Extend. Motion reference e composition reference
são controles distintos: um guia trajetória/caráter de câmera; o outro guia
estrutura, profundidade e layout. No Firefly Video atual, a referência de câmera
usa os primeiros 5 s do vídeo enviado; duração, FPS, combinação com style/frame e
demais controles precisam ser confirmados na tela. Generative Extend resolve
handles curtos de vídeo/ambiente; não deve ser tratado como extensão narrativa
universal nem como preservação de diálogo.

Fontes: [Motion Reference](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/match-camera-motion-to-reference-video.html), [Composition Reference](https://helpx.adobe.com/firefly/web/work-with-audio-and-video/work-with-video/use-video-as-composition-reference.html), [Generative Media no Premiere](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generative-media-tool-overview.html).

## Imagem e assets

### GPT Image

Use para geração/edição de imagem e high-fidelity inputs quando disponível. Validar texto, produto e identidade no resultado.

Fonte: [OpenAI image models](https://developers.openai.com/api/docs/models/gpt-image-2).

### Gemini image generation

Use para composição multi-reference, edição conversacional, character/product iterations e vistas consistentes; limites de referências dependem do modelo atual.

Fonte: [Google image generation](https://ai.google.dev/gemini-api/docs/image-generation).

### Seedream

Use quando controles de sketch, seleção espacial, materiais, multi-image fusion e separação de camadas forem relevantes.

Fonte: [Seedream 5.0 Pro](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro).

## OpenAI Sora

Não recomendar como rota nova neste snapshot. A OpenAI informa que o produto
Sora deixou de estar disponível em 2026-04-26 e que a API Sora 2 está deprecated,
com desligamento anunciado para 2026-09-24. Material antigo sobre Storyboard,
Remix, Re-cut ou Characters serve como referência histórica, não como capacidade
de produção atual.

Fonte: [OpenAI Videos API](https://developers.openai.com/api/reference/typescript/resources/videos/methods/create).

## Política de roteamento

1. Descreva a tarefa e controles necessários.
2. Separe plano em estágios se nenhum motor oferece todos os controles.
3. Escolha a modalidade com menor ambiguidade, não a interface mais famosa.
4. Use refs principalmente para substantivos, aparência e relações. Motion,
   performance, white/clay model ou vídeo também podem controlar movimento e
   timing. Use o prompt para atribuir papéis, ordenar a ação e declarar a mudança;
   referência não garante separação perfeita de atributos.
5. Preserve plano de montagem, comp, branding, texto, VFX, som e cor.
6. Teste o plano mais arriscado antes de gerar o volume.
7. Registre versão do modelo, modo, inputs e resultado aprovado.

## Exemplos de roteamento

- atuação humana complexa em criatura: performance capture → Act-Two/V2V → comp/som;
- produto exato em transformação: product masters + first/last + plano de pós para label;
- câmera coreografada impossível: previs/white model ou reference video → motor multimodal/V2V;
- mundo variável com personagem estável: identity refs separadas + ambiente/look por versão;
- filme de vários planos com diálogo: storyboard/multimodal depois de teste do
  speaker mapping; senão pacotes por plano, passes de performance e edição externa.
