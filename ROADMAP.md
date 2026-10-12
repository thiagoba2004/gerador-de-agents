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
## EA-000002-000008 — Padrão editorial de Atualidade, Análise e Observação para Sites — CONCLUÍDA

Plano: `estrategia-padrao-atualidade-analise-observacao.md`.

1. FASE 01/06 [F-000002-000008-001] — Diagnóstico e estado da arte — CONCLUÍDA.
2. FASE 02/06 [F-000002-000008-002] — Modelo canônico das três funções editoriais — CONCLUÍDA.
3. FASE 03/06 [F-000002-000008-003] — Propagação normativa no Gerador — CONCLUÍDA.
4. FASE 04/06 [F-000002-000008-004] — Sincronização dos perfis piloto — CONCLUÍDA.
5. FASE 05/06 [F-000002-000008-005] — Regras de composição do menu e mapa do site — CONCLUÍDA.
6. FASE 06/06 [F-000002-000008-006] — Auditoria cruzada e fechamento — CONCLUÍDA.

**Resultado:** Gerador 1.11 aprovado em 13/13 controles. Próxima execução pertence às estratégias locais dos PRJ-000003 e PRJ-000004.


## EA-000002-000013 — Reconciliação canônica pós-Observatório e continuidade determinística — CONCLUÍDA

1. FASE 01/04 [F-000002-000013-001] — Inventário de divergências canônicas — CONCLUÍDA.
2. FASE 02/04 [F-000002-000013-002] — Reconciliação dos projetos piloto — CONCLUÍDA.
3. FASE 03/04 [F-000002-000013-003] — Sincronização do registro agregado — CONCLUÍDA.
4. FASE 04/04 [F-000002-000013-004] — Auditoria cruzada e fechamento — CONCLUÍDA.

**Resultado:** GDA 1–13, AJ 1–27 e PF 1–42 contíguos no registro agregado; ROADMAPs reconciliados; pendência material preservada no PRJ-000003: 10 achados da EA-000003-000019 ainda sem correção pública integral comprovada.


## EA-000002-000014 — Padrão reutilizável de navegação dinâmica responsiva — CONCLUÍDA

1. FASE 01/03 [F-000002-000014-001] — Delimitação da lacuna — CONCLUÍDA.
2. FASE 02/03 [F-000002-000014-002] — Atualização do módulo web-site e template AGENTS — CONCLUÍDA.
3. FASE 03/03 [F-000002-000014-003] — Auditoria, registro agregado e fechamento — CONCLUÍDA.

**Resultado:** Gerador 1.16 passa a distinguir responsividade estática de navegação dinâmica; menu denso no mobile deve preferir disclosure/recolhimento acessível, com fallback sem JavaScript.


## EA-000002-000022 — Arquitetura Universal v2 — Isolamento, Fontes de Conhecimento e Handoff

1. FASE 01/04 [F-000002-000022-001] — Registro, diagnóstico e modelo v2 — CONCLUÍDA.
2. FASE 02/04 [F-000002-000022-002] — Kernel, módulo e templates — CONCLUÍDA.
3. FASE 03/04 [F-000002-000022-003] — Propagação aos Projetos — CONCLUÍDA.
4. FASE 04/04 [F-000002-000022-004] — Auditoria, release e fechamento — CONCLUÍDA.

**Resultado:** Gerador 1.24 / Kernel 1.9; arquitetura v2 propagada e auditada.


## EA-000002-000027 — Ciclo de criação de Projetos, Instruções e testes por Comunicados (11/10/2026)

**Estado:** IN_PROGRESS, F001. **Autoridade:** REQ-20261011-008 e programa global EA-000000-000034. **Plano de Fases:** `estrategias/EA-000002-000027-ciclo-criacao-projeto-sciv-recebimento.md`.

