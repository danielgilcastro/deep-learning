"""Aula 2: quatro exercícios de redes neurais com Keras.

Versão executável do notebook ``noteboock.ipynb``. Execute a partir da raiz do
projeto com ``python aula2/aula2_redes_keras.py``.

Dependências: numpy, pandas, matplotlib, seaborn, scikit-learn, keras e
tensorflow. Instalação: ``python -m pip install numpy pandas matplotlib
seaborn scikit-learn keras tensorflow``.

O exercício 4 lê a base Banknote Authentication da UCI e requer internet.
Os gráficos são abertos juntos ao final da execução; feche a janela para
encerrar o processo.
"""

from __future__ import annotations

import keras
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


SEMENTE = 42
URL_CEDULAS = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    "00267/data_banknote_authentication.txt"
)
COLUNAS_CEDULAS = ["variance", "skewness", "kurtosis", "entropy"]


def exercicio_1() -> None:
    """Monta uma rede de regressão e inspeciona seus 41 parâmetros."""
    print("\n=== Exercício 1: rede para regressão ===")

    modelo = keras.Sequential(
        [
            # shape descreve UMA amostra: duas características. A dimensão do
            # lote é variável e não faz parte dessa tupla; (2,) é tupla de 1 item.
            keras.Input(shape=(2,)),
            # Dense(units, activation): cada um dos 10 neurônios recebe as duas
            # entradas, calcula uma soma ponderada + viés e aplica ReLU.
            layers.Dense(10, activation="relu"),
            # Sem activation, a saída é linear e pode prever qualquer real.
            layers.Dense(1),
        ]
    )
    modelo.summary()

    # Para Dense, parâmetros = (entradas + 1 viés) * neurônios.
    print(f"Parâmetros esperados: (2 + 1) * 10 + (10 + 1) * 1 = 41")
    print(f"Parâmetros no modelo: {modelo.count_params()}")


def exercicio_2() -> None:
    """Calcula os parâmetros de cada camada e compara com o modelo."""
    print("\n=== Exercício 2: contagem de parâmetros ===")
    parametros_oculta = (3 + 1) * 5  # 3 pesos e 1 viés por neurônio.
    parametros_saida = (5 + 1) * 1  # A saída recebe 5 valores da camada oculta.

    modelo = keras.Sequential(
        [
            keras.Input(shape=(3,)),
            layers.Dense(5, activation="relu"),
            layers.Dense(1),
        ]
    )
    modelo.summary()
    print(f"Camada oculta: {parametros_oculta} parâmetros")
    print(f"Camada de saída: {parametros_saida} parâmetros")
    print(f"Total calculado: {parametros_oculta + parametros_saida}")
    print(f"Total no modelo: {modelo.count_params()}")


def gerar_pontos(n_por_classe: int = 120) -> tuple[np.ndarray, ...]:
    """Cria anel (classe 0) e centro (classe 1) com semente fixa.

    Args:
        n_por_classe: Quantidade de amostras em cada classe.

    Returns:
        Tupla (anel, centro, X, y). X tem forma (2*n_por_classe, 2);
        y tem um rótulo 0 ou 1 para cada linha de X.
    """
    gerador = np.random.default_rng(SEMENTE)
    angulo = gerador.uniform(0, 2 * np.pi, n_por_classe)
    raio = 1 + gerador.normal(0, 0.1, n_por_classe)
    anel = np.column_stack((raio * np.cos(angulo), raio * np.sin(angulo)))
    centro = gerador.normal(0, 0.15, size=(n_por_classe, 2))

    # A concatenação de X e y usa a mesma ordem: anel primeiro, centro depois.
    coordenadas = np.vstack((anel, centro))
    rotulos = np.concatenate((np.zeros(n_por_classe), np.ones(n_por_classe)))
    return anel, centro, coordenadas, rotulos


def desenhar_pontos(anel: np.ndarray, centro: np.ndarray) -> None:
    """Mostra a geometria dos dados antes do treinamento."""
    _, eixo = plt.subplots(figsize=(5, 5))
    eixo.scatter(anel[:, 0], anel[:, 1], s=12, c="gray", label="0: anel")
    eixo.scatter(centro[:, 0], centro[:, 1], s=12, c="tab:blue", label="1: centro")
    eixo.set(title="Dados: anel e centro", xlabel="x", ylabel="y")
    eixo.axis("equal")
    eixo.legend()


def desenhar_fronteira(
    modelo: keras.Model, anel: np.ndarray, centro: np.ndarray, titulo: str
) -> None:
    """Pinta P(classe 1) em uma grade e sobrepõe os pontos observados.

    Args:
        modelo: Rede treinada que recebe duas coordenadas e prevê uma sigmoid.
        anel: Pontos da classe 0, com duas colunas (x, y).
        centro: Pontos da classe 1, com duas colunas (x, y).
        titulo: Texto exibido acima do gráfico.
    """
    eixo_grade = np.linspace(-1.5, 1.5, num=100)
    grade_x, grade_y = np.meshgrid(eixo_grade, eixo_grade)
    grade = np.column_stack((grade_x.ravel(), grade_y.ravel()))

    # predict retorna (10_000, 1): uma probabilidade por ponto. reshape
    # recupera a forma (100, 100) exigida por contourf.
    probabilidades = modelo.predict(grade, verbose=0).reshape(grade_x.shape)
    _, eixo = plt.subplots(figsize=(5, 5))
    eixo.contourf(
        grade_x, grade_y, probabilidades,
        levels=20, cmap="RdBu_r", alpha=0.4, vmin=0, vmax=1,
    )
    eixo.scatter(anel[:, 0], anel[:, 1], s=12, c="gray", label="0: anel")
    eixo.scatter(centro[:, 0], centro[:, 1], s=12, c="tab:blue", label="1: centro")
    eixo.set(title=titulo, xlabel="x", ylabel="y")
    eixo.axis("equal")
    eixo.legend()


