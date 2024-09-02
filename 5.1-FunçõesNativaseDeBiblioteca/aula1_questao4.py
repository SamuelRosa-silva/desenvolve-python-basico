from datetime import datetime

def exibir_data_e_hora():
    #     #extrai a informação de hora e data atual
    agora = datetime.now()

    #formata a data e hora
    data_formatada = agora.strftime("Data: %d/%m/%Y")
    hora_formatada = agora.strftime("Hora: %H:%M")

    #exibe a data e hora
    print(data_formatada)
    print(hora_formatada)

#executa a função principal
exibir_data_e_hora()