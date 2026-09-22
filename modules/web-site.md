# Módulo: Web Site

**module_id:** `web-site`

## Quando se aplica

Ativar quando o projeto possuir Site Público, portal, aplicação web informativa, documentação navegável ou qualquer interface web destinada a terceiros.

Não ativar apenas porque há arquivos HTML isolados. O módulo se aplica quando existe ou deve existir uma **arquitetura de Site**, com navegação, páginas públicas e identidade visual.

## Arquivos canônicos exigidos

Quando ativado, manter, conforme aplicável:

- `SITE_ARCHITECTURE.md` — mapa canônico de menus, páginas, hierarquia e função de cada área;
- `SITE_STYLE_GUIDE.md` — identidade visual, design tokens e regras de interface;
- folha de estilos global ou sistema equivalente;
- mapa/manifesto de rotas públicas quando o Site tiver mais de uma área;
- procedimento verificável de auditoria de navegação, responsividade e vazamento de governança.

## Regras obrigatórias

### 1. Site é arquitetura de informação, não uma página longa

1. Se o projeto foi definido como **Site**, a interface não pode ser reduzida a uma homepage com cards que simulam menus e uma única página longa.
2. As áreas do projeto devem possuir páginas próprias quando representarem seções autônomas.
3. Páginas centrais de menu devem conter conteúdo útil ou navegação substantiva; placeholders vazios são proibidos.
4. O conteúdo deve ser organizado segundo a necessidade do visitante, não segundo a estrutura interna do repositório.

### 2. Menu global

1. Todo Site multipágina deve possuir **menu global permanente**.
2. O mesmo conjunto e ordem de itens deve ser mantido em todas as páginas, salvo exceção documentada.
3. A página corrente deve possuir `aria-current="page"`.
4. Links internos devem usar rotas estáveis e ser auditados após alteração estrutural.
5. Quando o módulo `contact-protocol` estiver ativo, **Fale Conosco** integra o menu global.
6. **Mapa do Site não substitui o menu global**.

### 2.1. Camadas editoriais transversais: Notícias, Artigos e Observatório

Sites com vocação de conhecimento, consulta, formação, pesquisa, análise ou atualização temática devem avaliar explicitamente três funções editoriais transversais:

1. **Notícias** — camada temporal e factual. Responde prioritariamente **“o que mudou?”** e acompanha fatos, atos, decisões, normas, dados, eventos e desenvolvimentos relevantes aos temas já cobertos pelo Site.
2. **Artigos** — camada autoral e argumentativa. Responde prioritariamente **“como interpretar, confrontar ou problematizar?”** e desenvolve teses, raciocínio crítico, novas perspectivas e implicações, distinguindo fatos, fontes, inferências e posição editorial/autoral.
3. **Observatório** — camada cumulativa de inteligência e conhecimento. Responde prioritariamente **“o que sabemos, como se conecta, o que está mudando e onde estão as lacunas?”** e sistematiza pesquisa, sinais, tendências, relações, lacunas, linhas do tempo e sínteses atualizáveis.

Essas três funções são distintas. Uma notícia não deve ser artificialmente alongada para funcionar como artigo; um artigo não deve se apresentar como notícia neutra; e o Observatório não deve virar depósito cronológico de notícias ou mera lista de fontes.

A avaliação das três camadas é obrigatória quando materialmente pertinente, mas **a presença conceitual não implica três itens independentes no menu global**. O perfil e o `SITE_ARCHITECTURE.md` devem registrar explicitamente:

- quais camadas são aplicáveis;
- quais estão públicas, planejadas ou não aplicáveis;
- o modo de navegação escolhido;
- o rótulo de eventual hub editorial;
- as rotas e relações com áreas temáticas estáveis;
- a regra de classificação primária de cada conteúdo.

Modos canônicos de composição:

```text
TOP_LEVEL_SEPARATE   = Notícias, Artigos e Observatório como itens independentes
EDITORIAL_HUB        = um item de primeiro nível agrega as três subáreas
NESTED_CONTEXTUAL    = camadas acessíveis dentro de área temática/hub já existente
NOT_APPLICABLE       = função justificada como não aplicável ao projeto
```

