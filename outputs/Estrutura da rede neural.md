# Estrutura da rede neural

## Resumo

Uma **rede neural** é formada por neurônios artificiais organizados em camadas. A primeira camada recebe os dados, as camadas intermediárias aprendem padrões e a última camada produz a resposta da rede.

## Explicação detalhada

A estrutura básica de uma rede neural possui três tipos de camada:

1. **Camada de entrada:** recebe os dados originais. Em uma imagem, por exemplo, as entradas podem ser os valores dos pixels.
2. **Camadas ocultas:** transformam as informações recebidas e aprendem padrões úteis. Uma rede pode ter uma ou várias dessas camadas.
3. **Camada de saída:** gera o resultado final, como uma categoria, uma probabilidade ou um valor numérico.

Cada camada contém unidades de cálculo chamadas [[Neurônio em Deep Learning]]. Os neurônios de uma camada recebem valores, fazem cálculos e enviam seus resultados para a camada seguinte.

As conexões entre os neurônios possuem **pesos**, que indicam a importância de cada informação. Durante o treinamento, esses pesos são ajustados para melhorar as respostas da rede.

No *deep learning*, a rede possui várias camadas ocultas. Essa profundidade permite que ela aprenda padrões em diferentes níveis. Em uma imagem, por exemplo, as primeiras camadas podem reconhecer bordas, enquanto as camadas posteriores combinam essas informações para reconhecer objetos completos.

