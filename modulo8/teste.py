## Implemente aqui sua solução

import string 

alfabeto = set(string.ascii_lowercase) #conjunto com todas as letras do alfabeto em minúsculas.

eh_panagrama = input ("digite uma frase para verificar se é panagrama: ")
letras_frase = set(c.lower() for c in eh_panagrama if c.isalpha()) #cria um conjunto contendo todas as letras da string frase.
    
if letras_frase == alfabeto:
    print (f"'{eh_panagrama}' é um panagrama")
else:
    print (f"'{eh_panagrama}' não é um panagrama")