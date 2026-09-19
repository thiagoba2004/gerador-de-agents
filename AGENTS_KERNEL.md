# AGENTS KERNEL — NÚCLEO UNIVERSAL

**kernel_version:** 1.4  
**project_code de origem:** `PRJ-000002`  
**project_alias de origem:** `GDA`  
**data:** 19/09/2026

## 1. Finalidade

Este kernel reúne regras universais de governança para projetos assistidos por Modelos de IA. Ele deve ser herdado por `AGENTS.md` de outros projetos sem importar automaticamente regras específicas de domínio.

## 2. Ordem obrigatória para novos pedidos

Ao receber qualquer novo pedido, correção, complemento, pergunta, determinação, interrupção ou mudança de instrução:

1. registrar primeiro o pedido de forma persistente, sequencial e rastreável;
2. confirmar tecnicamente o registro;
3. informar ao usuário: **“Pedido registrado.”**;
4. informar que irá ler o prompt, analisar e tomar as providências necessárias;
5. somente então iniciar leitura substantiva, análise, ferramentas ou execução.

É proibido afirmar que o pedido foi registrado antes da confirmação técnica.

## 3. Registro de pedidos

O mecanismo preferencial é `REQUEST_LOG.jsonl` ou equivalente estruturado. Cada pedido deve registrar, quando aplicável: identificador, timestamp, texto integral ou representação fiel, escopo, estratégia relacionada, estado, ação solicitada e referências de resultado.

O registro de pedidos é a fonte principal para responder “qual foi meu último pedido?”, “onde paramos?” e “o que ficou pendente?”.

## 4. Fonte da verdade

Hierarquia padrão:

1. arquivos canônicos persistentes e versionados;
2. arquivos estruturados de estado;
3. histórico de versionamento e commits comprovados;
4. cópias persistentes verificáveis;
5. somente depois, memória, contexto de conversa ou resumo do Modelo de IA.

Memória nunca prevalece sobre evidência documental mais recente.

## 5. Estratégia antes da execução

Nenhuma tarefa substantiva deve existir como atividade órfã. Antes de executar, identificar estratégia, objetivo, plano, fase, gate, dependências, tarefa atual, resultado esperado e próximo passo lógico.

Toda Estratégia Autônoma deve possuir, antes da execução substantiva:

```text
strategy_code
strategy_name
```

O `strategy_code` é o identificador canônico, numérico, hierárquico e independente da denominação. Sua gramática universal é:

```text
EA-PPPPPP-EEEEEE
```

onde `PPPPPP` é a sequência do Projeto e `EEEEEE` é a sequência monotônica da Estratégia dentro do Projeto.

Para Estratégias novas, `strategy_id` deve ser igual a `strategy_code`. Estratégias históricas com identificadores legados preservam o identificador antigo em `legacy_strategy_id` ou mapeamento equivalente; o histórico append-only não deve ser reescrito.

O `strategy_name` é a denominação humana inequívoca da Estratégia Autônoma.

A alocação e a migração devem obedecer a `IDENTIFICATION_STANDARD.md`.

O evento correspondente deve ser persistido em `STRATEGY_LOG.jsonl` antes da execução substantiva.

Regra:

> **ESTRATÉGIA AUTÔNOMA NOVA = `strategy_code` NOVO + `strategy_id = strategy_code` + EVENTO `CREATED` PERSISTIDO ANTES DA EXECUÇÃO.**

Continuações, retomadas e alterações mantêm o mesmo `strategy_code` e geram novos eventos. Eventos mínimos: `CREATED`, `UPDATED`, `PAUSED`, `RESUMED`, `SUPERSEDED`, `CONCLUDED`, `CANCELLED`, `BACKFILLED`.

Backfill somente pode ser feito com evidência persistente suficiente.

## 6. Identificação de projeto

Cada projeto deve possuir identificação canônica composta, no mínimo, por:

```text
project_code
project_sequence
project_name
project_alias
```

O `project_code` é numérico, globalmente único, estável, imutável e independente da denominação:

```text
PRJ-NNNNNN
```

`NNNNNN` é uma sequência global de seis algarismos registrada em `PROJECT_REGISTRY.jsonl`.

O `project_name` é a denominação humana estável do Projeto. O `project_alias` é opcional e exclusivamente mnemônico; siglas como `CEM` e `GDA` não constituem identidade canônica e nunca participam do cálculo dos códigos descendentes.

Quando existir `project_id` legado, slug técnico ou código antigo, ele deve ser preservado para compatibilidade histórica, mas não substitui o `project_code`.

Códigos nunca são reutilizados nem renumerados. Renomear o Projeto, mover o repositório, arquivar ou cancelar não altera o código.

A metodologia completa de alocação, hierarquia e migração é `IDENTIFICATION_STANDARD.md`.

## 7. Plano de Fases obrigatório

Toda Estratégia Autônoma deve possuir Plano de Fases explícito, integralmente numerado e persistente.

Cada fase deve possuir obrigatoriamente:

```text
phase_number
phase_code
phase_name
phase_total
```

Convenção:

```text
phase_number = inteiro sequencial iniciado em 1
phase_code   = F-PPPPPP-EEEEEE-FFF
phase_name   = denominação humana inequívoca
phase_total  = número total de fases do plano vigente
```

O código da Fase herda numericamente Projeto e Estratégia. A forma textual canônica é:

```text
FASE 01/05 [F-000001-000014-001] — Registro e delimitação
FASE 02/05 [F-000001-000014-002] — Pesquisa e análise
...
FASE 05/05 [F-000001-000014-005] — Verificação e fechamento
```

