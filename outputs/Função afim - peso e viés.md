# Função afim: peso e viés

## Resumo

Uma **função afim** é o cálculo usado por um neurônio para combinar os valores de entrada. Ela multiplica cada entrada por um peso, soma os resultados e acrescenta um viés.

## Explicação detalhada

O cálculo de uma função afim pode ser representado assim:

$$
z = w_1x_1 + w_2x_2 + \cdots + w_nx_n + b
$$

Nessa expressão:

- $x_1, x_2, \ldots, x_n$ são os valores de entrada;
- $w_1, w_2, \ldots, w_n$ são os **pesos**;
- $b$ é o **viés**;
- $z$ é o resultado do cálculo.

O **peso** indica o quanto uma entrada influencia o resultado. Um peso com valor alto pode dar mais importância à entrada, enquanto um peso negativo pode fazer essa entrada reduzir o resultado.

O **viés** é um valor adicional que desloca o resultado. Ele permite que o neurônio produza uma resposta mais adequada mesmo quando todas as entradas são zero.

Por exemplo, considere $x = 3$, $w = 2$ e $b = 1$:

$$
z = 2 \cdot 3 + 1 = 7
$$

Durante o treinamento, a rede ajusta os pesos e os vieses. O resultado da função afim normalmente segue para uma [[Função de ativação]], que decide como o neurônio responderá.

