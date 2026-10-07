# O que seriam esses valores de entrada de um neurônio?

## Resposta

Os **valores de entrada** são os números que um neurônio recebe para fazer seu cálculo. Eles podem vir diretamente dos dados ou ser produzidos por outros neurônios.

Na primeira camada da rede, esses valores são as **características** de um exemplo. Imagine uma rede que tenta prever se uma pessoa comprará um produto usando duas informações:

```text
idade = 30
renda = 3000
```

Para um neurônio da primeira camada, os valores de entrada poderiam ser:

$$
x_1 = 30
$$

$$
x_2 = 3000
$$

O neurônio multiplica cada entrada por um peso, soma os resultados e acrescenta um viés:

$$
z = x_1w_1 + x_2w_2 + b
$$

Nesse cálculo:

- $x_1$ e $x_2$ são os valores de entrada;
- $w_1$ e $w_2$ são os pesos, que indicam a importância de cada entrada;
- $b$ é o viés, que ajuda a ajustar o resultado.

Em outros tipos de dados, as entradas podem ser diferentes:

- em uma tabela, podem ser idade, renda, altura ou temperatura;
- em uma imagem, podem ser os valores dos pixels;
- em um áudio, podem ser números que representam partes do som;
- em um texto, podem ser números usados para representar palavras ou partes de palavras.

Nas camadas ocultas, a situação muda um pouco. Os neurônios normalmente não recebem diretamente os dados originais. Eles recebem como entrada as **saídas dos neurônios da camada anterior**.

```text
dados originais
      ↓
primeira camada de neurônios
      ↓
valores produzidos pela primeira camada
      ↓
segunda camada de neurônios
```

Portanto, “valor de entrada de um neurônio” significa simplesmente **cada número que chega até aquele neurônio para participar do cálculo**. Na primeira camada, esses números vêm dos dados. Nas camadas seguintes, eles vêm da camada anterior.

Veja também: [[perguntas aluno/como que a camada de entrada recebe dados, por um data frame ou outra coisa|Como os dados chegam à camada de entrada?]]
