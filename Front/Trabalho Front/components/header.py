import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# from ..main import mostrar_pagina



# def createButton(container, mostrar_pagina, texts):
#     frame = ttk.Frame(container)
#     frame.pack()
    
#     # for index, text in enumerate(texts):
#     button = ttk.Button(frame, text="Matemática Financeira", bootstyle="link", command=lambda e: mostrar_pagina("Matemática Financeira"))
#     button.pack(side=LEFT)
    
#     button = ttk.Button(frame, text="Porcentagem", bootstyle="link", command=lambda e: mostrar_pagina("Porcentagem"))
#     button.pack(side=LEFT)
    
#     button = ttk.Button(frame, text="Lucro / Prejuízo", bootstyle="link", command=lambda e: mostrar_pagina("Lucro / Prejuízo"))
#     button.pack(side=LEFT)
    
#     button = ttk.Button(frame, text="Juros / Montante", bootstyle="link", command=lambda e: mostrar_pagina("Juros / Montante"))
#     button.pack(side=LEFT)
    
#     button = ttk.Button(frame, text="Desconto / Acrescimo", bootstyle="link", command=lambda e: mostrar_pagina("Desconto / Acrescimo"))
#     button.pack(side=LEFT)
    
#     button = ttk.Button(frame, text="ROI", bootstyle="link", command=lambda e: mostrar_pagina("ROI"))
#     button.pack(side=LEFT)
    
#     button = ttk.Button(frame, text="VPL", bootstyle="link", command=lambda e: mostrar_pagina("VPL"))
#     button.pack(side=LEFT)
    
#     button = ttk.Button(frame, text="TIR", bootstyle="link", command=lambda e: mostrar_pagina("TIR"))
#     button.pack(side=LEFT)
    

#     return frame


def Header(container, mostrar_pagina):
    frame = ttk.Frame(container)
    frame.pack(side=tk.TOP, expand=1)
    
    # for index, text in enumerate(texts):
    button = ttk.Button(frame, text="Matemática Financeira", bootstyle="link", command=lambda: mostrar_pagina("Matemática Financeira"))
    button.pack(side=LEFT)
    
    button = ttk.Button(frame, text="Porcentagem", bootstyle="link", command=lambda: mostrar_pagina("Porcentagem"))
    button.pack(side=LEFT)
    
    button = ttk.Button(frame, text="Lucro / Prejuízo", bootstyle="link", command=lambda: mostrar_pagina("Lucro / Prejuízo"))
    button.pack(side=LEFT)
    
    button = ttk.Button(frame, text="Juros / Montante", bootstyle="link", command=lambda: mostrar_pagina("Juros / Montante"))
    button.pack(side=LEFT)
    
    button = ttk.Button(frame, text="Desconto / Acrescimo", bootstyle="link", command=lambda: mostrar_pagina("Desconto / Acrescimo"))
    button.pack(side=LEFT)
    
    button = ttk.Button(frame, text="ROI", bootstyle="link", command=lambda: mostrar_pagina("ROI"))
    button.pack(side=LEFT)
    
    button = ttk.Button(frame, text="VPL", bootstyle="link", command=lambda: mostrar_pagina("VPL"))
    button.pack(side=LEFT)
    
    button = ttk.Button(frame, text="TIR", bootstyle="link", command=lambda: mostrar_pagina("TIR"))
    button.pack(side=LEFT)
    # return createButton(container, mostrar_pagina, ("Matemática Financeira", "Porcentagem", "Lucro / Prejuízo", "Juros / Montante", "Desconto / Acrescimo", "ROI", "VPL", "TIR"))
    
