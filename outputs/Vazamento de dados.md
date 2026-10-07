# Vazamento de dados

## Resumo

Em *machine learning*, **vazamento de dados** acontece quando o modelo recebe, durante o treinamento, uma informação que não estaria disponível no momento de fazer uma previsão real. Isso pode produzir resultados muito bons na validação ou no teste, mas que não se repetem quando o modelo é usado com dados novos.

## Explicação detalhada

Nesta matéria, vazamento de dados não significa o roubo ou a exposição de informações pessoais. O termo se refere ao **vazamento de informação** entre etapas do desenvolvimento de um modelo.

Um exemplo ocorre quando queremos prever, no momento de uma chamada, se será necessário enviar uma segunda viatura. Se usamos como entrada o número de policiais que chegaram ao local, estamos entregando ao modelo uma informação que só existe depois da decisão. A rede pode parecer muito precisa, mas essa precisão não representa o uso real.

Também pode ocorrer vazamento quando informações do conjunto de teste influenciam a preparação do treino. Por exemplo, esta ordem está errada:

```python
X_padronizado = padronizador.fit_transform(X)
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X_padronizado, y, test_size=0.3
)
```

O padronizador calculou a média e o desvio usando todos os dados, inclusive os que depois foram colocados no teste. Assim, uma pequena informação do teste chegou ao treinamento.

A ordem correta é separar os conjuntos primeiro e ajustar o padronizador somente no treino:

```python
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.3, random_state=42
)

padronizador.fit(X_treino)
X_treino = padronizador.transform(X_treino)
X_teste = padronizador.transform(X_teste)
```

Outro caso acontece quando registros da mesma pessoa aparecem no treino e no teste. A rede pode reconhecer características daquela pessoa em vez de aprender um padrão que funcione para pessoas novas. Nesse cenário, todos os registros de uma pessoa devem permanecer no mesmo conjunto.

Para evitar vazamento:

- use apenas informações disponíveis no momento real da previsão;
- separe treino, validação e teste antes de calcular transformações nos dados;
- ajuste padronizadores e outras etapas de preparação somente com o treino;
- mantenha pessoas, pacientes ou outros grupos inteiros no mesmo conjunto quando necessário;
- preserve a ordem do tempo em problemas que usam dados históricos para prever o futuro.

O vazamento é diferente de [[Aprendizado por atalho]]. No vazamento, chega ao modelo uma informação que ele não deveria receber. No aprendizado por atalho, a informação pode estar disponível, mas a rede aprende uma pista acidental em vez do padrão desejado.
