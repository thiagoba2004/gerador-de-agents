# CHANGELOG — GERADOR DE AGENTS

Todas as alterações materiais do núcleo universal e da infraestrutura do Gerador devem ser registradas aqui.

## 1.2 — 17/09/2026

- implantação do repositório independente `thiagoba2004/gerador-de-agents`;
- criação do `AGENTS_KERNEL.md` v1.2;
- criação do `AGENTS.md` do próprio Gerador;
- adoção formal de `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl`, `STRATEGY_REGISTRY.jsonl`, `PROJECT_STATE.json` e `ROADMAP.md`;
- alteração da ordem operacional dos pedidos: registrar primeiro, confirmar o registro, informar “Pedido registrado.” e somente depois iniciar leitura substantiva, análise, ferramentas ou execução;
- formalização da arquitetura núcleo universal + perfil do projeto + módulos especializados;
- preservação de `strategy_id` e `project_id` estáveis e do modelo append-only de estratégias.

## 1.1 — 17/09/2026

- obrigatoriedade de `STRATEGY_LOG.jsonl` em todos os projetos;
- instituição de `strategy_id` e `project_id`;
- eventos append-only;
- backfill controlado por evidência persistente;
- criação conceitual do `STRATEGY_REGISTRY.jsonl` agregado.

## 1.0 — 17/09/2026

- criação das instruções canônicas do Projeto Gerador de Agents;
- definição do kernel universal, perfis de projeto e módulos especializados.
