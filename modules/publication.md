# Módulo: Publication

**module_id:** `publication`

## Quando se aplica

Ativar quando o projeto possuir publicação editorial, site, blog, newsletter, repositório público de artigos ou qualquer fluxo em que produzir conteúdo e torná-lo público sejam etapas distintas.

## Arquivos canônicos exigidos

Para conteúdo textual/editorial publicável, manter obrigatoriamente o trio coordenado:

- fonte canônica em Markdown (`.md`);
- artefato de publicação em HTML (`.html`);
- representação estruturada/metadados em JSON (`.json`).

Além disso, conforme o caso:

- manifesto ou estado de publicação;
- referência ao destino público;
- histórico recuperável de versões relevantes.

## Regras obrigatórias

1. Distinguir `PRODUZIDO`, `SALVO`, `VERSIONADO`, `PUBLICADO` e `VERIFICADO PUBLICAMENTE`.
2. Nunca afirmar publicação apenas porque o arquivo local ou remoto foi atualizado.
3. Preservar a versão anterior antes de mudanças materiais em conteúdo já publicado.
4. Verificar o resultado no destino público quando tecnicamente possível.
5. Manter coerência entre título, metadados, corpo, links internos e referências.
6. Para conteúdo textual/editorial, Markdown é a fonte textual canônica; HTML é o artefato de publicação; JSON é a representação estruturada e interoperável.
7. Cada texto editorial/publicável deve possuir os três artefatos coordenados — `.md`, `.html` e `.json` — preferencialmente com o mesmo basename/slug.
8. O JSON deve identificar, no mínimo quando aplicável, id/slug, tipo, título, status, datas, caminho da fonte Markdown, caminho do HTML e referência de versão/commit/hash quando disponível.
9. Alterações materiais de título, subtítulo, autoria, data, corpo, referências, status ou slug devem ser sincronizadas nos três artefatos antes de o conteúdo atingir estado de conclusão/publicação.
10. HTML publicado sem Markdown correspondente, ou conteúdo editorial sem JSON correspondente, constitui lacuna documental e não deve ser tratado como estado completo.
11. Exceções somente são válidas quando houver decisão expressa, persistente e versionada no projeto-alvo, com justificativa e indicação da fonte da verdade substitutiva.

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

Uma publicação textual/editorial só está concluída quando o conteúdo correto chegou ao destino pretendido, os três artefatos `.md` + `.html` + `.json` existem e estão materialmente coerentes e, quando tecnicamente possível, o resultado foi verificado no endereço ou canal público correspondente.

## Verificação

Antes do fechamento:

- conferir a versão publicada contra a fonte Markdown canônica;
- verificar a existência e coerência do JSON correspondente;
- verificar links e referências críticas;
- registrar URL ou identificador público;
- registrar data da verificação;
- atualizar o estado do projeto.

## Riscos próprios

- confundir commit com publicação;
- publicar versão desatualizada;
- quebrar links ou navegação;
- perder versão anterior;
- divergência entre fonte canônica e cópia pública.
