# Tanh

## Resumo

**Tanh**, ou **tangente hiperbólica**, é uma [[Função de ativação]] que transforma um número em um valor entre $-1$ e $1$. Diferentemente da [[Sigmoid|sigmoide]], sua saída pode ser negativa e é centrada em zero.

## Explicação detalhada

A função é definida por:

$$
\tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}
$$

O símbolo $e$ representa uma constante matemática. A função se comporta assim:

- entradas muito negativas geram saídas próximas de $-1$;
- a entrada $0$ gera a saída $0$;
- entradas muito positivas geram saídas próximas de $1$.

Por exemplo, $\tanh(-1)\approx -0{,}76$ e $\tanh(1)\approx 0{,}76$. Ela pode ser usada em camadas ocultas quando é útil trabalhar com saídas positivas e negativas.

Uma limitação é que, para entradas muito distantes de zero, a saída muda cada vez menos. Nessa região, os ajustes durante o treinamento podem ficar pequenos, contribuindo para o **desaparecimento do gradiente**. Por isso, a tanh não costuma ser a primeira escolha para todas as camadas ocultas de uma rede profunda.
