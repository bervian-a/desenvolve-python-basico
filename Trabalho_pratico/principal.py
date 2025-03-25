import csv
from collections import namedtuple
from getpass import getpass

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

##################### INICIO FUNÇÕES INICIAIS BASE DE DADOS #####################
#Base de dados dos USUARIOS/ login
dados_usuarios  = [
    ['nome_usuario','senha','nome','telefone','permissao'],
['alinesouza','asg123','Aline Souza','(11)98765-4321','administrador'],
['joaosilva','jsc234','Joao Silva','(21)99876-5432','cliente'],
['mariaoliveira','moc234','Maria Oliveira','(31)91234-5678','cliente'],
['pedrosouza','psc234','Pedro Souza','(41)98765-1234','cliente'],
['anacosta','act234','Ana Costa','(51)96543-2109','profissional'],
['lucaspereira','lpt234','Lucas Pereira','(61)93456-7890','profissional'],
['beatrizalmeida','bat234','Beatriz Almeida','(71)96789-3456','profissional']
]
#with open("usuarios.csv", mode="w", newline="") as file: #criando a base de dados
#    writer = csv.writer(file, delimiter=',')
#    writer.writerows(dados_usuarios)
#########################################################

#Base de dados dos SERVICOS
dados_servicos  = [
    ['codigo','atividade','regiao','profissional','preco'],
['aq01','assistencia qualidade','MG sul', 'Ana Costa','R$ 2.000,00'],
['aq02','assistencia qualidade','RS noroeste','Lucas Pereira','R$ 2.000,00'],
['te01','treinamento equipe','MG sul','Ana Costa','R$ 1.000,00'],
['te02','treinamento equipe','RS noroeste','Lucas Pereira','R$ 1.000,00'],
['le01','limpeza de equipamento','MG sul','Ana Costa','R$ 2.500,00'],
['le02','limpeza de equipamento','RS noroeste','Lucas Pereira','R$ 2.500,00'],
['rp01','reproducao','MG centrooeste','Beatriz Almeida','R$ 5.000,00']
]

#with open("servicos.csv", mode="w", newline="") as file: #criando a base de dados serviços
#    writer = csv.writer(file, delimiter=',')
#    writer.writerows(dados_servicos)
#########################################################

#Base de dados dos AGENDAMENTOS
dados_agenda  = [
['Cliente','cod_serv','servico','tecnico','data'],
['Pedro Souza','rp01','reproducao','Beatriz Almeida','2025-03-29'],
['Maria Oliveira','le01','limpeza de equipamento','Ana Costa','2025-04-01'],
['Joao Silva','aq02','assistencia qualidade','Lucas Pereira','2025-03-28']
]
#with open("agenda.csv", mode="w", newline="") as file: #criando a base de dados agendamentos #administrador
#    writer = csv.writer(file, delimiter=',')
#    writer.writerows(dados_agenda)
########### APENAS PARA CRIAR NO START DO PROGRAMA ###################
##################### FIM DAS FUNÇÕES INICIAIS BASE DE DADOS #####################

###CONSTANTES###
## arquivos
ARQUIVO_USUARIOS = 'usuarios.csv'
ARQUIVO_SERVICOS = 'servicos.csv'
ARQUIVO_AGENDA = 'agenda.csv'
#usuario
USUARIO_LOGADO = None

