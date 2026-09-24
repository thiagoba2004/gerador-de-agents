# Módulo: Publication

**module_id:** `publication`

## Quando se aplica

Ativar quando o projeto possuir publicação editorial, site, blog, newsletter, repositório público de artigos ou qualquer fluxo em que produzir conteúdo e torná-lo público sejam etapas distintas.

## Arquivos canônicos

Para conteúdo textual/editorial publicável, o padrão é:

- fonte canônica em Markdown (`.md`);
- artefato de publicação em HTML (`.html`) quando houver publicação;
- JSON/JSONL **somente quando houver função estruturada real**.

JSON não é terceiro artefato obrigatório.

## Regra de necessidade para JSON

Criar ou manter JSON/JSONL quando houver uso objetivo de máquina, como:

- estado e governança;
- registros append-only;
- configuração;
- datasets, catálogos, taxonomias, glossários, fixtures ou schemas;
- metadados realmente consumidos por processo;
- dados usados por script, automação, API, busca estruturada, filtro, cálculo ou validação;
- interoperabilidade comprovada entre projetos.

É vedado criar `.json` apenas para repetir título, descrição, outline, links, caminhos ou conteúdo já preservado no Markdown e no HTML.

Antes de criar um JSON novo, o agente deve conseguir responder:

```text
QUAL PROCESSO CONSOME ESTE JSON?
QUAL DADO ESTRUTURADO ELE PRESERVA QUE O MARKDOWN NÃO ATENDE ADEQUADAMENTE?
```

Se não houver resposta concreta, não criar.

## Regras obrigatórias

1. Distinguir `PRODUZIDO`, `SALVO`, `VERSIONADO`, `PUBLICADO` e `VERIFICADO PUBLICAMENTE`.
2. Nunca afirmar publicação apenas porque o arquivo local ou remoto foi atualizado.
3. Preservar a versão anterior antes de mudanças materiais em conteúdo já publicado.
4. Verificar o resultado no destino público quando tecnicamente possível.
5. Manter coerência entre título, corpo, links internos e referências.
6. Para conteúdo textual/editorial, Markdown é a fonte textual canônica e HTML é o artefato de publicação.
7. A ausência de JSON não constitui lacuna quando não houver função estruturada real.
8. JSON existente só precisa acompanhar mudanças quando sua função de dados exigir.
9. Quando o conteúdo publicado for um **Modelo reutilizável**, o HTML deve conter botão canônico **`COPIAR MODELO`** imediatamente acima do bloco exato a ser copiado, sem elemento intermediário.
10. O botão de cópia deve copiar somente o conteúdo do Modelo e deve ser verificado funcionalmente antes do estado `VERIFICADO PUBLICAMENTE`.
11. O Site Público deve disponibilizar somente a edição vigente de cada Modelo.
12. É proibido manter botões, links, cards, menus, rotas navegáveis ou outros portões públicos para edições anteriores de Modelos.
13. O histórico de edições anteriores deve ser preservado pelo Git ou por mecanismo não publicado no Site Público.
14. A auditoria de publicação deve procurar regressões desses padrões em todas as seções do site, e não apenas na página modificada.
15. Quando o projeto utilizar **Notícias, Artigos e/ou Observatório**, todo conteúdo publicável deve possuir uma função editorial primária identificável, ainda que seja cruzado por tags e links para outras áreas.
16. **Notícia:** registrar data do fato quando conhecida, data de publicação, fontes recuperáveis e distinção entre fato verificado, alegação e impacto ainda incerto. Cadência de busca não cria obrigação de publicar conteúdo sem materialidade.
17. **Artigo:** distinguir fatos, marco normativo/técnico, evidências, inferências, objeções e posição autoral/editorial. O artigo deve indicar suas fontes e não se apresentar como simples notícia.
18. **Observatório:** expor escopo, data pública de atualização, conclusões, mudanças já analisadas, questões em aberto, fontes e relações com conteúdos estáveis. Versionamento técnico e pipeline de pesquisa permanecem internos, salvo utilidade pública comprovada.
19. Uma mesma informação pode alimentar as três camadas, mas não deve gerar três textos duplicados. Preferir referência cruzada, atualização da página estável ou produto derivado com função genuinamente diferente.
20. Arquivar ou atualizar conteúdo perecível sem quebrar a proveniência. Notícias históricas podem permanecer como registro; sínteses e observatórios devem indicar quando uma conclusão foi superada ou revista.


21. Quando Notícias, Artigos ou Observatório forem publicados em Site multipágina, aplicar o padrão **Coleção → Detalhe**: a página da seção funciona como índice/arquivo e o conteúdo integral vive em URL individual própria.
22. Em páginas de coleção, o **título do item deve ser o hiperlink principal** para a página individual. Exibir metadados mínimos e resumo/subtítulo curto quando úteis para orientar a escolha.
23. É vedado usar a página de índice como recipiente contínuo de múltiplas notícias, artigos ou relatórios integrais, salvo justificativa arquitetural expressa para conteúdo único e não cumulativo.
24. A fonte Markdown canônica deve acompanhar a granularidade pública: índice/coleção possui Markdown próprio e cada conteúdo individual possui seu Markdown próprio.
25. O gate de publicação deve testar coleção→detalhe, detalhe→coleção/contexto, URLs individuais e ausência de duplicação integral entre índice e detalhe.

