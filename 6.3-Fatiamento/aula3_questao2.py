#lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

#cria a lista de domínios
dominios = [url[4:-4] for url in urls]

#imprime a lista de domínios
print("URLs:", urls)
print("Domínios:", dominios)