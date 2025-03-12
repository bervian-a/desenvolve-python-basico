#entrada
n_respostas = int (input("número de respostas: "))

soma = 0
cont = 0

#processamento e entrada
while cont <n_respostas:
    idade = int(input("idade: "))
    soma += idade
    cont += 1

#saida
print (f"A idade média dos {n_respostas} respondentes é de {int (soma/n_respostas): .0f} anos")
