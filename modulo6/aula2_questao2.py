import random
elementos = []
num_elementos = random.randint (5, 20)

for n in range (num_elementos):
    n = random.randint (0, 10)
    elementos.append (n)
print ("Lista elementos: " , elementos)

soma = 0
for i in range (num_elementos):
    soma += elementos[i]
print ("Soma da lista: " , soma)

print ("Media da lista: " , (soma/num_elementos))
