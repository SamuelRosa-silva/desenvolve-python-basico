#Lê o número de experimentos
N = int(input("Digite a quantidade de experimentos registrados: "))

#Inicializa as variáveis para contar o total de cobaias e o total de cada tipo
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

#Processa cada experimento
for _ in range(N):
    entrada = input("Digite a quantidade e o tipo de cobaia (quantia Tipo): ").split()
    quantia = int(entrada[0])
    tipo = entrada[1]
    
    #Atualiza os totais conforme o tipo de cobaia
    total_cobaias += quantia
    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':
        total_coelhos += quantia

#Calcula os percentuais de cada tipo
percentual_sapos = (total_sapos / total_cobaias) * 100
percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_coelhos = (total_coelhos / total_cobaias) * 100

#Exibe os resultados
print(f"Total de cobaias: {total_cobaias}")
print(f"Total de sapos: {total_sapos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de coelhos: {total_coelhos}")
print(f"Percentual de sapos: {percentual_sapos:.2f}%")
print(f"Percentual de ratos: {percentual_ratos:.2f}%")
print(f"Percentual de coelhos: {percentual_coelhos:.2f}%")