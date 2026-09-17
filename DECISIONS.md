# DECISIONS — GERADOR DE AGENTS

## ADR-001 — Repositório independente

**Data:** 17/09/2026  
**Estado:** ACEITA

O Gerador de Agents será mantido fora do repositório Classe e Massas, em `thiagoba2004/gerador-de-agents`.

**Motivo:** o Gerador é infraestrutura reutilizável para múltiplos projetos e não deve ficar subordinado a um domínio específico.

---

## ADR-002 — Arquitetura em três camadas

**Data:** 17/09/2026  
**Estado:** ACEITA

A arquitetura será composta por:

1. `AGENTS_KERNEL.md` — núcleo universal;
2. `profiles/` — perfil de cada projeto;
3. `modules/` — módulos especializados reutilizáveis.

**Consequência:** regras setoriais não entram no kernel sem demonstração de universalidade.

---

## ADR-003 — Registro obrigatório de pedidos antes do processamento

**Data:** 17/09/2026  
**Estado:** ACEITA

A ordem operacional obrigatória passa a ser:

```text
registrar pedido
→ confirmar tecnicamente
→ informar “Pedido registrado.”
→ informar leitura/análise/providências
→ executar
```

Esta decisão substitui a ordem anterior da instrução canônica v1.1, que previa uma mensagem antes do registro persistente.

---

## ADR-004 — Estratégias com identidade estável e log append-only

**Data:** 17/09/2026  
**Estado:** ACEITA

Toda Estratégia Autônoma possuirá `strategy_id` estável e eventos append-only em `STRATEGY_LOG.jsonl`. Cada projeto possuirá `project_id` estável.

O `STRATEGY_REGISTRY.jsonl` será apenas índice agregado reconstruível; o log local permanece fonte primária.

---

## ADR-005 — Plano de Fases obrigatório

**Data:** 17/09/2026  
**Estado:** ACEITA

Toda Estratégia Autônoma deverá possuir Plano de Fases explícito, com estado, objetivo e gate quando aplicável.

---

## ADR-006 — Git como memória histórica preferencial

**Data:** 17/09/2026  
**Estado:** ACEITA

Quando disponível, Git será a memória histórica preferencial. Estados como produzido, salvo, versionado, enviado ao remoto e publicado/implantado permanecem distintos.
