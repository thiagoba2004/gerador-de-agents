# Módulo: Contact Protocol

**module_id:** `contact-protocol`

## Quando se aplica

Ativar quando um Site Público possuir formulário **Fale Conosco**, canal de recebimento de mensagens, denúncias, dúvidas, documentos ou colaboração com geração de protocolo e/ou confirmação por e-mail.

## Arquivos canônicos exigidos

Quando ativado, manter:

- página pública `fale-conosco/`;
- página de confirmação/recibo;
- `CONTACT_STACK.md` ou configuração equivalente descrevendo provedores, IDs públicos, destinatário, prefixo de protocolo, limites e estados de ativação;
- referência ao e-mail institucional no perfil do projeto;
- procedimento de teste end-to-end.

Segredos reais nunca devem ser versionados em repositório público. Chaves explicitamente públicas de SDK podem ser registradas somente quando o provedor as classificar como públicas e a arquitetura exigir uso no cliente.

## Padrão de referência: Classe e Massas

Quando o projeto adotar o padrão **“igual ao Fale Conosco do Classe e Massas”**, a expressão significa **stack técnica e comportamento**, não apenas aparência.

Stack de referência:

```text
Forminit = recebimento/aceite da submissão e anexos
EmailJS  = envio da confirmação do protocolo ao e-mail informado pelo visitante
Página de confirmação = exibição do protocolo após aceite do Forminit
```

É proibido substituir silenciosamente essa stack por FormSubmit, outro backend ou serviço diferente. Mudança de provedor exige decisão expressa, persistida e aprovada no projeto-alvo.

## Regras obrigatórias

### 1. Separação entre recebimento e confirmação

1. O protocolo pode ser preparado no cliente antes do envio.
2. Ele **só pode ser apresentado como protocolo confirmado depois que o backend de recebimento retornar sucesso**.
3. Falha de recebimento não pode produzir página que diga “mensagem recebida”.
4. O protocolo identifica a comunicação; não significa análise, aceite do conteúdo ou resposta.

### 2. Protocolo

1. Cada projeto deve possuir prefixo próprio.
2. O formato deve combinar, no mínimo, prefixo + data + hora + componente aleatório/único.
3. O mesmo protocolo deve:
   - acompanhar a submissão recebida;
   - aparecer na página de confirmação;
   - ser enviado ao e-mail de retorno, quando informado.
4. A página de confirmação deve oferecer **Copiar protocolo**.
5. A página de confirmação deve usar `noindex,nofollow`.

### 3. E-mail de retorno

1. O e-mail de retorno é opcional, salvo decisão específica do projeto.
2. Se informado, a confirmação deve ser tentada **somente depois do backend confirmar o recebimento**.
3. Falha no e-mail não invalida protocolo de submissão já aceita.
4. A página de confirmação deve distinguir:
   - protocolo confirmado + e-mail enviado;
   - protocolo confirmado + falha no e-mail;
   - protocolo confirmado + nenhum e-mail informado.
5. Nunca declarar que o e-mail foi enviado sem retorno técnico de sucesso do provedor.

### 4. Isolamento entre projetos

1. Cada Site deve possuir e-mail institucional próprio.
2. Formulários/backends devem possuir roteamento isolado por projeto.
3. Não reutilizar `FORM_ID` do projeto de referência se isso fizer mensagens de outro Site cair no mesmo destino ou banco lógico, salvo decisão expressa.
4. IDs de serviço/template podem ser compartilhados somente quando a configuração foi projetada para múltiplos projetos e o isolamento do destinatário foi comprovado.

### 5. Anexos e segurança básica

1. Registrar limite total de anexos e tipos aceitos conforme o provedor real.
2. Validar tamanho antes do envio quando tecnicamente possível.
3. Usar honeypot ou mecanismo anti-spam compatível.
4. Não solicitar senhas ou dados sensíveis desnecessários.
5. Informar que processamento pode envolver provedor externo.
6. Não prometer sigilo absoluto sem base operacional/jurídica.

### 6. Estados operacionais

Distinguir explicitamente:

```text
DESENHADO
FRONTEND_IMPLEMENTADO
BACKEND_NAO_CONFIGURADO
BACKEND_CONFIGURADO
TESTE_DE_SUBMISSAO_OK
TESTE_DE_EMAIL_OK
E2E_VERIFICADO
```

`FRONTEND_IMPLEMENTADO` nunca equivale a `E2E_VERIFICADO`.

### 7. Teste end-to-end obrigatório

Antes de declarar o Fale Conosco operacional:

1. enviar submissão real de teste;
2. confirmar sucesso do backend;
3. verificar que o protocolo recebido é o mesmo exibido;
4. informar um e-mail de retorno e confirmar chegada do mesmo protocolo;
5. verificar comportamento sem e-mail;
6. testar falha simulada ou, no mínimo, garantir que erro não redireciona para confirmação falsa;
7. testar anexos quando essa função for publicada;
8. registrar data, provedores, IDs públicos usados e evidência de resultado.

## Critério de conclusão

O Fale Conosco só atinge estado **E2E_VERIFICADO** quando recebimento e confirmação por e-mail forem tecnicamente comprovados, usando a stack aprovada do projeto.

## Riscos próprios

- trocar provedor sem aprovação;
- gerar protocolo sem submissão aceita;
- confirmar e-mail sem evidência;
- reutilizar formulário de outro projeto e misturar mensagens;
- expor segredo em frontend;
- declarar canal operacional apenas porque o HTML existe;
- página de confirmação acessível por URL sem vínculo com recebimento real;
- limite de anexos divergente do provedor.
