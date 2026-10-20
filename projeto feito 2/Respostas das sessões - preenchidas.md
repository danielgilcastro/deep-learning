# Respostas das sessões — linguagem simples

Os números vêm do [[Projeto_Grupo4.ipynb|notebook do projeto]]. A ordem segue o [[../projeto/Modelo de Relatório.pdf|modelo de relatório]].

## 1. Objetivo da modelagem

**Problema:** reconhecer um algarismo ou uma letra maiúscula em uma imagem de um único caractere.

**Entrada e saída:** entra uma imagem de 20 × 16 pixels, com valores 0 ou 1. Sai a escolha de uma entre 36 classes.

**Por que uma rede?** Uma rede convolucional pode aprender traços e curvas nas imagens, como na [[../aula4/note.ipynb|aula 4]].

## 2. Dados utilizados

**Origem:** base pública Binary Alpha Digits, escolhida pela equipe no catálogo TensorFlow Datasets. O arquivo bruto veio do endereço público indicado para a base.

**Preparação:** usamos as 1.404 imagens e conferimos dimensões, classes e pixels. Encontramos imagens iguais com rótulos `0` e `O`.

**Divisão:** 971 imagens de treino, 217 de validação e 216 de teste. Imagens idênticas ficaram no mesmo conjunto.

## 3. Arquitetura e desempenho

**Rede:** duas etapas de convolução e redução, depois uma camada densa e uma saída com 36 valores. A segunda versão acrescenta Dropout.

**Treino:** lotes de 32 imagens, até 80 épocas e parada antecipada pela perda de validação.

**Medida principal:** acurácia, a porcentagem de acertos.

**Resultados:** na validação, a referência simples teve 2,76%, a rede inicial 73,73% e a rede com Dropout 77,42%. Esta foi escolhida. No teste, ela teve 82,41%, ou 178 acertos em 216 imagens.

## 4. Análise do treinamento

**Curvas:** a perda de treino caiu. A perda de validação parou de melhorar antes do fim, sinal de sobreajuste.

**Tentativa de melhoria:** adicionamos Dropout. Na validação, foram oito acertos a mais nesta execução. Isso não garante o mesmo resultado em outras execuções.

## 5. Limitações

**Erros:** foram 38 no teste. Quatro imagens `O` foram previstas como `0`. Duas imagens `S` foram previstas como `5`.

**Dificuldade dos dados:** algumas imagens têm pixels idênticos, mas rótulos `0` e `O`. Há só seis imagens por classe no teste.

## 6. Uso pretendido e restrições

**Uso possível:** demonstração ou sugestão de transcrição de um caractere isolado, com conferência por uma pessoa.

**Onde não foi testado:** palavras, fotos, placas, documentos e outros tipos de imagem. O resultado atual não comprova desempenho nessas situações.
