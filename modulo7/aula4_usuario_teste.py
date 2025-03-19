#programa principal
nome_arquivo = "usuario.txt"

#funçoes
def cadastro_usuario ():
    nome_usuario = input ("digite o nome")
    with open (nome_arquivo, 'a+') as fp:
        for linha in fp:
            if nome_usuario == linha [:-1]:
                print ("usuario ja cadastrado")
                return
        fp.write (nome_usuario+'\n')


def login_usuario ():
    nome_usuario = input ("digite o nome")
    with open (nome_arquivo, 'r') as fp:
        for linha in fp:
            if not nome_usuario == linha [:-1]:
                print ("usuario nao cadastrado")
                return
            else:
                fp = open (nome_arquivo, "r")
                fp.write (nome_usuario+'\n')
                fp.close ()
                print ('login realizado')




#programa principal
while True:
    print ('1-Cadatrar \n2-Login \n3- Sair')
    op=int(input("Escolha uma opção: "))
    if op ==1:
        cadastro_usuario()
    elif op ==2:
        login_usuario()
    
    elif op == 3: break
    else:
        print ("opçao invalida")
        print ('*'*15)

    
