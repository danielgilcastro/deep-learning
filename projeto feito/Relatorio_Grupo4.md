# Reconhecimento de caracteres alfanuméricos

Relatório do modelo | IASEG - Disciplina 3 - Deep Learning | Grupo 4

Bruno Groppo • Bruno Pimentel • Reynato Junior • Wallace Jardim • Daniel Gil

Dataset: Binary Alpha Digits | Execução local: 19/10/2026 | Professor: Rafael Stutz

## 1. Objetivo da modelagem

Responsável: Bruno Groppo.

Identificar automaticamente a letra maiúscula ou o algarismo presente em uma imagem binária de um único caractere.

A entrada é uma matriz de 20 × 16 pixels com um canal; a saída contém 36 pontuações softmax, uma para cada classe de 0 a 9 e de A a Z. A previsão é a classe de maior pontuação. Trata-se de classificação multiclasse: cada registro possui um único rótulo, e não um valor contínuo.

Deep Learning é plausível porque camadas convolucionais podem aprender padrões espaciais, como traços, curvas e encontros de linhas, diretamente dos pixels. A base pequena não permite presumir superioridade sobre métodos simples; por isso comparamos as redes com uma referência constante e uma MLP.

A aplicação estudada é uma demonstração de reconhecimento de caracteres já recortados e binarizados. Segmentar palavras ou ler placas em fotografias está fora do escopo.

## 2. Dados utilizados

Responsável: Bruno Pimentel.

A base foi escolhida nas respostas das sessões a partir do catálogo TensorFlow Datasets. O arquivo original preservado pela NYU contém 1.404 imagens, 39 por classe. Utilizamos todas as imagens e mantivemos seus rótulos. A fonte atribui os dados ao sistema Algoval, de Simon Lucas; os endereços estão nas referências.

| Característica | Verificação |
| --- | --- |
| Quantidade / classes | 1.404 registros / 36 classes |
| Entrada | 20 × 16 × 1; valores 0 e 1 |
| Alvo | Índice inteiro da classe, de 0 a 35 |
| Imagens distintas | 1.363 padrões únicos de pixels |
| Conjunto oficial | Um único split train; sem teste oficial separado |

A execução e as métricas foram produzidas em Python local. O notebook foi preparado para Colab, mas a execução dentro do serviço Google Colab ainda precisa ser conferida pelo grupo. A aprovação da base e a autorização do grupo com cinco pessoas não estão comprovadas nos materiais.


---

## 2. Dados utilizados - exploração e integridade

Figura 1. Um exemplo de treino por classe. Matrizes exibidas na orientação original; a semelhança entre 0 e O também aparece visualmente.

![[resultados/amostras.png]]

O endereço antigo de download retornou HTTP 403. A cópia preservada pela própria NYU foi baixada e seu SHA-256 coincidiu com o checksum publicado pelo TensorFlow Datasets. Lemos os rótulos do MAT e conferimos a sequência 0-9, A-Z. Validamos formato, contagens, valores binários e ausência de valores não finitos. Convertê-los para float32 foi suficiente: não dividimos por 255, pois os pixels já estão em 0/1.

### Duplicatas e prevenção de vazamento

A auditoria encontrou 39 grupos com repetições, totalizando 41 registros além dos padrões únicos. Desses grupos, 38 contêm rótulos conflitantes: as 39 imagens da classe 0 coincidem com as 39 da classe O, incluindo uma repetição interna. Há ainda uma repetição na classe 7. Não é possível distinguir 0 de O apenas pelos pixels nessa base.

Agrupamos imagens pelo hash dos pixels, independentemente do rótulo. Cada grupo inteiro foi destinado a um único conjunto. Os grupos foram estratificados pela combinação de rótulos e embaralhados com seed 42: aproximadamente 70% para treino e 15% para cada reserva. Asserções verificaram que nenhum índice nem hash aparece em mais de um conjunto.

