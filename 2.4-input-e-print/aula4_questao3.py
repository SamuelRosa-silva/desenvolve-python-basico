import match
np1 = input('Digite o nome do produto 1:')
vp1 = float(input('Digite o preço unitário do produto 1:'))
qp1= int(input('Digite a quantidade do produto 1:'))
np2 = input('Digite o nome do produto 2:')
vp2 = float(input('Digite o preço unitário do produto 2:'))
qp2= int(input('Digite a quantidade do produto 2:'))
np3 = input('Digite o nome do produto 3:')
vp3 = float(input('Digite o preço unitário do produto 3:'))
qp3= int(input('Digite a quantidade do produto 3:'))
pt = (vp1 * qp1) + (vp2 * qp2) + (vp3 * qp3)
print ('Total R$', (pt))