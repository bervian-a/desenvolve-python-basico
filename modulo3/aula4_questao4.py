#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:

##TENTATIVA E ERRO
#if  peso>10:
#     print ("Valor do frete é de R$: " )
#
#(f"Tu já podes te aposentar: {a or b or c}")
#if distancia == d1:
#        print (f"Valor do frete é de R$: {}" , peso*1)
#else:
#    if distancia == d2:
#        print ("Valor do frete é de R$:" , peso*1.5)
#    else:
#        if distancia == d3:
#            print ("Valor do frete é de R$:" , peso*2)
#        else:
#            print ("")##

#### CORRETO::::


#entrada
distancia = int (input ("digite a distancia da entrega (em km): "))
peso = int (input ("digite o peso total do produto, em quilogramas: "))

#processamento - condiciando à distancia
if distancia<=100:
     taxa_distancia = 1
elif distancia>100 and distancia<=300:
     taxa_distancia = 1.5
elif distancia>300:
     taxa_distancia = 2
else:
     print ("dados incorretos")

#processamento - Segunda parte do calculo, de acordo com o peso maior ou nao que 10kg:

if peso<10:
    valor_do_frete = peso*taxa_distancia
else:
    valor_do_frete = (peso*taxa_distancia)+10

#saida
print(f"Valor do frerte R$: {valor_do_frete}")
