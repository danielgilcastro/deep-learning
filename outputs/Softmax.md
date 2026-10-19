# Softmax

## Resumo

**Softmax** é uma [[Função de ativação]] aplicada a um conjunto de valores de saída. Ela produz um valor entre $0$ e $1$ para cada classe, e todos esses valores somam $1$. É comum na saída de uma rede de [[Classificação multiclasse e multirrótulo|classificação multiclasse]], em que apenas uma classe pode ser a correta.

## Explicação detalhada

Ao contrário da [[Sigmoid|sigmoide]], que transforma cada valor separadamente, a softmax considera todos os valores de saída ao mesmo tempo. Para valores $z_1,\ldots,z_K$, o resultado da classe $i$ é:

$$
\operatorname{softmax}(z)_i=\frac{e^{z_i}}{\sum_{j=1}^{K}e^{z_j}}
$$

O símbolo $e$ representa uma constante matemática. Como cada resultado é positivo e todos têm o mesmo denominador, a soma dos resultados é $1$.

Por exemplo, para as classes gato, cachorro e pássaro, uma rede pode produzir:

| Classe | Saída da softmax |
| --- | --- |
| Gato | $0{,}7$ |
| Cachorro | $0{,}2$ |
| Pássaro | $0{,}1$ |

O maior valor indica a classe escolhida pela rede. Esses números podem ser usados como probabilidades previstas pelo modelo, mas um valor alto não garante, por si só, que a previsão esteja correta.

Quando um exemplo pode ter vários rótulos ao mesmo tempo, costuma-se usar uma sigmoid para cada rótulo. Nesse caso, cada saída é calculada separadamente e os valores não precisam somar $1$. Veja [[Classificação multiclasse e multirrótulo]].
