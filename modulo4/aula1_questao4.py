#entrada
n = int (input("Digite um numero: "))

maior =  0

#processamento e saida
while n>0:
    x = int (input("digite x: "))
    while x > maior:
        maior = x
    n = n-1

#Saida False
print (maior)
