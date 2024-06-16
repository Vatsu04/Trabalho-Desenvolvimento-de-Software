from tkinter import *
# from tkinter import tk
from tkinter import ttk
from components.header import Header



def tir_page(container, mostrar_pagina):
    frame = ttk.Frame(container)

    label = ttk.Label(frame, text="TIR")
    label.pack(pady=10, padx=10)
    
    Header(frame, mostrar_pagina)
    
    return frame