| Conjunto | Registros | Imagens únicas | Por classe |
| --- | --- | --- | --- |
| Treino | 971 | 943 | 27; classe 7: 26 |
| Validação | 217 | 210 | 6; classe 7: 7 |
| Teste | 216 | 210 | 6 em todas |

A proposta inicial de 972/216/216 foi ajustada para preservar as duplicatas juntas. Não há informação de escritor; portanto, o controle elimina cópias exatas entre conjuntos, mas não demonstra separação por pessoa nem detecta todas as imagens quase idênticas.


---

## 3. Arquitetura e desempenho

Responsáveis: Reynato Junior e Bruno Groppo.

A MLP adicional usa Flatten, Dense(64, ReLU) e Dense(36, softmax), com 22.884 parâmetros. A CNN inicial e a CNN com Dropout têm a estrutura abaixo. A única alteração entre as CNNs é Dropout(0,3), que não acrescenta pesos treináveis.

| Camada da CNN | Saída por imagem | Parâmetros |
| --- | --- | --- |
| Entrada | 20 × 16 × 1 | 0 |
| Conv2D: 16 filtros 3×3, same, ReLU | 20 × 16 × 16 | 160 |
| MaxPooling2D(2) | 10 × 8 × 16 | 0 |
| Conv2D: 32 filtros 3×3, same, ReLU | 10 × 8 × 32 | 4.640 |
| MaxPooling2D(2) e Flatten | 5 × 4 × 32 → 640 | 0 |
| Dense(64, ReLU) | 64 | 41.024 |
| Dropout(0,3), só no segundo experimento | 64 | 0 |
| Dense(36, softmax) | 36 | 2.340 |
| Total | 36 classes | 48.164 |

Convoluções aprendem padrões locais; pooling reduz as dimensões espaciais; Flatten organiza os mapas em um vetor; a camada densa combina as características. ReLU introduz não linearidade. Softmax é adequada para uma classe entre 36, e sparse_categorical_crossentropy corresponde aos rótulos inteiros. A perda penaliza baixa pontuação para a classe correta.

As três redes usam Adam com learning_rate=0,001, batch_size=32 e máximo de 80 épocas. EarlyStopping monitora val_loss, com paciência de dez épocas e restauração dos melhores pesos. Inicializadores e embaralhamento usam sementes fixas. As CNNs partem dos mesmos pesos nas camadas correspondentes; cada modelo é criado novamente antes de treinar.

### Métrica e seleção

Acurácia é a métrica principal, pois as classes têm frequências iguais na base e no teste. Macro-F1, precisão macro e recall macro complementam a análise por classe. O baseline escolhe a classe mais frequente no treino; no empate, a de menor índice, 0. Para cada rede restauramos a época de menor perda de validação. Escolhemos a rede com maior acurácia de validação; empates seriam resolvidos pela menor perda e pelo menor número de parâmetros.

Não utilizamos teste para escolher arquitetura, época ou hiperparâmetros. O teste foi acessado para métricas e análise de erros apenas após a seleção final.


---

## 3. Arquitetura e desempenho - resultados

### Comparação na validação (217 imagens)

| Modelo | Acurácia | Macro-F1 | Alteração / referência |
| --- | --- | --- | --- |
| Baseline constante | 2,76% | 0,001 | Sempre prevê 0 |
| MLP | 71,43% | 0,701 | Referência densa adicional |
| CNN inicial | 73,73% | 0,740 | Convoluções e pooling |
| CNN Dropout | 77,42% | 0,771 | Dropout de 30% na camada densa |

A CNN com Dropout obteve 77,42% na validação (168/217), contra 73,73% da CNN inicial (160/217). A diferença foi de 3,69 pontos percentuais, ou oito acertos. Essa foi a configuração escolhida; o ganho se refere a uma única divisão e execução, sem demonstração de significância estatística.

### Avaliação final no teste (216 imagens)

