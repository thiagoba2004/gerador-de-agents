# Auditoria — cards-link e navegação horizontal deslizante

**Estratégia:** EA-000002-000015  
**Data:** 22/09/2026

## Escopo

Auditar a atualização transversal derivada da EA-000001-000024 do Classe e Massas.

## Verificações

- `modules/web-site.md` distingue explicitamente `HORIZONTAL_SCROLL` e `COLLAPSIBLE_DISCLOSURE`;
- a navegação horizontal é admitida quando deliberada, sem quebra dos itens e com overflow confinado ao componente;
- o padrão visual de uma família de Sites pode ser preservado de forma consistente, sem transformar disclosure em requisito universal;
- `templates/AGENTS.example.md` herda a escolha arquitetural entre os dois padrões;
- cards de destino único são tratados como hiperlinks integrais;
- cards clicáveis devem ser distinguíveis visualmente de cards informativos;
- botões são reservados a ações reais de interface, não à simples navegação;
- cards com múltiplos destinos preservam links secundários claros.

## Resultado

Gate aprovado. A regra anterior da versão 1.16 não é apagada do histórico, mas deixa de ser interpretada como obrigatoriedade universal de menu recolhível. O padrão reutilizável passa a permitir decisão arquitetural explícita e consistente entre navegação horizontal deslizante e disclosure recolhível.
