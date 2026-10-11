# GERADOR WORKFLOW — PROCEDIMENTO OPERACIONAL

**project_code:** `PRJ-000002`  
**project_alias:** `GDA`  
**project_id legado:** `GDA`  
**kernel_version do workflow original:** `1.4` (histórico); **kernel em uso pelo Gerador:** `1.12`.

Este documento transforma a arquitetura do Gerador de Agents em um procedimento executável e reproduzível.

## 1. Regra de entrada

Antes de qualquer diagnóstico substantivo:

1. registrar o pedido no `REQUEST_LOG.jsonl` do projeto que governa a execução;
2. confirmar tecnicamente que o registro foi persistido;
3. informar ao usuário: **“Pedido registrado.”**;
4. informar que irá ler o prompt, analisar e tomar as providências necessárias;
5. identificar ou registrar a Estratégia Autônoma correspondente;
6. identificar o Plano de Fases e a fase atual;
7. somente então executar a rota aplicável.

### 1.1. Auditoria não destrutiva de outro projeto

Quando o Gerador estiver apenas auditando outro projeto, sem autorização para migrá-lo ou alterá-lo, o pedido e a estratégia de auditoria permanecem registrados no **Gerador de Agents**. A leitura do projeto-alvo não autoriza escrever nele.

Somente quando houver execução aprovada dentro do projeto-alvo é que os registros locais daquele projeto deverão ser criados ou atualizados conforme seu próprio `AGENTS.md` e o plano de migração.

A distinção é obrigatória:

```text
AUDITAR ≠ MIGRAR ≠ IMPLANTAR
```

## 2. Rota A — Novo projeto

### Etapa A1 — Diagnóstico mínimo

Identificar e registrar:

- nome e finalidade;
- alocação de `project_code` canônico em `PROJECT_REGISTRY.jsonl`;
- `project_name` e `project_alias` opcional;
- `project_id` legado, quando existir;
- repositório ou fonte persistente;
- existência ou não de Git/versionamento;
- formatos canônicos;
- ferramentas e integrações disponíveis;
- riscos de perda, publicação, segurança e operações destrutivas;
- tipos de entregas;
- restrições conhecidas;
- se houver Site Público: público-alvo, papel da Home, menu global, páginas centrais, Mapa do Site, identidade visual e referência estrutural;
- se houver Fale Conosco: e-mail institucional, necessidade de protocolo, confirmação por e-mail, anexos, stack de referência e estado real do backend.

**Gate A1:** nenhuma capacidade ou integração relevante foi inventada; todas as fontes persistentes conhecidas estão identificadas.

### Etapa A1.1 — Alocação do código canônico

Antes de criar Estratégias Autônomas no novo Projeto, aplicar `IDENTIFICATION_STANDARD.md`:

1. ler `PROJECT_REGISTRY.jsonl`;
2. alocar o próximo `PRJ-NNNNNN` disponível;
3. persistir e verificar o registro;
4. somente depois gerar códigos `EA-PPPPPP-EEEEEE`.

**Gate A1.1:** código único, persistido e não derivado da denominação.

### Etapa A1.2 — Estratégia inicial e Plano de Fases (gate obrigatório)

Antes de executar trabalho substantivo, criar a primeira EA do PRJ com Plano de Fases próprio, registrar pedido, CREATED no `STRATEGY_LOG.jsonl`, estado, Roadmap e catálogo global mediante prova. `templates/PROJECT_CREATION_EA.example.md` contém o modelo. O Código PRJ deve estar alocado previamente; para repositório antigo (Rota B), preservar EAs históricas. O Gate A1.2 bloqueia a constituição nova quando faltar EA ou Plano; confirmar a verificação estrutural na Etapa A5 usando `tools/project_creation_gate.py --gate bootstrap`.


### Etapa A2 — Seleção de módulos

Aplicar `MODULE_SELECTION.md`. Cada módulo deve receber um dos estados:

- `ATIVADO`;
- `NÃO APLICÁVEL`;
- `PENDENTE DE EVIDÊNCIA`.

Toda ativação deve ter justificativa rastreável.

Regras de dependência:
- projeto com Site Público → avaliar obrigatoriamente `web-site`;
- Site Público com Fale Conosco/protocolo → avaliar obrigatoriamente `contact-protocol`;
- `web-site` normalmente coexiste com `publication` e `software`, mas cada ativação mantém justificativa própria.

