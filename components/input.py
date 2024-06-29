import ttkbootstrap as ttk

def create_input(parent, row, column, padx=20):
    entry = ttk.Entry(parent, bootstyle="success")
    entry.grid(row=row, column=column, padx=padx)
    return entry
