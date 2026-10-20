# Reconhecimento de letras e números em imagens

**Grupo 4 — Disciplina 3: Deep Learning**  
Bruno Groppo, Bruno Pimentel, Reynato Junior, Wallace Jardim e Daniel Gil  
Base: Binary Alpha Digits | Resultados da execução de 19/10/2026

Este relatório segue as seis seções do [[../projeto/Modelo de Relatório.pdf|modelo de relatório]]. Os números e gráficos vêm do [[Projeto_Grupo4.ipynb|notebook do projeto]].

## 1. Objetivo da modelagem

**Responsável: Bruno Groppo.**

Queremos identificar **um único caractere** em uma imagem: um algarismo de 0 a 9 ou uma letra maiúscula de A a Z. A imagem entra na rede; a rede escolhe uma entre 36 classes. É uma classificação, pois a resposta é uma categoria.

Cada imagem tem 20 linhas, 16 colunas e um canal. Os pixels valem 0 ou 1. A rede devolve 36 valores, e escolhemos a classe com o maior valor. Uma rede convolucional pode aprender traços e curvas em pequenas partes da imagem, como mostra a [[../aula4/note.ipynb|aula 4]]. O projeto é uma demonstração com caracteres já separados. Ele não lê uma palavra ou uma placa inteira.

## 2. Dados utilizados

**Responsável: Bruno Pimentel.**