A escolha deve considerar encontrabilidade, clareza de rótulo, estabilidade transversal, densidade do menu, mobile, expectativa do visitante e sobreposição com áreas já existentes. É proibido escolher um modo apenas para reproduzir a estrutura interna do repositório.

### 2.2. Gate de composição da navegação editorial

Aplicar os seguintes critérios antes de alterar o primeiro nível do menu:

1. **Usar `TOP_LEVEL_SEPARATE`** somente quando Notícias, Artigos e Observatório forem, individualmente, destinos frequentes e prioritários para o visitante e a inclusão das três opções não degradar a leitura do menu em desktop ou mobile.
2. **Preferir `EDITORIAL_HUB`** em Sites de conhecimento já densos, quando as três funções forem transversais a várias áreas temáticas e sua promoção individual tornar o primeiro nível excessivamente fragmentado.
3. **Usar `NESTED_CONTEXTUAL`** quando as funções editoriais fizerem sentido apenas dentro de uma única área estável e não tiverem autonomia transversal real.
4. **Usar `NOT_APPLICABLE`** somente com justificativa persistida; ausência histórica da seção não constitui justificativa suficiente.
5. Um hub editorial deve possuir página central útil, com explicação breve das três funções e acesso inequívoco às subáreas; não pode ser um dropdown sem destino ou um contêiner vazio.
6. O rótulo do hub deve ser compreensível ao visitante e testado contra os demais nomes do menu. Não adotar automaticamente “Editorial”, “Conteúdo”, “Publicações” ou qualquer outro rótulo sem confronto com o vocabulário do projeto.
7. Independentemente do modo escolhido, o **Mapa do Site** deve expor explicitamente Notícias, Artigos e Observatório quando forem públicos, inclusive quando não estiverem no primeiro nível.
8. Mudança de composição exige auditoria de todas as páginas públicas para garantir ordem uniforme, `aria-current`, rotas, breadcrumbs quando usados e ausência de links órfãos.
9. A arquitetura deve preservar as **áreas estáveis de conhecimento** como fontes de referência. Notícias, Artigos e Observatório são camadas transversais, não substitutos automáticos de dossiês, guias, conhecimentos, jurisprudência, ferramentas, fontes ou equivalentes.
10. Conteúdo derivado deve privilegiar ligação bidirecional: notícia aponta para a página estável afetada; artigo referencia os conteúdos-base; observatório mantém mapa/síntese e aponta para evidências e produtos relacionados.



### 2.3. Padrão canônico Coleção → Detalhe para Publicações

Quando Notícias, Artigos e/ou Observatório possuírem mais de uma unidade publicável — ou quando a área tiver vocação de crescimento cumulativo — a arquitetura deve separar obrigatoriamente dois níveis:

```text
SEÇÃO EDITORIAL
→ PÁGINA DE COLEÇÃO/ÍNDICE
→ PÁGINA INDIVIDUAL DE DETALHE
```

Regras:

1. **A página da seção não deve incorporar integralmente todos os conteúdos individuais.** Sua função principal é descoberta, comparação e navegação.
2. Cada item da coleção deve apresentar, no mínimo:
   - **título único e descritivo como hiperlink** para a página individual;
   - data pertinente;
   - tema/categoria quando útil;
   - resumo curto ou subtítulo que ofereça informação suficiente para o visitante decidir se deseja abrir o conteúdo.
