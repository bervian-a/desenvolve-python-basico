import csv
from collections import namedtuple
from getpass import getpass

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel


## constantes
ARQUIVO_USUARIOS = 'usuarios.txt'
USUARIO_LOGADO = None

##################### Funções de usuário #####################

##### CRUD Read
# Função para ler usuários de um arquivo CSV.
# Parâmetro: arquivo_csv (str) - caminho do arquivo CSV.
# Retorno: dict - dicionário com logins como chaves e tuplas nomeadas Usuario como valores.
# conheça as tuplas nomeadas: https://www.geeksforgeeks.org/namedtuple-in-python/
def ler_usuarios(arquivo_csv):
    Usuario = namedtuple('Usuario', ['login', 'senha', 'tipo'])
    usuarios = {}
    
    with open(arquivo_csv, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            nome_usuario, senha, tipo = row
            usuarios[nome_usuario] = Usuario(login=nome_usuario,senha=senha, tipo=tipo)
    
    return usuarios


##### CRUD Read
# Função para realizar login de um usuário.
# Atualiza a variável global USUARIO_LOGADO em caso de login bem sucedido.
# Parâmetro: usuarios (dict) - dicionário de usuários.
# Retorno: None
def fazer_login(usuarios):
    # preciso explicitar o acesso à variável global
    # senão a atribuição ao final da função criará uma nova variável local
    global USUARIO_LOGADO

    console.print(Panel('''🟢 [bold green]Login[/bold green] 🟢\n\nPor favor, insira suas credenciais.''', 
                        expand=False, title="Tela de Login"))
    username = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")
    senha = getpass("Senha: ")

    user = usuarios.get(username, None)
    if user is not None and user.senha == senha:
        console.print("\n[bold green]Login bem-sucedido![/bold green]")
        USUARIO_LOGADO = user
    else:
        console.print(f"[bold red]Erro: usuário ou senha incorretos!", style="red")



##### CRUD Create
# Função para cadastrar um novo usuário.
# Parâmetros: 
#   usuarios (dict) - dicionário de usuários.
#   arquivo_csv (str) - caminho do arquivo CSV.
# Retorno: str - nome do novo usuário ou False em caso de falha.
def cadastrar_usuario(usuarios, arquivo_csv):
    console.print(Panel('''[bold green]Cadastro de Novo Usuário[/bold green]\nPor favor, insira os dados do novo usuário.''', 
                        title="Novo Usuário", expand=False))

    nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")
    senha = getpass("Senha: ")

    # controle de acesso permite criação de novos admins somente se usuário logado é admin
    if USUARIO_LOGADO is not None and USUARIO_LOGADO.tipo == 'admin':
        tipo = Prompt.ask("[bold cyan]Tipo de Usuário (admin/cliente)[/bold cyan]") 
    else:
        tipo = 'cliente'

    if usuarios.get(nome_usuario, None) is not None:
        console.print(f"[bold red]Erro:[/bold red] Usuário '[bold red]{nome_usuario}[/bold red]' já existe!", style="red")
        return False
    else: 
        with open(arquivo_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nome_usuario, senha, tipo]) 
        console.print(f"[bold green]Usuário '{nome_usuario}' cadastrado com sucesso![/bold green]")

    return nome_usuario