A equipe escolheu Binary Alpha Digits no [catálogo TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/binary_alpha_digits). O notebook baixa o [arquivo bruto público](https://cs.nyu.edu/home/people/in_memoriam/roweis/data.html) indicado para essa base. São **1.404 imagens**, com 39 exemplos de cada uma das 36 classes. Usamos a base inteira. Conferimos tamanho, rótulos e valores dos pixels. Como os pixels já valem 0 ou 1, não dividimos seus valores por 255.

![[resultados/amostras.png]]

*Figura 1 — Um exemplo de treino para cada classe. MAT (arquivo de dados em formato MATLAB) é o tipo do arquivo original.*

Há **1.363 imagens diferentes**. Algumas se repetem. As imagens da classe `0` também aparecem com o rótulo `O`. Isso significa que os mesmos pixels podem ter duas respostas diferentes.

Mantivemos todas as cópias de cada imagem no mesmo conjunto. Assim, uma cópia exata do treino não aparece na validação ou no teste. A [[../aula3/note.ipynb|aula 3]] explica o problema do vazamento de dados entre conjuntos.

| Conjunto | Imagens | Uso |
| --- | ---: | --- |
| Treino | 971 | Ajustar os pesos. |
| Validação | 217 | Comparar as redes e decidir quando parar. |
| Teste | 216 | Medir o resultado final. |

Não temos informação sobre quem escreveu cada caractere. Por isso, a divisão evita cópias exatas entre conjuntos, mas não garante escritores diferentes.

## 3. Arquitetura e desempenho

**Responsáveis: Reynato Junior e Bruno Groppo.**

A referência mais simples prevê sempre `0`, a classe escolhida pelo critério de maior frequência no treino. Também treinamos uma rede com camadas densas. As duas redes principais são convolucionais: procuram padrões em pequenas partes da imagem, reduzem seu tamanho e combinam os padrões para escolher a classe. A segunda acrescenta **Dropout**, que desliga temporariamente algumas saídas durante o treino. A [[../aula4/note.ipynb|aula 4]] mostra as camadas de imagens; a [[../aula5/note.ipynb|aula 5]] explica o Dropout.

| Etapa das redes convolucionais | Resultado |
| --- | --- |
| Entrada | 20 × 16 × 1 |
| Primeira convolução e redução | 10 × 8 × 16 |
| Segunda convolução e redução | 5 × 4 × 32 |
| Camada densa | 64 valores |
| Saída `softmax` | 36 valores, um por classe |

Cada imagem tem um rótulo inteiro. Por isso, usamos a perda `sparse_categorical_crossentropy`. O treino usa Adam com taxa 0,001, lotes de 32 imagens e limite de 80 épocas. Uma época é uma passagem por todo o treino. A parada antecipada acompanha a perda de validação e recupera os pesos da melhor época. Esses recursos aparecem nas [[../aula3/note.ipynb|aulas 3]] e [[../aula5/note.ipynb|5]].

Usamos como medida principal a **acurácia**, a porcentagem de imagens classificadas corretamente. Comparamos os modelos nas mesmas 217 imagens de validação.

| Modelo | Acertos na validação | Acurácia |
| --- | ---: | ---: |
| Referência: sempre `0` | 6 de 217 | 2,76% |
| Rede com camadas densas | 155 de 217 | 71,43% |
| Rede convolucional inicial | 160 de 217 | 73,73% |
| Rede convolucional com Dropout | 168 de 217 | **77,42%** |

Escolhemos a rede com Dropout por ter a maior acurácia na validação. **Só depois** usamos o teste, conforme o [[../projeto/Modelo de Relatório.pdf|modelo de relatório]].

| Modelo | Acertos no teste | Acurácia |
| --- | ---: | ---: |
| Referência: sempre `0` | 6 de 216 | 2,78% |
| Rede escolhida | 178 de 216 | **82,41%** |

O resultado vale para **estas 216 imagens**. Não indica como a rede se sairia em imagens de outra origem.

## 4. Análise do treinamento

**Responsável: Wallace Jardim.**

A perda mede quanto a previsão se afasta da resposta correta; menor é melhor. O gráfico mostra a perda no treino e na validação.

![[resultados/curvas.png]]

*Figura 2 — Perda ao longo das épocas. MLP (perceptron de múltiplas camadas) é a rede densa; CNN (rede neural convolucional) é a rede de imagens. As linhas marcam a época cujos pesos foram recuperados.*

A rede inicial treinou por 20 épocas e recuperou os pesos da época 10. Com Dropout, treinou por 39 épocas e recuperou os pesos da época 29. Na rede inicial, a perda de treino continuou caindo enquanto a validação deixou de melhorar. Isso é sinal de **sobreajuste**: melhorar no treino sem melhorar do mesmo modo em outros exemplos.

Acrescentamos Dropout para tentar reduzir esse problema, como na [[../aula5/note.ipynb|aula 5]]. Na validação, a nova rede acertou **oito imagens a mais**: 168 contra 160. Foi uma melhoria nesta execução e nesta divisão dos dados. O Dropout não eliminou toda a diferença entre treino e validação.

## 5. Limitações

**Responsável: Daniel Gil.**

A rede escolhida errou **38 das 216 imagens de teste**. Previu `0` para `O` quatro vezes e `5` para `S` duas vezes.

![[resultados/matriz_confusao.png]]

*Figura 3 — Matriz de confusão: linha é a classe verdadeira; coluna é a previsão.*

No teste, a classe `O` teve apenas **um acerto em seis imagens**. Parte da dificuldade está nos dados: há imagens idênticas com rótulos `0` e `O`. A rede recebe os mesmos pixels para duas respostas. Há somente seis exemplos por classe no teste, e fizemos uma única divisão dos dados. Não avaliamos outros escritores ou fotografias reais.

![[resultados/acertos_erros.png]]

*Figura 4 — Alguns acertos e erros do teste.*

## 6. Uso pretendido e restrições

**Responsável: Daniel Gil, com revisão do grupo.**

O modelo pode servir como **demonstração de classificação** ou sugerir a transcrição de um caractere isolado. Uma pessoa deve conferir a sugestão. A entrada precisa ter o mesmo formato usado no estudo: um caractere recortado, em preto e branco, com 20 × 16 pixels.

O modelo **não foi testado** em palavras, placas, documentos, letras minúsculas ou fotos. A acurácia de 82,41% neste teste não comprova segurança para uso real. Antes de outra aplicação, seria necessário testar imagens novas que representem essa aplicação.

### Materiais usados

- [[../projeto/Descrição do Projeto.pdf|Descrição do Projeto]] e [[../projeto/Modelo de Relatório.pdf|Modelo de Relatório]]: ordem, entregas, comparação e uso do teste.
- [[../aula1/Aula1_DEPAI.pdf|Aula 1]]: redes neurais e aprendizado.
- [[../aula2/noteboock.ipynb|Notebook da aula 2]]: construção e treino com Keras.
- [[../aula3/note.ipynb|Notebook da aula 3]] e [[../aula3/Aula3_DEPAI (2).pdf|arquivo da aula 3]]: separação dos dados, `softmax`, perda e treinamento.
- [[../aula4/note.ipynb|Notebook da aula 4]] e [[../aula4/Redes_convolucionais__deep_learning_para_imagens__2_.pdf|arquivo da aula 4]]: convolução e redução da imagem.
- [[../aula5/note.ipynb|Notebook da aula 5]] e [[../aula5/CNNs - Regularização, Aumentação, Transfer Learning e Interpretabilidade.pdf|arquivo da aula 5]]: parada antecipada, Dropout e sobreajuste.
- [[Projeto_Grupo4.ipynb|Notebook deste projeto]]: código, figuras e números deste relatório.
