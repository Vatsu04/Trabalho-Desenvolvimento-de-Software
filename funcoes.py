def porcentagem(valor, porcentagem):
    return (valor * porcentagem) / 100

def lucro(L, C, V):
    V = L + C
    L = V - C
    percentual = (L / C) * 100 
    return L, percentual

def prejuizo(L, C, V):
    V = L + C
    P = C - L
    percentual = (P / C) * 100 
    return P, percentual

def calcular_montante(capital, taxa_juros, tempo):
 
    montante = capital * (1 + taxa_juros) ** tempo
    return montante



def juros_simples(valor_principal, taxa_juros, tempo):

    juros = valor_principal * (taxa_juros / 100) * tempo
    montante = valor_principal + juros
    return montante

def juros_compostos(valor_principal, taxa_juros, tempo):
 
    montante = valor_principal * ((1 + taxa_juros / 100) ** tempo)
    return montante


def calcular_desconto(preco_inicial, taxa_desconto):
   
    desconto = preco_inicial * (taxa_desconto/100)
    preco_novo = preco_inicial - desconto
    return desconto, preco_novo

def calcular_acrescimo(preco_inicial, taxa_acrescimo):
   
    acrescimo = preco_inicial * (taxa_acrescimo/100)
    preco_novo = preco_inicial + acrescimo
    return acrescimo, preco_novo