3. Evitar links genéricos como “Leia mais” como único destino. O título do item deve ser clicável.
4. A página individual deve possuir URL própria, título/H1 próprio, metadados próprios e ligação de retorno ou contexto para a coleção.
5. **Notícias:** índice cronológico ou temático; cada notícia publicada possui página própria.
6. **Artigos:** índice/arquivo com título, tese/subtítulo ou resumo e metadados; cada artigo possui página própria.
7. **Observatório:** índice de temas ou unidades de conhecimento; cada unidade possui página própria. Na UI pública, preferir data de atualização e linguagem compreensível ao leitor; versões técnicas permanecem internas salvo utilidade pública comprovada.
8. Uma seção com apenas um item pode já adotar o padrão para evitar migração estrutural futura.
9. Páginas de coleção podem incorporar paginação, filtros ou agrupamentos somente quando o volume justificar; não criar complexidade antecipadamente.
10. O Mapa do Site deve distinguir a seção editorial das páginas individuais materialmente relevantes, conforme a densidade do acervo.
11. A auditoria deve verificar links título→detalhe, retorno/contexto detalhe→coleção, ausência de conteúdo integral duplicado no índice e inexistência de páginas órfãs.


### 2.4. Arquitetura pública do Observatório

O Observatório não é uma página de relatório nem uma exposição do pipeline de pesquisa. É uma camada pública para organizar **o estado atual do conhecimento** sobre temas já cobertos pelo Site.

Regras:

1. O índice público apresenta **temas do Observatório**, com título clicável, resumo e **Atualizado em DD/MM/AAAA**.
2. Não expor identificadores técnicos como `Snapshot 0.1`, `v0.1`, número de build, estado de rascunho ou equivalente, salvo significado público comprovado.
3. O detalhe temático deve permitir ao leitor responder: **o que sabemos, o que mudou, o que ainda está em aberto, quais fontes sustentam a síntese e onde aprofundar**.
4. O conjunto de seções é adaptado ao domínio. Não copiar mecanicamente subtítulos de um projeto para outro.
5. Estrutura-base recomendada:
   - **Em síntese**;
   - blocos de conhecimento específicos do domínio;
   - **O que mudou desde a última atualização**;
   - **Questões em aberto**;
   - **Fontes principais**;
   - **Conteúdos relacionados**;
   - data clara de atualização.
6. Para projetos jurídicos, quando aplicável: **Legislação vigente**, **Jurisprudência relevante**, **Doutrina e posições institucionais**.
7. Para planejamento financeiro/formação profissional, quando aplicável: **Evidências e premissas atuais**, **Implicações para o planejamento**, **Mapa de interdependências**.
8. “Questões em aberto” pode ser pública quando descreve lacuna substantiva real. Monitoramento, triagem, fila, gatilhos e versões de trabalho permanecem internos.
9. A primeira publicação pode informar que não existe atualização pública anterior para comparação; não deve simular histórico inexistente.
10. A auditoria deve verificar ausência de versionamento técnico na UI, presença de data de atualização, seções essenciais, fontes/conteúdos relacionados e retorno ao índice.

### 3. Página Início

1. A página **Início** é institucional e enxuta por padrão.
2. É proibido duplicar na Home todo o conteúdo do menu por meio de blocos como “Explore o Site”, “Conheça as áreas”, catálogo de menus ou equivalentes, salvo decisão expressa do perfil do projeto.
3. A Home deve apresentar identidade, finalidade e, quando pertinente, um destaque editorial real — não explicar a própria navegação.
4. A arquitetura completa pertence ao **Mapa do Site**.

### 4. Mapa do Site

1. Todo Site multipágina deve possuir página própria **Mapa do Site**.
2. Toda página pública deve conter no rodapé um hiperlink denominado exatamente **Mapa do Site**.
3. O Mapa do Site deve refletir as rotas públicas reais e ser atualizado quando menus ou páginas forem alterados.
4. O Mapa do Site pode detalhar subpáginas e hierarquias que não cabem no menu global.

### 5. Identidade visual própria

1. Cada projeto deve possuir identidade visual própria, definida no perfil e em `SITE_STYLE_GUIDE.md`.
2. Reutilizar um padrão estrutural de outro Site **não autoriza copiar sua identidade visual**.
3. Projetos distintos não devem compartilhar mecanicamente paleta, combinação tipográfica, forma de cards, ornamentos ou composição de Home.
4. Definir no mínimo:
   - cor de fundo;
   - cor de superfície;
   - cor de texto;
   - cor primária;
   - cor secundária/interação;
   - cor de acento;
   - cor de linhas/bordas;
   - tipografia de títulos;
   - tipografia de corpo/interface;
   - larguras de leitura e de layout;
   - raio, sombra ou linguagem de contêineres, quando usados.
