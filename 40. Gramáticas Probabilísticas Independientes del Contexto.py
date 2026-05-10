def calcular_probabilidad_arbol():
    # Reglas gramaticales con sus probabilidades P(Regla)
    # O = Oración, SN = Sintagma Nominal, SV = Sintagma Verbal
    regras = {
        "O -> SN SV": 1.0,
        "SN -> 'La' 'IA'": 0.4,
        "SN -> 'El' 'algoritmo'": 0.6,
        "SV -> 'aprende'": 0.5,
        "SV -> 'falla'": 0.5
    }

    # Frase a evaluar: El algoritmo aprende
    # Estructura: (O (SN 'El' 'algoritmo') (SV 'aprende'))
    
    # La probabilidad del árbol es el producto de las probabilidades de sus reglas
    p_o = regras["O -> SN SV"]
    p_sn = regras["SN -> 'El' 'algoritmo'"]
    p_sv = regras["SV -> 'aprende'"]
    
    probabilidad_total = p_o * p_sn * p_sv
    
    print(f"Estructura: [O [SN El algoritmo] [SV aprende]]")
    print(f"Cálculo: {p_o} * {p_sn} * {p_sv}")
    print(f"Probabilidad de este análisis sintáctico: {probabilidad_total:.4f}")

# Ejecución de la lógica PCFG
calcular_probabilidad_arbol()