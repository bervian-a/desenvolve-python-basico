# 3 - Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True se o participante tiver entre 16 e 18 anos, já tiver jogado pelo menos 3 jogos e já ter vencido pelo menos 1 jogo, permitindo seu ingresso no clube. Sua expressão deve imprimir False caso contrário. Aqui está um exemplo de interação com seu código no terminal, com entradas de dados destacadas em laranja e as impressões de seu código em branco.

#entrada
idade = int (input ("Qual tua idade: "))
jogos = (input ("Tu já jogou pelo menos 3 jogos de tabuleiro? (digite 'True' para 'Sim' e 'False' para 'Não') "))
    ##jogos = bool (input ("Tu já jogou pelo menos 3 jogos de tabuleiro? (digite 'True' para 'Sim' e 'False' para 'Não') "))
    ##Não usa bool nesses casos? tentei usar e deu erro; tive que alterar o True no algoritmo jogostrue
venceu = int (input ("Tu já venceu quantos jogos? "))

#processamento
idade16_18 = (idade>=16 and idade<=18)
jogostrue = (jogos == 'True')
vencedor = (venceu >=1)

#saida
print (idade16_18)
print (jogostrue)
print (vencedor)
print (f"Apto para ingressar no clube de jogos de tabuleiro: {idade16_18 and jogostrue and vencedor}")