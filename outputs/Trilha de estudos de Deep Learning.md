# Trilha de estudos de Deep Learning

Esta nota organiza o conteúdo do projeto em uma ordem progressiva. Os materiais estão ligados por links internos do Obsidian para facilitar a navegação e mostrar a estrutura de estudo no gráfico.

## Visão geral da trilha

```text
1. Entender o que é deep learning
                 ↓
2. Entender como os dados entram na rede
                 ↓
3. Estudar neurônios, cálculos e ativações
                 ↓
4. Entender a estrutura de uma rede neural
                 ↓
5. Entender como a rede aprende
                 ↓
6. Criar e treinar redes com Keras
                 ↓
7. Avaliar se o modelo funciona de verdade
                 ↓
8. Revisar e praticar
```

---

## Etapa 1 — Fundamentos de deep learning

### Ordem de estudo

1. [[outputs/Deep Learning|Deep Learning]]
2. [[outputs/Redes neurais|Redes neurais]]

### O que aprender

- O que diferencia inteligência artificial, machine learning e deep learning.
- O que é uma rede neural.
- Por que uma rede aprende com exemplos em vez de receber todas as regras prontas.
- O que significa uma rede ser “profunda”.
- Diferença entre classificação e regressão.

### Material principal

- [[aula1/Aula1_DEPAI.pdf|Aula 1 — DEPAI]]
- [[aula1/Gabarito - Questoes de monitoria 1|Gabarito das questões de monitoria 1]], questões T01, T04, T07 e T10.

### Antes de avançar

- [ ] Consigo explicar deep learning com minhas próprias palavras.
- [ ] Consigo dar um exemplo de classificação e um de regressão.
- [ ] Consigo explicar por que uma rede precisa de exemplos com respostas corretas durante o aprendizado supervisionado.

---

## Etapa 2 — Dados e camada de entrada

### Ordem de estudo

3. [[perguntas aluno/como que a camada de entrada recebe dados, por um data frame ou outra coisa|Como a camada de entrada recebe dados?]]

### O que aprender

- Diferença entre arquivo, DataFrame, array e tensor.
- Como separar as características de entrada `X` e a resposta esperada `y`.
- O significado do formato de uma entrada, como `(1000, 4)`.
- Por que a rede recebe números preparados, e não o arquivo original.
- Como tabelas, imagens, textos e áudios precisam ser transformados em representações numéricas.

### Material principal

- [[aula1/Aula1_DEPAI.pdf|Aula 1 — DEPAI]], parte sobre representações.
- [[aula1/Gabarito - Questoes de monitoria 1|Gabarito das questões de monitoria 1]], questões T06 e T08.
- [[aula2/Gabarito - Questoes de monitoria 2|Gabarito das questões de monitoria 2]], questões T04, T10, T11, T12 e T15.

### Antes de avançar

- [ ] Consigo explicar o caminho `arquivo → DataFrame → X e y → tensor → rede`.
- [ ] Consigo identificar o número de exemplos e de características pelo formato de `X`.
- [ ] Consigo explicar por que uma coluna com a resposta deve ficar em `y`, e não dentro de `X`.

---

## Etapa 3 — Neurônio, pesos e ativações

### Ordem de estudo

4. [[outputs/Neurônio em Deep Learning|Neurônio em Deep Learning]]
5. [[perguntas aluno/o que seriam esses valores de entrada de um neurônio|O que seriam os valores de entrada de um neurônio?]]
6. [[outputs/Função afim - peso e viés|Função afim: peso e viés]]
7. [[outputs/Viés|Viés]]
8. [[outputs/Função de ativação|Função de ativação]]
9. [[outputs/ReLU|ReLU]]
10. [[outputs/Sigmoid|Sigmoid]]
11. [[outputs/Camada densa|Camada densa]]

### O que aprender

- Como um neurônio recebe e combina valores.
- O papel dos pesos e do viés.
- O cálculo $z = w_1x_1 + w_2x_2 + \cdots + w_nx_n + b$.
- Por que uma função de ativação é aplicada depois da função afim.
- Quando ReLU e sigmoid são usadas.
- O que significa todos os neurônios estarem conectados em uma camada densa.

