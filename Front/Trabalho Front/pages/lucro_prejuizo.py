from tkinter import *
from tkinter import ttk
from components.header import Header
from components.h1 import h1
from components.h2 import h2
from components.text import text
from components.label import create_label
from components.input import create_input
from components.button import create_button


def lucro_prejuizo_page(container, mostrar_pagina, add_scroll_to_frame):
    frame = ttk.Frame(container)
    scrollable_frame = add_scroll_to_frame(frame)

    Header(scrollable_frame, mostrar_pagina)

    h1(scrollable_frame, "Lucro / Prejuízo")

    # h2(scrollable_frame, "Cálculo de Lucro")
    
    input_container_1 = ttk.Frame(scrollable_frame)
    input_container_2 = ttk.Frame(scrollable_frame)
    
    input_container_1.pack(expand=1, pady=10)
    input_container_2.pack(expand=1, pady=(10, 100))
    
    # row e column
    create_label(input_container_1, "Receita Total: ", 0, 0) 
    receita = create_input(input_container_1, 1, 0)
    
    create_label(input_container_1, "Custos Totais: ", 0, 1)
    custo = create_input(input_container_1, 1, 1)
    
    response_text = create_label(input_container_2, "Lucro/Prejuízo: R$0,00\nPercentual: 0,00%", 0, 0)
    create_button(input_container_2, "CALCULAR", row=0, column=1, command=lambda: definir_calculo(custo.get(), receita.get(), response_text))

    
    # input_container_3 = ttk.Frame(scrollable_frame)
    # input_container_4 = ttk.Frame(scrollable_frame)
    
    # input_container_3.pack(expand=1, pady=10)
    # input_container_4.pack(expand=1, pady=50)
    
    text_container = ttk.Frame(scrollable_frame)
    text_container.pack()

    h2(text_container, "O que é Lucro e Prejuízo?")

    text(text_container, "Lucro e prejuízo são conceitos fundamentais em contabilidade e finanças que indicam o resultado financeiro de uma empresa ou indivíduo em um determinado período. Lucro ocorre quando a receita excede os custos e despesas, enquanto prejuízo acontece quando os custos e despesas superam a receita.")

    h2(text_container, "Como Calcular Lucro e Prejuízo?")

    text(text_container, "O cálculo de lucro ou prejuízo é simples:\n\nLucro = Receita Total - Custos Totais\n\nPrejuízo = Custos Totais - Receita Total\n\nPor exemplo, se uma empresa tem uma receita de R$ 10.000 e custos totais de R$ 8.000, o lucro seria R$ 2.000. Se os custos totais fossem R$ 12.000, haveria um prejuízo de R$ 2.000.")

    h2(text_container, "Importância de Lucro e Prejuízo")

    text(text_container, "● Indicadores Financeiros: Lucro e prejuízo são indicadores-chave de desempenho financeiro de uma empresa, refletindo sua eficiência operacional e capacidade de geração de receita.\n\n● Tomada de Decisão: Baseiam decisões sobre investimentos, expansões, cortes de custos e estratégias de crescimento./n/n● Avaliação de Performance: Permitem comparar o desempenho atual com períodos anteriores ou metas estabelecidas.")

    h2(text_container, "Considerações Adicionais")

    text(text_container, "É importante analisar o contexto e as circunstâncias que levam ao lucro ou prejuízo. Fatores como sazonalidade, concorrência e mudanças no mercado podem impactar significativamente os resultados financeiros.")

    h2(text_container, "Conclusão")

    text(text_container, "Lucro e prejuízo são conceitos cruciais para avaliação financeira, guiando decisões estratégicas e indicando a saúde financeira de uma organização ou indivíduo. Ao compreender e monitorar esses indicadores, pode-se otimizar o desempenho financeiro e garantir sustentabilidade a longo prazo.")

    return frame


def definir_calculo(custo, receita, response):
    if custo > receita: 
        prejuizo(custo, receita, response)
        
    else: 
        lucro(custo, receita, response)
        
        
def lucro(custo, receita, response):
    percentual = (float(custo) / float(receita)) * 100 
    lucro = float(receita) - float(custo)
    
    response.config(text="Lucro: R$" + str(lucro) + "\nPercentual de Lucro: " + str(percentual) + "%")
    
    
def prejuizo(custo, receita, response):
    percentual = ((float(receita) / float(custo)) - 1) * 100 * -1
    prejuizo = float(custo) - float(receita)
    
    response.config(text="Prejuízo: R$" + str(prejuizo) + "\nPercentual de Prejuízo: " + str(percentual) + "%")
