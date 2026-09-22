# AGENTS.md — {{PROJECT_NAME}}

**project_id legado:** `{{PROJECT_ID_LEGACY}}`  
**project_code:** `{{PROJECT_CODE}}`  
**project_sequence:** `{{PROJECT_SEQUENCE}}`  
**project_alias:** `{{PROJECT_ALIAS}}`  
**project_name:** `{{PROJECT_NAME}}`  
**generated_from_kernel:** `{{KERNEL_VERSION}}`  
**repository/source:** `{{PROJECT_REF}}`  
**modules:** {{MODULE_LIST}}

## 1. Missão do projeto

{{PROJECT_PURPOSE}}

## 2. Ordem obrigatória para qualquer novo pedido

```text
REGISTRAR O PEDIDO
↓
CONFIRMAR TECNICAMENTE O REGISTRO
↓
INFORMAR “PEDIDO REGISTRADO.”
↓
INFORMAR QUE IRÁ LER O PROMPT, ANALISAR E TOMAR AS PROVIDÊNCIAS
↓
EXECUTAR
```

Todo pedido, correção, complemento, pergunta, interrupção ou mudança de instrução deve ser registrado em `REQUEST_LOG.jsonl` ou mecanismo persistente equivalente antes da execução substantiva.

## 3. Fonte da verdade

Hierarquia deste projeto:

1. {{CANONICAL_SOURCE_1}}
2. {{CANONICAL_SOURCE_2}}
3. `PROJECT_STATE.json` ou equivalente;
4. `STRATEGY_LOG.jsonl`;
5. histórico de versionamento comprovado;
6. somente depois, memória ou contexto conversacional.

## 4. Estratégias

Toda Estratégia Autônoma deve possuir `strategy_code` e `strategy_name` estáveis e evento persistido em `STRATEGY_LOG.jsonl` antes da execução substantiva.

Padrão canônico:

```text
EA-{{PROJECT_SEQUENCE}}-EEEEEE
```

Para Estratégias novas, `strategy_id = strategy_code`. Identificadores históricos, quando existirem, ficam em `legacy_strategy_id` ou mapeamento equivalente.

Continuações e retomadas mantêm o mesmo identificador. Apenas nova unidade estratégica recebe novo `strategy_id`.

## 5. Plano de Fases

Toda Estratégia Autônoma deve possuir Plano de Fases explícito, persistente e integralmente numerado.

Cada fase deve possuir `phase_number`, `phase_code`, `phase_name` e `phase_total`, além de estado, objetivo e gate quando aplicável.

Padrão canônico:

```text
F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-FFF
```

Padrão obrigatório:

```text
FASE 01/{{PHASE_TOTAL}} [F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-001] — Registro e delimitação
FASE 02/{{PHASE_TOTAL}} [F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-002] — ...
FASE {{PHASE_TOTAL}}/{{PHASE_TOTAL}} [F-{{PROJECT_SEQUENCE}}-{{STRATEGY_SEQUENCE}}-{{PHASE_TOTAL_PADDED3}}] — Verificação e fechamento
```

Não usar fases sem número, inclusive “FASE FINAL” isoladamente.

## 5.1. Padrão de resposta de continuidade

Quando o usuário perguntar **“Onde paramos? Qual a Estratégia Autônoma em curso? Qual a Fase dessa Estratégia Autônoma? E qual o Projeto?”** ou equivalente, responder:

```text
PROJETO: <PROJECT_CODE> — <PROJECT_NAME>
ALIAS: <PROJECT_ALIAS, quando existir>
ESTRATÉGIA AUTÔNOMA: <STRATEGY_CODE> — <STRATEGY_NAME>
FASE: <PHASE_NUMBER>/<PHASE_TOTAL> [<PHASE_CODE>] — <PHASE_NAME>
ESTADO: <estado comprovado>
ONDE PARAMOS: <ponto exato comprovado>
PRÓXIMO PASSO LÓGICO: <próximo passo comprovado>
```

## 6. Persistência progressiva

Trabalho substancial não deve permanecer somente no chat.

```text
PRODUZIR → SALVAR → VERIFICAR → ATUALIZAR ESTADO → CONTINUAR
```

## 7. Versionamento e verificabilidade

{{VERSIONING_RULES}}

Nunca afirmar salvamento, commit, push, publicação, envio ou implantação sem confirmação técnica correspondente.

## 8. Recuperação e não regressão

Diante de perda aparente:

> **RECUPERAR → VERIFICAR → RECONSTRUIR SOMENTE O QUE FALTA.**

Retomar sempre do estado mais avançado comprovado.

## 9. Regras específicas do projeto

{{PROJECT_SPECIFIC_RULES}}

