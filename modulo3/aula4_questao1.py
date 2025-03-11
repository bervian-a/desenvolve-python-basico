#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar. Critério: se o resto da divisão do número por 2 for 0, o número é /
# par, caso contrário é ímpar. Lembre-se do operador do python % que retorna o resto de uma divisão.

#entrada
n1 = int (input ("digite um numero: "))
n2 = int (input ("digite outro numero: "))

#processamento
soma = n1+n2

#saida
if soma % 2 == 0:
    print ("Par")
else:
    print("Ímpar")
