import random
from collections import Counter

# Gera duas listas com 20 valores aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

#cria contadores para as duas listas
contador1 = Counter(lista1)
contador2 = Counter(lista2)

#cria a lista de interseção sem duplicatas
interseccao = sorted(set(lista1) & set(lista2))

#imprime as listas originais
print("Lista 1:", lista1)
print("Lista 2:", lista2)

#imprime a lista de interseção ordenada
print("Interseccao:", interseccao)

#imprime a contagem de elementos
print("Contagem:")
for elemento in interseccao:
    print(f"{elemento}: (lista1={contador1[elemento]}, lista2={contador2[elemento]})")
