from tkinter import *
from tkinter import ttk



def roi_page(container):
    frame = ttk.Frame(container)
    frame.grid(row=0, column=0, sticky="nsew")


    label = ttk.Label(frame, text="ROI")
    label.pack(pady=10, padx=10)
    
    return frame