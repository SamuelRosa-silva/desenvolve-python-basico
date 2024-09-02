#realiza a atribuição de valores para as variaveis
n1, n2, n3 = map(int, input("Digite três notas separadas por espaço: ").split())

#defini o resultado do calculo para a variavel
m = (n1 + n2 + n3) / 3

#realiza a comparação do resultado para retornar a situação do aluno
if m >= 60:
    print("aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("reprovado")