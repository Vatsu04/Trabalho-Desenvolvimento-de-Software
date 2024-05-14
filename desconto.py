def calcular_desconto(preco_inicial, taxa_desconto):
   
    desconto = preco_inicial * taxa_desconto
    return desconto, preco_inicial - desconto

