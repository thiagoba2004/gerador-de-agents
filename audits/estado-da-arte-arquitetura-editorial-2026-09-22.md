# Estado da arte — arquitetura editorial para Notícias, Artigos e Observatório

**Data de corte:** 22/09/2026  
**Escopo:** PRJ-000002, PRJ-000003 e PRJ-000004.

## Achados do estado da arte

1. Arquitetura da informação deve priorizar encontrabilidade, compreensão, rotulagem clara e nesting apropriado segundo necessidades do visitante, não a estrutura interna do repositório.
2. Jornalismo digital distingue reporting/notícia, análise e opinião/comentário; a literatura recente recomenda sinalização clara entre gêneros porque o ambiente digital tende a borrar as fronteiras.
3. Estratégias editoriais contemporâneas valorizam análise, framing, verificação e reporting original como funções distintas.
4. Horizon scanning é processo sistemático e recorrente de identificação, filtragem, priorização, avaliação, disseminação e acompanhamento de sinais; portanto é metodologicamente diferente de um fluxo de notícias.
5. Living evidence e living systematic reviews demonstram que monitoramento contínuo exige cadências predefinidas, versionamento, registro das mudanças e critérios de atualização.
6. A gestão do conhecimento contemporânea trata conhecimento como sistema dinâmico que deve ser criado, adquirido, codificado, compartilhado, aplicado e revisto continuamente.

## Diagnóstico dos projetos

### Ações Judiciais
SITE_ARCHITECTURE.md define: Início · Ações · Guias · Modelos · Jurisprudência · Doutrina · Legislação · Fontes · Fale Conosco. Não existem Notícias, Artigos ou Observatório. A própria arquitetura declara que não cria novos itens globais por padrão.

O perfil do Gerador está defasado: profiles/acoes-judiciais.json não inclui Doutrina, embora a arquitetura pública atual a trate como área própria.

### Planejamento Financeiro
SITE_ARCHITECTURE.md define: Início · CFP® · Conhecimentos · Casos · Ferramentas · Fontes · Fale Conosco. Não existem Notícias, Artigos ou Observatório.

O perfil do Gerador também está defasado: profiles/planejamento-financeiro.json ainda registra Gestão Financeira e Métricas como itens globais, enquanto a arquitetura atual consolidou Gestão Financeira sob Conhecimentos e Métricas sob Ferramentas.

## Conclusão metodológica

Há lacuna normativa real no Gerador: ele regula como um Site deve ter arquitetura, menu, mapa e páginas centrais, mas não modela uma camada editorial transversal de atualidade, análise e observação. As três funções não são redundantes se suas fronteiras forem formalizadas.

A recomendação arquitetural preliminar é padronizar as três funções no Gerador como **camadas editoriais canônicas**, e deixar a decisão de navegação para cada projeto. Para Sites já densos, o padrão preferencial é um **hub editorial único no menu global** com três subáreas públicas: Notícias, Artigos e Observatório. Isso preserva a distinção conceitual sem aumentar excessivamente o número de itens de primeiro nível.

## Fontes principais

- Digital.gov — Information architecture: https://digital.gov/topics/information-architecture
- Digital.gov — Content goals/content audit: https://digital.gov/guides/research-collaboration/design-goals/content
- Reuters Institute — The relevance of impartial news in a polarised world: https://reutersinstitute.politics.ox.ac.uk/relevance-impartial-news-polarised-world
- Reuters Institute — Journalism, media, and technology trends and predictions 2026: https://reutersinstitute.politics.ox.ac.uk/journalism-media-and-technology-trends-and-predictions-2026
- Reuters Institute — Changing definitions of news in a digital environment (2026): https://reutersinstitute.politics.ox.ac.uk/changing-definitions-news-digital-environment-how-public-defines-news-across-six-countries
- OECD — Strategic intelligence tools for emerging technology governance (2025): https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/07/strategic-intelligence-tools-for-emerging-technology-governance_b7009977/02c05775-en.pdf
- OECD — Building capacity in technology horizon scanning (2026): https://www.oecd.org/en/publications/building-capacity-in-technology-horizon-scanning_b4f0d383-en.html
- GOV.UK — UK NSC horizon scanning: https://www.gov.uk/government/publications/uk-nsc-approach-to-horizon-scanning/uk-nsc-horizon-scanning
- BMJ — PRISMA-LSR (2024): https://www.bmj.com/content/387/bmj-2024-079183
- Cochrane Handbook — Prospective approaches to accumulating evidence: https://training.cochrane.org/handbook/current/chapter-22
- ISO — ISO 30401 / ISO-DIS 30401: https://www.iso.org/standard/68683.html and https://www.iso.org/standard/89436.html
