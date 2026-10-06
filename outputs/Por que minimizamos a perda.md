# Por que minimizamos a perda

## Resumo

Minimizamos a perda porque ela representa o erro da rede neural. Ao reduzir esse valor, buscamos fazer com que as previsões fiquem mais próximas das respostas corretas.

## Explicação detalhada

A [[Função de perda]] transforma o erro da rede em um número. Esse número cria um objetivo claro para o treinamento: encontrar pesos e vieses que produzam a menor perda possível.

Se a perda diminui, normalmente significa que a rede está melhorando suas previsões nos exemplos usados no treinamento. Um otimizador procura fazer isso em pequenas etapas, ajustando os parâmetros da rede.

Podemos imaginar uma paisagem em que a altura representa a perda. O treinamento tenta descer essa paisagem até chegar a uma região mais baixa. O **gradiente** indica a direção em que a perda aumenta mais rapidamente; por isso, o gradiente descendente segue a direção contrária.

Porém, não basta diminuir a perda apenas nos dados de treinamento. A rede também precisa funcionar bem com dados novos. Quando ela memoriza os exemplos de treinamento, mas apresenta resultados ruins em novos exemplos, ocorre o **sobreajuste**, também chamado de *overfitting*.

Por esse motivo, a perda costuma ser acompanhada tanto nos dados de treinamento quanto em um conjunto separado de validação. O objetivo real é reduzir o erro e, ao mesmo tempo, fazer a rede aprender padrões que possam ser usados em situações novas.
