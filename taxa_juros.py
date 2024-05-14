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

def taxa_juros_para_decimal(taxa_percentual):
    """
    Converte uma taxa de juros de percentual para decimal.

    Args:
    - taxa_percentual (float): A taxa de juros em percentual.

    Returns:
    - float: A taxa de juros em decimal.
    """
    taxa_decimal = taxa_percentual / 100
    return taxa_decimal

def taxa_juros_para_percentual(taxa_decimal):
    """
    Converte uma taxa de juros de decimal para percentual.

    Args:
    - taxa_decimal (float): A taxa de juros em decimal.

    Returns:
    - float: A taxa de juros em percentual.
    """
    taxa_percentual = taxa_decimal * 100
    return taxa_percentual

def calcular_montante(capital, taxa_juros, tempo):
    """
    Calcula o montante de um investimento.

    Args:
    - capital (float): O capital inicial do investimento.
    - taxa_juros (float): A taxa de juros (em decimal).
    - tempo (int): O tempo em anos.

    Returns:
    - float: O montante do investimento.
    """
    montante = capital * (1 + taxa_juros) ** tempo
    return montante

def calcular():
    capital_inicial = entry_capital.get()
    taxa_juros = entry_taxa_juros.get()
    tempo = entry_tempo.get()

    # Verificar se os campos estão preenchidos
    if capital_inicial == "" or taxa_juros == "" or tempo == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    # Validar os campos de entrada
    if not validar_entrada(capital_inicial) or not validar_entrada(taxa_juros) or not tempo.isdigit():
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
        return

    # Converter para float
    capital_inicial = float(capital_inicial)
    taxa_juros = float(taxa_juros)
    tempo = int(tempo)

    # Calcular o montante
    montante = calcular_montante(capital_inicial, taxa_juros, tempo)
    resultado_var.set(f"Montante: {montante:.2f}")

def converter_para_decimal():
    taxa_percentual = entry_taxa_juros.get()
    if validar_entrada(taxa_percentual):
        taxa_percentual = float(taxa_percentual)
        taxa_decimal = taxa_juros_para_decimal(taxa_percentual)
        resultado_var.set(f"Taxa de juros em decimal: {taxa_decimal:.4f}")
    else:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para a taxa de juros.")

def converter_para_percentual():
    taxa_decimal = entry_taxa_juros.get()
    if validar_entrada(taxa_decimal):
        taxa_decimal = float(taxa_decimal)
        taxa_percentual = taxa_juros_para_percentual(taxa_decimal)
        resultado_var.set(f"Taxa de juros em percentual: {taxa_percentual:.2f}%")
    else:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para a taxa de juros.")

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de Montante")

# Disable resizing of the window
root.resizable(False, False)

# Set a fixed size for the window
root.geometry("300x250")

# Calculate the position for the window to appear at the center
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 300) // 2
y = (screen_height - 250) // 2

# Set the position for the window
root.geometry("+{}+{}".format(x, y))

# Criar os widgets
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_capital = ttk.Label(frame, text="Capital Inicial:")
label_capital.grid(row=0, column=0, sticky=tk.W)

entry_capital = ttk.Entry(frame)
entry_capital.grid(row=0, column=1)

label_taxa_juros = ttk.Label(frame, text="Taxa de Juros:")
label_taxa_juros.grid(row=1, column=0, sticky=tk.W)

entry_taxa_juros = ttk.Entry(frame)
entry_taxa_juros.grid(row=1, column=1)

label_tempo = ttk.Label(frame, text="Tempo (anos):")
label_tempo.grid(row=2, column=0, sticky=tk.W)

entry_tempo = ttk.Entry(frame)
entry_tempo.grid(row=2, column=1)

resultado_var = tk.StringVar()
label_resultado = ttk.Label(frame, textvariable=resultado_var)
label_resultado.grid(row=4, column=0, columnspan=2)

button_calcular = ttk.Button(frame, text="Calcular Montante", command=calcular)
button_calcular.grid(row=3, column=0, columnspan=2)

button_converter_decimal = ttk.Button(frame, text="Converter para Decimal", command=converter_para_decimal)
button_converter_decimal.grid(row=5, column=0, columnspan=2)

button_converter_percentual = ttk.Button(frame, text="Converter para Percentual", command=converter_para_percentual)
button_converter_percentual.grid(row=6, column=0, columnspan=2)

# Configurar validação de entrada para aceitar apenas números e pontos
validacao_numerica = frame.register(validar_entrada)
entry_capital.config(validate="key", validatecommand=(validacao_numerica, "%P"))
entry_taxa_juros.config(validate="key", validatecommand=(validacao_numerica, "%P"))
entry_tempo.config(validate="key", validatecommand=(validacao_numerica, "%P"))

# Place the elements in the center of the window
frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

# Executar o loop principal da janela
root.mainloop()