**Gate A2:** lista de módulos decidida e registrada.

### Etapa A3 — Infraestrutura mínima

Criar ou adaptar, conforme necessário:

```text
AGENTS.md
REQUEST_LOG.jsonl
STRATEGY_LOG.jsonl
PROJECT_STATE.json
ROADMAP.md ou PLAN.md
DECISIONS.md, quando aplicável
SITE_ARCHITECTURE.md, quando web-site estiver ativo
SITE_STYLE_GUIDE.md, quando web-site estiver ativo
CONTACT_STACK.md, quando contact-protocol estiver ativo
governanca/PAUTA_EDITORIAL.md, quando publication estiver ativo e houver Artigos/fila editorial futura
```

**Gate A3:** cada função essencial — regras, pedidos, estratégias, estado e planejamento — possui fonte persistente.

### Etapa A4 — Geração do AGENTS

Derivar o `AGENTS.md` a partir de:

1. `AGENTS_KERNEL.md` vigente;
2. perfil específico do projeto;
3. módulos ativados;
4. regras locais comprovadas.

Registrar `generated_from_kernel`.

**Gate A4:** nenhuma regra setorial foi incorporada ao kernel; nenhuma regra universal obrigatória foi omitida sem justificativa.

### Etapa A5 — Verificação

Verificar:

- arquivos realmente existentes;
- referências internas válidas;
- compatibilidade com ferramentas disponíveis;
- ausência de confirmações falsas;
- estado e próximo passo persistidos;
- se `web-site` estiver ativo: menu, Home, Mapa do Site, identidade, mobile e separação público/interno;
- se `contact-protocol` estiver ativo: stack aprovada, isolamento por projeto e estado real do teste end-to-end;
- se `publication` + Artigos/fila editorial estiverem ativos: `governanca/PAUTA_EDITORIAL.md` existente ou decisão `NOT_APPLICABLE` justificada, e ausência da pauta no artefato público.

**Gate A5 obrigatório:** executar `python tools/project_creation_gate.py --project-root <REPO_LOCAL> --route A --gate bootstrap`; resultado FAIL bloqueia a constituição técnica e o registro de PASS. Nenhum comando não executado pode ser declarado aprovado. Para migração legítima usar `--route B`, preservando EAs existentes.

**Saída:** base técnica implantada ou relatório de pendências; o handoff operacional é tratado separadamente na Etapa A6.

---

### Etapa A6 — Transferência de titularidade operacional (Handoff)

**Autoridade:** `REQ-GLOBAL-20261010-014`, `ADR-GOV-0005`, `PRJ-000002:REQ-20261010-003`. A Rota A não termina com a suposição de que o Chat Global ou o Gerador acompanharão indefinidamente o Projeto.

Após concluir **A1–A5**, distinguir o encerramento técnico de dois resultados possíveis:
1. **Constituição técnica verificada**: `TECHNICAL_BOOTSTRAP_VERIFIED`, sem alegar recebimento do novo titular.
2. **Transferência operacional recebida**: `PROJECT_OPERATIONAL_HANDOFF_ACCEPTED`, somente após demonstração dos requisitos abaixo.

#### Requisitos mínimos

1. Confirmar `PRJ-NNNNNN`, repositório, missão aprovada (ou pendência expressa), `AGENTS.md`, `PROJECT_STATE.json`, roadmap, logs e commit/cópia canônica.
2. Identificar o **titular especializado** (instância que acompanha o domínio) e seu método de acesso; Codex/Work como executores não assumem automaticamente essa titularidade.
3. Se o acompanhamento **conversacional contínuo for atribuído ao ChatGPT**, exigir Projeto ChatGPT **próprio, comprovadamente criado e vinculado ao PRJ** (`B1_CHATGPT_PROJECT_BOUND`) e memória `C2` ou `C3` escolhida pelo responsável humano. O Gerador pode preparar instruções e contexto, mas **não pode afirmar que criou ou configurou contêiner ChatGPT** sem ação e recibo da plataforma.
4. Para Projeto essencialmente técnico **sem acompanhamento conversacional atribuído ao ChatGPT**, admitir `B0` com instância de engenharia/executor especializado explicitamente nomeado e validação de acesso e continuidade; não converter esse caso em obrigação genérica de contêiner.
5. Fornecer pacote mínimo de handoff com estado/identificadores, missão, fontes permitidas e revisões, classificação, executor aplicável, permissões e gasto, próxima entrega, critérios de aceite e riscos em aberto.
6. **Verificar recebimento**: em contêiner ChatGPT, abrir conversa **dentro do Projeto vinculado** e confirmar que ela recupera `AGENTS`, estado, identidade, fonte e limite de trabalho; registrar evidência de aceite. Uma resposta do Chat Global não substitui teste local.
7. Antes do aceite, registrar `SPECIALIZED_INSTANCE_REQUIRED`, `HANDOFF_PREPARED` ou `BINDING_VERIFICATION_PENDING` com pendências verdadeiras. Nunca promover `PROJECT_OPERATIONAL_HANDOFF_ACCEPTED` pela existência de um README, perfil ou chat avulso.

