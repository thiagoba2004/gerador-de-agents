# Gerador de Agents

**Release operacional:** 1.24 · **Kernel:** 1.9

Infraestrutura para criar, auditar, adaptar, atualizar e versionar `AGENTS.md` de projetos novos ou existentes, com continuidade, persistência, rastreabilidade, estratégia, planejamento e verificabilidade.

## Entrada para qualquer Modelo de IA

Ao abrir este repositório pela primeira vez, ler nesta ordem:

1. `AGENTS.md` — regras específicas do próprio Gerador;
2. `AGENTS_KERNEL.md` — núcleo universal vigente;
3. `PROJECT_STATE.json` — estado corrente;
4. `STRATEGY_LOG.jsonl` — história das Estratégias Autônomas;
5. `ROADMAP.md` — Plano de Fases;
6. `GERADOR_WORKFLOW.md` — procedimento operacional para projeto novo ou existente;
7. `MODULE_SELECTION.md` — política de seleção de módulos;
8. `DECISIONS.md` e `CHANGELOG.md` — decisões e evolução.

Não reconstruir o estado a partir do chat quando essas fontes estiverem disponíveis.

## Arquitetura

```text
AGENTS.md
AGENTS_KERNEL.md
GERADOR_WORKFLOW.md
MODULE_SELECTION.md
REQUEST_LOG.jsonl
STRATEGY_LOG.jsonl
STRATEGY_REGISTRY.jsonl
PROJECT_STATE.json
ROADMAP.md
DECISIONS.md
CHANGELOG.md

templates/
modules/
profiles/
audits/
history/
```

### Kernel

`AGENTS_KERNEL.md` contém apenas garantias universais. Regras de domínio não devem entrar no kernel sem demonstração de universalidade.

### Perfis

`profiles/` registra características comprovadas de projetos auditados ou gerados: `project_id`, finalidade, fontes persistentes, versão do kernel e módulos aplicáveis.

### Módulos

`modules/` contém regras reutilizáveis ativadas apenas por evidência do projeto. O estado de cada módulo deve ser `ATIVADO`, `NÃO APLICÁVEL` ou `PENDENTE DE EVIDÊNCIA`.

### Sites e contato protocolado

Projetos com Site Público devem avaliar o módulo `web-site`. Sites com Fale Conosco protocolado devem avaliar `contact-protocol`.

O Gerador distingue:
- arquitetura pública de publicação editorial;
- identidade visual de infraestrutura de software;
- formulário implementado de backend realmente configurado;
- protocolo gerado de protocolo confirmado;
- semelhança visual de equivalência de stack técnica.

### Templates

`templates/` contém modelos para `AGENTS.md`, logs, estado, roadmap, perfil e relatório de auditoria/migração.

### Auditorias

`audits/` registra testes e auditorias de projetos existentes. Auditoria não equivale a implantação: nenhum projeto deve ser alterado automaticamente apenas porque foi auditado.

### Histórico

`history/` preserva proveniência e versões históricas relevantes do próprio Gerador.

## Regra operacional de entrada de pedidos

```text
REGISTRAR
↓
CONFIRMAR TECNICAMENTE
↓
INFORMAR “PEDIDO REGISTRADO.”
↓
INFORMAR LEITURA / ANÁLISE / PROVIDÊNCIAS
↓
EXECUTAR
```

## Estado atual

Consultar `PROJECT_STATE.json`. Ele é a fotografia corrente; não substitui o histórico em `STRATEGY_LOG.jsonl`.

## Primeiro teste real

O fluxo operacional foi testado de forma não destrutiva no projeto `thiagoba2004/classe-e-massas`. O resultado está em:

- `profiles/classe-e-massas.json`;
- `audits/classe-e-massas-2026-09-17.md`.

O repositório auditado não foi modificado durante o teste.

## Princípio máximo

> Nunca obrigar o usuário a pagar novamente, com tempo, energia ou recursos, por falha de memória, persistência, continuidade, planejamento ou verificação do Modelo de IA.
