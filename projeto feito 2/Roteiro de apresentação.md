# Roteiro de apresentação — até 15 minutos

Use os dez slides de [[Apresentacao_Grupo4.pptx]]. Cada pessoa fala por cerca de três minutos. Os números abaixo são os do [[Projeto_Grupo4.ipynb|notebook do projeto]].

| Pessoa | Slides | O que explicar |
| --- | --- | --- |
| Bruno Groppo | 1 e 2 | Problema, entrada, saída e referência simples. |
| Bruno Pimentel | 3 e 4 | Dados, imagens repetidas e divisão. |
| Reynato Junior | 5 e 6 | Camadas da rede e treinamento. |
| Wallace Jardim | 7 e 8 | Comparação e curvas de perda. |
| Daniel Gil | 9 e 10 | Teste, erros e limites de uso. |

## Bruno Groppo — slides 1 e 2

“Nosso projeto identifica **um caractere por vez**. A imagem mede 20 por 16 pixels e contém um número de 0 a 9 ou uma letra maiúscula de A a Z. A resposta é uma entre 36 classes.”

“Começamos com uma referência simples: prever sempre `0`. Ela acertou 6 das 217 imagens de validação, ou 2,76%. Depois, comparamos redes treinadas com os mesmos dados.”

## Bruno Pimentel — slides 3 e 4

“A equipe escolheu a base Binary Alpha Digits no catálogo TensorFlow Datasets. Ela tem 1.404 imagens, 39 por classe. Os pixels já valem 0 ou 1.”

“Encontramos imagens iguais com rótulos `0` e `O`. Mantivemos cada grupo de imagens idênticas no mesmo conjunto. Ficamos com 971 imagens de treino, 217 de validação e 216 de teste. Assim, não há uma cópia exata em conjuntos diferentes.”

## Reynato Junior — slides 5 e 6

“A rede convolucional olha pequenas partes da imagem para encontrar traços. Em seguida, reduz o tamanho dos dados, combina o que encontrou e escolhe uma das 36 classes.”

“Treinamos em lotes de 32 imagens, com até 80 épocas. A parada antecipada acompanha a perda de validação. Uma época é uma passagem por todo o treino. O teste ficou reservado para o final.”

## Wallace Jardim — slides 7 e 8

“Na validação, a rede inicial acertou 160 imagens. Acrescentamos Dropout, que desliga temporariamente algumas saídas durante o treino. A nova rede acertou 168. Foram **oito acertos a mais nesta execução**.”

“O gráfico mostra que a perda de treino continuou caindo mesmo quando a validação já não melhorava muito. Isso é sinal de sobreajuste. O Dropout ajudou nesta execução, mas não garante melhora em qualquer base.”

## Daniel Gil — slides 9 e 10

“Depois de escolher a rede pela validação, fizemos o teste final. Ela acertou 178 de 216 imagens: 82,41%. Errou 38.”

“Um problema é que há imagens idênticas chamadas `0` e `O`. O modelo vê os mesmos pixels e recebe respostas diferentes. Por isso, o resultado serve para esta demonstração com caracteres isolados. Não testamos fotografias, placas ou documentos reais.”

## Perguntas para praticar

1. **Por que separar treino, validação e teste?** O treino ajusta a rede; a validação orienta a escolha; o teste mede o resultado final.
2. **Por que a saída tem 36 valores?** Há 36 classes possíveis e uma resposta para cada imagem.
3. **O que é uma época?** Uma passagem por todos os exemplos de treino.
4. **O que é Dropout?** Uma forma de desligar temporariamente algumas saídas durante o treino, explicada na aula 5.
5. **Por que `0` e `O` são difíceis?** Nesta base, há imagens com pixels idênticos e rótulos diferentes.
6. **O que significa 82,41%?** São 178 acertos entre as 216 imagens reservadas para o teste deste experimento.