### Material principal

- [[aula1/Aula1_DEPAI.pdf|Aula 1 — DEPAI]], parte sobre a rede neural.
- [[aula1/Gabarito - Questoes de monitoria 1|Gabarito das questões de monitoria 1]], questões T02, T03 e T05.
- [[aula2/Gabarito - Questoes de monitoria 2|Gabarito das questões de monitoria 2]], questões T05, T16 e T18.

### Antes de avançar

- [ ] Consigo calcular a função afim de um neurônio simples.
- [ ] Consigo diferenciar peso, viés e função de ativação.
- [ ] Consigo explicar por que várias camadas sem ativações não lineares continuam equivalendo a um cálculo linear.
- [ ] Sei por que a ReLU é comum nas camadas ocultas e a sigmoid pode ser usada na saída binária.

---

## Etapa 4 — Estrutura da rede neural

### Ordem de estudo

12. [[outputs/Estrutura da rede neural|Estrutura da rede neural]]
13. [[perguntas aluno/o que são camadas em deep learning|O que são camadas em deep learning?]]

### O que aprender

- Diferença entre camada de entrada, camadas ocultas e camada de saída.
- Como a saída de uma camada se torna a entrada da próxima.
- Como escolher o tamanho da entrada conforme as características de `X`.
- Como a camada de saída depende do problema.
- Por que mais camadas e neurônios aumentam a capacidade, mas também aumentam o risco de sobreajuste.

### Antes de avançar

- [ ] Consigo desenhar uma rede e identificar entrada, camadas ocultas e saída.
- [ ] Consigo dizer quantos valores cada exemplo precisa fornecer à camada de entrada.
- [ ] Consigo explicar a diferença entre uma saída de regressão e uma saída de classificação binária.

---

## Etapa 5 — Como a rede aprende

### Ordem de estudo

14. [[outputs/Função de perda|Função de perda]]
15. [[outputs/Por que minimizamos a perda|Por que minimizamos a perda]]
16. [[outputs/Como a rede aprende|Como a rede aprende]]
17. [[outputs/Época|Época]]

### O que aprender

- Como a função de perda mede o erro.
- Por que o treinamento tenta minimizar a perda.
- O que acontece no forward pass e na retropropagação.
- Como o otimizador atualiza pesos e vieses.
- Diferença entre exemplo, lote, atualização e época.
- Diferença entre parâmetros treináveis e hiperparâmetros.

### Material principal

- [[aula1/Aula1_DEPAI.pdf|Aula 1 — DEPAI]], parte “Como a rede aprende”.
- [[aula2/Gabarito - Questoes de monitoria 2|Gabarito das questões de monitoria 2]], questões T01, T06, T07 e T17.

### Antes de avançar

- [ ] Consigo narrar um ciclo de treinamento do início ao fim.
- [ ] Consigo explicar por que a perda é necessária para ajustar os pesos.
- [ ] Consigo diferenciar uma época de uma atualização dos parâmetros.
- [ ] Entendo que reduzir a perda no treino não garante bom desempenho em dados novos.

---

## Etapa 6 — Primeiras redes com Keras

### Ordem de estudo

18. [[outputs/Keras|Keras]]
19. [[outputs/Como estruturar uma rede no Keras|Como estruturar uma rede no Keras]]
20. [[outputs/Classificação multiclasse e multirrótulo|Classificação multiclasse e multirrótulo]]
21. [[outputs/Como treinar uma rede no Keras|Como treinar uma rede no Keras]]
22. [[aula2/noteboock.ipynb|Notebook da Aula 2]]

### Ordem prática no notebook

1. Ler a receita `montar → compilar → treinar → usar`.
2. Montar a rede de regressão.
3. Contar os parâmetros das camadas densas.
4. Comparar a regressão logística com uma rede que possui camada oculta.
5. Treinar e avaliar o modelo de identificação de cédulas falsas.

### O que aprender

