# AGENTS.md — GERADOR DE AGENTS

**project_id:** `GDA`  
**generated_from_kernel:** `1.2`  
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
7. `DECISIONS.md` para decisões arquiteturais/metodológicas;
8. `CHANGELOG.md` para evolução do kernel e do Gerador;
9. histórico Git comprovado;
10. somente depois, memória ou contexto conversacional.

## 4. Estratégias

Toda Estratégia Autônoma deve possuir `strategy_id` estável e evento no `STRATEGY_LOG.jsonl` antes de qualquer execução substantiva.

Padrão de identificação deste projeto:

```text
STRAT-GDA-AAAAMMDD-NNN
```

O log é append-only. Continuação, retomada ou alteração material mantém o mesmo `strategy_id`; somente nova estratégia autônoma recebe novo identificador.

O `STRATEGY_REGISTRY.jsonl` é índice agregado e reconstruível. Nunca prevalece sobre o `STRATEGY_LOG.jsonl` local do projeto de origem.

## 5. Plano de Fases

Nenhuma estratégia autônoma pode existir sem Plano de Fases explícito. O plano deve possuir, no mínimo:

- registro e delimitação;
- fases intermediárias de trabalho;
- consolidação/verificação;
- fase final.

Cada fase deve registrar estado, objetivo e gate quando aplicável.

## 6. Persistência e Git

Trabalho substancial deve ser persistido progressivamente. Sempre que uma unidade lógica se tornar autônoma:

```text
PRODUZIR → SALVAR → VERIFICAR → ATUALIZAR ESTADO → CONTINUAR
```

Git é a memória histórica preferencial deste projeto. Não afirmar commit, atualização remota, publicação ou implantação sem confirmação técnica.

## 7. Arquitetura esperada

```text
AGENTS.md
AGENTS_KERNEL.md
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
```

## 8. Templates

`templates/` deve manter modelos reutilizáveis, pelo menos, para:

- `REQUEST_LOG.jsonl`;
- `STRATEGY_LOG.jsonl`;
- `PROJECT_STATE.json`;
- `ROADMAP.md`;
- `AGENTS.md`.

## 9. Módulos

Cada módulo em `modules/` deve declarar:

- quando se aplica;
- arquivos canônicos exigidos;
- estados específicos;
- critérios de conclusão;
- procedimentos de verificação;
- riscos próprios do domínio.

## 10. Perfis

Cada perfil em `profiles/` deve registrar, quando aplicável:

- `project_id`;
- nome e finalidade;
- repositório/fonte de persistência;
- versão do kernel utilizada;
- módulos ativados;
- arquivos canônicos;
- riscos e restrições;
- estado de migração/implantação.

## 11. Projeto novo

Para projeto novo: identificar finalidade, persistência, versionamento, formatos, ferramentas, riscos, `project_id`, módulos aplicáveis e arquivos auxiliares; depois gerar e verificar o `AGENTS.md` e registrar a origem do kernel.

## 12. Projeto existente

Nunca substituir cegamente o `AGENTS.md` existente. Primeiro ler Agents, estado e planejamento; inventariar estratégias comprováveis; comparar com o kernel; preservar regras específicas válidas; identificar lacunas/conflitos; produzir plano de migração; preservar versão anterior; atualizar; verificar; versionar.

## 13. Não regressão e recuperação

Diante de perda aparente:

> **RECUPERAR → VERIFICAR → RECONSTRUIR SOMENTE O QUE FALTA.**

Retomar sempre do estado mais avançado comprovado.

## 14. Fechamento

Antes de declarar uma operação substancial concluída, confirmar persistência, versionamento remoto, estado do projeto, referências produzidas e próximo passo lógico.

## 15. Regra máxima

> **Nunca obrigar o usuário a pagar novamente, com tempo, energia ou recursos, por falha de memória, persistência, continuidade, planejamento ou verificação do Modelo de IA.**
