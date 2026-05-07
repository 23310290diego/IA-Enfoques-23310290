def aprendizaje_hmm_basico():
    # Modelo inicial (suposiciones mediocres)
    # P(Estado_t | Estado_t-1)
    transicion = {"A->A": 0.5, "A->B": 0.5}
    
    # Secuencia de estados estimada (tras un paso E)
    secuencia_estimada = ["A", "A", "A", "B", "A", "A"]
    
    # Actualizar frecuencias
    conteo_AA = 0
    conteo_AB = 0
    
    for i in range(len(secuencia_estimada) - 1):
        estado_actual = secuencia_estimada[i]
        siguiente = secuencia_estimada[i+1]
        
        if estado_actual == "A":
            if siguiente == "A":
                conteo_AA += 1
            else:
                conteo_AB += 1
                
    # Recalcular probabilidades
    total_desde_A = conteo_AA + conteo_AB
    transicion["A->A"] = conteo_AA / total_desde_A
    transicion["A->B"] = conteo_AB / total_desde_A
    
    print(f"Nueva probabilidad A->A: {transicion['A->A']:.2f}")
    print(f"Nueva probabilidad A->B: {transicion['A->B']:.2f}")

aprendizaje_hmm_basico()