##################### INICIO FUNÇÕES DE USUÁRIO #####################
##### CRUD Read
# Função para ler usuários do arquivo CSV.
# Parâmetro: arq_user_csv (str) - caminho do arquivo CSV. #Retorno: dict - dicionário com logins como chaves e tuplas; Login como valores.
def ler_usuarios(arq_user_csv):
    Usuario = namedtuple('Usuario', ['login','senha', 'nome','telefone','permissao'])
    usuarios = {}
    
    with open(arq_user_csv, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            nome_usuario,senha,nome,telefone,permissao = row
            usuarios[nome_usuario] = Usuario(login=nome_usuario,senha=senha,nome=nome,telefone=telefone,permissao=permissao)
    
    return usuarios #return será utilizado para demais funcoes com usuario

##### CRUD Read
# Função para realizar login de um usuário.
# Atualiza a variável global USUARIO_LOGADO em caso de login bem sucedido.
# Parâmetro: usuarios (dict) - dicionário de usuários. # Retorno: None
def fazer_login(usuarios):
    # preciso explicitar o acesso à variável global senão a atribuição ao final da função criará uma nova variável local
    global USUARIO_LOGADO

    console.print(Panel('🟢 [bold green]Login[/bold green] 🟢\n\nPor favor, insira suas credenciais.', 
                        expand=False, title="Tela de Login"))
    username = Prompt.ask("[bold cyan]Nome de Usuário: [/bold cyan]")
    senha = getpass("Senha: ")

    user = usuarios.get(username, None)
    if user is not None and user.senha == senha:
        console.print("\n[bold green]Login bem-sucedido![/bold green]")
        USUARIO_LOGADO = user #atualiza o usuario logado
    else:
        console.print(f"[bold red]Erro: usuário ou senha incorretos!", style="red")

##### CRUD Create
# Função para cadastrar um novo usuário.
# Parâmetros: 
#   usuarios (dict) - dicionário de usuários.
#   arq_user_csv (str) - caminho do arquivo CSV.
# Retorno: str - nome do novo usuário ou False em caso de falha.
def cadastrar_usuario(usuarios, arq_user_csv):
    console.print(Panel('''[bold green]Cadastro de Novo Usuário[/bold green]\nPor favor, insira os dados do novo usuário.''', 
                        title="Novo Usuário", expand=False))

    nome_usuario = Prompt.ask("[bold cyan]Login: [/bold cyan]")
    senha = getpass("Senha: ")
    nome = Prompt.ask("[bold cyan]Nome completo: [/bold cyan]")
    telefone = Prompt.ask("[bold cyan]Telefone: [/bold cyan]")

    # controle de acesso: criar todos os niveis somente admin, profissional e clientes podem add apenas clientes
    if USUARIO_LOGADO is not None and USUARIO_LOGADO.permissao == 'administrador':
        permissao = Prompt.ask("[bold cyan]Permissão do Usuário (administrador/profissional/cliente)[/bold cyan]")

    else:
        permissao = 'cliente'

    if usuarios.get(nome_usuario, None) is not None:
        console.print(f"[bold red]Erro:[/bold red] Usuário '[bold red]{nome_usuario}[/bold red]' já existe!", style="red")
        return False
    else: 
        with open(arq_user_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nome_usuario, senha, nome, telefone, permissao]) 
        console.print(f"[bold green]Usuário '{nome}', login: '{nome_usuario}', telefone: '{telefone}' cadastrado com sucesso![/bold green]")

    return nome_usuario