**Gate A6:** `PROJECT_OPERATIONAL_HANDOFF_ACCEPTED` **somente** com destinatário e prova verificáveis. Se faltar criação humana do Projeto ChatGPT, encerrar **somente** a Rota A técnica e manter handoff como `PENDING_HUMAN_PROJECT_CREATION`. Não reabrir a estratégia técnica anterior nem executar domínio especializado no lugar do titular.

**Fronteira de segurança:** o handoff não altera classificação, autorizações de `action_id`, permissões Git, custos, Work/Codex, modos C2/C3 ou regras do projeto; todas seguem seus gates próprios.

## 3. Rota B — Projeto existente

### Etapa B1 — Preservação e leitura

Antes de alterar qualquer arquivo:

1. localizar `AGENTS.md` existente;
2. localizar estado, roadmap, decisões e logs;
3. preservar a versão anterior recuperável;
4. registrar o estado comprovado.

**Gate B1:** nenhuma alteração destrutiva ocorreu antes da preservação.

### Etapa B2 — Inventário

Inventariar:

- regras existentes;
- arquivos canônicos;
- estratégias autônomas comprováveis;
- mecanismos de persistência e versionamento;
- integrações e ferramentas;
- lacunas documentais;
- arquitetura pública existente, menus, Home, Mapa do Site, CSS/tokens e responsividade;
- formulário de contato, provedores, IDs/configuração pública, e-mail institucional, protocolo e evidências de teste;
- pauta editorial interna/backlog de conteúdo, quando houver Artigos ou fila editorial futura, incluindo verificação de que não está exposta no Site Público.

Backfill de estratégia somente com evidência persistente.

### Etapa B3 — Classificação das regras

Classificar cada regra relevante como:

- `UNIVERSAL`;
- `ESPECÍFICA DO PROJETO`;
- `MÓDULO REUTILIZÁVEL`;
- `DUPLICADA`;
- `CONFLITANTE`;
- `OBSOLETA`, somente com fundamento explícito.

### Etapa B4 — Comparação com kernel

Comparar com `AGENTS_KERNEL.md` vigente e produzir relatório de auditoria a partir de `templates/AUDIT_REPORT.example.md`.

**Gate B4:** lacunas, conflitos e regras locais mais rigorosas estão explicitamente identificados.

### Etapa B5 — Plano de migração

Definir, sem executar ainda alterações destrutivas:

- o que será preservado;
- o que será acrescentado;
- o que será reestruturado;
- o que será removido e por quê;
- módulos que serão ativados;
- arquivos auxiliares que serão criados;
- riscos e rollback.

### Etapa B6 — Implantação controlada

Aplicar a migração progressivamente:

```text
ALTERAR
↓
SALVAR
↓
VERIFICAR
↓
VERSIONAR
↓
ATUALIZAR ESTADO
↓
CONTINUAR
```

### Etapa B7 — Verificação pós-migração

Confirmar:

- `AGENTS.md` preserva regras específicas válidas;
- kernel vigente foi aplicado corretamente;
- logs e estado são reconstruíveis;
- não houve regressão comprovada;
- próximo passo está persistido.

**Saída:** migração documental concluída ou pendências; o recebimento operacional exige B8 quando aplicável.

---

### Etapa B8 — Verificação da titularidade após migração

Após B1–B7, aplicar os requisitos e o gate de **A6** à instância especializada **destinatária** da alteração. Preservar titularidade local comprovada e não impor novo Projeto ChatGPT a uma arquitetura técnica em B0 que não delegue acompanhamento conversacional continuado.

