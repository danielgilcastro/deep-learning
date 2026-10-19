# Leaky ReLU

## Resumo

**Leaky ReLU** é uma variação da [[ReLU]] que mantém os valores positivos e deixa passar uma pequena parte dos valores negativos. Ela pode ajudar quando neurônios com ReLU passam a produzir apenas zero.

## Explicação detalhada

A função usa um número pequeno e positivo $\alpha$ para definir quanto de uma entrada negativa será mantido:

$$
f(z)=
\begin{cases}
z, & z\geq 0 \\
\alpha z, & z<0
\end{cases}
$$

Por exemplo, com $\alpha=0{,}01$, a entrada $-3$ produz $-0{,}03$, enquanto a entrada $5$ continua sendo $5$. Na ReLU comum, $-3$ produziria $0$.

Essa pequena saída negativa mantém uma inclinação diferente de zero nessa região. Por isso, a Leaky ReLU pode reduzir o problema da **ReLU morta**, quando um neurônio deixa de responder às entradas durante o treinamento. Ela não garante que esse problema desapareça nem é sempre melhor que a ReLU.

Assim como a ReLU, a Leaky ReLU é uma [[Função de ativação]] usada principalmente em camadas ocultas. O valor de $\alpha$ é uma escolha do modelo.
