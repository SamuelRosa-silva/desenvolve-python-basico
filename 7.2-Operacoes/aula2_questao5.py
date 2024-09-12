import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) <= 2:
            return palavra  #palavras com 2 ou menos letras não são modificadas
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        return palavra[0] + ''.join(meio) + palavra[-1]
    
    palavras = frase.split()  #divide a frase em palavras
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    return ' '.join(palavras_embaralhadas)

#solicita a frase do usuário
entrada_usuario = input("Digite uma frase: ")
resultado = embaralhar_palavras(entrada_usuario)
print("Frase modificada:", resultado)
