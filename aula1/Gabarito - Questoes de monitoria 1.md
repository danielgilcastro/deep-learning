---
tags:
  - deep-learning
  - aula-1
  - gabarito
---

# Gabarito - Questões de monitoria 1

Fonte: [[Questoes_monitoria_1.pdf]]

## Resumo

| Questão | Resposta | Tema principal |
| --- | --- | --- |
| T01 | **c** | Aprendizado supervisionado e correlações espúrias |
| T02 | **d** | Neurônio sigmoide e regressão logística |
| T03 | **c** | Fluxo de dados entre camadas densas |
| T04 | **d** | Classificação e regressão |
| T05 | **b** | Composição de camadas afins |
| T06 | **b** | Representação de dados e limitações do kNN |
| T07 | **c** | Necessidade de rótulos no aprendizado supervisionado |
| T08 | **b** | Correlação espúria e mudança de distribuição |
| T09 | **b** | Alta variância e overfitting |
| T10 | **a** | Ruído nos rótulos e erro irredutível |

## Gabarito comentado

### T01 - **c**

A rede aprende comparando suas previsões com os rótulos corretos e ajustando os pesos para reduzir o erro. Esse é o princípio do aprendizado supervisionado. Ela também pode aprender uma correlação espúria, como associar música de fundo a fogos de artifício, em vez de identificar apenas as características relevantes do estampido.

### T02 - **d**

Um único neurônio sigmoide ligado diretamente às quatro entradas possui pesos e viés treináveis. Esse modelo equivale à regressão logística e produz uma fronteira de decisão linear, portanto não consegue representar padrões não linearmente separáveis, como XOR.

### T03 - **c**

Em uma camada densa, o neurônio de saída recebe as ativações de todos os três neurônios da camada oculta. As cinco entradas originais influenciam a saída indiretamente, por meio desses neurônios ocultos.

### T04 - **d**

1. Estimar a quantidade de chamados produz um número: **regressão**.
2. Decidir se há disparo ou não escolhe uma categoria: **classificação**.
3. Decidir se haverá mais de 50 chamados também escolhe entre duas categorias: **classificação**.

Logo, a sequência é: **regressão; classificação; classificação**.

### T05 - **b**

Substituindo $u = 2x - 3$ na segunda camada:

$$
y = -4u + 5 = -4(2x - 3) + 5 = -8x + 12 + 5 = -8x + 17.
$$

Sem função de ativação entre as camadas, a composição de transformações afins continua sendo uma transformação afim. Mesmo com várias camadas desse tipo, a rede continua representando uma reta, e não uma curva.

### T06 - **b**

A distância usada pelo kNN compara as amostras posição por posição. Dois sons da mesma sirene, mas deslocados no tempo, podem parecer distantes nessa representação bruta. Um caminho melhor é utilizar características que representem o padrão do som e sejam menos sensíveis ao deslocamento temporal, inclusive representações aprendidas por uma rede.

### T07 - **c**

No treinamento supervisionado, a rede precisa de exemplos acompanhados das respostas corretas. O grupo deve definir o que conta como trote e rotular ao menos parte das chamadas. Esses rótulos são necessários tanto para treinar quanto para avaliar o modelo.

### T08 - **b**

O modelo pode ter aprendido o fundo das imagens: oficina para viaturas avariadas e pátio para viaturas sem avaria. O teste sorteado da mesma coleção mantém essa correlação e, por isso, pode superestimar o desempenho real. A verificação adequada é avaliar o modelo com fotos de viaturas avariadas também tiradas no pátio, reproduzindo o cenário de aplicação.

### T09 - **b**

Erro de treino quase zero acompanhado de previsões muito diferentes entre modelos treinados com amostras distintas indica **alta variância**, associada a overfitting. Cada rede aprendeu detalhes e ruídos particulares de sua amostra. Possíveis medidas incluem obter mais dados, aplicar regularização, reduzir a complexidade do modelo ou combinar as previsões de várias redes.

### T10 - **a**

Se supervisores experientes discordam em 25% dos casos, os próprios rótulos apresentam ambiguidade ou ruído. Isso cria um limite para o desempenho: aumentar a rede não elimina informações inconsistentes no alvo. É mais coerente revisar os critérios de rotulação e analisar os relatos em que houve discordância.
