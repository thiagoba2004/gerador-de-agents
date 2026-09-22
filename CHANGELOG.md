# CHANGELOG — GERADOR DE AGENTS

Todas as alterações materiais do núcleo universal e da infraestrutura do Gerador devem ser registradas aqui.

## 1.12 — 22/09/2026 — Coleção → Detalhe em Publicações

- páginas de Notícias, Artigos e Observatório passam a separar **índice/coleção** de **conteúdo individual**;
- o título de cada item é o hiperlink principal para sua página própria;
- índice deve oferecer metadados e resumo/subtítulo curto, sem reproduzir integralmente múltiplos conteúdos;
- Observatório passa a tratar snapshots/relatórios/unidades temáticas como objetos individuais versionáveis;
- Markdown canônico passa a acompanhar a mesma granularidade pública;
- regra incorporada a `web-site`, `publication`, template de AGENTS e template de perfil;
- estratégia: `EA-000002-000009`.


## 1.11 — 22/09/2026 — Arquitetura editorial transversal

- instituídas as funções canônicas **Notícias**, **Artigos** e **Observatório** para Sites de conhecimento quando materialmente aplicáveis;
- definida a separação funcional entre atualização factual, análise autoral e inteligência/pesquisa cumulativa;
- criados quatro modos de composição: `TOP_LEVEL_SEPARATE`, `EDITORIAL_HUB`, `NESTED_CONTEXTUAL` e `NOT_APPLICABLE`;
- `EDITORIAL_HUB` passa a ser hipótese preferencial a testar em Sites já densos, sem impor rótulo automático ao hub;
- módulo `research` passa a prever busca recorrente, horizon scanning e evidência viva;
- módulo `publication` passa a exigir função editorial primária e regras específicas por tipo;
- template de perfil passa a registrar `editorial_architecture`;
- perfis de Ações Judiciais e Planejamento Financeiro sincronizados com suas arquiteturas públicas vigentes e com as novas camadas planejadas;
- estratégia: `EA-000002-000008`.

## 1.10 — 20/09/2026 — JSON condicional

- revogada a regra de triplicidade editorial obrigatória `.md + .html + .json`;
- Markdown permanece como fonte textual canônica;
- HTML permanece como artefato de publicação quando houver;
- JSON/JSONL passa a ser criado somente quando houver função estruturada real e finalidade/consumidor identificável;
- proibida a criação de JSON apenas para duplicar título, outline, caminhos, metadados ou conteúdo já preservado em Markdown/HTML;
- atualizado `modules/publication.md`, `templates/AGENTS.example.md`, `AGENTS.md` e os perfis de Classe e Massas, Ações Judiciais e Planejamento Financeiro;
- a versão 1.4 do changelog permanece como registro histórico da política posteriormente revogada;
- estratégia de manutenção: `EA-000002-000007`.

## 1.8 — 20/09/2026 — Primeiro teste real da Rota A e educação profissional

- criação de `PRJ-000003 — Ações Judiciais` e `PRJ-000004 — Planejamento Financeiro`;
- primeiro teste do Gerador em dois repositórios novos e vazios;
- criação do módulo reutilizável `professional-education`, motivado pela necessidade comprovada de separar preparação para certificação de desenvolvimento de competência profissional;
- o módulo exige distinção `TRILHA_PROVA` / `TRILHA_PRATICA`, mapeamento de fontes, objetivos de competência, avaliação e atualização;
- o kernel permanece em 1.4 porque a evolução é modular, não universal;
- estratégia: `EA-000002-000006`.

## 1.7 — 19/09/2026 — Padrão de Modelos Públicos

- módulo `publication` passa a exigir botão **`COPIAR MODELO`** imediatamente acima do conteúdo copiável;
- somente a edição vigente de cada Modelo pode permanecer disponível no Site Público;
- edições anteriores devem ser preservadas por Git ou mecanismo não publicado, sem botões, links, cards, menus ou rotas públicas de acesso;
- `AGENTS.md` do Gerador passa a exigir propagação material dessas regras para projetos-alvo;
- `templates/AGENTS.example.md` atualizado para materializar o padrão em novos AGENTS;
- estratégia: `EA-000002-000005`.

