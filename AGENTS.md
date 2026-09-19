# AGENTS.md — GERADOR DE AGENTS

**project_id:** `GDA`  
**project_code:** `GDA`  
**project_name:** `Gerador de Agents`  
**generated_from_kernel:** `1.3`  
**repository:** `thiagoba2004/gerador-de-agents`

## 1. Missão do projeto

Este repositório mantém o Gerador de Agents: infraestrutura para criar, auditar, adaptar, atualizar e versionar `AGENTS.md` de outros projetos, preservando continuidade, persistência, estratégia, planejamento, verificabilidade e recuperação.

O Gerador não deve copiar cegamente regras de um projeto de origem. Deve separar:

1. **núcleo universal** — `AGENTS_KERNEL.md`;
2. **perfil do projeto** — `profiles/`;
3. **módulos especializados** — `modules/`.

## 2. Regra de entrada de qualquer pedido

Todo novo pedido deve seguir obrigatoriamente esta ordem:

```text
REGISTRAR EM REQUEST_LOG.jsonl
↓
CONFIRMAR TECNICAMENTE O REGISTRO
↓
INFORMAR “PEDIDO REGISTRADO.”
↓
INFORMAR QUE IRÁ LER O PROMPT, ANALISAR E TOMAR AS PROVIDÊNCIAS
↓
EXECUTAR
```

Nenhum pedido deve ser tratado apenas no chat quando o repositório estiver acessível.

## 3. Fonte da verdade deste projeto

Ordem de precedência:

1. `AGENTS_KERNEL.md` para regras universais;
2. `AGENTS.md` para regras específicas deste repositório;
3. `REQUEST_LOG.jsonl` para sequência de pedidos;
4. `STRATEGY_LOG.jsonl` para histórico de estratégias;
5. `PROJECT_STATE.json` para fotografia do estado corrente;
6. `ROADMAP.md` para Plano de Fases;
7. `GERADOR_WORKFLOW.md` para o procedimento operacional;
8. `MODULE_SELECTION.md` para decisão de módulos;
9. `DECISIONS.md` para decisões arquiteturais/metodológicas;
10. `CHANGELOG.md` para evolução do kernel e do Gerador;
11. histórico Git comprovado;
12. somente depois, memória ou contexto conversacional.

## 4. Estratégias

Toda Estratégia Autônoma deve possuir `strategy_id` e `strategy_name` estáveis e evento no `STRATEGY_LOG.jsonl` antes de qualquer execução substantiva.

O código da Estratégia Autônoma deve usar o código canônico do Projeto:

Padrão de identificação deste projeto:

```text
STRAT-<PROJECT_CODE>-AAAAMMDD-NNN
```

O log é append-only. Continuação, retomada ou alteração material mantém o mesmo `strategy_id`; somente nova estratégia autônoma recebe novo identificador.

O `STRATEGY_REGISTRY.jsonl` é índice agregado e reconstruível. Nunca prevalece sobre o `STRATEGY_LOG.jsonl` local do projeto de origem. Quando o Gerador tiver acesso a estratégias comprovadas de projetos auditados ou gerados, o índice deverá ser atualizado sem inventar estados ausentes.

## 5. Plano de Fases

Nenhuma Estratégia Autônoma pode existir sem Plano de Fases explícito, persistente e integralmente numerado.

Cada fase deve registrar obrigatoriamente `phase_number`, `phase_code`, `phase_name` e `phase_total`, além de estado, objetivo e gate quando aplicável.

Padrão textual:

```text
FASE 01/05 (F01) — Registro e delimitação
FASE 02/05 (F02) — ...
FASE 05/05 (F05) — Verificação e fechamento
```

É proibido manter fases sem número, inclusive rótulos como “FASE FINAL” isoladamente.

## 5.1. Padrão de resposta para recuperação de estado

Quando o usuário perguntar **“Onde paramos? Qual a Estratégia Autônoma em curso? Qual a Fase dessa Estratégia Autônoma? E qual o Projeto?”** ou formulação equivalente, responder obrigatoriamente:

```text
PROJETO: <PROJECT_CODE> — <PROJECT_NAME>
ESTRATÉGIA AUTÔNOMA: <STRATEGY_ID> — <STRATEGY_NAME>
FASE: <PHASE_NUMBER>/<PHASE_TOTAL> (<PHASE_CODE>) — <PHASE_NAME>
ESTADO: <estado comprovado>
ONDE PARAMOS: <ponto exato comprovado>
PRÓXIMO PASSO LÓGICO: <próximo passo comprovado>
```

A recuperação deve usar fontes persistentes, não memória isolada.

## 6. Persistência e Git

Trabalho substancial deve ser persistido progressivamente. Sempre que uma unidade lógica se tornar autônoma:

