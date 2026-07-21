# Como usar no browser

Este guia e para quem usa IA pelo navegador e quer levar o contexto de uma conversa para outra IA.

Voce nao precisa instalar nada.

## Caso simples

Use quando a conversa tem um tema principal.

1. Abra o chat antigo.
2. Abra o prompt em portugues: [`prompts/pt-BR/chat-do-browser-para-context-passport.md`](../../prompts/pt-BR/chat-do-browser-para-context-passport.md).
3. Copie o texto dentro do bloco "Copie e cole".
4. Cole no final do chat antigo.
5. Se voce estiver no ChatGPT, peca para ele gerar um arquivo `context-passport.md` para download, quando disponivel.
6. Se a IA nao gerar arquivo, copie o bloco de texto que ela escreveu.
7. Salve esse conteudo em um arquivo de texto chamado `context-passport.md`, ou cole diretamente na nova IA.
8. Abra a nova IA.
9. Cole o prompt de retomada que veio no final do `context-passport.md`.
10. Anexe ou cole o `context-passport.md`.

Pronto. A nova IA deve conseguir continuar o trabalho.

## Se o chat mistura muitos assuntos

Use quando a conversa tem varios temas no mesmo chat.

Exemplos:

- um projeto de trabalho;
- uma duvida de aula;
- uma ideia de produto;
- uma revisao de texto;
- uma pergunta pessoal.

Nesse caso, nao gere um Context Passport unico para tudo.

Faca assim:

1. Abra o chat antigo.
2. Cole o prompt em portugues.
3. A IA deve criar primeiro um **Mapa de Temas**.
4. Escolha qual tema voce quer levar para outra IA.
5. Peca: `Agora gere o Context Passport do tema [nome do tema].`
6. Salve a resposta como `context-passport-[tema].md`.
7. Leve esse arquivo para a nova IA.

## Como saber se funcionou

Depois de colar o Context Passport na nova IA, ela deve conseguir responder:

- qual era o objetivo;
- o que ja foi decidido;
- qual e o status atual;
- quais sao as pendencias;
- qual e o proximo passo.

Se a nova IA nao conseguir responder isso, o passaporte ficou fraco e deve ser gerado novamente com mais detalhes.

## Como o arquivo e entregue

No ChatGPT pelo browser ou desktop, e comum conseguir pedir um arquivo real para download, como `context-passport.md`. A propria documentacao da OpenAI fala em arquivos criados no ChatGPT e salvos na Biblioteca.

Claude e Gemini tambem documentam recursos de criacao ou download de arquivos em superficies compatíveis. Mesmo assim, o comportamento pode variar conforme ferramenta, plano, workspace, tipo de arquivo e interface.

Por isso, existem dois caminhos validos:

1. **Com download:** se a plataforma criar `context-passport.md`, baixe o arquivo e leve para a nova IA.
2. **Sem download:** se a plataforma nao criar arquivo, ela deve mostrar o conteudo no chat dentro de um bloco copiavel. Copie esse bloco e cole na nova IA ou salve manualmente como `context-passport.md`.

O prompt foi escrito para priorizar arquivo quando a plataforma suportar e usar copia/cola como fallback. Ele nao deve prometer link falso: so deve oferecer link quando o arquivo existir de verdade.

## Quando pode falhar

O processo funciona melhor quando a IA ainda consegue acessar o contexto importante da conversa antiga.

Pode falhar ou ficar incompleto quando:

- o chat antigo e longo demais;
- a conversa misturou muitos assuntos;
- arquivos ou imagens foram citados, mas a IA nao consegue mais acessa-los;
- partes importantes estavam em anexos que nao foram incluidos;
- a IA gerou um resumo generico demais;
- o Context Passport foi levado para outra IA sem o prompt de retomada.

Se isso acontecer, use uma destas saidas:

1. Peca primeiro um **Mapa de Temas**.
2. Gere um Context Passport por tema.
3. Cole trechos importantes do chat antigo junto com o prompt.
4. Inclua os arquivos ou anexos importantes quando possivel.
5. Na nova IA, pergunte: `Com base neste Context Passport, o que ainda esta incerto?`

## O que nao colocar

Antes de levar o arquivo para outra IA, revise se ele tem:

- senhas;
- tokens;
- chaves de API;
- dados pessoais desnecessarios;
- informacoes confidenciais que nao deveriam sair da ferramenta original.

Se tiver, remova antes de compartilhar.
