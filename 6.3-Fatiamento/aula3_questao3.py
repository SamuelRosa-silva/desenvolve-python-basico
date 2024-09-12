import random

#gera uma lista com 20 elementos aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

#função para encontrar o intervalo com o maior número de negativos
def intervalo_maior_negativos(lista):
    max_negativos = 0
    melhor_inicio = 0
    melhor_fim = 0

    #verifica todos os possíveis intervalos
    for i in range(len(lista)):
        for j in range(i + 1, len(lista) + 1):
            intervalo = lista[i:j]
            num_negativos = sum(1 for x in intervalo if x < 0)
            if num_negativos > max_negativos:
                max_negativos = num_negativos
                melhor_inicio = i
                melhor_fim = j
    
    return melhor_inicio, melhor_fim

#imprime a lista original
print("Original:", lista)

#encontra o intervalo com o maior número de números negativos
inicio, fim = intervalo_maior_negativos(lista)

#deleta o intervalo da lista
del lista[inicio:fim]

#imprime a lista editada
print("Editada:", lista)
