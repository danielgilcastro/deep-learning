# Protocolo: pergunta aluno

## Quando usar

Quando o usuário iniciar o pedido com `!pergunta aluno`, `!perguntas aluno` ou `!pa`.

Sem o prefixo `!`, a expressão não deve ativar este protocolo.

## Onde salvar

Salvar as notas na pasta `perguntas aluno`, dentro do projeto Deep Learning. Criar essa pasta se ela ainda não existir.

## Criar ou alimentar a nota

1. Identificar a pergunta do aluno no pedido. Se nenhuma pergunta tiver sido informada, pedir a pergunta antes de criar a nota.
2. Usar a própria pergunta como nome  tratado ,do arquivo, com a extensão `.md`.
3. Para o nome do arquivo ser válido no Windows, substituir os caracteres proibidos (`< > : " / \ | ? *`) por espaços, remover espaços repetidos e pontos ou espaços no final. Se necessário, encurtar o nome ou ajustar um nome reservado do Windows, mantendo a pergunta reconhecível. Preservar a pergunta completa no título dentro da nota.
4. Procurar a nota correspondente na pasta `perguntas aluno`. Se já existir, atualizar ou complementar essa nota, preservando seu conteúdo útil e evitando repetir informações. Se não existir, criar uma nova nota.
5. Registrar a pergunta e sua resposta na nota. Explicar a resposta com linguagem fácil e definir os termos técnicos necessários.
6. Se o pedido trouxer várias perguntas, criar ou atualizar uma nota para cada pergunta.

## Links

- Nas notas deste protocolo, só criar links para arquivos Markdown da própria pasta `perguntas aluno` deste projeto.
- Não criar links ou incorporações para notas de outras pastas, incluindo aulas, protocolos ou o AGENTS.md. Essa regra vale para links Markdown, wikilinks (`[[...]]`) e incorporações (`![[...]]`).
- Criar links entre perguntas apenas quando forem úteis e a nota de destino existir. Usar o caminho da pasta quando necessário para evitar apontar para uma nota de mesmo nome fora dela.
- Não é obrigatório adicionar links. É permitido mencionar conceitos e nomes de outras notas em texto simples, sem link.

## Formato de uma nova nota

```markdown
# [Pergunta completa do aluno]

## Resposta

[Resposta em linguagem fácil.]
```

## Exemplo de pedido

"!Pergunta aluno: o que é uma rede neural?"

Arquivo correspondente: `perguntas aluno/o que é uma rede neural.md`.