| Modelo | Acurácia | Macro-F1 | Acertos |
| --- | --- | --- | --- |
| Baseline constante | 2,78% | 0,002 | 6/216 |
| CNN Dropout | 82,41% | 0,817 | 178/216 |

O modelo escolhido acertou 178 imagens e errou 38, com acurácia de 82,41%. A precisão macro foi 83,54% e o recall macro, 82,41%. A referência constante acertou seis imagens. O resultado sustenta aprendizado de padrões úteis nesta base; não comprova desempenho em fotografias ou documentos reais.

A acurácia de teste ficou acima da validação. Isso pode ocorrer por variação da composição dos conjuntos pequenos; não significa que o teste foi mais fácil por construção nem demonstra estabilidade. A MLP e a CNN inicial não foram avaliadas no teste, para preservar a avaliação final do modelo selecionado.

### Reprodução e rastreabilidade

Projeto_Grupo4.ipynb contém as etapas completas e saídas da execução local, incluindo as curvas, métricas e previsões. A pasta resultados guarda históricos, índices das divisões, auditoria de duplicatas, métricas por classe, previsões do teste e o modelo_final.keras. experimento.py é a versão em script; gerar_relatorio.py recompõe este documento a partir dos resultados.

Ambiente observado: Python 3.14.7, TensorFlow 2.22.0-rc0, Keras 3.15.1, NumPy 2.5.3. TensorFlow é uma versão de pré-lançamento neste computador. O Colab pode usar outras versões; diferenças numéricas são possíveis. As versões completas estão em ambiente.json.


---

## 4. Análise do treinamento

Responsável: Wallace Jardim.

Figura 2. Perda e acurácia de treino e validação. As linhas pontilhadas indicam a época de menor perda de validação, restaurada pelo EarlyStopping.

![[resultados/curvas.png]]

| Rede | Épocas executadas | Melhor época | Menor val_loss |
| --- | --- | --- | --- |
| MLP | 29 | 19 | 0,970 |
| CNN inicial | 20 | 10 | 0,840 |
| CNN Dropout | 39 | 29 | 0,689 |

Na MLP, a perda de treino caiu de 3,448 para 0,148, enquanto a validação atingiu mínimo de 0,970 na época 19 e terminou em 1,007. A distância crescente entre as curvas indica sobreajuste. Na CNN inicial, a melhor perda de validação foi 0,840 na época 10; o treino continuou melhorando, mas a validação oscilou e terminou em 0,888.

A tentativa de melhoria foi acrescentar Dropout(0,3) antes da camada de saída, mantendo as demais escolhas. Esperávamos reduzir dependência excessiva de unidades da camada densa. A menor perda de validação passou a 0,689, na época 29, com acurácia de 77,42%. O treino terminou na época 39, após dez épocas sem novo mínimo; os pesos da época 29 foram restaurados.

O Dropout melhorou a validação nesta execução e retardou o sobreajuste, mas não o eliminou: a perda de treino continuou caindo enquanto a validação estabilizava. Não há evidência principal de subajuste na MLP ou na CNN inicial, pois o desempenho de treino supera consideravelmente o de validação. No Dropout, a métrica de treino é calculada com unidades desativadas, ao contrário da validação; essa diferença exige cautela na comparação das curvas.

Não testamos aumentação, transferência de aprendizado ou uma busca extensa. Virar caracteres horizontalmente pode mudar sua identidade, e transferir modelos de imagens naturais exigiria adaptações adicionais. A comparação controlada com Dropout atende à tentativa de melhoria exigida.


---

## 5. Limitações

Responsável: Daniel Gil.

Figura 3. Matriz de confusão do teste. Linhas: rótulo real; colunas: previsão. Cada classe tem seis exemplos; células vazias representam zero.

![[resultados/matriz_confusao.png]]

As maiores contagens de confusão foram O → 0 (quatro casos) e S → 5 (dois casos). A classe O acertou apenas 1/6 (recall 16,67%); K e S acertaram 3/6 (50%). Um único erro altera o recall de uma classe em 16,67 pontos percentuais, o que torna essas estimativas instáveis.

