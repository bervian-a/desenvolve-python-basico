#Escreva um script que peça o nome e a idade de todos na fila de uma balada.
# Crie uma lista de tuplas com os pares ```(nome, idade)``` de cada um. 
# Em seguida crie e imprima duas tuplas apenas com os nomes, uma com os menores de idade que não poderão entrar, 
# e uma com os maiores de idade (```idade >= 18```). 

print ("Digite nome e idade, digite 0 para sair")
lista = []

while True:
  nome = (input ("Nome: "))
  if nome == '0' : break
  idade = int(input ("Idade: "))
  lista.append((nome , idade))

menores = []
maiores = []
for nome, idade in lista:
    if idade >= 18:
        maiores.append(nome)
    else:
        menores.append(nome)

# Criando as tuplas com os nomes
tupla_menores = tuple(menores)
tupla_maiores = tuple(maiores)

# Exibindo as tuplas
print("\nPessoas que não poderão entrar (menores de idade):", tupla_menores)
print("Pessoas que poderão entrar (maiores de idade):", tupla_maiores)

