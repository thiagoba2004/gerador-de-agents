# AGENTS.md — {{PROJECT_NAME}}

**project_id:** `{{PROJECT_ID}}`  
**project_code:** `{{PROJECT_CODE}}`  
**project_name:** `{{PROJECT_NAME}}`  
**generated_from_kernel:** `{{KERNEL_VERSION}}`  
**repository/source:** `{{PROJECT_REF}}`  
**modules:** {{MODULE_LIST}}

## 1. Missão do projeto

{{PROJECT_PURPOSE}}

## 2. Ordem obrigatória para qualquer novo pedido

```text
REGISTRAR O PEDIDO
↓
CONFIRMAR TECNICAMENTE O REGISTRO
↓
INFORMAR “PEDIDO REGISTRADO.”
↓
INFORMAR QUE IRÁ LER O PROMPT, ANALISAR E TOMAR AS PROVIDÊNCIAS
↓
EXECUTAR
```

Todo pedido, correção, complemento, pergunta, interrupção ou mudança de instrução deve ser registrado em `REQUEST_LOG.jsonl` ou mecanismo persistente equivalente antes da execução substantiva.

## 3. Fonte da verdade

Hierarquia deste projeto:

1. {{CANONICAL_SOURCE_1}}
2. {{CANONICAL_SOURCE_2}}
3. `PROJECT_STATE.json` ou equivalente;
4. `STRATEGY_LOG.jsonl`;
5. histórico de versionamento comprovado;
6. somente depois, memória ou contexto conversacional.

## 4. Estratégias

Toda Estratégia Autônoma deve possuir `strategy_id` e `strategy_name` estáveis e evento persistido em `STRATEGY_LOG.jsonl` antes da execução substantiva.

Padrão:

```text
STRAT-{{PROJECT_CODE}}-AAAAMMDD-NNN
```

Continuações e retomadas mantêm o mesmo identificador. Apenas nova unidade estratégica recebe novo `strategy_id`.

## 5. Plano de Fases

Toda Estratégia Autônoma deve possuir Plano de Fases explícito, persistente e integralmente numerado.

Cada fase deve possuir `phase_number`, `phase_code`, `phase_name` e `phase_total`, além de estado, objetivo e gate quando aplicável.

Padrão obrigatório:

```text
FASE 01/{{PHASE_TOTAL}} (F01) — Registro e delimitação
FASE 02/{{PHASE_TOTAL}} (F02) — ...
FASE {{PHASE_TOTAL}}/{{PHASE_TOTAL}} (F{{PHASE_TOTAL_PADDED}}) — Verificação e fechamento
```

Não usar fases sem número, inclusive “FASE FINAL” isoladamente.

## 5.1. Padrão de resposta de continuidade

Quando o usuário perguntar **“Onde paramos? Qual a Estratégia Autônoma em curso? Qual a Fase dessa Estratégia Autônoma? E qual o Projeto?”** ou equivalente, responder:

```text
PROJETO: <PROJECT_CODE> — <PROJECT_NAME>
ESTRATÉGIA AUTÔNOMA: <STRATEGY_ID> — <STRATEGY_NAME>
FASE: <PHASE_NUMBER>/<PHASE_TOTAL> (<PHASE_CODE>) — <PHASE_NAME>
ESTADO: <estado comprovado>
ONDE PARAMOS: <ponto exato comprovado>
PRÓXIMO PASSO LÓGICO: <próximo passo comprovado>
```

## 6. Persistência progressiva

Trabalho substancial não deve permanecer somente no chat.

```text
PRODUZIR → SALVAR → VERIFICAR → ATUALIZAR ESTADO → CONTINUAR
```

## 7. Versionamento e verificabilidade

{{VERSIONING_RULES}}

Nunca afirmar salvamento, commit, push, publicação, envio ou implantação sem confirmação técnica correspondente.

## 8. Recuperação e não regressão

Diante de perda aparente:

> **RECUPERAR → VERIFICAR → RECONSTRUIR SOMENTE O QUE FALTA.**

Retomar sempre do estado mais avançado comprovado.

## 9. Regras específicas do projeto

{{PROJECT_SPECIFIC_RULES}}

## 10. Módulos ativados

{{MODULE_RULES_OR_REFERENCES}}

As regras obrigatórias dos módulos ativados devem ser materializadas nesta seção; não basta listar ou referenciar o nome do módulo.

Quando o módulo `publication` estiver ativado para conteúdo textual/editorial, incluir expressamente a obrigação de manter, para cada texto publicável, o trio coordenado `.md` + `.html` + `.json`, com Markdown como fonte textual canônica, HTML como publicação e JSON como representação estruturada, salvo exceção persistente e versionada.

## 11. Estados e critérios de conclusão

{{STATE_MODEL_AND_DONE_CRITERIA}}

## 12. Fechamento obrigatório

Antes de declarar trabalho substancial concluído, confirmar conforme aplicável:

- arquivo canônico atualizado;
- estado atualizado;
- persistência confirmada;
- versionamento confirmado;
- remoto confirmado;
- publicação/implantação confirmada;
- próximo passo lógico registrado.

## 13. Regra máxima

> **Nunca obrigar o usuário a pagar novamente, com tempo, energia ou recursos, por falha de memória, persistência, continuidade, planejamento ou verificação do Modelo de IA.**
