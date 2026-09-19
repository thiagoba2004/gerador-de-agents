# IDENTIFICATION_STANDARD.md — Metodologia Universal de Codificação Hierárquica

**Status:** CANÔNICO  
**Versão:** 1.0  
**Data:** 19/09/2026  
**Escopo:** todos os projetos governados ou gerados pelo Gerador de Agents.

## 1. Princípio

O identificador canônico nunca deve depender do nome, das iniciais, do idioma ou de uma sigla do objeto.

A metodologia separa três funções:

1. **código canônico** — identidade matemática, única e imutável;
2. **denominação** — nome humano do objeto;
3. **alias mnemônico** — abreviação opcional para leitura, sem função identificadora primária.

Nomes e aliases podem mudar. O código canônico não muda.

## 2. Código de Projeto

Gramática:

```text
PRJ-NNNNNN
```

onde `NNNNNN` é um inteiro sequencial global de seis algarismos, iniciado em `000001`.

Exemplos iniciais:

```text
PRJ-000001 — Classe e Massas
PRJ-000002 — Gerador de Agents
```

Campos:

```text
project_code
project_sequence
project_name
project_alias
project_id_legacy
```

O `project_alias` é opcional. Exemplos: `CEM`, `GDA`. Ele não participa do cálculo do código.

### 2.1. Alocação

Para registrar novo Projeto:

1. ler `PROJECT_REGISTRY.jsonl`;
2. localizar o maior `project_sequence` já atribuído;
3. calcular `next = max + 1`;
4. formatar com seis algarismos;
5. verificar que o código não existe;
6. persistir o novo registro;
7. verificar a persistência antes de usar o código.

Códigos nunca são reutilizados, nem após cancelamento, arquivamento, fusão ou renomeação.

A sequência expressa ordem de alocação, não prioridade, importância, hierarquia política ou valor.

## 3. Código de Estratégia Autônoma

Gramática:

```text
EA-PPPPPP-EEEEEE
```

onde:

- `PPPPPP` = sequência numérica do Projeto;
- `EEEEEE` = sequência da Estratégia Autônoma dentro daquele Projeto.

Exemplo:

```text
EA-000001-000014
```

significa: Estratégia Autônoma 14 do Projeto `PRJ-000001`.

Campos:

```text
strategy_code
strategy_sequence
strategy_name
legacy_strategy_id
```

Para Estratégias novas, `strategy_id` deve ser igual a `strategy_code`. Para estratégias históricas já registradas com identificadores legados, o identificador antigo é preservado e mapeado para `strategy_code`; o histórico append-only não é reescrito.

A sequência de Estratégia é monotônica dentro do Projeto e nunca é reutilizada.

## 4. Código de Fase

Gramática:

```text
F-PPPPPP-EEEEEE-FFF
```

onde:

- `PPPPPP` = sequência do Projeto;
- `EEEEEE` = sequência da Estratégia;
- `FFF` = número ordinal da Fase, com três algarismos.

Exemplo:

```text
F-000001-000014-003
```

corresponde à Fase 3 da Estratégia `EA-000001-000014`.

Campos obrigatórios:

```text
phase_code
phase_number
phase_total
phase_name
```

Forma humana:

```text
FASE 03/05 [F-000001-000014-003] — Denominação da fase
```

Se o total de fases mudar, `phase_total` pode ser atualizado. O `phase_code` de uma fase já existente não muda.

## 5. Aliases e denominações

`project_name` e `strategy_name` são denominações humanas.

`project_alias` é apenas mnemônico. Não é fonte de unicidade e não integra códigos descendentes.

Se dois Projetos tiverem as mesmas iniciais, seus códigos continuam distintos. Exemplo hipotético:

```text
PRJ-000021 — Centro de Estudos Marxistas — alias CEM
PRJ-000043 — Comissão de Estudos Municipais — alias CEM-MUN
```

A eventual colisão de alias é resolvida no alias, nunca por alteração do código canônico.

## 6. Imutabilidade e não reutilização

São invariantes:

- código canônico atribuído nunca muda;
- código canônico nunca é reutilizado;
- renomear objeto não renumera objeto;
- mover repositório não renumera Projeto;
- arquivar ou cancelar não libera número;
- fusões e cisões geram registros próprios, com vínculos aos predecessores;
- histórico legado é preservado por mapeamento, não por reescrita.

## 7. Migração dos Projetos conhecidos

Alocação inicial:

```text
PRJ-000001 — Classe e Massas — alias CEM — legado classe-e-massas/CEM
PRJ-000002 — Gerador de Agents — alias GDA — legado GDA
```

A numeração inicial é uma alocação administrativa do registro canônico e não expressa precedência substantiva.

## 8. Padrão de resposta de continuidade

Quando o usuário perguntar onde paramos, a resposta deverá usar os códigos canônicos:

```text
PROJETO: PRJ-000001 — Classe e Massas
ALIAS: CEM

ESTRATÉGIA AUTÔNOMA: EA-000001-000014 — <denominação>

FASE: 03/05 [F-000001-000014-003] — <denominação>

ESTADO: <estado comprovado>
ONDE PARAMOS: <ponto exato comprovado>
PRÓXIMO PASSO LÓGICO: <próximo passo comprovado>
```

Identificadores legados só devem aparecer quando necessários para rastreabilidade histórica.
