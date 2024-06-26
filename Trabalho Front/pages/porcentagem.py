from tkinter import *
from tkinter import ttk
from components.header import Header
from components.h1 import h1
from components.h2 import h2
from components.text import text
from components.label import create_label
from components.input import create_input
from components.button import create_button
from funcoes import porcentagem

def porcentagem_page(container, mostrar_pagina, add_scroll_to_frame):
    frame = ttk.Frame(container)
    scrollable_frame = add_scroll_to_frame(frame)

    Header(scrollable_frame, mostrar_pagina)

    h1(scrollable_frame, "Cálculo de Porcentagem")

    input_container_1 = ttk.Frame(scrollable_frame)
    input_container_2 = ttk.Frame(scrollable_frame)
    
    input_container_1.pack(expand=1, pady=10)
    input_container_2.pack(expand=1, pady=(10, 100))
    
    create_label(input_container_1, "Valor: ", 0, 0) 
    valor_entry = create_input(input_container_1, 1, 0)

    create_label(input_container_1, "Porcentagem (%): ", 0, 1)
    porcentagem_entry = create_input(input_container_1, 1, 1)

    response_text = create_label(input_container_2, "Resultado: R$0,00", 0, 0)
    create_button(input_container_2, "CALCULAR", row=0, column=1, command=lambda: porcentagem(valor_entry.get(), porcentagem_entry.get(), response_text))

    text_container = ttk.Frame(scrollable_frame)
    text_container.pack()

    text(text_container, "A calculadora de porcentagem é uma ferramenta simples utilizada para calcular a porcentagem de um valor em relação a outro. Ela é amplamente utilizada em diversas áreas, como finanças pessoais, matemática, e estudos de mercado.")

    h2(text_container, "Como Calcular Porcentagem?")

    text(text_container, "Para calcular a porcentagem de um valor em relação a outro, utiliza-se a fórmula:\n\nPorcentagem = (Valor * Porcentagem%) / 100\n\nOnde:\n\n- Valor é o valor base;\n- Porcentagem% é a porcentagem que se deseja calcular sobre o valor base.")

    h2(text_container, "Interpretação do Resultado")

    text(text_container, "O resultado obtido representa a quantidade correspondente ao percentual calculado em relação ao valor base.")

    h2(text_container, "Considerações Adicionais")

    text(text_container, "É importante utilizar corretamente a unidade percentual (o símbolo %) ao inserir os valores de entrada para obter resultados precisos.")

    h2(text_container, "Conclusão")

    text(text_container, "A calculadora de porcentagem é uma ferramenta útil e prática para realizar cálculos rápidos e precisos relacionados a percentuais, facilitando análises e decisões em diversas situações.")

    return frame
