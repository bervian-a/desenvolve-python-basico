#Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string.
# Dica: letra in "aeiou". Exemplo:

frase = input ("Digite uma frase: ")
#Meu amor mora em Roma e me deu um ramo de flores
#19 vogais
# Índices [1, 2, 4, 6, 10, 12, 14, 18, 20, 22, 25, 28, 29, 31, 35, 37, 40, 44, 46]

vogais = 0
indice = []
for i in range (len(frase)):
        if frase [i].lower() in "aeiou":
                vogais += 1
                indice.append (i)

print ('Indices: ', indice)
print ("Vogais: ", vogais)