Não é permitido usar `FASE FINAL`, `FASE DE CONSOLIDAÇÃO` ou expressão equivalente sem número. A função da fase pode constar na denominação, mas toda fase deve permanecer matematicamente posicionada no plano.

Cada fase deve possuir estado, objetivo e gate quando aplicável. Se o plano for alterado materialmente, `phase_total` e a numeração vigente devem ser atualizados sem reescrever o histórico já persistido.

Estratégias legadas permanecem historicamente preservadas, mas, ao serem retomadas, seu Plano de Fases vigente deve ser normalizado para este esquema **antes** de nova execução substantiva ou de uma resposta que pretenda informar a fase atual com precisão. É proibido inventar retrospectivamente números de fase sem apoio em evidência persistente.

## 7.1. Padrão obrigatório de resposta de continuidade

Quando o usuário perguntar **“Onde paramos?”**, **“Qual a Estratégia Autônoma em curso?”**, **“Qual a Fase dessa Estratégia Autônoma?”**, **“Qual o Projeto?”** ou equivalente, a resposta deve ser determinística e conter, nesta ordem:

```text
PROJETO: <PROJECT_CODE> — <PROJECT_NAME>
ALIAS: <PROJECT_ALIAS, quando existir>
ESTRATÉGIA AUTÔNOMA: <STRATEGY_CODE> — <STRATEGY_NAME>
FASE: <PHASE_NUMBER>/<PHASE_TOTAL> [<PHASE_CODE>] — <PHASE_NAME>
ESTADO: <estado comprovado>
ONDE PARAMOS: <ponto exato comprovado>
PRÓXIMO PASSO LÓGICO: <próximo passo comprovado pelo plano>
```

Identificador canônico e denominação são obrigatórios para Projeto e Estratégia Autônoma. Alias é apenas mnemônico. Número, total, código hierárquico e denominação são obrigatórios para a Fase.

A resposta deve ser reconstruída prioritariamente de `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl`, `PROJECT_STATE.json`, Plano de Fases e arquivos canônicos. Memória conversacional só pode ser usada subsidiariamente.

---

## 8. Persistência progressiva

Trabalho substancial não deve existir apenas no chat. Ao iniciar conteúdo de reconstrução custosa, identificar ou criar o arquivo canônico correspondente e persistir progressivamente.

Fluxo preferencial:

```text
PRODUZIR
↓
SALVAR
↓
VERIFICAR
↓
ATUALIZAR ESTADO
↓
CONTINUAR
```

O máximo tolerável de conteúdo não persistido deve ser, em regra, somente a unidade lógica corrente ainda não concluída.

## 9. Versionamento como memória histórica

Quando houver Git ou equivalente, alterações materiais devem gerar marcos recuperáveis. Nunca afirmar que houve commit, push, publicação, sincronização ou atualização remota sem confirmação técnica.

Quando não houver Git, utilizar mecanismo persistente equivalente.

## 10. Verificação e honestidade operacional

Emitir uma ação não equivale a comprovar seu resultado. Sempre que tecnicamente possível, salvar, publicar, enviar, atualizar, mover ou excluir deve ser seguido de verificação independente.

É proibido confirmar como concluído aquilo que não foi tecnicamente comprovado.

## 11. Recuperação antes de reconstrução

Diante de perda aparente:

> **RECUPERAR → VERIFICAR → RECONSTRUIR SOMENTE O QUE FALTA.**

Antes de refazer trabalho, investigar arquivos, histórico, branches, commits, cópias, artefatos e demais fontes persistentes.

## 12. Não regressão

Retomar sempre do estado mais avançado comprovado. Desconhecimento do modelo não prova que uma etapa não foi realizada. Quando não houver comprovação, registrar “não comprovado no contexto atual” em vez de inventar estado anterior.

## 13. Preservação antes de operações destrutivas

Antes de apagar, substituir, truncar, migrar ou reestruturar conteúdo relevante, preservar versão recuperável e verificar risco de perda de informação única.

## 14. Estados explícitos

Projetos devem distinguir estados como `NÃO INICIADO`, `EM PREPARAÇÃO`, `EM EXECUÇÃO`, `EM REVISÃO`, `REVISADO`, `PRONTO PARA ENTREGA`, `CONCLUÍDO`, `PUBLICADO/IMPLANTADO` e `ARQUIVADO` quando aplicáveis.

“Produzido no chat”, “salvo”, “versionado”, “enviado ao remoto” e “publicado” são estados diferentes.

## 15. Continuidade entre conversas, agentes e modelos

Os arquivos persistentes devem permitir reconstruir objetivo, arquitetura, estratégia vigente, fases, estado atual, último marco concluído, pendências, pedido mais recente e próximo passo lógico sem depender do contexto do chat.

## 16. Autonomia com verificabilidade

O agente deve executar diretamente o trabalho mecânico permitido pelas ferramentas disponíveis, sem transferir desnecessariamente tarefas ao usuário. Autonomia nunca autoriza opacidade, improvisação estratégica ou afirmações não verificadas.

## 17. Checkpoints

Em trabalhos prolongados, informar periodicamente o avanço e o estado real de preservação do trabalho.

## 18. Fechamento obrigatório

Antes de declarar trabalho substancial concluído, verificar conforme aplicável:

- arquivo canônico atualizado;
- estado atualizado;
- persistência confirmada;
- versionamento realizado;
- remoto confirmado;
- publicação/implantação confirmada;
- cópia adicional de marco crítico, quando necessária;
- próximo passo lógico registrado.

## 19. Regra máxima

> **Nunca obrigar o usuário a pagar novamente, com tempo, energia ou recursos, por falha de memória, persistência, continuidade, planejamento ou verificação do Modelo de IA.**
