# ROADMAP — GERADOR DE AGENTS

**project_id:** `GDA`  
**strategy_id:** `STRAT-GDA-20260917-001`  
**status:** EM EXECUÇÃO  
**data de início no repositório:** 17/09/2026

## Objetivo

Implantar o Projeto Gerador de Agents como repositório independente, capaz de criar, auditar, adaptar, atualizar e versionar `AGENTS.md` para outros projetos, com núcleo universal, perfis de projeto, módulos especializados e infraestrutura de continuidade, persistência e rastreabilidade.

## Plano de Fases

### FASE 1 — Registro e delimitação

**Estado:** CONCLUÍDA

**Objetivo:** estabelecer identidade do projeto, logs obrigatórios, fonte canônica, estratégia vigente e estrutura mínima do repositório.

**Gate atingido:** `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl`, `PROJECT_STATE.json` e roadmap criados e verificados remotamente.

### FASE 2 — Kernel universal

**Estado:** CONCLUÍDA

**Objetivo:** criar `AGENTS_KERNEL.md`, separar regras universais de regras específicas e definir esquema de versionamento do kernel.

**Gate atingido:** `AGENTS_KERNEL.md` v1.2 e `AGENTS.md` do próprio Gerador criados, versionados e confirmados no branch `main`.

### FASE 3 — Infraestrutura reutilizável

**Estado:** CONCLUÍDA

**Objetivo:** criar `templates/`, `modules/` e `profiles/`, com esquemas mínimos para pedidos, estratégias, estado e planejamento.

**Gate atingido:** diretórios criados; templates de `REQUEST_LOG`, `STRATEGY_LOG`, `PROJECT_STATE` e `ROADMAP` persistidos e verificados remotamente; regras-base de módulos e perfis documentadas.

### FASE 4 — Gerador operacional

**Estado:** CONCLUÍDA

**Objetivo:** transformar a arquitetura documental em procedimento executável para projeto novo e projeto existente, incluindo auditoria, migração, atualização, seleção de módulos e relatório de lacunas.

**Gate atingido:** workflow operacional, seleção determinística de módulos, templates de `AGENTS` e auditoria, módulos especializados e perfil de projeto foram criados; o fluxo foi testado de ponta a ponta no projeto `thiagoba2004/classe-e-massas` em modo não destrutivo, gerando `profiles/classe-e-massas.json` e `audits/classe-e-massas-2026-09-17.md` sem sobrescrever personalizações locais.

### FASE 5 — Consolidação e verificação

**Estado:** EM EXECUÇÃO

**Objetivo:** auditar consistência entre kernel, templates, logs, estado, changelog e instruções do próprio Gerador.

**Gate:** nenhuma contradição material conhecida e repositório capaz de reconstruir seu próprio estado sem depender do chat.

**Itens de verificação:**

- coerência entre `AGENTS_KERNEL.md`, `AGENTS.md`, `GERADOR_WORKFLOW.md` e `MODULE_SELECTION.md`;
- completude de templates, módulos e perfis;
- sincronização entre `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl`, `STRATEGY_REGISTRY.jsonl`, `PROJECT_STATE.json` e este roadmap;
- registro histórico dos pedidos e da estratégia anteriores ao repositório próprio;
- atualização do `CHANGELOG.md`;
- preservação documental da versão histórica v1.1;
- existência de um ponto de entrada claro para novos agentes/modelos.

### FASE FINAL — Implantação do Gerador

**Estado:** NÃO INICIADO

**Objetivo:** declarar a versão inicial do Gerador operacional, registrar o marco no changelog e encerrar a estratégia de bootstrap ou abrir estratégia sucessora de evolução.

**Gate:** persistência, versionamento remoto e verificação final confirmados.

## Próximo passo lógico

Concluir a autoauditoria da Fase 5, corrigir as lacunas documentais encontradas, verificar remotamente os arquivos críticos e somente então decidir se o gate da Fase 5 permite avançar à implantação final.
