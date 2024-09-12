import random

#gera aleatoriamente um valor entre 5 e 20 para o número de elementos
num_elementos = random.randint(5, 20)

#gera uma lista com 'num_elementos' valores aleatórios entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

#calcula a soma e a média dos valores da lista
soma = sum(elementos)
media = soma / num_elementos

#imprime os resultados
print("Lista elementos:", elementos)
print("Soma dos valores:", soma)
print("Média dos valores:", media)
