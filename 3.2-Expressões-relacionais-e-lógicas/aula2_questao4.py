def validar_ficha(classe, forca, magia):
    if classe == "guerreiro":
        return forca >= 15 and magia <= 10
    elif classe == "mago":
        return forca <= 10 and magia >= 15
    elif classe == "arqueiro":
        return 5 < forca <= 15 and 5 < magia <= 15
    else:
        return False
clas=input("Escolha a classe do personagem (guerreiro, mago ou arqueiro): ").strip().lower()
forca=int(input("Digite os pontos de força: ")) #entrada de dados
magia=int(input("Digite os pontos de magia: "))
valido=validar_ficha(clas, forca, magia)
print(valido)
