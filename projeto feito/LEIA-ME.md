# Projeto feito - Grupo 4

## É possível fazer o projeto com os materiais fornecidos?

Sim. As respostas das sessões definem a tarefa e o dataset; os PDFs do professor definem as entregas e os critérios; as aulas 1 a 5 fundamentam a implementação. As perguntas ainda vazias exigiam decisões metodológicas e experimentos. Essas etapas foram implementadas e executadas, com resultados reais salvos nesta pasta.

**Estado em 19/10/2026:** notebook executado localmente, redes treinadas, avaliação final realizada e relatório preenchido. O pacote ainda depende da revisão do grupo e da execução de conferência no Google Colab antes da entrega acadêmica.

## Comece por estes arquivos

| Arquivo | Finalidade |
| --- | --- |
| [[Relatorio_Grupo4.pdf]] | Relatório com as seis seções exigidas, responsáveis, resultados e gráficos. |
| [[Relatorio_Grupo4.md]] | Versão editável no Obsidian. |
| [[Projeto_Grupo4.ipynb]] | Notebook independente, com código completo e saídas da execução local. |
| [[Apresentacao_Grupo4.pptx]] | Slides editáveis, com dados, gráficos e notas para os apresentadores. |
| [[Apresentacao_Grupo4.pdf]] | Cópia dos dez slides para leitura e projeção, sem notas do apresentador. |
| [[Roteiro de apresentação.md]] | Cinco participações de três minutos e preparação para perguntas. |
| [[Respostas das sessões - preenchidas.md]] | Respostas consolidadas às perguntas que estavam em aberto. |
| [[Mapa das exigências.md]] | Correspondência entre o enunciado, as aulas e os arquivos produzidos. |

Os materiais originais em `projeto` e `aula1` a `aula5` foram preservados.

## Resultado desta execução

| Modelo | Acurácia na validação |
| --- | --- |
| Baseline constante | 2,76% |
| MLP de referência | 71,43% |
| CNN inicial | 73,73% |
| CNN com Dropout | 77,42% |

Escolhida exclusivamente pela validação, a CNN com Dropout alcançou **82,41% de acurácia no teste** (178/216) e **macro-F1 de 0,817**. O baseline de teste alcançou 2,78%. Não foram avaliadas no teste as redes não escolhidas.

O ganho do Dropout refere-se a uma única execução. Não demonstra superioridade geral sobre outras arquiteturas ou métodos de Machine Learning.

## Descoberta importante nos dados

O arquivo tem 1.404 registros, mas somente 1.363 imagens distintas. Todas as 39 imagens de `0` também aparecem como `O`. Há 38 grupos com rótulos conflitantes e outro grupo de repetição na classe `7`.

A divisão mantém todas as imagens idênticas no mesmo conjunto, inclusive quando têm rótulos diferentes. Assim, o estudo usa **971 imagens de treino, 217 de validação e 216 de teste**, preservando as 36 classes e impedindo vazamento de cópias exatas. O agrupamento por pixels não garante independência por escritor: esses identificadores não estão disponíveis.

Manter 36 classes preserva a tarefa que vocês escolheram e permite discutir um limite real dos dados. Unificar `0/O` ou excluir classes mudaria a pergunta do projeto e exigiria um novo experimento; isso não foi feito.

## Como conferir no Google Colab

1. Abra [Google Colab](https://colab.research.google.com/) e envie `Projeto_Grupo4.ipynb` por **Arquivo > Fazer upload de notebook**.
2. Use uma sessão nova. CPU é suficiente para esta base; GPU é opcional.
3. Execute a célula de instalação e depois todas as células na ordem. A instalação pode levar alguns minutos.
4. O notebook baixa o MAT público da NYU e confere seu SHA-256. Não precisa enviar arquivos locais.
5. Confira que as asserções de rótulos, dimensões e separação passam e que todas as células terminam sem erro.
6. Leia a matriz e as curvas; confira as versões em `resultados/ambiente.json`.
7. Salve o notebook com as saídas e baixe a pasta `resultados` se quiser preservar essa execução.

Não executei uma sessão remota no Colab: o notebook entregue foi executado célula a célula em Python local. A célula `%pip` ficou sem execução registrada, pois as bibliotecas já existiam no computador. As figuras e métricas registradas são saídas reais das demais células.

Resultados podem variar conforme TensorFlow, Keras, CPU/GPU e operações numéricas. **Se o Colab gerar valores diferentes, atualize relatório e apresentação para a mesma execução entregue. Não ajuste as configurações com base no resultado do teste.** A comparação já foi encerrada antes da inspeção do teste.

## Reprodução local

No terminal, entre nesta pasta e execute:

```powershell
python -m pip install -r requirements.txt
python experimento.py
```

Para recriar o notebook com saídas, use `python executar_notebook.py`. Esse executor requer também `ipython`. Ele captura as saídas sequenciais em Python, sem depender de um servidor Jupyter.

`gerar_relatorio.py` usa `reportlab` e `Pillow`, além das fontes Arial do Windows. Execute-o depois dos experimentos para gerar o PDF e o Markdown. Os resultados numéricos principais são lidos dos JSONs, mas a análise textual se refere à execução entregue e deve ser revisada se o treinamento mudar. A geração dos slides também contém conclusões específicas desta execução.

`gerar_apresentacao.mjs` usa o runtime de artefatos do Codex disponível neste computador; o PPTX final é independente desse runtime. Os caminhos absolutos desse gerador não são utilizados no notebook do Colab.

## Evidências técnicas

- `dados/binaryalphadigs.mat`: arquivo da fonte pública, com checksum verificado.
- `resultados/auditoria.json` e `duplicatas.json`: integridade e grupos repetidos.
- `resultados/divisao.json`: índices exatos de cada conjunto.
- `resultados/contagens.json`: contagens por classe e por conjunto.
- `resultados/historicos.json`, `execucoes.json` e `execucao.log`: registro do treinamento.
- `resultados/validacao.json` e `selecao.json`: comparação e escolha antes do teste.
- `resultados/teste.json`, `metricas_por_classe.json` e `matriz_confusao.csv`: avaliação final.
- `resultados/previsoes_teste.npz`: IDs, classes reais, previsões e softmax do teste.
- `resultados/modelo_final.keras` e `classes.json`: modelo selecionado e ordem das classes.
- `resultados/ambiente.json` e `configuracao.json`: versões, dispositivos e hiperparâmetros.

## O que o grupo ainda precisa conferir

- [ ] Confirmar aprovação do Binary Alpha Digits, pois ele não consta na lista sugerida do enunciado.
- [ ] Confirmar autorização para cinco integrantes; o enunciado menciona quatro.
- [ ] Confirmar as datas definitivas. O documento informa entrega em 21/10 às 23h59 e apresentação em 22/10, sujeitas à confirmação do professor.
- [ ] Executar o notebook em uma sessão limpa do Colab e salvar as saídas.
- [ ] Revisar os responsáveis e garantir que todos expliquem o trabalho completo.
- [ ] Ensaiar a apresentação com limite de 15 minutos.

## Fonte do download

[Catálogo TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/binary_alpha_digits) e [página preservada da NYU](https://cs.nyu.edu/home/people/in_memoriam/roweis/data.html).

O endereço antigo retornou HTTP 403; o novo endereço da própria NYU forneceu o arquivo com o checksum oficial:

```text
3ee9392e64e4e3bb7b35502b69bf2555a0b4197c1b31048c4189b84bc0bc6ea7
```
