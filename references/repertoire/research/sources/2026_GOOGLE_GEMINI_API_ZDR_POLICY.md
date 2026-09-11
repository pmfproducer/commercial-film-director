# Gemini API — política de retenção usada no gate de transferência externa

- **Source ID:** `SRC-2026-GOOGLE-GEMINI-API-ZDR-POLICY`
- **Organização:** Google AI for Developers
- **URL:** https://ai.google.dev/gemini-api/docs/zdr
- **Termos associados:** https://ai.google.dev/gemini-api/terms
- **Leitura desta ficha:** 2026-08-11
- **Estado:** `POLICY_SNAPSHOT_SUMMARY_NOT_LEGAL_CLEARANCE`

## O que a fonte declara

- Em serviços pagos, prompts, system instructions, arquivos enviados e respostas não são usados para melhorar os produtos do Google.
- Retenção zero não decorre automaticamente de usar a API. Ela depende da configuração/projeto e de evitar ou configurar recursos específicos.
- Logs limitados podem existir para monitoramento de abuso; aprovação ZDR possui condições próprias.
- Grounding, Interactions API, Live API, Files API e caching têm comportamentos de armazenamento específicos.
- A lane deste projeto usa bytes inline em uma chamada stateless de `generate_content`; não usa Files API, grounding, Live API ou explicit caching.

## Autoridade, viés e limite

Fonte primária do provedor para política técnica vigente. É também autodescrição do próprio fornecedor e pode mudar. Esta ficha não prova a configuração de billing/ZDR do projeto, residência de dados, licença do conteúdo, consentimento de voz ou clearance jurídico. Por isso, o receipt registra região como provider-managed, não promete ZDR e bloqueia mídia confidencial, sensível ou com menores.

## Aplicação

O hash desta ficha ancora qual política foi consultada quando um receipt foi emitido. Alteração da ficha quebra o receipt e exige nova autorização. O link vivo continua sendo referência, não snapshot imutável por si só.
