# AGENTS.md — {{PROJECT_NAME}}

**project_id:** `{{PROJECT_ID}}`  
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

Toda Estratégia Autônoma deve possuir `strategy_id` estável e evento persistido em `STRATEGY_LOG.jsonl` antes da execução substantiva.

Padrão:

```text
STRAT-{{PROJECT_ID}}-AAAAMMDD-NNN
```

Continuações e retomadas mantêm o mesmo identificador. Apenas nova unidade estratégica recebe novo `strategy_id`.

## 5. Plano de Fases

Toda Estratégia Autônoma deve possuir Plano de Fases explícito, com estado, objetivo e gate quando aplicável.

Estrutura mínima:

- Fase 1 — registro e delimitação;
- fases intermediárias — pesquisa, análise, produção ou execução;
- fase de consolidação — síntese, teste e verificação;
- fase final — entrega, publicação, implantação ou fechamento.

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
