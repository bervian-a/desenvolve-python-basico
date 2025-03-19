#Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador com o nome "estomago.txt".
# Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
# 
# O texto das primeiras 25 linhas
# O número de linhas do arquivo
# A linha com maior número de caracteres
# O número de menções aos nomes dos personagens "Nonato" e "Íria" 
# (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).

import sys, os, re

def ler_arquivo(arquivo):
    if not os.path.exists(arquivo):
        print(f"Erro: O arquivo {arquivo} não foi encontrado!")
        return
    #print primeiras 25 linhas:
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    for i in range(min(25, len(linhas))):
        print(linhas[i].strip())

       #num de linhas count
    num_linhas = len(linhas)
    print(f"\nNúmero total de linhas: {num_linhas}")

    #Linha com maior n de caracteres
    linha_max = max(linhas, key=len)
    print(f"\nLinha com maior número de caracteres:\n{linha_max.strip()}")

    #Contagem das menções aos nomes "Nonato" e "Íria"
    cont_nonato = 0
    cont_iria = 0
    for linha in linhas:
            # Usando expressões regulares para evitar substrings indesejadas (como 'iria' em 'séria')
            cont_nonato += len(re.findall(r'\bNonato\b', linha, re.IGNORECASE))
            cont_iria += len(re.findall(r'\bÍria\b', linha, re.IGNORECASE))

    print(f"\nNúmero de menções a 'Nonato': {cont_nonato}")
    print(f"Número de menções a 'Íria': {cont_iria}")



ler_arquivo ('estomago.txt')