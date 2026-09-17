# RELATÓRIO DE AUDITORIA — CLASSE E MASSAS

**project_id:** `classe-e-massas`  
**projeto:** Classe e Massas  
**fonte:** `thiagoba2004/classe-e-massas`  
**kernel de comparação:** `1.2`  
**AGENTS encontrado:** `1.8`  
**data:** 17/09/2026  
**modo:** TESTE INTEGRAL NÃO DESTRUTIVO

## 1. Objetivo

Testar o Gerador de Agents em um projeto real e complexo, verificando se o workflow consegue ler o estado persistente, identificar regras universais e específicas, selecionar módulos, localizar conflitos e produzir plano de migração sem alterar o repositório auditado.

## 2. Fontes examinadas

- `AGENTS.md` v1.8 — blob `0c0fc7bd17de1084728ed1f1f2c4aa61405d1a86`;
- `PROJECT_STATE.json` — blob `175e275be7264ba1c05b417cbba53e2541a19c0b`;
- `REQUEST_LOG.jsonl` — presença confirmada no repositório;
- `STRATEGY_LOG.jsonl` — blob `5fb2061fff04f70aceb1b3d4f3f8a021381b5f2d`;
- estrutura raiz do repositório, incluindo `artigos/`, `biblioteca/`, `editorial/`, `governanca/`, `index.html` e infraestrutura do site.

## 3. Estado comprovado antes de qualquer migração

O projeto já possui uma infraestrutura de governança avançada: `AGENTS.md`, `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl` e `PROJECT_STATE.json` existem no repositório. O `PROJECT_STATE.json` contém frentes ativas com estado, fontes canônicas, marcos comprovados, restrições e próximos passos. O `AGENTS.md` v1.8 contém regras extensas de persistência progressiva, write-through, fonte da verdade, Git como memória histórica, recuperação antes de reconstrução, não regressão, registro de pedidos, estratégias autônomas e Plano de Fases.

Portanto, o projeto não deve ser tratado como instalação nova. A rota correta é **projeto existente com migração controlada e preservação de regras locais mais rigorosas**.

## 4. Compatibilidade com o kernel 1.2

O `AGENTS.md` atual já implementa, em grau igual ou mais rigoroso que o kernel, os seguintes princípios:

- fonte da verdade documental superior à memória;
- proibição de trabalho substancial apenas no chat;
- persistência progressiva e write-through;
- verificação de salvamento;
- Git como memória histórica;
- distinção entre salvo, commitado, remoto e publicado;
- recuperação antes de reconstrução;
- não regressão;
- preservação antes de operações destrutivas;
- continuidade entre conversas e modelos;
- `REQUEST_LOG.jsonl`;
- `STRATEGY_LOG.jsonl` append-only;
- `strategy_id` estável;
- `project_id` nos eventos de estratégia;
- Plano de Fases obrigatório para Estratégias Autônomas;
- proibição de execução estrategicamente órfã.

Essas regras devem ser **preservadas**, não reescritas de forma simplificadora.

## 5. Conflito material encontrado

### Ordem de tratamento de novos pedidos

O `AGENTS.md` v1.8 ainda contém a ordem anterior nos itens 23, 24.14 e 24.15:

```text
informar imediatamente ao usuário
→ ler/analisar o necessário
→ registrar no REQUEST_LOG.jsonl
→ verificar
→ confirmar “Pedido registrado”
→ executar
```

O `AGENTS_KERNEL.md` 1.2 do Gerador adotou posteriormente a decisão `ADR-003`:

```text
registrar primeiro
→ confirmar tecnicamente o registro
→ informar “Pedido registrado.”
→ informar que irá ler o prompt, analisar e tomar as providências
→ executar
```

**Classificação:** CONFLITANTE.  
**Ação proposta:** atualizar os itens 23, 24.14 e 24.15 do Classe e Massas em migração futura, preservando a finalidade de evitar silêncio, mas obedecendo à determinação mais recente do usuário de que o registro anteceda a mensagem de confirmação.

