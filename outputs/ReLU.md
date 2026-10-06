# ReLU

## Resumo

**ReLU** é uma função de ativação muito usada em *deep learning*. Ela transforma valores negativos em zero e mantém os valores positivos. Isso ajuda as redes neurais a aprender padrões complexos de forma eficiente.

## Explicação detalhada

ReLU é a sigla de **Rectified Linear Unit**, que pode ser traduzida como **Unidade Linear Retificada**. Ela normalmente é aplicada à saída de cada neurônio antes que o resultado siga para a próxima camada da rede.

Sua regra é simples:

$$
f(x) = \max(0, x)
$$

Isso significa que:

- se o valor de entrada for negativo, a saída será $0$;
- se o valor de entrada for positivo, a saída será o próprio valor;
- se o valor de entrada for $0$, a saída também será $0$.

Por exemplo, a ReLU transforma $-3$ em $0$ e mantém $5$ como $5$.

A ReLU é importante porque adiciona **não linearidade** à rede neural. Em linguagem simples, isso permite que a rede aprenda relações mais complexas do que apenas proporções e linhas retas. Ela também exige um cálculo simples, o que costuma tornar o treinamento mais rápido.

Uma limitação é que alguns neurônios podem passar a produzir apenas zero durante o treinamento. Esse problema é conhecido como **ReLU morta**. Existem variações, como a **Leaky ReLU**, que permitem uma pequena saída para valores negativos e podem reduzir esse problema.

No Keras, a ReLU pode ser usada em uma camada densa desta forma:

```python
from keras import layers

camada = layers.Dense(8, activation="relu")
```

Nesse exemplo, `activation="relu"` indica que a saída dos oito neurônios da [[Camada densa]] será transformada pela função ReLU.

Veja também: [[Neurônio em Deep Learning]] e [[Keras]].
