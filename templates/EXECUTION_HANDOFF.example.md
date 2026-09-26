# EXECUTION HANDOFF — TEMPLATE

**project_code:** `{{PROJECT_CODE}}`  
**project_name:** `{{PROJECT_NAME}}`  
**strategy_code:** `{{STRATEGY_CODE}}`  
**strategy_name:** `{{STRATEGY_NAME}}`  
**phase:** `{{PHASE_CODE}} — {{PHASE_NAME}}`  
**source_context:** `{{SOURCE_CONTEXT}}`  
**target_executor:** `{{TARGET_EXECUTOR}}`  
**created_at:** `{{DATE}}`

## Objetivo da execução

{{OBJECTIVE}}

## Decisões já tomadas

- {{DECISION_1}}

## Fontes indispensáveis

- {{SOURCE_1}}

## Restrições e sensibilidade

- classificação aplicável: `{{SENSITIVITY}}`;
- transferir somente o contexto necessário;
- preservar as proibições da política de informação.

## Fonte/destino canônico

`{{CANONICAL_DESTINATION}}`

## Gate de conclusão

{{COMPLETION_GATE}}

## Retorno obrigatório

1. validar o resultado;
2. persistir na fonte canônica;
3. atualizar estado e logs;
4. registrar divergências ou limitações;
5. não presumir que o executor de destino compartilha a memória do contexto de origem.
