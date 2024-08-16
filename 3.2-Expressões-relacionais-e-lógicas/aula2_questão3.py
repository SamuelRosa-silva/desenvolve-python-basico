id=int(input('Qual a sua idade? ')) #input para coletar idade
jj=input('Você já jogou pelo menos 3 jogos de tabuleiro? responda com True ou False').lower() == 'true' #pergunta para requisitos
jg=int(input('Quantas vezes você venceu um jogo de tabuleiro? '))#pergunta para requisitos
if 16 <= id <= 18 and jj and jg >= 1: #estrutura de compração
    print(True)
else:
    print(False)
