# EA-000002-000027 — Ciclo verificável de criação de Projetos, Instruções e recebimento por SCIV

**Projeto:** PRJ-000002 — Gerador de Agents  
**Autoridade:** solicitação expressa do titular em 11/10/2026; programa global EA-000000-000034; issue #5, ADR-GOV-0009; política de registro dual.  
**Pedido local:** REQ-20261011-008. **Status:** IN_PROGRESS, F001 em execução, demais fases NÃO INICIADAS.  
**Executor:** Gerador e engenharia supervisionada; limite ao repositório do Gerador para esta EA; nenhuma escrita automática em PRJ-alvo ou Instruções nativas.

## Objetivo e critérios de conclusão

Impedir que novos Projetos e a implantação do SCIV fiquem dependentes da memória do Coordenador: o Gerador deve gerar **Estratégia Autônoma de constituição com Plano de Fases antes de trabalho substantivo**, manter estado de continuidade e guiar o fluxo completo até handoff A6/B8 e testes de Comunicados quando houver vínculo especializado/SCIV opt-in. Garantir com regras, templates, checagem determinística (fail closed) e regressões, não somente com orientação textual.

**Invariantes:** identidade PRJ/EA/F única e reconciliada; Rota A nunca inicia trabalho substantivo sem primeira EA e plano; Rota B não reescreve genealogia; Projeto ChatGPT C3 não se presume; SCIV opt-in `ON_DEMAND`; endereço de caixa do próprio PRJ; mensagens publicadas **não acionam** automaticamente chats; instalação de Instruções nativas é ato humano distinto da versão Git; Teste A6/B8 após essa instalação é **distinto** do teste técnico/conversacional do SCIV; recibos novos não sobrescrevem relatórios de 10/10; nenhum gate se autoaprova.

## Fases

| Fase | Atividades obrigatórias | Gate |
|---|---|---|
| **F-000002-000027-001** — Baseline e rastreabilidade | Recuperar GERADOR_WORKFLOW, AGENTS_KERNEL, AGENTS, módulo SCIV, templates, logs/registries, pilotos e EAs locais; verificar namespace 000002, sequência livre 000027, mandatos e autorizações | `GENERATOR_LIFECYCLE_BASELINE_VERIFIED` |
| **F-000002-000027-002** — Contrato completo Rota A/B | Especificar etapas/gates invariantes da primeira EA e plano; novo Projeto ChatGPT quando aplicável; diferenciação de SCIV opt-in, adaptação Git, instalação nativa, A6/B8 por Comunicado, testes SCIV, resposta e arquivo; estados/retomada | `GENERATOR_PROJECT_LIFECYCLE_CONTRACT_VERSIONED` |
| **F-000002-000027-003** — Enforcement determinístico | Implementar validador offline sem efeitos externos que **rejeita bootstrap de PRJ sem EA inicial, plano e vínculo no log**; modo SCIV exige caixas, modo ON_DEMAND e adaptador, sem fingir B1/C3 ou uso nativo | `FIRST_EA_AND_SCIV_GATES_FAIL_CLOSED_TESTED` |
| **F-000002-000027-004** — Modelos e testes de recebimento | Atualizar workflow/AGENTS/kernel/template e módulo SCIV; criar padrão de Comunicado `POST_NATIVE_INSTRUCTIONS_RECEIPT_TEST` e resposta; exigir A6/B8 reexecutado após instalação nativa, um por projeto; distinção dos testes SCIV; gates de persistência/proveniência | `POST_INSTRUCTION_A6_B8_SCIV_WORKFLOW_INTEGRATED` |
| **F-000002-000027-005** — Integração e compatibilidade | Testar cenários Rota A (incluindo ausência da EA), Rota B histórica, opt-in/out SCIV, regeneração idempotente; **acrescentar ciclo de site condicional por EA local, paletas distintas, validador e limites de publicação**; leitura/reconciliação documental. Preservar sites existentes dos PRJ-000007/008 e não criar sites nos PRJ-000022/023 sem mandato. Encaixar futuras EAs locais da EA-034 sem criá-las artificialmente | `GENERATOR_CREATION_AND_CONDITIONAL_SITE_REGRESSION_VERIFIED` |
| **F-000002-000027-006** — Auditoria e continuidade | Commit/readback remoto, registro dual global se autorizado, relatório de evidências, estado/log/ROADMAP, documentação dos limites; publicar próxima ação da EA-034 e encerrar apenas os gates efetivamente aprovados | `GENERATOR_CREATION_FLOW_VERIFIED_IN_SCOPE` |

## Fases do Projeto criado (contrato herdado)

A **EA local de constituição** deve existir fisicamente em `estrategias/` com objetivo, fases e gates próprios; registrar `CREATED` em `STRATEGY_LOG.jsonl`, pedido em `REQUEST_LOG.jsonl`, estado em `PROJECT_STATE.json`, referência no `ROADMAP.md` e catálogo global, sem colisão. A EA inicial permite concluir a **constituição técnica** mesmo com A6 ou B8 pendente, desde que deixe handoff e próxima fase claramente persistidos.