Nenhuma alteração foi feita no repositório Classe e Massas durante este teste.

## 6. Metadado de origem do kernel

O `AGENTS.md` v1.8 é anterior à implantação operacional do Gerador e não possui `generated_from_kernel`.

**Classificação:** LACUNA DE MIGRAÇÃO, não erro histórico.  
**Ação proposta:** após migração aprovada, registrar a versão do kernel usada sem apagar a versão própria do documento.

Exemplo:

```text
generated_from_kernel: 1.2
```

## 7. Regras locais mais rigorosas ou específicas que devem ser preservadas

As seguintes regras não devem ser eliminadas pela aplicação do kernel:

- RPO próximo de zero para unidades lógicas concluídas;
- salvamento em quatro camadas para marcos críticos, com segunda cópia independente quando possível;
- estrutura específica de tradução com `traducao.md`, `status.json` e `fontes/`;
- exigência de desenvolver siglas relevantes na primeira ocorrência;
- metodologia específica para cadeia sindical `Sindicato > Federação > Confederação`;
- regras específicas de estados editoriais, tradução e publicação;
- referência ao Roadmap do Observatório Classe e Massas;
- dever de informar em checkpoints se o estado foi ou não persistido;
- regras setoriais relacionadas ao objeto político, editorial, documental e sindical do projeto.

Esses elementos pertencem ao perfil do projeto ou a módulos especializados, não ao kernel universal.

## 8. Seleção de módulos

| Módulo | Decisão | Fundamentação |
|---|---|---|
| `translation` | ATIVADO | O AGENTS possui protocolo específico de traduções e o estado canônico mantém TCM-001 em revisão. |
| `research` | ATIVADO | Pesquisa e levantamento documental integram expressamente o escopo e frentes ativas. |
| `legal` | ATIVADO | Denúncias, peças jurídicas e materiais do MPT integram o projeto. |
| `publication` | ATIVADO | O projeto mantém artigos, notícias, HTML e site público. |
| `software` | ATIVADO | Código e infraestrutura técnica do site integram o escopo. |
| `data` | ATIVADO | Bases de dados e arquivos estruturados são objetos expressos do projeto. |
| `automation` | PENDENTE DE EVIDÊNCIA | A menção genérica a automações no escopo do AGENTS, isoladamente, não comprova dependência recorrente de tarefas agendadas, gatilhos ou pipelines. |
| `digital-evidence` | PENDENTE DE EVIDÊNCIA | A leitura realizada comprova dossiês e pesquisa documental, mas não basta para afirmar que preservação probatória digital é função transversal do repositório. |

As decisões estruturadas, com `decided_at`, `kernel_version`, justificativas e fontes, estão em `profiles/classe-e-massas.json`.

## 9. Estratégias autônomas e logs

O `STRATEGY_LOG.jsonl` examinado contém cinco eventos persistidos, concentrados em duas estratégias:

- `STRAT-CEM-20260917-001` — Governança e continuidade documental do Classe e Massas;
- `STRAT-GDA-20260917-001` — Projeto Gerador de Agents, registrado provisoriamente no repositório Classe e Massas antes da criação do repositório próprio.

O próprio log já registra que estratégias anteriores ainda exigem inventário retroativo baseado em evidência persistente.

Ao mesmo tempo, o `PROJECT_STATE.json` contém várias frentes com características de Estratégia Autônoma — por exemplo TCM-001 e DOS-PLR-BB-2026 — que não aparecem no `STRATEGY_LOG.jsonl` examinado.

**Classificação:** LACUNA DE BACKFILL JÁ RECONHECIDA PELO PRÓPRIO PROJETO.

**Ação proposta:** inventário progressivo e `BACKFILLED` apenas quando cada frente puder ser comprovada por arquivos, commits, pedidos, roadmaps ou outros registros persistentes. Não preencher lacunas por memória.

## 10. Migração da história do Gerador de Agents

