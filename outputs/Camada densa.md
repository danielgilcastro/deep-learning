# Camada densa

## Resumo

Uma **camada densa** é uma camada de rede neural em que cada neurônio recebe informações de todos os neurônios da camada anterior. Ela combina esses valores para aprender padrões e produzir uma nova saída.

## Explicação detalhada

Cada conexão de uma camada densa possui um **peso**, que representa a importância daquela informação. Cada neurônio também possui um **viés**, um valor adicional que ajuda a ajustar o resultado.

O neurônio faz três coisas:

1. multiplica cada valor de entrada pelo peso correspondente;
2. soma os resultados e o viés;
3. aplica uma **função de ativação**, que define como o resultado será transformado.

Durante o treinamento, a rede modifica os pesos e os vieses para diminuir seus erros. Assim, a camada aprende quais características dos dados são mais importantes.

No Keras, uma camada densa pode ser criada assim:

```python
from keras import layers

camada = layers.Dense(8, activation="relu")
```

Nesse exemplo, `8` indica que a camada possui oito neurônios, e `relu` é a função de ativação utilizada.

As camadas densas são muito usadas nas partes finais de uma rede neural para combinar as informações aprendidas e gerar uma previsão, como identificar uma categoria ou estimar um valor.

Veja também: [[Keras]]
