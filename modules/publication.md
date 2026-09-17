# Módulo: Publication

**module_id:** `publication`

## Quando se aplica

Ativar quando o projeto possuir publicação editorial, site, blog, newsletter, repositório público de artigos ou qualquer fluxo em que produzir conteúdo e torná-lo público sejam etapas distintas.

## Arquivos canônicos exigidos

Conforme o caso:

- fonte canônica do conteúdo;
- manifesto ou estado de publicação;
- referência ao destino público;
- histórico recuperável de versões relevantes.

## Regras obrigatórias

1. Distinguir `PRODUZIDO`, `SALVO`, `VERSIONADO`, `PUBLICADO` e `VERIFICADO PUBLICAMENTE`.
2. Nunca afirmar publicação apenas porque o arquivo local ou remoto foi atualizado.
3. Preservar a versão anterior antes de mudanças materiais em conteúdo já publicado.
4. Verificar o resultado no destino público quando tecnicamente possível.
5. Manter coerência entre título, metadados, corpo, links internos e referências.
6. Quando múltiplos formatos forem derivados da mesma fonte, declarar qual é a fonte canônica e quais são artefatos de publicação.

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

Uma publicação só está concluída quando o conteúdo correto chegou ao destino pretendido e, quando tecnicamente possível, foi verificado no endereço ou canal público correspondente.

## Verificação

Antes do fechamento:

- conferir a versão publicada contra a fonte canônica;
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
