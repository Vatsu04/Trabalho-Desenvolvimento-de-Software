import tkinter as tk
from tkinter import ttk

def calcular_acrescimo():
    try:
        preco_inicial = float(entry_preco_inicial.get())
        taxa_acrescimo = float(entry_taxa_acrescimo.get())
        acrescimo = preco_inicial * taxa_acrescimo
        preco_final = preco_inicial + acrescimo
        resultado.set(f"Valor do acréscimo: {acrescimo:.2f}\nPreço final: {preco_final:.2f}")
    except ValueError:
        resultado.set("Por favor, insira valores válidos.")

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de Acréscimo")

# Criar os widgets
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_preco_inicial = ttk.Label(frame, text="Preço Inicial:")
label_preco_inicial.grid(row=0, column=0, sticky=tk.W)

entry_preco_inicial = ttk.Entry(frame)
entry_preco_inicial.grid(row=0, column=1)

label_taxa_acrescimo = ttk.Label(frame, text="Taxa de Acréscimo (decimal):")
label_taxa_acrescimo.grid(row=1, column=0, sticky=tk.W)

entry_taxa_acrescimo = ttk.Entry(frame)
entry_taxa_acrescimo.grid(row=1, column=1)

button_calcular = ttk.Button(frame, text="Calcular", command=calcular_acrescimo)
button_calcular.grid(row=2, column=0, columnspan=2)

resultado = tk.StringVar()
label_resultado = ttk.Label(frame, textvariable=resultado)
label_resultado.grid(row=3, column=0, columnspan=2)

# Executar o loop principal da janela
root.mainloop()
