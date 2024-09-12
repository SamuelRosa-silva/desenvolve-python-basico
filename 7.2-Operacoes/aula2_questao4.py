import string

def validador_senha(senha):
    #verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    
    #inicializa as flags
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_caracter_especial = False

    #define os caracteres especiais permitidos
    caracteres_especiais = string.punctuation

    #verifica cada caractere da senha
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in caracteres_especiais:
            tem_caracter_especial = True
    
    #verifica se todos os critérios foram atendidos
    return tem_maiuscula and tem_minuscula and tem_numero and tem_caracter_especial

#exemplos de uso
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))
print(validador_senha(senha2))
print(validador_senha(senha3))  