- Se já existir Projeto ChatGPT vinculado (`B1`), verificar as instruções, o contexto e a recuperação do novo estado, sem converter `C2/C3` por inferência.
- Se uma migração pressupuser um novo titular, só transferir após aceite dele. Não interromper o titular atual sem sucessor válido.
- Uma migração documental pode ser encerrada com `MIGRATION_VERIFIED_HANDOFF_PENDING`; somente `PROJECT_OPERATIONAL_HANDOFF_ACCEPTED` comprova recebimento e continuidade.
- Não confundir alterar os arquivos do repositório com instalar ou ativar o ChatGPT Project, Codex, Work ou qualquer efeito externo.

**Gate B8:** `PROJECT_OPERATIONAL_HANDOFF_ACCEPTED` quando necessário e comprovado; senão `HANDOFF_PENDING` com dono, pendência e próxima ação explicitados.

## 4. Estados de saída obrigatórios

O Gerador deve distinguir:

```text
PROPOSTO
SALVO
VERSIONADO
ENVIADO AO REMOTO
IMPLANTADO
PUBLICADO, quando aplicável
```

Nunca inferir um estado a partir de outro.

## 5. Resultado mínimo de cada execução relevante

A saída deve informar, conforme aplicável:

- `project_code`, `project_name` e alias, quando houver;
- versão do kernel;
- módulos ativados;
- arquivos criados/alterados;
- estratégias registradas ou migradas;
- lacunas encontradas;
- estado real da persistência/versionamento;
- próximo passo lógico.


## 6. Gates transversais de conhecimento e melhoria

Em Rota A ou Rota B, antes do fechamento:

1. avaliar se o corpus exige `knowledge-index`; para Sites/projetos documentais persistentes, a resposta padrão é SIM;
2. criar/validar `IMPROVEMENT_LOG.jsonl`;
3. verificar se oportunidades materiais identificadas durante a execução foram comunicadas e registradas;
4. quando `research` e produção acadêmica brasileira forem pertinentes, incluir BDTD/IBICT no protocolo;
5. executar o innovation check final e registrar propostas ainda não implementadas;
6. impedir exposição pública do índice e do log de melhorias, salvo decisão expressa em contrário.

## 7. Persistência padronizada dos testes de recebimento A6/B8

**Autoridade:** `PRJ-000002:REQ-20261010-007` e `REQ-GLOBAL-20261010-018`. **Motivação:** cinco Chats especializados arquivaram seus diagnósticos em pastas/nomenclaturas arbitrárias; ausência de convenção tornou a recuperação e a auditoria menos previsíveis.

### 7.1. Convenção canônica (obrigatória)

**Raiz:** `governanca/recebimentos/` **dentro do repositório do próprio Projeto**, não apenas no Gerador, na UI do ChatGPT ou no chat da Governança Global.

**Nome:** `AAAA-MM-DD-prj-NNNNNN-gate-a6.md` para Rota A ou `AAAA-MM-DD-prj-NNNNNN-gate-b8.md` para Rota B. Usar **data do teste**, código único real do Projeto e nome em letras minúsculas para compatibilidade entre sistemas. Exemplo:

```text
governanca/recebimentos/2026-10-10-prj-000023-gate-a6.md
governanca/recebimentos/2026-10-10-prj-000007-gate-b8.md
```

**Mais de um teste no mesmo dia:** nunca sobrescrever sem preservar evidências; usar `-r02`, `-r03` etc. antes de `.md` e registrar relação com a avaliação anterior. Se o relatório possuir informação S2+ ou for incompatível com Git público, **não publicar** no repositório público: registrar ali apenas ponteiro sanitizado, situação da evidência e destino privado autorizado sem vazar conteúdo.

### 7.2. Entregáveis obrigatórios do Gerador em cada handoff

Ao fornecer a instrução de Projeto ChatGPT e o prompt de homologação, incluir em ambos as seguintes regras:

