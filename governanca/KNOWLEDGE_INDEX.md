# Mecanismo universal de indexação semântica e factual

## Finalidade

Permitir que perguntas do tipo “isso já existe no Projeto?”, “onde citamos X?”, “quais fontes usamos?”, “em quais documentos aparece determinada instituição, Estratégia, tema, DOI ou URL?” sejam respondidas sem varredura manual integral do repositório.

## Artefatos

- `tools/build_knowledge_index.py` — gera índice determinístico do acervo textual;
- `tools/query_knowledge_index.py` — consulta um ou vários índices;
- `governanca/KNOWLEDGE_INDEX.jsonl` — um registro por arquivo indexável;
- `governanca/KNOWLEDGE_INDEX_META.json` — contagens e metadados do índice.

## Conteúdo do índice

Cada registro contém caminho, extensão, tamanho, SHA-256, título, headings, palavras-chave, tags semânticas controladas, domínios externos, sistemas de fonte reconhecidos e identificadores persistentes/canônicos (Projeto, Estratégia, Fase, pedido, DOI e Handle).

O índice **não replica o texto integral**. Markdown/HTML continuam com suas funções próprias. JSONL existe aqui por necessidade real de processamento por máquina.

## Regra de consulta

Para perguntas transversais sobre o acervo, consultar primeiro o índice. Se houver resultado material, abrir os arquivos apontados para confirmar o contexto. Resultado nulo do índice deve ser qualificado pela data/estado da última geração; não substituir verificação direta quando o índice estiver desatualizado.

## Atualização

O índice deve ser regenerado após alterações materiais do corpus. O workflow `.github/workflows/knowledge-index.yml` automatiza a atualização e evita loop de commits ao ignorar alterações exclusivamente nos arquivos gerados.

## Limites

Tags e palavras-chave são mecanismos de descoberta, não conclusões substantivas. A fonte da verdade continua sendo o documento original.
