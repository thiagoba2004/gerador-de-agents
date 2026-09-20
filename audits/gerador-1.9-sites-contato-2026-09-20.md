# Autoauditoria — Gerador 1.9 — Sites e Contato Protocolado

**Data:** 20/09/2026  
**Estratégia:** EA-000002-000007 — Padrão reutilizável de Sites e Contato Protocolado  
**Kernel:** 1.4  
**Release:** 1.9

## 1. Problema identificado

A implantação piloto dos Sites Ações Judiciais e Planejamento Financeiro revelou que o Gerador possuía módulos de `publication` e `software`, mas não possuía uma camada normativa própria para:

- arquitetura de informação de Site;
- menu global;
- papel da Home;
- Mapa do Site;
- identidade visual própria;
- responsividade/acessibilidade;
- separação entre governança interna e UI pública;
- Fale Conosco protocolado;
- definição e preservação da stack técnica de recebimento/retorno;
- teste end-to-end do protocolo.

A ausência permitiu decisões ad hoc e a troca indevida de stack do Fale Conosco: o padrão do Classe e Massas usa **Forminit + EmailJS**, enquanto os dois projetos piloto receberam **FormSubmit**.

## 2. Correções implantadas no Gerador

- criado `modules/web-site.md`;
- criado `modules/contact-protocol.md`;
- atualizado `MODULE_SELECTION.md`;
- atualizado `GERADOR_WORKFLOW.md`;
- atualizado `templates/AGENTS.example.md`;
- atualizado `templates/PROJECT_PROFILE.example.json`;
- atualizado `modules/README.md`;
- atualizados `modules/publication.md` e `modules/software.md` para explicitar as fronteiras dos módulos;
- atualizado `AGENTS.md` do Gerador com propagação obrigatória;
- atualizados perfis de Classe e Massas, Ações Judiciais e Planejamento Financeiro;
- registrada decisão arquitetural em `DECISIONS.md`;
- release do Gerador elevada para **1.9**.

## 3. Padrão de Site consolidado

Quando `web-site` estiver ativo, o AGENTS do projeto-alvo deve materializar:

1. arquitetura multipágina;
2. menu global consistente;
3. Home institucional enxuta por padrão;
4. Mapa do Site em página própria;
5. link **Mapa do Site** no rodapé de todas as páginas públicas;
6. identidade visual exclusiva;
7. design tokens documentados;
8. responsividade e acessibilidade básica;
9. páginas centrais com conteúdo real;
10. separação entre governança interna e UI;
11. `SITE_ARCHITECTURE.md`;
12. `SITE_STYLE_GUIDE.md`;
13. gate de auditoria pública.

## 4. Padrão de contato consolidado

Quando `contact-protocol` estiver ativo:

1. Fale Conosco integra o menu global;
2. `CONTACT_STACK.md` é obrigatório;
3. e-mail institucional e prefixo de protocolo são registrados;
4. protocolo só é confirmado após aceite do backend;
5. e-mail de retorno só é tentado depois do recebimento confirmado;
6. teste end-to-end é obrigatório;
7. troca silenciosa de provedor é proibida.

Quando a determinação for “mesmo padrão do Classe e Massas”:

```text
Forminit = recebimento/aceite da submissão e anexos
EmailJS  = confirmação do protocolo ao remetente
```

## 5. Migração dos projetos piloto

### PRJ-000003 — Ações Judiciais

- AGENTS migrado para Gerador 1.9;
- módulos `web-site` e `contact-protocol` materializados;
- `SITE_STYLE_GUIDE.md` criado;
- `CONTACT_STACK.md` criado;
- FormSubmit classificado como divergência;
- migração para Forminit + EmailJS pendente da estratégia local EA-000003-000003.

### PRJ-000004 — Planejamento Financeiro

- AGENTS migrado para Gerador 1.9;
- módulos `web-site` e `contact-protocol` materializados;
- `SITE_STYLE_GUIDE.md` criado;
- `CONTACT_STACK.md` criado;
- contradição da Home corrigida;
- FormSubmit classificado como divergência;
- migração para Forminit + EmailJS pendente da estratégia local EA-000004-000003.

## 6. Verificações

| Verificação | Resultado |
|---|---|
| módulo web-site existe e é selecionável | OK |
| módulo contact-protocol existe e é selecionável | OK |
| template de AGENTS propaga ambos | OK |
| workflow pergunta requisitos de Site e contato | OK |
| template de perfil possui campos de Site/contato | OK |
| perfis AJ/PF registram stack canônica e divergência atual | OK |
| AGENTS AJ possui menu/Home/Mapa/identidade/stack | OK |
| AGENTS PF possui menu/Home/Mapa/identidade/stack | OK |
| numeração dos capítulos dos AGENTS piloto | OK |
| FormSubmit tratado como padrão aprovado | NÃO — corretamente classificado como divergência |
| Forminit + EmailJS registrado como referência CEM | OK |
| teste E2E dos dois novos contatos | PENDENTE — pertence às estratégias locais após migração |

## 7. Conclusão

O gate da Estratégia EA-000002-000007 está satisfeito.

A lacuna do **Gerador** foi eliminada. O que permanece pendente não é normativo: é a migração técnica dos dois formulários públicos para a stack canônica e a posterior verificação end-to-end em cada projeto-alvo.