1. A IA especializada deve ler efetivamente `AGENTS.md`, `PROJECT_STATE.json`, `ROADMAP.md`, `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl` e o Plano de Fases vigente; reunir apenas as evidências que realmente recuperou.
2. O prompt de teste deve solicitar **persistência do relatório no caminho exato acima** depois do diagnóstico, dentro do **próprio PRJ**, quando a ação for autorizada e o conector permitir escrita. Um prompt de teste que apenas peça apresentar respostas em chat é entrega **incompleta** do Gerador.
3. Registrar primeiro o pedido de auditoria/persistência no `REQUEST_LOG.jsonl`, conforme Kernel e catálogo de executor; conferir mandato, política de sigilo e permissão de escrita. Quando escrita não for possível, entregar o Markdown completo para execução autorizada posterior, marcar `NOT_PERSISTED` e **não inventar URL ou commit**.
4. Nomear no relatório: `PRJ`, EA, Fase, Gate, data, repositório/branch, fontes (versões e commits quando obtidos), matriz de requisitos, pendências, distinção entre **teste documental** e **aceite**, próximo passo e ações efetivamente realizadas.
5. Após gravar, realizar leitura remota de retorno; incluir link canônico na resposta ao usuário. **Ter arquivo versionado não equivale à configuração C2/C3, vínculo B1 ou `PROJECT_OPERATIONAL_HANDOFF_ACCEPTED`.**
6. Para evolução de um relatório já versionado, acrescentar novo recibo datado e manter histórico. Se arquivos anteriores estiverem em outras pastas, migrar para `governanca/recebimentos/` com links Markdown relativos corrigidos, preservando os URLs antigos mediante ponteiros quando necessário. Não destruir fontes ou história Git por conveniência.
7. O `AGENTS.md` especializado deve indicar esta convenção; o adaptador de plataforma em `adaptadores/chatgpt/INSTRUCOES.md` continua fonte recuperável, mas não se sincroniza automaticamente com a interface ChatGPT. Mudança de regra depende de versionamento e verificação.

### 7.3. Evidência mínima de conclusão do ciclo

O Gerador só declara a entrega do **pacote de homologação** completa se entregar, em conjunto: Instruções especializadas, prompt de teste com caminho, diagnóstico recuperável, regra de persistência, fonte/código de referência e distinção entre gates previstos e aceites.

Para os PRJ-000007/000008/000021/000022/000023, os relatórios **de 10/10/2026** foram reorganizados nos caminhos acima, com versões integrais, ponteiros legados e índice `governanca/recebimentos/README.md`. Seus resultados permanecem `HANDOFF_PENDING` / `NOT_ACCEPTED` conforme cada documento; não levantar gate por movimentação documental.

**Critério anti-loop:** não abrir nova EA global exclusivamente para redistribuir arquivos; priorizar a retomada das entregas locais após rastreabilidade e segurança.

### 7.4. Precedente SCIV Sob Demanda em adaptadores ChatGPT (issue #5)

Autoridade: issue #5 / ADR-GOV-0009, substitui gatilho automático da issue #4; demais regras permanecem. Opt-in por sciv_bootstrap.enabled=true e mode=ON_DEMAND, evidências e caixas locais.

1. Conferir perfil, PRJ/repo, capacidade de leitura, provisionamento e operational_ref, sem criar vínculo ou permissões.
2. Comparar adaptador local/handoff; compor offline somente bloco SCIV_BOOTSTRAP_BEGIN/END, preservando todos os demais bytes. Não sobrescrever evolução local por fonte antiga; perfil não habilitado permanece intacto.
3. Materializar leitura SOMENTE sob solicitação explícita do titular. Não consultar em Oi, pergunta acadêmica ou tarefa normal. Identificar pendências/versões/histórico quando solicitado, separar falha de acesso de vazio, preservar GVC/PEP.
4. Resposta real exige ferramenta/política e readback; entrada arquivada somente após tratamento rastreável. G0 consulta saída a pedido e arquiva depois de ciência/decisão/handoff confirmado. Pendência precisa owner/decisão/ref. Não confundir arquivamento e execução.
5. Testar preservação/dedup/ref/mode/integridade; publicar engenharia em branch e conferir commit/ref/bytes. Preservar provas anteriores no Git/audits.
6. Titular compara/instala manualmente arquivo integral no campo Instruções nativo. Nova conversa acadêmica normal deve comprovar ausência de chamadas SCIV; depois pedir leitura explicitamente e conferir fila/histórico/correlação. Sem UI manter NATIVE_INSTRUCTIONS_PENDING / REAL_CONVERSATION_VALIDATION_PENDING. Sem merge/C3/A6/B8/F2/F3 automático.

Após integração humana autorizada, atualizar operational_ref e regenerar/confrontar pacote sem deixar fontes concorrentes. Não criar EA/creds/gastos/agendas.

## SCIV Essencial Sob Demanda — precedência issue #5

