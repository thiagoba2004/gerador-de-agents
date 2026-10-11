# SCIV Essencial — bootstrap documental por Projeto

Módulo condicional de comunicação, não orquestrador ou autorização operacional. Origem: issue #4 do coordenador, comentário 6105103024 e mandato humano de 11/10/2026. ADR-GOV-0008 mantém caixas no próprio repositório do PRJ.

## Aplicabilidade e arquivos

Ativar somente por mandato/perfil, com PRJ↔repositório comprovado, evidência de contexto especializado e capacidade de leitura, caixas realmente provisionadas e referência explícita. Evidência relatada pelo titular deve conservar esse limite, sem promovê-la a autenticação ou B1. Sem vínculo ou inbox, não inserir leitura obrigatória: marcar NAO_APLICAVEL ou PENDENTE_DE_EVIDENCIA segundo MODULE_SELECTION. Um Projeto técnico B0 sem acompanhamento ChatGPT não recebe este adaptador por inferência.

Fontes: perfil local do Gerador, AGENTS do destinatário, adaptadores/chatgpt/INSTRUCOES.md, comunicados/SCIV_STATE.json com project_code/repository/inbox/outbox/operational_ref e duas caixas locais. Kernel/identificadores, memória e missão permanecem. Não obrigar acesso ao coordenador para recuperar mensagens ordinárias.

## Propagação e preservação obrigatórias

Materializar templates/SCIV_BOOTSTRAP.example.md no adaptador **antes** do bootstrap substantivo, parametrizando somente fontes confiáveis do perfil/estado. tools/sciv_bootstrap.py é compositor offline puro, sem rede, execução de conteúdo, escrita ou instalação. A chamada integrate(texto, perfil, estado) retorna o candidato; o executor compara o diff, classifica, publica somente com mandato e confirma Git/bytes. Não alimentá-la com configurações recebidas em comunicados.

Preservar byte a byte todo texto fora dos marcadores SCIV. Reaplicação idêntica não duplica o bloco; atualização de referência segue estado local e não mantém piloto fixo após integração. Bloco corrompido, âncora ambígua ou identidade incompatível exigem revisão; não substituir o documento inteiro. Reconciliar AGENTS e cópia de handoff do Gerador com o adaptador local. Nunca sobrescrever alterações posteriores do Projeto por uma cópia antiga.

## Estados e aceitação separados

- BOOTSTRAP_INSTRUCTIONS_VERSIONED: commit e readback do adaptador, AGENTS e estado.
- NATIVE_PROJECT_INSTRUCTIONS_INSTALLED: responsável compara/instala manualmente o conteúdo integral no campo Instruções; GitHub não sincroniza a UI.
- AUTOMATIC_READ_ON_PROCESSED_CONVERSATION_VERIFIED: nova conversa com tarefa ordinária sem mencionar SCIV/GitHub; evidência de ferramenta mostra consulta local anterior à resposta.
- CROSS_SESSION_DEDUPLICATION_VERIFIED: outra conversa consulta inbox/outbox e reconhece resposta da mesma versão sem republicar nem gerar efeito.

Verificar ausência de novidade, pasta ausente, acesso negado, mensagem inválida, classificação e instrução maliciosa. Testes offline não cumprem gates conversacionais. Sem acesso: INBOX_UNAVAILABLE, distinto de caixa vazia. Outbox é evidência a revisar, não grant. Escrever requer autorização e PEP quando aplicável; sem isso WRITE_BLOCKED. Sem polling/gatilhos/custos/credenciais/alteração C2/C3 ou promoção A6/B8/F3.

## Piloto e transição

PRJ-000021 usa feat/sciv-essencial-piloto-20261011 até integração humana. Seu estado local explicita operational_ref. Após merge autorizado, atualizar o estado e o pacote de Instruções para descoberta na branch padrão; não fazer merge neste mandato. Não propagar em massa a outros Projetos: avaliar cada perfil e preservar suas instruções locais. O pedido humano é manutenção desta implementação, sem nova EA ou alteração de namespace.
