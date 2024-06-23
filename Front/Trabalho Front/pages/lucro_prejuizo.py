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



    text(text_container, """A Taxa Interna de Retorno, ou TIR, é uma métrica utilizada na
análise financeira para avaliar a atratividade de um investimento
ou projeto. Ela representa a taxa de desconto que iguala o valor
presente líquido (VPL) dos fluxos de caixa futuros ao investimento
inicial. Em outras palavras, é a taxa de crescimento anualizada
esperada do investimento.""")

    text(text_container, """Como Calcular a TIR?
A TIR é calculada encontrando a taxa de desconto que faz com que
o VPL do projeto seja igual a zero. Em termos matemáticos, a TIR
é o valor de r que satisfaz a equação:
VPL = Σ [(FC_t / (1 + r)^t)] - C_0 = 0
onde:
- FC_t são os fluxos de caixa no período t;
- r é a taxa de desconto (TIR);
- C_0 é o investimento inicial.""")

    text(text_container, """Por que a TIR é Importante?
● Critério de Viabilidade: Projetos com TIR superior ao custo
de oportunidade do capital (ou taxa mínima de retorno exigida)
são considerados atrativos.
● Comparação de Projetos: Permite comparar diferentes projetos
de investimento, selecionando aqueles com maior potencial de
retorno financeiro.
● Avaliação de Risco: A TIR incorpora o risco ao considerar
o retorno esperado ajustado pela taxa de desconto necessária.""")

    text(text_container, """Considerações Adicionais
Embora a TIR seja uma métrica valiosa, sua interpretação deve
levar em conta algumas considerações críticas, como a possibilidade
de múltiplas TIRs em cenários complexos e a necessidade de ajustar
a taxa de desconto para refletir adequadamente o risco do projeto.""")

    text(text_container, """Conclusão
A Taxa Interna de Retorno é essencial na avaliação de projetos de
investimento, oferecendo uma medida robusta de atratividade financeira.
Ao calcular a TIR e compará-la com o custo de oportunidade do capital,
as empresas podem tomar decisões mais fundamentadas e maximizar o
retorno sobre seus investimentos. No entanto, é importante usá-la em
conjunto com outras métricas, como o Valor Presente Líquido (VPL),
para uma análise completa e equilibrada.""")

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
