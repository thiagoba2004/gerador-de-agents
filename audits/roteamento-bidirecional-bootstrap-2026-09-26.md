# Auditoria — EA-000002-000019 — Roteamento bidirecional com o Bootstrap

**Data:** 26/09/2026  
**Resultado:** APROVADO

## Gates

- [x] AGENTS local contém ponteiro explícito para `/Governanca-Geral-Modelos-IA/00_BOOTSTRAP_COORDENADOR_GERAL.md`;
- [x] consulta ao Bootstrap é condicional;
- [x] regra anti-loop explicitada;
- [x] ausência de acesso à Biblioteca não autoriza invenção do conteúdo global;
- [x] governança global permanece externa ao repositório;
- [x] Kernel 1.6 e template propagam o padrão a futuros Projetos;\n- [x] release 1.21 registrada no CHANGELOG;

## Fluxos verificados

1. entrada global → Bootstrap → Projeto/Gerador;
2. entrada direta por Projeto/Gerador → AGENTS local → Bootstrap somente quando houver gatilho transversal/global;
3. após a classificação, a governança local reassume o trabalho.

## Conclusão

Ponte implantada sem circularidade e sem carregar a governança global em tarefas inequivocamente locais.
