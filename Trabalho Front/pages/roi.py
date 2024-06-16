from tkinter import *
from tkinter import ttk
from components.header import Header



def roi_page(container, mostrar_pagina):
    frame = ttk.Frame(container)
    
    label = ttk.Label(frame, text="ROI")
    label.pack(pady=10, padx=10)
    
    Header(frame, mostrar_pagina)

    
    return frame