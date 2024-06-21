from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from components.header import Header
from components.h1 import h1
from components.h2 import h2
from components.text import text
from components.label import create_label
from components.input import create_input
from components.button import create_button


def roi_page(container, mostrar_pagina, add_scroll_to_frame):
    frame = ttk.Frame(container)
    scrollable_frame = add_scroll_to_frame(frame)

    Header(scrollable_frame, mostrar_pagina)

    h1(scrollable_frame, "Retorno Sobre Investimento (ROI)")

    input_container_1 = ttk.Frame(scrollable_frame)
    input_container_2 = ttk.Frame(scrollable_frame)
    
    input_container_1.pack(expand=1, pady=50)
    input_container_2.pack(expand=1, pady=50)
    
    # row e column
    create_label(input_container_1, "Digite o ganho do investimento", 0, 0) 
    ganho_investimento = create_input(input_container_1, 1, 0)
    
    create_label(input_container_1, "Digite o custo do investimento", 0, 1)
    custo_investimento = create_input(input_container_1, 1, 1)
    
    retorno_investimento = create_label(input_container_2, "O retorno sobre o investimento \n (ROI) é: 00,00%", 0, 1)

    create_button(input_container_2, "CALCULAR", lambda: calcular_roi(ganho_investimento, custo_investimento, retorno_investimento), 0, 0)
    
    h2(scrollable_frame, "O que é Retorno sobre Investimento (ROI)?")

    text_container = ttk.Frame(scrollable_frame)
    text_container.pack()

    text(text_container, """Retorno sobre Investimento, ou ROI, é uma métrica usada para
avaliar a eficiência ou lucratividade de um investimento. Ele
mede o quanto você ganha em relação ao que investiu e é
expressado como uma porcentagem.""")

    text(text_container, """Como Calcular o ROI?
A fórmula básica do ROI é:
ROI = ((Ganho do Investimento - Custo do Investimento) / Custo do Investimento) * 100""")

    text(text_container, """Exemplo:
Você comprou ações por R$ 1.000 e vendeu por R$ 1.200 após um ano.
Ganho do Investimento = R$ 1.200 - R$ 1.000 = R$ 200
ROI = (200 / 1000) * 100 = 20%""")

    text(text_container, """Por que o ROI é Importante?
● Comparação de Investimentos: Permite comparar diferentes investimentos independentemente do valor investido.
● Tomada de Decisões: Ajuda a decidir onde alocar recursos.
● Avaliação de Desempenho: Avalia o desempenho de investimentos passados, identificando áreas de melhoria.""")

    text(text_container, """Limitações do ROI
● Não Considera o Tempo: Não leva em conta o tempo necessário para obter o retorno.
● Custos Adicionais: Pode não considerar todos os custos associados ao investimento.
● Risco Não Avaliado: Não leva em conta o risco envolvido.""")

    text(text_container, """Melhorando o Uso do ROI
Para superar algumas limitações, use outras métricas como:
● Valor Presente Líquido (VPL): Considera o valor do dinheiro no tempo.
● Taxa Interna de Retorno (TIR): Avalia o risco do investimento.""")

    text(text_container, """Conclusão
O ROI é essencial para avaliar a lucratividade de um investimento.
Embora tenha limitações, quando usado corretamente, pode fornecer
insights valiosos para tomar decisões financeiras mais informadas.""")

    return frame


def calcular_roi(ganho_investimento, custo_investimento, label):
    roi = (float(ganho_investimento.get()) - float(custo_investimento.get())) / float(custo_investimento.get()) * 100
    label.config(text="O retorno sobre o investimento \n (ROI) é: " + str(roi) + "%")
    # return roi
