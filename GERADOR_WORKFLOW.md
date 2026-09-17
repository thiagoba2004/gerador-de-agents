# GERADOR WORKFLOW — PROCEDIMENTO OPERACIONAL

**project_id:** `GDA`  
**kernel_version:** `1.2`

Este documento transforma a arquitetura do Gerador de Agents em um procedimento executável e reproduzível.

## 1. Regra de entrada

Antes de qualquer diagnóstico substantivo:

1. registrar o pedido no `REQUEST_LOG.jsonl` do projeto em que o Gerador estiver operando;
2. confirmar tecnicamente o registro;
3. identificar ou registrar a Estratégia Autônoma correspondente;
4. identificar o Plano de Fases e a fase atual;
5. somente então executar a rota aplicável.

## 2. Rota A — Novo projeto

### Etapa A1 — Diagnóstico mínimo

Identificar e registrar:

- nome e finalidade;
- `project_id` estável;
- repositório ou fonte persistente;
- existência ou não de Git/versionamento;
- formatos canônicos;
- ferramentas e integrações disponíveis;
- riscos de perda, publicação, segurança e operações destrutivas;
- tipos de entregas;
- restrições conhecidas.

**Gate A1:** nenhuma capacidade ou integração relevante foi inventada; todas as fontes persistentes conhecidas estão identificadas.

### Etapa A2 — Seleção de módulos

Aplicar `MODULE_SELECTION.md`. Cada módulo deve receber um dos estados:

- `ATIVADO`;
- `NÃO APLICÁVEL`;
- `PENDENTE DE EVIDÊNCIA`.

Toda ativação deve ter justificativa rastreável.

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
- estado e próximo passo persistidos.

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
- lacunas documentais.

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

- `project_id`;
- versão do kernel;
- módulos ativados;
- arquivos criados/alterados;
- estratégias registradas ou migradas;
- lacunas encontradas;
- estado real da persistência/versionamento;
- próximo passo lógico.
