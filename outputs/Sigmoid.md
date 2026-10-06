# Sigmoid

## Resumo

A **sigmoid**, também chamada de **função sigmoide**, é uma função de ativação que transforma qualquer número em um valor entre $0$ e $1$. Ela é muito usada na saída de modelos que precisam escolher entre duas possibilidades.

## Explicação detalhada

A função sigmoid é definida por:

$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$

O símbolo $e$ representa uma constante matemática, e $x$ é o valor recebido pela função.

O resultado se comporta desta forma:

- valores muito negativos produzem resultados próximos de $0$;
- o valor $0$ produz o resultado $0{,}5$;
- valores muito positivos produzem resultados próximos de $1$.

Por causa desse intervalo, a saída pode ser interpretada como uma probabilidade em alguns modelos. Em uma classificação entre “sim” e “não”, por exemplo, um resultado de $0{,}9$ pode indicar uma forte tendência para a categoria representada pelo valor $1$.

A sigmoid é comum na camada de saída de problemas de **classificação binária**, nos quais existem duas possibilidades. Ela é um tipo de [[Função de ativação]].

Uma limitação da sigmoid aparece quando a entrada é muito positiva ou muito negativa. Nessas regiões, a função muda muito pouco, o que pode tornar o aprendizado lento. Esse efeito contribui para o problema do **desaparecimento do gradiente**, em que os ajustes feitos nas primeiras camadas ficam muito pequenos.

Por esse motivo, a sigmoid é menos usada nas camadas ocultas de redes profundas. Nessas camadas, funções como a ReLU costumam ser mais eficientes.

