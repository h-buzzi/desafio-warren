# Desafio 1 Warren Tech Academy

## Desafio:
Alguns números inteiros positivos n possuem uma propriedade na qual a soma de n + reverso(n) resultam em números ímpares. Por exemplo, 36 + 63 = 99 e 409 + 904 = 1313. Considere que n ou reverso(n) não podem começar com 0.

Existem 120 números reversíveis abaixo de 1000.

Construa um algoritmo que mostre na tela todos os números n onde a soma de n + reverso(n) resultem em números ímpares que estão abaixo de 1 milhão.

##Código:
O código possui como variável de entrada o Limiar do resultado especificado (neste caso o resultado precisa estar abaixo de 1milhão (10^6)).
O código começa então pelo número 11, para evitar os números e números reversos que começam com 0.

Ele verifica se o número já foi adicionado na lista, isto pois em número anteriores que passaram nos testes também se adicionava seu número reverso, que poderia ser um número a frente, e então, assim otimiza-se tempo por não ter que verificar este número novamente. (Ex: 12 e 21, quando testa-se o 12, já adiciona o 21 na lista, evitando que quando chegar em 21, tenha-se que testar novamente). Além disto, ele também verifica se o número termina em 0, pois números terminado em 0 tem resto 0 quando divididos por 10.

Caso ele não tenha sido testado ainda e não termina em 0 (o que faria seu reverso começar com 0, oque não é permitido), então pega-se o seu reverso e soma com o número original. Se este resultado apenas possuir números ímpares (ou seja, cada número individual do resultado é ímpar, Ex: 1313) e estar abaixo de 1 milhão (Limiar de entrada), então o número e seu reverso é adicionado na lista.

### Segunda versão
O enunciado não ficou tão claro, pois ele pede que apenas resultem em números ímpares, mas, se considerarmos apenas números ímpares, então a afirmação que existem 120 números reversíveis abaixo de 1000 é falsa, logo o enunciado leva ao engano. A afirmação dos 120 números reversíveis abaixo de 1000 é apenas para os números onde o resultado é composto APENAS por números ímpares, ou seja, 409+904=1313, podemos ver que o número 1313 é composto apenas por 1 e 3, que são número ímpares.

Então, dentro do código existe uma parte de código comentado, abaixo do código original, que é onde está a solução se desconsiderarmos que todos os números do resultado precisam ser ímpares, que seria a condição que satisfaz os 120 números de 1000, e apenas leva em consideração que o resultado precisa ser ímpar e abaixo de 1 milhão. Um exemplo de como as coisas mudam: Antes, o número 29+92 = 121 não era considerado número válido, porque por mais que fosse um número ímpar, ele possui o número 2 em sua composição, logo não satisfazendo a propriedade matemática. Se considerar o jeito que foi escrito no enunciado este número agora é válido, pois é um resultado ímpar abaixo de 1 milhão.
