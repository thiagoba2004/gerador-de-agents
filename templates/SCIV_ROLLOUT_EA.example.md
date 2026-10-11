# EA-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}} — Implantação SCIV em {{PROJECT_NAME}}

**Projeto:** {{PROJECT_CODE}}. **Pedido:** {{REQUEST_ID}}. **EA:** EA-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}} (confirmar livre). **Status:** PLANNED, opt-in ON_DEMAND.

1. F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-001 — Mandato, autorização, B1/C3 e pré-requisitos; gate SCIV_ADMITIDO.
2. F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-002 — Caixas bilaterais, estado e classificação, commit/readback; gate CAIXAS_VERSIONADAS.
3. F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-003 — Adaptador integral, bloco gerenciado e preservação da missão; gate INSTRUCOES_VERSIONADAS.
4. F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-004 — Testes técnicos, idempotência e gate SCIV documental; gate SCIV_REPO_VERIFICADO.
5. F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-005 — Titular instala Instruções nativas; G0 envia teste A6/B8 histórico por Comunicado; IA especializada responde e salva relatório/recibo novo; gate A6_B8_POS_INSTALACAO_CLASSIFICADO.
6. F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-006 — Testes funcionais SCIV distintos, tratamento/arquivamento bilateral, readback e aceite separado; gate SCIV_COMPORTAMENTO_CLASSIFICADO.

**Sem simular respostas nem assumir aceite do Projeto.** Se a instalação humana ou as ferramentas faltarem, persistir bloqueio e próximo passo.

## Ações vinculadas às Fases

Ao instanciar esta EA, criar matriz `estrategias/EA-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-actions.json` usando o modelo `templates/EXECUTION_ACTION_PLAN.example.json`, preenchendo uma ou mais ações reais **para cada fase**, com responsável, executor, ferramenta, ambiente, autorização, fonte/destino, prova e gate. Validar `tools/validate_execution_action_plan.py` antes de declarar READY; duas ações de exemplo não cobrem automaticamente seis fases. `PASS` não substitui autorização ou execução comprovada.