1. F001 — Baseline, namespace, inventário/mandatos.
2. F002 — Contrato Rota A/B: EA inicial + Plano obrigatório, B1/C3, SCIV opt-in, Instruções.
3. F003 — Gate determinístico que rejeita Projeto novo sem EA e Plano; verificação SCIV local.
4. F004 — Templates, comunicação A6/B8 após instalação de Instruções, teste SCIV em separado.
5. F005 — Regressão, idempotência, compatibilidade e proveniência.
6. F006 — Auditoria, readback, registro dual e fechamento.

**Próximo passo:** executar F001 com prova; não confundir registro da estratégia com conclusão do gate ou alteração das instruções nativas dos Projetos.

**Readback de 11/10:** EA-000002-000027 F001 e F002 concluídas em escopo documental, conforme eventos -002/-003. F003 contém validador e testes versionados, **mas a suíte Python não foi executada/verificada**; F003 continua IN_PROGRESS_TESTS_PENDING, sem promoção das Fases 4-6.

**Checkpoint adicional de 11/10:** F003 concluída com **12 testes PASS** no GitHub Actions [run 38155476207](https://github.com/thiagoba2004/gerador-de-agents/actions/runs/38155476207), após inclusão da suíte `test_project_creation_gate.py` no workflow preexistente Knowledge Index. F004 concluída **somente em escopo documental**, modelos e fluxo A6/B8 por Comunicados versionados. **F005 em andamento:** aplicar/regredir nos quatro Projetos, sem presumir Instruções nativas atualizadas, testes A6/B8 executados ou SCIV aceito.


**Aditamento da F005 (REQ-20261011-009, 11/10/2026):** centralizar **responsabilidade técnica de Sites** no Gerador com padrão compartilhado, identidade/paleta distinta por PRJ e **EA local de Site com Plano de Fases quando autorizada**. Criar modelo `templates/WEBSITE_PUBLICATION_EA.example.md`, estado de publicação, gate/contraste e testes. PRJ-000007/008 já possuem EAs de Site (F004 bloqueada por Pages), sem reabertura artificial. PRJ-000022/023 não tiveram site autorizado. SCIV global 034 coordena rollout, **não substitui EAs locais**; publicação do Site não é gate SCIV. F005 continua IN_PROGRESS até evidências.

**Aditamento F005 (REQ-20261011-010):** norma de **planejamento por ação** com responsável, executor, ferramenta, ambiente, autorização, prova, custo e bloqueio; Gerador valida matriz por fase, atualiza templates e exige matriz na Rota A. A EA-000002-000027 continua F005 até readback e testes; não declarar enforcement universal do catálogo/PEP.

**Checkpoint de 11/10 — Matriz por ação publicada e testada:** EA-000002-000027 tem `estrategias/EA-000002-000027-actions.json` (9 ações em 6 fases); a EA global 034 possui matriz de 27 ações/8 fases. `EXECUTION_ACTION_PLAN_STANDARD.md` é política canônica. CI [run 38157073016](https://github.com/thiagoba2004/gerador-de-agents/actions/runs/38157073016): **14 testes Rota A/SCIV + 12 testes do novo validador + arquivo real da EA27 PASS**. A F005 permanece IN_PROGRESS; site gate, rollout aos quatro PRJ e F006 continuam pendentes. Este PASS não é enforcement universal do dispatcher/PEP.


## Checkpoint EA-034 / F002 — planos locais SCIV (11/10/2026)

No escopo de EA-000002-000027 F005, o Gerador reconciliou a numeração nos logs locais dos quatro Projetos e preparou em `handoffs/sciv/EA-000000-000034/` quatro **propostas**, ainda sem CREATED nos destinatários: `EA-000022-000003` (reservar `000002` à missão/handoff), `EA-000023-000002`, `EA-000007-000003`, `EA-000008-000003`. Os perfis registram opt-in autorizado, `mode=ON_DEMAND`, **enabled=false** até provisionamento/testes. Piloto PRJ-000021 reconciliado como HUMAN_ATTESTED, sem prova independente da UI. Relatório `audits/EA-000000-000034-F002-preparacao-gerador-2026-10-11.md`.

**Pendências sem promoção de fase:** Codex do Gerador executará regressões/CI; G0 corrigirá `ACT-000000-000034-003` da matriz global (que ainda aponta equivocadamente `EA-000022-000002` para SCIV). Nenhum código do PRJ, Instrução nativa, mensagem real ou website foi alterado; F002 global segue aberta, F005 local segue IN_PROGRESS.


**Checkpoint CODEX 11/10 — FASE 05/06 [F-000002-000027-005] — Integração e compatibilidade:** ACT-000002-000027-006 VERIFIED em escopo de implementação e regressão offline; gate Site condicional com EA própria/paleta/contraste, 73 testes PASS, matriz real PASS, commit `1ec78aa`. Evidência: [EA-000002-000027-F005-codex-site-2026-10-11.md](audits/EA-000002-000027-F005-codex-site-2026-10-11.md). F005 permanece IN_PROGRESS. Próximo executor: CHAT/Gerador ACT-007 e G0 para correção ACT-000000-000034-003; F006 ACT-008/009 pendentes. Nenhuma escrita nos quatro destinatários, SCIV habilitado, instalação nativa ou publicação.


## Checkpoint CHAT — ACT-000002-000027-007 (11/10/2026)

Confirmada por leitura remota a correspondência dos quatro Planos preparatórios SCIV de seis fases com os perfis `ON_DEMAND` autorizados, `enabled=false`, e logs locais sem CREATED. Corrigido no plano/matriz da EA global o código do PRJ-000022 para **EA-000022-000003**; `EA-000022-000002` permanece reservada à finalidade de missão/handoff a formalizar, não a SCIV. **ACT-007 VERIFIED no escopo de conferência documental read-only**, conforme `audits/EA-000002-000027-F005-chat-sciv-handoff-2026-10-11.md`. ACT-006 continua VERIFIED (Codex, 73 testes, CI 38167801309). F005 permanece **IN_PROGRESS**, sem avançar F006, sem EAs locais criadas, sem instalação nativa ou alteração nos quatro alvos. Próxima frente: G0 decide gate F002 da EA-034 sem presumir provisionamento; se for bloqueado, persistir motivo e responsável.

## Regressão do rollout real PRJ-000022 — ACT-010 (11/10/2026)

**Checkpoint CODEX ACT-010:** correção implementada, 88 testes PASS e compatibilidade documental PRJ-000022 verificada somente em leitura; EA000001 `NOT_BACKFILLED`, EA SCIV corrente EA000003 matriz PASS, bootstrap A estrito preservado. Relatório: `audits/EA-000002-000027-F005-codex-legacy-matrix-2026-10-11.md`. CI/readback constam do checkpoint remoto subsequente. FASE 05/06 [F-000002-000027-005] continua IN_PROGRESS; ACT006/007 preservadas, sem F006 ou promoção de gates dos destinatários.

No PRJ-000022, CODEX concluiu SCIV local F002/F003 no repositório (commits `6700203` e `dd38b14`), mas F004 falhou em `FIRST_EA_ACTION_PLAN_UNVERIFIED` porque o `--route A --gate sciv` do Gerador exige matriz da primeira EA de constituição concluída antes da adoção do contrato de ações. Norma global proíbe backfill fictício de ações históricas. **EA-000002-000027 F005: ACT-010 PLANNED, executor CODEX Local no Gerador**, roteiro `handoffs/codex/EA-000002-000027-F005-LEGACY-MATRIX-GATE.md`. Testar distinção Rota A nova/histórica e regressão; sem enfraquecer validação, sem substituir CODEX por CHAT. ACT006/007 permanecem VERIFIED, F005 continua IN_PROGRESS, F006 não começou. Independente: G0 runtime `EA-000000-000034 ACT028` trata fixture branch/symlink; depois CODEX PRJ000022 repete F004. Nenhuma UI nativa/C3/A6 ou site publicada.
