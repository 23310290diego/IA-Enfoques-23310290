# Validador de Uniones Geométricas
def validar_union_geometrica(tipo_union, etiquetas):
   
    #Simula un catálogo un tipo_union: Y, L, T, W etiquetas: lista de etiquetas propuestas (+, -, >)
   
    
    # Catálogo simplificado de uniones permitidas en un mundo de bloques
    # Por ejemplo, en una unión tipo 'Y', todas pueden ser + esquina de un cubo
    uniones_permitidas = {
        "Y": [("+", "+", "+"), ("-", "-", "-")],
        "W": [(">", "+", "<"), ("-", "+", "-")],
        "L": [(">", "<"), ("+", ">"), ("<", "-")]
    }

    print(f"Analizando unión tipo {tipo_union} con etiquetas: {etiquetas}")

    # La IA busca si la combinación propuesta existe en la física de los objetos
    if etiquetas in uniones_permitidas.get(tipo_union, []):
        return "VÁLIDO: Es una estructura físicamente posible."
    else:
        return "ERROR: Es un objeto imposible (tipo M.C. Escher)."

# Caso 1: Una esquina exterior de un cubo (Unión Y con tres aristas convexas)
print(f"Resultado 1: {validar_union_geometrica('Y', ('+', '+', '+'))}")

# Caso 2: Una propuesta inconsistente (Unión L con etiquetas contradictorias)
print(f"Resultado 2: {validar_union_geometrica('L', ('+', '-'))}")