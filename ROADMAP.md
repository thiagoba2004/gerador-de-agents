# ROADMAP — GERADOR DE AGENTS

**project_id:** `GDA`  
**strategy_id:** `STRAT-GDA-20260917-001`  
**status:** EM EXECUÇÃO  
**data de início no repositório:** 17/09/2026

## Objetivo

Implantar o Projeto Gerador de Agents como repositório independente, capaz de criar, auditar, adaptar, atualizar e versionar `AGENTS.md` para outros projetos, com núcleo universal, perfis de projeto, módulos especializados e infraestrutura de continuidade, persistência e rastreabilidade.

## Plano de Fases

### FASE 1 — Registro e delimitação

**Estado:** EM EXECUÇÃO

**Objetivo:** estabelecer identidade do projeto, logs obrigatórios, fonte canônica, estratégia vigente e estrutura mínima do repositório.

**Gate:** existência e verificação de `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl`, `PROJECT_STATE.json`, instruções canônicas e roadmap.

### FASE 2 — Kernel universal

**Estado:** NÃO INICIADO

**Objetivo:** criar `AGENTS_KERNEL.md`, separar regras universais de regras específicas e definir esquema de versionamento do kernel.

**Gate:** kernel versionado, auditável e coerente com as instruções canônicas vigentes.

### FASE 3 — Infraestrutura reutilizável

**Estado:** NÃO INICIADO

**Objetivo:** criar `templates/`, `modules/` e `profiles/`, com esquemas mínimos para pedidos, estratégias, estado e planejamento.

**Gate:** templates válidos e pelo menos a estrutura-base documentada para módulos e perfis.

### FASE 4 — Gerador operacional

**Estado:** NÃO INICIADO

**Objetivo:** definir o procedimento executável para projeto novo e projeto existente, incluindo auditoria, migração, atualização e relatório de lacunas.

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

Concluir a Fase 1, consolidando o estado do projeto e migrando a fonte canônica recuperada para o novo repositório antes de derivar o kernel universal.
