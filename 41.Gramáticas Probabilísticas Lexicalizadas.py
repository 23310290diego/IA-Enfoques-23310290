def analisis_lexicalizado():
    # Probabilidad de que un verbo tenga un objeto directo (P(V -> V SN))
    # No es lo mismo para Devorar que para Reír
    probabilidades_nucleo = {
        "comió": {"tiene_objeto": 0.9, "es_intransitivo": 0.1},
        "sonrió": {"tiene_objeto": 0.05, "es_intransitivo": 0.95}
    }

    def evaluar_frase(verbo, estructura):
        prob = probabilidades_nucleo.get(verbo, {"tiene_objeto": 0.5})
        
        if estructura == "Verbo + Objeto":
            return prob["tiene_objeto"]
        else:
            return prob.get("es_intransitivo", 0.5)

    # El niño comió la manzana(Estructura con objeto)
    p_a = evaluar_frase("comió", "Verbo + Objeto")
    
    # El niño sonrió la manzana (Estructura con objeto - Poco probable)
    p_b = evaluar_frase("sonrió", "Verbo + Objeto")

    print(f"Probabilidad sintáctica para 'comió la manzana': {p_a:.2f}")
    print(f"Probabilidad sintáctica para 'sonrió la manzana': {p_b:.2f}")

analisis_lexicalizado()