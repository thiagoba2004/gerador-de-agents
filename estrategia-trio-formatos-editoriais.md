# Estratégia — Regra reutilizável de triplicidade editorial

**strategy_id:** `STRAT-GDA-20260918-001`  
**project_id:** `GDA`  
**Data:** 18/09/2026  
**Estado:** EM EXECUÇÃO

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
Reler artefatos, confirmar commits e registrar conclusão.
