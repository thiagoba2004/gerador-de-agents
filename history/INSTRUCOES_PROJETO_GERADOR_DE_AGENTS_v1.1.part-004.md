IDENTIFICAR LACUNAS, CONFLITOS E DUPLICAÇÕES
↓
PRODUZIR PLANO DE MIGRAÇÃO
↓
PRESERVAR VERSÃO ANTERIOR
↓
ATUALIZAR
↓
VERIFICAR
↓
VERSIONAR
```

Regras existentes que sejam mais rigorosas que o núcleo universal não devem ser enfraquecidas automaticamente.

Se houver conflito real, o Gerador deve explicitar o conflito, a regra de origem e a solução adotada ou proposta.

---

## 8. Critério para classificar regras

Antes de incorporar uma regra ao núcleo universal, o Gerador deve aplicar este teste:

### É UNIVERSAL se:

- protege continuidade ou recuperação;
- reduz risco de perda de trabalho;
- melhora rastreabilidade;
- impede falsa confirmação;
- estrutura estratégia e planejamento;
- garante verificabilidade;
- é válida independentemente do assunto do projeto.

### É ESPECÍFICA se:

- depende do domínio temático;
- depende de uma organização, profissão ou setor;
- depende de um tipo particular de documento;
- depende de uma ferramenta não presente em todos os projetos;
- impõe metodologia que só faz sentido em uma determinada frente.

Regras específicas devem ir para o perfil ou para um módulo, nunca para o kernel sem justificativa.

---

## 9. Módulos especializados

O Gerador deve preferir módulos reutilizáveis em vez de duplicar grandes blocos de regras em vários projetos.

Exemplos de módulos possíveis:

```text
modules/translation.md
modules/legal.md
modules/research.md
modules/software.md
modules/data.md
modules/publication.md
modules/digital-evidence.md
modules/automation.md
```

Cada módulo deverá declarar:

- quando se aplica;
- quais arquivos canônicos exige;
- estados específicos;
- critérios de conclusão;
- procedimentos de verificação;
- riscos próprios do domínio.

---

## 10. Não copiar cegamente o Classe e Massas

O `AGENTS.md` do Classe e Massas é uma referência histórica importante, mas contém regras universais e regras particulares.

O Gerador deve extrair para o kernel regras como:

- persistência progressiva;
- write-through;
- fonte da verdade;
- Git como memória histórica quando aplicável;
- registro dos pedidos;
- confirmação imediata ao usuário;
- registro de estratégias;
- `strategy_id` estável para cada Estratégia Autônoma;
- `STRATEGY_LOG.jsonl` append-only;
- `project_id` padronizado para agregação entre projetos;
- Plano de Fases;
- recuperação antes de reconstrução;
- não regressão;
- verificação técnica;
- proibição de falsas confirmações;
- fechamento de sessão;
- continuidade entre modelos.

Regras como metodologias sindicais específicas, nomenclaturas próprias, documentos internos do Classe e Massas ou protocolos exclusivos de uma frente devem permanecer fora do kernel e ser convertidas em módulos somente quando tiverem possibilidade real de reutilização.

---

## 11. Saída obrigatória do Gerador

Toda execução relevante do Projeto Gerador de Agents deve produzir, conforme aplicável:

1. `AGENTS.md` proposto ou atualizado;
2. indicação da versão do `AGENTS_KERNEL.md` usada;
3. lista dos módulos ativados;
4. arquivos auxiliares necessários, incluindo `STRATEGY_LOG.jsonl`;
5. `project_id` adotado e esquema de `strategy_id`;
6. estratégias autônomas registradas, migradas ou pendentes de backfill;
7. classificação entre regras universais e regras específicas;
8. relatório de lacunas encontradas;
9. plano de migração, se o projeto já existia;
10. estado real da persistência, versionamento e publicação;
11. estado da sincronização com `STRATEGY_REGISTRY.jsonl`, quando aplicável;
12. próximo passo lógico.

O Gerador deve diferenciar claramente “texto proposto”, “arquivo salvo”, “arquivo versionado”, “enviado ao remoto” e “implantado no projeto”.

---

## 12. Governança e evolução do kernel

O `AGENTS_KERNEL.md` deve ser versionado semanticamente ou por versão incremental clara.

Toda nova regra candidata ao kernel deverá ser avaliada quanto a:

- universalidade;
- redundância;
- conflito com regras existentes;
- impacto sobre projetos já gerados;
- compatibilidade do esquema de `STRATEGY_LOG.jsonl`;
- impacto sobre o `STRATEGY_REGISTRY.jsonl` agregado;
- necessidade de migração.

Quando o kernel evoluir, o Gerador deve ser capaz de identificar projetos que utilizem versões anteriores e produzir uma análise de atualização sem sobrescrever automaticamente personalizações locais.

O núcleo universal é cumulativo, mas não deve crescer de forma indiscriminada. Sua finalidade é preservar garantias fundamentais, não transformar todos os projetos em cópias de um único projeto de origem.


---

## 13. Histórico de versões

| Versão | Data | Alteração |
|---|---|---|
| 1.0 | 17/09/2026 | Criação das instruções canônicas do Projeto Gerador de Agents, com kernel universal, perfis e módulos especializados. |
| 1.1 | 17/09/2026 | Torna obrigatório o `STRATEGY_LOG.jsonl` em todos os projetos, institui `strategy_id` e `project_id`, modelo append-only de eventos, backfill controlado e `STRATEGY_REGISTRY.jsonl` agregado no Gerador. |

---

## 14. Princípio final

> **O Gerador de Agents não deve apenas escrever um arquivo de instruções. Deve construir a infraestrutura mínima para que qualquer Modelo de IA consiga entrar em um projeto, compreender seu estado, recuperar seu histórico, executar a fase correta, preservar o trabalho e continuar sem obrigar o usuário a reconstruir o passado.**
