import random
import math


valor = int (random.randint (0,10))
print (valor)

while True:
    n = int (input("adivinhe o numero: "))
    if n == valor:
        print (f"Correto, o número é {valor}")
        break
    if n > valor:
        print (f"{n} é muito alto, tente novamente!")
        continue
    if n < valor:
        print (f"{n} é muito baixo, tente novamente!")
        continue
