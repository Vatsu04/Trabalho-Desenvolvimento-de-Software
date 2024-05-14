

def juros_simples(valor_principal, taxa_juros, tempo):
    """
    Calcula o montante de um investimento com juros simples.
    
    Args:
    - valor_principal (float): O valor principal do investimento.
    - taxa_juros (float): A taxa de juros (em porcentagem).
    - tempo (int): O tempo em anos.
    
    Returns:
    - float: O montante do investimento após o tempo especificado.
    """
    juros = valor_principal * (taxa_juros / 100) * tempo
    montante = valor_principal + juros
    return montante

def juros_compostos(valor_principal, taxa_juros, tempo):
    """
    Calcula o montante de um investimento com juros compostos.
    
    Args:
    - valor_principal (float): O valor principal do investimento.
    - taxa_juros (float): A taxa de juros (em porcentagem).
    - tempo (int): O tempo em anos.
    
    Returns:
    - float: O montante do investimento após o tempo especificado.
    """
    montante = valor_principal * ((1 + taxa_juros / 100) ** tempo)
    return montante


