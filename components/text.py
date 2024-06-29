from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def text(container, titulo):
    frame = ttk.Frame(container)
    frame.pack(fill="x", padx=10, pady=20)
    
    label = ttk.Label(frame, text=titulo, anchor="w", justify="left")

    Font_tuple = ("Inter", 12)

    label.configure(font = Font_tuple, wraplength=820)
    #label.pack(pady=10, padx=10)
    label.pack(fill="both", expand=True, padx=20, pady=5)
