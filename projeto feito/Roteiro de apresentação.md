# Roteiro de apresentação - 15 minutos

Usar [[Apresentacao_Grupo4.pptx]]. As notas dos slides contêm explicações e fontes. As perguntas do professor são um período adicional.

| Integrante | Slides | Tempo | Foco |
| --- | --- | --- | --- |
| Bruno Groppo | 1 e 2 | 3 min | Problema, entrada/saída, baseline |
| Bruno Pimentel | 3 e 4 | 3 min | Dados, duplicatas, divisão |
| Reynato Junior | 5 e 6 | 3 min | Arquitetura, perda, treinamento |
| Wallace Jardim | 7 e 8 | 3 min | Comparação e curvas |
| Daniel Gil | 9 e 10 | 3 min | Teste, erros e restrições |

## Bruno Groppo

“Queremos reconhecer um único caractere, de 0 a 9 ou de A a Z, em uma imagem binária. A entrada tem 20 por 16 pixels; a saída escolhe uma entre 36 classes. Não estamos construindo um leitor completo de placas ou palavras.”

Explicar que uma CNN pode aprender traços e curvas. O baseline calcula a classe mais frequente no treino; o empate leva à classe 0. Na validação, prevê 0 para todas as imagens e acerta 6/217, ou 2,76%. Também há uma MLP de referência; superar o baseline constante sozinho seria evidência limitada.

## Bruno Pimentel

Apresentar as 1.404 imagens, 39 por classe, baixadas da NYU e conferidas por checksum. Mostrar alguns exemplos e explicar que pixels já estão em 0/1, portanto não foram divididos por 255.

“A auditoria revelou que as imagens de 0 e O são idênticas. Uma separação comum poderia colocar cópias no treino e no teste. Agrupamos pelo hash dos pixels e mantivemos cada grupo inteiro em um único conjunto.”

Divisão: 971 treino, 217 validação, 216 teste. A mudança em relação à proposta inicial preserva as duplicatas juntas. Não existe informação de escritor; essa independência não foi verificada.

## Reynato Junior

Explicar a CNN acompanhando as dimensões: 20×16×1, convolução e pooling até 5×4×32, Flatten de 640 valores, Dense de 64 e saída de 36. Convoluções aprendem padrões locais e pooling reduz dimensões sem aprender pesos.

Softmax representa a escolha de uma classe entre várias. Sparse categorical crossentropy usa rótulos inteiros. Adam usa taxa 0,001; batch 32. Até 80 épocas, com EarlyStopping em val_loss e paciência dez. A época vem da menor perda de validação; a configuração final, da maior acurácia de validação.

## Wallace Jardim

Ler a tabela de validação: 2,76% baseline, 71,43% MLP, 73,73% CNN inicial, 77,42% CNN Dropout. O Dropout trouxe oito acertos adicionais, ou 3,69 pontos percentuais, nessa execução.

Mostrar que a perda de treino continua caindo quando a validação estabiliza. Isso indica sobreajuste. O Dropout melhora a validação mas não elimina o problema. A CNN inicial restaurou a época 10; a CNN Dropout, a 29. Não afirmar que mais épocas sempre melhoram ou que o Dropout sempre funciona.

## Daniel Gil

“Após escolher pela validação, avaliamos somente o baseline e a CNN Dropout no teste. A CNN acertou 178/216, acurácia de 82,41% e macro-F1 de 0,817. O baseline acertou seis.”

Apresentar erros concretos: O→0 quatro vezes; S→5 duas vezes. O recall de O foi 1/6. Como existem pares idênticos 0/O, pelo menos seis erros no teste são inevitáveis para um classificador determinístico que usa só a imagem.

Concluir com o uso didático e a necessidade de revisão humana. O experimento não valida fotografias, placas ou documentos reais. Faltam dados externos, avaliação de estabilidade e capacidade de rejeitar entradas desconhecidas.

## Perguntas para ensaio

1. **Por que softmax e não sigmoid?** Há uma classe por registro entre 36 alternativas. Sigmoids independentes seriam apropriadas para múltiplos rótulos simultâneos.
2. **Por que sparse na perda?** O alvo é um índice inteiro; categorical_crossentropy normalmente usa one-hot.
3. **Qual a diferença entre época e batch?** Uma época percorre todo o treino; cada batch reúne exemplos para uma atualização dos pesos.
4. **Por que val_loss no EarlyStopping?** A perda de treino pode continuar caindo durante o sobreajuste. Validação ajuda a detectar piora fora do conjunto de ajuste.
5. **Por que a validação escolhe e o teste não?** Se o teste orientar ajustes, deixa de ser uma avaliação final independente das escolhas.
6. **Por que não dividir os pixels por 255?** Eles já valem 0 ou 1.
7. **Dropout apaga pesos?** Não. Desativa temporariamente saídas no treino e fica desativado na inferência.
8. **O que representa 82,41%?** A proporção de acertos nestas 216 imagens reservadas; não uma garantia de confiabilidade para uso real.
9. **O que significa macro-F1?** Média do F1 das classes, dando o mesmo peso a cada classe; zero foi atribuído a divisões indefinidas.
10. **Por que as duas CNNs têm o mesmo número de parâmetros?** Dropout não aprende pesos adicionais.
11. **Por que não juntar 0 e O?** Isso mudaria para uma tarefa de 35 classes. Mantivemos a tarefa escolhida e documentamos a ambiguidade.
12. **É seguro dizer que o Dropout é sempre melhor?** Não: uma seed e uma divisão não demonstram superioridade geral.
13. **O modelo reconhece uma placa inteira?** Não. Recebe um único caractere já preparado; segmentação e captura real não foram estudadas.
14. **Por que o teste ficou melhor que a validação?** Conjuntos pequenos variam; essa diferença não prova estabilidade nem erro no procedimento.
15. **O que vocês fariam depois?** Validar com novas fontes e escritores, comparar métodos simples e repetir a seleção em grupos sem reutilizar o teste para ajustes.

Antes de apresentar, cada integrante deve explicar uma parte de outro colega e localizar no notebook a evidência de cada conclusão.