- Usar `keras.Sequential` para organizar as camadas.
- Declarar o formato da entrada com `keras.Input`.
- Criar camadas com `layers.Dense`.
- Escolher a ativação e a perda de acordo com a tarefa.
- Entender a função de `compile`, `fit`, `evaluate` e `predict`.
- Ler o resultado de `model.summary()`.
- Contar parâmetros com $(\text{entradas} + 1) \times \text{neurônios}$.

### Escolhas básicas

| Tarefa | Camada de saída | Perda |
| --- | --- | --- |
| Regressão | `Dense(1)` | `"mse"` |
| Classificação binária | `Dense(1, activation="sigmoid")` | `"binary_crossentropy"` |

### Antes de avançar

- [ ] Consigo montar uma rede pequena no Keras sem copiar o código inteiro.
- [ ] Consigo justificar o formato da entrada.
- [ ] Consigo escolher uma saída para regressão ou classificação binária.
- [ ] Consigo explicar o que `compile`, `fit`, `evaluate` e `predict` fazem.
- [ ] Consigo interpretar as camadas e os parâmetros mostrados por `summary()`.

---

## Etapa 7 — Avaliação e generalização

### Ordem de estudo

23. [[outputs/Vazamento de dados|Vazamento de dados]]
24. [[outputs/Aprendizado por atalho|Aprendizado por atalho]]

### O que aprender

- Por que treino, validação e teste devem ficar separados.
- O que é sobreajuste.
- Como reconhecer vazamento de informação.
- Por que transformações como padronização devem ser ajustadas apenas no treino.
- Quando registros de uma mesma pessoa ou grupo precisam permanecer juntos.
- Por que séries temporais exigem respeito à ordem do tempo.
- Como uma rede pode aprender uma pista acidental em vez do padrão desejado.
- Diferença entre vazamento de dados e aprendizado por atalho.

### Material principal

- [[aula1/Gabarito - Questoes de monitoria 1|Gabarito das questões de monitoria 1]], questões T08, T09 e T10.
- [[aula2/Gabarito - Questoes de monitoria 2|Gabarito das questões de monitoria 2]], questões T02 e T09 até T15.
- [[aula2/noteboock.ipynb|Notebook da Aula 2]], exercício das cédulas falsas.

### Antes de avançar

- [ ] Consigo explicar por que uma avaliação pode parecer melhor do que o desempenho real.
- [ ] Consigo identificar uma variável que não estaria disponível no momento da previsão.
- [ ] Sei preparar um padronizador sem usar informações do teste.
- [ ] Consigo diferenciar vazamento, sobreajuste e aprendizado por atalho.

---

## Etapa 8 — Revisão e prática

### Sequência final

1. Responder [[aula1/Questoes_monitoria_1.pdf|Questões de monitoria 1]] sem consultar o gabarito.
2. Corrigir as respostas com [[aula1/Gabarito - Questoes de monitoria 1|Gabarito das questões de monitoria 1]].
3. Explicar em voz alta o caminho dos dados até a saída da rede.
4. Desenhar uma rede e identificar entradas, pesos, vieses, ativações e saída.
5. Executar [[aula2/noteboock.ipynb|Notebook da Aula 2]] de cima para baixo e preencher as lacunas.
6. Responder [[aula2/Questoes_monitoria_2.pdf|Questões de monitoria 2]] sem consultar o gabarito.
7. Corrigir as respostas com [[aula2/Gabarito - Questoes de monitoria 2|Gabarito das questões de monitoria 2]].
8. Revisar apenas as etapas em que houver erros ou dificuldade para explicar.

### Teste de domínio

- [ ] Explico cada conceito sem depender das palavras exatas da nota.
- [ ] Resolvo pelo menos 80% das questões sem consultar o gabarito.
- [ ] Consigo relacionar os conceitos ao código do notebook.
- [ ] Consigo montar, treinar e avaliar uma rede pequena.
- [ ] Consigo perceber quando um resultado aparentemente bom não é confiável.

## Regra para avançar

Avance para a próxima etapa quando conseguir explicar o conteúdo com suas próprias palavras e concluir a lista “Antes de avançar”. Se uma explicação ainda estiver confusa, anote a dúvida e revise somente o ponto necessário antes de continuar.
