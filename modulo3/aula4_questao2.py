#Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. Escreva um programa em Python que solicita ao/
# usuário para inserir a avaliação de um filme em uma escala de 1 a 5. O programa deve imprimir uma mensagem correspondente à classificação do filme:


#entrada
classificacao = (input ("Digite um numero entre 1 a 5 para avaliação do filme (considerando 1 ruim e 5 excelente): "))

#processamento e saida 
# JEITO 1:
#print ("Ruim." if classificacao == "1" else 
#       (print ("Regular." if classificacao == "2" else
#               (print ("Bom!" if classificacao == "3" else (print ("Muito Bom!") if classificacao == "4" else
#                                                            (print ("Excelente!") if classificacao == "5" else "Nota Invalida")))))))

#processamento e saida
if classificacao == "1":
    print ("Ruim.")
else:
       if classificacao == "2":
           print ("Regular.")
       else:
               if classificacao == "3":
                    print ("Bom!")
               else:
                        if classificacao == "4":
                            print ("Muito Bom!")
                        else:
                                     if classificacao == "5":
                                        print ("Excelente!")
                                     else:
                                        print ("Nota Invalida")