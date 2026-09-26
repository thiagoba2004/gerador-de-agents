# Módulo: Knowledge Index

**module_id:** `knowledge-index`

## Finalidade

Oferecer descoberta rápida, auditável e independente do índice de código do provedor Git sobre todo acervo textual persistente do projeto.

## Regra

Projetos com corpus persistente relevante devem manter índice semântico-factual próprio em `governanca/KNOWLEDGE_INDEX.jsonl`, gerado por ferramenta determinística. O índice é infraestrutura interna e não conteúdo público.

## Princípios

1. Não duplicar texto integral em JSON.
2. Indexar metadados, hashes, títulos, headings, termos, fontes externas, identificadores e tags.
3. Consultar o índice antes de varreduras manuais extensas.
4. Confirmar no documento original antes de usar o achado substantivamente.
5. Regenerar após mudanças materiais.
6. Permitir consulta cruzada entre projetos por catálogo de índices.
7. Distinguir “nenhuma ocorrência no índice atualizado” de “inexistência absoluta”.
