# Auditoria de propagação — Tipografia responsiva e Home — 22/09/2026

## PRJ-000003 — Ações Judiciais
- `h1`: 1,5rem–1,9rem;
- Home `h1`: 1,75rem–2,25rem;
- mobile `h1`: 1,5rem;
- estado: **compatível com Gerador 1.13**;
- síntese institucional atualizada para incluir Doutrina e Publicações;
- GitHub Pages run `35747259846`: **success**.

## PRJ-000004 — Planejamento Financeiro
Antes:
- `h1` até 5rem;
- Home `h1` até 6,5rem;
- Home em flex horizontal com nota institucional lateral.

Depois:
- `h1`: 1,55rem–1,90rem;
- Home `h1`: 1,75rem–2,10rem;
- mobile `h1`: 1,60rem;
- Home em coluna;
- nota redundante de independência removida da Home e mantida no CFP®;
- GitHub Pages run `35747406857`: **success**.

## Conclusão
O achado local revelou uma lacuna reutilizável. O Gerador 1.13 passa a exigir:
1. escala tipográfica moderada;
2. limites responsivos explícitos;
3. Home empilhada no mobile quando necessário;
4. ausência de overflow horizontal geral;
5. teste mínimo em 360 px, 390 px e 412 px.