Se o escopo incluir **Projeto ChatGPT especializado**, entregar Instruções versionadas, definir B0/B1 e C2/C3 sem inferência, exigir instalação humana e comprovação de recebimento no próprio contêiner. Se **SCIV habilitado por mandato e evidência**, criar uma **EA local própria** (ou fase explicitamente abrangida em EA vigente validada), provisionar caixas com refs e classificação e compor bloco gerenciado. Depois da instalação manual **repetir o teste A6/B8 específico por comunicado**, entregando ao titular apenas uma mensagem curta de disparo por Projeto. Registrar resposta real com correlação, tratamento e arquivamento bilateral; em separado validar comportamento sob demanda e não leitura em conversa normal. Não usar resultados do SCIV como aceite do A6/B8.

## Bloqueios e escopo

Sem novos custos, gatilhos, workflows, credenciais, permissões ou mudanças nativas automáticas; não intervir nas quatro EAs locais da EA-034 por esta estratégia do Gerador; não reativar EA-033/F004 ou T6; não presumir falhas históricas corrigidas; qualquer bloqueio de ferramenta é bloqueio, não autorização para workaround. Os gates são comprovados por leitura/validação efetiva, nunca pelo texto do plano.

**Próximo passo:** concluir F001 com baseline e preparar implementação da F002, seguindo sem reconfirmação para ações materiais já cobertas.

## Aditamento do titular — Publicação de Sites sob responsabilidade técnica do Gerador (11/10/2026)

**Autoridade:** REQ-20261011-009. **Escopo:** execução no Gerador durante F005, sem criar outra EA transversal. O Gerador passa a manter padrão técnico reutilizável e **EA de Site própria por Projeto**, gerada condicionalmente quando `web-site=ATIVADO` por mandato; o conteúdo especializado continua no PRJ e a publicação/hosting exige executor autorizado. Entregas adicionais: `GERADOR_WORKFLOW.md` §9, `modules/web-site.md`, `templates/WEBSITE_PUBLICATION_EA.example.md`, `templates/SITE_PUBLICATION_STATE.example.json` e gate local site em `tools/project_creation_gate.py`, com testes positivos e negativos e readback.

**Coordenação versus execução:** EA global SCIV-034 coordena **quatro implantações de SCIV**, mas cada PRJ terá EA local SCIV própria. EA do Gerador 027 cria padrões e controles. EAs de sites são **distintas** dessas e já existem para Conselhos Profissionais (`EA-000007-000002`) e Ordem dos Advogados (`EA-000008-000002`); ambas aguardam ação de Pages na F004. Instituições Bancárias e Bancas Examinadoras **não possuem mandato de site aprovado** neste corte. Não incorporar publicação dos sites ao gate de conclusão do SCIV 034.

**F005 permanece IN_PROGRESS** até regressões e compatibilidade testadas. Fases F001–F004 anteriormente classificadas não ganham certificação adicional por este aditamento.

## Aditamento F005 — execução por ação (REQ-20261011-010)

O titular determinou que cada ação de EA possua executor/ferramenta/ambiente designados. Na F005, adotar norma `EXECUTION_ACTION_PLAN_STANDARD.md`, matriz `estrategias/EA-000002-000027-actions.json`, validador e testes; atualizar Kernel/Workflow/templates e gate Rota A. Preservar histórico F001–F004 e não promover F005 sem provas. A ação pode ser bloqueada por ferramenta/segurança sem desaparecer do Plano.

**Matriz de execução por ação:** [EA-000002-000027-actions.json](EA-000002-000027-actions.json). Responsável, executor, ferramenta, ambiente, autorização e gate por ação, conforme norma global. Histórico F001–F004 permanece; F005/F006 não são promovidas por esta inclusão.


## Aditamento de regressão por projeto real — PRJ-000022 (11/10/2026)

O primeiro rollout real PRJ-000022 revelou falha de compatibilidade do `tools/project_creation_gate.py`: com `--route A --gate sciv`, o validador passou a exigir matriz de ações da EA de **bootstrap histórico concluído em 10/10**, anterior à norma de matriz obrigatória de 11/10. `EXECUTION_ACTION_PLAN_STANDARD.md` determina que EAs legadas não recebam planejamento fictício retroativo; registrar lacunas como `NOT_BACKFILLED`. Essa incompatibilidade bloqueou F004 local, apesar de F002 e F003 versionadas. Gate afetado: `FIRST_EA_ACTION_PLAN_UNVERIFIED`.

**Nova ACT-000002-000027-010, F005:** executor CODEX CLI local no próprio Gerador; ajustar gate e testes para exigir matriz da primeira EA de nova constituição, mas permitir validação SCIV posterior de bootstrap **historicamente concluído e comprovado**, sem considerar a ausência da matriz histórica como `PASS` de validador. Não relaxar verificações de CREATE/plan/request/namespace/EA atual, Rota A nova, Rota B, SCIV nem PEP. Roteiro versionado: `handoffs/codex/EA-000002-000027-F005-LEGACY-MATRIX-GATE.md`. ACT-006/007 continuam VERIFIED; F005 e F006 não promovidas. Fonte: `thiagoba2004/instituicoes-bancarias/auditorias/EA-000022-000003-codex-f002-f004-2026-10-11.md`.
