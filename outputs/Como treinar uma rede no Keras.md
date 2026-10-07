# Como treinar uma rede no Keras

## Resumo

Treinar uma rede no Keras significa mostrar exemplos ao modelo para que ele ajuste seus pesos e diminua os erros. O processo básico é preparar os dados, compilar o modelo, executar `fit` e avaliar o resultado em dados que não foram usados no treinamento.

## Explicação detalhada

Antes de treinar, os dados devem ser separados em entradas `X` e respostas corretas `y`. Também é importante reservar dados de teste para verificar se a rede funciona com exemplos novos:

```python
from sklearn.model_selection import train_test_split

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)
```

Depois de criar a arquitetura, o modelo precisa ser compilado. Para uma classificação binária, podemos usar:

```python
modelo.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
```

Cada argumento possui uma função:

- `optimizer="adam"` escolhe como os pesos serão ajustados;
- `loss="binary_crossentropy"` define como o erro será medido;
- `metrics=["accuracy"]` pede que o Keras também mostre a proporção de acertos.

Para uma regressão, uma escolha comum é usar uma saída `Dense(1)` e a perda `"mse"`, que mede o erro quadrático médio.

O treinamento é iniciado com `fit`:

```python
historico = modelo.fit(
    X_treino,
    y_treino,
    epochs=20,
    batch_size=32,
    validation_split=0.2
)
```

Nesse comando:

- `epochs=20` faz a rede percorrer os dados de treino 20 vezes;
- `batch_size=32` divide os dados em lotes de 32 exemplos antes de cada atualização dos pesos;
- `validation_split=0.2` separa parte do treino para acompanhar o desempenho durante as épocas.

Em cada lote, a rede faz uma previsão, calcula a [[Função de perda|perda]], calcula como os parâmetros contribuíram para o erro e atualiza os pesos e vieses. Esse ciclo é explicado em [[Como a rede aprende]].

Depois do treinamento, avaliamos o modelo com dados de teste que ficaram separados:

```python
perda, acuracia = modelo.evaluate(X_teste, y_teste)
```

Para fazer previsões em novas entradas, usamos:

```python
probabilidades = modelo.predict(X_novos)
```

O fluxo completo é:

```text
preparar os dados
        ↓
criar a estrutura
        ↓
compilar o modelo
        ↓
treinar com fit
        ↓
avaliar com evaluate
        ↓
prever com predict
```

O teste não deve ser usado para escolher a arquitetura, ajustar o número de épocas ou preparar os dados. Isso ajuda a evitar [[Vazamento de dados]] e torna a avaliação mais confiável.

Veja também: [[Keras]], [[Como estruturar uma rede no Keras]] e [[Época]].