## 1.6 — 19/09/2026 — Codificação hierárquica universal

- atualização do núcleo universal para `AGENTS_KERNEL.md` **1.4**;
- criação de `IDENTIFICATION_STANDARD.md` como metodologia canônica única para identificação;
- substituição de códigos de Projeto derivados de iniciais por `PRJ-NNNNNN`;
- definição de `EA-PPPPPP-EEEEEE` para Estratégias Autônomas;
- definição de `F-PPPPPP-EEEEEE-FFF` para Fases;
- reclassificação de `CEM` e `GDA` como aliases mnemônicos, sem função identificadora;
- alocação inicial: `PRJ-000001 — Classe e Massas` e `PRJ-000002 — Gerador de Agents`;
- migração do `PROJECT_REGISTRY.jsonl` e do `STRATEGY_REGISTRY.jsonl` com preservação dos identificadores legados;
- regra de não reutilização e não renumeração de códigos;
- atualização de `AGENTS.md`, template de AGENTS, perfil do Classe e Massas e estados estruturados;
- estratégia canônica: `EA-000002-000004`; identificador legado: `STRAT-GDA-20260919-002`.

## 1.5 — 19/09/2026 — Governança numérica e continuidade determinística

- atualização do núcleo universal para `AGENTS_KERNEL.md` **1.3**;
- criação de `PROJECT_REGISTRY.jsonl` com `project_code` + `project_name` para os Projetos conhecidos;
- obrigatoriedade de código e denominação para todo Projeto e toda Estratégia Autônoma;
- padronização de `strategy_id` como `STRAT-<PROJECT_CODE>-AAAAMMDD-NNN` para novas estratégias;
- obrigatoriedade de `phase_number`, `phase_total`, `phase_code` e `phase_name` em todos os Planos de Fases;
- proibição de fases não numeradas como “FASE FINAL” isoladamente;
- instituição do padrão determinístico de resposta para “Onde paramos?” com Projeto, Estratégia, Fase, estado, ponto exato e próximo passo;
- atualização do `AGENTS.md`, `templates/AGENTS.example.md`, `STRATEGY_REGISTRY.jsonl`, `PROJECT_STATE.json` e perfil do Classe e Massas;
- estratégia: `STRAT-GDA-20260919-001`.

## 1.4 — 18/09/2026 — Triplicidade editorial

- criação de regra reutilizável no módulo `publication` para exigir, em conteúdo textual/editorial, o trio coordenado Markdown + HTML + JSON;
- definição de Markdown como fonte textual canônica, HTML como artefato de publicação e JSON como representação estruturada/interoperável;
- criação de gate que impede considerar completa uma publicação textual sem os três artefatos coerentes;
- exigência de decisão expressa, persistente e versionada para qualquer exceção;
- atualização do `AGENTS.md` do Gerador para obrigar a propagação das regras modulares ao `AGENTS.md` gerado;
- atualização de `templates/AGENTS.example.md` para materializar a regra quando o módulo `publication` estiver ativado;
- estratégia: `STRAT-GDA-20260918-001`.

## 1.3 — 17/09/2026 — Gerador operacional sobre kernel 1.2

