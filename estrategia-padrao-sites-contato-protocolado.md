# Estratégia EA-000002-000007 — Padrão reutilizável de Sites e Contato Protocolado

## Objetivo

Eliminar lacunas do Gerador relativas a arquitetura pública, layout, navegação, identidade visual, separação público/interno e Fale Conosco protocolado.

## Plano de Fases

### FASE 01/05 [F-000002-000007-001] — Auditoria e delimitação
Inventariar regras atuais do Gerador e dos projetos piloto; comparar com o Site Classe e Massas; identificar lacunas e divergências técnicas.

### FASE 02/05 [F-000002-000007-002] — Módulos reutilizáveis
Criar módulos `web-site` e `contact-protocol`, com critérios de ativação, arquivos canônicos, estados, testes e riscos.

### FASE 03/05 [F-000002-000007-003] — Propagação do Gerador
Atualizar AGENTS do Gerador, MODULE_SELECTION, template, workflow, documentação de módulos, changelog e perfis.

### FASE 04/05 [F-000002-000007-004] — Migração dos projetos piloto
Atualizar AGENTS, arquitetura e documentação de PRJ-000003 e PRJ-000004; registrar a divergência do stack de contato e plano de migração para Forminit+EmailJS.

### FASE 05/05 [F-000002-000007-005] — Verificação e fechamento
Auditar propagação, ausência de contradições, seleção de módulos, perfis, template e projetos-alvo; atualizar estado/release e encerrar.
