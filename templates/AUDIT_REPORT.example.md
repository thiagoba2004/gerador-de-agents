# RELATÓRIO DE AUDITORIA / MIGRAÇÃO DE AGENTS

**project_id:** `{{PROJECT_ID}}`  
**projeto:** {{PROJECT_NAME}}  
**fonte/repositório:** {{PROJECT_REF}}  
**kernel de comparação:** `{{KERNEL_VERSION}}`  
**data:** {{DATE}}

## 1. Objetivo da auditoria

{{AUDIT_OBJECTIVE}}

## 2. Fontes examinadas

{{SOURCES_EXAMINED}}

## 3. Estado comprovado antes da migração

{{PRE_MIGRATION_STATE}}

## 4. Regras encontradas

| Regra / tema | Origem | Classificação | Estado | Observação |
|---|---|---|---|---|
| {{RULE}} | {{SOURCE}} | UNIVERSAL / ESPECÍFICA / MÓDULO / DUPLICADA / CONFLITANTE / OBSOLETA | {{STATUS}} | {{NOTE}} |

## 5. Lacunas em relação ao kernel

{{KERNEL_GAPS}}

## 6. Regras locais mais rigorosas que o kernel

{{STRICTER_LOCAL_RULES}}

## 7. Conflitos identificados

{{CONFLICTS}}

## 8. Módulos

| Módulo | Decisão | Evidência / justificativa |
|---|---|---|
| {{MODULE}} | ATIVADO / NÃO APLICÁVEL / PENDENTE DE EVIDÊNCIA | {{RATIONALE}} |

## 9. Estratégias autônomas

{{STRATEGY_INVENTORY}}

Indicar claramente quais estratégias são comprovadas por fonte persistente, quais exigem `BACKFILLED` e quais não podem ser reconstruídas com segurança.

## 10. Plano de migração

### Preservar
{{PRESERVE}}

### Acrescentar
{{ADD}}

### Reestruturar
{{RESTRUCTURE}}

### Remover
{{REMOVE_WITH_JUSTIFICATION}}

### Rollback
{{ROLLBACK_PLAN}}

## 11. Alterações efetivamente implantadas

{{IMPLEMENTED_CHANGES}}

## 12. Verificação pós-migração

{{POST_MIGRATION_VERIFICATION}}

## 13. Estado real

- texto proposto: {{PROPOSED_STATUS}}
- salvo: {{SAVED_STATUS}}
- versionado: {{VERSIONED_STATUS}}
- enviado ao remoto: {{REMOTE_STATUS}}
- implantado: {{DEPLOYED_STATUS}}
- publicado, quando aplicável: {{PUBLISHED_STATUS}}

## 14. Pendências

{{PENDING_ITEMS}}

## 15. Próximo passo lógico

{{NEXT_LOGICAL_STEP}}
