#Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", 
# use o conceito de fatiamento de listas para criar uma lista dominios com o nome principal de todos os domínios, conforme exemplo a seguir. 

#URLs: ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
#dominios:  ["google", "gmail", "github", "reddit", "yahoo"] 

lista_urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com", "www.amazon.com" , "www.python.com"]


def extrair_dominio(url):
    partes = url.split('.')
    if len(partes) > 1:
        return partes[1]
    return None

# Aplica a função em cada URL
lista_dominio = [extrair_dominio (url) for url in lista_urls]
lista_dominio = [url for url in lista_dominio if url is not None]

print ("Lista urls: ", lista_urls)
print("Lista dominos: ",lista_dominio)