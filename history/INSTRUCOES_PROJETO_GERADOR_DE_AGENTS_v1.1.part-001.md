# INSTRUÇÕES CANÔNICAS — PROJETO GERADOR DE AGENTS

**Versão:** 1.1  
**Data:** 17/09/2026  
**Status:** CANÔNICO / BASE DO PROJETO  

## 1. Finalidade

Este projeto existe para **criar, auditar, atualizar, adaptar e versionar arquivos `AGENTS.md` para qualquer projeto**, novo ou já existente, de modo que regras cruciais de continuidade, persistência, rastreabilidade, estratégia, planejamento, recuperação e honestidade operacional não precisem ser reinventadas a cada novo projeto.

O `AGENTS.md` do projeto **Classe e Massas** deve ser tratado como uma **fonte de experiência e referência metodológica**, e não como um modelo a ser copiado cegamente. O Gerador de Agents deve separar aquilo que é **universal** daquilo que é **específico do domínio**.

A regra central é:

> **Todo projeto deve herdar um núcleo universal de governança e acrescentar apenas as regras específicas necessárias ao seu objeto, ferramentas, riscos, formatos e fluxo de trabalho.**

O Projeto Gerador de Agents deve possuir e versionar sua própria fonte canônica universal, preferencialmente denominada `AGENTS_KERNEL.md`, da qual os `AGENTS.md` dos demais projetos serão derivados.

---

## 2. Arquitetura obrigatória

O Gerador de Agents deve trabalhar com três camadas distintas:

### CAMADA 1 — NÚCLEO UNIVERSAL

Regras comuns e obrigatórias para qualquer projeto, independentemente do tema.

### CAMADA 2 — PERFIL DO PROJETO

Informações próprias de cada projeto: finalidade, arquitetura, fontes da verdade, repositórios, ferramentas, formatos canônicos, tipos de entregas, riscos, fases e critérios de conclusão.

### CAMADA 3 — MÓDULOS ESPECIALIZADOS

Regras adicionais ativadas apenas quando forem aplicáveis, por exemplo:

- tradução;
- pesquisa documental;
- produção jurídica;
- desenvolvimento de software;
- análise de dados;
- publicação editorial;
- automações;
- uso de APIs;
- produção de documentos, planilhas, apresentações ou PDFs;
- coleta e preservação de provas digitais;
- outros domínios especializados.

É proibido transformar uma regra setorial de um projeto específico em regra universal sem demonstrar que ela é realmente independente do domínio.

---

## 3. Núcleo universal obrigatório

Todo `AGENTS.md` gerado ou revisado deverá incorporar, adaptando apenas a terminologia necessária, os seguintes princípios.

### 3.1. Confirmação imediata ao usuário

Ao receber um novo pedido que possa exigir leitura, análise, registro, ferramentas ou processamento perceptível, o agente deve responder imediatamente, antes da primeira operação demorada:

> **Vou ler o seu prompt, analisar, registrar o pedido e tomar as devidas providências.**

Essa mensagem deve ocorrer antes do registro persistente para impedir períodos iniciais de silêncio que possam ser interpretados como travamento.

O agente não deve afirmar que o pedido já foi registrado antes da confirmação técnica do registro.

### 3.2. Registro obrigatório de todos os pedidos

Todo pedido, correção, complemento, pergunta, determinação, interrupção ou mudança de instrução deve ser registrado de forma persistente, sequencial e rastreável antes da execução substantiva.

O mecanismo preferencial é `REQUEST_LOG.jsonl` ou equivalente estruturado.

Cada registro deve conter, quando aplicável:

- identificador único;
- marcador temporal;
- texto integral ou representação fiel do pedido;
- escopo ou frente de trabalho;
- estratégia relacionada;
- estado do pedido;
- ação solicitada;
- referências aos resultados produzidos.

Depois de confirmar tecnicamente o registro, quando a execução continuar, o agente deve informar:

> **Pedido registrado.**

O registro de pedidos deve ser a principal fonte para responder perguntas como “qual foi meu último pedido?”, “onde paramos?” e “o que ficou pendente?”.

### 3.3. Fonte da verdade

O projeto deve declarar uma hierarquia explícita de fontes da verdade.

Como padrão:

1. arquivos canônicos persistentes e versionados;
2. manifestos ou arquivos estruturados de estado;
3. histórico de versionamento e commits comprovados;
4. cópias persistentes verificáveis;
5. somente depois, memória, contexto de conversa ou resumo do Modelo de IA.

Memória nunca deve prevalecer sobre evidência documental mais recente.

### 3.4. Estratégia registrada antes da execução substantiva

Nenhuma tarefa substantiva deve ser executada como atividade órfã.

Antes de executar, o agente deve identificar:

- estratégia;
- `strategy_id`, quando se tratar de estratégia autônoma;
- objetivo;
- plano ou roadmap;
- fase atual;
- entrega, objetivo ou gate da fase;
- dependências;
- tarefa atual;
- resultado esperado;
- próximo passo lógico.

Toda estratégia autônoma deve existir em registro persistente e auditável antes de sua execução substantiva.

O Gerador deverá impor dois registros complementares:

- `PROJECT_STATE.json` ou equivalente — fotografia do estado corrente da estratégia;
- `STRATEGY_LOG.jsonl` — histórico cronológico, append-only e auditável da criação e evolução das estratégias autônomas.

Um arquivo não substitui o outro.

#### 3.4.1. Registro obrigatório de toda Estratégia Autônoma

Todo `AGENTS.md` gerado ou revisado deverá tornar obrigatório registrar **cada Estratégia Autônoma** antes de qualquer execução substantiva a ela vinculada.

Considera-se Estratégia Autônoma uma frente de trabalho que possua objetivo próprio e identificável, possa ter fases ou gates próprios e seja capaz de ser retomada como unidade independente, ainda que vinculada a estratégia maior. Uma tarefa instrumental isolada não cria, por si só, nova estratégia.

A regra universal é:

> **ESTRATÉGIA AUTÔNOMA NOVA = `strategy_id` NOVO + EVENTO `CREATED` PERSISTIDO NO `STRATEGY_LOG.jsonl` ANTES DA EXECUÇÃO SUBSTANTIVA.**

O `strategy_id` deve permanecer estável durante toda a vida da estratégia e nunca ser reutilizado para outra. O padrão deve incorporar identificação do projeto, data e sequência, por exemplo:

```text
STRAT-CEM-20260917-001
STRAT-GDA-20260917-001
```

Cada linha do `STRATEGY_LOG.jsonl` representa um **evento**, preservando o histórico em modelo append-only. Eventos mínimos:

```text
CREATED
UPDATED
PAUSED
RESUMED
SUPERSEDED
CONCLUDED
CANCELLED
BACKFILLED
```

Cada evento deverá conter, sempre que tecnicamente possível:
