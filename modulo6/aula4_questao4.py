## Reescreva o código a seguir para construir a lista aprovados usando compreensão de listas, ou seja, eliminando o laço de repetição.

alunos = ["Maria", "Jose", "Carla", "Sol"]

notas = [35, 50, 20, 80]

aprovados = [alunos[i] for i in range (len(alunos)) if notas [i] >=60]

print ("Lista aprovados: " , aprovados)