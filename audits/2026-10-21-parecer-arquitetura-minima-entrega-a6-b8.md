# Parecer técnico — Arquitetura mínima verificável para handoff A6/B8

**Data:** 21/10/2026 · **Projeto:** PRJ-000002 — Gerador de Agents · **Pedido:** `REQ-20261021-GDA-CHAT-002` · **Objetivo:** `OBJ-ENTREGA-5-IA-ESPECIALIZADA`.  
**Destinatário previsto:** Governança Geral, para avaliação e decisão estratégica.  
**Natureza:** avaliação de Engenharia de Software, formulação arquitetural e propostas; **não** altera políticas ou concessões G0, não instala software, não executa chats especializados e não concede aceites.  
**Fontes canônicas confrontadas:** `GERADOR_WORKFLOW.md` (A6/B8), `AGENTS_KERNEL.md`, `AGENTS.md`, `PROJECT_STATE.json`, `EA-000002-000027`; parecer e decisão G0 de F007 (21/10); `policies/POLITICA_VINCULO_ESTRATEGICO_ANTI_LOOP.md`, `direcao/2026-10-21-delegacao-cinco-projetos-gerador.md`; registros de recebimento dos cinco Projetos e checkpoint local `handoffs/governanca-geral/2026-10-21-sintese-execucao-cinco-projetos-gda.md`.

## 1. Juízo executivo

**Existe sobrecarga processual comprovável e risco elevado de circularidade.** A G0 reconheceu formalmente repetições de handoffs de engenharia, clones/ZIPs, CPD e comandos sem nexo com A6/B8. Há cinco recuperações documentais especializadas, quatro conjuntos julgados substancialmente suficientes e zero recibos positivos comprovados no checkpoint. O déficit prioritário não é inventário geral, novas EAs, código ou SCIV; é aceite formal pela IA destinatária, com B1 específico adicional para PRJ021.

A hipótese de **livelock operacional** (movimentos repetidos sem progresso terminal) é plausível, mas não foi formalmente provada por exploração completa de estados. O diagnóstico baseia-se em registros e nos mecanismos conhecidos. Não há base para atribuir toda demora a uma pessoa ou declarar que segurança é supérflua.

**Orientação arquitetural:** manter segurança e autoria do recebimento; simplificar o caminho crítico, preservar evidência histórica, modelar handoff por estados, tornar ações idempotentes, registrar bloqueios com precondição material e terminar cada execução com estado observável. Em vez de construir imediatamente um motor de workflow, iniciar com contrato e registros versionados já existentes.

## 2. Avaliação de obrigações

