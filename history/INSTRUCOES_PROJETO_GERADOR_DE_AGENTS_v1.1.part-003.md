NÃO INICIADO
EM PREPARAÇÃO
EM EXECUÇÃO
EM REVISÃO
REVISADO
PRONTO PARA ENTREGA
CONCLUÍDO
PUBLICADO / IMPLANTADO, quando aplicável
ARQUIVADO
```

“Produzido no chat”, “salvo”, “versionado”, “enviado ao remoto” e “publicado” são estados diferentes.

### 3.16. Continuidade entre conversas, agentes e modelos

O projeto não pode depender da hipótese de que o próximo modelo terá acesso ao contexto atual.

Os arquivos persistentes devem permitir reconstruir:

- objetivo do projeto;
- arquitetura;
- estratégia vigente;
- fases;
- estado atual;
- último marco concluído;
- pendências;
- pedido mais recente;
- próximo passo lógico.

### 3.17. Autonomia com verificabilidade

O agente deve executar diretamente o trabalho mecânico que puder realizar com ferramentas autorizadas, sem transferir desnecessariamente tarefas ao usuário.

Essa autonomia nunca autoriza opacidade, improvisação estratégica ou afirmações não verificadas.

### 3.18. Checkpoints e atualizações

Em trabalhos prolongados, o agente deve informar periodicamente o avanço e indicar se o estado produzido já foi persistido.

Uma atualização intermediária não deve ser apenas narrativa; deve deixar claro o estado real de preservação do trabalho.

### 3.19. Fechamento obrigatório

Antes de declarar uma operação substancial concluída, verificar, conforme aplicável:

- arquivo canônico atualizado;
- estado/manifesto atualizado;
- persistência confirmada;
- versionamento realizado;
- remoto confirmado;
- publicação/implantação confirmada;
- segunda cópia de marcos críticos, quando necessária;
- próximo passo lógico registrado.

### 3.20. Regra máxima

> **Nunca obrigar o usuário a pagar novamente, com tempo, energia ou recursos, por falha de memória, persistência, continuidade, planejamento ou verificação do Modelo de IA.**

---

## 4. Pacote canônico preferencial de cada projeto

O Gerador de Agents deve avaliar a complexidade do projeto e, salvo justificativa em contrário, criar ou recomendar a seguinte estrutura mínima:

```text
AGENTS.md
REQUEST_LOG.jsonl
STRATEGY_LOG.jsonl
PROJECT_STATE.json
ROADMAP.md ou PLAN.md
DECISIONS.md, quando houver decisões arquiteturais ou metodológicas relevantes
```

Projetos simples podem fundir arquivos, mas não podem eliminar as funções essenciais: regras, registro de pedidos, estado, planejamento e histórico de decisões.

Quando houver Git, o repositório deve ser a memória histórica preferencial. Quando não houver, o Gerador deve indicar mecanismo persistente equivalente.

---

## 5. Fonte canônica do próprio Gerador de Agents

O próprio Projeto Gerador de Agents deverá manter:

```text
AGENTS_KERNEL.md
STRATEGY_LOG.jsonl
STRATEGY_REGISTRY.jsonl
modules/
profiles/
templates/
CHANGELOG.md
```

`AGENTS_KERNEL.md` será a fonte da verdade das regras universais.

A pasta `modules/` conterá módulos especializados reutilizáveis.

A pasta `profiles/` poderá registrar o perfil de cada projeto para o qual um `AGENTS.md` tenha sido gerado.

A pasta `templates/` conterá estruturas reutilizáveis de arquivos auxiliares como `REQUEST_LOG.jsonl`, `STRATEGY_LOG.jsonl`, `PROJECT_STATE.json` e `ROADMAP.md`.

O `STRATEGY_LOG.jsonl` do próprio Gerador registrará suas estratégias autônomas. O `STRATEGY_REGISTRY.jsonl` funcionará como índice agregado das estratégias conhecidas dos projetos gerados ou auditados, sem substituir os logs locais.

O `CHANGELOG.md` registrará toda alteração material no núcleo universal.

Todo `AGENTS.md` gerado deverá registrar, quando possível, a versão do núcleo que lhe deu origem, por exemplo:

```text
generated_from_kernel: 1.0
```

Isso permitirá identificar quais projetos precisam ser atualizados quando o núcleo universal evoluir.

---

## 6. Procedimento para NOVO projeto

Quando o usuário pedir a criação do Agents de um novo projeto, o Gerador deverá:

1. identificar nome, finalidade e tipo do projeto;
2. identificar onde o trabalho será persistido;
3. identificar se existe Git/repositório ou outro mecanismo de versionamento;
4. identificar formatos canônicos e tipos de artefatos;
5. identificar ferramentas, integrações e restrições relevantes;
6. identificar riscos de perda, segurança, publicação ou operações destrutivas;
7. aplicar integralmente o núcleo universal;
8. selecionar apenas os módulos especializados realmente aplicáveis;
9. definir o perfil específico do projeto;
10. atribuir um `project_id` estável;
11. criar `STRATEGY_LOG.jsonl` e seu esquema padronizado;
12. gerar o `AGENTS.md` final e os arquivos auxiliares necessários;
13. registrar versão, origem do kernel e data;
14. verificar se as instruções geradas são executáveis pelas ferramentas realmente disponíveis;
15. quando houver acesso ao Gerador central, registrar o projeto no `STRATEGY_REGISTRY.jsonl`.

O Gerador não deve inventar capacidades, repositórios, integrações ou fluxos que não existam.

---

## 7. Procedimento para projeto JÁ EXISTENTE

Ao adaptar um projeto em curso, o Gerador não deve simplesmente substituir o `AGENTS.md` existente.

A sequência obrigatória é:

```text
LER O AGENTS EXISTENTE
↓
LER OS ARQUIVOS DE ESTADO E PLANEJAMENTO
↓
LOCALIZAR OU CRIAR O STRATEGY_LOG.jsonl
↓
INVENTARIAR ESTRATÉGIAS AUTÔNOMAS COMPROVÁVEIS, USANDO BACKFILLED QUANDO NECESSÁRIO
↓
IDENTIFICAR REGRAS JÁ EXISTENTES
↓
COMPARAR COM O NÚCLEO UNIVERSAL
↓
PRESERVAR REGRAS ESPECÍFICAS VÁLIDAS
↓
