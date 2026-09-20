# ROADMAP — GERADOR DE AGENTS

**project_id:** `GDA`  
**strategy_id de bootstrap:** `STRAT-GDA-20260917-001`  
**status:** OPERACIONAL  
**data de início no repositório:** 17/09/2026  
**versão operacional inicial:** `1.3`  
**kernel vigente:** `1.2`

## Objetivo

Implantar o Projeto Gerador de Agents como repositório independente, capaz de criar, auditar, adaptar, atualizar e versionar `AGENTS.md` para outros projetos, com núcleo universal, perfis de projeto, módulos especializados e infraestrutura de continuidade, persistência e rastreabilidade.

## Plano de Fases da estratégia de bootstrap

### FASE 1 — Registro e delimitação

**Estado:** CONCLUÍDA

**Gate atingido:** `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl`, `PROJECT_STATE.json` e roadmap criados e verificados remotamente.

### FASE 2 — Kernel universal

**Estado:** CONCLUÍDA

**Gate atingido:** `AGENTS_KERNEL.md` v1.2 e `AGENTS.md` do próprio Gerador criados, versionados e confirmados no branch `main`.

### FASE 3 — Infraestrutura reutilizável

**Estado:** CONCLUÍDA

**Gate atingido:** templates, módulos, perfis e estruturas auxiliares criados e persistidos.

### FASE 4 — Gerador operacional

**Estado:** CONCLUÍDA

**Gate atingido:** `GERADOR_WORKFLOW.md`, `MODULE_SELECTION.md`, templates operacionais, oito módulos especializados, perfil e relatório de auditoria foram criados. A Rota B foi testada no projeto `thiagoba2004/classe-e-massas` em modo não destrutivo.

### FASE 5 — Consolidação e verificação

**Estado:** CONCLUÍDA

**Gate atingido:** autoauditoria registrada em `audits/gerador-de-agents-self-audit-2026-09-17.md`; inconsistências de workflow, arquitetura, esquema de módulos, perfil, auditoria, registry e preservação histórica foram corrigidas. A versão 1.1 foi preservada integralmente e verificada em `history/`.

### FASE FINAL — Implantação do Gerador

**Estado:** CONCLUÍDA

**Objetivo:** declarar a versão operacional inicial, confirmar persistência/versionamento remoto e encerrar a estratégia de bootstrap.

**Gate atingido:** versão operacional `1.3` declarada sobre kernel `1.2`; estado, roadmap, changelog, logs e registro agregado sincronizados; repositório possui ponto de entrada e documentação suficiente para reconstrução sem o chat.

## Estado pós-bootstrap

O Gerador entra em **modo operacional/manutenção**. A estratégia `STRAT-GDA-20260917-001` não deve permanecer artificialmente aberta depois de cumprido seu objetivo.

Novas evoluções materiais devem ser classificadas conforme o kernel:

- continuação/ajuste pequeno de trabalho ainda pertencente a estratégia existente → registrar evento na estratégia correspondente;
- nova frente autônoma de evolução, novo módulo complexo, nova geração ou mudança arquitetural relevante → criar novo `strategy_id` antes da execução substantiva.

## Dívidas não bloqueantes conhecidas

- migração efetiva do Classe e Massas para o kernel 1.2 — pertence ao projeto-alvo e exige execução específica;
- backfill progressivo das demais estratégias do Classe e Massas — pertence ao log local daquele projeto;
- testes futuros adicionais da Rota A e expansão de módulos — evolução normal do Gerador.

## Próximo passo lógico

Aguardar novo pedido. Ao recebê-lo, registrar primeiro em `REQUEST_LOG.jsonl` e decidir, antes da execução substantiva, se ele pertence a manutenção simples ou cria nova Estratégia Autônoma.


## EA-000002-000007 — Padrão reutilizável de Sites e Contato Protocolado

1. FASE 01/05 [F-000002-000007-001] — Auditoria e delimitação.
2. FASE 02/05 [F-000002-000007-002] — Módulos reutilizáveis.
3. FASE 03/05 [F-000002-000007-003] — Propagação do Gerador.
4. FASE 04/05 [F-000002-000007-004] — Migração dos projetos piloto.
5. FASE 05/05 [F-000002-000007-005] — Verificação e fechamento.
