# Fonte atomica — Jeff Buchanan e o fluxo editorial de *Welcome Home*

## Identidade

- Ledger de origem: `#13`.
- URL: https://appleinsider.com/articles/18/04/23/editor-of-spike-jonzes-homepod-ad-details-production-process
- Publicacao: AppleInsider.
- Autor: Andrew O'Hara.
- Data: 2018-04-23.
- Pessoas/obra: editor Jeff Buchanan, diretor Spike Jonze, Apple HomePod *Welcome Home*.
- Origem declarada pelo artigo: entrevista de Buchanan publicada pela Frame.io e making-of anterior da Apple.
- Tipo: reportagem secundaria que resume fonte primaria externa.
- Acesso integral: 2026-08-10.
- Forca para ingestao: `B`; requer cruzamento quando a precisao de workflow for critica.

## Autoridade, vies e escopo

- Buchanan e testemunha direta do fluxo editorial, mas a pagina da AppleInsider parafraseia sua entrevista em vez de publicar a transcricao completa.
- O veiculo e especializado em Apple e usa linguagem promocional sobre o anuncio; isso aumenta o risco de enquadramento favoravel a marca.
- O artigo tem boa utilidade para cronograma e encadeamento editorial reportados, mas nao explica a filosofia de Jonze nem a cadeia completa de aprovacao.

## Declaracoes e fatos reportados

| ID | Tipo | Alegacao parafraseada | Responsavel/fonte | Pode sustentar | Nao pode sustentar |
|---|---|---|---|---|---|
| HOME-AI18-01 | RELATO_SECUNDARIO | Buchanan permaneceu no set durante quase toda a filmagem para iniciar a montagem imediatamente. | AppleInsider resumindo Frame.io/Buchanan | integracao de editorial e set no caso relatado | que Jonze sempre trabalhe assim ou que o editor decidisse cobertura |
| HOME-AI18-02 | RELATO_SECUNDARIO | A filmagem durou quatro dias, a pos duas semanas e o primeiro material entrou em montagem cerca de duas horas apos o inicio da captura. | AppleInsider resumindo Buchanan | ordem de grandeza e simultaneidade reportadas | cronograma auditado, horas de trabalho ou todas as etapas da pos |
| HOME-AI18-03 | RELATO_TECNICO_SECUNDARIO | O fluxo descrito foi ALEXA XT → DIT → assistente → Buchanan; proxies DNx36 1080p foram montados no Media Composer e depois enviados a cor/conform. | AppleInsider resumindo Buchanan | pipeline editorial especifico reportado | configuracao completa de camera, lentes, codec de aquisicao ou pipeline de VFX |
| HOME-AI18-04 | RELATO_SECUNDARIO | A maior parte das transformacoes visuais veio de cenarios praticos hidraulicos ou movidos por pessoas; o plano do espelho recebeu componente de motion capture. | AppleInsider + making-of citado | combinacao practical/digital em termos gerais | percentual quadro a quadro, ausencia de outros VFX ou autoria de cada mecanismo |
| HOME-AI18-05 | RELATO_SECUNDARIO | Buchanan buscava efeitos sonoros desde o roteiro para construir o humor do inicio chuvoso e monotono. | AppleInsider resumindo Buchanan | desenho sonoro/editorial comecou antes do corte fechado | desenho de som final completo ou autoria exclusiva do editor |

## Citacao curta

- Nao preservada: a pagina acessada apresenta esses pontos principalmente em parafrase editorial, nao como transcricao direta de Buchanan.

## Observacoes da leitura

- O titulo destaca Spike Jonze, mas a evidencia de processo vem do editor e das fontes que o artigo resume.
- “Pouco VFX” no texto se refere a carga percebida pela equipe editorial; nao significa filme sem compositing, cleanup ou acabamento digital.
- A velocidade do pipeline so e interpretavel junto da presenca do editor no set e da passagem rapida por DIT/assistencia.

## Inferencias separadas

- **Inferencia candidata:** quando cenografia, coreografia e montagem precisam ser calibradas em poucos dias, editor no set e ingestao imediata podem reduzir atraso de feedback.
- **Inferencia candidata:** construir som desde o roteiro ajuda a definir contraste emocional antes de a imagem estar fechada.
- **Limite:** a fonte nao demonstra que a montagem em duas horas causou decisoes de camera ou alteracoes do set.

## Aplicabilidade operacional

- Em filmes coreografados, prever estacao editorial no set, responsavel de ingestao e ciclos de revisao com diretor/AD.
- Incluir desenho sonoro preliminar no roteiro e no animatic, sobretudo quando o arco depende de contraste de ambiente.
- Nomear separadamente `efeito pratico capturado`, `cleanup`, `composite`, `mocap` e `acabamento`, evitando a etiqueta imprecisa “sem CGI”.

## Registro atomico

```yaml
id: SRC-HOME-APPLEINSIDER-2018-EDITORIAL
pessoa: Jeff Buchanan
papel: editor
obra: Welcome Home
marca: Apple HomePod
diretor: Spike Jonze
etapas: [captacao, dailies, montagem, som, pos_producao]
artefato: "montagem iniciada no set a partir de proxies"
fato: "AppleInsider resume entrevista da Frame.io e making-of da Apple"
citacao_curta: null
inferencia: "feedback editorial antecipado pode apoiar producoes coreografadas sob prazo curto"
fonte_url: "https://appleinsider.com/articles/18/04/23/editor-of-spike-jonzes-homepod-ad-details-production-process"
tipo_fonte: "reportagem secundaria baseada em entrevista primaria"
forca_evidencia: B
necessita_validacao_cruzada: true
```
