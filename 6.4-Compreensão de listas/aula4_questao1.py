#lista de todos os números pares entre 20 e 50
pares = [x for x in range(20, 51) if x % 2 == 0]

#lista dos quadrados de todos os valores da lista [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [x**2 for x in range(1, 10)]

#lista de todos os números entre 1 e 100 que são divisíveis por 7
divisiveis_por_7 = [x for x in range(1, 101) if x % 7 == 0]

#lista que indica "par" ou "ímpar" para todos os valores em range(0, 30, 3)
paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]

#imprime as listas
print("Números pares entre 20 e 50:", pares)
print("Quadrados dos valores de 1 a 9:", quadrados)
print("Números entre 1 e 100 divisíveis por 7:", divisiveis_por_7)
print("Paridade para valores em range(0, 30, 3):", paridade)
