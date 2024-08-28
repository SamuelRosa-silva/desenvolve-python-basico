#Entrada da distancia informada pelo usúario 
dis = float(input("Informe a distância da entrega em quilômetros: "))

#Entrada da peso informado pelo usúrario
peso = float(input("Informe o peso do pacote em quilogramas: "))

#Processo de calculo do frete com base no peso 
if dis <= 100:
    valor_frete = peso * 1
elif 101 <= dis <= 300:
    valor_frete = peso * 1.50
else:
    valor_frete = peso * 2

#Adicona a taxa extra para pacotes com peso maior que 10kg
if peso > 10:
    valor_frete += 10

#iImprime o valor total do frete
print(f"O valor total do frete é: R${valor_frete:.2f}")