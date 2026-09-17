# Templates

Modelos reutilizáveis para os arquivos auxiliares gerados ou exigidos pelo Gerador de Agents.

Todo template deve ser genérico, não conter dados específicos de um projeto real e indicar claramente os campos obrigatórios.

Templates atualmente disponíveis:

- `REQUEST_LOG.example.jsonl` — registro sequencial e persistente de pedidos;
- `STRATEGY_LOG.example.jsonl` — eventos append-only de Estratégias Autônomas;
- `PROJECT_STATE.example.json` — fotografia do estado corrente;
- `ROADMAP.example.md` — Plano de Fases;
- `AGENTS.example.md` — estrutura-base de `AGENTS.md` derivada do kernel e do perfil do projeto;
- `AUDIT_REPORT.example.md` — relatório padronizado para auditoria e migração de projeto existente;
- `PROJECT_PROFILE.example.json` — perfil estruturado do projeto, módulos, riscos, ferramentas e estado de migração.

A existência de um template não obriga sua utilização literal. O Gerador deve adaptar a estrutura ao projeto concreto sem eliminar as funções essenciais de governança, rastreabilidade, persistência e continuidade.
