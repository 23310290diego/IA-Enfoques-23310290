def reconocer_palabra():
    # Evidencia acústica detectada (simplificada como sonidos)
    sonidos_detectados = ["K", "A", "S", "A"]
    
    # Diccionario de probabilidades (Modelo de Lenguaje + Acústico)
    # P(Palabra | Sonidos)
    posibles_candidatos = {
        "CASA": 0.90,
        "CAZA": 0.05,
        "CARA": 0.03,
        "MASA": 0.02
    }
    
    # La IA selecciona la explicación más probable (Viterbi)
    mejor_hipotesis = max(posibles_candidatos, key=posibles_candidatos.get)
    probabilidad = posibles_candidatos[mejor_hipotesis]
    
    print(f"Señales acústicas: {'-'.join(sonidos_detectados)}")
    print(f"Palabra reconocida: {mejor_hipotesis} ({probabilidad:.2%})")

reconocer_palabra()