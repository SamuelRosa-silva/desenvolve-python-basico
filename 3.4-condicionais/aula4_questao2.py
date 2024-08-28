#input da avaliação do usúario
avaliacao = int(input("Olá, você gostou do filme? deixe sua avalização de 1 a 5  ):"))

#processo de verivicação se o input está dentro dos limites
if 1 <= avaliacao <= 5:
    #imrime a avaliação do usúrio 
    if avaliacao == 1:
        print("Classificação: ruim, Obrigado por avaliar!")
    elif avaliacao == 2:
        print("Classificação: Regular, Obrigado por avaliar!")
    elif avaliacao == 3:
        print("Classificação: Bom! Obrigado por avaliar!")
    elif avaliacao == 4:
        print("Classificação: Muito bom! Obrigado por avaliar!")
    elif avaliacao == 5:
        print("Classificação: Excelente! Obrigado por avaliar!")
else:
    print("Avaliação inválida. Por favor, insira um número entre 1 e 5.")