# MODULE SELECTION — POLÍTICA DE ATIVAÇÃO DE MÓDULOS

**kernel_version:** `1.2`

O Gerador de Agents deve selecionar módulos especializados por evidência do projeto, nunca por associação vaga ou preferência do modelo.

## 1. Estados possíveis

Cada módulo avaliado deve receber exatamente um estado:

- `ATIVADO` — há evidência suficiente de que o domínio ou fluxo faz parte do projeto;
- `NÃO APLICÁVEL` — o domínio não integra o escopo comprovado;
- `PENDENTE DE EVIDÊNCIA` — há sinais insuficientes ou contraditórios; não ativar até confirmação documental.

## 2. Regra de decisão

Um módulo pode ser `ATIVADO` quando pelo menos uma das condições abaixo for comprovada:

1. o projeto declara explicitamente aquele domínio como parte de sua finalidade;
2. arquivos canônicos demonstram trabalho recorrente no domínio;
3. o usuário determina explicitamente que aquele fluxo fará parte do projeto;
4. entregas, riscos ou ferramentas do projeto exigem regras especializadas daquele módulo.

A mera possibilidade futura não basta.

## 3. Registro obrigatório

Toda decisão deve registrar:

```text
module_id
status
rationale
source_refs
decided_at
kernel_version
```

A decisão pode ser persistida no perfil do projeto ou em arquivo estruturado próprio.

## 4. Matriz inicial de módulos

### `research`

Ativar quando houver pesquisa documental, bibliográfica, jornalística, normativa, histórica, científica ou coleta sistemática de fontes.

### `legal`

Ativar quando o projeto produzir ou analisar conteúdo jurídico substantivo: legislação, jurisprudência, doutrina, peças, pareceres, contratos, denúncias ou teses jurídicas.

### `publication`

Ativar quando houver publicação editorial, site, blog, newsletter, repositório público de artigos ou outro fluxo com estado distinto entre produção e publicação.

### `digital-evidence`

Ativar quando houver coleta, preservação, autenticação, hashing, cadeia de custódia, arquivamento ou apresentação de prova digital.

### `translation`

Ativar quando tradução integral, parcial ou recorrente for uma entrega real do projeto, especialmente quando fidelidade terminológica, revisão e controle de versão forem relevantes.

### `software`

Ativar quando código-fonte, scripts, automações, APIs, testes, implantação ou manutenção de software fizerem parte do projeto.

### `data`

Ativar quando análise, transformação, modelagem, validação ou visualização de dados estruturados for atividade recorrente ou crítica.

### `automation`

Ativar quando o projeto depender de tarefas agendadas, gatilhos, monitoramento recorrente, pipelines ou ações automáticas.

## 5. Regras de combinação

Módulos não são mutuamente exclusivos. Um projeto jurídico com pesquisa documental e publicação pode ativar `legal`, `research` e `publication` simultaneamente.

Quando duas regras de módulos entrarem em conflito:

1. identificar o conflito;
2. aplicar a regra mais específica para o risco concreto, se compatível com o kernel;
3. registrar a decisão em `DECISIONS.md` ou equivalente;
4. nunca enfraquecer uma garantia universal do kernel.

## 6. Desativação ou revisão

Módulos ativados não devem ser removidos apenas porque uma conversa atual não os utiliza. A desativação exige evidência de mudança material do escopo do projeto e deve ser registrada.
