# Entrada: A primeira linha de entrada é um inteiro N com a quantidade de experimentos registrados. 
# As N linhas seguintes contém um inteiro Quantia que representa a quantidade de cobaias utilizadas e um caractere Tipo 
# ('S', 'R' ou 'C') com o tipo de cobaia (S:Sapo, R:Rato ou C:Coelho).

###########################

#entrada
n = int(input("numero de experimentos realizados: "))

cont = 0
s, r, c = 0, 0 ,0

#processamento e entrada
while cont< n:
    tipo = input(("tipo de cobaia (s: sapo; r: coelho; c: coelho): "))
    quantia = int (input("quantia de cobaias utilizadas: "))
    
    if tipo =='s':
        s += quantia
    elif tipo =='r':
        r += quantia
    elif tipo =='c':
        c += quantia
    else:
        print ("Erro, tipo {tipo} de cobaia nao cadastrada!") 

    cont +=1
    somat = s+r+c

#saida
print (f"Foram utilizados {s+r+c} de cobaias, destes: ")
print (f"{s}, {(s/(s+r+c))*100:.1f}% sapos, {r}, {(r/somat)*100:.1f}% ratos e {c} , {(c/somat)*100:.1f}% coelhos")