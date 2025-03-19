#A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula".
# É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets.
# Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções:::::::::
#Selecione pelo menos 10 livros que você leu ou gostaria de ler.
# Você deve reunir as seguintes informações: título, autor, ano de publicação e número de páginas.
#No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.
#Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.
#A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.
#Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. Como você já tem conta no Google, sugiro abrir com o Google Sheets.


#cab = ['titulo', 'autor', 'ano de publicacao' , 'num de pgs']
#livros = [['1984', 'George Orwell', '1949', '328'] , ['Dom Casmurro', 'Machado de Assis', '1899', '304'] , ['O Grande Gatsby', 'F. Scott Fitzgerald', '1925', '218'] , ['Cem Anos de Solidão', 'Gabriel García Márquez', '1967', '448'] , ['O Senhor dos Anéis: A Sociedade do Anel', 'J.R.R. Tolkien', '1954', '423']]
#livros = [i +'\n' for i in cab]

#with open ('livros1.csv', 'w') as f:
#    f.writelines (cab)

import csv
livros = [['titulo', 'autor', 'ano de publicacao' , 'num de pgs'] , ['1984', 'George Orwell', '1949', '328'] , ['Dom Casmurro', 'Machado de Assis', '1899', '304'] , ['O Grande Gatsby', 'F. Scott Fitzgerald', '1925', '218'] , ['Cem Anos de Solidão', 'Gabriel García Márquez', '1967', '448'] , ['O Senhor dos Anéis: A Sociedade do Anel', 'J.R.R. Tolkien', '1954', '423']]

with open('livros.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Escrevendo todas as linhas no arquivo CSV
    writer.writerows(livros)