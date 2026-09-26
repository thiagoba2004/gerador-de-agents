# GERADOR WORKFLOW — PROCEDIMENTO OPERACIONAL

**project_code:** `PRJ-000002`  
**project_alias:** `GDA`  
**project_id legado:** `GDA`  
**kernel_version:** `1.4`

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

**Saída:** projeto implantado ou relatório explícito das pendências restantes.

---

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

**Saída:** migração concluída ou lista explícita de itens não implantados.

---

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
