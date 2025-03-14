from itertools import zip_longest

lista1_quant = int(input("Quantos elementos na lista 1: "))
lista2_quant = int(input("Quantos elementos na lista 2: "))

lista1 = []
lista2 = []

for i in range (lista1_quant):
    el1 = int (input("elemento lista 1: "))
    lista1.append (el1)

for i in range (lista2_quant):
    el2 = int (input("elemento lista 2: "))
    lista2.append (el2)

intercalada = []
for a, b in zip_longest (lista1, lista2, fillvalue=None):
    if a is not None:
        intercalada.append (a)
    if b is not None:
        intercalada.append (b)

print ("Lista 1: " , lista1)
print ("Lista 2: " , lista2)
print ("Lista Intersecção: " , intercalada)

