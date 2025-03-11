##4 - Uma conta poupança foi aberta com um depósito de R$500,00. Esta conta é remunerada em 1% de juros ao mês. O código a seguir apresenta uma forma de implementação para calcular três meses de acúmulo de juros. Reescreva esse código usando apenas duas variáveis.

juros = 1.01
saldo = 500.0
print("Saldo inicial é R$", (saldo))
saldo = saldo * juros
saldo = saldo * juros
saldo = saldo * juros
print("Após 3 meses meu novo saldo é R$", (saldo))
