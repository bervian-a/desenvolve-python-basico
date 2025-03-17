#Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente.
# Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. 
# Adicione o separador "-" na sua impressão.

#Digite o numero: 97651234
#Número completo: 99765-1234

def numero_completo (celular):
    
    # Verifica se o número tem 8 ou 9 dígitos
    if len(celular) == 8:
        celular = "9" + celular  # Adiciona o 9 na frente se tiver 8 dígitos
    
    elif len(celular) == 9:
        if celular[0] != "9":
            print("Número inválido, o primeiro dígito deve ser 9.")
            return
        
    else:
        print ("Número inválido! O número deve ter 8 ou 9 dígitos.")
        return
    
    numero_completo = celular[:5] + "-" + celular[5:] # Adiciona o separador "-"
    print(f"Número completo: {numero_completo}")

# Chama a função
celular = input ("Digite o número do seu celular: ")
numero_completo (celular)