- criação de `GERADOR_WORKFLOW.md` com rotas distintas para projeto novo e projeto existente;
- criação de `MODULE_SELECTION.md` com estados conceituais `ATIVADO`, `NÃO APLICÁVEL` e `PENDENTE DE EVIDÊNCIA`, além dos códigos estruturados equivalentes;
- criação de `templates/AGENTS.example.md`, `templates/AUDIT_REPORT.example.md` e `templates/PROJECT_PROFILE.example.json`;
- criação dos módulos `research`, `legal`, `publication`, `digital-evidence`, `translation`, `software`, `data` e `automation`;
- primeiro teste integral não destrutivo no projeto `thiagoba2004/classe-e-massas`;
- criação e consolidação de `profiles/classe-e-massas.json` e `audits/classe-e-massas-2026-09-17.md`;
- identificação, no teste real, de conflito entre a ordem antiga de registro do `AGENTS.md` v1.8 do Classe e Massas e a ordem vigente do kernel 1.2;
- recuperação dos pedidos históricos `REQ-20260917-011` a `REQ-20260917-014` a partir do `REQUEST_LOG.jsonl` do Classe e Massas;
- backfill comprovado dos eventos históricos de criação, evolução e pausa de `STRAT-GDA-20260917-001` a partir do `STRATEGY_LOG.jsonl` do Classe e Massas;
- preservação integral e verificável da instrução histórica v1.1 em quatro segmentos em `history/`, com SHA-256 original `abf7089cb7896dd33b419126192c5da8ab6ea1bb98922a02fe44f6933ae002e2`;
- criação de `README.md` como ponto de entrada para novos modelos/agentes;
- correção do workflow para reproduzir integralmente a ordem do kernel 1.2 e distinguir `AUDITAR ≠ MIGRAR ≠ IMPLANTAR`;
- atualização de `AGENTS.md` para refletir a arquitetura operacional real do repositório;
- alinhamento entre `MODULE_SELECTION.md`, template de perfil e perfil auditado, incluindo `decided_at` e `kernel_version` por decisão;
- revisão de `automation` no perfil do Classe e Massas para `PENDENTE_DE_EVIDENCIA` por insuficiência de evidência para ativação;
- inclusão de `STRAT-CEM-20260917-001` no `STRATEGY_REGISTRY.jsonl` apenas com estado comprovado pelo log local;
- autoauditoria registrada em `audits/gerador-de-agents-self-audit-2026-09-17.md` com gate da Fase 5 satisfeito;
- conclusão das Fases 4, 5 e Final do roadmap;
- declaração do Gerador de Agents **1.3** como versão operacional inicial sobre o kernel **1.2**;
- conclusão da estratégia de bootstrap `STRAT-GDA-20260917-001` e transição do projeto para modo operacional/manutenção.

## 1.2 — 17/09/2026

- implantação do repositório independente `thiagoba2004/gerador-de-agents`;
- criação do `AGENTS_KERNEL.md` v1.2;
- criação do `AGENTS.md` do próprio Gerador;
- adoção formal de `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl`, `STRATEGY_REGISTRY.jsonl`, `PROJECT_STATE.json` e `ROADMAP.md`;
- alteração da ordem operacional dos pedidos: registrar primeiro, confirmar o registro, informar “Pedido registrado.” e somente depois iniciar leitura substantiva, análise, ferramentas ou execução;
- formalização da arquitetura núcleo universal + perfil do projeto + módulos especializados;
- preservação de `strategy_id` e `project_id` estáveis e do modelo append-only de estratégias.

## 1.1 — 17/09/2026

- obrigatoriedade de `STRATEGY_LOG.jsonl` em todos os projetos;
- instituição de `strategy_id` e `project_id`;
- eventos append-only;
- backfill controlado por evidência persistente;
- criação conceitual do `STRATEGY_REGISTRY.jsonl` agregado.

## 1.0 — 17/09/2026

- criação das instruções canônicas do Projeto Gerador de Agents;
- definição do kernel universal, perfis de projeto e módulos especializados.


## 1.9 — 20/09/2026 — Sites e contato protocolado

- criado módulo `web-site`;
- criado módulo `contact-protocol`;
- Site Público passa a exigir arquitetura explícita, menu global, Home com papel definido, Mapa do Site, identidade própria e auditoria mobile;
- Fale Conosco protocolado passa a exigir stack declarada, protocolo confirmado somente após aceite do backend e teste end-to-end;
- padrão de referência do Classe e Massas documentado como **Forminit + EmailJS**;
- troca silenciosa por FormSubmit ou outro provedor passa a ser proibida;
- perfis de Ações Judiciais e Planejamento Financeiro registram migração técnica pendente do FormSubmit para a stack canônica.
