---
tags:
  - deep-learning
  - redes-neurais
  - neurônio-artificial
---

# Neurônio em Deep Learning

## Resumo

Um **neurônio artificial** é uma pequena unidade de cálculo de uma rede neural. Ele recebe vários valores de entrada, atribui uma importância diferente a cada um, soma essas informações e produz uma saída. Ao combinar muitos neurônios em camadas, uma rede consegue aprender padrões complexos em imagens, textos, sons e outros dados.

## Explicação detalhada

O neurônio artificial foi inspirado, de forma simplificada, no funcionamento dos neurônios biológicos. Em uma rede neural, ele recebe entradas como $x_1, x_2, \ldots, x_n$. Cada entrada é multiplicada por um **peso** $w_i$, que representa o quanto aquela informação é importante para a decisão.

Depois, o neurônio soma os valores ponderados e acrescenta um **viés** (*bias*):

$$
z = w_1x_1 + w_2x_2 + \cdots + w_nx_n + b
$$

O resultado $z$ passa por uma **função de ativação**, que determina a saída do neurônio:

$$
y = f(z)
$$

Uma função de ativação comum é a **ReLU**, definida como $f(z) = \max(0,z)$. Ela devolve zero quando o valor é negativo e mantém o valor quando ele é positivo. Essas funções permitem que a rede aprenda relações não lineares e resolva problemas mais complexos.

Durante o treinamento, a rede compara sua previsão com a resposta correta. Em seguida, ajusta os pesos e os vieses para reduzir o erro. Esse processo é repetido muitas vezes, fazendo com que cada neurônio aprenda a reconhecer características úteis dos dados.

Por exemplo, em uma rede que reconhece imagens de gatos, os primeiros neurônios podem aprender a identificar bordas e cores. Camadas posteriores combinam essas características para reconhecer formas, como olhos, orelhas e, por fim, o gato completo.

Em resumo, um neurônio realiza quatro etapas:

1. Recebe valores de entrada.
2. Multiplica cada entrada por um peso.
3. Soma os resultados e adiciona o viés.
4. Aplica uma função de ativação para gerar a saída.

Sozinho, um neurônio realiza um cálculo simples. O poder do *deep learning* surge da combinação de muitos neurônios organizados em várias camadas.
