# Auditoria transversal de títulos visíveis — todos os Projetos

**Data:** 21/09/2026  
**Escopo canônico:** `PROJECT_REGISTRY.jsonl`  
**Natureza:** auditoria não destrutiva

## 1. Projetos auditados

1. `PRJ-000001 — Classe e Massas` — `thiagoba2004/classe-e-massas`
2. `PRJ-000002 — Gerador de Agents` — `thiagoba2004/gerador-de-agents`
3. `PRJ-000003 — Ações Judiciais` — `thiagoba2004/acoes-judiciais`
4. `PRJ-000004 — Planejamento Financeiro` — `thiagoba2004/planejamento-financeiro`

## 2. Critério

Para cada arquivo HTML:

- verificar presença de `<title>` técnico não vazio;
- verificar presença de `<h1>` editorial visível não vazio;
- classificar separadamente páginas com ausência de H1 e páginas com múltiplos H1.

A auditoria não altera projetos-alvo. Correções dependem de execução autorizada no projeto correspondente.

## 3. Universo

| Projeto | HTML auditados |
|---|---:|
| Classe e Massas | 59 |
| Gerador de Agents | 0 |
| Ações Judiciais | 14 |
| Planejamento Financeiro | 24 |
| **Total** | **97** |

## 4. Resultado principal — páginas sem título visível

### PRJ-000001 — Classe e Massas

- HTML: 59
- sem `<title>`: 0
- sem `<h1>`: 0
- com exatamente um `<h1>`: 49
- com múltiplos `<h1>`: 10

**Conclusão quanto ao pedido:** nenhuma página sem título visível.

### PRJ-000002 — Gerador de Agents

- HTML: 0

**Conclusão:** não possui Site/HTML a auditar.

### PRJ-000003 — Ações Judiciais

- HTML: 14
- sem `<title>`: 0
- sem `<h1>`: 0
- com exatamente um `<h1>`: 14

**Conclusão:** 14/14 conformes após a correção anterior dos dossiês de Superendividamento e Divórcio Litigioso.

### PRJ-000004 — Planejamento Financeiro

- HTML: 24
- sem `<title>`: 0
- sem `<h1>`: **3**
- com exatamente um `<h1>`: 21

Páginas afetadas:

1. `temas/divorcio-transicao-financeira.html`
   - `<title>`: “Divórcio: transição financeira | Planejamento Financeiro”
   - `<h1>`: ausente
   - Markdown canônico possui H1: “Divórcio: diagnóstico financeiro da ruptura e orçamento de transição”

2. `temas/patrimonio-partilha-liquidez.html`
   - `<title>`: “Patrimônio, avaliação e liquidez na partilha | Planejamento Financeiro”
   - `<h1>`: ausente
   - Markdown canônico possui H1: “Patrimônio, avaliação econômica e liquidez na partilha”

3. `temas/superendividamento-pf.html`
   - `<title>`: “Superendividamento das Pessoas Físicas | Planejamento Financeiro”
   - `<h1>`: ausente
   - Markdown canônico possui H1: “Superendividamento das Pessoas Físicas”

**Diagnóstico:** falha de publicação HTML, não ausência de título na fonte Markdown.

## 5. Achado secundário — múltiplos H1 no Classe e Massas

Não são páginas sem título. Porém, 10 documentos HTML possuem múltiplos `<h1>`, o que viola o critério semântico de um único título principal por página:

- `observatorio/documentos/00_Observatorio_Classe_e_Massas_Refundacao_Identidade.html`
- `observatorio/documentos/01_Observatorio_da_Classe_Trabalhadora.html`
- `observatorio/documentos/02_Observatorio_do_Movimento_dos_Trabalhadores.html`
- `observatorio/documentos/03_Observatorio_das_Lutas_de_Classes.html`
- `observatorio/documentos/04_Rede_de_Observatorios_Setoriais_e_Nucleo_Bancario.html`
- `observatorio/documentos/05_Mapas_do_Trabalho_do_Capital_e_Relacoes_de_Forca.html`
- `observatorio/documentos/06_Arquitetura_Publica_Metodo_e_Governanca.html`
- `observatorio/documentos/Observatorio_Classe_e_Massas_Diretriz_Canonica_Arquitetura_Documental.html`
- `observatorio/documentos/Observatorio_Movimento_Sindical_Bancario_Diretriz_Canonica_Arquitetura_Codex.html`
- `observatorio/documentos/Observatorio_Movimento_Sindical_Bancario_Documento_Canonico_Fundacao.html`

## 6. Consolidação

- HTML examinados: **97**
- páginas sem `<title>` técnico: **0**
- páginas sem `<h1>` editorial: **3**
- páginas com múltiplos `<h1>`: **10**
- páginas com exatamente um `<h1>`: **84**
- Projeto com páginas sem título editorial: **somente PRJ-000004 — Planejamento Financeiro**

## 7. Estado

**AUDITORIA CONCLUÍDA COM ACHADOS.**

Nenhuma correção foi aplicada aos projetos-alvo nesta execução, em respeito à regra de auditoria não destrutiva do Gerador de Agents.
