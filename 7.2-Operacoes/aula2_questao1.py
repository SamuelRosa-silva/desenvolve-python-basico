def obter_nome_mes(numero_mes):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    #retorna o nome do mês correspondente ao número do mês
    return meses[numero_mes - 1]

#solicita ao usuário que digite a data de nascimento
data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

#divide a data em partes (dia, mês e ano)
dia, mes, ano = data_nascimento.split('/')

#converte o mês para um número inteiro
numero_mes = int(mes)

#obtém o nome do mês
nome_mes = obter_nome_mes(numero_mes)

#imprime a data formatada com o nome do mês por extenso
print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")