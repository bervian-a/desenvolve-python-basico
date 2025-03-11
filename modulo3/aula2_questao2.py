# 2 - Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.

#entrada
idade1 = int (input ("Idade da Juliana: "))
idade2 = int (input ("Idade da Cris: "))

#processamento e saida
print (f"Podem entrar: {idade1 >17 or idade2 >17}")