---
tags:
  - deep-learning
  - aula-3
  - gabarito
---

# Gabarito - Questões da aula 3

Fonte: [[Questoes_aula_3.pdf]]

## Resumo

| Questão | Resposta | Tema principal |
| --- | --- | --- |
| T01 | **d** | Softmax e competição entre classes |
| T02 | **b** | Acurácia como métrica e entropia cruzada como perda |
| T03 | **b** | Taxa de aprendizado e divergência |
| T04 | **c** | Parada antecipada e restauração dos melhores pesos |
| T05 | **a** | ReLU e função linear por partes |
| T06 | **a** | MAE, MSE e erros grandes |
| T07 | **b** | Divisão de validação, lotes e atualizações |
| T08 | **a** | Entropia cruzada e erros confiantes |
| T09 | **a** | Tamanho do passo na descida do gradiente |
| T10 | **b** | Neurônios ReLU mortos |
| T11 | **b** | Desbalanceamento de classes e recall |
| T12 | **c** | Unidades de MAE e MSE |

## Gabarito comentado

### T01 - **d**

A *softmax* transforma as três pontuações em probabilidades que somam 1. A probabilidade de uma classe é sua exponencial dividida pela soma das exponenciais de **todas** as classes. Se apenas a pontuação de roubo aumenta, sua probabilidade sobe e as de furto e outro caem, mesmo que as pontuações destas duas não mudem. Elas disputam a mesma soma total.

### T02 - **b**

A acurácia conta quantas previsões acertaram após escolher uma classe. Pequenas mudanças nos pesos geralmente não mudam essa escolha; por isso, a acurácia fica constante em muitos trechos e não oferece um gradiente útil para o treinamento usual. Além disso, dois acertos com probabilidades de 0,51 e 0,99 recebem a mesma pontuação de acurácia. A entropia cruzada diferencia esses casos e fornece um sinal de ajuste. A acurácia continua útil para **avaliar** o modelo.

### T03 - **b**

A perda cresce rapidamente, de 0,69 até 312,6, e depois vira `nan` (valor numérico indefinido). Isso é compatível com passos de otimização grandes demais: com `learning_rate=0.5`, o Adam pode ultrapassar regiões de menor perda e divergir. A primeira tentativa é reduzir bastante a taxa, por exemplo para 0,001, e repetir o treino. Sobreajuste seria identificado comparando treino e validação; aqui a própria perda de treino está explodindo.

### T04 - **c**

O melhor valor de `val_loss` ocorreu na época 23. Com `patience=5`, o treinamento tolera cinco épocas seguidas sem melhora: 24, 25, 26, 27 e 28. Portanto, para na **época 28**. Como `restore_best_weights=True`, o modelo termina com os **pesos da época 23**.

### T05 - **a**

A ReLU devolve zero para entradas negativas e mantém as positivas: $\operatorname{ReLU}(z)=\max(0,z)$.

| Hora | Cálculo | $y$ |
| --- | --- | --- |
| 4h | $2\cdot 0-3\cdot 0$ | **0** |
| 10h | $2(10-6)-3\cdot 0$ | **8** |
| 18h | $2(18-6)-3(18-14)$ | **12** |

Até 6h, a saída é zero. Entre 6h e 14h, ela cresce com inclinação 2. Depois das 14h, passa a decrescer com inclinação $2-3=-1$. Assim, a curva é **linear por partes**, com dobras em 6h e 14h, determinadas pelos deslocamentos dentro das ReLUs.

### T06 - **a**

O **MAE** é a média dos valores absolutos dos erros; o **MSE** é a média dos erros ao quadrado.

| Modelo | MAE | MSE |
| --- | --- | --- |
| A: $4,4,4,4$ | $(4+4+4+4)/4=4$ | $(16+16+16+16)/4=16$ |
| B: $0,0,0,12$ | $(0+0+0+12)/4=3$ | $(0+0+0+144)/4=36$ |

Logo, o MAE prefere **B**, mas o MSE prefere **A**. Se um atraso muito grande for especialmente grave, o MSE expressa melhor essa prioridade porque ele eleva o erro ao quadrado: o erro de 12 pesa muito mais que cada erro de 4.

### T07 - **b**

`validation_split=0.25` separa $12.000\times 0{,}25=3.000$ linhas para validação. Restam **9.000** linhas para o treino e para as atualizações dos pesos. Com lotes de 64:

$$
\left\lceil\frac{9.000}{64}\right\rceil=141\text{ lotes por época}.
$$

O último lote é menor, mas ainda conta. O contador mostra **141/141**. Em 30 épocas, são $141\times 30=\mathbf{4.230}$ atualizações, supondo uma atualização por lote de treino. Os lotes de validação não atualizam os pesos.

### T08 - **a**

Na entropia cruzada, a perda de um exemplo é $-\ln(p)$, em que $p$ é a probabilidade dada à resposta correta. Assim:

$$
-\ln(0{,}4)\approx 0{,}92,\qquad -\ln(0{,}01)\approx 4{,}61.
$$

As duas redes têm a mesma acurácia, mas a B dá probabilidade extremamente baixa à classe correta quando erra. Por isso, seus erros custam muito mais e sua perda de validação é maior. Isso merece atenção se as probabilidades forem usadas para priorizar chamadas.

### T09 - **a**

Com perda $w^2$, o gradiente é $2w$. Partindo de $w=2$, o próximo valor é $w_{\text{novo}}=2-\eta\cdot 4$, onde $\eta$ é a taxa de aprendizado:

| Taxa $\eta$ | Peso após um passo | Com passos repetidos |
| --- | --- | --- |
| $0{,}25$ | **1** | O peso é reduzido à metade a cada passo e se aproxima de 0. |
| $1{,}0$ | **−2** | O peso alterna entre 2 e −2; a perda fica em 4. |
| $1{,}5$ | **−4** | O valor absoluto do peso dobra a cada passo; a perda cresce. |

A alternativa **a** descreve esse comportamento. Rigorosamente, com taxa 0,25 o peso **se aproxima** do mínimo 0; ele não chega exatamente a 0 em um número finito de passos. Com taxa 1,5, o crescimento pode acabar causando `nan` por limites numéricos.

### T10 - **b**

Se a entrada da ReLU é negativa para todos os exemplos, ela devolve sempre zero. Nessa região, seu gradiente também é zero; esses **neurônios mortos** deixam de receber ajustes úteis nos seus pesos. Como três dos quatro neurônios ocultos estão nessa situação, a rede perde capacidade de formar a fronteira curva necessária para separar centro e anel. Vale tentar uma taxa de aprendizado menor, outra inicialização, mais neurônios ou **Leaky ReLU**, que mantém uma pequena inclinação para valores negativos.

### T11 - **b**

Só 3% das chamadas são da classe de interesse. Um modelo que responda sempre “não” acerta os outros 97% e atinge **97% de acurácia**, embora não identifique nenhum caso real de violência doméstica. É essencial verificar o **recall** dessa classe: entre todos os casos reais, qual proporção o modelo encontrou? Também é útil conferir os falsos positivos e a precisão, mas a acurácia isolada não justifica o uso.

### T12 - **c**

O **MAE de validação é 3,0 minutos**: em média, o valor absoluto do erro foi 3 minutos. O **MSE de validação é 25,0 minutos²**, pois os erros foram elevados ao quadrado. Sua raiz, o RMSE, é $\sqrt{25}=5$ minutos; ela não é o erro absoluto médio. O fato de RMSE ser maior que MAE indica que os erros têm magnitudes diferentes e que alguns erros maiores pesam bastante no MSE. Esses dois números, sozinhos, não demonstram sobreajuste.
