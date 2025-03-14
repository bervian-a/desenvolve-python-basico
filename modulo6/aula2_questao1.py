import random

lista_aleatória = random.sample (range(-100, 101), 20)
lista_ordenada = sorted (lista_aleatória)


print ("Lista ordenada: " , lista_ordenada)
print ("Lista original: " , lista_aleatória)
print ("índice do maior valor da lista: ", lista_aleatória.index (max(lista_aleatória)))
print ("índice do menor valor da lista: " , lista_aleatória.index (min(lista_aleatória)))