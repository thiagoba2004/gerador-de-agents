# Estratégia — Regra reutilizável de triplicidade editorial

**strategy_id:** `STRAT-GDA-20260918-001`  
**project_id:** `GDA`  
**Data:** 18/09/2026  
**Estado:** CONCLUÍDA

## Objetivo

Transformar a lacuna observada no Classe e Massas em uma regra reutilizável do Gerador de Agents para projetos editoriais/publicáveis.

## Delimitação

A regra pertence ao módulo `publication`, não ao kernel universal. Projetos sem publicação editorial não devem ser obrigados a criar HTML e JSON para todo texto.

Quando o módulo `publication` estiver ativado e o perfil do projeto adotar a triplicidade editorial, cada texto editorial/publicável deverá possuir:

- `.md` como fonte textual canônica;
- `.html` como artefato de publicação;
- `.json` como metadados/estrutura interoperável.

Exceções exigem decisão documentada.

## Plano de Fases

### Fase 1 — Registro e delimitação
Pedido e estratégia persistidos.

### Fase 2 — Regra modular
Atualizar `modules/publication.md` com a obrigação e seus critérios de sincronização.

### Fase 3 — Geração
Atualizar `templates/AGENTS.example.md` para que o Gerador consiga materializar a regra em projetos aplicáveis.

### Fase 4 — Regra do próprio Gerador
Atualizar `AGENTS.md` do Gerador para registrar que módulos ativados devem propagar suas regras obrigatórias ao AGENTS gerado.

### Fase 5 — Verificação e fechamento
**CONCLUÍDA.** Artefatos relidos, commits confirmados e regra incorporada ao Gerador 1.4.

## Resultado

- `AGENTS.md` do Gerador obriga propagação das regras modulares;
- `modules/publication.md` exige `.md` + `.html` + `.json`;
- `templates/AGENTS.example.md` materializa a obrigação quando `publication` estiver ativado;
- `CHANGELOG.md` registra a versão 1.4;
- perfil do Classe e Massas atualizado para `AGENTS.md` v2.0.
