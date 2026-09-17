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

**Estado:** EM EXECUÇÃO

**Objetivo:** transformar a arquitetura documental em procedimento executável para projeto novo e projeto existente, incluindo auditoria, migração, atualização, seleção de módulos e relatório de lacunas.

**Gate:** fluxo completo testado em pelo menos um projeto de referência sem sobrescrever personalizações locais.

### FASE 5 — Consolidação e verificação

**Estado:** NÃO INICIADO

**Objetivo:** auditar consistência entre kernel, templates, logs, estado, changelog e instruções do próprio Gerador.

**Gate:** nenhuma contradição material conhecida e repositório capaz de reconstruir seu próprio estado sem depender do chat.

### FASE FINAL — Implantação do Gerador

**Estado:** NÃO INICIADO

**Objetivo:** declarar a versão inicial do Gerador operacional, registrar o marco no changelog e encerrar a estratégia de bootstrap ou abrir estratégia sucessora de evolução.

**Gate:** persistência, versionamento remoto e verificação final confirmados.

## Próximo passo lógico

Desenvolver a Fase 4: procedimento operacional reproduzível para criação e migração de `AGENTS.md`, incluindo template de `AGENTS.md`, relatório de auditoria e mecanismo explícito de seleção de módulos/perfis.
