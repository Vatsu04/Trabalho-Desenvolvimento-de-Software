import tkinter as tk
from tkinter import ttk
from pages.login import login_page
from pages.roi import ROIPage


# Interface gráfica com tkinter
root = tk.Tk()
root.title("Matemática financeira")

# Container para as páginas
container = ttk.Frame(root)
container.pack(fill="both", expand=True)


def mostrar_pagina(page_name):
    # Função para mostrar a página solicitada
    frame = frames[page_name]
    frame.tkraise()
    

# Dicionário para armazenar as páginas
frames = {}
# "Matemática Financeira", "Matemática Financeira", "Porcentagem", "Lucro / Prejuízo", "Juros / Montante", "Desconto / Acrescimo", "ROI", "VPL", "TIR"
# Adicionar todas as páginas ao dicionário
frames["ROI"] = ROIPage(container)
frames["Login"] = login_page(container, mostrar_pagina)


# Abre em fullscreen    
# root.state('zoomed')



# frames["framesecundaria"] = criar_pagina_secundaria(container)

# Mostrar a página inicial
mostrar_pagina("Login")



root.mainloop()