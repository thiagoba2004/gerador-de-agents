# Módulo: Information Classification

**module_id:** `information-classification`

## Finalidade

Aplicar a Classificação Universal de Informação por Sensibilidade e Publicação antes de qualquer persistência, upload, commit ou publicação.

## Eixos

### Sensibilidade

- `S0_PUBLICO`
- `S1_INTERNO_NAO_SENSIVEL`
- `S2_CONFIDENCIAL`
- `S3_ALTAMENTE_SENSIVEL`
- `S4_SEGREDO_CRITICO`

### Superfície

- `P0_COFRE_EXTERNO`
- `P1_GIT_PRIVADO`
- `P2_GIT_PUBLICO_REPOSITORIO`
- `P3_PUBLICO_SITE`

## Regras universais

1. `S2+` nunca pode ir a `P2` ou `P3`.
2. Documento bruto `S3` usa `P0` por padrão; Git privado recebe apenas derivado minimizado quando necessário.
3. `S4` nunca entra em Git, Biblioteca, chat, Markdown, JSON, logs ou contexto do Modelo.
4. Rebaixamento de sensibilidade exige derivado sanitizado; o original preserva sua classe.
5. Repositório público é superfície pública mesmo sem link no Site.
6. Git privado não é cofre documental.
7. Mudança de visibilidade, ativação de Pages ou alteração de destino reabre o gate.

## Perfil obrigatório

Projetos persistentes devem manter `INFORMATION_HANDLING_PROFILE.json` com:

- visibilidade do repositório;
- superfície;
- estado do Pages;
- classes permitidas/proibidas;
- destino para documentos S3;
- política de segredos;
- necessidade de auditoria retroativa.

## Manifesto

Quando houver coleção de documentos classificados, usar manifesto estruturado com identificador, classe, superfície, estado de sanitização e publicação permitida, sem reproduzir o dado sensível.
