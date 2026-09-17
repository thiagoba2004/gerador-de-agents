# Módulo: Automation

**module_id:** `automation`

## Quando se aplica

Ativar quando o projeto depender de tarefas agendadas, gatilhos, monitoramento recorrente, pipelines, sincronizações ou ações automáticas executadas por sistemas, agentes ou integrações.

## Arquivos canônicos exigidos

Conforme o caso:

- definição do gatilho ou agenda;
- descrição da ação executada;
- registro de estado/última execução;
- logs ou evidência de execução quando disponíveis;
- critérios de falha, retry e desativação.

## Regras obrigatórias

1. Distinguir automação configurada, habilitada, executada e executada com sucesso.
2. Não afirmar monitoramento contínuo quando a ferramenta opera por verificações discretas.
3. Registrar frequência, gatilho, condição e destino da ação.
4. Quando a automação depender de condição externa, registrar claramente o critério de disparo.
5. Evitar duplicação de tarefas equivalentes sem justificativa.
6. Mudanças de agenda ou escopo devem preservar rastreabilidade histórica quando relevantes.
7. Quando houver falha, registrar se o erro ocorreu no gatilho, na execução ou na entrega do resultado.
8. Automações destrutivas ou de alto impacto exigem controles e verificação proporcionais ao risco.

## Estados específicos

```text
DEFINIDA
CONFIGURADA
HABILITADA
AGUARDANDO GATILHO
EXECUTADA
EXECUÇÃO VERIFICADA
FALHOU
PAUSADA
DESATIVADA
```

## Critério de conclusão

A implantação de uma automação está concluída quando a configuração foi persistida, seu estado real é verificável e pelo menos o mecanismo de execução/entrega foi validado de forma adequada ao risco.

## Verificação

Antes do fechamento:

- conferir agenda ou gatilho;
- conferir condição e destino;
- verificar se a automação está realmente habilitada;
- inspecionar execução recente ou teste quando possível;
- registrar limitações de frequência e confiabilidade.

## Riscos próprios

- confundir configuração com execução;
- duplicidade de disparos;
- monitoramento com frequência inadequada;
- falha silenciosa;
- condição mal definida;
- ação automática de alto impacto sem verificação.
