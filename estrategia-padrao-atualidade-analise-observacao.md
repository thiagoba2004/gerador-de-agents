# EA-000002-000008 — Padrão editorial de Atualidade, Análise e Observação para Sites

**Projeto:** PRJ-000002 — Gerador de Agents  
**Status:** CONCLUÍDA  
**Objetivo:** definir um padrão reutilizável para Sites com três funções editoriais distintas — Notícias, Artigos e Observatório — sem confundir tipos de conteúdo, inflar o menu global ou duplicar áreas temáticas já existentes.

## Plano de Fases

### FASE 01/06 [F-000002-000008-001] — Diagnóstico e estado da arte
**Estado:** CONCLUÍDA  
**Objetivo:** confrontar a arquitetura vigente do Gerador e dos dois projetos-piloto com literatura atual de arquitetura da informação, jornalismo digital, gestão do conhecimento, horizon scanning e living evidence.  
**Gate:** diagnóstico documentado, fontes recuperáveis e lacunas explicitadas.

### FASE 02/06 [F-000002-000008-002] — Modelo canônico das três funções editoriais
**Estado:** CONCLUÍDA  
**Objetivo:** definir fronteiras funcionais, entradas, produtos, cadências e relações entre Notícias, Artigos e Observatório.  
**Gate:** nenhuma função pode ser mera duplicação nominal de outra área do Site.

### FASE 03/06 [F-000002-000008-003] — Propagação normativa no Gerador
**Estado:** CONCLUÍDA  
**Objetivo:** atualizar modules/web-site.md, modules/publication.md, modules/research.md, AGENTS.md e templates para incorporar o padrão.  
**Gate:** regra reutilizável explícita, sem impor automaticamente três itens de primeiro nível a todo Site.

### FASE 04/06 [F-000002-000008-004] — Sincronização dos perfis piloto
**Estado:** CONCLUÍDA  
**Objetivo:** corrigir drift entre profiles/acoes-judiciais.json, profiles/planejamento-financeiro.json e as arquiteturas públicas efetivamente vigentes.  
**Gate:** menus e funções dos perfis reproduzem o estado canônico dos projetos.

### FASE 05/06 [F-000002-000008-005] — Regras de composição do menu e mapa do site
**Estado:** PENDENTE  
**Objetivo:** definir quando as três funções aparecem como itens de primeiro nível, quando são agrupadas sob um hub editorial e como são refletidas no Mapa do Site.  
**Gate:** decisão baseada em necessidade do visitante, estabilidade transversal, clareza de rótulos e custo de navegação.

### FASE 06/06 [F-000002-000008-006] — Auditoria cruzada e fechamento
**Estado:** PENDENTE  
**Objetivo:** testar o padrão nos PRJ-000003 e PRJ-000004, registrar exceções e fechar a versão do Gerador.  
**Gate:** arquitetura coerente nos dois pilotos, sem regressão de rotas, menus, mobile, conteúdo ou governança.

## Decisão preliminar da Fase 02

As três funções são canonicamente distintas:

- **Notícias:** camada temporal de monitoramento de fatos, atos, decisões, normas, dados e acontecimentos relevantes; responde “o que mudou?”.
- **Artigos:** camada autoral de análise, argumentação, crítica e desenvolvimento de teses; responde “como interpretar, confrontar e problematizar?”.
- **Observatório:** camada cumulativa de pesquisa, leitura, classificação, síntese, vigilância de sinais, lacunas e evolução dos temas; responde “o que sabemos, como isso se conecta, o que está mudando e onde ainda há lacunas?”.

O padrão deve tornar as três funções obrigatoriamente modeláveis quando o Site possuir vocação editorial/analítica, mas não deve impor três itens independentes no menu global. A exposição de primeiro nível depende da arquitetura de informação do projeto.
