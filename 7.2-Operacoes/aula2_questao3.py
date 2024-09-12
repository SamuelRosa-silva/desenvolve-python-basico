import string

def preparar_frase(frase):
    #remove espaços e sinais de pontuação e converte para minúsculas
    frase = frase.lower()  #converte a frase para minúsculas
    frase = frase.translate(str.maketrans('', '', string.punctuation))  #remove sinais de pontuação
    frase = frase.replace(' ', '')  #remove espaços em branco
    return frase

def verificar_palindromo(frase):
    #prepara a frase
    frase_preparada = preparar_frase(frase)
    #verifica se a frase preparada é igual à sua versão invertida
    return frase_preparada == frase_preparada[::-1]

def main():
    while True:
        #solicita a frase do usuário
        frase = input("Digite uma frase (digite \"fim\" para encerrar): ")
        
        #verifica se o usuário deseja encerrar o programa
        if frase.lower() == "fim":
            break
        
        #verifica se a frase é um palíndromo
        if verificar_palindromo(frase):
            print(f"\"{frase}\" é palíndromo")
        else:
            print(f"\"{frase}\" não é palíndromo")

#executa o programa
main()
