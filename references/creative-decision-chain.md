# Cadeia de decisões criativas

## Regra central

A skill funciona como uma rede de dependências, não como departamentos isolados. A pergunta mais a montante tem precedência; a solução especializada precisa preservar sua função.

```text
problema de marca
→ mudança no público
→ tensão humana
→ proposição e prova
→ ideia/dispositivo
→ roteiro e ação
→ visão do diretor
→ cena, performance e blocking
→ mundo, arte, fotografia, som e VFX
→ storyboard, plano, montagem e acabamento
→ assets, modelo e modo de IA
→ prompt
```

## Objeto de decisão

```yaml
decision:
  upstream_intent: "qual decisão anterior exige esta escolha"
  expressive_problem: "o problema narrativo, emocional ou comercial"
  recommendation: "escolha concreta"
  mechanism: "como ela tende a causar o efeito"
  expected_audience_effect: "o que muda para o espectador"
  dependencies: ["áreas e planos afetados"]
  alternatives:
    - option: "alternativa real"
      tradeoff: "ganho e perda"
  test: "como validar antes de comprometer a produção"
  downstream_handoff: "o que os próximos elementos recebem"
  status: "open | testing | locked"
```

Não precisa exibir esse objeto em toda resposta. Use-o para impedir arbitrariedade.

## Autoridade e colaboração

- Marca/cliente decide problema, fatos, objetivos, obrigações e limites; não prescreve sozinho linguagem cinematográfica.
- Estratégia/criação formula insight, promessa, ideia e texto-base; não escolhe lente ou blocking por capricho.
- Diretor integra todos os elementos em um sistema de ponto de vista, performance, imagem, tempo e som.
- Chefes de área traduzem o problema expressivo em soluções especializadas e apresentam consequências.
- Produção expõe custo, agenda, risco e alternativas; não substitui silenciosamente a função criativa.
- Editor, sound designer, VFX e colorista são autores da realização, não serviços de limpeza tardia.

## Interfaces obrigatórias

### Estratégia → ideia

Pesquisa separa fato, observação, padrão de categoria e hipótese. O insight precisa virar mecanismo filmável. Pergunte: que comportamento contém a tensão e que ação, relação, demonstração, metáfora ou transformação prova a proposição sem explicá-la?

### Ideia → roteiro

Defina quem deseja o quê, qual força resiste, o que muda, qual papel não intercambiável a marca assume e como o tempo curto concentra a experiência. Em filme de produto, a marca tende a ser causal ou probatória; em institucional, pode ser regra, testemunha ou assinatura legítima, nunca mero logo substituível.

### Roteiro → direção

Para cada cena: mudança, POV, subtexto, ação, beat, mundo e papel do produto.

### Performance/blocking → fotografia e arte

Comece por comportamento e geografia. Desenvolva espaço, props, câmera e luz como respostas e restrições recíprocas. Um plano-conceito ou uma arquitetura específica pode exigir outro blocking, mas a alteração precisa preservar objetivo, relação, legibilidade e performance. Alterar qualquer lado obriga reavaliar os demais.

### Diretor ↔ DP

Diretor determina efeito e princípio. DP propõe posição, óptica, formato, exposição, filtro, luz e ferramenta de movimento. Escolha conjunta e testada.

### DP ↔ arte ↔ figurino ↔ HMU ↔ cor

Paleta é interação de pigmento, material, reflectância, pele, fonte, sensor, óptica e transform. Não é uma cartela separada do mundo.

### Arte ↔ VFX/IA

Decida o que é físico, gerado, estendido, substituído ou composto. O mesmo master aprovado deve viajar por concept, board, geração e pós.

### Diretor ↔ editor ↔ som

Distinguir planos essenciais, cobertura e material de transição. Som pode estruturar imagem e corte desde o roteiro.

### Direção → contrato mestre → prompt executável

O contrato mestre preserva intenção, POV, ação, performance, blocking, estados, som e continuidade. O compilador entrega ao modelo apenas os controles úteis ao modo escolhido. Prompt curto não significa direção rasa; prompt longo não compensa uma cena indecisa.

### DP ↔ VFX ↔ colorista

Look, metadata, plates, transforms, referências e integração precisam ser planejados antes da geração/captação.

## Quando subir um nível

Se um prompt não controla o plano, verifique antes:

1. O modo escolhido aceita o controle?
2. O asset está correto e tem função única?
3. O plano está tentando executar ações demais?
4. O blocking/estado inicial e final estão definidos?
5. A cena tem uma intenção clara?
6. A ideia está pedindo uma imagem que não dramatiza a proposição?

Corrija a primeira causa verdadeira. Não acrescente adjetivos ao final do prompt.
