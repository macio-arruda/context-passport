# Prompt: Contexto Acessivel Para Context Passport

Use este prompt em um chat novo ou em um projeto quando voce quer criar um Context Passport a partir do contexto que a ferramenta consegue referenciar, em vez de migrar uma conversa por vez.

Isso e util quando o trabalho esta espalhado em chats de projeto, memorias, conversas anteriores, arquivos enviados ou um workspace de uso continuo.

Importante: este e um fluxo de varredura de contexto acessivel. A IA nao deve afirmar que pesquisou ou exportou tudo se a plataforma nao der esse acesso. Se o acesso for limitado, ela deve dizer o que ficou faltando e orientar como voce pode levantar o material manualmente.

Recomendacao: selecione o modelo mais capaz ou o modo de raciocinio mais forte disponivel antes de colar o prompt.

Copie e cole:

```text
Quero criar um Context Passport a partir do contexto que esta acessivel para voce nesta ferramenta de IA, nao apenas a partir deste chat atual.

Context Passport e um documento estruturado de transferencia de contexto para eu continuar um trabalho em outra IA sem perder objetivos, decisoes, restricoes, pendencias e status atual.

Primeiro, nao gere ainda o passaporte final.

Comece criando um Inventario de Contexto.

Use apenas contexto que voce realmente consegue referenciar neste workspace, como:

- esta conversa atual;
- conversas anteriores que voce tem permissao de referenciar;
- memoria do projeto;
- arquivos do projeto;
- memorias salvas;
- instrucoes disponiveis neste workspace;
- qualquer fonte que eu cole ou anexe aqui.

Nao diga que varreu todos os chats, projetos, arquivos ou memorias se voce nao tiver esse nivel de acesso.

Crie um Inventario de Contexto com estas secoes:

1. Escopo que eu pedi
2. Fontes de contexto que voce consegue acessar ou inferir
3. Fontes de contexto que voce nao consegue acessar
4. Inventario de temas
5. Nivel de confianca por tema
6. Lacunas ou fontes ausentes
7. Termos de busca manual sugeridos, se necessario
8. Context Passports recomendados
9. Qual passaporte deveria ser gerado primeiro e por que

Para cada tema, inclua:

- nome do tema;
- resumo em uma frase;
- fonte ou local provavel;
- status atual;
- decisoes importantes ja conhecidas;
- perguntas abertas;
- se o tema deve virar um Context Passport separado.

Depois do inventario, pare e me pergunte qual passaporte eu quero gerar primeiro.

Se eu ja tiver indicado um tema especifico, gere o Inventario de Contexto desse tema e pergunte se pode seguir para o passaporte final.

Quando eu aprovar um tema especifico, gere um documento Markdown com estas secoes:

1. Titulo
2. Objetivo do passaporte
3. Objetivo original do usuario
4. Como o objetivo evoluiu
5. Cronologia dos acontecimentos importantes
6. Informacoes confirmadas
7. Suposicoes e pontos incertos
8. Decisoes tomadas
9. Caminhos descartados ou deixados para depois
10. Status atual
11. Perguntas abertas
12. Riscos e cuidados
13. Preferencias de tom, estilo e forma de trabalho do usuario
14. Fontes, arquivos, links e anexos relevantes
15. Termos e definicoes
16. Proximas acoes recomendadas
17. Prompt de retomada para outra IA

Regras:

- Separe fatos confirmados de suposicoes.
- Separe temas nao relacionados. Nao force varios projetos em um unico passaporte.
- Deixe visiveis as limitacoes de fonte.
- Nao inclua senhas, credenciais, tokens, chaves privadas ou dados pessoais desnecessarios.
- Se arquivos ou anexos foram mencionados mas nao estao acessiveis, diga isso claramente.
- Escreva de forma util para uma pessoa e para outro agente de IA.

Formato de entrega:

- Se esta plataforma conseguir criar arquivo para download, prefira criar `context-inventory.md` para o inventario e `context-passport-[tema].md` para o passaporte final.
- Se nao for possivel gerar arquivo, entregue o conteudo completo no chat dentro de um unico bloco Markdown copiavel.
- Nao invente link de download. So ofereca link se o arquivo tiver sido realmente criado pela plataforma.
```
