# Como usar no browser

Este guia e para quem usa IA pelo navegador e quer levar contexto para outra IA.

Voce nao precisa instalar nada.

Existem dois modos principais:

- **uma conversa especifica:** quando o trabalho esta concentrado em um chat antigo;
- **contexto acessivel:** quando o trabalho esta espalhado em projeto, memoria, arquivos ou conversas anteriores que a ferramenta consegue referenciar.

## Modo 1: uma conversa especifica

Use quando a conversa tem um tema principal.

1. Abra o chat antigo.
2. Abra o prompt em portugues: [`prompts/pt-BR/chat-do-browser-para-context-passport.md`](../../prompts/pt-BR/chat-do-browser-para-context-passport.md).
3. Se puder escolher, use o modelo mais capaz ou o modo de raciocinio mais forte disponivel.
4. Copie o texto dentro do bloco "Copie e cole".
5. Cole no final do chat antigo.
6. Se voce estiver no ChatGPT, peca para ele gerar um arquivo `context-passport.md` para download, quando disponivel.
7. Se a IA nao gerar arquivo, copie o bloco de texto que ela escreveu.
8. Salve esse conteudo em um arquivo de texto chamado `context-passport.md`, ou cole diretamente na nova IA.
9. Abra a nova IA.
10. Cole o prompt de retomada que veio no final do `context-passport.md`.
11. Anexe ou cole o `context-passport.md`.

Pronto. A nova IA deve conseguir continuar o trabalho.

## Modo 2: contexto acessivel

Use quando voce quer fazer o que muita gente faz no ChatGPT: abrir um chat novo dentro de um projeto ou workspace e pedir para a IA levantar o que ela consegue encontrar sobre um tema.

Esse modo serve para casos como:

- "busque tudo que voce sabe sobre este projeto";
- "levante todos os temas de IA generativa que discutimos";
- "crie um handoff da pre-venda do Metro de Sao Paulo";
- "olhe os chats e arquivos deste projeto e diga quais passaportes devo gerar".

Use o prompt:

[`prompts/pt-BR/contexto-acessivel-para-context-passport.md`](../../prompts/pt-BR/contexto-acessivel-para-context-passport.md)

Passo a passo:

1. Abra um chat novo na ferramenta onde o contexto ja existe.
2. Se for ChatGPT, prefira fazer isso dentro do projeto correto, quando houver um projeto.
3. Use o modelo mais capaz ou o modo de raciocinio mais forte disponivel.
4. Cole o prompt de contexto acessivel.
5. Peca primeiro um **Inventario de Contexto**, nao o passaporte final.
6. Revise os temas encontrados, fontes, nivel de confianca e lacunas.
7. Escolha qual tema deve virar passaporte.
8. Peca para gerar `context-passport-[tema].md`.
9. Leve esse arquivo para a outra IA.

Fluxo:

> contexto acessivel -> Inventario de Contexto -> Context Passport focado -> nova IA

Esse modo nao e uma exportacao magica de todos os chats. Ele depende do que a ferramenta consegue realmente acessar naquele momento, das configuracoes de memoria, do plano, do projeto, dos arquivos anexados e do historico disponivel.

Se o inventario vier fraco ou incompleto, faca um reforco manual:

1. Use a busca do ChatGPT, Claude, Gemini ou da ferramenta original.
2. Procure por palavras-chave do tema.
3. Abra os chats relevantes.
4. Cole trechos importantes no chat que esta gerando o inventario.
5. Gere novamente o Inventario de Contexto.

## Escolha do modelo

A qualidade do Context Passport depende da qualidade do modelo que vai ler a conversa antiga.

Para chats simples, um modelo rapido pode funcionar. Para conversas longas, temas misturados, decisoes importantes, contexto sensivel ou varredura de contexto acessivel, prefira o modelo mais forte disponivel.

No ChatGPT, isso significa usar Thinking, maior nivel de raciocinio ou Pro quando estiver disponivel. A documentacao atual da OpenAI descreve Instant como uma opcao rapida para tarefas do dia a dia, Thinking como raciocinio mais profundo para tarefas complexas, e Pro como a opcao de maior capacidade para tarefas dificeis e fluxos longos.

Em resumo:

- chat simples: modelo rapido pode bastar;
- chat longo ou importante: use modelo mais capaz;
- varios temas misturados: use raciocinio mais forte e gere primeiro um Mapa de Temas;
- contexto espalhado em projeto/historico: gere primeiro um Inventario de Contexto.

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
- a IA nao tem permissao/configuracao para referenciar chats, memorias, projetos ou arquivos antigos;
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
