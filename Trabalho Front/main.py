import tkinter as tk
import ttkbootstrap as ttk
from pages.login import login_page
from pages.roi import roi_page
from pages.desconto_acrescimo import desconto_acrescimo_page
from pages.juros_montante import juros_montante_page
from pages.lucro_prejuizo import lucro_prejuizo_page
from pages.mat_fin import mat_fin_page
from pages.porcentagem import porcentagem_page
from pages.vpl import vpl_page
from pages.tir import tir_page
from components.scrollable_frame import add_scroll_to_frame



root = ttk.Window()
root.title("Matemática financeira")
root.geometry("900x600")
root.resizable(True, True)
root.minsize(width=900, height=600)
root.maxsize(width=1000, height=800)
style = ttk.Style("solar")

# Abre em fullscreen    
root.state('zoomed')

# Container para as páginas
container = ttk.Frame(root)
container.pack(fill="both", expand=True)


def bind_mouse_wheel(root, canvas):
    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))
    canvas.bind_all("<Button-4>", lambda event: canvas.yview_scroll(-1, "units"))  # Linux specific
    canvas.bind_all("<Button-5>", lambda event: canvas.yview_scroll(1, "units"))   # Linux specific


def mostrar_pagina(page_name):
    # Função para mostrar a página solicitada
    frame = frames[page_name]
    frame.tkraise()
    
    current_canvas = frame.winfo_children()[0]

    bind_mouse_wheel(root, current_canvas)
    

# Dicionário para armazenar as páginas
frames = {}
# Adicionar todas as páginas ao dicionário
# "Matemática Financeira", "Porcentagem", "Lucro / Prejuízo", "Juros / Montante", "Desconto / Acrescimo", "ROI", "VPL", "TIR"
frames["Login"] = login_page(container, mostrar_pagina)
frames["Matemática Financeira"] = mat_fin_page(container, mostrar_pagina, add_scroll_to_frame)
frames["Porcentagem"] = porcentagem_page(container, mostrar_pagina, add_scroll_to_frame)
frames["Lucro / Prejuízo"] = lucro_prejuizo_page(container, mostrar_pagina, add_scroll_to_frame)
frames["Juros / Montante"] = juros_montante_page(container, mostrar_pagina, add_scroll_to_frame)
frames["Desconto / Acrescimo"] = desconto_acrescimo_page(container, mostrar_pagina, add_scroll_to_frame)
frames["ROI"] = roi_page(container, mostrar_pagina, add_scroll_to_frame)
frames["VPL"] = vpl_page(container, mostrar_pagina, add_scroll_to_frame)
frames["TIR"] = tir_page(container, mostrar_pagina, add_scroll_to_frame)


for frame in frames.values():
    frame.grid(row=0, column=0, sticky="nsew")
    
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Mostrar a página inicial
mostrar_pagina("Login")

root.mainloop()