import tkinter as tk
import random

# ==========ESTADO DO JOGO==========
opcoes = ["Pedra", "Papel", "Tesoura"]
vitorias = 0
derrotas = 0
empates = 0
round_atual = 1

# ==========FUNÇÕES DO JOGO==========
def jogar(escolha_jogador):
    global vitorias, derrotas, empates, round_atual
    escolha_computador = random.choice(opcoes)
    label_computador.config(
        text = f"🖥 Computador escolheu: {escolha_computador}"
    )
    if escolha_jogador == escolha_computador:
        empates += 1
        resultado = "----EMPATE----"
        cor = "#03fc8c"
    elif (
        (escolha_jogador == "Pedra" and escolha_computador == "Tesoura")
        or
        (escolha_jogador == "Tesoura" and escolha_computador == "Papel")
        or
        (escolha_jogador == "Papel" and escolha_computador == "Pedra")
    ):
        vitorias += 1
        resultado = "----VITÓRIA----"
        cor = "#03cefc"
    else:
        derrotas += 1
        resultado = "----DERROTA----"
        cor = "#d203fc"
    label_resultado.config(text=resultado, fg=cor)
    atualizar_placar()
    round_atual += 1
    label_round.config(text=f"ROUND {round_atual}")

def atualizar_placar():
    label_placar.config(
        text=f"🏆 Número de vitórias : {vitorias}   😑 Número de empates : {empates}    ☠  Número de derrotas : {derrotas}"
    )

def resetar_jogo():
    global vitorias, derrotas, empates, round_atual
    vitorias = 0
    derrotas = 0
    empates = 0
    round_atual = 1
    label_round.config(text="Round 1")
    label_resultado.config(text="",fg="black")
    label_computador.config(text="")
    atualizar_placar()

# ==========INTERFACE==========
janela = tk.Tk()
janela.title("=====JOGO=====\nPedra X Papel X Tesoura")
janela.geometry("420x380")
janela.resizable(False,False)
janela.configure(bg="#1e2b2e")

# [Título]
titulo = tk.Label(
    janela,
    text="Jogo do 💎 Pedra, 📄 Papel e ✂ Tesoura",
    font=("Arial", 16, "bold"),
    fg="white",
    bg = "#1e2b2e"
)
titulo.pack(pady=10)

# [Round]
label_round = tk.Label(
    janela,
    text= "Round 1",
    font= ("Arial", 12),
    fg= "#a29bfe",
    bg="#1e2b2e"
)
label_round.pack()

# [Placar]
label_placar = tk.Label(
    janela,
    text="🏆 0   😑 0   💀 0",
    font=("Arial", "14"),
    fg= "white",
    bg= "#1e2b2e"
)
label_placar.pack(pady=10)

# [Botões]
frame_botoes = tk.Frame(janela, bg="#1e2b2e")
frame_botoes.pack(pady=10)

def criar_botao(texto, escolha):
    return tk.Button(
        frame_botoes,
        text=texto,
        font=("Arial", 11),
        width= 10,
        command=lambda: jogar(escolha)
    )
criar_botao("💎 Pedra", "Pedra").grid(row=0, column=0, padx=5)
criar_botao("📄 Papel", "Papel").grid(row=0, column=1, padx=5)
criar_botao("✂ Tesoura", "Tesoura").grid(row=0, column=2, padx=5)

# [Escolha do computador]
label_computador = tk.Label(
    janela,
    text="",
    font=("Arial", 12),
    fg="white",
    bg="#1e2b2e"
)
label_computador.pack(pady=10)

# [Resultado]
label_resultado = tk.Label(
    janela,
    text="",
    font=("Arial", 16, "bold"),
    bg="#1e2b2e"
)
label_resultado.pack(pady=5)

# [Botão reset]
button_reset = tk.Button(
    janela,
    text="Foi bom jogar com você!! Até a próxima!! 🤗",
    font=("Arial",11),
    command=resetar_jogo()
)
button_reset.pack(pady=15)

# [Loop principal]
janela.mainloop()