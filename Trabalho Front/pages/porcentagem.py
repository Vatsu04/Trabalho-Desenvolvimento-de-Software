from tkinter import *
from tkinter import ttk
from components.header import Header



def porcentagem_page(container, mostrar_pagina):
    frame = ttk.Frame(container)
 
    label = ttk.Label(frame, text="Porcentagem")
    label.pack(pady=10, padx=10)
    
    Header(frame, mostrar_pagina)
    
    return frame