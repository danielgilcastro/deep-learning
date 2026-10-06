---
tags:
  - deep-learning
  - aula-2
  - gabarito
---

# Gabarito - Questões de monitoria 2

Fonte: [[Questoes_monitoria_2.pdf]]

## Resumo

| Questão | Resposta | Tema principal |
| --- | --- | --- |
| T01 | **b** | Hiperparâmetros e parâmetros treináveis |
| T02 | **c** | Divisão entre treino, validação e teste |
| T03 | **a** | Diferença entre programação e aprendizado de máquina |
| T04 | **d** | Aprendizado de representações em deep learning |
| T05 | **c** | Funções de ativação ReLU e sigmoide |
| T06 | **b** | Entropia cruzada |
| T07 | **d** | Lotes, épocas e atualização dos pesos |
| T08 | **a** | História das redes neurais |
| T09 | **d** | Sobreajuste e parada antecipada |
| T10 | **a** | Vazamento de informação |
| T11 | **c** | Divisão por grupos e vazamento entre pessoas |
| T12 | **b** | Validação de séries temporais |
| T13 | **a** | Viés, variância e escolha de hiperparâmetros |
| T14 | **d** | Ruído, viés e variância |
| T15 | **b** | Aprendizado por atalho |
| T16 | **c** | Teorema da aproximação universal |
| T17 | **a** | Modelo, perda e otimização |
| T18 | **b** | Fronteira linear e camada oculta |

## Gabarito comentado

### T01 - **b**

Hiperparâmetros são escolhas feitas antes ou durante a configuração do treinamento, como o número de camadas, a quantidade de neurônios por camada, a taxa de aprendizado e o tamanho do lote. Pesos e vieses não são hiperparâmetros: são parâmetros que a própria rede ajusta durante o treinamento.

### T02 - **c**

Os pesos são ajustados apenas com o conjunto de treino. O conjunto de validação serve para comparar as configurações, como redes com diferentes quantidades de camadas. Depois da escolha, o conjunto de teste deve ser usado uma única vez para estimar o desempenho final em dados novos. Consultar repetidamente o teste faria com que ele também influenciasse a escolha do modelo.

### T03 - **a**

Na programação clássica, uma pessoa escreve as regras e o computador as aplica aos dados para produzir respostas. No aprendizado supervisionado, o sistema recebe dados acompanhados das respostas corretas e ajusta um modelo que representa as regras aprendidas. Por isso, dizemos que ele é treinado, e não programado regra por regra.

### T04 - **d**

No exemplo da floresta aleatória, pessoas escolhem ou constroem características como o número de laços fechados de cada dígito. Na rede profunda, os pixels entram no modelo e as camadas aprendem representações progressivamente. As primeiras camadas podem detectar traços simples, enquanto as posteriores combinam esses traços em formas mais complexas. Os rótulos continuam necessários para o treinamento supervisionado.

### T05 - **c**

Primeiro calculamos a função afim:

$$
z = w_1x_1 + w_2x_2 + b = 2 \cdot 1 + (-1) \cdot 4 + 1 = -1.
$$

A ReLU devolve $\max(0,-1)=0$. A sigmoide devolve:

$$
\sigma(-1)=\frac{1}{1+e^1}\approx 0{,}27.
$$

### T06 - **b**

Na entropia cruzada, a perda para a probabilidade atribuída à resposta correta é $-\ln p$. Assim:

$$
-\ln(0{,}9)\approx 0{,}11
$$

e

$$
-\ln(0{,}1)\approx 2{,}30.
$$

A rede B recebe uma punição muito maior porque atribuiu probabilidade baixa à classe correta.

### T07 - **d**

Cada época possui:

$$
\frac{2000}{50}=40\text{ lotes}.
$$

Em 10 épocas, ocorrem $40 \times 10=400$ atualizações. Em cada atualização, o otimizador usa o gradiente calculado no lote e move os pesos na direção oposta, buscando reduzir a perda. O tamanho do passo depende da taxa de aprendizado.

### T08 - **a**

A correspondência correta é:

