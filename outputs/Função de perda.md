# Função de perda

## Resumo

Uma **função de perda** mede o tamanho do erro cometido por uma rede neural. Ela compara a previsão da rede com a resposta correta e produz um número que orienta o aprendizado.

## Explicação detalhada

Durante o treinamento, a rede faz uma previsão. A função de perda compara essa previsão com o valor esperado:

$$
\text{perda} = L(\text{previsão}, \text{resposta correta})
$$

Uma perda pequena indica que a previsão está próxima da resposta correta. Uma perda grande indica que o erro é maior.

Por exemplo, se o valor correto é $10$, uma previsão igual a $9{,}8$ deve produzir uma perda menor do que uma previsão igual a $2$.

Existem diferentes funções de perda para diferentes problemas:

- **erro quadrático médio:** comum quando a rede prevê valores numéricos;
- **entropia cruzada binária:** comum em classificações com duas possibilidades;
- **entropia cruzada categórica:** comum em classificações com várias categorias.

A função de perda não corrige a rede sozinha. Ela fornece uma medida que permite calcular como os pesos e vieses devem mudar. Por isso, ela é uma parte central do processo descrito em [[Como a rede aprende]].

