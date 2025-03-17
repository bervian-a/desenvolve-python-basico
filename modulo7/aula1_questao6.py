#Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo.
# Anagramas são palavras com os mesmos caracteres rearranjados.

#Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
#Digite a palavra objetivo: amor
#Anagramas: ["amor", "mora", "ramo", "Roma"] 

frase = input ("Digite uma frase: ")
lista_palavras = (frase.lower()).split(" ")

palavra_padrão = sorted ("amor")

for palavra in lista_palavras:
    if sorted (palavra) == palavra_padrão:
        print (palavra)