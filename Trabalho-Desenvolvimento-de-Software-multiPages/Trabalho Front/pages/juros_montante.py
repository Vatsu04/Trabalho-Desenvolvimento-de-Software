from tkinter import *
from tkinter import ttk
from components.header import Header
from components.h1 import h1


def juros_montante_page(container, mostrar_pagina):
    frame = ttk.Frame(container)
    
    Header(frame, mostrar_pagina)
    
    h1(frame, "Juros / Montante")
    
    return frame