from tkinter import *
from tkinter import ttk
from components.header import Header
from components.h1 import h1
from components.h2 import h2
from components.text import text
from components.label import create_label
from components.input import create_input
from components.button import create_button
from funcoes import calcular_vpl_handler

def vpl_page(container, mostrar_pagina, add_scroll_to_frame):
    frame = ttk.Frame(container)
    scrollable_frame = add_scroll_to_frame(frame)

    Header(scrollable_frame, mostrar_pagina)

    h1(scrollable_frame, "Valor Presente Líquido (VPL)")

    input_container_1 = ttk.Frame(scrollable_frame)
    input_container_2 = ttk.Frame(scrollable_frame)
    
    input_container_1.pack(expand=1, pady=10)
    input_container_2.pack(expand=1, pady=(10, 100))
    
    create_label(input_container_1, "Taxa de Desconto (% a.a.): ", 0, 0) 
    taxa_entry = create_input(input_container_1, 1, 0)

    create_label(input_container_1, "Investimento Inicial: ", 0, 1)
    investimento_entry = create_input(input_container_1, 1, 1)

    create_label(input_container_1, "Fluxo de Caixa (separado por vírgula): ", 2, 0)
    fluxo_entry = create_input(input_container_1, 3, 0)

    response_text = create_label(input_container_2, "VPL: R$0,00", 0, 0)
    create_button(input_container_2, "CALCULAR", row=0, column=1, command=lambda: calcular_vpl_handler(taxa_entry.get(), fluxo_entry.get(), investimento_entry.get(), response_text))

    text_container = ttk.Frame(scrollable_frame)
    text_container.pack()

    h2(text_container, "O que é Valor Presente Líquido (VPL)?")

    text(text_container, "Valor Presente Líquido, ou VPL, é uma métrica utilizada na análise financeira para determinar a viabilidade de um projeto ou investimento. Ele representa a diferença entre o valor presente de entradas de caixa (receitas) e saídas de caixa (custos e investimentos), trazidos a valor presente para o início do projeto, utilizando uma taxa de desconto apropriada.")

    h2(text_container, "Como Calcular o VPL?")

    text(text_container, "Para calcular o VPL, é necessário estimar os fluxos de caixa esperados ao longo da vida do projeto e aplicar uma taxa de desconto apropriada. \n\nA fórmula básica do VPL é:\n\nVPL = Σ [(FC_t / (1 + r)^t)] - C_0\n\nOnde:\n\n- FC_t são os fluxos de caixa no período t;\n- r é a taxa de desconto;\n- C_0 é o investimento inicial.")

    h2(text_container, "Por que o VPL é Importante?")

    text(text_container, "● Critério de Viabilidade: Projetos com VPL positivo são geralmente considerados viáveis economicamente, indicando que o retorno esperado supera o custo do capital investido.\n\n● Comparação de Projetos: Permite comparar projetos de diferentes tamanhos e durações de forma justa, ao trazer todos os fluxos de caixa a um valor presente comum.\n\n● Consideração do Tempo: Incorpora o valor temporal do dinheiro, garantindo que os fluxos de caixa sejam ponderados adequadamente.")

    h2(text_container, "Considerações Adicionais")

    text(text_container, "Embora seja uma ferramenta poderosa, o VPL requer uma escolha cuidadosa da taxa de desconto e estimativas precisas de fluxo de caixa para uma análise robusta. É importante também realizar análises de sensibilidade e considerar os riscos associados ao projeto para uma avaliação completa.")

    h2(text_container, "Conclusão")

    text(text_container, "O Valor Presente Líquido é essencial para a tomada de decisões de investimento, oferecendo uma análise quantitativa que leva em consideração o valor temporal do dinheiro. Ao ponderar adequadamente os fluxos de caixa e comparar projetos de forma justa, o VPL ajuda a maximizar o retorno sobre investimentos empresariais e a tomar decisões financeiras mais informadas.")

    return frame