Aplicar modules/sciv-essential.md somente opt-in com mode=ON_DEMAND e evidências/capacidade/caixas locais. tools/sciv_bootstrap.py compõe apenas o bloco gerenciado, preserva demais bytes e impede reintrodução automática. Leitura somente a pedido do titular, nunca em tarefas normais. Arquivamento bilateral requer tratamento/readback; histórico não é fila. GVC/PEP preservados. Instalação nativa manual e conversa real pendentes; evidências anteriores permanecem cortes históricos, sem novos grants/EA/C3/main/gatilhos.


## 8. Contrato integral de criação e recebimento especializado — EA-000002-000027

**Autoridade:** pedido humano de 11/10/2026, EA-000002-000027, programa global EA-000000-000034. **Regra bloqueante:** nenhum Projeto persistente novo inicia trabalho substantivo ou é declarado tecnicamente constituído sem uma primeira **Estratégia Autônoma com Plano de Fases**, evento CREATED no Strategy Log, pedido, referência no estado e Roadmap, código resolvido pelo registry, readback e validação determinística. A Rota B preserva genealogia e EAs históricas, sem recriar 000001.

### 8.1. Ordem obrigatória na Rota A

1. Identificar missão aprovada, PRJ e namespace sem colisão; persistir pedido e decidir executor/repositório/classificação/custo.
2. **Criar EA-PPPPPP-000001 e Plano de Fases antes do trabalho substantivo**, com código, fases F-PPPPPP-000001-FFF, gates e owners; usar `templates/PROJECT_CREATION_EA.example.md`. Persistir CREATED, request, estado/Roadmap e registro global por readback real.
3. Gerar AGENTS/Kernel/perfil/módulos e arquivos do repositório; decidir explicitamente `sciv-essential` como ATIVADO, PENDENTE_DE_EVIDENCIA ou NAO_APLICAVEL, sem habilitar por padrão.
4. Após A3–A5, executar `python tools/project_creation_gate.py --project-root <REPO_LOCAL> --route A --gate bootstrap`. O script deve ser executado em ambiente autorizado e seu resultado persistido; mera existência do arquivo não equivale a PASS. Qualquer FAIL impede `TECHNICAL_BOOTSTRAP_VERIFIED`.
5. Ao terminar a constituição técnica, fechar apenas seu escopo, preservando handoff A6 pendente quando o Projeto ChatGPT não estiver validado. A Rota B usa `--route B` sem reescrever EAs de origem.

### 8.2. Continuidade SCIV condicionada a opt-in

6. Para Projeto ChatGPT especializado B1, preparar Instruções **integrais** versionadas em `adaptadores/chatgpt/INSTRUCOES.md` e classificação C2/C3 com evidência; nunca presumir configuração nativa.
7. Se o titular autorizou SCIV, abrir **EA local própria com Plano de Fases** (ou vincular fase explicitamente abrangida por EA local já admitida), usando `templates/SCIV_ROLLOUT_EA.example.md`. Provisionar no **repositório do PRJ** o estado `comunicados/SCIV_STATE.json`, as caixas bilaterais `governanca-geral/...` e `ia-especializada/...`, e históricos; modo obrigatoriamente `ON_DEMAND` e `operational_ref=main`. Não habilitar polling, cron ou consulta em conversa comum.
8. Compor **apenas** o bloco gerenciado `SCIV_BOOTSTRAP_BEGIN` via `tools/sciv_bootstrap.py`, preservando os demais bytes das Instruções. Fazer teste técnico/readback e executar `--gate sciv` do validador. Esse gate prova somente os arquivos, não a instalação nativa.

### 8.3. Teste de recebimento APÓS instalar as Instruções — distinto do SCIV

