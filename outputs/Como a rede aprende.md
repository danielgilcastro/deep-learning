# Como a rede aprende

## Resumo

Uma rede neural aprende fazendo previsões, medindo seus erros e ajustando seus pesos e [[Viés|vieses]]. Esse processo é repetido muitas vezes até que as previsões melhorem.

## Explicação detalhada

O aprendizado de uma rede neural acontece durante o **treinamento**. De forma simplificada, cada etapa segue este ciclo:

1. A rede recebe exemplos de entrada.
2. Ela usa seus pesos e vieses para produzir uma previsão.
3. Uma [[Função de perda]] mede a diferença entre a previsão e a resposta correta.
4. O algoritmo calcula como cada peso e viés contribuiu para o erro.
5. Os pesos e vieses são ajustados para tentar reduzir o erro.

O processo usado para calcular a contribuição de cada parâmetro para o erro é chamado de **retropropagação**, ou *backpropagation*. Ele percorre a rede no sentido contrário, começando pela saída.

Depois, um **otimizador** aplica os ajustes. Um exemplo comum é o **gradiente descendente**, que altera os parâmetros em uma direção que tende a diminuir a perda.

A quantidade de ajuste feita em cada etapa é controlada pela **taxa de aprendizado**. Uma taxa muito alta pode fazer a rede ultrapassar boas soluções. Uma taxa muito baixa pode tornar o treinamento lento.

Esse ciclo é repetido com muitos exemplos. Com o tempo, a rede encontra pesos e vieses que representam melhor os padrões presentes nos dados.
