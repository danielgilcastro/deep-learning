# Exemplos de gráficos em Markdown

Esta nota serve para testar a visualização de gráficos e diagramas no Obsidian. Abra-a no modo de leitura ou na visualização ao vivo para ver os blocos Mermaid renderizados.

## Exemplo 1 — divisão dos dados

Os valores abaixo são apenas ilustrativos.

```mermaid
pie showData
    title Divisão dos dados
    "Treino (70%)" : 70
    "Validação (15%)" : 15
    "Teste (15%)" : 15
```

## Exemplo 2 — fluxo de desenvolvimento

```mermaid
flowchart LR
    A[Dados] --> B[Treino]
    B --> C[Validação]
    C --> D{Resultado satisfatório?}
    D -- Não --> E[Ajustar o modelo]
    E --> B
    D -- Sim --> F[Teste final]
```

## Exemplo 3 — tabela de resultados

Tabelas também funcionam diretamente em Markdown:

| Etapa     | Exemplos | Acurácia ilustrativa |
| --------- | -------: | -------------------: |
| Treino    |      700 |                  92% |
| Validação |      150 |                  87% |
| Teste     |      150 |                  85% |

**Acurácia** é a proporção de previsões corretas. Os números desta tabela são fictícios.
