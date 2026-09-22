# EA-000002-000015 — Padrão reutilizável de cards-link e navegação horizontal deslizante

**Status:** EM EXECUÇÃO  
**Origem:** derivada de PRJ-000001 / EA-000001-000024.

## Objetivo

Superar duas lacunas do padrão transversal de Sites:

1. distinguir visual e semanticamente cards clicáveis de cards informativos, reservando botões para ações reais;
2. deixar de tratar navegação recolhível como solução obrigatória para menus densos no mobile, reconhecendo a barra horizontal rolável/deslizante como padrão válido e, quando definida pela família visual do Site, canônico.

## Plano de Fases

1. **FASE 01/03 [F-000002-000015-001] — Delimitação da regressão normativa** — CONCLUÍDA.
2. **FASE 02/03 [F-000002-000015-002] — Atualização do módulo web-site e template AGENTS** — EM EXECUÇÃO.
3. **FASE 03/03 [F-000002-000015-003] — Auditoria, versionamento e fechamento** — AGUARDA implementação.

## Regra pretendida

- menu móvel pode adotar `HORIZONTAL_SCROLL` ou `COLLAPSIBLE_DISCLOSURE`, conforme arquitetura, densidade e padrão visual documentado;
- a escolha deve ser explícita e consistente no Site;
- em famílias de Sites que já usam barra horizontal rolável como AJ/PF, novos Sites alinhados a essa família devem preservar o mesmo paradigma, salvo decisão rastreável em contrário;
- overflow horizontal geral da página continua sendo falha; a rolagem pode existir apenas no componente deliberadamente rolável;
- cards de destino único devem ser links de bloco inteiro com diferenciação visual;
- botões devem representar ações, não simples navegação quando o próprio card pode ser o link.
