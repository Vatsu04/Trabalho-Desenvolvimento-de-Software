import tkinter as tk
from tkinter import ttk


def add_scroll_to_frame(parent):
    canvas = tk.Canvas(parent)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    scrollable_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", tags="frame")
    # scrollable_frame.pack(fill=tk.BOTH, expand=True)

    # scrollable_frame.bind(
    #     "<Configure>",
    #     lambda e: canvas.configure(
    #         scrollregion=canvas.bbox("all")
    #     )
    # )
    
    
    canvas.bind_all("<MouseWheel>", lambda e: on_mousewheel(e, canvas=canvas))
    # canvas.bind("<Configure>", lambda e: onCanvasConfigure(e, canvas=canvas))



    return scrollable_frame

    
   

def on_mousewheel(event, canvas):
    shift = (event.state & 0x1) != 0
    scroll = -1 if event.delta > 0 else 1
    if shift:
        canvas.xview_scroll(scroll, "units")
    else:
        canvas.yview_scroll(scroll, "units")


def onCanvasConfigure(event, canvas):
    canvas.itemconfig('frame', height=canvas.winfo_height(), width=canvas.winfo_width())
    # print(canvas.winfo_width())

