# Módulo: Execution Environments

**module_id:** `execution-environments`

## Finalidade

Separar identidade de governança, ambiente de execução/contexto e persistência/publicação.

## Planos

### Plano G — identidade

- Governança Global;
- Projeto `PRJ-NNNNNN`;
- Estratégia `EA-PPPPPP-EEEEEE`;
- Fase `F-PPPPPP-EEEEEE-FFF`.

A identidade não depende de Chat, Work, Projeto ChatGPT, Biblioteca, Codex, dispositivo ou sessão.

### Plano X — ambiente

- `X1_CHAT`: diálogo, decisão, explicação e tarefa delimitada;
- `X2_WORK`: execução substancial multi-etapas, auditoria, pesquisa ampla, muitos arquivos/apps e entrega acabada;
- `X3_CHATGPT_PROJECT`: contêiner contextual opcional; nunca substitui PRJ;
- `X4_LIBRARY`: persistência/descoberta dentro da conta; espelho/contexto operacional;
- `X5_CODEX`: código, testes e engenharia de repositório;
- `X6_APPS_CONNECTORS`: ponte autenticada para sistemas externos.

### Plano P — persistência

- `P0_COFRE_EXTERNO`;
- `P1_GIT_PRIVADO`;
- `P2_GIT_PUBLICO_REPOSITORIO`;
- `P3_PUBLICO_SITE`.

## Regras universais

1. Projeto ChatGPT não é Projeto de Governança.
2. Work e Codex executam; não substituem a fonte de verdade.
3. Biblioteca pode ser espelho/contexto; não deve ser a única fonte quando a independência de plataforma for requisito.
4. GitHub é a fonte versionada dos Projetos quando houver repositório.
5. O ambiente preferencial deve ser escolhido pelo perfil da tarefa.
6. Se o ambiente preferencial não estiver disponível, preservar `PRJ/EA/F`, usar fallback e persistir o estado.
7. Trabalho substancial deve terminar com persistência verificável.

## Perfil obrigatório

Projetos persistentes devem manter `EXECUTION_ENVIRONMENT_PROFILE.json`, declarando:

- identidade do Projeto;
- repositório canônico;
- ambientes preferenciais por tipo de tarefa;
- regra de fallback;
- relação com Projeto ChatGPT;
- papel da Biblioteca.

## Gate de escolha de ambiente

Antes de execução substancial, avaliar:

- tamanho e duração;
- número de arquivos;
- intensidade de pesquisa/navegação/apps;
- intensidade de código/repositório;
- necessidade de entrega acabada;
- continuidade;
- sensibilidade e superfície de persistência.