def exercicio_3() -> None:
    """Compara rede com camada oculta e regressão logística no mesmo conjunto."""
    print("\n=== Exercício 3: classificação binária ===")
    anel, centro, coordenadas, rotulos = gerar_pontos()
    print(f"Coordenadas: {coordenadas.shape} | Rótulos: {rotulos.shape}")
    desenhar_pontos(anel, centro)

    keras.utils.set_random_seed(SEMENTE)
    rede = keras.Sequential(
        [
            keras.Input(shape=(2,)),
            layers.Dense(8, activation="relu"),
            # Uma sigmoid fornece P(classe 1) no intervalo (0, 1).
            layers.Dense(1, activation="sigmoid"),
        ]
    )
    rede.summary()
    # compile configura o treinamento: Adam atualiza os pesos; a entropia
    # cruzada binária compara o rótulo 0/1 com a probabilidade prevista.
    # accuracy é apenas métrica de acompanhamento, não a perda otimizada.
    rede.compile(
        optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
    )
    # epochs=300 percorre o conjunto inteiro 300 vezes; verbose=0 suprime
    # o registro de progresso sem alterar o treinamento.
    rede.fit(coordenadas, rotulos, epochs=300, verbose=0)
    probabilidades = rede.predict(coordenadas, verbose=0)[:, 0]
    classes = (probabilidades > 0.5).astype(int)
    print(f"Acurácia da rede nos dados de treino: {(classes == rotulos).mean():.3f}")
    desenhar_fronteira(rede, anel, centro, "Rede com 8 neurônios ReLU")

    # Sem camada oculta, a fronteira da sigmoid é uma reta: w1*x+w2*y+b=0.
    keras.utils.set_random_seed(SEMENTE)
    logistica = keras.Sequential(
        [keras.Input(shape=(2,)), layers.Dense(1, activation="sigmoid")]
    )
    logistica.compile(
        optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
    )
    logistica.fit(coordenadas, rotulos, epochs=300, verbose=0)
    classes_logistica = (
        logistica.predict(coordenadas, verbose=0)[:, 0] > 0.5
    ).astype(int)
    print(
        "Acurácia da regressão logística nos dados de treino: "
        f"{(classes_logistica == rotulos).mean():.3f}"
    )
    desenhar_fronteira(logistica, anel, centro, "Regressão logística")
    print("Essas duas acurácias usam dados de treino, não dados inéditos.")


def exercicio_4() -> None:
    """Treina e avalia uma regressão logística na base de cédulas da UCI."""
    print("\n=== Exercício 4: cédulas falsas ===")
    # O arquivo da UCI não possui cabeçalho; names atribui os nomes às
    # quatro características e ao rótulo (1=falsa, 0=verdadeira).
    cedulas = pd.read_csv(
        URL_CEDULAS, header=None, names=COLUNAS_CEDULAS + ["class"]
    )
    print(cedulas.head())
    print("\nEstatísticas descritivas:\n", cedulas.describe())
    print("\nQuantidade por classe:\n", cedulas["class"].value_counts())
    grafico = sns.pairplot(cedulas, hue="class")
    grafico.fig.suptitle("Banknote Authentication: variáveis por classe", y=1.02)

    X = cedulas[COLUNAS_CEDULAS].to_numpy()
    y = cedulas["class"].to_numpy()
    # test_size=0.3 reserva 30% para teste; stratify preserva a proporção
    # de classes; random_state fixa a divisão para comparação reproduzível.
    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y, test_size=0.3, random_state=SEMENTE, stratify=y
    )

    # fit aprende média e desvio só no treino. transform aplica os mesmos
    # números ao teste, evitando vazamento de informação do conjunto de teste.
    padronizador = StandardScaler().fit(X_treino)
    X_treino = padronizador.transform(X_treino)
    X_teste = padronizador.transform(X_teste)
    print(f"Treino: {len(X_treino)} | Teste: {len(X_teste)}")
    print(f"Referência (prever sempre verdadeira): {1 - y_teste.mean():.3f}")

    keras.utils.set_random_seed(SEMENTE)
    modelo = keras.Sequential(
        [
            keras.Input(shape=(4,)),
            layers.Dense(1, activation="sigmoid"),
        ]
    )
    # SGD usa gradiente descendente para atualizar os cinco parâmetros:
    # quatro pesos e um viés. A perda binária corresponde à saída sigmoid.
    modelo.compile(
        optimizer="sgd", loss="binary_crossentropy", metrics=["accuracy"]
    )
    modelo.summary()
    modelo.fit(X_treino, y_treino, epochs=20, verbose=0)
    # evaluate retorna perda e, depois, accuracy (ordem definida em compile).
    perda, acuracia = modelo.evaluate(X_teste, y_teste, verbose=0)
    print(f"Perda no teste: {perda:.3f}")
    print(f"Acurácia no teste: {acuracia:.3f}")


def main() -> None:
    """Executa os exercícios na sequência do notebook e exibe os gráficos."""
    keras.utils.set_random_seed(SEMENTE)
    print(f"Keras {keras.__version__}")
    # exercicio_1()
    exercicio_2()
    # exercicio_3()
    # exercicio_4()
    # plt.show()


if __name__ == "__main__":
    main()
