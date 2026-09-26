# Módulo: Execution Environments v2

**module_id:** `execution-environments`  
**architecture_version:** `2.2`

## Finalidade

Separar identidade, superfície de acesso, executor, contexto/memória, fontes de conhecimento e persistência/publicação.

## Planos

### Plano G — Identidade/Governança
- `G0_GOVERNANCA_GLOBAL`
- `G1_PROJETO_GOVERNANCA` → `PRJ-NNNNNN`
- `G2_ESTRATEGIA_AUTONOMA` → `EA-PPPPPP-EEEEEE`
- `G3_FASE` → `F-PPPPPP-EEEEEE-FFF`

### Plano A — Superfície de acesso
- `A1_ANDROID_MOBILE`
- `A2_WEB`
- `A3_DESKTOP`

Superfície não define capacidade exclusiva.

### Plano E — Executor
- `E1_CHAT`: diálogo, decisão, pesquisa/tarefa delimitada;
- `E2_WORK`: execução substancial multi-etapas;
- `E3_CODEX`: engenharia de software e repositório.

### Plano B — Vínculo com Projeto ChatGPT
- `B0_NO_CHATGPT_PROJECT_BINDING`
- `B1_CHATGPT_PROJECT_BOUND`

### Plano C — Contexto/Memória
- `C1_CHAT_AVULSO`
- `C2_CHATGPT_PROJECT_DEFAULT_MEMORY`
- `C3_CHATGPT_PROJECT_ONLY_MEMORY`
- `C4_TEMPORARY_CHAT`

**Regra:** primeiro declarar `B0_NO_CHATGPT_PROJECT_BINDING` ou `B1_CHATGPT_PROJECT_BOUND`. Somente em `B1` declarar `C2` ou `C3`. O módulo não pode inferir vínculo nem modo de memória.

**Restrição:** Work não está disponível dentro de `C3`.

### Plano K — Fontes de Conhecimento
- `K1_PROJECT_ATTACHED_SOURCES`: Core Context curado;
- `K2_CHATGPT_LIBRARY`: descoberta/espelho operacional;
- `K3_GIT_REPOSITORY`: fonte versionada e estado canônico quando designado;
- `K4_CONNECTED_CLOUD_SOURCE`: Drive e fontes em nuvem equivalentes;
- `K5_LOCAL_FILESYSTEM`: working copy/cache, nunca única fonte necessária à continuidade;
- `K6_WEB_EXTERNAL`: evidência e descoberta externas.

Para Plus, o limite vigente de Projeto é 25 arquivos, com até 10 uploads simultâneos. O limite é teto técnico, não objetivo de preenchimento.

### Plano P — Persistência/Publicação
- `P0_COFRE_EXTERNO`
- `P1_GIT_PRIVADO`
- `P2_GIT_PUBLICO_REPOSITORIO`
- `P3_PUBLICO_SITE`

## Regras universais

1. Projeto ChatGPT não é Projeto de Governança.
2. Memória não é verdade; persistência não é validação.
3. Memória exclusiva é fronteira contextual, não armazenamento local.
4. Isolar memória não implica isolar o acervo documental.
5. Fontes anexadas formam Core Context, não repositório integral.
6. GitHub é fonte versionada quando o Projeto assim o define.
7. Biblioteca e nuvens conectadas são fontes recuperáveis, não substitutos automáticos da fonte canônica.
8. Filesystem local é working copy e não pode ser a única cópia necessária à continuidade.
9. Work/Codex que não herdem o contexto devem receber handoff explícito.
10. Handoff transfere apenas contexto necessário e classificado.
11. Ambiente ou fonte indisponível não altera `PRJ/EA/F`.
12. Trabalho substancial termina com persistência verificável.

## Core Context

Priorizar:
- manifesto/escopo;
- AGENTS/governança;
- estado atual;
- roadmap/plano vigente;
- backlog/pauta quando material;
- índice/mapa documental;
- decisões arquiteturais vigentes.

Qualidade e relevância prevalecem sobre quantidade.

## Handoff

Quando o executor preferencial não estiver disponível no contexto atual:

```text
estado canônico verificado
→ pacote mínimo de contexto
→ Work/Codex
→ resultado
→ validação
→ persistência canônica
→ atualização de estado
```

Campos mínimos do pacote:
- projeto;
- estratégia;
- fase;
- objetivo;
- decisões;
- fontes indispensáveis;
- restrições de sensibilidade;
- destino canônico;
- gate de conclusão.

## Compatibilidade v1

- `X1_CHAT` → `E1_CHAT`
- `X2_WORK` → `E2_WORK`
- `X3_CHATGPT_PROJECT` → `C2` ou `C3`
- `X4_LIBRARY` → `K2_CHATGPT_LIBRARY`
- `X5_CODEX` → `E3_CODEX`
- `X6_APPS_CONNECTORS` → `K4` ou sistema externo autorizado

Novos perfis devem usar schema v2.
