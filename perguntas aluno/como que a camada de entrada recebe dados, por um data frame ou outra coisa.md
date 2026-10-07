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

## Nos códigos, a gente passa um arquivo com esse conteúdo? Como isso acontece?

## Resposta

Podemos começar com um arquivo, mas normalmente **não passamos o arquivo diretamente para a camada de entrada**. O código primeiro abre o arquivo, organiza seu conteúdo e transforma os valores em arrays ou tensores numéricos.

No exercício das cédulas da Aula 2, os dados estão em um arquivo disponível na internet. Este trecho lê o conteúdo e cria um DataFrame:

```python
URL = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
       "00267/data_banknote_authentication.txt")

COLUNAS = ["variance", "skewness", "kurtosis", "entropy"]

cedulas = pd.read_csv(
    URL,
    header=None,
    names=COLUNAS + ["class"]
)
```

O `pd.read_csv()` acessa o endereço, lê as linhas do arquivo e coloca os dados em uma tabela chamada `cedulas`. Se o arquivo estivesse salvo no computador, poderíamos passar seu caminho no lugar da URL:

```python
cedulas = pd.read_csv("dados/cedulas.csv")
```

Depois, o código separa as **entradas** da **resposta correta**:

```python
X = cedulas[COLUNAS].values
y = cedulas["class"].values
```

Nesse código:

- `X` contém as quatro características de cada cédula;
- `y` contém o rótulo de cada exemplo: cédula falsa ou verdadeira;
- `.values` transforma os dados selecionados do DataFrame em arrays numéricos.

Em seguida, os dados são divididos e preparados. Por fim, os arrays são entregues ao treinamento:

```python
modelo.fit(X_train, y_train, epochs=20)
```

O caminho completo é:

```text
arquivo ou URL
        ↓
pd.read_csv()
        ↓
DataFrame
        ↓
separação em X e y
        ↓
arrays ou tensores
        ↓
modelo.fit(X_train, y_train)
```

Também é possível criar os dados diretamente no código, sem usar um arquivo. Isso acontece no exercício dos pontos no centro e no anel: o NumPy gera as coordenadas e os rótulos, que depois são enviados ao modelo.

Portanto, o arquivo é apenas uma possível fonte dos dados. A rede recebe os números preparados pelo código, não o arquivo em si.

## Depois que o tensor é gerado, ele fica na memória RAM? Como ele vai para a camada de entrada?

## Resposta

Sim. Quando um array ou tensor é criado, seus valores normalmente ficam na **memória RAM** do computador. Porém, a camada de entrada não é um recipiente separado para o qual o Python precisa copiar manualmente os dados.

Quando executamos:

```python
modelo.fit(X_train, y_train, batch_size=32)
```

o processo ocorre, de forma simplificada, assim:

```text
X_train na memória RAM
        ↓
Keras separa um lote de exemplos
        ↓
o lote é transformado em um tensor
        ↓
o tensor é colocado no dispositivo de cálculo
        ↓
a rede executa os cálculos da primeira camada
        ↓
o resultado segue para as próximas camadas
```

O **dispositivo de cálculo** pode ser:

- a CPU, que trabalha usando a memória RAM;
- uma GPU, que normalmente usa sua própria memória, chamada **VRAM**.

Se o treinamento estiver usando uma GPU, o sistema copia para a VRAM os lotes necessários ao cálculo. Isso não significa que todos os dados precisam ser copiados de uma vez. Eles podem ser enviados lote por lote.

Imagine que `X_train` tenha formato `(1000, 4)`:

```text
1000 exemplos
4 valores em cada exemplo
```

Se `batch_size=32`, o Keras seleciona inicialmente 32 exemplos. O tensor desse lote terá formato `(32, 4)`.

Uma entrada declarada assim:

```python
keras.Input(shape=(4,))
```

informa que **cada exemplo** precisa possuir quatro valores. Ela não guarda o tensor inteiro. Sua função principal é informar e verificar o formato esperado pela rede.

O lote `(32, 4)` chega à primeira camada que realiza cálculos. Se ela for:

```python
layers.Dense(8, activation="relu")
```

cada um dos 32 exemplos passa pelos oito neurônios. A camada multiplica os valores de entrada pelos pesos, soma os vieses e aplica a função ReLU. Sua saída terá formato `(32, 8)`:

```text
entrada do lote:  (32, 4)
                         ↓
camada Dense com 8 neurônios
                         ↓
saída da camada:  (32, 8)
```

Essa saída se torna automaticamente a entrada da camada seguinte. O Keras já conhece a ordem das camadas e executa essas operações quando `fit`, `predict` ou `evaluate` é chamado.

Portanto, não existe um comando separado para “colocar o tensor na camada de entrada”. Ao chamar `modelo.fit(X_train, y_train)`, entregamos os dados ao Keras. Ele forma os lotes, coloca cada tensor no dispositivo de cálculo e faz os valores percorrerem as camadas na ordem definida no modelo.

Veja também: [[perguntas aluno/o que seriam esses valores de entrada de um neurônio|O que seriam os valores de entrada de um neurônio?]]