```text
PRODUZIR → SALVAR → VERIFICAR → ATUALIZAR ESTADO → CONTINUAR
```

Git é a memória histórica preferencial deste projeto. Não afirmar commit, atualização remota, publicação ou implantação sem confirmação técnica.

## 7. Arquitetura vigente

```text
README.md
AGENTS.md
AGENTS_KERNEL.md
GERADOR_WORKFLOW.md
MODULE_SELECTION.md
REQUEST_LOG.jsonl
STRATEGY_LOG.jsonl
STRATEGY_REGISTRY.jsonl
PROJECT_STATE.json
ROADMAP.md
DECISIONS.md
CHANGELOG.md
modules/
profiles/
templates/
audits/
history/
```

`README.md` é o ponto de entrada para novos agentes/modelos. `audits/` registra auditorias e testes não destrutivos. `history/` preserva proveniência e versões históricas do próprio Gerador.

## 8. Templates

`templates/` deve manter modelos reutilizáveis, conforme aplicável, para:

- `REQUEST_LOG.jsonl`;
- `STRATEGY_LOG.jsonl`;
- `PROJECT_STATE.json`;
- `ROADMAP.md`;
- `AGENTS.md`;
- relatório de auditoria/migração;
- perfil estruturado do projeto.

O índice atualizado de templates fica em `templates/README.md`.

## 9. Módulos

Cada módulo em `modules/` deve declarar:

- quando se aplica;
- arquivos canônicos exigidos;
- estados específicos;
- critérios de conclusão;
- procedimentos de verificação;
- riscos próprios do domínio.

A ativação deve seguir `MODULE_SELECTION.md`; não ativar módulo apenas por possibilidade abstrata.

### 9.1. Propagação obrigatória de regras modulares

Quando um módulo estiver `ATIVADO`, as regras marcadas como obrigatórias nesse módulo devem ser materializadas no `AGENTS.md` gerado ou migrado para o projeto-alvo, e não apenas citadas genericamente.

Para o módulo `publication`, quando houver publicação de conteúdo textual/editorial, deve ser propagada a regra de triplicidade documental:

```text
Markdown (.md) = fonte textual canônica
HTML (.html) = artefato de publicação
JSON (.json) = representação estruturada/metadados interoperáveis
```

Cada texto editorial/publicável deve possuir os três artefatos coordenados, salvo exceção expressa, persistente e versionada no projeto-alvo.

## 10. Perfis

Cada perfil em `profiles/` deve registrar, quando aplicável:

- `project_id`;
- nome e finalidade;
- repositório/fonte de persistência;
- versão do kernel utilizada ou auditada;
- módulos ativados, não aplicáveis ou pendentes de evidência;
- arquivos canônicos;
- riscos e restrições;
- estado de migração/implantação;
- referência ao log local de estratégias.

## 11. Projeto novo

Para projeto novo, seguir a **Rota A** de `GERADOR_WORKFLOW.md`: identificar finalidade, persistência, versionamento, formatos, ferramentas, riscos, `project_id`, módulos aplicáveis e arquivos auxiliares; depois gerar e verificar o `AGENTS.md` e registrar a origem do kernel.

## 12. Projeto existente

Para projeto existente, seguir a **Rota B** de `GERADOR_WORKFLOW.md`. Nunca substituir cegamente o `AGENTS.md` existente. Primeiro ler Agents, estado e planejamento; inventariar estratégias comprováveis; comparar com o kernel; preservar regras específicas válidas; identificar lacunas/conflitos; produzir plano de migração; preservar versão anterior; atualizar; verificar; versionar.

### 12.1. Auditoria não é migração

Quando o Gerador estiver realizando auditoria não destrutiva, o projeto-alvo deve permanecer inalterado. O pedido, a estratégia da auditoria, o perfil e o relatório são persistidos no repositório do Gerador. A escrita no projeto-alvo somente ocorre quando houver execução de migração/implantação autorizada e governada pelas regras locais daquele projeto.

## 13. Não regressão e recuperação

Diante de perda aparente:

> **RECUPERAR → VERIFICAR → RECONSTRUIR SOMENTE O QUE FALTA.**

Retomar sempre do estado mais avançado comprovado.

## 14. Histórico e proveniência

Versões históricas das instruções do próprio Gerador devem permanecer recuperáveis em `history/` com proveniência e verificação de integridade. Material histórico não prevalece sobre o kernel vigente em caso de conflito normativo.

## 15. Fechamento

Antes de declarar uma operação substancial concluída, confirmar persistência, versionamento remoto, estado do projeto, referências produzidas, sincronização do registro agregado quando aplicável e próximo passo lógico.

## 16. Regra máxima

> **Nunca obrigar o usuário a pagar novamente, com tempo, energia ou recursos, por falha de memória, persistência, continuidade, planejamento ou verificação do Modelo de IA.**