| Obrigação/controle | Diagnóstico | Decisão proposta |
| --- | --- | --- |
| Identidade PRJ, missão aprovada, destinatário competente, limitações/permissões e fonte canônica | Essencial para aceite verdadeiro | **MUST — manter**; recuperar por referências verificáveis e reaproveitar evidências |
| Vínculo B1, escolha humana C3 quando destino conversacional ChatGPT e manifestação positiva da própria IA | Essencial sob o contrato A6/B8 vigente | **MUST — manter**, admitindo a categoria real da prova humana/visual, sem exigir API administrativa inexistente |
| Registro do recibo, autoria/proveniência lógica, commit/readback quando escrita autorizada | Essencial para rastreabilidade, sem confundir commit com assinatura criptográfica | **MUST — manter**, com modelo conciso e fallback `NOT_PERSISTED` |
| Releitura integral de cinco auditorias após juízo F007 de suficiência | Retrabalho sem mudança factual demonstrada | **MUST NOT — repetir sem evidence_delta relevante** |
| Criar EA nova ou Plano de Fases apenas porque há tarefa de aceite | Aumenta estados e aprovações sem novo objetivo autônomo | **MUST NOT — criar por hábito**; vincular a EA vigente |
| Confirmar novamente C3/B1 nos quatro Projetos com atestação posterior já válida | Revalidação redundante | **SHOULD — reutilizar evidência**; revalidar só se houver contradição ou mudança relevante |
| Comprovar internamente isolamento de memória C3 via API não disponibilizada | Requisito possivelmente impossível com ferramentas atuais | **MUST NOT — impor sem contrato explícito e meio técnico existente**; relatar observação UI / atestação |
| Rodar SCIV, CPD, site Pages, symlink físico, novo checkout/ZIP | Não integra critério necessário A6/B8 nos cinco casos, segundo G0 | **MUST NOT — bloquear A6/B8 por essa trilha sem dependência causal nova e provada** |
| Emitir parecer em sete campos antes de cada ato simples (`POLITICA_VINCULO_ESTRATEGICO_ANTI_LOOP.md`) | Política contra loop, mas se invocada indiscriminadamente pode gerar metaprocesso e novos bloqueios | **SHOULD — adotar preflight conciso**, com parecer ampliado apenas para comando novo, excepcional, arriscado ou tecnicamente não óbvio |
| Registrar inclusive perguntas efêmeras/saudações antes de qualquer resposta (Kernel) | Custo linear de escrita remota e dependência adicional sem ganho comprovado em todos os casos | **PROPOR ALTERAÇÃO NORMATIVA G0**: registro persistente obrigatório para pedidos decisórios/alterações/efeitos; interação efêmera não produzir escrita por padrão, preservando auditabilidade dos atos materiais |
| Rodar testes técnicos genéricos para avaliar mera titularidade operacional | Sobreacoplamento de gate funcional com gate de handoff | **SHOULD — separar testes de software, de configuração e de recebimento** |
| Transmitir aceites de outros contêineres apenas por instrução em GitHub | Não aciona instância nem comprova manifestação | **MUST — requerer manifestação real da IA** ou integração explicitamente autorizada e comprovada |

**Importante:** linhas "MUST/SHOULD" são propostas arquiteturais, não política vigente automaticamente alterada. Segurança PEP/GVC, classificação S2+, autorizações e ação por executor continuam vinculantes.

## 3. Estado da arte e fundamento

1. **Soundness de workflow nets / Petri nets.** Correção exige ausência de deadlocks/livelocks e possibilidade de término, com tarefas vivas. Fonte: Liu, Reisig, Jiang & Zhou, *IEEE Access* 4 (2016), https://digitalcommons.njit.edu/fac_pubs/10922/ ; pesquisa adicional em https://www.sciencedirect.com/science/article/pii/S2352220824000117 . **Inferência de projeto:** evitar transições que regressem de `READY_FOR_ACCEPTANCE` a `AUDIT_REPEAT` sem fatos novos.
2. **Safety, liveness, fairness (Lamport).** Lamport, *A Science of Concurrent Programs*, cap. 4, Cambridge University Press (2026), https://www.cambridge.org/core/books/abs/science-of-concurrent-programs/safety-liveness-and-fairness/DFA4A361F8674D2978DAE8580F8A6A20 . **Inferência:** nenhum aceite falso (safety), e toda instância pronta com destinatário acessível e cooperação suficiente pode progredir para aceite ou bloqueio material (liveness condicional). Nenhuma arquitetura garante aceite humano sem cooperação/decisão.
3. **Google SRE / redução de toil.** https://sre.google/sre-book/eliminating-toil/ e https://sre.google/workbook/eliminating-toil/ . Trabalhos repetitivos, manuais e automatizáveis sem valor duradouro são desperdício operacional; reduzir reauditorias, evidência duplicada e repetições de comando.
4. **Idempotent Receiver / Unmesh Joshi (2023).** https://martinfowler.com/articles/patterns-of-distributed-systems/idempotent-receiver.html . Reentrega de pedido com mesmo ID deve retornar resultado já verificado, não executar o mesmo trabalho novamente.
5. **Saga / coordenação de transações locais.** https://learn.microsoft.com/en-us/azure/architecture/patterns/saga . Analogia arquitetural: cada IA mantém autonomia para aceitar ou negar, enquanto o Gerador acompanha decisões sem representar as participantes; não implica implementar mecanismo compensatório completo nem tratar aceite de IA como transação ACID.
6. **DORA 2025 e estudo 2026 sobre tradeoffs da IA.** https://dora.dev/research/2025/dora-report/ ; https://dora.dev/insights/balancing-ai-tensions/ . A adoção de IA amplifica condições do sistema de trabalho; tempo ganho na produção pode voltar como sobrecarga de verificação. Não é experimento causal específico sobre A6/B8.
7. **Requisitos normativos RFC 2119/8174 e YAGNI.** https://www.rfc-editor.org/info/rfc2119/ ; https://www.rfc-editor.org/info/rfc8174/ ; https://martinfowler.com/bliki/Yagni.html . Distinguir obrigação absoluta, recomendação e funcionalidade especulativa; não usar YAGNI para relativizar controles de segurança.

