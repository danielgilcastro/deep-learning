# Função de ativação

## Resumo

Uma **função de ativação** transforma o resultado calculado por um neurônio antes que ele siga para a próxima camada ou se torne a previsão da rede. Nas camadas ocultas, funções não lineares permitem que a rede aprenda relações mais complexas do que uma única transformação afim.

## Explicação detalhada

O neurônio combina as entradas usando pesos e um viés, produzindo o valor $z$. A função de ativação recebe esse valor e gera a saída:

$$
y = f(z)
$$

Aqui, $f$ representa a função escolhida e $y$ é a saída. Se todas as camadas ocultas usassem apenas transformações lineares, a composição delas equivaleria a uma única transformação afim, mesmo com várias camadas.

### Funções comuns

- **[[ReLU]]:** $f(z)=\max(0,z)$. Devolve $0$ para entradas negativas e mantém as positivas. É muito usada em camadas ocultas.
- **[[Leaky ReLU]]:** $f(z)=z$ quando $z\geq 0$ e $f(z)=\alpha z$ quando $z<0$, com $\alpha$ pequeno e positivo. Mantém uma pequena saída para entradas negativas; é uma alternativa à ReLU em camadas ocultas.
- **[[Sigmoid|Sigmoide (sigmoid)]]:** $\sigma(z)=1/(1+e^{-z})$. Produz um valor entre $0$ e $1$; é comum na saída de classificação binária e em cada saída de classificação multirrótulo.
- **[[Tanh|Tangente hiperbólica (tanh)]]:** $\tanh(z)=(e^z-e^{-z})/(e^z+e^{-z})$. Produz um valor entre $-1$ e $1$, com $\tanh(0)=0$. Pode ser usada em camadas ocultas quando se deseja uma saída centrada em zero.
- **[[Softmax]]:** recebe um *vetor* de valores, em vez de transformar cada valor isoladamente. Para cada classe $i$, calcula $e^{z_i}/\sum_j e^{z_j}$. As saídas ficam entre $0$ e $1$ e somam $1$; é comum na classificação multiclasse, quando apenas uma classe pode ser correta.

Por exemplo, se a rede deve escolher entre gato, cachorro e pássaro, a softmax pode produzir $0{,}7$, $0{,}2$ e $0{,}1$. Já em uma tarefa em que a mesma imagem pode ter vários rótulos, cada saída pode usar sigmoid, e os resultados não precisam somar $1$. Veja [[Classificação multiclasse e multirrótulo]].

Essas são algumas funções de ativação, não uma lista completa. A escolha depende do papel da camada e do tipo de previsão que a rede deve produzir.
