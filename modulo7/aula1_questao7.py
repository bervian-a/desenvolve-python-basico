#Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:

#Chave de criptografia: gere um valor n aleatório entre 1 e 10
#Substitua cada caracter c pelo caracter c + n. 
#Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)
#nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']



import random
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz", "Carlos"]

chave_aleatoria = random.randint(1,10)

def encrypt (c, chave_aleatoria, minchr=33,maxchr=126):
    chave_aleatoriac = c+chave_aleatoria
    return (chave_aleatoriac)

nomes_cript = (encrypt)