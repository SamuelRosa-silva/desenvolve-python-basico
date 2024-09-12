def obter_lista(nome_lista):
    quantidade = int(input(f"Digite a quantidade de elementos da {nome_lista}: "))
    lista = []
    print(f"Digite os {quantidade} elementos da {nome_lista}:")
    for _ in range(quantidade):
        elemento = int(input())
        lista.append(elemento)
    return lista

def intercalar_listas(lista1, lista2):
    intercalada = []
    len1, len2 = len(lista1), len(lista2)
    min_len = min(len1, len2)

    #intercala os elementos das duas listas até o menor comprimento
    for i in range(min_len):
        intercalada.append(lista1[i])
        intercalada.append(lista2[i])

    #adiciona os elementos restantes da lista maior
    if len1 > len2:
        intercalada.extend(lista1[min_len:])
    else:
        intercalada.extend(lista2[min_len:])

    return intercalada

#obtém as listas do usuário
lista1 = obter_lista("lista 1")
lista2 = obter_lista("lista 2")

#intercala as listas
lista_intercalada = intercalar_listas(lista1, lista2)

#imprime o resultado
print("Lista intercalada:", " ".join(map(str, lista_intercalada)))
