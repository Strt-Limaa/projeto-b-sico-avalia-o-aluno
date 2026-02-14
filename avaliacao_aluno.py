from sklearn import tree
import tkinter as tk

# ===== DADOS =====
x = [
    [9,6,14,95,9], [6,34,7,65,8], [10,0,25,100,10], [3,70,3,40,1],
    [7,20,10,75,7], [4,75,7,50,5], [9,10,17,95,9], [1,120,0,10,0],
    [8,12,12,65,10], [6,70,7,70,6], [3,40,4,50,6], [5,60,4,70,5],
    [8,25,10,80,10], [5,5,10,55,5], [7,50,10,50,6], [6,69,5,65,6],
    [5,70,4,64,5], [9,10,9,85,8], [9,11,9,84,7], [2,45,0,30,4],
    [6,50,10,64,8], [7,71,12,78,8], [5,80,6,55,4], [8,8,15,90,8],
    [4,90,2,40,2], [9,2,20,100,10], [7,17,17,17,10], [10,68,6,80,5],
    [3,100,2,20,1], [8,5,18,85,9], [6,60,8,60,6], [7,30,12,75,7]
]

y_passar = [
    1,1,1,0,1,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,
    0,0,0,1,0,1,0,0,1,1,1,1
]

y_tipoaluno = [
    2,1,2,0,1,0,2,0,1,1,0,0,1,0,1,1,0,2,1,0,
    1,1,0,2,0,2,0,0,2,1,1,2
]

y_advertencia = [
    0,1,0,1,0,1,0,1,0,0,1,1,0,1,1,1,1,0,0,1,
    1,1,1,0,1,0,1,1,0,0,1,0
]

# ===== MODELOS =====
model_passar = tree.DecisionTreeClassifier()
model_passar.fit(x, y_passar)

model_tipo = tree.DecisionTreeClassifier()
model_tipo.fit(x, y_tipoaluno)

model_advertencia = tree.DecisionTreeClassifier()
model_advertencia.fit(x, y_advertencia)

# ===== TKINTER =====
janela = tk.Tk()
janela.title("Avaliação Final")
janela.geometry("500x500")
janela.configure(bg="#f0f0f0")

# Título
tk.Label(janela, text="Sistema de Avaliação de Alunos", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# Frame para inputs
frame_inputs = tk.Frame(janela, bg="#f0f0f0")
frame_inputs.pack(pady=10)

# Labels e Entradas
tk.Label(frame_inputs, text="Média Final:", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
entrada_media = tk.Entry(frame_inputs)
entrada_media.grid(row=0, column=1)

tk.Label(frame_inputs, text="Faltas:", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
entrada_faltas = tk.Entry(frame_inputs)
entrada_faltas.grid(row=1, column=1)

tk.Label(frame_inputs, text="Horas de estudo/semana:", bg="#f0f0f0").grid(row=2, column=0, sticky="w")
entrada_horas = tk.Entry(frame_inputs)
entrada_horas.grid(row=2, column=1)

tk.Label(frame_inputs, text="% Trabalhos entregues:", bg="#f0f0f0").grid(row=3, column=0, sticky="w")
entrada_trabalhos = tk.Entry(frame_inputs)
entrada_trabalhos.grid(row=3, column=1)

tk.Label(frame_inputs, text="Nota de comportamento:", bg="#f0f0f0").grid(row=4, column=0, sticky="w")
entrada_comportamento = tk.Entry(frame_inputs)
entrada_comportamento.grid(row=4, column=1)

# Labels de resultado
label_situacao = tk.Label(janela, text="", font=("Arial", 12, "bold"), fg="blue", bg="#f0f0f0")
label_situacao.pack(pady=5)
label_tipo = tk.Label(janela, text="", font=("Arial", 12, "bold"), fg="green", bg="#f0f0f0")
label_tipo.pack(pady=5)
label_advertencia = tk.Label(janela, text="", font=("Arial", 12, "bold"), fg="red", bg="#f0f0f0")
label_advertencia.pack(pady=5)

# Função de avaliação
def avaliar_aluno():
    try:
        media = int(entrada_media.get())
        faltas = int(entrada_faltas.get())
        horas = int(entrada_horas.get())
        trabalhos = int(entrada_trabalhos.get())
        comportamento = int(entrada_comportamento.get())

        aluno = [[media, faltas, horas, trabalhos, comportamento]]

        passar = model_passar.predict(aluno)
        tipo = model_tipo.predict(aluno)
        advertencia = model_advertencia.predict(aluno)

        resultado_passar = "Aprovado" if passar[0] == 1 else "Reprovado"
        tipos = {0: "Um dos piores alunos", 1: "Aluno normal", 2: "Um dos melhores alunos"}
        resultado_tipo = tipos[tipo[0]]
        resultado_advertencia = "Recebe advertência" if advertencia[0] == 1 else "Não recebe advertência"

        label_situacao.config(text="Situação: " + resultado_passar)
        label_tipo.config(text="Tipo de aluno: " + resultado_tipo)
        label_advertencia.config(text="Advertência: " + resultado_advertencia)

    except ValueError:
        label_situacao.config(text="Digite apenas números válidos")
        label_tipo.config(text="")
        label_advertencia.config(text="")

# Botão
botao_calcular = tk.Button(janela, text="Calcular Resultado", font=("Arial", 12, "bold"), command=avaliar_aluno)
botao_calcular.pack(pady=10)

entrada_media.bind("<Return>", lambda event: entrada_faltas.focus_set())
entrada_faltas.bind("<Return>", lambda event: entrada_horas.focus_set())
entrada_horas.bind("<Return>", lambda event: entrada_trabalhos.focus_set())
entrada_trabalhos.bind("<Return>", lambda event: entrada_comportamento.focus_set())
entrada_comportamento.bind("<Return>", lambda event: botao_calcular.focus_set())


janela.mainloop()