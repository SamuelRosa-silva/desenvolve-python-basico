def formatar_numero_celular(numero):
    #verifica o comprimento do número
    if len(numero) == 8:
        #adiciona o dígito 9 na frente
        numero = '9' + numero
    elif len(numero) == 9:
        if numero[0] != '9':
            #se o primeiro dígito não é 9, exibe uma mensagem de erro
            return "Número inválido. Um número de 9 dígitos deve começar com 9."
    else:
        return "Número inválido. Deve ter 8 ou 9 dígitos."

    #adiciona o separador "-" na impressão
    numero_formatado = numero[:5] + '-' + numero[5:]
    return numero_formatado

#solicita ao usuário que insira o número de celular
numero = input("Digite o número de celular: ")

#formata e imprime o número de celular
resultado = formatar_numero_celular(numero)
print(resultado)
