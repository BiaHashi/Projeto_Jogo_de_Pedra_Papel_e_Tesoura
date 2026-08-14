import random
random.randint(1,10)

opcoes = ["Pedra", "Papel", "Tesoura"]


def jogar(escolha_jogador):
    print("Resultado do jogo:\n.\n.\n.")
    escolha_computador = random.choice(opcoes)
    print("Você: ", escolha_jogador)
    print("Computador: ", escolha_computador)
    if escolha_jogador == escolha_computador:
        print("----DEU EMPATE----")
    elif (
        (escolha_jogador == "Pedra" and escolha_computador == "Tesoura")
        or
        (escolha_jogador == "Tesoura" and escolha_computador == "Papel")
        or
        (escolha_jogador == "Papel" and escolha_computador == "Pedra")
    ):
        print("----VOCÊ VENCEU----")
    else:
        print("----VOCÊ PERDEU----")

jogar("Tesoura")
"""
def jogar():
    print("Resultado do jogo:\n.\n.\n.")
    escolha_computador = random.choice(opcoes)
    escolha_computador02 = random.choice(opcoes)
    print("Computador 1: ", escolha_computador)
    print("Computador 2: ", escolha_computador02)
    if escolha_computador == escolha_computador02:
        print("----EMPATE ENTRE COMPUTADORES----")
    elif (
        (escolha_computador == "Pedra" and escolha_computador02 == "Tesoura")
        or
        (escolha_computador == "Tesoura" and escolha_computador02 == "Papel")
        or
        (escolha_computador == "Papel" and escolha_computador02 == "Pedra")
    ):
        print("----COMPUTADOR 1 VENCEU----")
    else:
        print("----COMPUTADOR 2 VENCEU----")
jogar()
"""