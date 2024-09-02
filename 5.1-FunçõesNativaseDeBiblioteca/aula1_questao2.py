import random
import math

def raiz_soma():
    try:
        #solicita ao usuário o número de valores a serem gerados
        n = int(input("Digite o número de valores inteiros aleatórios a serem gerados: "))

        if n <= 0:
            print("Por favor, insira um número inteiro positivo.")
            return

        #gera n valores inteiros aleatórios entre 0 e 100
        nums = [random.randint(0, 100) for _ in range(n)]

        #calcula a soma dos valores
        total = sum(nums)

        #calcula a raiz quadrada da soma
        raiz = math.sqrt(total)

        #exibe o resultado
        print(f"Valores gerados: {nums}")
        print(f"Soma dos valores: {total}")
        print(f"Raiz quadrada da soma: {raiz:.2f}")

    except ValueError:
        print("Por favor, insira um número inteiro válido.")

#executa a função principal
raiz_soma()

