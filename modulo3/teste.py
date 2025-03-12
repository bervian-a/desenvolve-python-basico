# Entrada
vtotal = float (input ("valor total da compra: R$ "))

#processamento
if vtotal>=100:
    vfinal=vtotal*0.8
    desc=20
   
elif vtotal>=50 and vtotal<100:
    desc=10
    vfinal=vtotal*0.9
else:
    desc=0
    vfinal=vtotal

#saida
print(f"Valor total da compra: R$ {vtotal:,.02f}")
print(f"Desconto aplicado {desc} %")
print(f"Valor final com desconto: R$ {vfinal:,.02f}")