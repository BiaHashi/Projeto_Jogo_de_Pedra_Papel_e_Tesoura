import random

opcoes = ["Pedra", "Papel", "Tesoura"]
vitorias = 0
derrotas = 0
empates = 0
round_atual = 1

def atualizar_placar(): # Mostra o placar em seu estado atual
    print("="*10)
    print("PLACAR")
    print(f"🏆 Número de vitórias : {vitorias} vitórias 🎉")
    print(f"😎 Número de empates : {empates} empates 🤩")
    print(f"☠  Número de derrotas : {derrotas} derrotas 💩")
    print("="*10)

def resetar_jogo(): # Reinicia o jogo
    global vitorias, derrotas, empates, round_atual
    vitorias = 0
    derrotas = 0
    empates = 0
    round_atual = 1
    atualizar_placar()
    print("\nJogo reiniciado 🔁")

def jogar(escolha_jogador): # Decide o resultado da partida
    global vitorias, derrotas, empates, round_atual
    escolha_computador = random.choice(opcoes)
    print("="*15,f"ROUND {round_atual}","="*15)
    print("Você escolheu: ", escolha_jogador)
    print("Computador escolheu: ", escolha_computador)
    print("Resultado do jogo:\n.\n.\n.")
    if escolha_jogador == escolha_computador:
        empates += 1
        print("----EMPATE----")
    elif (
        (escolha_jogador == "Pedra" and escolha_computador == "Tesoura")
        or
        (escolha_jogador == "Tesoura" and escolha_computador == "Papel")
        or
        (escolha_jogador == "Papel" and escolha_computador == "Pedra")
    ):
        vitorias += 1
        print("----VITÓRIA----")
    else:
        derrotas += 1
        print("----DERROTA----")
    round_atual += 1
    atualizar_placar()
while True:
    print("="*20,"ROUND","="*20)
    print("[1] - 💎 Pedra")
    print("[2] - 📄 Papel")
    print("[3] - ✂ Tesoura")
    print("[4] - 🔁 Reiniciar Jogo")
    print("[0] - 🕳  Sair")

    opcao = input("\nEcolha uma opção para jogar 🎮: ")

    if opcao == "1":
        jogar("Pedra")
    elif opcao == "2":
        jogar("Papel")
    elif opcao == "3":
        jogar("Tesoura")
    elif opcao == "4":
        resetar_jogo()
    elif opcao == "0":
        print("Foi bom jogar com você!! Até a próxima!! 🤗")
    else:
        print("Ops!! Parece que essa opção não existe no sistema 😕. Tente novamente com as opções indicadas:")