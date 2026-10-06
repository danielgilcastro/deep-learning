# Keras

## Resumo

Keras é uma biblioteca de Python usada para criar, treinar e testar redes neurais. Ela facilita o desenvolvimento de projetos de *deep learning* porque oferece comandos simples para montar modelos sem precisar programar todos os cálculos matemáticos manualmente.

## Explicação detalhada

O Keras organiza uma rede neural em **camadas**. Cada camada recebe dados, realiza cálculos e passa o resultado para a próxima. Atualmente, o Keras pode funcionar sobre TensorFlow, JAX ou PyTorch, que são os sistemas responsáveis pelos cálculos mais pesados.

Um uso básico segue estas etapas:

1. Instalar o Keras e um sistema de apoio, como o TensorFlow:

```bash
pip install --upgrade keras tensorflow
```

2. Importar o Keras e criar o modelo:

```python
import keras
from keras import layers

modelo = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(8, activation="relu"),
    layers.Dense(1)
])
```

Nesse exemplo:

- `Sequential` cria um modelo em que as camadas ficam uma após a outra.
- `Input(shape=(2,))` informa que cada exemplo possui dois valores de entrada.
- `Dense` cria uma camada em que todos os neurônios se conectam à camada seguinte.
- `relu` é uma função que ajuda a rede a aprender relações mais complexas.

3. Preparar o treinamento:

```python
modelo.compile(
    optimizer="adam",
    loss="mean_squared_error"
)
```

O **otimizador** ajusta os valores internos da rede durante o aprendizado. A **função de perda** mede o tamanho do erro das respostas.

4. Treinar o modelo com dados:

```python
modelo.fit(x_treino, y_treino, epochs=50)
```

`x_treino` contém os dados de entrada, `y_treino` contém as respostas corretas e `epochs=50` indica que o modelo estudará os dados durante 50 [[Época|épocas]].

5. Fazer previsões:

```python
previsoes = modelo.predict(x_novos)
```

Em resumo, o fluxo principal é: criar o modelo com `Sequential`, configurar com `compile`, treinar com `fit` e gerar resultados com `predict`.

Fontes oficiais: [Sobre o Keras 3](https://keras.io/about/) e [guia de instalação](https://keras.io/getting_started/).
