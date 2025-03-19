#Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", 
# removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. 
# Ao final, imprima o conteúdo do arquivo "palavras.txt".

import sys, os, re

def processar_arquivo(arquivo_entrada, arquivo_saida):
    if not os.path.exists(arquivo_entrada):
        print(f"Erro: O arquivo {arquivo_entrada} não foi encontrado!")
        return
    
    with open(arquivo_entrada, 'r') as f:
        conteudo = f.read()
    palavras = re.findall(r'[a-zA-Z]+', conteudo)
    
    with open(arquivo_saida, 'w') as f:
        for palavra in palavras:
            f.write(palavra + '\n')
    
    with open(arquivo_saida, 'r') as f:
        print(f.read())

processar_arquivo ('frase.txt', 'palavras.txt')
