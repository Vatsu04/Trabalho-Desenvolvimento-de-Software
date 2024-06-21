from tkinter import ttk

def create_label(parent, text, row, column, padx=20):
    font_tuple = ("Inter", 12)
    label = ttk.Label(parent, text=text, font=font_tuple)
    label.grid(row=row, column=column, padx=padx)
    return label
