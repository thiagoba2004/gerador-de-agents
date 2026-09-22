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

### 6. Responsividade e acessibilidade

1. O Site deve funcionar em desktop e mobile.
2. No mobile, menu global não pode desaparecer sem alternativa; pode usar linha horizontal rolável quando esse for o padrão do projeto.
3. O item atual deve permanecer identificável.
4. Alvos interativos devem buscar dimensão mínima próxima de 44 px.
5. Deve haver foco visível por teclado.
6. Usar HTML semântico para `header`, `nav`, `main`, `footer`, headings e formulários.
7. Evitar overflow horizontal da página; exceções controladas podem existir para menu rolável e tabelas.
8. Contraste deve permanecer legível; não depender apenas de cor para indicar estado.
9. Respeitar preferências de redução de movimento quando houver animações relevantes.

### 7. Separação entre governança interna e camada pública

É proibido expor na interface pública, salvo necessidade expressa do visitante:

- códigos internos de projeto, estratégia, fase, pedido, evento ou fonte;
- estados editoriais/técnicos e gates;
- IDs de workflow, run, commit ou branch;
- nomes de arquivos de governança;
- versões de kernel/gerador;
- rótulos metodológicos que só façam sentido internamente.

A governança pode permanecer no repositório público. A regra é sobre **interface e artefato publicado**, não sobre ocultação do código-fonte do repositório.

### 8. Conteúdo e componentes

1. Não criar cards, menus, caixas ou seções apenas para “preencher” a página.
2. Componentes devem ter função informacional ou operacional real.
3. Conteúdo de navegação não deve competir visualmente com conteúdo principal.
4. Modelos reutilizáveis seguem adicionalmente o módulo `publication`.
5. Formulários e protocolos seguem adicionalmente o módulo `contact-protocol`.

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
