# CHANGELOG — GERADOR DE AGENTS

Todas as alterações materiais do núcleo universal e da infraestrutura do Gerador devem ser registradas aqui.

## 1.3 — 17/09/2026 — Gerador operacional sobre kernel 1.2

- criação de `GERADOR_WORKFLOW.md` com rotas distintas para projeto novo e projeto existente;
- criação de `MODULE_SELECTION.md` com estados conceituais `ATIVADO`, `NÃO APLICÁVEL` e `PENDENTE DE EVIDÊNCIA`, além dos códigos estruturados equivalentes;
- criação de `templates/AGENTS.example.md`, `templates/AUDIT_REPORT.example.md` e `templates/PROJECT_PROFILE.example.json`;
- criação dos módulos `research`, `legal`, `publication`, `digital-evidence`, `translation`, `software`, `data` e `automation`;
- primeiro teste integral não destrutivo no projeto `thiagoba2004/classe-e-massas`;
- criação e consolidação de `profiles/classe-e-massas.json` e `audits/classe-e-massas-2026-09-17.md`;
- identificação, no teste real, de conflito entre a ordem antiga de registro do `AGENTS.md` v1.8 do Classe e Massas e a ordem vigente do kernel 1.2;
- recuperação dos pedidos históricos `REQ-20260917-011` a `REQ-20260917-014` a partir do `REQUEST_LOG.jsonl` do Classe e Massas;
- backfill comprovado dos eventos históricos de criação, evolução e pausa de `STRAT-GDA-20260917-001` a partir do `STRATEGY_LOG.jsonl` do Classe e Massas;
- preservação integral e verificável da instrução histórica v1.1 em quatro segmentos em `history/`, com SHA-256 original `abf7089cb7896dd33b419126192c5da8ab6ea1bb98922a02fe44f6933ae002e2`;
- criação de `README.md` como ponto de entrada para novos modelos/agentes;
- correção do workflow para reproduzir integralmente a ordem do kernel 1.2 e distinguir `AUDITAR ≠ MIGRAR ≠ IMPLANTAR`;
- atualização de `AGENTS.md` para refletir a arquitetura operacional real do repositório;
- alinhamento entre `MODULE_SELECTION.md`, template de perfil e perfil auditado, incluindo `decided_at` e `kernel_version` por decisão;
- revisão de `automation` no perfil do Classe e Massas para `PENDENTE_DE_EVIDENCIA` por insuficiência de evidência para ativação;
- inclusão de `STRAT-CEM-20260917-001` no `STRATEGY_REGISTRY.jsonl` apenas com estado comprovado pelo log local;
- autoauditoria registrada em `audits/gerador-de-agents-self-audit-2026-09-17.md` com gate da Fase 5 satisfeito;
- conclusão das Fases 4, 5 e Final do roadmap;
- declaração do Gerador de Agents **1.3** como versão operacional inicial sobre o kernel **1.2**;
- conclusão da estratégia de bootstrap `STRAT-GDA-20260917-001` e transição do projeto para modo operacional/manutenção.

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
