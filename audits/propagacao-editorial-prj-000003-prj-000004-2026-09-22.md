# Propagação do padrão editorial aos projetos piloto — 22/09/2026

## Origem

Padrão canônico: **EA-000002-000008 — Padrão editorial de Atualidade, Análise e Observação para Sites**.

## PRJ-000003 — Ações Judiciais

- estratégia local integradora: `EA-000003-000020`;
- navegação: `EDITORIAL_HUB`;
- rótulo: **Publicações**;
- subáreas: Notícias, Artigos e Observatório;
- páginas HTML auditadas: **20/20** com o novo item global;
- hrefs internos verificados: **540**;
- falhas de link: **0**;
- marcadores internos na camada pública: **0**;
- commit público: `6d161d0656f3053ea56d65b617d98c3a787f46e2`;
- workflow run: `35728854051` — **success**;
- estratégia local: **CONCLUÍDA**.

## PRJ-000004 — Planejamento Financeiro

- estratégia local integradora: `EA-000004-000035`;
- navegação: `EDITORIAL_HUB`;
- rótulo: **Publicações**;
- subáreas: Notícias, Artigos e Observatório;
- páginas HTML auditadas: **37/37** com o novo item global;
- hrefs internos verificados: **900**;
- falhas de link: **0**;
- marcadores internos na camada pública: **0**;
- commit público: `564775f06979052de485134f958011bece91aa11`;
- workflow run: `35729180230` — **success**;
- estratégia local: **CONCLUÍDA**.

## Consistência do Gerador

Os perfis dos dois projetos foram atualizados do estado `PLANEJADO/NAO_IMPLEMENTADO` para `IMPLEMENTADO_E_VERIFICADO`, com:
- menus públicos atuais;
- `navigation_mode=EDITORIAL_HUB`;
- `hub_label=Publicações`;
- três camadas marcadas como publicadas;
- rotas públicas registradas;
- referências às auditorias locais.

Também foram removidos do `PROJECT_STATE.json` débitos que já estavam comprovadamente superados: habilitação do GitHub Pages e migração de contato Forminit + EmailJS nos dois projetos.
