# EA-000002-000015 — Padrão reutilizável de cards-link e navegação horizontal deslizante

**Status:** CONCLUÍDA  
**Origem:** derivada de PRJ-000001 / EA-000001-000024.

## Objetivo

Superar duas lacunas do padrão transversal de Sites:

1. distinguir visual e semanticamente cards clicáveis de cards informativos, reservando botões para ações reais;
2. deixar de tratar navegação recolhível como solução obrigatória para menus densos no mobile, reconhecendo a barra horizontal rolável/deslizante como padrão válido e, quando definida pela família visual do Site, canônico.

## Plano de Fases

1. **FASE 01/03 [F-000002-000015-001] — Delimitação da regressão normativa** — CONCLUÍDA.
2. **FASE 02/03 [F-000002-000015-002] — Atualização do módulo web-site e template AGENTS** — CONCLUÍDA.
3. **FASE 03/03 [F-000002-000015-003] — Auditoria, versionamento e fechamento** — CONCLUÍDA.

## Regra pretendida

- menu móvel pode adotar `HORIZONTAL_SCROLL` ou `COLLAPSIBLE_DISCLOSURE`, conforme arquitetura, densidade e padrão visual documentado;
- a escolha deve ser explícita e consistente no Site;
- em famílias de Sites que já usam barra horizontal rolável como AJ/PF, novos Sites alinhados a essa família devem preservar o mesmo paradigma, salvo decisão rastreável em contrário;
- overflow horizontal geral da página continua sendo falha; a rolagem pode existir apenas no componente deliberadamente rolável;
- cards de destino único devem ser links de bloco inteiro com diferenciação visual;
- botões devem representar ações, não simples navegação quando o próprio card pode ser o link.

## Fechamento

Padrão transversal implantado e auditado em `modules/web-site.md` e `templates/AGENTS.example.md`. A versão 1.17 admite `HORIZONTAL_SCROLL` ou `COLLAPSIBLE_DISCLOSURE` por decisão arquitetural explícita e formaliza cards-link para destinos únicos.