## Estados específicos

```text
RASCUNHO
REVISADO
PRONTO PARA PUBLICAÇÃO
PUBLICADO
VERIFICADO PUBLICAMENTE
ATUALIZADO
ARQUIVADO
```

## Critério de conclusão

Uma publicação textual/editorial está concluída quando a fonte Markdown e a publicação HTML estão materialmente coerentes, o conteúdo correto chegou ao destino pretendido e, quando tecnicamente possível, o resultado foi verificado no endereço público correspondente.

Se houver JSON/JSONL funcional associado, sua consistência também integra o gate.

## Verificação

Antes do fechamento:

- conferir a versão publicada contra a fonte Markdown canônica;
- verificar links e referências críticas;
- verificar JSON/JSONL somente quando eles tiverem função estruturada aplicável;
- registrar URL ou identificador público;
- registrar data da verificação;
- atualizar o estado do projeto.

## Riscos próprios

- confundir commit com publicação;
- publicar versão desatualizada;
- quebrar links ou navegação;
- perder versão anterior;
- divergência entre fonte canônica e cópia pública;
- criar JSON redundante sem consumidor;
- Modelo sem botão de cópia ou com botão distante do texto;
- edição histórica de Modelo exposta ou navegável no Site Público.

## Relação com `web-site` e `contact-protocol`

O módulo `publication` governa artefatos e estados de publicação. Ele **não substitui** regras de arquitetura/UI.

- Site Público → avaliar `web-site`;
- Fale Conosco protocolado → avaliar `contact-protocol`;
- publicação bem-sucedida não prova responsividade, navegação correta ou contato funcional.


## Estados editoriais internos e pré-publicação

- O pipeline editorial pode manter internamente itens em monitoramento, triagem, pendência, horizon scanning ou fila de publicação.
- Esses estados **não devem ser publicados** na interface do Site.
- Uma coleção pública lista somente objetos editoriais já publicados.
- O Observatório público pode publicar sínteses, conclusões, lacunas e mudanças analisadas, mas não a fila de sinais internos, gatilhos ou itens aguardando maturação.
- “Critério editorial”, “Em monitoramento”, “Próximos gatilhos” e rótulos equivalentes devem permanecer nos documentos internos quando representarem governança e não conteúdo substantivo para o leitor.
- O gate de publicação inclui busca por vazamento de estados editoriais internos.


## Estrutura pública do Observatório

- O índice organiza **temas**, não versões técnicas.
- Cada tema público exibe **Atualizado em DD/MM/AAAA**.
- Identificadores como `Snapshot 0.1` ou `v0.1` são internos por padrão.
- O detalhe temático organiza síntese, conhecimento específico do domínio, mudanças analisadas, questões em aberto, fontes principais e conteúdos relacionados.
- Projetos jurídicos podem estruturar legislação, jurisprudência e doutrina/posições institucionais.
- Projetos financeiros/formativos podem estruturar premissas/evidências, implicações e interdependências.
- “Questões em aberto” é conteúdo público quando descreve uma lacuna substantiva já analisada; monitoramento e gatilhos continuam internos.
- O gate de publicação verifica data de atualização, retorno ao índice, links para fontes/conteúdos relacionados e ausência de versionamento técnico sem função pública.

## Pauta editorial interna / backlog de conteúdo

Quando o projeto possuir **Artigos** ou outro fluxo editorial de conteúdo analítico futuro, o módulo `publication` deve avaliar e, por padrão, criar:

```text
governanca/PAUTA_EDITORIAL.md
```

Esse arquivo é **governança interna**, não conteúdo público.

Regras obrigatórias:

1. a pauta registra hipóteses de conteúdos futuros; não constitui promessa de pesquisa, redação ou publicação;
2. uma entrada deve registrar, quando possível, identificador, título provisório, pergunta/ângulo, eixo, relação com conteúdo existente, prioridade, estado, densidade e Estratégia Autônoma vinculada;
3. antes de pesquisa substantiva, avaliar relevância, novidade, densidade, fontes disponíveis e risco de redundância;
4. pauta editorial e Roadmap têm funções diferentes: a pauta organiza possibilidades; Roadmap/Planos de Fases governam trabalho priorizado;
5. item aprovado para execução deve ser vinculado a Estratégia Autônoma e Plano de Fases antes da pesquisa substantiva;
6. item publicado deve ser atualizado para `PUBLICADA` com referência final;
7. itens suspensos ou descartados permanecem rastreáveis com motivo suficiente para evitar retrabalho;
8. o arquivo, seus estados, prioridades e itens não publicados **não podem aparecer no Site Público**, inclusive menus, cards, coleções, Mapa do Site, sitemap, feeds ou metadados públicos;
9. a auditoria de publicação deve procurar vazamento da pauta e bloquear a publicação em caso de exposição acidental.

Estados canônicos:

```text
IDEIA
EM_TRIAGEM
APROVADA_PARA_PESQUISA
EM_PESQUISA
PRONTA_PARA_REDACAO
EM_REDACAO
PRONTA_PARA_PUBLICACAO
PUBLICADA
SUSPENSA
DESCARTADA
```

Se o projeto não possuir nem planejar Artigos ou fila editorial futura, registrar `NOT_APPLICABLE` com justificativa em vez de criar um backlog vazio.

