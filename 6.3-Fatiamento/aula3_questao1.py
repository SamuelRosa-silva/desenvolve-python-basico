def obter_numeros():
    print("Digite pelo menos 4 números inteiros, depois figite 'fim' para encerrar.")
    numeros = []
    while True:
        entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")
        if entrada.lower() == 'fim':
            if len(numeros) >= 4:
                break
            else:
                print("Por favor Você deve insira pelo menos 4 números, Tente novamente.")
        else:
            try:
                numero = int(entrada)
                numeros.append(numero)
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    return numeros

#obtém a lista de números do usuário
lista_numeros = obter_numeros()

#imprime a lista original
print("Lista original:", lista_numeros)

#imprime os 3 primeiros elementos
print("Os 3 primeiros elementos:", lista_numeros[:3])

#imprime os 2 últimos elementos
print("Os 2 últimos elementos:", lista_numeros[-2:])

#imprime a lista invertida
print("Lista invertida:", lista_numeros[::-1])

#imprime os elementos de índice par
print("Elementos de índice par:", lista_numeros[::2])

#imprime os elementos de índice ímpar
print("Elementos de índice ímpar:", lista_numeros[1::2])
