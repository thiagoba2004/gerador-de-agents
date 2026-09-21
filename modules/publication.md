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
