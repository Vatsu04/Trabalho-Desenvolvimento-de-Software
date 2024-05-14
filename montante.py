def calcular_montante(capital, taxa_juros, tempo):
    """
    Calcula o montante de um investimento com base no capital inicial, taxa de juros e tempo.

    Args:
    - capital (float): O capital inicial do investimento.
    - taxa_juros (float): A taxa de juros (em decimal).
    - tempo (int): O tempo em anos.

    Returns:
    - float: O montante do investimento após o tempo especificado.
    """
    montante = capital * (1 + taxa_juros) ** tempo
    return montante

# Exemplo de uso da função
capital_inicial = 1000  # Capital inicial do investimento
taxa_juros_decimal = 0.05  # Taxa de juros em decimal (5%)
tempo = 3  # Tempo em anos

montante = calcular_montante(capital_inicial, taxa_juros_decimal, tempo)
print("Montante:", montante)