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
    h2(frame, "Para que Serve a Matemática Financeira?")
    text(frame, "● Planejamento e Controle Financeiro:\nA Matemática Financeira ajuda indivíduos e empresas a planejar e controlar suas finanças, garantindo uma gestão eficiente dos recursos.\n\n● Avaliação de Investimentos:\nPermite avaliar a viabilidade e rentabilidade de investimentos, ajudando a tomar decisões informadas sobre onde e quando investir.\n\n● Gestão de Empréstimos e Financiamentos:\nAuxilia no cálculo de prestações, juros e amortizações, facilitando a gestão de dívidas e financiamentos.\n\n● Comparação de Produtos Financeiros:\nAjuda a comparar diferentes produtos financeiros, como empréstimos, investimentos e seguros, com base em seus custos e benefícios.\n\n● Tomada de Decisões:\nFornece ferramentas para tomar decisões financeiras informadas, considerando fatores como risco, retorno e valor do dinheiro no tempo.")
    h2(frame, "Principais Conceitos da Matemática Financeira:")
    text(frame, "● Juros Simples e Compostos:\nJuros são a remuneração pelo uso do dinheiro. Juros simples são calculados apenas sobre o valor principal, enquanto juros compostos são calculados sobre o principal mais os juros acumulados.\n\n● Valor Presente e Valor Futuro:\nValor presente é o valor atual de um montante que será recebido ou pago no futuro. Valor futuro é o valor que um montante atual acumulará em um determinado período, considerando uma taxa de juros.\n\n● Taxa Interna de Retorno (TIR):\nA TIR é a taxa de desconto que torna o valor presente líquido (VPL) de um investimento igual a zero, indicando a rentabilidade do investimento.\n\n● Valor Presente Líquido (VPL):\nO VPL é a soma dos fluxos de caixa descontados de um investimento menos o investimento inicial, usado para avaliar a viabilidade de projetos.")
    h2(frame, "Conclusão")
    text(frame, "A Matemática Financeira é uma ferramenta essencial para a gestão financeira eficaz. Ela fornece as bases necessárias para entender e gerenciar finanças pessoais e empresariais, permitindo a tomada de decisões mais informadas e estratégicas.")
    
    return frame