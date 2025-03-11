#Você está desenvolvendo um programa para verificar se um ano é bissexto. Escreva um código em Python que solicita ao usuário para inserir um ano e imprime "Bissexto" se o ano for (1) divisível por 4 e não for divisível por 100, ou (2) se for divisível por 400. Caso contrário, imprima "Não Bissexto". 
#Teste seu código com os valores: 1900 (não bissexto), 2000 (bissexto), 2016 (bissexto) e 2017 (não bissexto). 

#entrada
ano = int (input ("digite um ano: "))

#processamento - regras para ano ser bissexto
r1 = ano%4==0
r2 = ano%100 != 0
r3 = ano%400==0

#saida
if r1 and r2:
     print("é bissexto")
else:
    if r3:
        print("é bissexto")
    else:
        print("não é bissexto")