import tkinter as tk
from tkinter import ttk


def add_scroll_to_frame(parent, scrollspeed=35, r=0, c=0, rspan=1, cspan=1, grid={}, **kwargs):
    frame_container = tk.Frame(parent, **{'width':400, 'height':300, **kwargs})
    frame_container.grid(**{'row':r, 'column':c, 'rowspan':rspan, 'columnspan':cspan, 'sticky':'nswe', **grid})

    if {'width', 'height'} & set(kwargs):
        frame_container.grid_propagate(0)
    
    parent.grid_rowconfigure(r, weight=1)
    parent.grid_columnconfigure(c, weight=1)
    
    frame_container.grid_rowconfigure(0, weight=1)
    frame_container.grid_columnconfigure(0, weight=1)

    canvas = tk.Canvas(frame_container, bd=0, bg=frame_container['bg'], highlightthickness=0, yscrollincrement=scrollspeed)
    canvas.grid(row=0, column=0, sticky='nswe')
    
    frame = tk.Frame(canvas, **kwargs)
    frame_id = canvas.create_window((0, 0), window=frame, anchor="nw")
    
    vsb = tk.Scrollbar(frame_container, orient="vertical")
    vsb.grid(row=0, column=1, sticky='ns')
    vsb.configure(command=canvas.yview)
    
    canvas.configure(yscrollcommand=vsb.set)

    def on_canvas_configure(event):
        canvas.itemconfig(frame_id, width=event.width)

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    def on_mousewheel(event):
        canvas.yview_scroll(int(-event.delta / abs(event.delta)), 'units')

    canvas.bind("<Configure>", on_canvas_configure)
    frame.bind("<Configure>", on_frame_configure)
    canvas.bind('<Enter>', lambda e: canvas.bind_all('<MouseWheel>', on_mousewheel))
    canvas.bind('<Leave>', lambda e: canvas.unbind_all('<MouseWheel>'))

    return frame
