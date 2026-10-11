# AGENTS.md — GERADOR DE AGENTS

**project_id legado:** `GDA`  
**project_code:** `PRJ-000002`  
**project_sequence:** `000002`  
**project_alias:** `GDA`  
**project_name:** `Gerador de Agents`  
**generated_from_kernel:** `1.9`  
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

### Ponte bidirecional com o Coordenador Geral

Antes de tratar pedidos com **possível repercussão transversal**, **dúvida de pertencimento/roteamento**, possível vínculo com a **governança global** ou sinais de **candidato a novo Projeto**, consultar, quando a Biblioteca estiver acessível:

`/Governanca-Geral-Modelos-IA/00_BOOTSTRAP_COORDENADOR_GERAL.md`

Regras:

- pedidos inequivocamente locais e já abrangidos por este Projeto seguem diretamente este `AGENTS.md`, sem consulta obrigatória ao Bootstrap;
- a consulta ao Bootstrap é condicional e serve para classificar/rotear, não para substituir a governança local;
- evitar loop de roteamento: Bootstrap → Projeto é entrada normal; Projeto → Bootstrap ocorre apenas diante de dúvida, repercussão transversal ou governança global;
- se a Biblioteca/Bootstrap não estiver acessível na sessão, não inventar seu conteúdo; registrar a limitação quando material e prosseguir pela governança local comprovada;
- conversas classificadas como casuais/efêmeras pelo Coordenador Geral não devem ser artificialmente absorvidas por este Projeto.

### Arquitetura universal de ambientes v2.2

Este Projeto obedece à arquitetura global de seis planos:

1. G — identidade/governança;
2. A — superfície de acesso;
3. E — executor;
4. C — contexto/memória;
5. K — fontes de conhecimento;
6. P — persistência/publicação.

Fonte global versionada: `thiagoba2004/governanca-geral-modelos-ia/ARQUITETURA_UNIVERSAL_AMBIENTES_EXECUCAO_PERSISTENCIA.md`.

Regras mínimas:

- Projeto ChatGPT não é sinônimo deste Projeto de Governança;
- este PRJ está em `B0_NO_CHATGPT_PROJECT_BINDING`; não possui modo C2/C3 próprio;
- Work permanece um executor disponível fora de qualquer contêiner ChatGPT; handoff por isolamento só se aplica a um futuro vínculo B1 em C3;
- fontes anexadas formam Core Context curado, não acervo integral;
- Biblioteca é fonte/espelho operacional;
- GitHub permanece fonte canônica de regras, estado e histórico;
- filesystem local é working copy, nunca única cópia relevante;
- Codex trabalha sobre repositório/working tree e deve devolver resultados à persistência canônica;
- memória não prevalece sobre evidência persistente.

O arquivo `EXECUTION_ENVIRONMENT_PROFILE.json` schema v2 registra essas preferências.

## 3. Fonte da verdade deste projeto
## 3. Fonte da verdade deste projeto

Ordem de precedência:

1. `AGENTS_KERNEL.md` para regras universais;
2. `IDENTIFICATION_STANDARD.md` para a gramática canônica de códigos e alocação;
3. `AGENTS.md` para regras específicas deste repositório;
4. `REQUEST_LOG.jsonl` para sequência de pedidos;
5. `STRATEGY_LOG.jsonl` para histórico de estratégias;
6. `PROJECT_REGISTRY.jsonl` para códigos e denominações canônicos dos Projetos conhecidos;
7. `PROJECT_STATE.json` para fotografia do estado corrente;
8. `ROADMAP.md` para Plano de Fases;
9. `GERADOR_WORKFLOW.md` para o procedimento operacional;
10. `MODULE_SELECTION.md` para decisão de módulos;
11. `DECISIONS.md` para decisões arquiteturais/metodológicas;
12. `CHANGELOG.md` para evolução do kernel e do Gerador;
13. histórico Git comprovado;
14. somente depois, memória ou contexto conversacional.

## 4. Estratégias

Toda Estratégia Autônoma deve possuir `strategy_code` e `strategy_name` estáveis e evento no `STRATEGY_LOG.jsonl` antes de qualquer execução substantiva.

O código canônico é independente de nomes e aliases e segue `IDENTIFICATION_STANDARD.md`:

```text
EA-PPPPPP-EEEEEE
```

Para este Projeto, `PPPPPP = 000002`. Novas Estratégias devem usar `strategy_id = strategy_code`. Identificadores históricos `STRAT-GDA-...` permanecem apenas como legados mapeados.

