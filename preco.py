import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def validar_entrada(input):
    """
    Valida a entrada para permitir apenas números e pontos.
    """
    if input.isdigit():
        return True
    elif input.count('.') == 1 and all(char.isdigit() or char == '.' for char in input):
        return True
    elif input == "":
        return True
    else:
        return False

def calcular_acrescimo(preco_inicial, taxa_acrescimo):
    """
    Calcula o valor do acréscimo e o preço novo.

    Args:
    - preco_inicial (float): O preço inicial do produto ou serviço.
    - taxa_acrescimo (float): A taxa de acréscimo (em decimal).

    Returns:
    - tuple: Uma tupla contendo o valor do acréscimo e o preço novo.
    """
    acrescimo = preco_inicial * taxa_acrescimo
    preco_novo = preco_inicial + acrescimo
    return acrescimo, preco_novo

def calcular_desconto(preco_inicial, taxa_desconto):
    """
    Calcula o valor do desconto e o preço novo.

    Args:
    - preco_inicial (float): O preço inicial do produto ou serviço.
    - taxa_desconto (float): A taxa de desconto (em decimal).

    Returns:
    - tuple: Uma tupla contendo o valor do desconto e o preço novo.
    """
    desconto = preco_inicial * taxa_desconto
    preco_novo = preco_inicial - desconto
    return desconto, preco_novo

def calcular(tipo):
    preco_inicial = entry_preco_inicial.get()
    taxa = entry_taxa.get()

    # Verificar se os campos estão preenchidos
    if preco_inicial == "" or taxa == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    # Validar os campos de entrada
    if not validar_entrada(preco_inicial) or not validar_entrada(taxa):
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
        return

    # Converter para float
    preco_inicial = float(preco_inicial)
    taxa = float(taxa)

    # Calcular
    if tipo == "acrescimo":
        resultado = calcular_acrescimo(preco_inicial, taxa)
        resultado_texto = f"Valor do acréscimo: {resultado[0]:.2f}\nPreço novo: {resultado[1]:.2f}"
    elif tipo == "desconto":
        resultado = calcular_desconto(preco_inicial, taxa)
        resultado_texto = f"Valor do desconto: {resultado[0]:.2f}\nPreço novo: {resultado[1]:.2f}"
    resultado_var.set(resultado_texto)

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de Acréscimo e Desconto")

# Disable resizing of the window
root.resizable(False, False)

# Set a fixed size for the window
root.geometry("300x150")

# Calculate the position for the window to appear at the center
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 400) // 2
y = (screen_height - 200) // 2

# Set the position for the window
root.geometry("+{}+{}".format(x, y))

# Criar os widgets
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_preco_inicial = ttk.Label(frame, text="Preço Inicial:")
label_preco_inicial.grid(row=0, column=0, sticky=tk.W)

entry_preco_inicial = ttk.Entry(frame)
entry_preco_inicial.grid(row=0, column=1)

label_taxa = ttk.Label(frame, text="Taxa (decimal):")
label_taxa.grid(row=1, column=0, sticky=tk.W)

entry_taxa = ttk.Entry(frame)
entry_taxa.grid(row=1, column=1)

resultado_var = tk.StringVar()
label_resultado = ttk.Label(frame, textvariable=resultado_var)
label_resultado.grid(row=3, column=0, columnspan=2)

button_calcular_acrescimo = ttk.Button(frame, text="Calcular Acréscimo", command=lambda: calcular("acrescimo"))
button_calcular_acrescimo.grid(row=2, column=0)

button_calcular_desconto = ttk.Button(frame, text="Calcular Desconto", command=lambda: calcular("desconto"))
button_calcular_desconto.grid(row=2, column=1)

# Configurar validação de entrada para aceitar apenas números e pontos
validacao_numerica = frame.register(validar_entrada)
entry_preco_inicial.config(validate="key", validatecommand=(validacao_numerica, "%P"))
entry_taxa.config(validate="key", validatecommand=(validacao_numerica, "%P"))

# Place the elements in the center of the window
frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

# Executar o loop principal da janela
root.mainloop()
