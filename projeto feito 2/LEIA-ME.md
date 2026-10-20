# Projeto do Grupo 4 — versão em linguagem simples

Esta pasta é uma revisão de `projeto feito`. A ordem da apresentação e as seis seções do relatório foram mantidas. As explicações usam somente os temas apresentados no enunciado, nos arquivos em PDF (formato portátil de documento) e nos notebooks das aulas. Os **números** vêm da execução do [[Projeto_Grupo4.ipynb|notebook deste projeto]], não são resultados das aulas.

## Arquivos para ler ou entregar

| Arquivo | Conteúdo |
| --- | --- |
| [[Relatorio_Grupo4.md]] | Relatório editável, com as seis seções exigidas. |
| [[Relatorio_Grupo4.pdf]] | Mesmo relatório em PDF (formato portátil de documento). |
| [[Projeto_Grupo4.ipynb]] | Código, resultados e figuras da execução. |
| [[Apresentacao_Grupo4.pptx]] | Dez slides, na ordem da versão anterior. |
| [[Apresentacao_Grupo4.pdf]] | Slides para leitura. |
| [[Roteiro de apresentação.md]] | Falas simples para os cinco participantes. |
| [[Respostas das sessões - preenchidas.md]] | Respostas curtas às perguntas do grupo. |
| [[Mapa das exigências.md]] | Onde cada exigência e conceito das aulas aparece. |

## Resultado principal

Comparamos os modelos usando as 217 imagens de **validação**. A rede convolucional com Dropout acertou 168, ou **77,42%**. Depois de escolhê-la, usamos as 216 imagens de **teste**: ela acertou 178, ou **82,41%**.

Há uma limitação importante: as mesmas imagens aparecem com os rótulos `0` e `O`. Além disso, a rede não foi avaliada em fotografias, placas ou documentos reais. Consulte o relatório antes de apresentar o resultado.

## Antes da entrega

- [ ] Confirmar com o professor o uso da base Binary Alpha Digits, que não está na lista sugerida do enunciado.
- [ ] Confirmar a composição do grupo: o enunciado diz quatro pessoas, e o material do grupo lista cinco.
- [ ] Executar o notebook em uma sessão limpa do Google Colab e conferir as saídas.
- [ ] Se a nova execução mudar os números, atualizar relatório e slides com os resultados da mesma execução.
- [ ] Ensaiar para caber em até 15 minutos.

Os arquivos `experimento.py`, `executar_notebook.py`, `dados` e `resultados` foram preservados para reproduzir ou conferir a execução. O código usa alguns recursos para verificar a integridade dos dados e guardar resultados; a explicação didática se concentra nos conceitos apresentados nas aulas.
