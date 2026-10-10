# GERADOR WORKFLOW — PROCEDIMENTO OPERACIONAL

**project_code:** `PRJ-000002`  
**project_alias:** `GDA`  
**project_id legado:** `GDA`  
**kernel_version do workflow original:** `1.4` (histórico); **kernel em uso pelo Gerador:** `1.11`.

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
