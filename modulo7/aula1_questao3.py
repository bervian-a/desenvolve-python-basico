#Escreva um script que dado uma frase conta os espaços em branco.

#Digite a frase: Meu amor mora em Roma e me deu um ramo de flores
#Espaços em branco: 11

frase = input ("Digite a frase ")
espaços = 0

for e in range (len(frase)):
        if frase [e] in " ":
                espaços += 1

print ("espaços: ", espaços)