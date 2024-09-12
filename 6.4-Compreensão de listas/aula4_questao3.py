#dados
horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25

#construindo a lista pagamentos usando compreensão de listas
pagamentos = [
    ganho_por_hora * min(hora, 40) + hora_extra * max(0, hora - 40)
    for hora in horas_trabalhadas
]

#imprimindo a lista pagamentos
print(pagamentos)
