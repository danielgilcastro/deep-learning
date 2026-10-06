# Aprendizado por atalho

## Resumo

**Aprendizado por atalho** acontece quando um modelo aprende uma pista fácil e acidental dos dados, em vez do padrão que realmente deveria aprender. Ele pode apresentar bons resultados nos dados conhecidos, mas falhar quando essa pista muda ou desaparece.

## Explicação detalhada

Durante o treinamento, uma rede neural procura padrões que ajudem a diminuir o erro. Ela não sabe, por conta própria, quais padrões representam a verdadeira causa do problema. Por isso, pode escolher uma característica fácil que apenas está associada à resposta nos dados de treinamento.

Um exemplo da Aula 2 aparece na questão T15 de [[aula2/Questoes_monitoria_2.pdf|Questões de monitoria da Aula 2]]. Uma rede deve identificar relatos de violência doméstica pelo texto. Porém, quase todos esses relatos vieram de uma delegacia especializada, e o sistema dessa unidade adiciona seu nome ao rodapé.

Nesse caso, a rede pode aprender a procurar o nome da delegacia no rodapé, em vez de compreender o conteúdo do relato. O rodapé funciona como um **atalho**: é uma pista mais fácil, mas não representa o que define uma ocorrência de violência doméstica.

Uma validação sorteada da mesma base pode não revelar o problema. Como o mesmo rodapé aparece tanto no treino quanto na validação, a rede pode alcançar uma acurácia alta usando o atalho.

Para verificar se isso aconteceu, podemos avaliar a rede em relatos equivalentes:

- registrados em outras delegacias;
- sem o rodapé;
- com o rodapé alterado ou trocado.

Se o desempenho cair muito, isso indica que a rede dependia daquela pista. Para reduzir o problema, podemos remover a característica enganosa, coletar exemplos em contextos variados e separar treino, validação e teste de modo que o atalho não apareça igualmente em todos eles.

O aprendizado por atalho está relacionado à **generalização**, que é a capacidade de funcionar bem em dados novos. Ele não é exatamente o mesmo que vazamento de dados: no vazamento, uma informação que não deveria estar disponível chega ao modelo; no atalho, a informação pode estar disponível, mas leva o modelo a aprender a relação errada.