##### CRUD Delete
# Parâmetros: 
#   usuarios (dict) - dicionário de usuários.
#   arquivo_csv (str) - caminho do arquivo CSV.
# Retorno: bool - True se o usuário foi excluído com sucesso, False caso contrário.
def excluir_usuario(usuarios, arquivo_csv):
    console.print(Panel('''[bold red]Exclusão de Usuário[/bold red]\nPor favor, insira o nome do usuário a ser excluído.''', 
                        title="Excluir Usuário", expand=False))
    nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")

    # se encontrar o usuário, remova do arquivo
    if usuarios.get(nome_usuario, None) is not None:
        with open(arquivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            for usuario in usuarios.values():
                if usuario.login != nome_usuario:
                    writer.writerow([usuario.login, usuario.senha, usuario.tipo]) 
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
#   arquivo_csv (str) - caminho do arquivo CSV.
# Retorno: bool - True se a senha foi atualizada com sucesso, False caso contrário.
def atualiza_senha(usuarios, arquivo_csv):
    global USUARIO_LOGADO

    if USUARIO_LOGADO is None:
        print('Essa função não deve ser chamada sem um usuário logado!!!')
        return False

    if USUARIO_LOGADO.tipo == 'cliente':
        console.print(Panel('''[bold yellow]Atualização de Senha[/bold yellow]\nPor favor, informe a nova senha desejada.''', 
                            title="Atualizar Senha", expand=False))
        nome_usuario = USUARIO_LOGADO.login
    else:
        console.print(Panel('''[bold yellow]Atualização de Senha[/bold yellow]\nPor favor, insira o nome do usuário cuja senha será atualizada.''', 
                            title="Atualizar Senha", expand=False))

        nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")
    
    nova_senha = getpass("Nova senha: ")

    if usuarios.get(nome_usuario, None) is not None:
        with open(arquivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            for _, usuario in usuarios.items():
                if usuario.login != nome_usuario:
                    writer.writerow([usuario.login, usuario.senha, usuario.tipo])
                else:
                    writer.writerow([usuario.login, nova_senha, usuario.tipo])
        console.print(f"[bold green]Usuário '{nome_usuario}' excluído com sucesso![/bold green]")
        return True
    else:
        console.print(f"[bold yellow]Usuário '{nome_usuario}' não encontrado![/bold yellow]", style="yellow")
        return False
##################### FIM FUNÇÕES DE USUARIO ########################

# Função para exibir o menu inicial.
# Retorno: str - opção escolhida pelo usuário.
def menu_inicial():
    console.print(Panel("[bold green]Sistema de brincadeirinha![/bold green]\nEscolha uma das opções abaixo:", title="Menu Inicial", expand=False))
    console.print("[bold cyan]1.[/bold cyan] [bold white]Fazer Login[/bold white]")
    console.print("[bold cyan]2.[/bold cyan] [bold white]Cadastro[/bold white]")
    console.print("[bold cyan]3.[/bold cyan] [bold white]Sair do sistema[/bold white]")
    
    opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["1", "2", "3"])
    return opcao

# Função para exibir o menu interno.
# Retorno: str - opção escolhida pelo usuário.
def menu_interno():
    console.print(Panel(f"[bold green]Olá {USUARIO_LOGADO.login}![/bold green]\nEscolha uma das opções abaixo:", 
                        title="Menu Interno", expand=False))
    
    # controle de acesso para gerenciamento de usuários
    # admin pode atualizar ou excluir
    # cliente apenas atualizam (lógica interna para atualizar somente seu próprio cadastro)
    if USUARIO_LOGADO.tipo == 'admin':
        console.print("[bold cyan]1.[/bold cyan] [bold white]Atualizar cadastro[/bold white]")
        console.print("[bold cyan]2.[/bold cyan] [bold white]Excluir cadastro[/bold white]")
        console.print("[bold white]Para fazer logout digite[/bold white] [bold cyan]0[/bold cyan]")
        opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["0","1", "2"])
    else:
        console.print("[bold cyan]1.[/bold cyan] [bold white]Atualizar cadastro[/bold white]")
        console.print("[bold white]Para fazer logout digite[/bold white] [bold cyan]0[/bold cyan]")
        opcao = Prompt.ask("[bold yellow]Digite o número da opção desejada[/bold yellow]", choices=["0","1"])
    return  opcao

##################### Fluxo principal do código ###################### 
console = Console()
usuarios = ler_usuarios(ARQUIVO_USUARIOS)
while True:
    opcao = menu_inicial()
    if opcao == "1":
        fazer_login(usuarios)
    elif opcao == "2":
        novo_user = cadastrar_usuario(usuarios, ARQUIVO_USUARIOS)
        if novo_user != False:
            usuarios = ler_usuarios(ARQUIVO_USUARIOS)
            USUARIO_LOGADO = usuarios.get(novo_user)
    elif opcao == "3": 
        break
    else:
        console.print(f"[bold yellow]Opção inválida![/bold yellow]", style="yellow")

    if USUARIO_LOGADO is not None:
        while True:
            opcao = menu_interno()
            if opcao == '0': break
            elif opcao == "1": 
                if atualiza_senha(usuarios, ARQUIVO_USUARIOS):
                    usuarios = ler_usuarios(ARQUIVO_USUARIOS)
            elif opcao == "2": 
                if excluir_usuario(usuarios, ARQUIVO_USUARIOS):
                    usuarios = ler_usuarios(ARQUIVO_USUARIOS)
############################################################################
    
