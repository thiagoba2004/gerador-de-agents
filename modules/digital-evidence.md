# Módulo: Digital Evidence

**module_id:** `digital-evidence`

## Quando se aplica

Ativar quando o projeto envolver coleta, preservação, autenticação, hashing, cadeia de custódia, arquivamento ou apresentação de conteúdo digital como prova ou registro probatório.

## Arquivos canônicos exigidos

Conforme o caso:

- manifesto de coleta;
- arquivo original preservado;
- metadados de origem e data;
- hashes criptográficos;
- registro das transformações realizadas;
- cópias derivadas claramente identificadas.

## Regras obrigatórias

1. Preservar o original antes de converter, editar, consolidar, comprimir ou renomear substancialmente o conteúdo.
2. Calcular e registrar hash de arquivos relevantes quando tecnicamente possível.
3. Distinguir original, captura, cópia de trabalho, derivado e versão apresentada.
4. Registrar URL, origem, data/hora e método de coleta quando aplicáveis.
5. Não alegar autenticidade jurídica apenas porque um hash foi calculado; o hash comprova identidade do arquivo, não por si só autoria, origem ou veracidade do conteúdo.
6. Registrar toda transformação que possa alterar bytes ou apresentação.
7. Evitar sobrescrever arquivos probatórios.
8. Verificar integridade antes de empacotar ou apresentar o conjunto.

## Estados específicos

```text
FONTE IDENTIFICADA
COLETA REALIZADA
ORIGINAL PRESERVADO
HASH REGISTRADO
METADADOS REGISTRADOS
DERIVADOS GERADOS
INTEGRIDADE VERIFICADA
PACOTE PROBATÓRIO PRONTO
```

## Critério de conclusão

A coleta está concluída quando os originais relevantes estão preservados, os elementos de origem e integridade recuperáveis foram registrados e qualquer derivação pode ser rastreada ao respectivo original.

## Verificação

Antes do fechamento:

- recalcular hashes críticos quando necessário;
- conferir existência dos originais;
- conferir correspondência entre manifesto e arquivos;
- identificar lacunas na cadeia de preservação;
- registrar limitações técnicas ou probatórias.

## Riscos próprios

- captura incompleta;
- sobrescrita do original;
- perda de metadados;
- hash sem vinculação clara ao arquivo;
- confusão entre integridade e autenticidade;
- transformação não documentada;
- dependência de uma única cópia.
