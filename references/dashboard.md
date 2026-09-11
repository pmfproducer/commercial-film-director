# Dashboard local da produtora

O dashboard acompanha projetos reais do runtime. Roda em 127.0.0.1 e usa Python 3.10+
sem dependências externas. Fechar o processo encerra o painel; os arquivos permanecem.

## Abrir

A partir da pasta da skill:

```bash
python3 scripts/dashboard.py
python3 scripts/dashboard.py --project-dir "/caminho/FILME_PROJETO"
```

Para um assistente abrir no navegador integrado, use `--no-browser --port 0`, mantenha
o processo ativo e abra o campo `url` retornado. Reutilize essa URL na mesma sessão.
`--projects-dir` define onde novos projetos são criados; o padrão é
`~/Documents/Commercial Film Director/projects`. Abrir projeto aceita um caminho
local que já contém `00_PROJECT_STATE.json` compatível. Não copia nem apaga o original.

## Jornada

1. **Novo projeto:** registra a ideia em `inputs/briefing.md` e inicializa o runtime.
2. **Direção:** escolha trabalhar na etapa atual, desenvolver a jornada ou perguntar.
   A execução usa Codex CLI e os recursos reais de subagentes desse ambiente.
3. **Documentos:** leia e edite; cada edição exige motivo, confere o hash anterior e
   preserva uma cópia local. Alterações posteriores reabrem as etapas dependentes.
4. **Equipe e decisões:** mostra tarefas e pareceres registrados, sem progresso inventado.
5. **Visual:** abre arquivos reais de storyboard e mídia já existentes. O exemplo
   Remenda é identificado como exemplo e não substitui a produção do projeto.
6. **Revisão:** aprovação humana exige uma etapa válida. Pedir alteração invalida as
   rodadas anteriores e exige nova avaliação. Desenvolvimento não significa aprovação.
7. **Exportar:** baixa os arquivos reais do projeto; controles privados `.dashboard`
   e arquivos ocultos não entram no ZIP. Esse ZIP não inclui a instalação da skill.

## Conexão e limites

Se houver mais de uma instalação do Codex, `--codex-binary "/caminho/codex"`
escolhe explicitamente o executável, sem alterar o modelo ou a configuração global.
O modelo configurado precisa ser compatível com a versão do CLI.

O Codex CLI deve estar no PATH do servidor e conectado por `codex login`. O painel
não recebe senhas ou chaves. A conversa consome os limites da conta conectada. Se
houver indisponibilidade ou limite, a falha aparece no painel e os arquivos ficam
preservados. Uma execução finalizada não aprova etapas automaticamente.

Cada projeto permite uma execução por vez. Cancelar interrompe o processo; mudanças
já feitas permanecem e devem ser revisadas. Se uma rodada tiver sido interrompida,
use Pedir alteração para registrar a retomada e abrir uma nova rodada. Sem subagentes
reais disponíveis, a direção deve informar a limitação e parar, sem simular uma equipe.

O painel bloqueia edição, aprovação e exportação durante uma execução ativa. As
consultas continuam disponíveis. Os logs locais ficam em `.dashboard` e o estado
criativo em `00_PROJECT_STATE.json`. A interface não gera imagens, áudio ou vídeo
sozinha: mostra os artefatos produzidos pelas ferramentas disponíveis à equipe.

O link é local e não funciona no computador de outra pessoa. Compartilhe o ZIP do
projeto. Não exponha o servidor à internet. Publicação, compras, geração paga e
mensagens externas continuam dependendo de autorização específica.