O log é append-only. Continuação, retomada ou alteração material mantém o mesmo `strategy_code`; somente nova Estratégia Autônoma recebe novo código.

O `STRATEGY_REGISTRY.jsonl` é índice agregado e reconstruível. Nunca prevalece sobre o `STRATEGY_LOG.jsonl` local do projeto de origem. Quando o Gerador tiver acesso a estratégias comprovadas de projetos auditados ou gerados, o índice deverá ser atualizado sem inventar estados ausentes.

## 5. Plano de Fases

Nenhuma Estratégia Autônoma pode existir sem Plano de Fases explícito, persistente e integralmente numerado.

Cada fase deve registrar obrigatoriamente `phase_number`, `phase_code`, `phase_name` e `phase_total`, além de estado, objetivo e gate quando aplicável.

Padrão canônico:

```text
F-PPPPPP-EEEEEE-FFF
```

Padrão textual:

```text
FASE 01/05 [F-000002-000004-001] — Registro e delimitação
FASE 02/05 [F-000002-000004-002] — ...
FASE 05/05 [F-000002-000004-005] — Verificação e fechamento
```

É proibido manter fases sem número, inclusive rótulos como “FASE FINAL” isoladamente.

## 5.1. Padrão de resposta para recuperação de estado

Quando o usuário perguntar **“Onde paramos? Qual a Estratégia Autônoma em curso? Qual a Fase dessa Estratégia Autônoma? E qual o Projeto?”** ou formulação equivalente, responder obrigatoriamente:

