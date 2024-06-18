from tkinter import *
from tkinter import ttk
from components.header import Header



def mat_fin_page(container, mostrar_pagina):
    frame = ttk.Frame(container)
    # frame.pack(fill="x")
    label = ttk.Label(frame, text="Matmática Financeira")
    label.pack(pady=10, padx=10)

    Header(frame, mostrar_pagina)
    
    return frame