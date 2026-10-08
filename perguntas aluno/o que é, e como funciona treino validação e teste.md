# o que é, e como funciona treino validação e teste

## Resposta

**Treino, validação e teste** são três partes em que podemos dividir os dados para desenvolver e avaliar um modelo de machine learning. Cada parte tem uma função diferente:

1. **Treino:** o modelo vê exemplos e ajusta seus parâmetros, como os pesos de uma rede neural, para reduzir os erros.
2. **Validação:** usamos outros exemplos para acompanhar o desempenho durante o desenvolvimento e escolher ajustes, como a arquitetura do modelo ou por quanto tempo treiná-lo. O modelo não ajusta seus pesos diretamente com esses exemplos.
3. **Teste:** depois de terminar as escolhas, usamos exemplos reservados para medir como o modelo se sai em dados que não participaram do desenvolvimento.

Imagine que queremos identificar fotos de gatos e cachorros. Podemos separar as fotos em três grupos: o modelo **aprende** com o grupo de treino; usamos o grupo de validação para **escolher a versão** que funciona melhor; e, no final, usamos o grupo de teste para **avaliar essa versão**.

Essa separação ajuda a perceber se o modelo aprendeu padrões que funcionam em exemplos novos ou se apenas decorou os exemplos de treino. As proporções da divisão podem variar conforme o tamanho dos dados e o problema. Também é importante evitar que exemplos muito parecidos ou informações do teste apareçam no treino, pois isso faria o resultado parecer melhor do que realmente é.
