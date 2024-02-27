import random


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    # enquanto True
    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        imprime_mensagem_de_vencedor()
    else:
        imprime_mensagem_de_perdedor(palavra_secreta)


def imprime_mensagem_de_vencedor():
    print("Parabens, Você ganhou!")


    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("Fim do jogo")


def imprime_mensagem_de_perdedor(palavra_secreta):
    print("Puxa, Você foi enforcado!")
    print(f"A palavra era {palavra_secreta}!")

    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

    print("Fim do jogo")


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute.upper() == letra.upper():
            letras_acertadas[index] = letra
        index = index + 1


def pede_chute():
    chute = input("Qual letra ")
    chute = chute.strip().upper()
    return chute


def inicializa_letras_acertadas(palavra):
    return ["_" for _ in palavra]


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo no jogo de forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if __name__ == "__main__":
    jogar()
