#input de dois números
na = int(input("Informe um número:"))
nb = int(input("por favor mais um número:"))

#soma das entradas
sum = na + nb

#verifica se o resultado é par ou impar
if sum % 2 == 0:
    print("A soma é par.")
else:
    print("A soma é ímpar.")