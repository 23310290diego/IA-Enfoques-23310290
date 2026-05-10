def traductor_estadistico(frase_origen):
    # MODELO DE TRADUCCIÓN (Diccionario de Probabilidades)
    # Representa: P(Palabra_Destino | Palabra_Origen)
    # Aprendido de miles de textos traducidos previamente
    prob_traduccion = {
        "el": {"the": 0.95, "it": 0.05},
        "gato": {"cat": 0.90, "feline": 0.10},
        "negro": {"black": 0.85, "dark": 0.15}
    }

    # MODELO DE LENGUAJE (Probabilidad de Fluidez en Inglés)
    # Representa: P(Frase). El modelo sabe que the black cat
    # es mucho más común que the cat black
    prob_fluidez = {
        "the black cat": 0.8,
        "the cat black": 0.01
    }

    palabras = frase_origen.lower().split()
    
    # Candidato 1: Traducción literal palabra por palabra
    # Candidato 2: Traducción con reordenamiento (Adjetivo después del sustantivo)
    candidatos = ["the cat black", "the black cat"]
    
    mejor_p = 0
    mejor_traduccion = ""

    for cand in candidatos:
        # Cálculo de Probabilidad Total: P(Traducción) = P(Palabra1)*P(Palabra2)*... * P(Fluidez_Frase)
        
        # Aqui sumamos logaritmos o multiplicamos:
        p_trad = prob_traduccion["el"]["the"] * \
                 prob_traduccion["gato"]["cat"] * \
                 prob_traduccion["negro"]["black"]
        
        p_total = p_trad * prob_fluidez.get(cand, 0.001)
        
        print(f"Candidato: '{cand}' | Probabilidad Total: {p_total:.6f}")
        
        if p_total > mejor_p:
            mejor_p = p_total
            mejor_traduccion = cand

    return mejor_traduccion


resultado = traductor_estadistico("El gato negro")
print(f"\nResultado final: {resultado}")