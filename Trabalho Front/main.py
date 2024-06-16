import tkinter as tk
from tkinter import ttk
from pages.login import login_page
from pages.roi import roi_page
from pages.desconto_acrescimo import desconto_acrescimo_page
from pages.juros_montante import juros_montante_page
from pages.lucro_prejuizo import lucro_prejuizo_page
from pages.mat_fin import mat_fin_page
from pages.porcentagem import porcentagem_page
from pages.vpl import vpl_page
from pages.tir import tir_page


# Interface gráfica com tkinter
root = tk.Tk()
root.title("Matemática financeira")


# Abre em fullscreen    
# root.state('zoomed')

# Container para as páginas
container = ttk.Frame(root)
container.pack(fill="both", expand=True)


def mostrar_pagina(page_name):
    # Função para mostrar a página solicitada
    frame = frames[page_name]
    frame.tkraise()
    

# Dicionário para armazenar as páginas
frames = {}
# Adicionar todas as páginas ao dicionário
# "Matemática Financeira", "Porcentagem", "Lucro / Prejuízo", "Juros / Montante", "Desconto / Acrescimo", "ROI", "VPL", "TIR"
frames["Login"] = login_page(container, mostrar_pagina)
frames["Matemática Financeira"] = mat_fin_page(container)
frames["Porcentagem"] = porcentagem_page(container)
frames["Lucro / Prejuízo"] = lucro_prejuizo_page(container)
frames["Juros / Montante"] = juros_montante_page(container)
frames["Desconto / Acrescimo"] = desconto_acrescimo_page(container)
frames["ROI"] = roi_page(container)
frames["VPL"] = vpl_page(container)
frames["TIR"] = tir_page(container)



# Mostrar a página inicial
mostrar_pagina("Login")



root.mainloop()