# EA-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}} — Identidade visual e publicação do Site de {{PROJECT_NAME}}

**Projeto:** {{PROJECT_CODE}}. **EA:** EA-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}} (verificar código livre e registro local/global). **Pedido de autorização do Site:** {{REQUEST_ID}}. **Executor técnico responsável:** Gerador de Agents, com Codex/Chat conforme catálogo. **Responsável editorial:** IA especializada do Projeto. **Configuração administrativa:** titular/perfil com permissão real.

**Condição de abertura:** `web-site=ATIVADO` com mandato comprovado e destino de publicação aprovado. Sem isso, registrar `PENDENTE_DE_EVIDENCIA` e não criar/publicar. Sites já com EA não recebem duplicata; continuar estratégia vigente.

## Plano de Fases — cada gate exige recibo próprio

1. **F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-001 — Escopo e autorização:** objetivo do Site, público, repositório/host, classificação, custo, mandatos, executor e competências. **Gate:** `SITE_MANDATE_RECORDED`.
2. **F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-002 — Arquitetura e identidade própria:** `SITE_ARCHITECTURE.md`, `SITE_STYLE_GUIDE.md`, Home/menu/Mapa do Site, tokens de cor por PRJ, comparação de paletas, tipografia, acessibilidade e responsividade. **Gate:** `SITE_VISUAL_SYSTEM_REVIEWED`.
3. **F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-003 — Conteúdo e implementação:** revisão especializada das fontes, arquivos públicos/CSS/templates, governança não exposta, rotas e links; commit e readback. **Gate:** `SITE_CONTENT_AND_SOURCE_STAGED`.
4. **F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-004 — Teste pré-publicação:** checar integridade da EA/Plano, `governanca/SITE_PUBLICATION_STATE.json`, cores/contraste, rotas, responsividade e segurança; executar `project_creation_gate.py --gate site`. **Gate:** `SITE_TECHNICAL_PREFLIGHT_PASS` (somente documental/técnico).
5. **F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-005 — Publicação real:** configurar hosting/Pages por autoridade habilitada, comprovar pipeline, commit e URL, sem presumir acesso administrativo; se bloqueado `WAITING_HUMAN_PAGES_CONFIG`. **Gate:** `DEPLOY_CONFIGURATION_CONFIRMED`.
6. **F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-006 — Verificação pública/aceite:** HTTP, URL real, links, mobile, acessibilidade, fontes, independência e S0/S1 publicável; relatório e readback, encerramento local/global. **Gate:** `PUBLIC_SITE_VERIFIED` somente por evidência real.

**Modelo de estado:** `templates/SITE_PUBLICATION_STATE.example.json`. Nenhuma conclusão de HTTP é inferida de arquivo JSON ou de PASS estrutural. **Sites dos PRJ-000007/000008:** preservar EAs 000002 e bloqueio F004 de Pages em vez de duplicar este modelo. **PRJ-000022/000023:** sem autorização de site não criar estratégia/site por default.

## Ações vinculadas às Fases

Ao instanciar esta EA, criar matriz `estrategias/EA-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-actions.json` usando o modelo `templates/EXECUTION_ACTION_PLAN.example.json`, preenchendo uma ou mais ações reais **para cada fase**, com responsável, executor, ferramenta, ambiente, autorização, fonte/destino, prova e gate. Validar `tools/validate_execution_action_plan.py` antes de declarar READY; duas ações de exemplo não cobrem automaticamente seis fases. `PASS` não substitui autorização ou execução comprovada.