9. Titular substitui **manualmente** as Instruções nativas pelo **arquivo integral** `main` e confirma a versão; registrar `NATIVE_INSTRUCTIONS_HUMAN_ATTESTED`, com limites de observabilidade. GitHub não altera as Instruções da interface ChatGPT.
10. Somente **após** a instalação, a Governança Geral publica na caixa local `comunicados/governanca-geral/mensagens/` o Comunicado `POST_NATIVE_INSTRUCTIONS_RECEIPT_TEST`, referindo **o teste A6 ou B8 específico que já existia**, relatório histórico de 10/10, commit da nova versão integral, PRJ/EA/gate, id/correlação, critérios, destino do novo relatório e classificação de segurança. Usar `templates/SCIV_POST_NATIVE_RECEIPT.example.json`. Publicação Git não inicia conversa.
11. O titular, no Projeto ChatGPT destinatário, envia apenas: **«Leia os Comunicados da Governança Geral e execute o teste de recebimento operacional A6/B8 destinado a este Projeto. Registre e encaminhe a resposta pelo SCIV.»** Não entregar quatro prompts extensos para copiar. A IA especializada verifica mensagem/identidade/versão/GVC/PEP, consulta fontes de seu PRJ, responde criticamente, e só escreve o relatório e resposta correlacionada se a ferramenta/autorizações permitirem.
12. Persistir **novo** `governanca/recebimentos/AAAA-MM-DD-prj-NNNNNN-gate-a6|b8.md` (usar `-r02` para colisão), mantendo histórico intocado. Sem escrita autorizada, `WRITE_BLOCKED`; manter mensagem ativa. G0 recebe por solicitação explícita, trata e arquiva bilateralmente após recibos reais. **A6/B8 só é aceito por seus próprios requisitos**, não por sucesso do transporte SCIV.

### 8.4. Testes do mecanismo SCIV e encerramento

13. Em separado, verificar **não leitura SCIV** em conversa acadêmica normal, **leitura expressamente solicitada**, autenticidade/correlação, resposta real e arquivamento bilateral. Classificar `VERIFIED`, `HUMAN_ATTESTED`, `NOT_VERIFIED` e `BLOCKED` sem inventar ferramenta.
14. Se houver evidências reais, preencher `governanca/recebimentos/RECEIPT_EVIDENCE.json` conforme template; executar `--gate post_native` quando aplicável. O script só confere consistência documental; não autentica ação humana nem aceita A6/B8 automaticamente.
15. Encerrar as EAs/Planos somente com gates, readback e registro local/global reconciliado. Qualquer pendência de instalação, recibo, ferramenta, C3, Pages ou PEP fica persistida com owner e próxima ação — não desaparece porque outra estratégia começou.

**Quatro destinatários do rollout:** PRJ-000022/A6; PRJ-000023/A6; PRJ-000007/B8; PRJ-000008/B8. O PRJ-000021 foi o piloto SCIV concluído e não é quinto destinatário pendente. Reutilizar os roteiros de `governanca/recebimentos/` do respectivo Projeto, sem republicar resultados históricos como execução nova.

**Gates independentes:** `EA_INICIAL_VALIDATED` ≠ `SCIV_REPOSITORY_READY` ≠ `NATIVE_INSTRUCTIONS_HUMAN_ATTESTED` ≠ `A6_B8_TEST_AFTER_INSTALLATION` ≠ `SCIV_BEHAVIOR_VERIFIED` ≠ `PROJECT_OPERATIONAL_HANDOFF_ACCEPTED`. O mero transporte não outorga autorização. Sem custo novo, credenciais, mudanças nativas automáticas ou promoção de PEP live.

## 9. Publicação de Sites como entrega técnica do Gerador, governada por EA local

**Autoridade:** solicitação expressa de 11/10/2026 (REQ-20261011-009), como aditamento da EA-000002-000027 durante sua F005. **Finalidade:** nenhuma criação de Projeto com Site Público autorizado pode perder a identidade visual, os padrões e o percurso de publicação; a existência de um Projeto ChatGPT ou o SCIV não substitui a EA de Site.

### 9.1. Separação de responsabilidades (sem duas autoridades para a mesma ação)

- **Titular humano:** aprova se haverá Site, finalidade, exposição pública, custo, identidade proposta quando exigir escolha, e executa configurações administrativas de GitHub Pages não acessíveis pelo executor autorizado. A criação de Projeto documental não autoriza automaticamente criar Site.
- **Gerador de Agents / equipe de engenharia coordenada por ele:** autoridade técnica de padronização e entrega do Site quando houver mandato. Seleciona módulos, define arquitetura, gera ou atualiza `SITE_ARCHITECTURE.md`, `SITE_STYLE_GUIDE.md`, tokens/CSS, templates e arquivos públicos, prepara build, testa navegação/acessibilidade/segurança e verifica deployment/HTTP quando possível. Pode designar **Codex** como executor de código ou Chat para documentação de acordo com catálogo de capacidades/permissões; "responsável" não implica que o Gerador tenha acesso administrativo à conta.
- **IA especializada e Projeto PRJ destinatário:** titularidade da missão, fontes, critérios substantivos, revisão/aceite de conteúdo e estado da EA local. Publicação não transfere autoria editorial para a Governança Geral. O Gerador não altera escopo ou tese da IA.
- **Governança Geral:** governa interfaces, descoberta, registro dual e reconciliação de gates; não executa Sites dos quatro Projetos dentro da EA global SCIV-034.

