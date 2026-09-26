# EA-000002-000020 — Classificação Universal de Informação por Sensibilidade e Publicação

**Projeto:** PRJ-000002 — Gerador de Agents  
**Data:** 26/09/2026  
**Estado:** EM EXECUÇÃO

## Objetivo

Aplicar ao Projeto a política universal que separa **sensibilidade** da informação de **superfície de persistência/publicação**, impedindo que decisões técnicas de armazenamento produzam exposição indevida.

## Política global canônica

Quando a Biblioteca estiver acessível:

- `/Governanca-Geral-Modelos-IA/CLASSIFICACAO_UNIVERSAL_INFORMACAO.md`
- `/Governanca-Geral-Modelos-IA/INFORMATION_CLASSIFICATION_POLICY.json`

## Plano de Fases

1. **Fase 1/3 — F-000002-000020-001 — Registro e incorporação normativa**  
   Gate: pedido e estratégia persistidos; política global referenciada; regras mínimas locais definidas.

2. **Fase 2/3 — F-000002-000020-002 — Implementação e propagação**  
   Gate: AGENTS atualizado; Kernel, módulo e templates reutilizáveis implantados.

3. **Fase 3/3 — F-000002-000020-003 — Auditoria e fechamento**  
   Gate: regras de superfície verificadas; estado e logs atualizados; nenhuma regra pública contraditória.

## Regras mínimas não dependentes da Biblioteca

- `S2_CONFIDENCIAL` ou superior: nunca em repositório público nem Site;
- documento bruto `S3_ALTAMENTE_SENSIVEL`: cofre externo por padrão; não commitar ao Git;
- `S4_SEGREDO_CRITICO`: nunca enviar ao Modelo nem persistir em Git, Biblioteca, chat ou logs;
- mudança de classe para menos sensível somente por **derivado sanitizado**;
- antes de commit/publicação, classificar sensibilidade e superfície.
