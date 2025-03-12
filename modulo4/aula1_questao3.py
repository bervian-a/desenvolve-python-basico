#entrada
n1 = int (input("Digite um numero: "))
n2 = int (input("Digite um numero: "))
n3 = int (input("Digite um numero: "))

m= (n1+n2+n3)/3

#processamento e saida
if m>=60:
    print("Aprovado")
else:
    if m>=40:
        print("Recuperação")
    else:
        print("Reprovado")
print ("Fim")

