# Desafio 2 Warren Tech Academy

## Desafio
Um professor de programação, frustrado com a falta de disciplina de seus alunos, decidi cancelar a aula se menos de x alunos estiverem presentes quando a aula for iniciada. O tempo de chegada varia entre:

* Normal: tempoChegada <= 0
* Atraso: tempoChegada > 0

Construa um algoritmo que dado o tempo de chegada de cada aluno e o limite x de alunos presentes, determina se a classe vai ser cancelada ou não ("Aula cancelada” ou “Aula normal”).

## Código
O desafio é bem simples. Primeiro se fornece as 2 entradas, que seria a quantidade de alunos presentes mínimas para a aula ocorrer, e em segundo cada tempo de chegada de cada aluno. Então, percorre cada um dos tempos de chegada do vetor de alunos. Para cada tempo maior ou igual a 0, significa que o aluno estava presente no horário de início da aula, então, decrescenta 1 do número de alunos necessários para aula normal.
Caso o número de alunos necessários esteja em 0 ou abaixo, significa que tem-se alunos o suficiente.
