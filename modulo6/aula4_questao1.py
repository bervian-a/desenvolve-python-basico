## Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
lista_pares = list(range(19,51))
print ("Lista 20-50 pares: " ,  sorted({n for n in lista_pares if n%2==0}))

##Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]
lista_quadrados = [1,2,3,4,5,6,7,8,9]
print ("Lista quadrados: " ,  sorted({n**2 for n in lista_quadrados}))

## Todos os números entre 1 e 100 que sejam divisíveis por 7
lista_div7 = list(range(1,100))
print ("Lista 1-100 divisiveis por 7: " ,  sorted({n for n in lista_div7 if n%7==0}))

##Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex:['par', 'impar',… , 'impar'])
lista_parimpar = list(range(0,30,3))
print ("Lista original: " , lista_parimpar)
print ("Lista par ou impar: " ,  sorted({'par'if n%2==0 else 'impar' for n in lista_parimpar}))