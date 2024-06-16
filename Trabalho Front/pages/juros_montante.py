from tkinter import *
from tkinter import ttk
from components.header import Header



def juros_montante_page(container, mostrar_pagina):
    frame = ttk.Frame(container)

    label = ttk.Label(frame, text="Juros / Montante")
    label.pack(pady=10, padx=10)
    
    Header(frame, mostrar_pagina)
    
    return frame