## 4. Arquitetura-alvo: MVHA — Mínimo Handoff Auditável

### 4.1 Responsabilidades e fronteiras
- **G0 (governança estratégica):** estabelece a política do gate, resolve riscos/autorizações não rotineiros; não é executor dos cinco recebimentos.
- **Gerador (orquestrador leve):** lê fonte canônica, reaproveita evidência, prepara pacote mínimo, decide próximo bloqueio, consolida estados e cobra apenas atos necessários; não fabrica recibos.
- **IA especializada (autoridade do recebimento):** em seu próprio Projeto ChatGPT, confronta as evidências pertinentes, pode aceitar ou rejeitar fundamentadamente e emite recibo; assume o primeiro trabalho de domínio.
- **Titular/HUMAN:** confirma o que depende realmente da configuração/identidade nativa e dá eventual decisão humana indelegável; não executa comandos técnicos repetitivos.
- **GitHub:** registro imutável em commits e logs append-only de fonte, decisão, recibo, versão e readback; não é transporte automático para conversas.
- **CODEX/WORK:** executores de ações específicas por autorização/catálogo, não requisitos universais do A6/B8. SCIV permanece subsystem opcional separado, `enabled=false` respeitado.

### 4.2 Estados de cada handoff
```text
IDENTIFIED
   -> TECHNICAL_BOOTSTRAP_VERIFIED / MIGRATION_VERIFIED
   -> EVIDENCE_READY
   -> RECIPIENT_DECISION_PENDING
   -> ACCEPTED [positivo da própria IA + registro + readback]
   \-> MATERIAL_BLOCKED [bloqueio específico + owner + precondição + evidência]

MATERIAL_BLOCKED -> RECIPIENT_DECISION_PENDING
    somente se a precondição relevante mudar ou surgir prova nova.
```
`ACCEPTED` é terminal para o handoff naquela versão; novo escopo/migração posterior produz revisão versionada, não edição retroativa. `MATERIAL_BLOCKED` encerra a **tentativa**, não conta como entrega aceita.

### 4.3 Contrato mínimo do recibo
```json
{
  "receipt_version": "1.0",
  "handoff_id": "PRJ-000022/A6/2026-10-21",
  "project_code": "PRJ-000022",
  "gate": "A6",
  "recipient_context": "CHATGPT_PROJECT_PRJ-000022",
  "decision": "ACCEPTED",
  "source_revision": "<git-commit-ou-referencia-verificada>",
  "evidence_refs": ["<relatorio-primario>", "<B1/C3-atestacao>"],
  "mission_and_limits_acknowledged": true,
  "first_operational_step": "<acao-local-limitada>",
  "receipt_authority": "RECIPIENT_SPECIALIZED_AI",
  "receipt_persisted_ref": "<caminho-e-commit>",
  "readback_verified": true
}
```
Campos são **contrato conceitual**: strings ilustrativas, não recibo real; a prova B1/C3 precisa ser identificável e datada; não expor prova privada em repositório público. `receipt_authority` textual não é autenticação de identidade. Se a ferramenta disponível não puder escrever, marcar `NOT_PERSISTED` e manter pendência. Se o texto não vier da IA real no contexto destinatário, **não aceitar**.

