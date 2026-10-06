---
tags:
  - deep-learning
  - index
  - mapa-de-estudo
---

# Index — Mapa progressivo de estudo

Este índice organiza os materiais do projeto em uma sequência de estudo baseada em pré-requisitos.

> [!info] Referências sem ligação no gráfico
> Os arquivos são indicados como caminhos em texto, e não como links internos. Assim, esta nota não cria conexões com eles no gráfico do Obsidian. Para abrir um material, use a busca rápida (`Ctrl + O`) ou localize o caminho no explorador de arquivos.

## Visão geral

```text
1. Fundamentos de aprendizado de máquina
                ↓
2. Dados e representações
                ↓
3. Neurônios, camadas e ativações
                ↓
4. Como a rede aprende
                ↓
5. Primeiras redes com Keras
                ↓
6. Avaliação e generalização
                ↓
7. Revisão e consolidação
```

## 1. Fundamentos de aprendizado de máquina

### Objetivos

- Diferenciar inteligência artificial, aprendizado de máquina e deep learning.
- Entender a diferença entre programação clássica e aprendizado supervisionado.
- Reconhecer entradas $X$, respostas $y$, função desconhecida $f$ e ruído $\varepsilon$.
- Distinguir problemas de classificação e regressão.
- Entender as três escolhas de um treinamento: modelo, perda e otimização.

### Materiais

- Material principal: `aula1/Aula1_DEPAI.pdf`, especialmente os blocos “ML e deep learning” e “Aprender: três escolhas”.
- Exercícios conceituais: `aula1/Gabarito - Questoes de monitoria 1.md`, questões T01, T04, T07 e T10.
- Revisão complementar: `aula2/Gabarito - Questoes de monitoria 2.md`, questões T03 e T17.

### Sinal de domínio

Você consegue explicar por que um modelo é treinado em exemplos, dizer se um problema é de classificação ou regressão e separar modelo, perda e otimização.

## 2. Dados e representações

### Objetivos

- Entender que uma representação é uma forma de codificar os dados.
- Diferenciar dados estruturados e não estruturados.
- Entender por que uma representação adequada facilita o aprendizado.
- Perceber a diferença entre características construídas manualmente e representações aprendidas por uma rede.
- Reconhecer como tabelas, imagens, textos e áudios chegam à rede como tensores numéricos.

### Materiais

- Material principal: `aula1/Aula1_DEPAI.pdf`, bloco “Representações”.
- Explicação aplicada: `perguntas aluno/como que a camada de entrada recebe dados, por um data frame ou outra coisa.md`.
- Exercícios conceituais: `aula1/Gabarito - Questoes de monitoria 1.md`, questões T06 e T08.
- Revisão complementar: `aula2/Gabarito - Questoes de monitoria 2.md`, questões T04, T10, T11, T12 e T15.

### Sinal de domínio

Você consegue descrever o caminho `arquivo → DataFrame → X e y → arrays ou tensores → modelo` e explicar por que a representação influencia o desempenho.

## 3. Neurônios, camadas e ativações

### Objetivos

- Entender um neurônio como função afim seguida de função de ativação.
- Identificar camada de entrada, camadas ocultas e camada de saída.
- Compreender pesos, viés, ReLU e sigmoide.
- Entender por que empilhar apenas funções afins continua produzindo uma função afim.
- Relacionar camadas ocultas à capacidade de representar relações não lineares.
- Entender o significado de profundidade em deep learning.

### Materiais

- Material principal: `aula1/Aula1_DEPAI.pdf`, bloco “A rede neural”.
- Explicação introdutória: `perguntas aluno/o que são camadas em deep learning.md`.
- Exercícios conceituais: `aula1/Gabarito - Questoes de monitoria 1.md`, questões T02, T03 e T05.
- Revisão complementar: `aula2/Gabarito - Questoes de monitoria 2.md`, questões T05, T16 e T18.

### Sinal de domínio

Você consegue acompanhar o fluxo dos dados por uma rede, calcular a saída simples de um neurônio e explicar por que uma ativação não linear é necessária.

## 4. Como a rede aprende

### Objetivos

- Diferenciar parâmetros treináveis de hiperparâmetros.
- Entender o papel da função de perda.
- Compreender, em nível conceitual, o forward pass e o backward pass.
- Entender como o gradiente e o otimizador atualizam pesos e vieses.
- Relacionar épocas, lotes e número de atualizações.

### Materiais

