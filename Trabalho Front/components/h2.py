from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def h2(container, titulo):
    frame = ttk.Frame(container)
    frame.pack()
    
    label = ttk.Label(frame, text=titulo)

    Font_tuple = ("Inter", 14, "bold")

    label.configure(font = Font_tuple)
    label.pack(pady=20, padx=10)