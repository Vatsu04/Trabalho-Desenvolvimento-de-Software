from tkinter import *
from tkinter import ttk
from components.header import Header
from components.h1 import h1
from components.h2 import h2
from components.text import text
from components.label import create_label
from components.input import create_input
from components.button import create_button


def juros_montante_page(container, mostrar_pagina, add_scroll_to_frame):
    frame = ttk.Frame(container)
    scrollable_frame = add_scroll_to_frame(frame)

    Header(scrollable_frame, mostrar_pagina)

    h1(scrollable_frame, "Juros / Montante")
    
    
    h2(scrollable_frame, "Montante")
    
    input_container_5 = ttk.Frame(scrollable_frame)
    input_container_6 = ttk.Frame(scrollable_frame)
    
    input_container_5.pack(expand=1, pady=10)
    input_container_6.pack(expand=1, pady=(10, 100))
    
    # row e column
    create_label(input_container_5, "Investimento Inicial: ", 0, 0) 
    investimento_montante = create_input(input_container_5, 1, 0)
    
    create_label(input_container_5, "Juros: ", 0, 1)
    juros_montante = create_input(input_container_5, 1, 1)
    
    create_label(input_container_5, "Tempo: ", 0, 2)
    tempo_montante = create_input(input_container_5, 1, 2)
    
    response_text_montante = create_label(input_container_6, "O montante é: R$0,00", 0, 0)
    create_button(input_container_6, "CALCULAR", row=0, column=1, command=lambda: calcular_montante(investimento_montante.get(), juros_montante.get(), tempo_montante.get(), response_text_montante))

    
    
    montante_text_container = ttk.Frame(scrollable_frame)
    montante_text_container.pack()

    h2(montante_text_container, "O que é a Fórmula do Montante?")
    
    text(montante_text_container, "A fórmula do montante é utilizada para calcular o valor total acumulado em um investimento ou empréstimo ao final de um determinado período, considerando os juros aplicados.")

    h2(montante_text_container, "Como Calcular o Montante com Juros Compostos?")

    text(montante_text_container, "A fórmula do montante para juros compostos é:\n\nMontante = Principal * (1 + Taxa de Juros) ** Tempo\n\nOnde:\n\n● Principal: O valor inicial emprestado ou investido.\n● Taxa de Juros: A taxa de juros aplicada por período (em decimal).\n● Tempo: O número de períodos de tempo em que os juros são aplicados.")

    text(montante_text_container, "Exemplo de Juros Compostos:\n\nVocê investe R$ 1.000 a uma taxa de juros compostos de 5% ao ano por 3 anos.\n\nPrincipal = R$ 1.000\nTaxa de Juros = 5/100 = 0.05\nTempo = 3 anos\nMontante = 1.000 * (1 + 0.05) ** 3\nMontante = 1.000 * 1.157625 = R$ 1.157,63")

    text(montante_text_container, "O valor total acumulado após 3 anos será R$ 1.157,63, com os juros compostos sendo R$ 157,63.")

    h2(montante_text_container, "Como Calcular o Montante com Juros Simples?")

    text(montante_text_container, "A fórmula do montante para juros simples é:\n\nMontante = Principal + (Principal * Taxa de Juros * Tempo)")

    text(montante_text_container, "Exemplo de Juros Simples:\n\nVocê investe R$ 1.000 a uma taxa de juros simples de 5% ao ano por 3 anos.\n\nPrincipal = R$ 1.000\nTaxa de Juros = 5/100 = 0.05\nTempo = 3 anos\nMontante = 1.000 + (1.000 * 0.05 * 3)\nMontante = 1.000 + 150 = R$ 1.150")

    text(montante_text_container, "O valor total acumulado após 3 anos será R$ 1.150, com os juros simples sendo R$ 150.")

    h2(montante_text_container, "Por que Entender a Fórmula do Montante é Importante?")

    text(montante_text_container, "● Planejamento Financeiro: Ajuda a planejar melhor seus investimentos e empréstimos.\n\n● Educação Financeira: Entender como os juros impactam o montante final é fundamental para tomar decisões financeiras informadas.\n\n● Comparação de Produtos Financeiros: Permite comparar diferentes opções de investimentos com base em seus retornos.")

    h2(montante_text_container, "Conclusão")

    text(montante_text_container, "A fórmula do montante é uma ferramenta essencial na matemática financeira. Saber como calcular o montante acumulado permite compreender o impacto dos juros, seja simples ou compostos, ajudando a tomar decisões financeiras mais informadas e eficientes.")
    

    h2(scrollable_frame, "Juros Simples")
    
    input_container_1 = ttk.Frame(scrollable_frame)
    input_container_2 = ttk.Frame(scrollable_frame)
    
    input_container_1.pack(expand=1, pady=10)
    input_container_2.pack(expand=1, pady=(10, 100))
    
    # row e column
    create_label(input_container_1, "Investimento Inicial: ", 0, 0) 
    investimento_simples = create_input(input_container_1, 1, 0)
    
    create_label(input_container_1, "Juros: ", 0, 1)
    juros_simples = create_input(input_container_1, 1, 1)
    
    create_label(input_container_1, "Tempo: ", 0, 2)
    tempo_simples = create_input(input_container_1, 1, 2)
    
    response_text_simples = create_label(input_container_2, "O montante com juros simples é: R$0,00", 0, 0)
    create_button(input_container_2, "CALCULAR", row=0, column=1, command=lambda: calcular_juros_simples(investimento_simples.get(), juros_simples.get(), tempo_simples.get(), response_text_simples))
    # ttk.Button(input_container_2, text="CALCULAR", command=lambda: juros_simples(investimento.get(), juros.get(), tempo.get(), response_text)).grid(row=0, column=1, padx=10)
    
    
    
    # input_container_3 = ttk.Frame(scrollable_frame)
    # input_container_4 = ttk.Frame(scrollable_frame)
    
    # input_container_3.pack(expand=1, pady=10)
    # input_container_4.pack(expand=1, pady=50)
    



    simples_text_container = ttk.Frame(scrollable_frame)
    simples_text_container.pack()

    h2(simples_text_container, "O que são Juros Simples?")

    text(simples_text_container, "Juros Simples são uma forma de calcular os juros sobre um valor emprestado ou investido, onde os juros são calculados apenas sobre o valor principal, sem considerar os juros acumulados de períodos anteriores.")

    h2(simples_text_container, "Como Calcular Juros Simples?")

    text(simples_text_container, "A fórmula básica dos juros simples é:\n\nJuros Simples = Principal * Taxa de Juros * Tempo\n\nOnde:\n\n● Principal: O valor inicial emprestado ou investido.\n● Taxa de Juros: A taxa de juros aplicada (em decimal).\n● Tempo: O período de tempo pelo qual o dinheiro é emprestado ou investido.")

    text(simples_text_container, "Exemplo:\n\nVocê investe R$ 1.000 a uma taxa de juros simples de 5% ao ano por 3 anos.\n\nPrincipal = R$ 1.000\nTaxa de Juros = 5/100 = 0.05\nTempo = 3 anos\nJuros Simples = 1.000 * 0.05 * 3 = R$ 150")

    text(simples_text_container, "O valor total acumulado (Principal + Juros) após 3 anos será:\n\nValor Total = Principal + Juros Simples\n\nValor Total = 1.000 + 150 = R$ 1.150")

    h2(simples_text_container, "Por que Entender Juros Simples é Importante?")

    text(simples_text_container, "● Planejamento Financeiro: Ajuda a planejar empréstimos e investimentos.\n\n● Comparação de Produtos Financeiros: Permite comparar diferentes opções de empréstimos e investimentos.\n\n● Educação Financeira: Entender os juros simples é fundamental para tomar decisões financeiras informadas.")

    h2(simples_text_container, "Conclusão")

    text(simples_text_container, "Os juros simples são uma ferramenta básica, mas essencial na matemática financeira. Saber como calculá-los ajuda a compreender melhor como os investimentos e empréstimos funcionam, permitindo tomar decisões mais informadas e eficientes.")
    
    
    h2(scrollable_frame, "Juros Compostos")
    
    input_container_3 = ttk.Frame(scrollable_frame)
    input_container_4 = ttk.Frame(scrollable_frame)
    
    input_container_3.pack(expand=1, pady=10)
    input_container_4.pack(expand=1, pady=(10, 100))
    
    # row e column
    create_label(input_container_3, "Investimento Inicial: ", 0, 0) 
    investimento_composto = create_input(input_container_3, 1, 0)
    
    create_label(input_container_3, "Juros: ", 0, 1)
    juros_composto = create_input(input_container_3, 1, 1)
    
    create_label(input_container_3, "Tempo: ", 0, 2)
    tempo_composto = create_input(input_container_3, 1, 2)
    
    response_text_composto = create_label(input_container_4, "O montante com juros simples é: R$0,00", 0, 0)
    create_button(input_container_4, "CALCULAR", row=0, column=1, command=lambda: calcular_juros_compostos(investimento_composto.get(), juros_composto.get(), tempo_composto.get(), response_text_composto))

    
    composto_text_container = ttk.Frame(scrollable_frame)
    composto_text_container.pack()

    h2(composto_text_container, "O que são Juros Compostos?")
    
    text(composto_text_container, "Juros Compostos são uma forma de calcular os juros sobre um valor emprestado ou investido, onde os juros são calculados sobre o valor principal mais os juros acumulados de períodos anteriores. Isso resulta em um crescimento exponencial do montante.")

    h2(composto_text_container, "Como Calcular Juros Compostos?")

    text(composto_text_container, "A fórmula básica dos juros compostos é:\n\nMontante = Principal * (1 + Taxa de Juros) ** Tempo\n\nOnde:\n\n● Principal: O valor inicial emprestado ou investido.\n● Taxa de Juros: A taxa de juros aplicada por período (em decimal).\n● Tempo: O número de períodos de tempo em que os juros são aplicados.")

    text(composto_text_container, "Exemplo:\n\nVocê investe R$ 1.000 a uma taxa de juros compostos de 5% ao ano por 3 anos.\n\nPrincipal = R$ 1.000\nTaxa de Juros = 5/100 = 0.05\nTempo = 3 anos\nMontante = 1.000 * (1 + 0.05) ** 3\nMontante = 1.000 * 1.157625 = R$ 1.157,63")

    text(composto_text_container, "O valor total acumulado após 3 anos será R$ 1.157,63, com os juros compostos sendo R$ 157,63.")

    h2(composto_text_container, "Por que Entender Juros Compostos é Importante?")

    text(composto_text_container, "● Crescimento Exponencial: Juros compostos permitem que investimentos cresçam exponencialmente ao longo do tempo.\n\n● Planejamento Financeiro: Ajuda a planejar melhor seus investimentos entender o impacto do tempo nos retornos financeiros.\n\n● Comparação de Produtos Financeiros: Permite comparar diferentes opções de investimentos com base em seus potenciais de crescimento.")

    h2(composto_text_container, "Conclusão")

    text(composto_text_container, "Os juros compostos são uma ferramenta poderosa na matemática financeira. Saber como calculá-los permite compreender o potencial de crescimento dos investimentos ao longo do tempo, ajudando a tomar decisões financeiras mais informadas e estratégicas.")




    return frame



def calcular_montante(capital, taxa_juros, tempo, response):
    montante = float(capital) * (1 + (float(taxa_juros) / 100)) ** float(tempo)
    response.config(text="O montante é: R$" + str(round(montante, 2)))

def calcular_juros_simples(valor_principal, taxa_juros, tempo, response):
    juros = float(valor_principal) * (float(taxa_juros) / 100) * float(tempo)
    montante = float(valor_principal) + float(juros)
    response.config(text="O montante com juros simples é: R$" + str(round(montante, 2)))

def calcular_juros_compostos(valor_principal, taxa_juros, tempo, response):
    montante = float(valor_principal) * ((1 + float(taxa_juros) / 100) ** float(tempo))
    response.config(text="O montante com juros composetos é: R$" + str(round(montante, 2)))






# Juros Simples





# ---------------------------------------------------------------------------------------




# ############################################################
# #                          Juros Compostos                                  #
# ############################################################


# ---------------------------------------------------------------------------------------



# ############################################################
# #                          Fórmula do Montante                                #
# ############################################################



# -------------------------------------------------------------------------------------





