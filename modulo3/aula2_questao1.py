#1 - Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar no bar, e False caso contrário.

idade1 = int (input ("Idade da Juliana: "))
idade2 = int (input ("Idade da Cris: "))

print (f"Podem entrar: {idade1 >17 and idade2 >17}")
