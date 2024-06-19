from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from components.header import Header
from components.h1 import h1
from components.h2 import h2
from components.text import text

def roi_page(container, mostrar_pagina):
    frame = ttk.Frame(container)

    Header(frame, mostrar_pagina)

    h1(frame, "ROI")

    return frame