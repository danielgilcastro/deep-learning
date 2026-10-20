"""Atualiza apenas as explicações do notebook; preserva o código e as saídas."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
PATH = ROOT / "Projeto_Grupo4.ipynb"
notebook = json.loads(PATH.read_text(encoding="utf-8"))

markdown = {
    0: """# Reconhecimento de letras e números em imagens — Grupo 4

**Disciplina 3: Deep Learning | Resultados da execução de 19/10/2026**

Queremos identificar um único número de 0 a 9 ou uma letra maiúscula de A a Z em uma imagem. Cada imagem tem 20 × 16 pixels e uma resposta entre 36 classes.

O notebook segue esta ordem: carregar os dados, separá-los, criar uma referência simples, treinar as redes, comparar na validação e só então medir o resultado no teste. O código está completo; as explicações usam os conceitos dos notebooks e arquivos em PDF (formato portátil de documento) das aulas 1 a 5.

**Atenção antes de entregar:** confirmar com o professor a aprovação da base e do grupo com cinco integrantes. Conferir também a execução no Google Colab.

## 1. Preparação

No Google Colab, execute a célula de instalação e depois todas as demais na ordem. Os números podem mudar um pouco entre computadores.
""",
    3: """## 2. Carregar e conferir os dados

A base Binary Alpha Digits foi escolhida pelo grupo. O arquivo é público e contém imagens de letras e números. O código confere se o arquivo baixado é o esperado, se há 36 classes e se as imagens têm 20 × 16 pixels. Os pixels já valem 0 ou 1.

Fonte do arquivo: https://cs.nyu.edu/home/people/in_memoriam/roweis/data.html

Encontrar imagens iguais com respostas diferentes é importante para interpretar os erros depois.
""",
    5: """## 3. Separar os dados

Usamos três conjuntos. O **treino** ajusta os pesos. A **validação** compara as redes e ajuda a escolher quando parar. O **teste** fica reservado para a avaliação final.

Algumas imagens são cópias exatas, inclusive entre as classes `0` e `O`. O código coloca todas as cópias de uma mesma imagem no mesmo conjunto. Isso evita que a rede veja no treino uma cópia exata que depois apareça no teste. A aula 3 explica o problema do vazamento de dados.

Não há informação sobre quem escreveu os caracteres. Portanto, esta separação não garante escritores diferentes.
""",
    7: """## 4. Olhar exemplos e criar uma referência

Mostramos uma imagem de treino por classe e contamos as imagens em cada conjunto.

A referência mais simples escolhe a classe mais frequente no treino e prevê essa classe para todas as imagens. No empate, o código escolhe a primeira classe, `0`. As redes precisam ser comparadas com essa referência.

A **acurácia** é a porcentagem de previsões corretas. O código também guarda outras medidas por classe para ajudar a analisar os erros.
""",
    9: """## 5. Construir e treinar as redes

Treinamos uma rede com camadas densas, chamada no código de **MLP (perceptron de múltiplas camadas)**. Depois treinamos uma **CNN (rede neural convolucional)** inicial e outra com Dropout. A rede convolucional encontra padrões em pequenas partes da imagem; a aula 4 mostra esse tipo de camada.

Dropout desliga temporariamente algumas saídas durante o treino. É a única mudança entre as duas redes convolucionais. A aula 5 explica essa tentativa de reduzir sobreajuste.

Cada imagem tem um rótulo inteiro. Por isso usamos a perda `sparse_categorical_crossentropy` e uma saída `softmax` com 36 valores, como na aula 3. Usamos lotes de 32 imagens, até 80 épocas, e parada antecipada quando a perda de validação deixa de melhorar. Uma época é uma passagem por todos os exemplos de treino.

Escolhemos a rede com a maior acurácia de **validação**. O teste ainda não participa dessa escolha.
""",
    11: """## 6. Ver as curvas de treinamento

A **perda** mede o quanto a previsão se afasta da resposta correta. Observe a perda no treino e na validação ao longo das épocas. Se a perda de treino cair e a de validação parar de melhorar, há sinal de **sobreajuste**. As aulas 3 e 5 mostram como ler essas curvas e usar a parada antecipada.
""",
    13: """## 7. Fazer o teste final

A rede já foi escolhida pela validação. Agora o teste serve apenas para medir seu resultado final. Não alteramos a rede depois de ver esse resultado, conforme o enunciado e o modelo de relatório.

O código mostra acertos, erros e uma matriz de confusão. Nessa matriz, cada linha mostra a classe verdadeira e cada coluna mostra a previsão.
""",
    15: """## 8. Prever um caractere

A função abaixo recebe uma imagem binária de 20 × 16 pixels e devolve a classe prevista. Ela serve para demonstrar o modelo nas mesmas condições do estudo. Não testamos a função em palavras, fotografias, placas ou documentos reais.
""",
    17: """## 9. Resultado e limites

Na validação, a **CNN (rede neural convolucional)** inicial acertou 160 de 217 imagens. A **CNN (rede neural convolucional)** com Dropout acertou 168 e foi escolhida. No teste, a rede escolhida acertou 178 de 216 imagens, ou 82,41%.

A rede errou 38 imagens de teste. Há imagens idênticas com rótulos `0` e `O`, o que limita a classificação. O resultado descreve esta execução e esta base; não garante o mesmo desempenho em outras imagens.

As explicações usadas aqui seguem o enunciado, o modelo de relatório e os materiais das aulas 1 a 5. Os números vêm da execução registrada neste notebook.
""",
}

for index, value in markdown.items():
    cell = notebook["cells"][index]
    assert cell["cell_type"] == "markdown", index
    cell["source"] = value.splitlines(keepends=True)

PATH.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
                encoding="utf-8")
print(PATH)
