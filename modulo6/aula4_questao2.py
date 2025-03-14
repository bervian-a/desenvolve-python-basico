## Solicite uma frase do usuário e usando compreensão de listas imprima:
frase = input ("Diga uma frase: ").lower()

print ("Frase:", frase)


print ("Lista vogais: " ,  ({c for c in frase if c in ['a', 'e', 'i', 'o', 'u']}))
print ("Lista de consoantes:", [c for c in frase if c.isalpha() and c not in ['a', 'e', 'i', 'o', 'u']])


