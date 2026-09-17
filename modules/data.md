# Módulo: Data

**module_id:** `data`

## Quando se aplica

Ativar quando o projeto depender de coleta, transformação, limpeza, modelagem, validação, comparação, agregação ou visualização de dados estruturados.

## Arquivos canônicos exigidos

Conforme o caso:

- fonte ou inventário dos dados de origem;
- esquema ou dicionário de dados;
- arquivo canônico de dados estruturados;
- registro de transformações relevantes;
- relatório de validação quando os resultados sustentarem conclusões materiais.

## Regras obrigatórias

1. Distinguir dado bruto, dado transformado, cálculo derivado e interpretação.
2. Preservar os dados de origem antes de limpeza ou normalização destrutiva.
3. Registrar regras de transformação capazes de alterar resultados.
4. Não inventar valores ausentes nem convertê-los silenciosamente em zero.
5. Verificar tipos, unidades, datas, denominadores e critérios de inclusão/exclusão.
6. Manter rastreabilidade entre tabelas/resultados e os dados que os originaram.
7. Quando houver agregação, registrar população, período e fórmula relevantes.
8. Quando a análise for atualizada, não misturar silenciosamente séries ou metodologias incompatíveis.

## Estados específicos

```text
FONTE IDENTIFICADA
DADOS BRUTOS PRESERVADOS
ESQUEMA DEFINIDO
TRANSFORMAÇÃO EXECUTADA
VALIDAÇÃO EXECUTADA
ANÁLISE CONCLUÍDA
RESULTADO INCORPORADO
```

## Critério de conclusão

A análise de dados está concluída quando a origem, as transformações, os cálculos e as limitações relevantes são recuperáveis e os resultados foram validados de forma proporcional ao risco de uso.

## Verificação

Antes do fechamento:

- conferir contagens, totais e denominadores;
- verificar valores extremos e ausentes relevantes;
- conferir unidades e períodos;
- repetir cálculos críticos quando possível;
- registrar limitações e hipóteses.

## Riscos próprios

- perda do dado bruto;
- transformação não documentada;
- denominador incorreto;
- mistura de períodos ou populações;
- arredondamento material;
- inferência causal indevida a partir de associação.
