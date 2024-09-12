#solicita uma frase do usuário
frase = input("Digite uma frase")

#define as vogais
vogais = 'aeiouAEIOU'

#cria a lista de vogais da frase, ordenada alfabeticamente
lista_vogais = sorted([caractere for caractere in frase if caractere in vogais])

#cria a lista de consoantes da frase
lista_consoantes = [caractere for caractere in frase if caractere.isalpha() and caractere not in vogais]

#imprime os resultados
print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)
