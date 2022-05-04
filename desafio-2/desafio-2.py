# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:53:15 2022

@author: henrique buzzi
"""
## Entradas
x = 3 #Número de alunos mínimos presentes no horário da aula
tempoChegada = [-2,-1,0,1,2] #Vetor com os tempos de chegada de cada aluno

##Processamento
for chegada in tempoChegada: #Loop que passa por cada tempo de chegada
    if(chegada>=0): #Se o tempo de chegada for maior ou igual a zero, o aluno estava presente no horário de começar a aula
        x-=1 #Diminui em 1 o número de alunos necessários para garantir a Aula normal

if(x<=0): #Se o número de alunos necessários tiver sido atingido ou até superado
    print('Aula Normal') #Aula normal
else: #Se não atingiu o número necessário
    print('Aula Cancelada') #Aula cancelada