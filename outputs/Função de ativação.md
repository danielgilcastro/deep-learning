# Função de ativação

## Resumo

Uma **função de ativação** transforma o resultado calculado por um neurônio. Ela permite que a rede neural aprenda padrões complexos, em vez de realizar apenas cálculos lineares simples.

## Explicação detalhada

Primeiro, o neurônio combina suas entradas usando pesos e um viés. Depois, a função de ativação recebe o resultado desse cálculo e produz a saída do neurônio:

$$
y = f(z)
$$

Nessa expressão, $z$ é o valor calculado pelo neurônio, $f$ é a função de ativação e $y$ é a saída.

Sem funções de ativação não lineares, várias camadas se comportariam como um único cálculo linear. Isso impediria a rede de aprender relações mais complexas nos dados.

Uma função muito usada é a [[ReLU]]. Ela transforma valores negativos em zero e mantém os valores positivos. Outras funções comuns são:

- **[[Sigmoid|sigmoide]]:** produz valores entre $0$ e $1$;
- **tanh:** produz valores entre $-1$ e $1$;
- **softmax:** transforma vários valores em probabilidades cuja soma é $1$.

A escolha da função depende da camada e do tipo de problema. A ReLU é comum nas camadas ocultas, enquanto a sigmoide e a softmax são frequentemente usadas na camada de saída de tarefas de classificação.
