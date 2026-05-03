import random
# Queremos saber P(Gripe | Tos=True)
# Fijamos Tos = True y calculamos el peso de cada muestra

def ponderacion_verosimilitud(n_muestras=1000):
    suma_pesos_con_gripe = 0
    suma_pesos_total = 0
    
    # Probabilidades
    p_gripe = 0.1
    # P(Tos | Gripe) = 0.8, P(Tos | No Gripe) = 0.1
    p_tos_si_gripe = 0.8
    p_tos_si_no_gripe = 0.1
    
    for _ in range(n_muestras):
        # Muestreamos la variable oculta Gripe
        tiene_gripe = random.random() < p_gripe
        
        # (Tos = True)
        # En lugar de muestrear Tos, calculamos su peso (W)
        if tiene_gripe:
            peso = p_tos_si_gripe  # Qué tan probable es la evidencia si hay gripe
        else:
            peso = p_tos_si_no_gripe # Qué tan probable es la evidencia si no hay gripe
            
        # Acumulamos los pesos
        suma_pesos_total += peso
        if tiene_gripe:
            suma_pesos_con_gripe += peso
            
    # La probabilidad es la proporción de los pesos acumulados
    prob_estimada = suma_pesos_con_gripe / suma_pesos_total
    
    print(f"Total de simulaciones útiles: {n_muestras} (¡Cero rechazos!)智")
    print(f"Probabilidad estimada de Gripe: {prob_estimada:.2%}")

ponderacion_verosimilitud()