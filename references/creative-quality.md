# Qualidade criativa e testes

## Ordem do julgamento

### 1. Estratégia dramatizada

- A tensão é humana e específica?
- A marca possui papel legítimo?
- A promessa vira comportamento, ação, som ou transformação?
- O filme persuade sem depender de uma explicação posterior?

### 2. Ideia

- Existe um mecanismo, não apenas tema/estética?
- A ideia é apropriável por esta marca?
- A imagem/gesto central é memorável?
- A rota recomendada é realmente mais forte que as alternativas?

### 3. Direção

- POV e arco são claros?
- Performance e blocking expressam subtexto?
- O mundo parece escolhido e habitado?
- Câmera, luz, arte, montagem e som obedecem à mesma tese?
- Há escolhas arbitrárias justificadas apenas por “cinemático”?

### 4. Planos e tempo

- Cada plano muda informação, emoção, ação, composição ou ritmo?
- Movimento e corte têm motivo?
- O plano começa e termina em estados úteis?
- B-roll possui função?
- O produto aparece no tempo e na relação corretos?
- Todo verbo editorial (“corta para”, “volta”, “revela”) corresponde a um `SHOT-ID`,
  cobertura existente ou transição explicitamente prevista?

Quando o mecanismo depende de comédia, surpresa ou constrangimento, verifique a
cadeia `setup → percepção → escalada → payoff`. A escalada pode ser mínima — um
segundo olhar, uma pausa, uma repetição — mas precisa aumentar ou reorganizar a
pressão antes da resolução. Não use close de reação apenas para ensinar o público a rir.

### 5. AI-native

- Sem IA, a forma essencial deixa de existir?
- A impossibilidade serve à promessa?
- Existe invariante claro durante a transformação?
- O resultado evita morph aleatório, flutuação e mundo genérico?
- O pipeline preserva performance e brand truth?

### 6. Execução

- Assets resolvem os substantivos e estados críticos?
- Cada referência tem uma responsabilidade?
- Modo/modelo oferece os controles necessários?
- Prompt descreve ação/tempo e não tenta inventar direção?
- Continuidade de entrada/saída fecha?
- Texto/logo/produto/rosto possuem validação e pós?

## Reprovação automática de plano gerado

- identidade muda sem intenção;
- produto, label ou geometria deforma;
- anatomia/mãos quebram a ação;
- prop troca de lado ou estado;
- eyeline/direção de tela quebra sem propósito;
- câmera executa trajetória diferente da decidida;
- morph involuntário;
- luz/clima muda sem causa;
- física chama mais atenção que a ideia;
- áudio contradiz ação/performance;
- frame é bonito, mas não cumpre função dramática.

## Diagnóstico causal

```text
SINTOMA: câmera errada
POSSÍVEIS CAUSAS: prompt, modo, ref, blocking, função do plano ou tese

SINTOMA: personagem inconsistente
POSSÍVEIS CAUSAS: master fraco, refs conflitando, muitos atributos numa prancha,
modelo/modo inadequado ou estados mal versionados

SINTOMA: filme genérico
POSSÍVEIS CAUSAS: tensão abstrata, ideia sem mecanismo, referências tratadas como look,
decisões por adjetivo ou AI-native cosmético

SINTOMA: montagem sem energia
POSSÍVEIS CAUSAS: beats não mudam, planos sem entry/exit, ação com duração errada,
som sem estrutura ou cobertura sem função
```

Corrija a causa mais a montante.

## Benchmark de três briefings

A skill candidata deve funcionar em pelo menos três problemas contrastantes:

1. drama humano contido em que verdade de performance importa mais que espetáculo;
2. filme de produto AI-native em que material, escala ou física impossível prova o benefício;
3. comédia publicitária curta em que casting, blocking, timing, corte e som carregam a ideia.

Para cada teste, exija:

- três rotas de mecanismos diferentes;
- recomendação justificada;
- roteiro/beat sheet;
- tese do diretor;
- pelo menos um plano decisivo completamente resolvido;
- arquitetura de som;
- asset/prompt route proporcional ao risco;
- crítica adversarial;
- revisão da causa mais fraca.

## Red flags da própria skill

Reprovar a skill se ela:

- começa pelo formulário;
- exibe organograma/agentes;
- entrega apenas tratamento verbal;
- usa lente/movimento como decoração;
- escreve prompts antes de cena/assets;
- cria todos os documentos sem necessidade;
- chama qualquer fantasia de AI-native;
- ignora performance, sound design ou montagem;
- transforma risco/governança no assunto principal;
- recomenda ferramenta atual sem verificar documentação.

## Critério de instalação

Só substituir a skill instalada quando:

- estrutura e frontmatter validarem;
- referências apontadas existirem;
- os três benchmarks não acionarem os red flags;
- pelo menos uma revisão cruzada atacar decisões frágeis;
- a versão antiga estiver preservada em backup recuperável.
