# Protocolo de pesquisa viva por projeto

## Função

Este protocolo transforma um briefing novo em pesquisa orientada por problema antes de roteiro, decupagem ou storyboard. Ele existe para evitar dois erros opostos:

1. responder apenas com a memória interna, mesmo quando ela não cobre o assunto;
2. procurar `assunto + commercial` e copiar a superfície do primeiro filme encontrado.

A pesquisa termina em mecanismos com evidência, limites e contrafactuais. Não termina em um moodboard de semelhanças.

## Gate zero — intake suficiente

Antes de pesquisar, registrar ou marcar como desconhecido:

- marca, oferta e papel real do produto;
- objetivo comercial e mudança desejada no público;
- público, mercado, canal, duração e versões;
- verdade disponível para demonstração;
- restrições de orçamento, prazo, locação, elenco, direitos e ferramentas;
- riscos humanos, culturais, legais, ambientais e de segurança;
- clichês/superfícies que o projeto precisa evitar;
- decisão que a pesquisa deve ajudar a tomar.

Ausência de informação não autoriza completar o brief por fantasia. A pesquisa pode começar com hipóteses rotuladas, mas roteiro e produção ficam bloqueados nas dimensões críticas.

## Passo 1 — decompor o briefing em eixos

Gerar no mínimo estes eixos:

| Eixo | Pergunta |
|---|---|
| Literal | Onde o assunto/ambiente/produto já apareceu? |
| Problema | Que tensão comercial ou humana precisa mudar? |
| Função | O que a imagem, o som ou a performance precisam provar/fazer sentir? |
| Mecanismo | Que regra narrativa poderia produzir essa mudança? |
| Departamento | Que decisão pertence a direção, DP, arte, casting, montagem, som, VFX, produção ou segurança? |
| Contrafactual | Qual versão mais simples provaria a mesma coisa? |
| Contraexemplo | Onde a mesma superfície falhou, virou clichê ou produziu dano? |
| Adjacência | Que outra categoria resolveu função semelhante sem compartilhar a superfície? |

Exemplo: `piscina` não é um conceito. Pode ser limiar, prova de precisão, risco, memória, infraestrutura, corpo real, gravidade alterada, som filtrado ou clichê de lifestyle.

## Passo 2 — consultar o Atlas

Executar:

```bash
python3 research/scripts/search_atlas.py "<brief ampliado>"
```

Quando o intake estruturado possuir assunto/categoria principal, passá-lo
separadamente:

```bash
python3 research/scripts/search_atlas.py "<problema e mecanismos>" --subject "<assunto>"
```

O header diferencia:

- `subject_concepts`, `subject_covered` e `subject_uncovered`: cobertura
  categorial, separada de cenário ou mecanismo;
- `subject_safety_flags`: riscos acionados pelo assunto mesmo quando ele não
  aparece na frase de mecanismos;
- `requested_mechanisms`, `mechanisms_covered` e `mechanisms_uncovered`:
  mecanismos especializados que exigem evidência explícita no card. Um VFX
  genericamente invisível, por exemplo, não comprova stitch de continuidade.

Interpretar o estado literalmente:

- `ATLAS_MATCH`: memória cobre mais de uma dimensão; ainda fazer atualização ao vivo e checar versão/contexto;
- `ATLAS_PARTIAL_NEEDS_LIVE_RESEARCH`: usar cards apenas para formular perguntas e adjacências;
- `RESEARCH_GAP`: não recomendar linguagem como se houvesse precedente estudado.

Cards de `failure` e `counterexample` têm o mesmo peso de decisão que casos celebrados. `do_not_copy` e `limits` acompanham qualquer referência apresentada.

## Passo 3 — descoberta em três camadas

### 3.1 Campo profissional amplo

- shots — The Work: descoberta editorial recente;
- shots Vault: pessoas, empresas e créditos quando o acesso permitir;
- Ads of the World — Film: triagem ampla por marca, país, agência e asset;
- arquivos D&AD, One Show, AICP, British Arrows, CICLOPE, Clio, Cannes/The Work e prêmios regionais.

Estado máximo nesta camada: `CANDIDATO` ou `FONTES_LOCALIZADAS`.

### 3.2 Identidade e versão

Para cada candidato prioritário, verificar:

- master/cutdown/case film e duração exata;
- data, mercado, idioma e upload;
- diretor, DP, produtora, agência, arte, casting, montagem, som, cor e VFX quando publicados;
- conflitos de crédito e de romanização;
- se o asset acessível é realmente o filme discutido.

Não analisar um case film como se fosse o master.

### 3.3 Processo e decisão

Buscar fontes na seguinte ordem:

1. entrevista/treatment/making-of de diretor ou chefe de departamento;
2. página oficial de marca, agência, produtora ou fornecedor;
3. publicação técnica/profissional do departamento;
4. comentário real de júri;
5. imprensa/recepção e crítica situada;
6. fonte de saúde, lei, segurança ou cultura quando o risco exigir.

Prêmio prova seleção pelo júri, não causalidade, eficácia ou correção ética.

## Passo 4 — matriz mínima de busca

Para cada projeto, executar famílias de consulta, adaptadas ao idioma/mercado:

1. `<assunto> commercial film`, `<assunto> branded film`, `<assunto> ad campaign`;
2. `<problema/função> advertising film`;
3. `<mecanismo> director interview commercial`;
4. `<título/diretor> treatment`, `making of`, `behind the scenes`, `case study`;
5. `<título> cinematography`, `production design`, `casting`, `editing`, `sound design`, `VFX`, `color`;
6. `<assunto> cliché advertising`, `<assunto> campaign backlash`, `<assunto> representation critique`;
7. consultas site-specific em `shots.net`, `adsoftheworld.com`, arquivos de prêmio e páginas oficiais;
8. equivalentes no idioma do mercado e nomes transliterados quando necessário.

O utilitário `research/scripts/plan_project_research.py` gera uma primeira matriz auditável; ele não executa nem substitui a pesquisa.

## Passo 5 — funil 12 → 6 → 3

Como padrão de projeto, não como meta inflacionária:

- descobrir pelo menos 12 candidatos distintos;
- verificar identidade/versão/créditos de 6;
- estudar processo e mecanismo de 3 casos contrastantes;
- incluir pelo menos 1 contraexemplo;
- incluir pelo menos 1 caso de escala/orçamento comparável;
- incluir pelo menos 1 adjacência fora da categoria literal.

Se a disponibilidade de fonte impedir o funil, registrar o déficit. Não preencher com links fracos.

## Passo 6 — ficha de referência de projeto

Cada caso selecionado precisa responder:

- qual era o problema e qual evidência o sustenta;
- qual versão foi examinada;
- o que foi observado, declarado e inferido;
- qual mecanismo organiza a obra;
- por que cada plano/beat principal existe;
- o que câmera, luz, cor, arte, performance, montagem e som fazem — sem inventar equipamento;
- onde marca/produto entram causalmente;
- restrições, custo humano e interfaces de produção;
- contrafactual mais simples;
- o que é transferível e o que não pode ser copiado;
- que mudança no brief faria a recomendação deixar de valer.

## Passo 7 — síntese antes da criação

A entrega da pesquisa não é “faça igual a X”. É:

1. território de problema;
2. três a cinco mecanismos possíveis;
3. evidência e limite de cada mecanismo;
4. alternativa simples e custo relativo;
5. riscos/contraexemplos;
6. perguntas ainda abertas;
7. recomendação provisória de direção, sujeita ao debate entre departamentos.

Só depois entram conceito, roteiro, decupagem, plano de fotografia e storyboard.

## Gate de ingestão permanente

Pesquisa de projeto não entra automaticamente no Atlas. Para virar memória permanente, o caso precisa de:

- identidade/versionamento fechados;
- observação audiovisual no estado declarado;
- ao menos uma fonte de processo qualificada;
- separação entre fato, declaração, observação e leitura;
- princípio, limite, contrafactual e `do_not_copy`;
- crítica independente proporcional ao risco.

## Registro de decisão

Toda decisão principal da futura skill deve persistir:

```yaml
decision:
  what: ""
  function: ""
  evidence: []
  simpler_alternative: ""
  tradeoff: ""
  risks: []
  owner: ""
  consulted_departments: []
  confidence: low|medium|high
  change_condition: ""
```

Assim, a referência deixa de ser decoração e passa a ser argumento auditável.
