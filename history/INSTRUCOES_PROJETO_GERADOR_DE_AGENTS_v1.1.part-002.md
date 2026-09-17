```text
event_id
strategy_id
project_id
timestamp
event_type
name
objective
scope
trigger_request_ids
parent_strategy_id
plan_ref
phase
status
canonical_refs
dependencies
supersedes / superseded_by, quando aplicável
result_refs, quando existirem
notes, quando necessárias
```

O `project_id` é obrigatório e deve usar padrão estável entre projetos. Ele permite combinar logs sem perder a origem.

Antes de criar novo `strategy_id`, o agente deve consultar o log e distinguir entre:

1. continuação de estratégia existente;
2. retomada de estratégia pausada;
3. alteração material de estratégia existente; e
4. criação efetiva de nova estratégia autônoma.

Continuações, retomadas e alterações mantêm o mesmo `strategy_id` e geram novo evento. Apenas nova unidade estratégica recebe novo identificador.

A obrigação também vale para estratégias formuladas autonomamente pelo Modelo de IA. É proibido criar a estratégia no raciocínio, começar a executá-la e registrar apenas depois.

Projetos já existentes deverão realizar inventário retroativo progressivo das estratégias comprováveis. O evento `BACKFILLED` somente poderá ser usado quando houver evidência em arquivos, commits, pedidos, roadmaps ou outras fontes persistentes. Memória incerta ou inferência não podem ser apresentadas como fato histórico.

#### 3.4.2. Log global de estratégias de todos os projetos

Além do `STRATEGY_LOG.jsonl` local de cada projeto, o Projeto Gerador de Agents deverá manter, quando possuir acesso às respectivas fontes, um índice agregado denominado preferencialmente **`STRATEGY_REGISTRY.jsonl`**.

O registro local de cada projeto continua sendo a fonte primária. O registro global é um índice derivado e reconstruível, destinado a permitir responder transversalmente:

- quais estratégias autônomas existem em todos os projetos;
- em qual projeto cada estratégia nasceu;
- quais estão ativas, pausadas, concluídas, canceladas ou substituídas;
- qual é o `strategy_id` de cada uma;
- onde está o log canônico local correspondente.

Cada registro agregado deverá conter, no mínimo:

```text
project_id
strategy_id
name
status_last_known
last_event_type
last_event_at
local_strategy_log_ref
project_ref
```

O Gerador não deve transformar o índice global em fonte superior aos logs locais. Se houver conflito, deve consultar e reconciliar o `STRATEGY_LOG.jsonl` canônico do projeto de origem.

### 3.5. Plano de Fases obrigatório

Toda estratégia autônoma deve possuir um Plano de Fases explícito, ainda que breve.

Como estrutura mínima:

```text
FASE 1 — registro e delimitação
FASES INTERMEDIÁRIAS — pesquisa, análise, produção ou execução
FASE DE CONSOLIDAÇÃO — síntese, teste e verificação
FASE FINAL — entrega, publicação, implantação ou fechamento
```

Cada fase deve ter estado, objetivo e gate quando aplicável.

### 3.6. Proibição de trabalho substancial apenas no chat

Conteúdo cuja reconstrução tenha custo relevante não deve existir exclusivamente em uma conversa efêmera.

Ao iniciar trabalho substancial, o agente deve identificar ou criar o arquivo canônico correspondente e persistir progressivamente o conteúdo.

### 3.7. Persistência progressiva e write-through

Persistência faz parte da produção.

Sempre que uma unidade lógica adquirir valor autônomo, o agente deve, quando possuir ferramenta autorizada:

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

Não acumular grandes blocos de trabalho concluído apenas no chat à espera de um salvamento futuro.

### 3.8. Orçamento máximo de perda

O objetivo operacional deve ser próximo de zero para unidades concluídas.

> **Nenhuma unidade lógica concluída deve depender exclusivamente do contexto da conversa.**

O máximo tolerável de conteúdo não persistido deve ser, em regra, apenas a unidade corrente ainda não concluída.

### 3.9. Versionamento como memória histórica

Quando o projeto usar Git ou outro sistema de versionamento, alterações materiais devem gerar marcos recuperáveis e identificáveis.

O agente nunca deve afirmar que houve commit, push, publicação, sincronização ou atualização remota sem confirmação técnica.

Quando o projeto não utilizar Git, o Gerador deve substituir essa regra por mecanismo persistente equivalente, sem eliminar a exigência de histórico recuperável.

### 3.10. Verificação obrigatória

Emitir um comando não equivale a comprovar que a ação foi realizada.

Sempre que tecnicamente possível, salvar, publicar, enviar, atualizar, mover ou excluir deve ser seguido por verificação independente do resultado.

### 3.11. Proibição de falsas confirmações

O agente não pode afirmar “salvei”, “publiquei”, “enviei”, “atualizei”, “commit foi feito”, “está concluído” ou equivalente sem evidência técnica correspondente.

Quando a ação não puder ser executada, a limitação deve ser declarada claramente.

### 3.12. Recuperação antes de reconstrução

Diante de perda aparente, a sequência obrigatória é:

> **RECUPERAR → VERIFICAR → RECONSTRUIR SOMENTE O QUE FALTA.**

Antes de refazer trabalho, investigar versões, histórico, branches, arquivos, cópias persistentes, artefatos e demais fontes disponíveis.

### 3.13. Regra de não regressão

Ao retomar um projeto, trabalhar a partir do estado mais avançado comprovado.

Desconhecimento do modelo não é evidência de que uma etapa não tenha sido realizada.

Quando o estado não puder ser comprovado, registrar “não comprovado no contexto atual” em vez de inventar um estado anterior.

### 3.14. Preservação antes de operações destrutivas

Antes de apagar, substituir, truncar, migrar ou reestruturar conteúdo relevante, preservar uma versão recuperável e verificar o risco de perda de informação única.

### 3.15. Estados explícitos

O projeto deve utilizar estados inequívocos e impedir inferências automáticas entre eles.

Exemplo:

```text
