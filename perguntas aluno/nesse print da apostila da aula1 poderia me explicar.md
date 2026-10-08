# Nesse print da apostila da aula1, poderia me explicar?

## Resposta

O slide diz que, para um algoritmo aprender com exemplos, precisamos decidir **três coisas**: quais respostas ele pode produzir, como medir seus erros e como encontrar a resposta com menor erro.

Imagine que queremos prever a nota de uma prova a partir das horas de estudo:

1. **Classe de modelos — o que pode ser aprendido?** Decidimos usar uma reta, escrita como $\hat y=ax+b$. Aqui, $\hat y$ é a nota prevista, $x$ é o número de horas de estudo e $a$ e $b$ determinam a inclinação e a posição da reta. A classe contém *todas* as retas possíveis; o treinamento escolhe uma delas. Se a relação real for muito mais complexa, uma reta talvez não consiga representá-la bem.
2. **Função de perda — o que conta como erro?** Comparamos cada nota prevista com a nota real. No **erro quadrático**, calculamos $(y-\hat y)^2$: se a nota real foi 8 e a previsão foi 6, o erro é $(8-6)^2=4$. Para avaliar vários exemplos, podemos tirar a média desses valores. Quanto menor essa perda, melhores são as previsões **nos exemplos avaliados**.
3. **Otimização — como encontrar o melhor modelo?** Procuramos os valores de $a$ e $b$ que tornam a perda a menor possível. Na regressão linear com erro quadrático, isso pode ser feito por uma fórmula direta (como diz o slide) ou por ajustes graduais, como na descida do gradiente.

Em resumo: **a classe de modelos define onde procurar; a função de perda diz o que é melhor; a otimização faz a procura.** O resultado do aprendizado, nesse exemplo, é uma reta específica escolhida a partir dos dados.
