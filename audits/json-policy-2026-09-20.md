# Auditoria global — política de JSON condicional

**Data:** 20/09/2026

## Decisão

A política anterior de criação automática de `.json` para todo texto editorial foi revogada.

Padrão vigente:

- **Markdown**: fonte textual canônica;
- **HTML**: publicação, quando houver;
- **JSON/JSONL**: somente quando existir função estruturada real, com finalidade de máquina identificável.

JSON não deve ser criado apenas para repetir texto, título, resumo, outline, caminhos ou metadados já adequadamente preservados no Markdown/HTML.

## Repositórios auditados

1. `thiagoba2004/acoes-judiciais`
2. `thiagoba2004/planejamento-financeiro`
3. `thiagoba2004/classe-e-massas`
4. `thiagoba2004/gerador-de-agents`
5. `thiagoba2004/ordem-dos-advogados`
6. `thiagoba2004/painel-judiciario`
7. `thiagoba2004/conselhos-profissionais`
8. `thiagoba2004/taxonomia-rfb`

## Remoções

### Ações Judiciais
- 12 JSON editoriais/públicos redundantes removidos.
- Permanecem: `PROJECT_STATE.json` e registros `.jsonl`.

### Planejamento Financeiro
- 20 JSON editoriais/públicos redundantes removidos.
- Permanecem: `PROJECT_STATE.json` e registros `.jsonl`.

### Classe e Massas
- 46 JSON redundantes removidos.
- O conjunto removido inclui 45 espelhos de textos com Markdown + HTML e o espelho JSON da antiga auditoria de triplicidade.
- A auditoria histórica em Markdown foi preservada e marcada como regra superada.

**Total removido: 78 arquivos JSON.**

## JSON preservados por função real

### Classe e Massas
Foram preservados 23 JSON funcionais, incluindo:
- `PROJECT_STATE.json`;
- datasets de Biblioteca;
- rankings;
- política estruturada de traduções;
- ficha jurídica, glossário, manifest e texto-base estruturados do TCM-001;
- metadados canônicos `*.metadata.json`;
- `governanca/STRATEGY_MAP.json`;
- catálogo de documentos canônicos.

### Gerador de Agents
Foram preservados:
- estado do projeto;
- perfis estruturados;
- templates JSON de perfil/estado;
- registros JSONL.

### Painel Judiciário
- `.devcontainer/devcontainer.json` preservado como configuração técnica.

### Ordem dos Advogados / Conselhos Profissionais
- repositórios vazios; nada a remover.

### Taxonomia RFB
- nenhum JSON existente.

## Critério permanente

Antes de criar um novo JSON, responder:

1. **Qual processo consome este JSON?**
2. **Qual dado estruturado ele preserva que o Markdown não atende adequadamente?**

Sem resposta concreta, o JSON não deve ser criado.

## Gerador

A política foi propagada para:
- `AGENTS.md`;
- `modules/publication.md`;
- `templates/AGENTS.example.md`;
- `templates/PROJECT_PROFILE.example.json`;
- perfis de Ações Judiciais, Planejamento Financeiro e Classe e Massas;
- `CHANGELOG.md` — versão 1.10;
- `PROJECT_STATE.json`.

## Observação sobre buscas e auditorias por IA

Modelos de IA não dependem de um JSON narrativo duplicado para pesquisar, revisar ou auditar textos. Para conteúdo textual, Markdown é normalmente mais direto e suficiente. JSON agrega valor quando a tarefa exige estrutura de campos, relações, estados, filtros, validação ou processamento automatizado.
