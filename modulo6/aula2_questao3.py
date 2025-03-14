import random
#num_elementos = random.randint (5, 20)

#CRIAR LISTAS ALEATORIAS
lista1 = random.sample (range(0, 51), 20)
lista2 = random.sample (range(0, 51), 20)

interesccao = []

for n in lista1:
   if n in lista2 and n not in interesccao:
    interesccao.append (n)

interesccao_ord = sorted (interesccao)
lista1_ord = sorted(lista1)
lista2_ord = (lista2)

print ("Lista 1: " , lista1)
print ("Lista 2: " , lista2)
print ("Lista Intersecção: " , interesccao)
print ("Lista 1 ordenada: " , lista1_ord)
print ("Lista 2 ordenada: " , lista2_ord)
print ("Lista intersecção ordenada: " , interesccao_ord)

for n in interesccao_ord:
  print (f"{n}: Lista 1: {lista1.count(n)}, Lista 2: {lista2.count(n)}")