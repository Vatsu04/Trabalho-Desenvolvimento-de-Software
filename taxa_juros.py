def taxa_juros_para_decimal(taxa_percentual):
    """
    Converte uma taxa de juros de percentual para decimal.

    Args:
    - taxa_percentual (float): A taxa de juros em percentual.

    Returns:
    - float: A taxa de juros em decimal.
    """
    taxa_decimal = taxa_percentual / 100
    return taxa_decimal

def taxa_juros_para_percentual(taxa_decimal):
    """
    Converte uma taxa de juros de decimal para percentual.

    Args:
    - taxa_decimal (float): A taxa de juros em decimal.

    Returns:
    - float: A taxa de juros em percentual.
    """
    taxa_percentual = taxa_decimal * 100
    return taxa_percentual