## 10. Módulos ativados

{{MODULE_RULES_OR_REFERENCES}}

As regras obrigatórias dos módulos ativados devem ser materializadas nesta seção; não basta listar ou referenciar o nome do módulo.

Quando o módulo `publication` estiver ativado para conteúdo textual/editorial, incluir expressamente: Markdown como fonte textual canônica; HTML como publicação quando houver; JSON/JSONL somente quando existir função estruturada real e consumidor/processo identificável. É proibido criar JSON apenas para duplicar conteúdo ou metadados já adequadamente preservados no Markdown/HTML.
Quando o módulo `publication` estiver ativado **e o projeto publicar Modelos reutilizáveis**, incluir também expressamente:

- botão canônico **`COPIAR MODELO`** imediatamente acima do texto exato a ser copiado, sem elemento intermediário;
- cópia restrita ao corpo do Modelo;
- somente a edição vigente do Modelo disponível no Site Público;
- proibição de botões, links, cards, menus, rotas navegáveis ou outros portões públicos para edições anteriores;
- preservação histórica por Git ou mecanismo não publicado;
- gate de verificação que teste posição do botão, alvo da cópia e ausência de acesso público à edição superada.


Quando o módulo `web-site` estiver ativado, incluir expressamente:

- `SITE_ARCHITECTURE.md` e `SITE_STYLE_GUIDE.md`;
- menu global em todas as páginas;
- Home institucional enxuta por padrão, sem catálogo dos Menus;
- página **Mapa do Site** e link homônimo no rodapé de toda página pública;
- identidade visual exclusiva, definida por design tokens;
- escala tipográfica moderada: títulos apenas proporcionalmente maiores que o corpo, com limites responsivos e sem escala de display por padrão;
- Home empilhada no mobile quando houver mais de um bloco estrutural; overflow horizontal geral é falha;
- teste responsivo mínimo em 360 px, 390 px e 412 px;
- responsividade e acessibilidade básica;
- separação entre governança interna e camada pública;
- estados editoriais internos (monitoramento, triagem, pendência, critérios, gatilhos e pré-publicações) não aparecem no Site Público; coleções públicas listam apenas itens efetivamente publicados;
- gate de auditoria de navegação, rotas, mobile, links e identidade;
- avaliação explícita de **Notícias, Artigos e Observatório** em Sites de conhecimento/consulta/formação/pesquisa/análise/atualização;
- distinção funcional: Notícias = fatos e mudanças; Artigos = análise autoral e argumentação; Observatório = pesquisa cumulativa, visão sistêmica, sinais e lacunas;
- decisão explícita entre `TOP_LEVEL_SEPARATE`, `EDITORIAL_HUB`, `NESTED_CONTEXTUAL` e `NOT_APPLICABLE`;
- regra de que as três funções não precisam ser três itens independentes do menu;
- classificação editorial primária para evitar cópias redundantes entre as camadas.
- padrão **Coleção → Detalhe** para Notícias, Artigos e Observatório: página de índice/arquivo separada das páginas individuais; títulos dos itens são hiperlinks descritivos acompanhados de metadados e resumo curto.

Quando `research` estiver ativado junto com essas camadas, incluir também busca recorrente, horizon scanning, evidência viva, data de corte, critérios de relevância e distinção entre cadência de busca e gatilho de publicação. Quando `publication` estiver ativado, exigir metadados e transparência adequados ao tipo Notícias/Artigos/Observatório.

Quando o módulo `contact-protocol` estiver ativado, incluir expressamente:

- **Fale Conosco** no menu global;
- e-mail institucional e prefixo de protocolo;
- `CONTACT_STACK.md`;
- protocolo confirmado somente após aceite do backend;
- confirmação por e-mail somente após o recebimento confirmado;
- página de recibo `noindex,nofollow`;
- teste end-to-end antes de declarar o canal operacional;
- proibição de troca silenciosa de provedor;
- quando o padrão de referência for Classe e Massas, usar **Forminit + EmailJS**, salvo decisão expressa em contrário.

## 11. Estados e critérios de conclusão

{{STATE_MODEL_AND_DONE_CRITERIA}}

## 12. Fechamento obrigatório

Antes de declarar trabalho substancial concluído, confirmar conforme aplicável:

- arquivo canônico atualizado;
- estado atualizado;
- persistência confirmada;
- versionamento confirmado;
- remoto confirmado;
- publicação/implantação confirmada;
- próximo passo lógico registrado.

## 13. Regra máxima

> **Nunca obrigar o usuário a pagar novamente, com tempo, energia ou recursos, por falha de memória, persistência, continuidade, planejamento ou verificação do Modelo de IA.**
