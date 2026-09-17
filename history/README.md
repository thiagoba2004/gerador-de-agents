# Histórico canônico do Gerador de Agents

Este diretório preserva referências e versões históricas das instruções que deram origem ao Gerador de Agents.

## Versão 1.1 — 17/09/2026

Fonte original recuperada: `INSTRUCOES_PROJETO_GERADOR_DE_AGENTS_v1.1.md`  
Tamanho original: **23.505 bytes**  
Linhas: **635**  
SHA-256 do arquivo integral original: `abf7089cb7896dd33b419126192c5da8ab6ea1bb98922a02fe44f6933ae002e2`

A versão 1.1 é a base histórica imediatamente anterior ao `AGENTS_KERNEL.md` v1.2. Ela continha a ordem anterior de interação, em que uma mensagem de confirmação precedia o registro persistente. A decisão `ADR-003` em `DECISIONS.md` substituiu essa ordem pela regra vigente: registrar primeiro, confirmar tecnicamente, informar “Pedido registrado.” e somente então iniciar o processamento substantivo.

## Preservação integral no repositório

Por segurança operacional e para permitir gravação/verificação segmentada, o conteúdo integral da versão 1.1 está preservado em quatro partes contíguas:

1. `INSTRUCOES_PROJETO_GERADOR_DE_AGENTS_v1.1.part-001.md` — linhas originais 1–160 — 6.451 bytes — Git blob SHA-1 `0228139e84df872bd6659ed82d2a2ea708834028`;
2. `INSTRUCOES_PROJETO_GERADOR_DE_AGENTS_v1.1.part-002.md` — linhas originais 161–320 — 6.052 bytes — Git blob SHA-1 `f36964ef5a6d0e973e30e25b9a6cf56cc5018dad`;
3. `INSTRUCOES_PROJETO_GERADOR_DE_AGENTS_v1.1.part-003.md` — linhas originais 321–480 — 5.522 bytes — Git blob SHA-1 `6114a4305b399e1c36873d1fef514e014e42a94f`;
4. `INSTRUCOES_PROJETO_GERADOR_DE_AGENTS_v1.1.part-004.md` — linhas originais 481–635 — 5.480 bytes — Git blob SHA-1 `8173a6d6ba4f914108666e57d03b3e212395a8c0`.

A soma dos segmentos é **23.505 bytes**. Os quatro Git blob SHA-1 foram confrontados com os hashes calculados sobre os segmentos correspondentes do arquivo original recuperado e coincidem byte a byte.

Para reconstrução Unix/Linux/macOS:

```bash
cat \
  INSTRUCOES_PROJETO_GERADOR_DE_AGENTS_v1.1.part-001.md \
  INSTRUCOES_PROJETO_GERADOR_DE_AGENTS_v1.1.part-002.md \
  INSTRUCOES_PROJETO_GERADOR_DE_AGENTS_v1.1.part-003.md \
  INSTRUCOES_PROJETO_GERADOR_DE_AGENTS_v1.1.part-004.md \
  > INSTRUCOES_PROJETO_GERADOR_DE_AGENTS_v1.1.md

sha256sum INSTRUCOES_PROJETO_GERADOR_DE_AGENTS_v1.1.md
```

O resultado esperado é:

```text
abf7089cb7896dd33b419126192c5da8ab6ea1bb98922a02fe44f6933ae002e2
```

O conteúdo histórico deve permanecer imutável. Ele serve para proveniência e auditoria; em caso de conflito normativo, prevalece o kernel vigente, não a versão histórica.
