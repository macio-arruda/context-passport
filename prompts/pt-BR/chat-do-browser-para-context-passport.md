# Prompt: Chat Do Browser Para Context Passport

Use este prompt dentro de um chat longo no ChatGPT, Claude, Gemini ou outra IA no navegador.

O objetivo e transformar a conversa em um arquivo de transferencia de contexto para continuar o trabalho em outra IA.

Voce nao precisa instalar nada, usar Git, API ou plugin. E so copiar e colar.

Recomendacao: para conversas longas, importantes ou com muitos temas, selecione o modelo mais capaz ou o modo de raciocinio mais forte disponivel antes de colar o prompt.

Copie e cole:

```text
Quero transformar esta conversa em um Context Passport.

Context Passport e um resumo estruturado para eu conseguir levar este trabalho para outra IA sem perder o contexto.

Use raciocinio cuidadoso. Priorize precisao, separacao de temas, decisoes tomadas, pendencias e contexto necessario para continuidade.

Antes de gerar o documento final, verifique se esta conversa mistura varios temas diferentes.

Se houver varios temas, faca primeiro um "Mapa de Temas" com:

- nome de cada tema;
- resumo em uma frase;
- status de cada tema;
- se o tema merece um Context Passport separado;
- qual tema parece ser o principal.

Depois siga esta regra de decisao:

- se existir apenas um tema principal, gere um Context Passport focado nele e coloque os outros temas em uma secao chamada "Temas paralelos ou fora de escopo";
- se existirem varios temas importantes e eu nao tiver pedido um tema especifico, pare depois do Mapa de Temas e pergunte qual passaporte eu quero gerar primeiro;
- se eu tiver pedido explicitamente um tema especifico, ignore os demais e gere apenas o passaporte desse tema.

Nao misture temas diferentes em um unico Context Passport so para terminar em uma resposta.

Gere um documento em texto Markdown com estas secoes:

1. Titulo
2. Objetivo original da conversa
3. Como o objetivo mudou ao longo do tempo
4. Cronologia dos acontecimentos importantes
5. Informacoes confirmadas
6. Suposicoes ou pontos incertos
7. Decisoes tomadas
8. Caminhos descartados ou deixados para depois
9. Status atual
10. Pendencias e perguntas abertas
11. Riscos ou cuidados importantes
12. Preferencias de tom, estilo e forma de trabalho do usuario
13. Fontes, arquivos, links ou anexos mencionados
14. Proximas acoes recomendadas
15. Prompt de retomada para colar em outra IA

Regras:

- Separe fatos confirmados de suposicoes.
- Separe temas diferentes em blocos diferentes. Nao misture decisoes de um tema com outro.
- Nao invente informacoes que nao apareceram na conversa.
- Se algum arquivo, link ou anexo foi citado mas voce nao consegue acessar, diga isso claramente.
- Remova ou sinalize dados sensiveis, senhas, chaves de API, credenciais e informacoes privadas desnecessarias.
- Escreva de forma clara para que outra IA consiga continuar o trabalho sem ler a conversa inteira.
- No final, inclua um prompt curto que eu possa colar em outra IA junto com este Context Passport.

Formato de entrega:

- Se esta plataforma permitir gerar arquivo para download, prefira criar um arquivo chamado `context-passport.md`.
- Se nao for possivel gerar arquivo para download, entregue o conteudo completo no proprio chat dentro de um unico bloco de codigo Markdown.
- Antes do bloco, escreva: `Arquivo sugerido: context-passport.md`.
- Nao invente link de download. So ofereca link se o arquivo tiver sido realmente criado pela plataforma.
- Depois do bloco, escreva uma instrucao curta: `Copie o bloco acima, salve como context-passport.md ou cole diretamente na nova IA.`
```

## Como usar

1. Abra o chat antigo.
2. Cole o prompt acima.
3. Veja se a IA entregou um arquivo para download ou um bloco de texto no chat.
4. Se voce estiver no ChatGPT, peca preferencialmente um arquivo `context-passport.md` para download.
5. Se nao gerar arquivo, copie o bloco de texto e cole em um arquivo chamado `context-passport.md`. Voce nao precisa saber Markdown para usar.
6. Abra outra IA.
7. Cole o prompt de retomada que veio no final.
8. Anexe ou cole o `context-passport.md`.

Pronto: a nova IA tera o contexto essencial sem precisar ler todo o historico bruto.

## Se o chat tiver muitos assuntos misturados

Use este prompt alternativo primeiro:

```text
Esta conversa mistura varios assuntos. Antes de gerar qualquer Context Passport, crie um Mapa de Temas.

Para cada tema encontrado, informe:

1. Nome do tema
2. Resumo em uma frase
3. Principais decisoes
4. Status atual
5. Pendencias
6. Se vale gerar um Context Passport separado

No final, recomende quais passaportes eu deveria gerar e em que ordem.
```
