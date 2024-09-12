import random

#gera 20 valores aleatórios entre -100 e 100
valores = [random.randint(-100, 100) for _ in range(20)]

#copia a lista para ordenar sem modificar a lista original
valores_ordenados = sorted(valores)

#encontra o índice do maior e menor valor
indice_maior = valores.index(max(valores))
indice_menor = valores.index(min(valores))

#imprime os resultados
print("Lista ordenada:", valores_ordenados)
print("Lista original:", valores)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)