##### CRUD Delete
# Função para deletar um usuário.
# controle de acesso permite a admins esta função apenas
# Parâmetros: 
#   usuarios (dict) - dicionário de usuários.
#   arq_user_csv (str) - caminho do arquivo CSV.
# Retorno: bool - True se o usuário foi excluído com sucesso, False caso contrário.
def excluir_usuario(usuarios, arq_user_csv):
    console.print(Panel('''[bold red]Exclusão de Usuário[/bold red]\nPor favor, insira o login do usuário a ser excluído.''', 
                        title="Excluir Usuário", expand=False))
    nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário (nome_usuario)[/bold cyan]")

    # se encontrar o usuário, remova do arquivo
    if usuarios.get(nome_usuario, None) is not None:
        with open(arq_user_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            for usuario in usuarios.values():
                if usuario.login != nome_usuario:
                    writer.writerow([usuario.login, usuario.senha, usuario.nome, usuario.telefone, usuario.permissao]) 
        console.print(f"[bold green]Usuário '{nome_usuario}' excluído com sucesso![/bold green]")
        return True
    else:
        console.print(f"[bold yellow]Usuário '{nome_usuario}' não encontrado![/bold yellow]", style="yellow")
        return False
    
##### CRUD Update
# Função para atualizar a senha de um usuário.
# controle de acesso permite a admins alterar a senha de qualquer usuário
# e clientes podem apenas alterar a própria senha.
# Parâmetros: 
#   usuarios (dict) - dicionário de usuários.
#   arq_user_csv (str) - caminho do arquivo CSV.
# Retorno: bool - True se a senha foi atualizada com sucesso, False caso contrário.
def atualizar_senha(usuarios, arq_user_csv):
    global USUARIO_LOGADO

    if USUARIO_LOGADO is None:
        print('Essa função não deve ser chamada sem um usuário logado!!!')
        return False

    if USUARIO_LOGADO.permissao == 'cliente':
        console.print(Panel('''[bold yellow]Atualização de Senha[/bold yellow]\nPor favor, informe a nova senha desejada.''', 
                            title="Atualizar Senha", expand=False))
        nome_usuario = USUARIO_LOGADO.login
    

    if USUARIO_LOGADO.permissao == 'profissional':
        console.print(Panel('''[bold yellow]Atualização de Senha[/bold yellow]\nEscolha qual usuário terá a senha atualizada.''', 
                            title="Atualizar Senha", expand=False))     
        atualiza_profissional = Prompt.ask("[bold cyan]Por favor, digite '1' para atualizar a SUA senha ou '2' para atualizar a senha de algum cliente seu.[/bold cyan]")
        if atualiza_profissional == "1":
            nome_usuario = USUARIO_LOGADO.login
        elif atualiza_profissional == "2":
            nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário do cliente[/bold cyan]")
        else:
            print('Opção inválida!')
            return False

    else:
        console.print(Panel('''[bold yellow]Atualização de Senha[/bold yellow]\nPor favor, insira o login do usuário cuja senha será atualizada.''', 
                            title="Atualizar Senha", expand=False))
        nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário: [/bold cyan]")
    
    nova_senha = getpass("Nova senha: ")

    if usuarios.get(nome_usuario, None) is not None:
        with open(arq_user_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            for _, usuario in usuarios.items():
                if usuario.login != nome_usuario:
                    writer.writerow([usuario.login, usuario.senha, usuario.nome, usuario.telefone, usuario.permissao])
                else:
                    writer.writerow([usuario.login, nova_senha, usuario.nome, usuario.telefone, usuario.permissao])
        console.print(f"[bold green]Senha de '{nome_usuario}' atualizada com sucesso![/bold green]")
        return True
    else:
        console.print(f"[bold yellow]Usuário '{nome_usuario}' não encontrado![/bold yellow]", style="yellow")
        return False
    
##### CRUD Read
# Função para ler informações de cadastro de um usuário.
# controle de acesso permite o acesso unico por usuário e de todas as informações apenas a administradores.
# Parâmetros: 
#   usuarios (dict) - dicionário de usuários.
#   arq_user_csv (str) - caminho do arquivo CSV.
# Retorno: print das informações
def mostrar_informacoes(arq_user_csv):
    global USUARIO_LOGADO

    if USUARIO_LOGADO is None:
        print('Essa função não deve ser chamada sem um usuário logado!!!')
        return False

    if USUARIO_LOGADO.permissao == 'cliente' or USUARIO_LOGADO.permissao == 'profissional':
        console.print(Panel('[bold yellow]Informações de Cadastro[/bold yellow]', 
                            title="Informações de cadastro", expand=False))
        with open(arq_user_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
        
            next(reader) # Ignorar o cabeçalho (primeira linha)
            for row in reader:
                login, senha, nome, telefone, permissao = row
                if login == USUARIO_LOGADO.login:
                    print(f"Informações do usuário ({USUARIO_LOGADO.login}):")
                    print(f"Login: '{login}' , Nome: '{nome}', Senha: '{senha}', Telefone: '{telefone}', Permissão: '{permissao}'")
                return menu_interno
            ##ver se return da erro

    if USUARIO_LOGADO.permissao == 'administrador':
        console.print(Panel("[bold yellow]Informações de Cadastro [/bold yellow]", 
                            title="Informações de cadastro", expand=False))

        with open(arq_user_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    else:
        print(f"Usuário com login {USUARIO_LOGADO.login} não encontrado.")

##################### FIM FUNÇÕES DE USUARIO ########################


##################### INICIO FUNÇÕES DE SERVIÇOS #####################
##### CRUD Read
# Função para ler servicos do arquivo CSV.
# Parâmetro: arq_serv_csv (str) - caminho do arquivo CSV. #Retorno: dict - dicionário com servicos como chaves e tuplas; codigo como valores.
def ler_servicos(arq_serv_csv):
    servico = namedtuple('servico', ['codigo', 'atividade','regiao','tecnico','preco'])
    servicos = {}
    
    with open(arq_serv_csv, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            codigo,atividade,regiao,tecnico,preco = row
            servicos [codigo] = servico (codigo=codigo,atividade=atividade,regiao=regiao,tecnico=tecnico,preco=preco)
            print (servico)
    
    return servicos #return será utilizado para abrir demais funcoes servico

##### CRUD Create
# Função para cadastrar um novo serviço.
# controle de acesso permite apenas a admins criar/editar e excluir serviços
# Parâmetros: 
#   servicos (dict) - dicionário de servicos. 
#   arq_serv_csv (str) - caminho do arquivo CSV.
def cadastrar_servico(servicos, arq_serv_csv):
    if USUARIO_LOGADO is not None and USUARIO_LOGADO.permissao == 'administrador':
        console.print(Panel('''[bold green]Cadastro de Novo Serviço[/bold green]\nPor favor, insira os dados do novo serviço.''', 
                        title="Novo Serviço", expand=False))

        codigo = Prompt.ask("[bold cyan]codigo: [/bold cyan]")
        atividade = Prompt.ask("[bold cyan]atividade: [/bold cyan]")
        regiao = Prompt.ask("[bold cyan]regiao: [/bold cyan]")
        tecnico = Prompt.ask("[bold cyan]tecnico: [/bold cyan]")
        preco = Prompt.ask("[bold cyan]preco: [/bold cyan]")

        if servicos.get(codigo, None) is not None:
            console.print(f"[bold red]Erro:[/bold red] Serviço '[bold red]{login}[/bold red]' já existe!", style="red")
            return False
        else: 
            with open(arq_serv_csv, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([codigo,atividade,regiao,tecnico,preco]) 
            console.print(f"[bold green]codigo '{codigo}', atividade: '{atividade}', regiao: '{regiao}', tecnico: '{tecnico}', preco: '{preco}' cadastrado com sucesso![/bold green]")
    else:
        console.print("[bold yellow]Você não possui permissão para realizar esta ação. Contate a administração![/bold yellow]", style="yellow")
        return False
    return codigo

##### CRUD Delete
# Função para deletar um serviço.
# controle de acesso permite apenas a admins criar/editar e excluir serviços
# Parâmetros: 
#   servicos (dict) - dicionário de servicos.
#   arq_serv_csv (str) - caminho do arquivo CSV.
# Retorno: bool - True se o usuário foi excluído com sucesso, False caso contrário.
def excluir_servico(servicos, arq_serv_csv):
    if USUARIO_LOGADO is not None and USUARIO_LOGADO.permissao == 'administrador':
        console.print(Panel('''[bold red]Exclusão de Serviço[/bold red]\nPor favor, insira o Codigo do serviço a ser excluído.''', 
                        title="Excluir Serviço", expand=False))
        codigo = Prompt.ask("[bold cyan] Codigo do serviço[/bold cyan]")

        #se encontrar o servico, remova do arquivo
        if servicos.get(codigo, None) is not None:
            with open(arq_serv_csv, mode='w', newline='') as file:
                writer = csv.writer(file)
                for servico in servicos.values():
                    if servico.codigo != codigo:
                        writer.writerow([servico.codigo, servico.atividade, servico.regiao, servico.tecnico, servico.preco]) 
            console.print(f"[bold green]Serviço '{codigo}', excluído com sucesso![/bold green]")
            return True
        else:
            console.print(f"[bold yellow]Codigo '{codigo}' não encontrado![/bold yellow]", style="yellow")
            return False
    else:
        console.print("[bold yellow]Você não possui permissão para realizar esta ação. Contate a administração![/bold yellow]", style="yellow")
        return False
    

##### CRUD Update
# Função para atualizar o preço de um serviço.
# controle de acesso permite apenas a admins criar/editar e excluir serviços
# Parâmetros: 
#   servicos (dict) - dicionário de servicos.
#   arq_serv_csv (str) - caminho do arquivo CSV.
# Retorno: bool - True se a senha foi atualizado com sucesso, False caso contrário.
def atualizar_preco(servicos, arq_serv_csv):
    if USUARIO_LOGADO is not None and USUARIO_LOGADO.permissao == 'administrador':
        console.print(Panel('''[bold yellow]Atualização de Preço de serviço[/bold yellow]\nPor favor, insira o codigo do serviço para realizar a atualização.''', 
                            title="Atualizar preço", expand=False))

        codigo = Prompt.ask("[bold cyan]Codigo do serviço: [/bold cyan]")
    
        novo_preco = Prompt.ask("[bold cyan]Novo preço do serviço: [/bold cyan]")

        if servicos.get(codigo, None) is not None:
            with open(arq_serv_csv, mode='w', newline='') as file:
                writer = csv.writer(file)
                for _, servico in servicos.items():
                    if servico.codigo != codigo:
                        writer.writerow([servico.codigo, servico.atividade, servico.regiao, servico.tecnico, servico.preco])
                    else:
                        writer.writerow([servico.codigo, servico.atividade, servico.regiao, servico.tecnico, novo_preco])
            console.print(f"[bold green]Serviço '{codigo}' atualizado com sucesso![/bold green]")
            return True
        else:
            console.print(f"[bold yellow]Servico '{codigo}' não encontrado![/bold yellow]", style="yellow")
            return False
    else:
        console.print("[bold yellow]Você não possui permissão para realizar esta ação. Contate a administração![/bold yellow]", style="yellow")
        return False    
##################### FIM FUNÇÕES DE SERVIÇOS #####################


##################### INICIO FUNÇÕES DE AGENDAMENTOS #####################
## constantes
ARQUIVO_AGENDA = 'agenda.csv'

#with open ("agenda.csv", mode="r") as file: #visualização dos agendamentos #administrador
#    reader = csv.reader(file, )
#    writer.writerows(dados_agenda)

def agendar_visita(cliente, cod_serv, atividade, tecnico, data): #criar agenda #profissional #cliente
    with open("agenda.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([cliente, cod_serv, atividade, tecnico, data])
# Exemplo de uso
#agendar_visita = ('Carlos Silva', 'le01','limpeza de equipamento','Lucas Pereira', '2025-03-25')

#def listar_agendamentos():  #visualizar agendamentos (cliente, profissional e administrador)
#   with open("agenda.csv", mode="r", newline="") as file:
 #   reader = csv.reader(file)
   # for linha in reader:
    #    print(linha) 

#listar_agendamentos()
##################### FIM FUNÇÕES DE AGENDAMENTOS #####################

##################### INICIO FUNÇÕES DE MENU - INTERAÇÃO ########################
######### 1.TELA MENU INICIAL APP - OPÇÕES P/ LOGIN, CRIAR CADASTRO, SAIR ##################
# Função para exibir o menu inicial.
# Retorno: str - opção escolhida pelo usuário.
def menu_inicial(): #Customização
    console.print(Panel("[bold green]Sistema de Agendamentos de Visita Técnica![/bold green]\nEscolha uma das opções abaixo:", title="Menu Inicial", expand=False))
    console.print("[bold cyan]1.[/bold cyan] [bold white]Fazer Login[/bold white]")
    console.print("[bold cyan]2.[/bold cyan] [bold white]Cadastrar[/bold white]")
    console.print("[bold cyan]3.[/bold cyan] [bold white]Serviços[/bold white]")
    console.print("[bold cyan]0.[/bold cyan] [bold white]Sair do sistema[/bold white]")
    
    opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["1", "2", "3", "0"])
    return opcao

########## 2.TELA MENU INTERNO APP ###################
# Retorno: str - opção escolhida pelo usuário.
def menu_interno():
    console.print(Panel(f"[bold green]Olá {USUARIO_LOGADO.nome}![/bold green]\nEscolha uma das opções abaixo:", 
                        title="Menu Interno", expand=False))
    
    # controle de acesso - gerenciamento de permissões dos usuários
    # administrador pode atualizar ou excluir
    # cliente apenas atualizam (lógica interna para atualizar somente seu próprio cadastro)
    if USUARIO_LOGADO.permissao == 'administrador':
        console.print("[bold cyan]1.[/bold cyan] [bold white]Atualizar senha[/bold white]")
        console.print("[bold cyan]3.[/bold cyan] [bold white]Excluir cadastro[/bold white]")
        console.print("[bold cyan]4.[/bold cyan] [bold white]Visualizar cadastros de usuários[/bold white]")
        console.print("[bold cyan]5.[/bold cyan] [bold white]Visualizar cadastros de serviços[/bold white]")
        console.print("[bold cyan]6.[/bold cyan] [bold white]Adicionar serviço[/bold white]")
        console.print("[bold cyan]7.[/bold cyan] [bold white]Visualizar agendamentos[/bold white]")
        console.print("[bold cyan]0.[/bold cyan] [bold white]Para fazer logout digite '0'[/bold white]")
        opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["0","1", "3", "4", "5", "6", "7"])

    elif USUARIO_LOGADO.permissao == 'profissional':
        console.print("[bold cyan]1.[/bold cyan] [bold white]Atualizar senha[/bold white]")
        console.print("[bold cyan]2.[/bold cyan] [bold white]Visualizar informações de cadastro [/bold white]")
        console.print("[bold cyan]3.[/bold cyan] [bold white]Excluir cadastro[/bold white]")
        console.print("[bold cyan]7.[/bold cyan] [bold white]Visualizar agendamentos[/bold white]")
        console.print("[bold cyan]8.[/bold cyan] [bold white]Criar agendamento[/bold white]")
        console.print("[bold cyan]0.[/bold cyan] [bold white]Para fazer logout digite '0'[/bold white]")
        opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["0","1", "2", "7", "8"])

    else:
        console.print("[bold cyan]1.[/bold cyan] [bold white]Atualizar senha[/bold white]")
        console.print("[bold cyan]2.[/bold cyan] [bold white]Visualizar informações de cadastro [/bold white]")
        console.print("[bold cyan]0.[/bold cyan] [bold white]Para fazer logout digite '0'[/bold white]") ##visualizar agendamento
        opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["0","2", "1"])
    return  opcao

##### CRUD Read
# Parâmetro: usuarios (dict) - dicionário de usuários.
def fazer_login(usuarios):
    # explicitar o acesso à variável global senão a atribuição ao final da função vai criar uma nova variável local
    global USUARIO_LOGADO # Atualiza a variável global USUARIO_LOGADO em caso de login bem sucedido.

    console.print(Panel('''🟢 [bold green]Login[/bold green] 🟢\n\nPor favor, insira seus dados:''', #Customização
                        expand=False, title="Tela de Login"))
    usuario = Prompt.ask("[bold cyan]Login de Usuário[/bold cyan]")
    senha = getpass("Senha: ")

    login = usuarios.get(usuario, None)
    if login is not None and login.senha == senha:
        console.print("\n[bold green]Login bem-sucedido![/bold green]")
        USUARIO_LOGADO = login
    else:
        console.print(f"[bold red]Erro: usuário ou senha incorretos!", style="red")
##################### FIM FUNÇÕES DE MENU - INTERAÇÃO ########################

##################### INICIO FLUXO PRINCIPAL DO CODIGO ###################### 
console = Console()
usuarios = ler_usuarios(ARQUIVO_USUARIOS)
while True:
    opcao = menu_inicial() #CRUDE :::: READ
    if opcao == "1":
        fazer_login(usuarios) #encaminha para função fazer login
    elif opcao == "2":
        novo_user = cadastrar_usuario (usuarios, ARQUIVO_USUARIOS) #encaminha para função cadastrar
        if novo_user != False:
            usuarios = ler_usuarios(ARQUIVO_USUARIOS)
            USUARIO_LOGADO = usuarios.get(novo_user)
    elif opcao == "3":
       print (ler_servicos('servicos.csv')) #apresenta os serviços e retorna ao menu inicial
    elif opcao == "4":
        mostrar_informacoes (USUARIO_LOGADO, ARQUIVO_USUARIOS)
    elif opcao == "0": #sai do programa
        break
    else:
        console.print(f"[bold yellow]Opção inválida![/bold yellow]", style="yellow")

    if USUARIO_LOGADO is not None:
        while True:
            opcao = menu_interno()
            if opcao == '0': break
            elif opcao == "1": 
                if atualizar_senha(usuarios, ARQUIVO_USUARIOS): #CRUD :::: UPDATE
                    usuarios = ler_usuarios(ARQUIVO_USUARIOS)
            elif opcao == "2": 
                if excluir_usuario(usuarios, ARQUIVO_USUARIOS): #CRUD :::: DELETE
                    usuarios = ler_usuarios(ARQUIVO_USUARIOS)
            elif opcao == "3":
                print (ler_servicos('servicos.csv')) #apresenta os serviços e retorna ao menu inicial
            elif opcao == "4":
                mostrar_informacoes (ARQUIVO_USUARIOS)
##################### FIM FLUXO PRINCIPAL DO CODIGO ###################### 