### 9.2. Regra vinculante da Estratégia Autônoma de Site

1. **Na Rota A**, após registrar a primeira EA de constituição e decidir módulos, documentar `web-site` como `ATIVADO` (mandato comprovado), `PENDENTE_DE_EVIDENCIA` ou `NAO_APLICAVEL`. Se `ATIVADO`, **criar ou vincular EA local própria de Site com Plano de Fases**, mediante mandato e namespace, usando `templates/WEBSITE_PUBLICATION_EA.example.md` e evento `CREATED`; não deixar o trabalho de publicação como item implícito da EA de constituição já encerrada. Registrar dependência no `ROADMAP.md` e catálogo dual. Estado separado `governanca/SITE_PUBLICATION_STATE.json` quando a implantação avançar.
2. **Na Rota B**, respeitar EAs de Site já existentes e suas fases; não criar substituta apenas para renumerar. Exemplos: `EA-000007-000002` e `EA-000008-000002`, F004 bloqueada por configuração Pages. Complementar tokens e critérios apenas por mudança autorizada na própria EA sem concluir retroativamente o Gate F004.
3. O Gerador gera e executa tecnicamente as fases de Site **somente com escopo e permissões suficientes**, como executor central de padrões; o conteúdo substantivo e o aceite pertencem ao PRJ. Sem mandate `ATIVADO` não criar `docs/`, CSS ou publicar URL.
4. **Identidade visual exclusiva:** definir design tokens por Projeto (`background`, `surface`, `text`, `primary`, `secondary`, `accent`, `border`, `focus`) em `SITE_STYLE_GUIDE.md` e CSS/manifesto próprio; registrar referência da paleta e comparar com projetos do portfólio para evitar repetição integral não justificada. **Não fixar cores universais**, usar o mesmo sistema de componentes acessíveis adaptado à semântica institucional. Contraste de texto normal contra superfícies ≥4,5:1; títulos grandes ≥3:1; foco visível; cor não deve ser único sinal. O validador local consegue verificar contraste de `text` com `background` e `surface` nos tokens hex, mas a comparação visual de sites e revisão de cores interprojetos exigem auditoria distinta.
5. **Gate de pré-publicação:** fonte em pasta pública aprovada, menu global, Home e Mapa do Site, links, mobile, CSS/tokens, contraste, revisão de conteúdo e S0/S1 publicável, sem expor governança interna; commit e readback. Executar `python tools/project_creation_gate.py --project-root <REPO> --route A|B --gate site`. `PASS` valida **evidência documental local**, não prova que o site está no ar.
6. **Publicação efetiva:** uma autoridade com acesso configura Pages/hosting e confirma deploy; Gerador/Codex verifica URL realmente publicada, resposta HTTP, navegação, mobile e ausência de vazamento. Registrar `PUBLIC_SITE_VERIFIED` **somente** com prova da URL pública, deployment e conteúdo servido. Falta de configuração administrativa → `WAITING_HUMAN_PAGES_CONFIG`, com owner e próximo passo na EA, sem criar nova EA artificial.
7. **Encerramento e continuidade:** o Gerador atualiza recibo de site, fontes SHA, relatório, estado e log locais e catálogo global, sem marcar Fase/gate concluído sem prova real. `TECHNICAL_BOOTSTRAP_VERIFIED`, `SITE_SOURCE_STAGED`, `PAGES_CONFIGURED` e `PUBLIC_SITE_VERIFIED` são estados distintos.

### 9.3. Compatibilidade com SCIV e Instruções

Site é uma frente técnica **independente**, embora a EA do Projeto possa declarar dependências entre site, SCIV e handoff. Os testes A6/B8 por Comunicados, após instalação das Instruções, **não dependem de Pages** a menos que o próprio teste tenha esse requisito específico, e não podem concluir a publicação. O Gerador registra ambas as EAs e pendências em separado, sem múltiplas sessões humanas para copiar longos roteiros.
