import random

def adivinhar_numero():
    #gera um número aleatório entre 1 e 10
    numero_secreto = random.randint(1, 10)

    while True:
        try:
            #solicita ao usuário que adivinhe o número
            palpite = int(input("Adivinhe o número entre 1 e 10: "))

            #verifica se o palpite está dentro do intervalo permitido
            if palpite < 1 or palpite > 10:
                print("Por favor, insira um número entre 1 e 10.")
                continue

            #verifica o palpite
            if palpite < numero_secreto:
                print("Muito baixo, tente novamente!")
            elif palpite > numero_secreto:
                print("Muito alto, tente novamente!")
            else:
                print(f"Correto! O número é {numero_secreto}.")
                break

        except ValueError:
            print("Por favor, insira um número inteiro válido.")

#executa a função principal
adivinhar_numero()