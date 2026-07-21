# Prompt: Chat Do Browser Para Context Passport

Use este prompt dentro de um chat longo no ChatGPT, Claude, Gemini ou outra IA no navegador.

O objetivo e transformar a conversa em um arquivo de transferencia de contexto para continuar o trabalho em outra IA.

Voce nao precisa instalar nada, usar Git, API ou plugin. E so copiar e colar.

Copie e cole:

```text
Quero transformar esta conversa em um Context Passport.

Context Passport e um resumo estruturado para eu conseguir levar este trabalho para outra IA sem perder o contexto.

Antes de gerar o documento final, verifique se esta conversa mistura varios temas diferentes.

Se houver varios temas, faca primeiro um "Mapa de Temas" com:

- nome de cada tema;
- resumo em uma frase;
- status de cada tema;
- se o tema merece um Context Passport separado;
- qual tema parece ser o principal.

Depois disso:

- se existir apenas um tema principal, gere um Context Passport focado nele e coloque os outros temas em uma secao chamada "Temas paralelos ou fora de escopo";
- se existirem varios temas importantes, recomende quais Context Passports separados eu deveria gerar e pergunte se quero gerar todos ou apenas um;
- se eu tiver pedido explicitamente um tema especifico, ignore os demais e gere apenas o passaporte desse tema.

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
```

## Como usar

1. Abra o chat antigo.
2. Cole o prompt acima.
3. Copie a resposta gerada.
4. Cole a resposta em um arquivo de texto chamado `context-passport.md`. Voce nao precisa saber Markdown para usar.
5. Abra outra IA.
6. Cole o prompt de retomada que veio no final.
7. Anexe ou cole o `context-passport.md`.

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