As classes 0 e O somam cinco acertos em doze exemplos e sete erros. Seis pares de imagens do teste têm pixels idênticos e rótulos opostos. Um classificador determinístico baseado apenas na imagem precisa errar pelo menos seis desses doze registros, mesmo que acerte todos os outros. A limitação está nos dados, não apenas na arquitetura.

A base não identifica escritores nem documenta a diversidade necessária para o uso real. Imagens quase idênticas podem persistir entre conjuntos. Os resultados vêm de uma única seed; novos estudos devem comparar divisões por grupos no conjunto de desenvolvimento e reservar um novo teste independente.


---

## 5. Limitações - exemplos e próximos experimentos

Figura 4. Primeiros seis acertos e seis erros em ordem de índice no teste. Os IDs permitem localizar os registros em previsoes_teste.npz. A seleção é ilustrativa, sem pretensão de representar a frequência dos erros.

![[resultados/acertos_erros.png]]

Os exemplos mostram que semelhanças de traço, baixa resolução e ambiguidades do rótulo afetam a classificação. A análise não estabelece a causa de cada erro: seria necessário inspecionar mais amostras, testar hipóteses e verificar a origem dos dados. A confusão 0/O permanece sem solução dentro da tarefa de 36 classes.

Com mais tempo, compararíamos a CNN com k-vizinhos ou regressão logística, avaliaríamos pequenas translações somente no treino e repetiríamos a seleção em divisões por grupos. Unir 0/O seria outra tarefa, com 35 classes, e exigiria aprovação e novo protocolo. Para o uso real, a prioridade seria coletar dados externos, com autores e condições de captura conhecidos.


---

## 6. Uso pretendido e restrições

Responsável: Daniel Gil, com revisão do grupo.

O protótipo pode apoiar um estudante ou operador na sugestão de transcrição de um caractere isolado. No momento da previsão, deve existir uma imagem binária 20×16, já recortada, na mesma orientação e polaridade da base. O resultado deve ser revisado por uma pessoa; uma troca entre caracteres pode produzir um código ou registro incorreto.

Não há nível de confiabilidade operacional demonstrado. O requisito de aceitação deve ser definido conforme a aplicação e o custo de erro, e medido em dados externos representativos. A maior softmax não é garantia de acerto: o modelo não foi calibrado e não possui mecanismo validado para rejeitar entradas desconhecidas.

Não utilizar para leitura automática de placas ou documentos reais, letras minúsculas, palavras, imagens coloridas ou decisões que identifiquem pessoas e produzam sanções. Antes de qualquer aplicação, validar segmentação, orientação, ruído, mudança de distribuição, desempenho por classe, revisão humana e capacidade de abstenção.

### Referências e base didática

Stutz, Rafael. Descrição do Projeto; Modelo de Relatório; Aula 1 (neurônios e aprendizado); questões e exercícios Keras da aula 2 (separação e vazamento); Aula 3 (softmax e entropia cruzada, pp. PDF 50-64); Aula 4 (CNN e pooling, pp. PDF 129-140); Aula 5 (Dropout, p. PDF 49; aumentação e vazamento, pp. PDF 98-99). Materiais fornecidos pelo grupo.

- [TensorFlow Datasets - Binary Alpha Digits](https://www.tensorflow.org/datasets/catalog/binary_alpha_digits)
- [NYU - origem e arquivo de dados](https://cs.nyu.edu/home/people/in_memoriam/roweis/data.html)
- [Keras - EarlyStopping](https://keras.io/api/callbacks/early_stopping/)
Fontes consultadas em 19/10/2026. Os documentos de planejamento do Grupo 4 orientaram os responsáveis e o escopo. O enunciado e o modelo de relatório prevaleceram sobre diferenças nas sugestões preliminares.
