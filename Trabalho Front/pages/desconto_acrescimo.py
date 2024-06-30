from tkinter import *
from tkinter import ttk
from components.header import Header
from components.h1 import h1
from components.h2 import h2
from components.text import text
from components.label import create_label
from components.input import create_input
from components.button import create_button
from components.h1 import h1
from funcoes import calcular_acrescimo, calcular_desconto


def desconto_acrescimo_page(container, mostrar_pagina, add_scroll_to_frame):
    frame = ttk.Frame(container)
    scrollable_frame = add_scroll_to_frame(frame)

    Header(scrollable_frame, mostrar_pagina)

    h1(scrollable_frame, "Desconto / Acrescimo")
    
    
    h2(scrollable_frame, "Desconto")
    
    input_container_1 = ttk.Frame(scrollable_frame)
    input_container_2 = ttk.Frame(scrollable_frame)
    
    input_container_1.pack(expand=1, pady=10)
    input_container_2.pack(expand=1, pady=(10, 100))
    
    # row e column
    create_label(input_container_1, "Preço inicial: ", 0, 0) 
    preco_desconto = create_input(input_container_1, 1, 0)
    
    create_label(input_container_1, "Porcentagem de desconto: ", 0, 1)
    desconto = create_input(input_container_1, 1, 1)
    
    text_desconto = create_label(input_container_2, "O preço com desconto é: R$0,00", 0, 0)
    create_button(input_container_2, "CALCULAR", row=0, column=1, command=lambda: calcular_desconto(preco_desconto.get(), desconto.get(), text_desconto))

    
    h2(scrollable_frame, "Acréscimo")
    
    input_container_3 = ttk.Frame(scrollable_frame)
    input_container_4 = ttk.Frame(scrollable_frame)
    
    input_container_3.pack(expand=1, pady=10)
    input_container_4.pack(expand=1, pady=(10, 100))
    
    # row e column
    create_label(input_container_3, "Preço inicial: ", 0, 0) 
    preco_acrescimo = create_input(input_container_3, 1, 0)
    
    create_label(input_container_3, "Porcentagem de acréscimo: ", 0, 1)
    acrescimo = create_input(input_container_3, 1, 1)
    
    text_acrescimo = create_label(input_container_4, "O preço com acréscimo é: R$0,00", 0, 0)
    create_button(input_container_4, "CALCULAR", row=0, column=1, command=lambda: calcular_acrescimo(preco_acrescimo.get(), acrescimo.get(), text_acrescimo))

    
    
    text_container = ttk.Frame(scrollable_frame)
    text_container.pack()
    
    
    h2(text_container, "O que é Desconto?")
     
    text(text_container, "Desconto é uma redução no preço original de um produto ou serviço. Ele é geralmente oferecido para incentivar compras ou liquidar estoques. O valor do desconto é normalmente calculado como uma porcentagem do preço original.")
    
    h2(text_container, "Como Calcular o Desconto?")

    text(text_container, "A fórmula básica do desconto é:\n\nPreço com Desconto = Preço Original - (Preço Original * Percentual de Desconto)")
    
    text(text_container, "Exemplo:\n\nVocê quer comprar um produto que custa R$ 100 com um desconto de 20%.\n\nPreço com Desconto = 100 - (100 * 0.20) = 100 - 20 = R$ 80")
    
    h2(text_container, "O que é Acréscimo?")

    text(text_container, "Acréscimo é um aumento no preço original de um produto ou serviço. Ele é aplicado por diversas razões, como aumento de custos ou aumento de demanda. O valor do acréscimo também é geralmente calculado como uma porcentagem do preço original.")

    h2(text_container, "Como Calcular o Acréscimo?")

    text(text_container, "A fórmula básica do acréscimo é:\n\nPreço com Acréscimo = Preço Original + (Preço Original * Percentual de Acréscimo")

    text(text_container, "Exemplo:\n\nVocê quer comprar um produto que custa R$ 100 com um acréscimo de 20%.\n\nPreço com Acréscimo = 100 + (100 * 0.20) = 100 + 20 = R$ 120")
        
    h2(text_container, "Por que Entender Desconto e Acréscimo é Importante?")

    text(text_container,"● Economia: Conhecer como funcionam descontos pode ajudar a economizar dinheiro em compras.\n\n● Planejamento Financeiro: Saber calcular acréscimos e descontos é útil para planejar orçamentos e gastos.\n\n● Negociação: Entender essas métricas ajuda a negociar melhores preços em diversas situações.")

    h2(text_container, "Conclusão")

    text(text_container, "Descontos e acréscimos são fundamentais na vida financeira cotidiana. Saber como calculá-los permite tomar decisões mais informadas e aproveitar oportunidades de economia e investimento de forma mais eficiente.")
   
        
    return frame


