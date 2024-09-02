#função principal
def calcular_diferenca_absoluta():
    try:
        #solicita ao usuário para inserir dois números decimais
        num1 = float(input("Digite um número decimal: "))
        num2 = float(input("Digite mais um número decimal: "))

        #calcula a diferença absoluta entre os dois números
        diferenca = abs(num1 - num2)

        #arredonda a diferença para duas casas decimais
        diferenca_arredondada = round(diferenca, 2)

        #exibe o resultado
        print(f"A diferença absoluta entre {num1} e {num2} é {diferenca_arredondada:.2f}")

    except ValueError:
        print("Por favor, insira números válidos, que sejam decimais.")

#executa a função principal
calcular_diferenca_absoluta()