### 4.4 Formalização de invariantes
```text
S1: ACCEPTED(p) =>
    RecipientAckInOwnContext(p)
    AND ValidMissionAndLimits(p)
    AND B1_C3_WhenApplicable(p)
    AND EvidenceProvenance(p)
    AND AuthorizedCanonicalReceiptWithReadback(p)

S2: SCIV_DISABLED(p) => NO_SCIV_BOX_READ_OR_WRITE(p)

S3: SAME_ACTION_FINGERPRINT_AND_NO_NEW_EVIDENCE =>
    NO_REPEAT_OF_IDENTICAL_SUBSTANTIVE_ACTION

S4: NONCRITICAL_DEPENDENCY_BLOCKED =>
    HANDOFF_STATE_NOT_REGRESSED

L1: If EvidenceReady(p) and RecipientAccessible(p)
    and RecipientCooperates(p), the process must have a
    path to ACCEPTED(p) or MATERIAL_BLOCKED(p)
    without reiterating unchanged audits.
```
L1 é **propriedade condicional de possibilidade/progresso**, não promessa de aceite garantido independente de atores humanos.

### 4.5 Algoritmo mínimo operacional
```text
para cada PRJ autorizado:
  recuperar snapshot e decisao de suficiencia ja produzida
  if recibo positivo valido e readback comprovado:
      manter ACCEPTED; nao repetir
  else:
      obter somente missing_critical_evidence(prj)
      if prova faltante depende do titular:
          solicitar uma intervencao minima identificada
      elif contexto destinatario esta apto:
          submeter decisao curta a IA destinataria, em seu contêiner
      else:
          MATERIAL_BLOCKED com owner, precondicao e alternativa
      if a propria destinataria aceitou e recibo foi persistido:
          verificar readback e promover ACCEPTED
      else:
          manter HANDOFF_PENDING
  registrar delta real sem reabrir etapas ja verificadas
```
A checagem de permissões e do executor acontece antes de cada acesso/efeito, por catálogo; o pseudocódigo não é autorização de publicação ou acionamento de outros chats.

## 5. Decoupling e caminho crítico

**DAG do objetivo de entrega:** mandato/identidade -> evidência de missão/estado/competência -> configuração aplicável/B1 -> manifestação positiva da IA -> recibo/commit/readback -> `ACCEPTED`. O Gerador coordena cinco cadeias **independentes** e consolida os cinco resultados.

**Fora do DAG por ausência de dependência comprovada:** ativação SCIV, funcionamento de mensagens, site Pages, CPD, novos clones, symlink físico, automação APSP/MOGP, refatorações, microserviços e novos testes não relacionados. Não eliminar tais trabalhos de seus próprios planos; apenas desacoplá-los do handoff.

**Bootstrap em duas trilhas:** A1–A5/B1–B7 constitui/migra a base documental; A6/B8 atribui efetivamente um novo dono. Um resultado técnico não prova o outro. A execução de estudos setoriais começa somente depois do ato da IA correspondente, conforme suas permissões.

## 6. Mudanças propostas à G0, em ordem

| Prioridade | Decisão G0 proposta | Resultado |
| --- | --- | --- |
| P0 | Aprovar **contrato mínimo A6/B8**, com conjunto de invariantes acima e recibo breve emitido no próprio Projeto | Mantém rastreabilidade com menos redundância |
| P0 | Ratificar oficialmente **evidence reuse**: prova válida com revisão e proveniência não exige auditoria integral; revalidar somente `evidence_delta` material | Elimina reauditorias |
| P0 | Separar SCIV/CPD/Pages/symlink do DAG de handoff, salvo dependência documentada | Impede bloqueios laterais |
| P0 | Fixar no caminho crítico só quatro decisões positivas de IAs e B1 específico + decisão do PRJ021 (missão/EA002 já reconciliados) | Foco em 5/5 aceites verdadeiros |
| P1 | Reduzir o preflight anti-loop de sete campos para uma classificação interna ou justificativa de 2–3 frases **apenas quando há novo comando não trivial ao titular/executor**; preservar avaliação completa para risco, novidade e efeito material | Evita metamovimentos e mantém controle |
| P1 | Diferenciar **pedido persistente de conversa efêmera** no Kernel, com política de exceção explícita e rastreabilidade dos atos decisórios | Reduz escritas sem valor |
| P1 | Adotar `action_fingerprint` e supressão idempotente de ações sem mudança de precondição | Bloqueia repetição sem progresso |
| P2 | Introduzir verificador determinístico pequeno dos invariantes e uma visualização derivada do estado Git, **somente se houver repetição demonstrada que justifique o código** | Automação incremental, sem infraestrutura especulativa |