5. Esses valores devem existir como design tokens ou equivalente reutilizável.

### 5.1. Escala tipográfica responsiva e composição da Home

1. A hierarquia tipográfica deve ser clara sem transformar títulos em elementos de escala de display por padrão.
2. Para Sites informativos e formativos, adotar como referência inicial:
   - corpo em torno de `1rem`;
   - `h1` aproximadamente entre `1,5rem` e `2,0rem`;
   - `h1` da Home aproximadamente entre `1,7rem` e `2,2rem`;
   - `h2` aproximadamente entre `1,2rem` e `1,6rem`;
   - `h3` próximo de `1,05rem–1,15rem`.
3. Variações maiores exigem justificativa visual explícita no perfil do projeto; não usar `vw` sem limite superior seguro.
4. No mobile, títulos devem permanecer apenas moderadamente maiores que o corpo e não podem dominar a viewport, cortar palavras ou induzir rolagem horizontal.
5. A Home institucional deve empilhar seus blocos estruturais no mobile. Layouts lado a lado só podem permanecer quando comprovadamente couberem sem corte ou overflow.
6. Testar, no mínimo, larguras de 360 px, 390 px e 412 px, além de uma largura desktop.
7. Overflow horizontal geral é falha. Exceções deliberadas ficam restritas a componentes próprios de rolagem, como navegação horizontal e tabelas.
8. Avisos contextuais não devem ser duplicados na Home quando já pertencem claramente a uma página temática e a duplicação prejudica concisão ou responsividade.

### 6. Responsividade e acessibilidade

1. O Site deve funcionar em desktop e mobile.
2. No mobile, menu global não pode desaparecer sem alternativa.
3. Menus densos não devem ser simplesmente empilhados em múltiplas linhas. A arquitetura deve escolher explicitamente entre, pelo menos, `HORIZONTAL_SCROLL` e `COLLAPSIBLE_DISCLOSURE`.
4. `HORIZONTAL_SCROLL` é válido quando a faixa de navegação é deliberadamente rolável, preserva itens em uma linha, mantém o item atual identificável e confina o overflow ao componente. Quando uma família de Sites já adota esse paradigma de modo consistente, ele deve ser preservado salvo decisão arquitetural rastreável em contrário.
5. `COLLAPSIBLE_DISCLOSURE` é válido quando a densidade, hierarquia ou profundidade do menu justificarem recolhimento. O controle deve usar botão semântico, `aria-controls` e `aria-expanded`; a tecla Escape deve fechar a navegação quando aberta.
6. Hubs com subáreas, como **Publicações**, podem ser um destino simples de primeiro nível ou usar disclosure/dropdown. A escolha deve ser documentada; o hub deve continuar acessível por URL própria.
7. O comportamento deve seguir **progressive enhancement** quando depender de JavaScript: sem JavaScript, a navegação essencial permanece visível ou alcançável.
8. O item atual deve permanecer identificável.
9. Alvos interativos devem buscar dimensão mínima próxima de 44 px.
10. Deve haver foco visível por teclado.
11. Usar HTML semântico para `header`, `nav`, `main`, `footer`, headings e formulários.
12. Evitar overflow horizontal da página; exceções controladas podem existir para componentes deliberadamente roláveis e tabelas.
13. Contraste deve permanecer legível; não depender apenas de cor para indicar estado.
14. Respeitar preferências de redução de movimento quando houver animações relevantes.
15. O gate mobile deve verificar o padrão escolhido: em `HORIZONTAL_SCROLL`, rolagem tátil, ausência de quebra e item atual; em `COLLAPSIBLE_DISCLOSURE`, estado fechado/aberto, Escape, clique/toque, foco e fallback.

### 7. Separação entre governança interna e camada pública

É proibido expor na interface pública, salvo necessidade expressa do visitante:

