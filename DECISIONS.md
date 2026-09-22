# DECISIONS — GERADOR DE AGENTS

## ADR-001 — Repositório independente

**Data:** 17/09/2026  
**Estado:** ACEITA

O Gerador de Agents será mantido fora do repositório Classe e Massas, em `thiagoba2004/gerador-de-agents`.

**Motivo:** o Gerador é infraestrutura reutilizável para múltiplos projetos e não deve ficar subordinado a um domínio específico.

---

## ADR-002 — Arquitetura em três camadas

**Data:** 17/09/2026  
**Estado:** ACEITA

A arquitetura será composta por:

1. `AGENTS_KERNEL.md` — núcleo universal;
2. `profiles/` — perfil de cada projeto;
3. `modules/` — módulos especializados reutilizáveis.

**Consequência:** regras setoriais não entram no kernel sem demonstração de universalidade.

---

## ADR-003 — Registro obrigatório de pedidos antes do processamento

**Data:** 17/09/2026  
**Estado:** ACEITA

A ordem operacional obrigatória passa a ser:

```text
registrar pedido
→ confirmar tecnicamente
→ informar “Pedido registrado.”
→ informar leitura/análise/providências
→ executar
```

Esta decisão substitui a ordem anterior da instrução canônica v1.1, que previa uma mensagem antes do registro persistente.

---

## ADR-004 — Estratégias com identidade estável e log append-only

**Data:** 17/09/2026  
**Estado:** ACEITA

Toda Estratégia Autônoma possuirá `strategy_id` estável e eventos append-only em `STRATEGY_LOG.jsonl`. Cada projeto possuirá `project_id` estável.

O `STRATEGY_REGISTRY.jsonl` será apenas índice agregado reconstruível; o log local permanece fonte primária.

---

## ADR-005 — Plano de Fases obrigatório

**Data:** 17/09/2026  
**Estado:** ACEITA

Toda Estratégia Autônoma deverá possuir Plano de Fases explícito, com estado, objetivo e gate quando aplicável.

---

## ADR-006 — Git como memória histórica preferencial

**Data:** 17/09/2026  
**Estado:** ACEITA

Quando disponível, Git será a memória histórica preferencial. Estados como produzido, salvo, versionado, enviado ao remoto e publicado/implantado permanecem distintos.


## DEC-20260920-SITE-CONTACT — Site e Fale Conosco como módulos próprios

**Decisão:** arquitetura/UI de Site e contato protocolado deixam de ser regras ad hoc de `publication`/ `software` e passam a módulos reutilizáveis próprios: `web-site` e `contact-protocol`.

**Razão:** os projetos piloto revelaram lacunas recorrentes em menus, papel da Home, Mapa do Site, identidade visual e escolha de provedores de formulário.

**Padrão de referência para “igual ao Classe e Massas”:** Forminit para recebimento confirmado e EmailJS para confirmação do protocolo ao remetente.

**Consequência:** FormSubmit implantado nos projetos piloto é classificado como divergência técnica e deve ser migrado antes da verificação end-to-end.

## DEC-20260922-EDITORIAL-LAYERS — Notícias, Artigos e Observatório como camadas editoriais transversais

**Data:** 22/09/2026  
**Estado:** ACEITA

**Decisão:** Sites com vocação de conhecimento, consulta, formação, pesquisa, análise ou atualização devem avaliar explicitamente três funções editoriais distintas: **Notícias**, **Artigos** e **Observatório**.

**Fronteiras:** Notícias tratam mudança factual/temporal; Artigos tratam análise autoral/argumentativa; Observatório trata pesquisa cumulativa, inteligência, visão sistêmica, sinais e lacunas.

**Arquitetura:** a existência das três funções não obriga três itens independentes no primeiro nível. O projeto deve escolher e registrar `TOP_LEVEL_SEPARATE`, `EDITORIAL_HUB`, `NESTED_CONTEXTUAL` ou `NOT_APPLICABLE`. Em Sites já densos e com funções transversais, `EDITORIAL_HUB` é a hipótese preferencial a testar, não uma imposição automática.

**Publicação:** cada conteúdo possui função editorial primária. Uma mesma evidência pode alimentar mais de uma camada, mas não deve gerar cópias redundantes.

**Pesquisa:** monitoramento periódico separa cadência de busca de gatilho de publicação; Observatórios adotam, quando material, horizon scanning e lógica de evidência viva.

**Consequência:** perfis de projeto passam a registrar `editorial_architecture`, e o Mapa do Site deve expor as camadas públicas mesmo quando agrupadas sob hub.


## DEC-20260922-COLLECTION-DETAIL — Separação entre coleção e conteúdo individual

**Data:** 22/09/2026  
**Estado:** ACEITA

**Decisão:** Notícias, Artigos e Observatório públicos adotam, por padrão, arquitetura **Coleção → Detalhe**. A página da seção é um índice/arquivo para descoberta e comparação; cada conteúdo possui URL individual própria.

**Regra de interface:** o título é o hiperlink principal. Metadados e resumo/subtítulo fornecem pistas suficientes sobre o conteúdo antes do clique. Evitar “Leia mais” como único link.

**Consequência:** índices não acumulam textos integrais; Markdown e HTML seguem a mesma granularidade; Observatório organiza snapshots/relatórios/unidades temáticas como objetos individuais.
