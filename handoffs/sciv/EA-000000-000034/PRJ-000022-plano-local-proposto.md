# PROPOSTA NÃO INSTANCIADA — EA-000022-000003 — SCIV Essencial Sob Demanda

**Estado:** DRAFT_IN_GENERATOR / NOT_CREATED_IN_TARGET / NOT_REGISTERED_AS_LOCAL_EA.
**Elaboração:** 11/10/2026; programa global `EA-000000-000034` (`F-000000-000034-003`), Gerador `EA-000002-000027` F005.
**Projeto:** `PRJ-000022` — Instituições Bancárias; **destino futuro:** `thiagoba2004/instituicoes-bancarias` (`main`).
**Código candidato a confirmar antes de CREATED:** `EA-000022-000003`. **Gate de recebimento:** A6.
**Fonte do mandato:** `REQ-GLOBAL-20261011-001`; SCIV só mediante opt-in explícito, `mode=ON_DEMAND`.

## Reconciliador prévio e isolamento

EA-000022-000002 está destinada à missão aprovada e handoff, ainda NÃO criada; constituí-la/reconciliá-la em fluxo separado antes de registrar 000003.

Missão de comparação documental de bancos aprovada em REQ-000022-20261010-002; não renovar aprovação nem inferir C3 nativo.

Não há mandato de Site; não criar Pages. Revalidar `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl`, `PROJECT_STATE.json`, `estrategias/` e catálogo dual na hora de criar; o código é **candidato**, não reservado nem executado. Não modificar estratégias de domínio ou site no fluxo SCIV.

## Plano de Fases local proposto

### F-000022-000003-001

- **Ação:** Reconciliar identificadores, mandato e perfil opt-in; registrar pedido/CREATED e Plano local apenas após releitura de logs; bloquear em colisão.
- **Responsável:** G0 + Gerador; **executor:** CHAT; **ferramenta:** GitHub connector; **ambiente:** Chat global / repositório do PRJ.
- **Gate:** `SCIV_ADMISSAO_REGISTRADA`; **prova:** commit/bytes/readback e recibo próprio, quando aplicável; **estado inicial:** NOT_STARTED.

### F-000022-000003-002

- **Ação:** Provisionar SCIV_STATE/caixas bilateralmente e históricos no próprio PRJ; validar classificação, integridade e readback.
- **Responsável:** Engenharia do PRJ (Codex); **executor:** CODEX; **ferramenta:** Codex CLI + Git/testes; **ambiente:** Codex no checkout do PRJ.
- **Gate:** `CAIXAS_VERSIONADAS`; **prova:** commit/bytes/readback e recibo próprio, quando aplicável; **estado inicial:** NOT_STARTED.

### F-000022-000003-003

- **Ação:** Integrar bloco SCIV ON_DEMAND no adaptador integral, sem mudar missão ou regras C3; comparar bytes anteriores.
- **Responsável:** Engenharia do PRJ (Codex); **executor:** CODEX; **ferramenta:** Codex CLI + Git/testes; **ambiente:** Codex no checkout do PRJ.
- **Gate:** `INSTRUCOES_VERSIONADAS`; **prova:** commit/bytes/readback e recibo próprio, quando aplicável; **estado inicial:** NOT_STARTED.

### F-000022-000003-004

- **Ação:** Executar testes offline, idempotência, autorização PEP, gate --gate sciv e readback remoto; relatar falhas.
- **Responsável:** Engenharia do PRJ (Codex); **executor:** CODEX; **ferramenta:** Codex CLI + testes; **ambiente:** Codex no checkout do PRJ.
- **Gate:** `SCIV_REPO_VERIFICADO`; **prova:** commit/bytes/readback e recibo próprio, quando aplicável; **estado inicial:** NOT_STARTED.

### F-000022-000003-005

- **Ação:** Obter instalação manual das Instruções atuais; enviar Comunicado real A6/B8 preexistente e coletar novo resultado especializado, sem reusar recibo histórico.
- **Responsável:** Titular + G0 + IA Especializada; **executor:** HUMAN + CHAT; **ferramenta:** UI nativa ChatGPT + GitHub connector; **ambiente:** Projeto ChatGPT específico + Chat global.
- **Gate:** `INSTALACAO_E_TESTE_DE_RECEBIMENTO_CLASSIFICADOS`; **prova:** commit/bytes/readback e recibo próprio, quando aplicável; **estado inicial:** NOT_STARTED.

### F-000022-000003-006

- **Ação:** Testar ausência de leitura espontânea, leitura expressa, resposta/recibo/correlação e arquivo bilateral após tratamento; concluir apenas gates provados.
- **Responsável:** G0 + IA Especializada + Titular; **executor:** CHAT + HUMAN; **ferramenta:** GitHub connector + UI ChatGPT; **ambiente:** Projeto especializado + Chat global.
- **Gate:** `SCIV_COMPORTAMENTO_CLASSIFICADO`; **prova:** commit/bytes/readback e recibo próprio, quando aplicável; **estado inicial:** NOT_STARTED.

## Gates de segurança e implantação

- Repositório público P2: só S0 ou S1 revisado; S2+ e credenciais proibidos. Sem novos custos ou gatilhos automáticos (cron, polling, webhooks).
- Criar a EA no PRJ apenas com `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl` (CREATED), `PROJECT_STATE.json`, `ROADMAP.md`, Plano local e matriz de ações completa, e depois registrar no catálogo dual de Governança Geral; nunca registrar esta proposta como `CREATED`.
- Adaptador integral em `adaptadores/chatgpt/INSTRUCOES.md` não altera Instruções nativas; instalação é ato humano.
- Teste A6 pós-instalação utiliza o relatório histórico `governanca/recebimentos/2026-10-10-prj-000022-gate-a6.md` como **fonte**, não como nova evidência de sucesso; resposta verdadeira e nova versão do relatório são obrigatórias.
- Teste SCIV sob demanda é independente do A6; publicar mensagem não executa ação, não chama a IA automaticamente, não confere PEP live e não autoriza alteração substantiva.
- Se ferramentas/permissões não disponíveis: `BLOCKED`, executor responsável e referência do trabalho pendente. Código fica para Codex no contexto do checkout, sem substituição silenciosa por CHAT.

**Regra de promoção:** documento preparatório no Gerador não satisfaz o gate da Fase F-000000-000034-003; a estratégia só nasce na persistência local após releitura, alocação e provas.
