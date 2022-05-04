# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:44:35 2022

@author: henrique buzzi
"""
#### Entradas
limiar = 10**6      #Limite dos números ímpares que estão abaixo de 1 milhão, salvo como uma variável para facilmente testar com 1000 (10**3)
#### Processamento
num = 11            #Número inteiro positivo inicial, que irá ser acrescentado para testar os números seguintes
allNumbers = [];    #Pré-alocação do vetor dos números que satisfazem as condições

while (num < limiar-1):     #Enquanto o número estiver abaixo de 1 milhão -1 (isto porque o loop while checa antes de rodar, logo, se tirar o -1, ele checaria 999*10**3, a condição estaria OK, ele iria entrar, somar 1, e rodar com 10**6)
    num+=1                  #Acrescenta 1 ao número
    if(num%10 != 0 and num not in allNumbers):  #Se o número ainda não está na lista, e não possuir final 0 (que daria um número reverso iniciando com 0, o que não está permitido nas condições do desafio)
        reversedNum =int(str(num)[::-1])        #Pega seu número reverso (transforma em String, reverte a string, e passa pra int)    
        result = num + reversedNum              #Então, adiciona o número ao seu número reverso
        if(result < 10**6):                     #Se resultou em um número abaixo de 1 milhão
            par = False                         #Agora precisa conferir se o resultado é composto apenas por números ímpares (tal como 33,55,99), então cria-se uma variável que indicará se foi detectado algum número par em sua composição
            for individualNumber in str(result):        #Para cada número que compõe o resultado
                if(int(individualNumber)%2 ==0):        #Verifica-se se ele possui resto 0 se dividido por 2, indicando que é um número par
                    par = True                          #Se resto 0 então, existe pelo menos 1 número par que compõe os números do resultado
            if(not par):                                #Se ele não tem nenhum número par
                    allNumbers.append(num)              #Adiciona o número a lista
                    allNumbers.append(reversedNum)      #Adiciona também seu número reverso para otimização

print(allNumbers)       #Mostra na tela todos os números

############ Abaixo tem-se a outra versão do código, conforme explicado na README do GitHub.
############ Para rodar o código abaixo apenas remove o # do começo de cada linha, e mantenha a identação.
############ Se estiver usando a IDE Spyder, apenas selecione todas as linhas abaixo e pressione 'Ctrl+1'.
############ Recomenda-se também que comente todo o bloco de código que está acima (ou seja, a outra versão) Para otimizar o tempo. 
############ Pode-se utilizar do mesmo comando "Ctrl+1' para comentar todo código acima

# limiar = 10**6      #Limite dos números ímpares que estão abaixo de 1 milhão, salvo como uma variável para facilmente testar com 1000 (10**3)
# num = 11            #Número inteiro positivo inicial, que irá ser acrescentado para testar os números seguintes
# allNumbers = [];    #Pré-alocação do vetor dos números que satisfazem as condições
# while (num < limiar-1):     #Enquanto o número estiver abaixo de 1 milhão -1 (isto porque o loop while checa antes de rodar, logo, se tirar o -1, ele checaria 999*10**3, a condição estaria OK, ele iria entrar, somar 1, e rodar com 10**6)
#     num+=1                  #Acrescenta 1 ao número
#     if(num%10 != 0 and num not in allNumbers):      #Se o número ainda não está na lista, e não possuir final 0 (que daria um número reverso iniciando com 0, o que não está permitido nas condições do desafio)
#         reversedNum =int(str(num)[::-1])            #Pega seu número reverso (transforma em String, reverte a string, e passa pra int)    
#         result = num + reversedNum                  #Então, adiciona o número ao seu número reverso
#         if(result%2 != 0 and result < 10**6):       #Se o resultado for ímpar e abaixo de 1 milhão
#                 allNumbers.append(num)              #Adiciona o número a lista
#                 allNumbers.append(reversedNum)      #Adiciona o número reverso para otimizar
