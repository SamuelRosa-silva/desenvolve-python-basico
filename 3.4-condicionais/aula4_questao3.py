# entrada do ano escolhido pelo usúario
ano = int(input("Informe um ano: "))

#processo de verificação se o ano é bisseto ou não
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não Bissexto")