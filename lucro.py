def calcular_lucro(receita, custos_variaveis, custos_fixos):
    """
    Calcula o lucro bruto e o lucro líquido com base na receita, custos variáveis e custos fixos.

    Args:
    - receita (float): O valor da receita.
    - custos_variaveis (float): O valor dos custos variáveis.
    - custos_fixos (float): O valor dos custos fixos.

    Returns:
    - tuple: Uma tupla contendo o lucro bruto e o lucro líquido.
    """
    lucro_bruto = receita - custos_variaveis
    lucro_liquido = receita - (custos_variaveis + custos_fixos)
    return lucro_bruto, lucro_liquido

# Exemplo de uso da função
receita_total = 10000  # Receita total da empresa
custos_variaveis_total = 4000  # Custos variáveis totais da empresa
custos_fixos_total = 3000  # Custos fixos totais da empresa

lucro_bruto, lucro_liquido = calcular_lucro(receita_total, custos_variaveis_total, custos_fixos_total)
print("Lucro Bruto:", lucro_bruto)
print("Lucro Líquido:", lucro_liquido)