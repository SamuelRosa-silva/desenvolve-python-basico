#Inicializa a variável maior com 0
maior = 0

#Lê o valor de n
n = int(input("Digite a quantidade de números (n): "))

#Loop para processar os n números
while n > 0:
    #Lê o número x
    x = int(input("Digite um número (x): "))
    
    #Se x for maior que maior, atualize maior
    if x > maior:
        maior = x
    
    #Decrementa n
    n = n - 1

#Imprime o maior valor encontrado
print("O maior número é:", maior)
