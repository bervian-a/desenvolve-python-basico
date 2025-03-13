import random
import math

n = int (input("quantos numeros deseja: "))
soma = 0

for i in range (n):
    soma = soma + random.randint (0,100)

raiz = math.sqrt (soma)

print (f"raiz de {n} numeros aleatórios é: {raiz:.5f}")