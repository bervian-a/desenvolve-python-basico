
#entrada/ leitura de dados
p1item  = (input ("Digite o nome do produto 1: "))
p1preco = int (input ("Digite o preço unitário do produto: 1"))
p1quant = int (input ("Digite a quantidade do produto 1: "))
p2item  = (input ("Digite o nome do produto 2: "))
p2preco = int (input ("Digite o preço unitário do produto 2: "))
p2quant = int (input ("Digite a quantidade do produto 2: "))
p3item  = (input ("Digite o nome do produto 3: "))
p3preco = int (input ("Digite o preço unitário do produto 3: "))
p3quant = int (input ("Digite a quantidade do produto 3: "))

#processamento
totalp1 = p1preco*p1quant
totalp2= p2preco*p2quant
totalp3 = p3preco*p3quant
precototal = int (totalp1+totalp2+totalp3)

#saida
print (f"Total: R$  {precototal:,.2f}")

#saida extra :)
print (f"Detalhes da compra:Quant | Item | R$ Un | R$ Total {p1item , p1quant , p1preco , totalp1} , {p2item , p2quant , p2preco , totalp2} , {p3item , p3quant , p3preco , totalp3}")