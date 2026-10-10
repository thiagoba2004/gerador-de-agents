# Verificação da Rota B — Constituição pública PRJ-000007 / PRJ-000008

**Data:** 10/10/2026  
**Gerador:** PRJ-000002 · **Estratégia:** EA-000002-000024 · **Autoridade:** REQ-20261010-001  
**Método:** leitura remota de arquivos na `main` pelo conector GitHub, parsing JSON/JSONL e comparação de escopo, links, identidade e logs. **Não houve execução de build/testes de aplicativo, auditoria integral do histórico ou confirmação de Pages.**

## Baseline e resultado

| Critério | Conselhos Profissionais | Ordem dos Advogados |
|---|---|---|
| Projeto | PRJ-000007 | PRJ-000008 |
| Repositório GitHub | `thiagoba2004/conselhos-profissionais` | `thiagoba2004/ordem-dos-advogados` |
| Visibilidade observada | PUBLIC | PUBLIC |
| Estado anterior | `GOVERNANCE_BASELINE_ESTABLISHED` | `GOVERNANCE_BASELINE_ESTABLISHED` |
| Estratégia local nova e concluída | EA-000007-000001 | EA-000008-000001 |
| Gate local | `PUBLIC_DOCUMENTARY_CONSTITUTION_VERIFIED` | `PUBLIC_DOCUMENTARY_CONSTITUTION_VERIFIED` |
| Estado após constituição | `PUBLIC_DOCUMENTARY_CONSTITUTION_VERIFIED` | `PUBLIC_DOCUMENTARY_CONSTITUTION_VERIFIED` |

Os repositórios **não estavam tecnicamente vazios**: possuíam AGENTS, ROADMAP, STATE, logs e gate local criados na EA-000000-000019; todos foram preservados. O GDA aplicou a **Rota B** para completar uma base documental pública específica, não a Rota A com alocação de novos códigos.

## Evidências lidas nos dois repositórios

- `README.md`: entrada pública que apresenta projeto **independente e não oficial**, missão, limites e links canônicos.
- `MISSAO_E_ESCOPO.md`: finalidades aprovadas, escopo próprio, agenda de pesquisa **proposta e não executada**.
- `POLITICA_FONTES_E_PUBLICACAO.md`: critérios de pesquisa, verificação jurídica, separação entre versão Git e publicação em site e proibições para conteúdo confidencial.
- `AGENTS.md`: preservado e complementado por seção de missão, perfil de módulos e regras de sigilo.
- `INFORMATION_HANDLING_PROFILE.json`: JSON parseável; superfície `P2_GIT_PUBLICO_REPOSITORIO`, S2+ vedado; status `pages.enabled = null` (desconhecido, **não** considerado false sem prova).
- `REQUEST_LOG.jsonl`: registro do mandato confirmado; JSONL parseável e preservado.
- `STRATEGY_LOG.jsonl`: abertura, atualização e um único evento de conclusão da EA local; JSONL parseável.
- `ROADMAP.md` e `estrategias/EA-...-000001-constituicao-publica.md`: quatro fases numeradas, limites, gate e primeiro objetivo de pesquisa posterior; sem reescrever história.
- `PROJECT_STATE.json`: sem Estratégia local ativa após fechamento; próxima pesquisa depende de decisão de priorização e fontes verificadas.

### Decisões de módulos pelo Gerador

Perfis `profiles/conselhos-profissionais.json` e `profiles/ordem-dos-advogados.json`, derivação do Kernel `1.11`:
- **ATIVADO:** `research`, `legal`, `publication` documental, `information-classification`, `execution-environments`.
- **PENDENTE_DE_EVIDENCIA:** `knowledge-index`, `web-site`, `contact-protocol`, `software`, `data`, `automation`, `digital-evidence`, `professional-education`.
- **NAO_APLICAVEL no escopo atual:** `translation`.

Não se infere do status de GitHub público um Site GitHub Pages configurado, formulário, meio de cobrança ou publicação jurídica substantiva. Não é demonstrado vínculo institucional com entidades reais.

## Limites, débitos e segurança

1. **Corpus substantivo:** ainda não pesquisado, verificado ou publicado. Cada novo produto requer mandato local, triagem, fontes oficiais, data e revisão.
2. **Publicação web:** não foi criado website, workflow, página GitHub Pages, e-mail ou canal de contato; não foi executado teste HTTP de eventual destino.
3. **Histórico de segurança:** foram avaliados arquivos e conteúdo novos, mas **não** houve varredura integral de Git history para material privado antigo; não prometer ausência absoluta.
4. **Custo:** nenhuma despesa nova, execução produtiva em serviço externo, credencial ou deploy autorizados/acionados por este ciclo.
5. **Independência:** os projetos são fontes de pesquisa independentes, **não oficiais**; OAB não é tratada como simples conselho equivalente aos demais.

## Conclusão

**`TWO_PUBLIC_PROJECT_CONSTITUTIONS_VERIFIED`**, exclusivamente no escopo **DOCUMENTARY_PUBLIC_GITHUB** e com evidências de readback/JSON/JSONL. A fase seguinte é escolher trabalho **substantivo real** em cada Projeto com fontes e critérios, e não aprofundar o Gerador sem demanda. Sem nova Estratégia Global, sem reabertura de EA-000000-000019 e sem alterações à Academia Nacional de Concursos.
