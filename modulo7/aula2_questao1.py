#Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".


def data_com_nome_mes():
    # Solicita a data de nascimento no formato dd/mm/aaaa
    data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    
   
    dia, mes, ano = data.split('/')
    
    # Lista com os nomes dos meses por extenso (1 a 12)
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    # Substitui o número do mês pelo nome correspondente
    mes_nome = meses[int(mes) - 1]      
   
    print(f"Você nasceu em {dia} de {mes_nome} de {ano}.")

# Chama a função
data_com_nome_mes()