- códigos internos de projeto, estratégia, fase, pedido, evento ou fonte;
- estados editoriais/técnicos e gates;
- IDs de workflow, run, commit ou branch;
- nomes de arquivos de governança;
- versões de kernel/gerador;
- rótulos metodológicos que só façam sentido internamente.

A governança pode permanecer no repositório público. A regra é sobre **interface e artefato publicado**, não sobre ocultação do código-fonte do repositório.


### 7.1. Estados editoriais internos não são conteúdo público

1. Estados e mecanismos de trabalho como **“Em monitoramento”**, “fila editorial”, “triagem”, “pendente”, “pré-publicação”, “critério editorial”, “gatilho de revisão”, “gatilho de publicação” e equivalentes pertencem à governança interna.
2. O Site Público não deve listar itens ainda não aprovados como notícia, artigo ou unidade do Observatório.
3. Monitoramento, horizon scanning, critérios de materialidade, sinais imaturos e gatilhos podem existir em arquivos internos de pesquisa, logs, matrizes ou documentos de trabalho, mas não como blocos públicos de pré-publicação.
4. O Observatório Público pode apresentar **conclusões, estado do conhecimento, lacunas e mudanças já analisadas**, sem expor a fila interna de acompanhamento.
5. Notícias públicas devem conter apenas notícias efetivamente publicadas; itens descartados, imaturos ou aguardando confirmação permanecem fora da UI.
6. Antes do deploy, varrer HTML/Markdown públicos em busca de rótulos e microcopy que revelem estados editoriais internos. A presença desses elementos bloqueia publicação.

### 8. Conteúdo e componentes

1. Não criar cards, menus, caixas ou seções apenas para “preencher” a página.
2. Componentes devem ter função informacional ou operacional real.
3. Conteúdo de navegação não deve competir visualmente com conteúdo principal.
4. Quando um card representar **um único destino**, preferir que o próprio card seja o hiperlink de bloco inteiro; ele deve ser visualmente distinguível de card apenas informativo por superfície, borda ou outro contraste perceptível.
5. Não usar botão interno do tipo “LER”, “ABRIR” ou equivalente como única pista de navegação quando o card inteiro puder ser o link. Botões devem representar ações reais de interface, como copiar, enviar, confirmar, expandir ou executar comando.
6. Cards com múltiplos destinos ou ações não devem ser convertidos em um único link; manter estrutura informativa e links secundários semanticamente claros.
7. Hover e foco devem reforçar a affordance do card-link; cor não deve ser a única indicação de estado.
8. Modelos reutilizáveis seguem adicionalmente o módulo `publication`.
9. Formulários e protocolos seguem adicionalmente o módulo `contact-protocol`.

## Estados específicos

```text
ARQUITETURA_DEFINIDA
IDENTIDADE_DEFINIDA
IMPLEMENTADO
RESPONSIVO_AUDITADO
NAVEGACAO_AUDITADA
PUBLICADO
VERIFICADO_PUBLICAMENTE
```

## Critério de conclusão

Uma evolução de Site só é concluída quando:

- menu global está coerente em todas as rotas;
- Home respeita o papel definido no perfil;
- Mapa do Site existe e corresponde às rotas;
- identidade visual própria está documentada e aplicada;
- responsividade e acessibilidade básica foram auditadas;
- não há vazamento de governança interna na UI;
- o Site publicado foi verificado no destino quando tecnicamente possível.

## Verificação mínima

- enumerar rotas públicas;
- conferir menu e `aria-current`;
- conferir hiperlink **Mapa do Site** no rodapé;
- testar largura móvel;
- testar links internos;
- comparar tokens visuais com outros projetos para evitar clonagem involuntária;
- procurar marcadores internos proibidos;
- verificar deploy e URL pública.

## Riscos próprios

- Site virar blog/página única sem arquitetura;
- Home duplicar a navegação;
- Mapa do Site inexistente ou desatualizado;
- menu inconsistente entre páginas;
- cópia visual de outro projeto;
- aparência “vazia” por falta de hierarquia;
- quebra mobile;
- governança interna exposta ao visitante;
- páginas de menu sem conteúdo real.
