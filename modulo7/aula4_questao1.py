#Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script.
#Imprima em seguida o caminho completo do arquivo salvo.

#Digite uma frase: Bom dia, meu nome é Davi.

#Frase salva em /Users/laranjeira/python-basico/frase.txt
import os

frase = input ("Digite uma frase para ser salva: ")
nome_arquivo = 'frase.txt'

with open(nome_arquivo, "w") as arquivo:
    arquivo.write(frase)

caminho = os.path.abspath(nome_arquivo)

print (f"Arquivo salvo em: {caminho}")