```text
PROJETO: <PROJECT_CODE> — <PROJECT_NAME>
ALIAS: <PROJECT_ALIAS, quando existir>
ESTRATÉGIA AUTÔNOMA: <STRATEGY_CODE> — <STRATEGY_NAME>
FASE: <PHASE_NUMBER>/<PHASE_TOTAL> [<PHASE_CODE>] — <PHASE_NAME>
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
IDENTIFICATION_STANDARD.md
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

Para o módulo `publication`, quando houver publicação de conteúdo textual/editorial, deve ser propagada a política condicional de artefatos:

```text
Markdown (.md) = fonte textual canônica
HTML (.html) = artefato de publicação, quando houver publicação
JSON/JSONL    = somente quando houver função estruturada real
```

JSON não é terceiro artefato obrigatório. É proibido criar JSON apenas para duplicar conteúdo, outline, caminhos ou metadados já adequadamente preservados no Markdown/HTML. Quando houver JSON funcional, o perfil do projeto deve indicar sua finalidade estruturada ou consumidor/processo.


### 9.2. Propagação obrigatória do padrão de Modelos públicos

Quando o módulo `publication` estiver ativado e o projeto publicar **Modelos reutilizáveis**, o Gerador deve materializar no `AGENTS.md` do projeto-alvo, no mínimo, estas regras:

1. todo Modelo público possui botão **`COPIAR MODELO`**;
2. o botão fica **imediatamente acima** do texto exato a copiar, sem elementos intermediários;
3. a função copia somente o Modelo;
4. somente a edição vigente do Modelo permanece no Site Público;
5. edições anteriores não recebem botões, links, cards, menus, rotas navegáveis ou outros portões de acesso no Site Público;
6. o histórico de edições é preservado em Git ou mecanismo não publicado;
7. a verificação pública deve testar posição do botão, alvo de cópia e inexistência de acesso à edição superada.

Essas regras são obrigatórias para projetos com publicação de Modelos e não podem permanecer apenas no módulo: devem ser propagadas para o `AGENTS.md` gerado ou migrado.


### 9.3. Propagação obrigatória do padrão de Site Público

Quando o módulo `web-site` estiver `ATIVADO`, o Gerador deve materializar no `AGENTS.md` do projeto-alvo, no mínimo:

1. arquitetura multipágina quando o projeto foi definido como Site;
2. menu global consistente em todas as rotas;
3. Home institucional enxuta, sem duplicar os Menus, salvo decisão expressa;
4. página própria **Mapa do Site** e hiperlink **Mapa do Site** no rodapé de toda página pública;
5. identidade visual exclusiva do projeto, com design tokens documentados;
6. responsividade mobile/desktop, foco visível, semântica e `aria-current="page"`;
7. páginas centrais com conteúdo real, sem placeholders;
8. separação entre governança interna do repositório e interface pública;
9. `SITE_ARCHITECTURE.md` e `SITE_STYLE_GUIDE.md`;
10. gate de auditoria de rotas, menu, Mapa do Site, mobile, links, identidade e vazamento interno;
11. avaliação explícita das camadas **Notícias, Artigos e Observatório** quando o Site tiver vocação de conhecimento, consulta, formação, pesquisa, análise ou atualização temática;
12. distinção funcional obrigatória: Notícias = mudança factual/temporal; Artigos = análise autoral/argumentativa; Observatório = pesquisa cumulativa, visão sistêmica e sinais/lacunas;
13. decisão explícita de composição da navegação: `TOP_LEVEL_SEPARATE`, `EDITORIAL_HUB`, `NESTED_CONTEXTUAL` ou `NOT_APPLICABLE`;
14. regra de que a aplicabilidade das três camadas **não obriga** três itens independentes no menu global;
15. prevenção de duplicação editorial por classificação primária de conteúdo e referências cruzadas.

Quando `research` e/ou `publication` também estiverem ativos, o AGENTS do projeto-alvo deve propagar as regras complementares de monitoramento periódico, horizon scanning, evidência viva, distinção entre cadência de busca e gatilho de publicação e identificação do tipo editorial primário.

É proibido tratar “Site” como sinônimo de uma homepage com cards e uma página longa.

### 9.4. Propagação obrigatória do Fale Conosco protocolado

Quando o módulo `contact-protocol` estiver `ATIVADO`, o Gerador deve materializar no `AGENTS.md` do projeto-alvo:

1. **Fale Conosco** no menu global;
2. e-mail institucional do projeto;
3. prefixo e formato do protocolo;
4. backend/provedor aprovado e estado de configuração;
5. página de confirmação `noindex,nofollow`;
6. regra de que protocolo só é confirmado após aceite do backend;
7. confirmação por e-mail somente depois do recebimento confirmado;
8. teste end-to-end real antes do estado `E2E_VERIFICADO`;
9. `CONTACT_STACK.md` ou equivalente;
10. proibição de troca silenciosa de provedor.

Quando o usuário determinar “seguir o mesmo padrão do Fale Conosco do Classe e Massas”, o padrão técnico de referência é:

```text
Forminit = recebimento/aceite da submissão e anexos
EmailJS  = confirmação do protocolo ao e-mail informado
```

FormSubmit ou outro serviço não é substituto automático. A mudança exige decisão expressa e persistida.

## 10. Perfis

Cada perfil em `profiles/` deve registrar, quando aplicável:

- `project_code`, `project_sequence`, `project_name` e `project_alias`;
- `project_id` legado, quando existir;
- nome e finalidade;
- repositório/fonte de persistência;
- versão do kernel utilizada ou auditada;
- módulos ativados, não aplicáveis ou pendentes de evidência;
- arquivos canônicos;
- riscos e restrições;
- estado de migração/implantação;
- referência ao log local de estratégias.

## 11. Projeto novo

Para projeto novo, seguir a **Rota A** de `GERADOR_WORKFLOW.md`: identificar finalidade, persistência, versionamento, formatos, ferramentas e riscos; alocar `project_code` em `PROJECT_REGISTRY.jsonl`; definir `project_name` e alias opcional; selecionar módulos e arquivos auxiliares; depois gerar e verificar o `AGENTS.md` e registrar a origem do kernel.

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


### Padrão transversal do botão ENVIAR MENSAGEM

Quando o módulo `web-site` estiver ativo e houver formulário público, propagar para o AGENTS do projeto-alvo a regra de que **ENVIAR MENSAGEM** usa `submit-button`, sempre oval/pílula (`border-radius:999px`), preservando a cor primária própria do projeto.

### 9.5. Propagação obrigatória da pauta editorial interna

Quando o módulo `publication` estiver `ATIVADO` e o projeto possuir ou planejar **Artigos** ou uma fila de conteúdos analíticos futuros, o Gerador deve:

1. criar ou avaliar `governanca/PAUTA_EDITORIAL.md`;
2. usar `templates/PAUTA_EDITORIAL.example.md` como estrutura mínima;
3. materializar no `AGENTS.md` do projeto-alvo a distinção entre pauta editorial e Roadmap;
4. exigir triagem de densidade, novidade, relevância, fontes e redundância antes da pesquisa substantiva;
5. exigir Estratégia Autônoma e Plano de Fases antes da execução de um item priorizado;
6. manter estados editoriais internos em português e registrar publicação/suspensão/descarte;
7. impedir a exposição da pauta, prioridades e itens não publicados na camada pública;
8. incluir busca por vazamento da pauta na auditoria de publicação.

Se o projeto não possuir nem planejar Artigos/fila editorial futura, registrar a decisão como `NOT_APPLICABLE` em vez de criar um arquivo vazio.



## Classificação Universal de Informação

Antes de criar, mover, enviar, fazer upload, commit, publicar ou anexar arquivo persistente, aplicar a política global:

- `/Governanca-Geral-Modelos-IA/CLASSIFICACAO_UNIVERSAL_INFORMACAO.md`;
- `/Governanca-Geral-Modelos-IA/INFORMATION_CLASSIFICATION_POLICY.json`.

Se a Biblioteca não estiver acessível, aplicar obrigatoriamente as regras mínimas abaixo:

1. classificar **sensibilidade**: `S0_PUBLICO`, `S1_INTERNO_NAO_SENSIVEL`, `S2_CONFIDENCIAL`, `S3_ALTAMENTE_SENSIVEL` ou `S4_SEGREDO_CRITICO`;
2. classificar **superfície**: `P0_COFRE_EXTERNO`, `P1_GIT_PRIVADO`, `P2_GIT_PUBLICO_REPOSITORIO` ou `P3_PUBLICO_SITE`;
3. `S2` ou superior nunca pode ser salvo em repositório público nem no Site;
4. documento bruto `S3` permanece em cofre externo por padrão e não deve ser commitado ao Git;
5. `S4` nunca deve ser enviado ao Modelo nem persistido em Git, Biblioteca, chat ou logs;
6. conteúdo só pode descer de classe mediante criação de **derivado sanitizado**; o original mantém sua classificação;
7. mudança de visibilidade do repositório, ativação de Pages ou mudança de destino exige nova classificação.

O arquivo `INFORMATION_HANDLING_PROFILE.json` registra a superfície técnica e os limites deste repositório.

### 9.6. Propagação obrigatória do índice semântico-factual

Projetos com corpus persistente relevante devem herdar o módulo `knowledge-index`, com `governanca/KNOWLEDGE_INDEX.jsonl`, gerador determinístico e regra de consulta prévia para perguntas transversais. O índice é interno, não substitui os documentos originais e não reintroduz JSON como espelho editorial.

### 9.7. Propagação obrigatória da melhoria contínua proativa

Todo projeto gerado ou migrado deve receber:

- `IMPROVEMENT_LOG.jsonl` ou equivalente;
- obrigação de comunicar ao usuário oportunidades materiais de inovação/aperfeiçoamento identificadas;
- registro persistente da oportunidade;
- **innovation check** no fechamento de trabalho substancial;
- trava contra expansão silenciosa de escopo: sugestão e execução são estados diferentes.

Quando `research` estiver ativo e o tema admitir produção acadêmica brasileira, propagar também a BDTD/IBICT como fonte sistemática de descoberta, com validação no repositório institucional de origem.

## Gate de atribuição de ações por executor — 10/10/2026

**Decisão humana transversal:** manter banco local `governanca/EXECUTOR_ACTION_CATALOG.json`, herdando as ações globais do catálogo `GOV-EXEC-ACTIONS-000001` e a política `GOV-POL-ECO-000001`. Para trabalho persistente, decompor a tarefa em ações identificáveis; antes de cada ação material, conferir `action_id`, `required_executor`, autorização, capacidades, limites, segurança e gates locais. É proibido encaminhar uma ação não classificada ou a executor divergente. A exceção exige decisão humana **expressa e específica**, registrada no catálogo global de overrides, com evidência verificável; aprovação desta política não é autorização genérica de exceção.

Preferir mecanismo determinístico seguro quando suficiente; usar o Chat em análise/documentação acessível e reservar Work/Codex para capacidades técnicas necessárias. A catalogação não substitui metodologia, checkpoints, políticas de sigilo ou autorizações existentes. O verificador `runtime/executor_action_gate.py` no repositório da Governança só bloqueia **despachos que efetivamente o invocarem**: não alegar interceptação automática das interfaces nativas Chat, Work ou Codex, nem mudança de executor sem comprovação.

## Titularidade operacional e transferência ao Projeto especializado — 10/10/2026

**Autoridade:** `REQ-20261010-003`; regra transversal `REQ-GLOBAL-20261010-014` e `ADR-GOV-0005`; procedimento em `GERADOR_WORKFLOW.md` A6 e B8.

1. O Gerador **constitui** e adapta a infraestrutura dos Projetos; não recebe por inferência a competência de pesquisar, publicar ou gerenciar indefinidamente o conteúdo que pertence a cada Projeto.
2. O Chat Global é Coordenador do portfólio e roteador de demandas; não é substituto permanente do Chat especializado de cada Projeto.
3. Se o usuário atribuir acompanhamento conversacional **contínuo ao ChatGPT**, é obrigatório registrar e confirmar Projeto ChatGPT **específico** vinculado à identidade `PRJ-NNNNNN` antes de considerar aceita a transferência (`B1_CHATGPT_PROJECT_BOUND`). O modo `C2` ou `C3` depende da escolha humana; a existência do repositório GitHub não prova criação do contêiner.
4. Projetos técnicos com instância especializada de engenharia designada **sem mandato de acompanhamento ChatGPT contínuo** podem continuar em `B0`; essa possibilidade não justifica deixar sem dono operacional os Projetos destinados ao Chat especializado.
5. Após Rota A A1–A5, executar o **Gate A6**; após Rota B B1–B7, executar o **Gate B8**. Exigir prova de destino e leitura/aceite do estado local, não apenas versão Git.
6. Se faltar criação/configuração do contêiner, preservar `TECHNICAL_BOOTSTRAP_VERIFIED` ou `MIGRATION_VERIFIED`, registrar `SPECIALIZED_INSTANCE_REQUIRED` / `HANDOFF_PENDING` e preparar o pacote mínimo. **Proibido** declarar `PROJECT_OPERATIONAL_HANDOFF_ACCEPTED` sem comprovação de recebimento **dentro do contêiner**, quando ele é exigido.
7. Preparar Core Context curado e instruções do Projeto, mediante autorização e classificação, usando arquivos já existentes. O handoff **não** gera permissão de escrita, consumo ou troca de executor; aplicar catálogo global/local de `action_id` e PEP em cada operação.
8. A decisão de criar Projeto ChatGPT para o **próprio Gerador transversal** continua pendente de análise específica; nenhum vínculo `B1` é presumido para PRJ-000002.
9. As alterações desta regra são **normativas**. Não provam criação de Projetos ChatGPT, ativação de memória C2/C3, execução automatizada ou teste de integração.

**Próximo passo operacional:** quando os Projetos `PRJ-000021/022` demandarem acompanhamento conversacional contínuo, preparar e entregar aos seus Projetos ChatGPT especializados as instruções, o estado e os limites; aguardar criação/configuração humana e teste de recebimento antes de declarar aceite. A aprovação das missões setoriais por conversa não dispensa registrar fontes e estado local quando permitido.

## Regra de entrega e persistência de relatórios A6/B8 — 10/10/2026

**Autoridade:** `REQ-20261010-007` / `REQ-GLOBAL-20261010-018`; procedimento obrigatório em `GERADOR_WORKFLOW.md`, **seção 7**. Corrige a ausência anterior de instrução comum de localização e nomenclatura dos diagnósticos dos cinco Projetos especializados.

Ao preparar qualquer **Instrução inicial** ou **prompt de homologação** de Projeto ChatGPT, especificar expressamente:
1. o Gate correto da Rota A (`A6`) ou Rota B (`B8`);
2. a pasta `governanca/recebimentos/` no **repositório de cada Projeto**, nunca somente no Gerador;
3. o arquivo canônico `AAAA-MM-DD-prj-NNNNNN-gate-a6.md` ou `AAAA-MM-DD-prj-NNNNNN-gate-b8.md` com a data real do teste; iterações `-r02` etc.;
4. o procedimento de registrar pedido, verificar fontes, classificar informação, confirmar executor e autorização, persistir GitHub e ler o resultado;
5. que **relatório documental salvo não é Gate operacional aceito**, nem certifica B1/C3, GitHub Pages ou automação na plataforma.

O Gerador deve manter o modelo/perfil do Projeto e o `AGENTS.md` local coerentes com essa convenção. Falha de escrita GitHub deve produzir `NOT_PERSISTED` com relatório pronto para retomada, nunca link inventado. Trabalhos anteriores podem ser migrados preservando história e endereços legados com ponteiros Markdown. Não reabrir Estratégias concluídas ou acrescentar despesas apenas para reorganizar relatórios.
