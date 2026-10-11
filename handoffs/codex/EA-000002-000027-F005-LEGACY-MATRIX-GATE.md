# Handoff CODEX — EA-000002-000027 F005 / regressão de EA legada no gate SCIV

**Emissão:** G0/CHAT, 11/10/2026, em decorrência do teste real `PRJ-000022 / EA-000022-000003 / F004`. **Autoridade:** REQ-20261011-008 e REQ-GLOBAL-20261011-001; aditamento documental da EA027 ACT-010. **Executor da mudança de código:** CODEX CLI Local, checkout `thiagoba2004/gerador-de-agents`, somente este repositório.

## Falha concreta

O `tools/project_creation_gate.py` exige `estrategias/EA-000022-000001-actions.json` ao verificar `--route A --gate sciv` no PRJ-000022 já constituído, concluído e versionado em 10/10/2026. A matriz por ação entrou em vigor em 11/10/2026; norma `EXECUTION_ACTION_PLAN_STANDARD.md` §EAs legadas determina **preservar história** e registrar ações passadas como `NOT_BACKFILLED`, sem inventar planejamento prévio. O relatório do Codex `thiagoba2004/instituicoes-bancarias/auditorias/EA-000022-000003-codex-f002-f004-2026-10-11.md` confirma `FIRST_EA_ACTION_PLAN_UNVERIFIED`, e `governanca/testes-sciv/gate-sciv.log` detalha. Não criar matriz fictícia EA000001 só para contornar um gate técnico.

## Correção desejada

1. Introduzir distinção verificável entre **nova constituição** (`--gate bootstrap`, exigir plano/matriz desde a origem) e **validação posterior SCIV/Site/post_native de PRJ existente cujo bootstrap precedeu a norma**. Condição de legado deve ter evidência documental independente: `CREATED`, plano e fases existentes, evento `CONCLUDED` ou prova equivalente, origem/época/versionamento compatíveis; nenhuma dispensa baseada apenas em string não autenticada do estado. Registrar no resultado o status explicativo `LEGACY_FIRST_EA_MATRIX_NOT_BACKFILLED` e referências de prova, sem declarar `action_plan_result=PASS` quando matriz ausente.
2. Rejeitar ausência/matriz defeituosa para novas EAs criadas após vigência e para uma primeira EA não comprovadamente histórica. Não dispensar planos/REQUEST/CREATED/namespace/WIP ou o contrato **da EA SCIV corrente**; separar invariantes do legado e do novo rollout.
3. Adicionar testes unitários positivos/negativos de Rota A nova vs histórica, Rota B, retorno ao gate SCIV/Site, status `NOT_BACKFILLED`, prevenção de falso positivo, idempotência. Não enfraquecer fail-closed, PEP, classificação, C3 nativo ou Site publicação.
4. Executar suites atuais e, se houver workflow preexistente autorizado, CI; registrar contagem real, commit, readback, relatório. Não modificar o PRJ-000022 ou G0 via esse executor. Depois, o Codex no PRJ-000022 deverá repetir seus gates e registrar nova evidência.

**Etapas de preflight:** `git status`, `git worktree list`, fetch/sync seguro, preservar `.sciv-issue5-worktree/` e quaisquer alterações locais; não usar reset, clean ou force push. Não alegar teste ou PEP live por análise documental. Se segurança não puder ser provada, deixar BLOCKED com causa/owner/próximo passo. Sem nova despesa, credencial, permissão ou serviço.

**Relação estratégica:** a EA027 permanece F005 até regressão; não reabrir ACT-006 (Site já VERIFIED), não avançar F006 por esta remediação. A G0 EA034 F003 continua BLOCKED aguardando também teste runtime de branch e ensaio symlink em ambiente compatível.
