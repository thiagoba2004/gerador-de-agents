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


## Manutenção 1.10 — JSON condicional

**Estado:** CONCLUÍDA em 20/09/2026.

**Decisão:** revogada a criação automática do trio Markdown + HTML + JSON.

Padrão vigente:
- Markdown = fonte textual canônica;
- HTML = publicação quando houver;
- JSON/JSONL = somente quando houver função estruturada real e consumidor/processo identificável.

**Gate atingido:**
- módulo `publication` atualizado;
- template de AGENTS atualizado;
- template de perfil atualizado;
- perfis de Classe e Massas, Ações Judiciais e Planejamento Financeiro atualizados;
- política propagada aos projetos;
- auditoria global registrada em `audits/json-policy-2026-09-20.md`;
- 78 JSON redundantes removidos dos projetos auditados, preservando todos os JSON funcionais.
## EA-000002-000008 — Padrão editorial de Atualidade, Análise e Observação para Sites — EM EXECUÇÃO

Plano: `estrategia-padrao-atualidade-analise-observacao.md`.

1. FASE 01/06 [F-000002-000008-001] — Diagnóstico e estado da arte — CONCLUÍDA.
2. FASE 02/06 [F-000002-000008-002] — Modelo canônico das três funções editoriais — CONCLUÍDA.
3. FASE 03/06 [F-000002-000008-003] — Propagação normativa no Gerador — PENDENTE.
4. FASE 04/06 [F-000002-000008-004] — Sincronização dos perfis piloto — PENDENTE.
5. FASE 05/06 [F-000002-000008-005] — Regras de composição do menu e mapa do site — PENDENTE.
6. FASE 06/06 [F-000002-000008-006] — Auditoria cruzada e fechamento — PENDENTE.

**Próximo passo lógico:** Fase 03/06 — materializar o padrão em `modules/web-site.md`, `modules/publication.md`, `modules/research.md`, `AGENTS.md` e templates, sem ainda alterar os Sites Públicos dos projetos-piloto.
