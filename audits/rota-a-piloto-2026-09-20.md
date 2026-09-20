# Auditoria — Primeiro teste real da Rota A — 20/09/2026

**Estratégia do Gerador:** EA-000002-000006  
**Kernel:** 1.4  
**Release do Gerador:** 1.8

## Projetos testados

### PRJ-000003 — Ações Judiciais
- repositório: `thiagoba2004/acoes-judiciais`;
- estado inicial: repositório vazio;
- módulos ativados: research, legal, publication, software;
- primeira estratégia: `EA-000003-000001 — Ação de Repactuação de Dívidas por Superendividamento`;
- pacote crítico verificado: 11/11 arquivos;
- estado do site: ESTRUTURADO_NAO_PUBLICADO.

### PRJ-000004 — Planejamento Financeiro
- repositório: `thiagoba2004/planejamento-financeiro`;
- estado inicial: repositório vazio;
- módulos ativados: research, publication, software, data, professional-education;
- primeira estratégia: `EA-000004-000001 — Compreender o fenômeno do Superendividamento das Pessoas Físicas`;
- pacote crítico verificado: 13/13 arquivos;
- estado do site: ESTRUTURADO_NAO_PUBLICADO.

## Lacuna descoberta e correção

O catálogo não possuía módulo suficiente para projetos cuja finalidade combina certificação e competência profissional. Foi criado `modules/professional-education.md` e incorporado a `MODULE_SELECTION.md`.

O módulo institui:
- SABER / FAZER / DECIDIR;
- TRILHA_PROVA / TRILHA_PRATICA;
- fonte canônica por competência;
- casos e avaliação de domínio;
- atualização rastreável.

## Governança das fontes da Planejar

Os materiais oficiais da Planejar foram definidos como fontes canônicas do PRJ-000004. Canonicalidade não implica reprodução integral: o projeto registra referência, metadados, vigência e dependências; reprodução pública integral depende de permissão/licença compatível.

## Interoperabilidade entre projetos

O tema superendividamento aparece nos dois projetos, mas sem fusão de fonte da verdade:
- PRJ-000003: remédio/arquitetura jurídica;
- PRJ-000004: fenômeno financeiro, diagnóstico, prevenção, recuperação e competência profissional.

Referências cruzadas são permitidas; cópia silenciosa de conclusões não.

## Publicação

Os dois repositórios possuem `index.html` e pares canônicos Markdown + JSON. O conector GitHub disponível não expõe a configuração Settings → Pages. Portanto, publicação pública não foi declarada nem presumida.

## Resultado do teste

**ROTA A: APROVADA COM APERFEIÇOAMENTO.**

O teste comprovou que o Gerador consegue:
1. alocar projetos;
2. selecionar módulos por evidência;
3. detectar lacuna modular;
4. evoluir sem alterar o kernel indevidamente;
5. gerar governança completa;
6. registrar primeira estratégia antes da execução substantiva;
7. criar estrutura de publicação;
8. verificar persistência remota.

## Próximos passos dos projetos

- PRJ-000003: FASE 01/08 — delimitação e perguntas de pesquisa.
- PRJ-000004: FASE 01/08 — delimitação do fenômeno e perguntas de pesquisa; em seguida, inventário canônico da Planejar na FASE 02/08.
