from tkinter import *
from tkinter import ttk
from components.header import Header
from components.h1 import h1
from components.text import text
from components.label import create_label
from components.input import create_input
from components.button import create_button

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

    text(text_container, "O que é Valor Presente Líquido (VPL)?\nValor Presente Líquido, ou VPL, é uma métrica utilizada na análise financeira para determinar a viabilidade de um projeto ou investimento. Ele representa a diferença entre o valor presente de entradas de caixa (receitas) e saídas de caixa (custos e investimentos), trazidos a valor presente para o início do projeto, utilizando uma taxa de desconto apropriada.")

    text(text_container, "Como Calcular o VPL?\nPara calcular o VPL, é necessário estimar os fluxos de caixa esperados ao longo da vida do projeto e aplicar uma taxa de desconto apropriada. A fórmula básica do VPL é:\nVPL = Σ [(FC_t / (1 + r)^t)] - C_0\nOnde:\n- FC_t são os fluxos de caixa no período t;\n- r é a taxa de desconto;\n- C_0 é o investimento inicial.")

    text(text_container, "Por que o VPL é Importante?\n● Critério de Viabilidade: Projetos com VPL positivo são geralmente considerados viáveis economicamente, indicando que o retorno esperado supera o custo do capital investido.\n● Comparação de Projetos: Permite comparar projetos de diferentes tamanhos e durações de forma justa, ao trazer todos os fluxos de caixa a um valor presente comum.\n● Consideração do Tempo: Incorpora o valor temporal do dinheiro, garantindo que os fluxos de caixa sejam ponderados adequadamente.")

    text(text_container, "Considerações Adicionais\nEmbora seja uma ferramenta poderosa, o VPL requer uma escolha cuidadosa da taxa de desconto e estimativas precisas de fluxo de caixa para uma análise robusta. É importante também realizar análises de sensibilidade e considerar os riscos associados ao projeto para uma avaliação completa.")

    text(text_container, "Conclusão\nO Valor Presente Líquido é essencial para a tomada de decisões de investimento, oferecendo uma análise quantitativa que leva em consideração o valor temporal do dinheiro. Ao ponderar adequadamente os fluxos de caixa e comparar projetos de forma justa, o VPL ajuda a maximizar o retorno sobre investimentos empresariais e a tomar decisões financeiras mais informadas.")

    return frame

def calcular_vpl(taxa, fluxo_de_caixa, investimento_inicial):
    vpl = -investimento_inicial 
    for i, fluxo in enumerate(fluxo_de_caixa):
        vpl += fluxo / (1 + taxa) ** (i + 1)
    return vpl

def calcular_vpl_handler(taxa, fluxo_caixa_str, investimento_inicial, response_text):
    taxa = float(taxa) / 100
    investimento_inicial = float(investimento_inicial)
    fluxo_de_caixa = [float(valor.strip()) for valor in fluxo_caixa_str.split(',') if valor.strip()]
    
    vpl = calcular_vpl(taxa, fluxo_de_caixa, investimento_inicial)
    
    response_text.config(text=f"VPL: R${vpl:.2f}")