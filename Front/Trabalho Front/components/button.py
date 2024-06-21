from tkinter import ttk

def create_button(parent, text, command, row, column, padx=20):
    button = ttk.Button(parent, text=text, command=command)
    button.grid(row=row, column=column, padx=padx)
    return button
