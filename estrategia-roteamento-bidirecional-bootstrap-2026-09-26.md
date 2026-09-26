# EA-000002-000019 — Roteamento bidirecional com o Bootstrap do Coordenador Geral

**Projeto:** PRJ-000002 — Gerador de Agents  
**Data:** 26/09/2026  
**Estado:** EM EXECUÇÃO

## Objetivo

Criar uma ponte de descoberta em dois sentidos entre a governança global do Coordenador Geral e este repositório, sem duplicar a metagovernança global no AGENTS local.

## Regra-alvo

> Antes de tratar pedidos com possível repercussão transversal ou dúvida de roteamento, consultar `/Governanca-Geral-Modelos-IA/00_BOOTSTRAP_COORDENADOR_GERAL.md`.

O Bootstrap deve ser consultado **condicionalmente**, não em toda conversa. Pedidos inequivocamente locais seguem diretamente o AGENTS deste Projeto; pedidos casuais continuam fora da governança conforme a classificação global.

## Plano de Fases

1. **Fase 1/3 — F-000002-000019-001 — Registro e desenho da ponte**  
   Gate: pedido, estratégia e regra de precedência persistidos.

2. **Fase 2/3 — F-000002-000019-002 — Implementação e propagação**  
   Gate: AGENTS local atualizado; no Gerador, Kernel/template atualizados para novos projetos.

3. **Fase 3/3 — F-000002-000019-003 — Auditoria e fechamento**  
   Gate: ponte presente e não circular; estado e logs atualizados.

## Salvaguardas

- não copiar o conteúdo do Coordenador Geral para os repositórios;
- não exigir acesso ao Bootstrap quando o pedido for inequivocamente local e sem repercussão transversal;
- se a Biblioteca/Bootstrap não estiver acessível na sessão, registrar a limitação e continuar pela governança local sem inventar conteúdo global;
- evitar loop: o Bootstrap pode rotear ao Projeto; o Projeto só retorna ao Bootstrap quando houver dúvida de roteamento ou repercussão transversal;
- futuros projetos gerados pelo Gerador devem herdar a mesma regra.
