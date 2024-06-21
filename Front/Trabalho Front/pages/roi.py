from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from components.header import Header
from components.h1 import h1
from components.h2 import h2
from components.text import text




def roi_page(container, mostrar_pagina, add_scroll_to_frame):
    frame = ttk.Frame(container)
    scrollable_frame = add_scroll_to_frame(frame)
    

    font_tuple = ("Inter", 15, "bold")

    Header(scrollable_frame, mostrar_pagina)
    
    h1(scrollable_frame, "Retorno Sobre Investimento (ROI)")
    
    input_container_1 = ttk.Frame(scrollable_frame)
    input_container_2 = ttk.Frame(scrollable_frame)
    
    input_container_1.pack(expand=1, pady=50)    
    input_container_2.pack(expand=1, pady=50)
    
    
    ganho_label = ttk.Label(input_container_1, text="Digite o ganho do investimento", font=font_tuple)
    ganho_label.grid(row=0, column=0, padx=20)
    ganho_investimento = ttk.Entry(input_container_1)
    ganho_investimento.grid(row=1, column=0, padx=20)
    
    
    custo_label = ttk.Label(input_container_1, text="Digite o custo do investimento", font=font_tuple)
    custo_label.grid(row=0, column=1, padx=20)
    custo_investimento = ttk.Entry(input_container_1)
    custo_investimento.grid(row=1, column=1, padx=20)
    
    
    button = ttk.Button(input_container_2, text="CALCULAR", command=lambda: calcular_roi(ganho_investimento=ganho_investimento, custo_investimento=custo_investimento, label=retorno_investimento))
    button.grid(row=0, column=0, padx=20)
    
    retorno_investimento = ttk.Label(input_container_2, text="O retorno sobre o investimento \n (ROI) é: 00,00%")
    retorno_investimento.grid(row=0, column=1, padx=20)
    
    
    h1(scrollable_frame, "O que é Retorno sobre Investimento (ROI)?")
    
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