#entrada
quantia = int (input ('Digite o valor R$: '))

#processamento
nota100 = quantia // 100
quantia = quantia % 100
nota50 = quantia // 50
quantia = quantia % 50
nota20 = quantia // 20
quantia = quantia % 20
nota10 = quantia // 10
quantia = quantia % 10
nota5 = quantia // 5
quantia = quantia % 5
nota2 = quantia // 2
quantia = quantia % 2
nota1 = quantia // 1

#saida
print (f"{nota100} nota(s) de R$ 100,00")
print (f"{nota50} nota(s) de R$ 50,00")
print (f"{nota20} nota(s) de R$ 20,00")
print (f"{nota10} nota(s) de R$ 10,00")
print (f"{nota5} nota(s) de R$ 5,00")
print (f"{nota2} nota(s) de R$ 2,00")
print (f"{nota1} moeda(s) de R$ 1,00")