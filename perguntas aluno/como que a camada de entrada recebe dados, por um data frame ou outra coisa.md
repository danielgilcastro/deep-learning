# Como que a camada de entrada recebe dados, por um DataFrame ou outra coisa?

## Resposta

A camada de entrada recebe os dados como **números organizados em um tensor**. Um tensor é uma estrutura parecida com uma lista ou tabela, mas pode ter várias dimensões.

Um **DataFrame** pode ser usado para organizar e preparar dados tabulares, como uma planilha. Antes de os dados entrarem na rede, suas colunas são normalmente convertidas em um array ou tensor numérico.

Por exemplo:

```python
X = dataframe[["idade", "renda"]].to_numpy(dtype="float32")
y = dataframe["comprou"].to_numpy()

modelo.fit(X, y)
```

Nesse caso, cada linha representa um exemplo e as colunas `idade` e `renda` representam as características usadas pela rede. A coluna `comprou` contém a resposta que ela deve aprender a prever.

Algumas bibliotecas, como o Keras, permitem entregar um DataFrame numérico diretamente ao método de treinamento. Mesmo assim, a biblioteca converte os dados internamente. A camada de entrada não lê o DataFrame nem o arquivo original: ela recebe somente o tensor resultante.

Se `X` possui 1.000 linhas e duas colunas, por exemplo, seu formato será `(1000, 2)`. Isso significa que existem 1.000 exemplos, cada um com duas características. Durante o treinamento, apenas uma parte desses exemplos entra na rede por vez, de acordo com o tamanho do lote.

Cada tipo de dado precisa ser transformado de uma maneira adequada:

- **dados de tabela:** matriz com linhas e colunas numéricas;
- **imagens:** tensor com os valores dos pixels;
- **textos:** sequência de números que representam palavras ou partes de palavras;
- **áudios:** sequência de valores do som ou de características extraídas dele.

Os dados também costumam ser enviados em pequenos grupos chamados **lotes**, ou *batches*. Portanto, o DataFrame pode ser o recipiente usado na preparação, mas a camada de entrada recebe efetivamente os valores numéricos em forma de tensor.
