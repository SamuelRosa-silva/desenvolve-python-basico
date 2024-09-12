def substituir_vogais_por_asterisco(frase):
    # Define as vogais a serem substituídas
    vogais = 'aeiouAEIOU'
    #substitui cada vogal na frase por '*'
    frase_modificada = ''.join('*' if caractere in vogais else caractere for caractere in frase)
    return frase_modificada

#solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

#aplica a substituição e obtém a frase modificada
frase_modificada = substituir_vogais_por_asterisco(frase)

#imprime a frase modificada
print(f"Frase modificada: {frase_modificada}")