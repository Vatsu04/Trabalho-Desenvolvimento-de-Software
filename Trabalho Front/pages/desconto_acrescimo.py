from tkinter import *
from tkinter import ttk
from components.header import Header



def desconto_acrescimo_page(container, mostrar_pagina):
    frame = ttk.Frame(container)

    label = ttk.Label(frame, text="Desconto / Acréscimo")
    label.pack(pady=10, padx=10)
    
    Header(frame, mostrar_pagina)
    
    return frame