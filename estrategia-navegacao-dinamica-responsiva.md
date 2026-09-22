# EA-000002-000014 — Padrão reutilizável de navegação dinâmica responsiva

**Status:** CONCLUÍDA  
**Origem:** regressão identificada no PRJ-000001 / EA-000001-000023.

## Objetivo
Transformar o achado do Classe e Massas em regra reutilizável do Gerador para impedir que “responsividade” seja atendida apenas por empilhamento permanente ou rolagem lateral do menu.

## Plano de Fases
1. **FASE 01/03 [F-000002-000014-001] — Delimitação da lacuna** — CONCLUÍDA.
2. **FASE 02/03 [F-000002-000014-002] — Atualização do módulo web-site e template AGENTS** — CONCLUÍDA.
3. **FASE 03/03 [F-000002-000014-003] — Auditoria, registro agregado e fechamento** — CONCLUÍDA.

## Padrão consolidado
- menu denso em mobile deve preferir disclosure/recolhimento;
- botão semântico com `aria-controls` e `aria-expanded`;
- Escape fecha navegação aberta;
- submenu/hub acessível por teclado;
- progressive enhancement: sem JavaScript, navegação essencial continua acessível;
- rolagem horizontal não é solução padrão;
- auditoria deve testar fechado/aberto, submenu, teclado, toque e fallback.

## Origem comprovada
No Classe e Massas, a EA-000001-000022 removeu rolagem horizontal mas deixou o menu permanentemente empilhado. A EA-000001-000023 corrigiu o problema com MENU recolhível e Publicações como disclosure.