- Material principal: `aula1/Aula1_DEPAI.pdf`, bloco “Como a rede aprende”.
- Exercícios conceituais: `aula2/Gabarito - Questoes de monitoria 2.md`, questões T01, T06, T07 e T17.

### Sinal de domínio

Você consegue narrar um passo de treinamento: entrada dos dados, previsão, cálculo da perda, cálculo dos gradientes e atualização dos parâmetros.

## 5. Primeiras redes com Keras

### Objetivos

- Seguir a sequência `montar → compilar → treinar → usar`.
- Ler uma arquitetura criada com `keras.Sequential` e `layers.Dense`.
- Entender o formato esperado pela camada de entrada.
- Contar os parâmetros de uma camada densa.
- Escolher a camada de saída e a perda conforme o tipo de tarefa.

### Ordem prática

1. **Rede para regressão:** montar uma rede com entrada, camada oculta ReLU e saída linear.
2. **Contagem de parâmetros:** aplicar a fórmula $(\text{entradas} + 1) \times \text{neurônios}$.
3. **Classificação binária no plano:** comparar regressão logística e rede com camada oculta.
4. **Cédulas falsas:** carregar dados, separar $X$ e $y$, padronizar, treinar e avaliar.

### Materiais

- Notebook principal: `aula2/noteboock.ipynb`.
- Apoio sobre entrada de dados: `perguntas aluno/como que a camada de entrada recebe dados, por um data frame ou outra coisa.md`.
- Apoio sobre arquitetura: `perguntas aluno/o que são camadas em deep learning.md`.

### Sinal de domínio

Você consegue montar uma rede pequena, justificar sua entrada e sua saída, compilá-la, treiná-la e interpretar `summary()`, `fit()`, `predict()` e `evaluate()`.

## 6. Avaliação e generalização

### Objetivos

- Separar corretamente treino, validação e teste.
- Reconhecer sobreajuste, alto viés e alta variância.
- Evitar vazamento de informação.
- Escolher divisões adequadas para grupos e séries temporais.
- Comparar o modelo com uma referência simples.
- Entender correlações espúrias e aprendizado por atalho.

### Materiais

- Introdução aos problemas: `aula1/Gabarito - Questoes de monitoria 1.md`, questões T08, T09 e T10.
- Estudo principal: `aula2/Gabarito - Questoes de monitoria 2.md`, questões T02 e T09 a T15.
- Aplicação prática: `aula2/noteboock.ipynb`, Exercício 4, especialmente divisão, padronização e avaliação das cédulas.

### Sinal de domínio

Você consegue identificar quando uma avaliação é otimista, propor uma divisão coerente com o uso real e explicar a diferença entre desempenho de treino e desempenho em dados novos.

## 7. Revisão e consolidação

### Sequência sugerida

- [ ] Responder às questões de monitoria da Aula 1 sem consultar o gabarito.
- [ ] Explicar em voz alta o caminho dos dados desde o arquivo até a camada de entrada.
- [ ] Desenhar uma rede simples e identificar entradas, pesos, vieses, ativações e saída.
- [ ] Executar o notebook da Aula 2 de cima para baixo e preencher todas as lacunas.
- [ ] Comparar a regressão logística com a rede que possui camada oculta.
- [ ] Explicar por que a avaliação das cédulas usa dados de teste separados.
- [ ] Responder às questões de monitoria da Aula 2 sem consultar o gabarito.
- [ ] Revisar apenas os tópicos em que houver erro ou dificuldade de explicação.

### Materiais de revisão

- Questões: `aula1/Questoes_monitoria_1.pdf`.
- Gabarito: `aula1/Gabarito - Questoes de monitoria 1.md`.
- Questões: `aula2/Questoes_monitoria_2.pdf`.
- Gabarito: `aula2/Gabarito - Questoes de monitoria 2.md`.

## Critério para avançar

Avance para a etapa seguinte quando conseguir:

1. explicar os conceitos com suas próprias palavras;
2. resolver ao menos 80% das questões relacionadas sem consultar o gabarito;
3. relacionar o conceito a um trecho do notebook ou a um exemplo real;
4. identificar o que ainda não entendeu e formular uma pergunta específica.

## Próximos conteúdos previstos

Quando novos materiais forem adicionados, continuar o mapa nesta ordem:

1. curvas de aprendizado, sobreajuste e regularização;
2. redes convolucionais para imagens;
3. processamento de sequências;
4. mecanismos de atenção e Transformers;
5. projeto aplicado e comparação com modelos clássicos de machine learning.
