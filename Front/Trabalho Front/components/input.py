from tkinter import ttk

def create_input(parent, row, column, padx=20):
    entry = ttk.Entry(parent)
    entry.grid(row=row, column=column, padx=padx)
    return entry
