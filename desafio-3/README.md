# Desafio 3 Warren Tech Academy

## Desafio
Dado um vetor de números e um número n. Determine a soma com o menor número de elementos entre os números do vetor mais próxima de n e também mostre os elementos que compõem a soma. Para criar a soma, utilize qualquer elemento do vetor uma ou mais vezes.

Entrada de dados:
N = 10
V = [2, 3, 4]

## Código
A solução para este desafio não é tão simples de explicar, pois por mais que o código seja simples e limpo, ele necessita de um conhecimento prévio do conceito de grafos e seus caminhos. Para isto, assista a explicação em vídeo que eu produzi, nela eu mostro visualmente o que está acontecendo no código para aqueles que não conhecem grafos e seus caminhos. Link para o vídeo: https://youtu.be/Bem8neALPC4

## Explicação
Mas, a ideia é simples, eu começo somando sempre o maior número possível e verifico se ele deu maior, igual ou menor que o valor alvo. Se ele deu maior, eu retorno para a etapa anterior da soma e testo com o próximo valor disponível das combinações, em ordem decrescente, e faço a verficação novamente. Exemplo: 4+4+4 = 12, deu maior, então eu volto para 4+4 e tento com 3, que é próximo valor em ordem decrescente disponível, fazendo a soma ficar 4+4+3 = 11, e assim por diante.

Se ele deu igual, eu salvo esta combinação como válida e retorno para a soma anterior e continuando testando com o resto dos número disponíveis. Exemplo: Quando eu chegar na combinação 4+3+3 = 10, eu salvo está combinação como uma combinação válida, e então volto para o 4+3 e continuo agora com o 2, ficando 4+3+2=9.

Quando o valor der menor, significa que devo continuar somando o número atual. Exemplo: 0 + 4 = 4, então é menor que 10, logo continuo somando 4, 4+4=8, é menor, soma 4, 4+4+4 = 12, é maior, eu cancelo e volto, estou de novo em 4+4, agora eu pego o próximo da lista, 4+4+3 = 11, e assim por diante. Sempre que a soma estiver menor que o alvo, eu tento com o próximo número disponível que ainda não falhou.

Sempre que ele encontrar uma solução, ficar acima do limite, ou esgotar os números para a combinação atual, ele retorna para etapa anterior da soma.
