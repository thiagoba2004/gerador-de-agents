# Modules

Módulos especializados reutilizáveis do Gerador de Agents.

Cada módulo deve declarar, no mínimo:

1. quando se aplica;
2. quais arquivos canônicos exige;
3. estados específicos;
4. critérios de conclusão;
5. procedimentos de verificação;
6. riscos próprios do domínio.

A ativação de qualquer módulo deve seguir `../MODULE_SELECTION.md` e ser registrada no perfil do projeto com evidência suficiente.

## Módulos atualmente disponíveis

- `research.md` — pesquisa documental, bibliográfica, normativa, histórica, científica ou jornalística;
- `legal.md` — análise e produção jurídica substantiva;
- `publication.md` — fluxos editoriais e publicação em destinos públicos;
- `digital-evidence.md` — preservação, integridade e rastreabilidade de prova digital;
- `translation.md` — tradução com fonte, revisão e controle terminológico;
- `software.md` — código, scripts, APIs, testes e implantação;
- `data.md` — coleta, transformação, análise e validação de dados estruturados;
- `automation.md` — agendas, gatilhos, monitoramentos, pipelines e ações automáticas;
- `professional-education.md` — formação, certificações, competências e separação prova/prática.

Módulos não são ativados globalmente só por existirem neste diretório. Cada projeto deve classificá-los como `ATIVADO`, `NAO_APLICAVEL` ou `PENDENTE_DE_EVIDENCIA` conforme as fontes examinadas.


## Módulos de interface pública

- `web-site.md` — arquitetura de Site, menus, Home, Mapa do Site, identidade visual, responsividade, acessibilidade e separação público/interno.
- `contact-protocol.md` — Fale Conosco, protocolo, backend de recebimento, confirmação por e-mail e testes end-to-end.
