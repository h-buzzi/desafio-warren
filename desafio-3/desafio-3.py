# -*- coding: utf-8 -*-
"""
Created on Mon May  2 18:08:39 2022

@author: henrique buzzi
"""
def criarCaminho(initial):
    for j in range(initial,len(V)): #Percorre os caminhos disponíveis, a partir do caminho inicial
        caminho.append(V[j]) #Adiciona o caminho ao total percorrido
        if(sum(caminho)==N): #Se o total percorrido é igual ao alvo
            listaCaminhos.append(caminho.copy()) #Adiciona o caminho percorrido atual na lista de caminhos possíveis
        elif(sum(caminho)<N): #Se o total percorrido ainda está abaixo da distância alvo
            criarCaminho(j)   #Continua percorre os caminhos novamente a partir do caminho atual
        caminho.pop()         #Caso o caminho não seja válido (Total > N), ou ele já tenha concluído o caminho e está retornando, retira 1 passo do caminho atual
    return                    #Retorna pro nodo anterior

def mostrarMenoresSomas():
    minCaminhoSize = len(min(listaCaminhos,key=len)) #Calcula qual o menor tamanho das somas possíveis
    print(N)    #Printa o valor alvo
    for c in listaCaminhos:             #Para cada caminho na lista de caminhos
        if (len(c) == minCaminhoSize):  #Se ele tiver o mesmo tamanho que o menor tamanho
            c.sort()                    #Coloca os valores da combinação atual em ordem crescente
            print(c)                    #Mostra o vetor atual da combinação

#### Entradas
N = 10          #Número N alvo
V = [2, 3, 4]   #Vetor de números

#### Processamento
V.sort(reverse = True)  #Coloca o vetor de números em ordem decrescente
listaCaminhos = []      #Pré-alocação da lista com todos os caminhos
caminho = []            #Pré-alocação do caminho atual sendo percorrido
criarCaminho(0)         #Chama a função de caminho começando pelo primeiro caminho (4)
#### Printagem
mostrarMenoresSomas()   #Mostra as menores somas

        


