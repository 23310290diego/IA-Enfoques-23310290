def aprendizaje_bayesiano_moneda():
    # Hipótesis P(Cara)
    hipotesis = {"Justa": 0.5, "Cargada": 0.9}
    # Creencia inicial (Prior)
    creencias = {"Justa": 0.5, "Cargada": 0.5}
    
    # Datos observados 3 Caras seguidas
    datos = ["Cara", "Cara", "Cara"]
    
    print(f"Creencias iniciales: {creencias}")
    
    for i, observacion in enumerate(datos, 1):
        nuevas_creencias = {}
        for h, p_cara in hipotesis.items():
            # Verosimilitud: P(D|h)
            verosimilitud = p_cara if observacion == "Cara" else (1 - p_cara)
            # Bayes: P(h|D) = P(D|h) * P(h)
            nuevas_creencias[h] = verosimilitud * creencias[h]
            
        # Normalización para que sumen 1
        total = sum(nuevas_creencias.values())
        creencias = {h: p / total for h, p in nuevas_creencias.items()}
        
        print(f"Tras observación {i} ({observacion}): {creencias}")

aprendizaje_bayesiano_moneda()