# Mapa das exigências

## Enunciado e modelo de relatório

| Exigência | Onde está atendida |
| --- | --- |
| Notebook com Keras e download público | [[Projeto_Grupo4.ipynb]], células 1 a 8 de código, além da instalação |
| Preparação e exploração | Auditoria, contagens, amostras e hashes no notebook |
| Treino / validação / teste sem cópias compartilhadas | Célula 3 e `resultados/divisao.json` |
| Baseline | Classe mais frequente do treino, com desempate fixo |
| Primeira rede e melhoria justificada | CNN inicial e CNN Dropout; MLP como comparação adicional |
| Comparar na validação | `resultados/validacao.json`; relatório, seção 3 |
| Escolher sem usar teste | `resultados/selecao.json` gravado antes da avaliação final |
| Avaliar baseline e modelo escolhido no teste | `resultados/teste.json` |
| Curvas e análise de sobreajuste | `resultados/curvas.png`; seção 4 |
| Acertos, erros e matriz de confusão | Seção 5 e imagens em `resultados` |
| Relatório de até dez páginas e seis seções | [[Relatorio_Grupo4.pdf]] |
| Responsáveis por seção | Identificados no relatório conforme planejamento do Grupo 4 |
| Apresentação até 15 minutos e participação de todos | [[Apresentacao_Grupo4.pptx]] e [[Roteiro de apresentação]] |
| Teste em Google Colab | Notebook preparado; conferência no serviço ainda pendente |
| Aprovação da base e grupo | Não comprovada nos arquivos; confirmação do grupo com professor |

## Base nas aulas

| Material fornecido | Aplicação no projeto |
| --- | --- |
| Aula 1 - Introdução ao Deep Learning e às redes neurais | Aprendizado a partir de exemplos, pesos, representações e generalização |
| Aula 2 - Questões de monitoria e exemplos Keras | Separação treino/validação/teste, vazamento e uso de compile/fit |
| Aula 3 - Ativações, perdas e treinamento | ReLU nas camadas ocultas, softmax multiclasse, rótulos inteiros e entropia cruzada; taxa, batch e épocas |
| Aula 4 - Redes convolucionais | Conv2D, filtros, MaxPooling2D, Flatten e formato das imagens |
| Aula 5 - Regularização e aumentação | EarlyStopping e Dropout; cautela com aumentação e vazamento |

## Decisões adotadas para completar o que estava em aberto

- Mantivemos o objetivo de 36 classes indicado nas respostas e no planejamento.
- O baseline constante atende ao enunciado e à divisão de responsabilidades. A MLP também foi mantida como referência adicional por constar no planejamento inicial.
- A divisão inicial de 27/6/6 por classe foi adaptada para manter cópias exatas juntas, conforme a auditoria.
- A melhoria escolhida foi Dropout, isolando a alteração entre as CNNs. EarlyStopping foi usado nas três redes.
- Não criamos frontend, pois não é exigência do professor; a função de previsão no notebook permite uma demonstração simples.
- Os nomes indicam responsabilidades propostas nos materiais, não comprovam participação individual na execução automatizada. Todos precisam revisar e compreender o trabalho antes da entrega.
