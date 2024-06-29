## Botão padrão
# from tkinter import ttk

# def create_button(parent, text, command, row, column, padx=20):
#     button = ttk.Button(parent, text=text, command=command)
#     button.grid(row=row, column=column, padx=padx)
#     return button

## Botão gradiente

from tkinter import *

def create_button(parent, text, command, row, column, padx=20, pady=10,image_path=None):
    if image_path is None:
        image_path = "Front\Trabalho Front\components\gradiente-button.png"
    try:
        # Carrega a imagem usando PhotoImage
        image = PhotoImage(file=image_path)
        button = Button(parent, text=text, command=command, image=image, compound='center')
        button.image = image
    except Exception:
        # Volta para um botão sem imagem se houver erro
        button = Button(parent, text=text, command=command)

    button.grid(row=row, column=column, padx=padx, pady=pady)
    return button