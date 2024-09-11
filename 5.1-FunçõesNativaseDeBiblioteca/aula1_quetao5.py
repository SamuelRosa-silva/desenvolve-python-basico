import emoji

#função para listar emojis
def listar_emojis():
    #lista de alguns emojis com seus códigos
    emojis = {
        '😀': ':grinning:',
        '😂': ':joy:',
        '❤️': ':heart:',
        '😎': ':sunglasses:',
        '👍': ':thumbsup:',
        '🎉': ':tada:',
        '🌟': ':star:',
        '🚀': ':rocket:',
        '😢': ':cry:',
        '😡': ':angry:'
    }
    
    print("Lista de Emojis e seus códigos:")
    for emoji_char, emoji_code in emojis.items():
        print(f"{emoji_char} - {emoji_code}")

#função principal do programa
def main():
    listar_emojis()

    #solicitar a frase codificada com emojis
    frase_codificada = input("Digite a frase codificada com emojis (ex: Olá mundo! :rocket: :star:): ")

    #decodificar a frase
    frase_decodificada = emoji.emojize(frase_codificada)

    print(f"Frase decodificada: {frase_decodificada}")

#executar o programa
if __name__ == "__main__":
    main()