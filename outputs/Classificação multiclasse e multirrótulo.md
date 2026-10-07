# Classificação multiclasse e multirrótulo

## Resumo

Na **classificação multiclasse**, existem três ou mais classes possíveis, mas cada exemplo pertence a apenas uma delas. Na **classificação multirrótulo**, um mesmo exemplo pode receber vários rótulos ao mesmo tempo.

## Explicação detalhada

Uma **classe** ou **rótulo** é a categoria que o modelo tenta prever. A diferença entre multiclasse e multirrótulo está na quantidade de categorias que podem ser corretas para o mesmo exemplo.

### Classificação multiclasse

Na classificação multiclasse, o modelo deve escolher **uma única classe** entre três ou mais possibilidades.

Por exemplo, uma imagem deve ser classificada como:

- cachorro;
- gato;
- pássaro.

Se a resposta correta for “gato”, ela não poderá ser também “cachorro” ou “pássaro”. As classes são **mutuamente exclusivas**, ou seja, somente uma pode ser escolhida.

No Keras, uma rede para três classes pode terminar assim:

```python
layers.Dense(3, activation="softmax")
```

A função `softmax` produz uma probabilidade para cada classe. As probabilidades somam $1$:

```text
cachorro: 0,05
gato:     0,90
pássaro:  0,05
```

O modelo escolhe a classe com a maior probabilidade. Uma perda comum é:

```python
loss="sparse_categorical_crossentropy"
```

Essa versão é adequada quando as classes são representadas por números inteiros, como `0`, `1` e `2`.

### Classificação multirrótulo

Na classificação multirrótulo, um exemplo pode possuir **zero, um ou vários rótulos ao mesmo tempo**.

Por exemplo, uma fotografia pode receber os rótulos:

- cachorro;
- ao ar livre;
- correndo.

Todos esses rótulos podem estar corretos ao mesmo tempo. Cada saída funciona como uma pergunta independente de “sim ou não”:

```text
tem cachorro?   0,95
está ao ar livre? 0,88
está correndo?  0,72
```

No Keras, uma rede para três rótulos pode terminar assim:

```python
layers.Dense(3, activation="sigmoid")
```

A [[Sigmoid|sigmoid]] produz uma probabilidade independente para cada rótulo. Por isso, os valores não precisam somar $1$. Uma perda comum é:

```python
loss="binary_crossentropy"
```

Depois, podemos definir um limite, como $0{,}5$. Todo rótulo com probabilidade maior que esse limite é considerado presente.

### Comparação

| Tipo | Quantas opções existem? | Quantas podem estar corretas? | Ativação comum |
| --- | --- | --- | --- |
| Classificação binária | Duas | Uma | `sigmoid` |
| Classificação multiclasse | Três ou mais | Apenas uma | `softmax` |
| Classificação multirrótulo | Duas ou mais | Várias ao mesmo tempo | `sigmoid` |

Uma forma simples de lembrar é:

- **multiclasse:** “qual destas classes é a correta?”;
- **multirrótulo:** “quais destes rótulos estão presentes?”.

Veja também: [[Keras]] e [[Como estruturar uma rede no Keras]].
