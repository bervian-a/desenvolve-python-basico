#Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores), 
#os armazena em uma lista e, usando fatiamento de listas, imprima:

#A lista original

#Os 3 primeiros elementos
#Os 2 últimos elementos
#A lista invertida (do fim para o começo)
#Os elementos de índice par (0, 2, 4 … )
#Os elementos de índice ímpar (1, 3, 5, … )

print ("Digite no minimo 4 elementos, pressione 0 para finalizar a inserção: ")
lista = []
listapar = []
listaimpar = []

while True:
    el = int (input("elemento lista: "))
    if el == 0: break
    lista.append (el)
    if el%2 == 0:
        listapar.append (el)
    else: listaimpar.append (el)

print ("Lista original: " , lista)
print ("3 primeiros elementos: " , lista[0:3])
print ("2 ultimos elementos: " , lista[:-3:-1])
print ("Lista invertida: " , lista[::-1])
print ("Elementos pares: " , listapar)
print ("Elementos impares: " , listaimpar)
