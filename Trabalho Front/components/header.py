from tkinter import ttk
from tkinter import *
from tkinter import font




def createButton(root, texts):
    frame = ttk.Frame(root)
    frame.pack(side=TOP)
    
    for index, text in enumerate(texts):
        button = ttk.Button(frame, text=text, height=2, borderwidth=0, font=font.Font(weight='bold'))
        # button.pack()
        changeOnHover(button)
        # button.grid(row=0, column=(index * 2))
        button.pack(side=LEFT)
        
        root.columnconfigure((1 if index == 0 else ((index * 2) + 1)), weight=1, minsize=10)
    
    return frame
        
    
def Header(root):
    return createButton(root, ("Matemática Financeira", "Matemática Financeira", "Porcentagem", "Lucro / Prejuízo", "Juros / Montante", "Desconto / Acrescimo", "ROI", "VPL", "TIR"))
    

def changeOnHover(button):
    button.bind("<Enter>", func=lambda e: button.config(foreground="red"))

    button.bind("<Leave>", func=lambda e: button.config(foreground="black"))