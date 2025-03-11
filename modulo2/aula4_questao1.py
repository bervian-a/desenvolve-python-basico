##exercicio 1
#Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado como mostra o exemplo a seguir:
#O terreno possui 250m2 e custa R$512,490.50
 
#Comente na linha acima de cada instrução uma breve descrição da instrução.
#Fórmulas:
#•	area_m2 = comprimento * largura
#•	preco_total = preco_m2 * area_m2

#Input e leitura de dados
comprim = int(input("Qual o comprimento?"))
largura = int(input("Qual a largura?"))
cmetro = float (input("Qual o preço do m²? R$"))

#processamento (calculo da area e valor)
area = comprim * largura
ctotal = area*cmetro

#saida de dados
print(f"O terreno possui {int(area)} m² e custa R$ {ctotal:,.2f}.")