- **1958 - III:** o perceptron de Rosenblatt aprende pesos a partir de exemplos;
- **1969 - IV:** Minsky e Papert discutem limitações do perceptron, como não resolver XOR com um único neurônio;
- **1986 - II:** a popularização da retropropagação permite treinar redes com camadas ocultas;
- **2012 - I:** uma rede convolucional profunda vence a competição ImageNet.

Logo, a sequência é **1-III; 2-IV; 3-II; 4-I**.

### T09 - **d**

A perda de treino continua diminuindo, mas a perda de validação atinge seu menor valor na época 15 e depois aumenta. Isso indica sobreajuste: a rede melhora nos exemplos que já viu, mas perde capacidade de generalizar. Uma solução é usar parada antecipada e conservar os pesos da época com menor perda de validação. Também podem ajudar uma rede menor, mais dados ou regularização.

### T10 - **a**

A variável “número de policiais no local” só é conhecida depois do atendimento. No momento da chamada, que é quando a previsão deve ser feita, essa informação ainda não existe. Além disso, a presença de mais policiais pode revelar que uma segunda viatura foi enviada. Usar essa coluna causa vazamento de informação e torna os 98% de validação pouco confiáveis.

### T11 - **c**

Ao sortear registros individualmente, dados da mesma pessoa podem aparecer tanto no treino quanto na validação. A rede pode reconhecer características daquela pessoa, produzindo uma avaliação otimista. Como o uso real envolve pessoas sem registro anterior, todos os registros de uma pessoa devem permanecer no mesmo conjunto. Portanto, o resultado de 71% é a estimativa mais próxima do cenário real.

### T12 - **b**

Em uma série temporal, o modelo será usado para prever o futuro a partir do passado. Sortear os meses mistura períodos anteriores e posteriores, permitindo que a avaliação use uma situação mais fácil do que a real. A divisão deve respeitar a ordem do tempo, por exemplo: treino até 2022, validação em 2023 e teste em 2024.

### T13 - **a**

Com $k=1$, o kNN memoriza os exemplos de treino e apresenta grande diferença entre treino e validação, sinal de alta variância. Com $k=200$, os dois resultados são baixos, sinal de alto viés. O valor $k=15$ possui o melhor desempenho de validação e deve ser escolhido antes da avaliação final no conjunto de teste.

### T14 - **d**

As três ações atacam fontes diferentes de erro:

1. Critérios de rotulagem inconsistentes geram **ruído**; um manual mais claro reduz as divergências.
2. Uma rede pequena com baixo desempenho no treino e na validação apresenta **alto viés**; aumentar sua capacidade pode ajudar.
3. Uma rede muito melhor no treino do que na validação apresenta **alta variância**; obter mais dados pode reduzir o sobreajuste.

Logo, a sequência é **ruído; viés; variância**.

### T15 - **b**

A rede pode ter aprendido a procurar o nome da delegacia no rodapé, em vez de compreender o conteúdo do relato. Uma validação sorteada da mesma base preserva esse atalho. A verificação adequada é testar relatos de outras delegacias e comparar casos equivalentes com e sem o rodapé. Se o desempenho cair, a rede dependia dessa pista espúria.

### T16 - **c**

O teorema da aproximação universal afirma que existe uma rede com uma camada oculta e neurônios suficientes capaz de aproximar uma ampla classe de funções. Ele não informa quantos neurônios serão necessários, não garante que o treinamento encontrará os pesos corretos e não garante bom desempenho em dados novos. Também não permite eliminar o ruído ou a ambiguidade dos dados.

### T17 - **a**

A regressão logística representa uma função afim seguida de uma sigmoide. Uma rede com camadas ocultas pertence a uma classe de modelos mais flexível, capaz de representar relações não lineares. A otimização também pode mudar, por exemplo de L-BFGS para Adam. Para classificação binária, porém, ambas podem usar a mesma perda de entropia cruzada.

### T18 - **b**

Um único neurônio sigmoide sem camada oculta equivale a uma regressão logística. Sua fronteira de decisão é linear e não consegue separar um círculo central de um anel ao redor. Treinar por mais épocas não corrige essa limitação. Uma camada oculta com vários neurônios e ReLU permite combinar diferentes regiões lineares e aproximar uma fronteira curva.
