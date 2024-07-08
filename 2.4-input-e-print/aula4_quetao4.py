import match
vl = int(input ('Digite um valor inteiro em reais')) #entrada do valor a ser lido
nd = [100, 50, 20, 10, 5, 2, 1] #notas para serem usadas 
qn = [0] * len(nd) #lista de notas disponiveis
for i in range(len(nd)):#loop que itaera as listas
    qn[i] = vl // nd[i] #qualculando a quantidade de notas
    vl %= nd[i] #atualiza o valor restante 
print(vl) #imprime a contabilização de notas 
print(f"{qn[0]} nota(s) de R$100,00")
print(f"{qn[1]} nota(s) de R$50,00")
print(f"{qn[2]} nota(s) de R$20,00")
print(f"{qn[3]} nota(s) de R$10,00")
print(f"{qn[4]} nota(s) de R$5,00")
print(f"{qn[5]} nota(s) de R$2,00")
print(f"{qn[6]} nota(s) de R$1,00")