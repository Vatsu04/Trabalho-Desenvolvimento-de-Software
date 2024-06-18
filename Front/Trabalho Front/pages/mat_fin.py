from tkinter import *
from tkinter import ttk
from components.header import Header
from components.h1 import h1
from components.h2 import h2
from components.text import text


def mat_fin_page(container, mostrar_pagina):
    frame = ttk.Frame(container)
    # frame.pack(fill="x")

    Header(frame, mostrar_pagina)

    h1(frame, "Matemática Financeira")
    h2(frame, "O que é Matemática Financeira?")
    text(frame, "Matemática Financeira é um ramo da matemática aplicada que estuda e aplica técnicas matemáticas para resolver problemas financeiros. Ela envolve a análise de investimentos, financiamentos, empréstimos, juros, amortizações e outros aspectos relacionados à gestão financeira.")
    
    return frame