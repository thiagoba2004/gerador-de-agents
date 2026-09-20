# Módulo: Software

**module_id:** `software`

## Quando se aplica

Ativar quando código-fonte, scripts, automações, APIs, testes, implantação ou manutenção de software fizerem parte do projeto.

## Arquivos canônicos exigidos

Conforme o caso:

- código-fonte versionado;
- documentação de arquitetura ou funcionamento quando relevante;
- testes ou procedimento verificável de validação;
- registro de configuração e dependências críticas;
- estado de implantação separado do estado de desenvolvimento.

## Regras obrigatórias

1. Ler o código e a arquitetura existentes antes de alterar comportamento significativo.
2. Preservar compatibilidade e contratos existentes salvo decisão explícita de migração.
3. Não tratar código escrito como código testado.
4. Distinguir `IMPLEMENTADO`, `TESTADO`, `VERSIONADO` e `IMPLANTADO`.
5. Alterações de comportamento devem ser acompanhadas de teste adequado quando tecnicamente possível.
6. Corrigir a causa do defeito sem ampliar desnecessariamente o escopo.
7. Preservar configuração e segredos fora de arquivos públicos ou versionados inadequadamente.
8. Registrar migrações, mudanças de esquema e operações destrutivas com plano de rollback quando relevantes.

## Estados específicos

```text
DIAGNÓSTICO
IMPLEMENTAÇÃO EM ANDAMENTO
IMPLEMENTADO
TESTADO
VERSIONADO
PRONTO PARA IMPLANTAÇÃO
IMPLANTADO
VERIFICADO EM EXECUÇÃO
```

## Critério de conclusão

Uma alteração de software só está concluída no escopo definido quando o comportamento esperado foi implementado, testado de forma compatível com o risco, versionado e, se o objetivo incluía implantação, verificado no ambiente de destino.

## Verificação

Antes do fechamento:

- executar testes relevantes;
- inspecionar erros e regressões conhecidas;
- conferir arquivos modificados e dependências;
- verificar estado do versionamento;
- quando aplicável, verificar o ambiente implantado.

## Riscos próprios

- regressão não testada;
- confusão entre código local e implantado;
- alteração destrutiva sem rollback;
- dependência não registrada;
- segredo exposto;
- reconstrução de código já existente por não consultar o repositório.


## Relação com interfaces públicas

Quando software sustentar um Site Público, aplicar também `web-site` quando ativado. Quando houver Fale Conosco/protocolo, aplicar `contact-protocol`.

Código de formulário presente no HTML não prova backend configurado nem teste end-to-end.
