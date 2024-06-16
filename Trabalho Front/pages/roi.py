# import tkinter as tk
from tkinter import *
from tkinter import ttk
# from components.header import buildHeader







def ROIPage(container):
    frame = ttk.Frame(container)
    frame.grid(row=0, column=0, sticky="nsew")

    # buildHeader(root, '')

    label = ttk.Label(frame, text="Página 2")
    label.pack(pady=10, padx=10)
    
    return frame

    # button = tk.Button(frame, text="Voltar para a Página Inicial",
    #                     command=lambda: controller.show_frame("MainPage"))
    # button.pack()