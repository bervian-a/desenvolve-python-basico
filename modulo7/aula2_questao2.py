#Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".


def substituir_vogais():
    frase = input("Digite uma frase: ")
    
    # Definindo as vogais a serem substituídas
    vogais = "aeiouAEIOU"
    
    # Substituindo as vogais por '*'
    nova_frase = ''.join(['*' if char in vogais else char for char in frase])
    
    print("Frase alterada:", nova_frase)


substituir_vogais()


