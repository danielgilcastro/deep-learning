# Viés

## Resumo

O **viés**, chamado de *bias* em inglês, é um valor ajustável que o neurônio adiciona à soma das entradas multiplicadas por seus pesos. Ele ajuda o neurônio a deslocar sua resposta e encontrar padrões que não dependem apenas dos valores de entrada.

## Explicação detalhada

O cálculo básico de um neurônio pode ser escrito assim:

$$
z = w_1x_1 + w_2x_2 + \cdots + w_nx_n + b
$$

Nessa expressão, $x$ representa as entradas, $w$ representa os pesos e $b$ representa o viés.

Os pesos controlam a influência de cada entrada. O viés desloca o resultado total. Por causa dele, o neurônio pode produzir um valor diferente de zero mesmo quando todas as entradas são zero.

Por exemplo, considere um neurônio com uma entrada:

$$
z = 2x + 3
$$

Se $x = 0$, o resultado será $z = 3$. Esse valor vem do viés. Sem ele, o resultado seria obrigatoriamente zero.

O viés também ajuda a mudar o ponto em que um neurônio começa a responder. Podemos imaginá-lo como um ajuste que desloca uma linha ou uma fronteira de decisão, permitindo que ela se encaixe melhor nos dados.

Cada neurônio de uma camada densa normalmente possui seu próprio viés. Assim, uma camada com oito neurônios costuma ter oito valores de viés, além dos pesos de suas conexões.

Durante o treinamento, a rede ajusta os vieses junto com os pesos para reduzir a perda. Portanto, o viés é um **parâmetro treinável**, ou seja, um número que a rede aprende a partir dos exemplos.

Este significado aparece no cálculo da [[Função afim - peso e viés]] e não deve ser confundido com o **viés de um modelo** na relação entre viés e variância. Nesse outro uso, viés significa uma tendência de erro causada por um modelo simples demais ou por suposições inadequadas.