O `STRATEGY_LOG.jsonl` do Classe e Massas contém evidência persistente da vida de `STRAT-GDA-20260917-001` antes da criação do repositório próprio:

1. criação da estratégia;
2. atualização para kernel/logs obrigatórios;
3. pausa aguardando criação do repositório próprio.

Durante a consolidação do Gerador, essa trilha foi efetivamente **backfillada** no `STRATEGY_LOG.jsonl` local do Gerador por eventos `BACKFILLED`, preservando os identificadores dos eventos-fonte do Classe e Massas. Os pedidos `REQ-20260917-011` a `REQ-20260917-014` também foram recuperados a partir do `REQUEST_LOG.jsonl` do projeto de origem.

O log do Classe e Massas permanece prova histórica de origem; o log próprio do Gerador é a fonte local primária para a continuidade futura da estratégia.

## 11. Plano de migração proposto para o Classe e Massas

### Preservar

- `AGENTS.md` v1.8 como versão histórica recuperável;
- todas as regras locais mais rigorosas;
- `REQUEST_LOG.jsonl` existente;
- `STRATEGY_LOG.jsonl` existente;
- `PROJECT_STATE.json` e seus estados específicos;
- roadmaps e documentos setoriais.

### Acrescentar

- metadado `generated_from_kernel: 1.2` após migração aprovada;
- perfil do projeto vinculado ao Gerador;
- inventário de módulos;
- backfill progressivo das Estratégias Autônomas comprováveis.

### Reestruturar

- itens 23, 24.14 e 24.15 para a ordem vigente de registro dos pedidos;
- eventualmente separar regras reutilizáveis em módulos sem remover o texto local até que a equivalência tenha sido verificada.

### Remover

Nenhuma remoção é recomendada nesta primeira auditoria. Duplicações devem ser tratadas apenas depois de comprovar que a consolidação não reduz garantias.

### Rollback

Qualquer migração futura deve preservar a versão anterior do `AGENTS.md` por Git antes da alteração e permitir restauração integral.

## 12. Alterações efetivamente implantadas neste teste

No repositório `thiagoba2004/classe-e-massas`: **nenhuma**.

No repositório `thiagoba2004/gerador-de-agents`:

- perfil auditado criado e posteriormente alinhado ao esquema de seleção de módulos;
- este relatório de auditoria criado;
- módulos necessários à avaliação foram consolidados no Gerador;
- histórico do próprio Gerador recuperado das fontes persistentes do Classe e Massas.

## 13. Verificação do teste

O teste demonstrou que o Gerador consegue:

- reconhecer projeto existente e evitar sobrescrita automática;
- reconstruir estado a partir de fontes persistentes;
- comparar regras locais com o kernel;
- localizar conflito concreto entre versões;
- preservar regras locais mais rigorosas;
- selecionar módulos por evidência e revisar classificações excessivas;
- distinguir auditoria de implantação;
- localizar dívida de backfill sem inventar histórico;
- localizar e recuperar história migrável do próprio Gerador em outro repositório.

## 14. Estado real após consolidação

- auditoria: SALVA E VERSIONADA NO REPOSITÓRIO DO GERADOR;
- perfil: SALVO, VERSIONADO E ALINHADO À POLÍTICA DE MÓDULOS;
- migração do Classe e Massas: NÃO IMPLANTADA;
- `AGENTS.md` do Classe e Massas: NÃO ALTERADO;
- backfill histórico do Gerador: CONCLUÍDO PARA OS EVENTOS E PEDIDOS COMPROVADOS LOCALIZADOS;
- backfill das estratégias do Classe e Massas: PENDENTE E DEVE SER PROGRESSIVO.

## 15. Próximo passo lógico

A migração do Classe e Massas somente deverá ocorrer em estratégia própria e após autorização específica. Para o Gerador de Agents, este teste satisfaz o gate operacional da Fase 4; a continuidade está na Fase 5 — consolidação e verificação do próprio Gerador.
