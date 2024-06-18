from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def text(container, titulo):
    frame = ttk.Frame(container)
    frame.pack()
    
    label = ttk.Label(frame, text=titulo)

    Font_tuple = ("Inter", 12)

    label.configure(font = Font_tuple, wraplength=850)
    label.pack(pady=10, padx=10)