Qualquer alteração das políticas globais, do Kernel ou da definição normativa de aceite depende de decisão G0/titular e executor/rota autorizados; este parecer não muda o mandato vigente por si.

## 7. Critérios verificáveis e experimento antes/depois

**Métricas de resultado:** número de aceites reais `0..5`; lead time entre `EVIDENCE_READY` e `ACCEPTED`; tempo bloqueado por dependência; proporção de retrabalho sem `evidence_delta`; contatos humanos por aceite; tempo de processamento por IA; aceites indevidos (alvo zero). Não usar commits, pareceres, comandos ou número de EAs como proxy de entrega.

**Critérios de teste da arquitetura**:
- um relatório negativo nunca promove aceite;
- B1/C3 já válidos não geram nova exigência idêntica;
- `enabled=false` jamais libera SCIV;
- bloquear Pages não impede B8 independente;
- repetir pedido com mesmo fingerprint devolve checkpoint, não auditoria;
- mudar realmente B1 de 021 libera apenas a próxima decisão correspondente;
- sem destinatário acessível a tentativa para em `MATERIAL_BLOCKED`, sem fabricar manifestação;
- dois Projetos independentes podem avançar isoladamente, sem "all or nothing";
- o recebimento real cria recibo e readback; caso contrário, permanece pendente.

Aplicar primeiro em **modo documental** aos cinco Projetos, sem construir produto novo. Observar se a redução de retrabalho ocorre e se os aceites são efetivamente concluídos. Só depois cogitar verificador/código em nova frente autorizada.

## 8. Estado preciso dos cinco e primeira ação
- `PRJ-000021` A6: missão aprovada de 10/10 conciliada com EA002/estado em `02f1457941374e095af49ca2c21085808bec2440`; falta B1 **da conversa específica** + manifestação/recibo positivo da IA. Titular atesta B1 se não houver prova recuperável; IA 021 decide.
- `PRJ-000022` A6: diagnóstico e B1/C3 supervenientes aproveitáveis; falta só manifestação positiva atual, sem reauditar; IA 022 decide.
- `PRJ-000023` A6: C3 já aprovado em REQ local; falta só manifestação positiva atual; IA 023 decide.
- `PRJ-000007` B8: Pages não é bloqueio B8; falta manifestação positiva atual; IA 007 decide.
- `PRJ-000008` B8: Pages não é bloqueio B8; falta manifestação positiva atual; IA 008 decide.

**Intervenção humana mínima:** abrir cada contêiner ChatGPT já existente uma vez e solicitar a decisão curta, salvo recibo positivo primário já recuperável. Para 021 confirmar B1 específico. Custo = acesso aos contêineres, não conjunto de auditorias. Não há ferramenta nesta sessão para enviar mensagens em nome das outras IAs. Não propor cinco capturas nem nova instalação C3 sem prova de falha. A condição terminal da carteira permanece **5/5**; atualmente **0/5**, sem inventar homologação.

## 9. Recomendação de deliberação estratégica

**Que a G0 adote normativamente o princípio: "O único bloqueio legítimo do handoff A6/B8 é uma precondição indispensável ao recebimento efetivo, com evidência de sua ausência, owner e caminho de superação. Atividades úteis mas independentes seguem nos próprios planos, sem poder de veto sobre o aceite."**

Aprovar **arquitetura documental de estado e contrato mínimo**, com evidência reutilizável, recibo especializado e regras anti-loop proporcionais; não ordenar implantação de software antes de constatar necessidade. Manter autoria, segurança e readback. Este parecer está **PRONTO_PARA_SUBMISSAO_G0**, não é decisão G0 recebida.
