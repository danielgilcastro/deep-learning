# Época

## Resumo

Uma **época** é uma passagem completa por todos os exemplos do conjunto de treinamento. Se o treinamento possui 20 épocas, a rede terá a oportunidade de estudar cada exemplo 20 vezes.

## Explicação detalhada

Durante o treinamento, os dados normalmente são divididos em pequenos grupos chamados **lotes**, ou *batches*. A rede processa um lote, calcula o erro e ajusta seus pesos e vieses. Quando todos os lotes foram processados uma vez, uma época terminou.

Por exemplo, considere um conjunto com 1.000 exemplos e lotes de 100 exemplos:

- cada época terá 10 lotes;
- os pesos serão atualizados 10 vezes por época;
- em 20 épocas, acontecerão aproximadamente 200 atualizações.

Assim, **época** e **atualização** não são a mesma coisa. Uma época pode conter várias atualizações, dependendo do tamanho do conjunto e do lote.

No Keras, a quantidade de épocas é definida pelo argumento `epochs`:

```python
modelo.fit(X_treino, y_treino, epochs=20)
```

Nesse exemplo, a rede percorre o conjunto de treinamento 20 vezes. A ordem dos exemplos pode ser embaralhada entre as épocas, mas todos continuam fazendo parte de cada passagem completa.

Usar poucas épocas pode fazer a rede parar antes de aprender o suficiente. Usar épocas demais pode levar ao **sobreajuste**, quando a rede memoriza o treinamento e piora em dados novos.

Por isso, a quantidade adequada costuma ser escolhida acompanhando o desempenho em dados de validação. Uma técnica chamada **parada antecipada**, ou *early stopping*, encerra o treinamento quando a validação deixa de melhorar.

A época faz parte do processo explicado em [[Como a rede aprende]] e é controlada no código por ferramentas como o [[Keras]].

