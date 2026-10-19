# Respostas das sessões - preenchidas

Esta versão complementa as respostas originais com decisões de implementação e resultados da execução de 19/10/2026. Os resultados completos estão em [[Relatorio_Grupo4]] e no notebook [[Projeto_Grupo4.ipynb]].

## 1. Objetivo da modelagem

**Qual problema queremos resolver?** Reconhecer automaticamente um algarismo ou letra maiúscula em uma imagem binária de um único caractere.

**O que entra na rede e o que ela devolve?** Entra uma imagem 20×16×1, com pixels 0 e 1. A saída contém 36 pontuações softmax; a classe de maior pontuação é a previsão. As classes são 0-9 e A-Z.

**Por que utilizar Deep Learning?** Uma CNN aprende padrões locais de traços e curvas diretamente dos pixels. A plausibilidade dessa abordagem deve ser testada; não garante vantagem sobre métodos simples.

## 2. Dados utilizados

**De onde vieram os dados?** Do Binary Alpha Digits, escolhido no [catálogo TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/binary_alpha_digits). Usamos o MAT preservado na NYU, com o mesmo checksum registrado no catálogo.

**Como foram explorados e preparados?** Conferimos 1.404 registros, 39 por classe, dimensões, valores binários e rótulos lidos do arquivo. Exibimos uma imagem de treino por classe e auditamos duplicatas. Convertimos os pixels para float32 sem dividir por 255. As 36 classes foram mantidas.

**Como foram divididos?** Pelo hash dos pixels, mantendo cópias no mesmo conjunto. Grupos estratificados pela combinação de rótulos, com seed 42: 971 treino, 217 validação e 216 teste. Não existem cópias exatas compartilhadas entre conjuntos. Não há identificação de escritor para controlar esse fator.

## 3. Arquitetura e desempenho

**Como a rede foi construída?** Duas convoluções (16 e 32 filtros 3×3, ReLU, padding same), cada uma seguida de MaxPooling2D(2), depois Flatten, Dense(64, ReLU) e Dense(36, softmax). O segundo experimento adiciona Dropout(0,3) antes da saída. As duas CNNs têm 48.164 parâmetros. Também treinamos uma MLP adicional de 22.884 parâmetros.

**Quais configurações foram utilizadas?** Adam(0,001), batch 32, até 80 épocas, sparse_categorical_crossentropy e EarlyStopping em val_loss, patience 10, restore_best_weights=True. A CNN inicial executou 20 épocas e restaurou a 10; a CNN Dropout executou 39 e restaurou a 29.

**Qual métrica foi escolhida?** Acurácia como principal; macro-F1, precisão e recall macro como complementares. A base é balanceada, e o teste tem seis imagens por classe.

**Como o resultado se compara ao baseline?** Na validação: baseline 2,76%, MLP 71,43%, CNN inicial 73,73%, CNN Dropout 77,42%. No teste final: baseline 2,78% e CNN Dropout 82,41% (178/216). A rede foi escolhida pela validação, antes do teste.

## 4. Análise do treinamento

**O que aconteceu durante o treinamento?** A perda de treino caiu nos três modelos. A perda de validação atingiu um mínimo e depois estabilizou ou aumentou. O EarlyStopping interrompeu cada rede após dez épocas sem novo mínimo e restaurou os melhores pesos.

**Há overfitting ou underfitting?** A MLP e a CNN inicial exibem separação crescente entre treino e validação, compatível com overfitting. O Dropout reduziu esse efeito, mas não o eliminou. As curvas não sugerem subajuste como problema principal das duas redes sem Dropout.

**O que tentamos melhorar?** Adicionamos Dropout de 30% na camada densa, para reduzir dependência excessiva de unidades. Na validação, aumentou oito acertos e 3,69 pontos percentuais. É o resultado de uma única execução, sem comprovação estatística de superioridade geral.

## 5. Limitações

**Em quais situações o modelo erra?** Entre outras, em caracteres com traços semelhantes e imagens de baixa resolução. Foram 38 erros no teste; O→0 ocorreu quatro vezes e S→5, duas vezes. Exemplos e matriz estão no relatório.

**Quais exemplos têm maior dificuldade?** O teve recall de 16,67% (1/6); K e S, 50% (3/6). Há apenas seis exemplos de teste por classe, portanto um erro altera o recall em 16,67 pontos percentuais.

**Qual problema dos dados não foi resolvido?** Todas as imagens de 0 aparecem também como O. Não há informação nos pixels para distinguir esses rótulos. A divisão por grupos evita vazamento, mas não corrige a ambiguidade. A base também não permite verificar separação por escritor.

## 6. Uso pretendido e restrições

**Para que poderia ser utilizado?** Demonstração acadêmica e sugestão de transcrição de caracteres isolados, binarizados, recortados e orientados como os exemplos da base.

**Que decisão poderia apoiar?** Sugerir ao usuário uma classe para revisão humana. Não existe nível de confiabilidade operacional validado; a softmax não foi calibrada.

**Em quais situações não deveria ser usado?** Leitura automática de documentos ou placas reais, identificação de pessoas, decisões sancionatórias, palavras completas, minúsculas, fotografias coloridas ou entradas fora das condições estudadas. Seriam necessárias validação externa, análise de erros e revisão humana.
