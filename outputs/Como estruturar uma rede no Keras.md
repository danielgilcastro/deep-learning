# Como estruturar uma rede no Keras

## Resumo

Estruturar uma rede no Keras significa definir a entrada, as camadas ocultas e a saída do modelo. Cada parte deve combinar com o formato dos dados e com o tipo de problema que queremos resolver.

## Explicação detalhada

Uma forma simples de criar uma rede é usar `keras.Sequential`. Nesse modelo, os dados passam pelas camadas na ordem em que elas aparecem no código:

```python
import keras
from keras import layers

modelo = keras.Sequential([
    keras.Input(shape=(4,)),
    layers.Dense(8, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])
```

Essa rede possui três partes:

1. **Entrada:** `Input(shape=(4,))` informa que cada exemplo possui quatro características. O número `4` deve ser igual à quantidade de colunas de entrada em `X`.
2. **Camada oculta:** `Dense(8, activation="relu")` cria uma [[Camada densa]] com oito neurônios. A [[ReLU]] permite que a rede aprenda relações não lineares.
3. **Saída:** `Dense(1, activation="sigmoid")` cria uma saída entre 0 e 1, adequada para uma classificação com duas classes.

A camada de saída depende do problema:

| Problema | Camada de saída | Significado |
| --- | --- | --- |
| Regressão | `Dense(1)` | Produz um valor numérico, como preço ou temperatura. |
| Classificação binária | `Dense(1, activation="sigmoid")` | Produz a probabilidade de pertencer a uma das duas classes. |

O número de camadas ocultas e de neurônios é um **hiperparâmetro**, ou seja, uma escolha feita antes do treinamento. Uma rede maior pode aprender relações mais complexas, mas também pode demorar mais para treinar e sofrer sobreajuste.

Para conferir a estrutura criada, usamos:

```python
modelo.summary()
```

O resumo mostra as camadas, o formato de suas saídas e a quantidade de parâmetros treináveis. Em uma camada densa, a quantidade de parâmetros é:

$(\text{entradas} + 1) \times \text{neurônios}$

O `1` representa o [[Viés|viés]] de cada neurônio. A estrutura criada define o caminho que os dados percorrem; o ajuste dos pesos acontece depois, no processo explicado em [[Como treinar uma rede no Keras]].

Veja também: [[Keras]] e [[Estrutura da rede neural]].
