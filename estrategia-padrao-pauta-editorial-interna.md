# EA-000002-000017 — Padrão reutilizável de pauta editorial interna

**Origem:** REQ-20260924-001  
**Objetivo:** incorporar ao Gerador de Agents um padrão reutilizável para projetos com publicação editorial: `governanca/PAUTA_EDITORIAL.md` como backlog interno de conteúdo, nunca exposto automaticamente no Site Público.

## Fases

1. **Modelo e semântica** — definir finalidade, campos, estados, prioridade e vínculo com Estratégias Autônomas.
2. **Módulo e template** — atualizar `modules/publication.md`, `templates/AGENTS.example.md` e criar `templates/PAUTA_EDITORIAL.example.md`.
3. **Workflow e AGENTS do Gerador** — tornar a criação/avaliação da pauta parte do bootstrap ou migração quando `publication` estiver ativo.
4. **Auditoria e release** — verificar consistência, não exposição pública e registrar a nova versão do Gerador.
