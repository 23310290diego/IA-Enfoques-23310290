import math
def entrenamiento_kohonen_simple():
    # Red de 3 neuronas en línea (Posiciones: 0, 1, 2)
    # Cada neurona tiene un peso que representa un color (0 a 1)
    pesos_neuronas = [0.1, 0.5, 0.9] 
    
    # Llega un dato de entrada (un color turquesa, valor 0.2)
    entrada = 0.2
    tasa_aprendizaje = 0.1
    radio_vecindad = 1 # Afecta a la ganadora y a sus vecinos inmediatos

    # Hallar la neurona con la distancia mínima (BMU)
    distancias = [abs(entrada - w) for w in pesos_neuronas]
    indice_ganador = distancias.index(min(distancias))
    
    print(f"Entrada: {entrada} | Pesos actuales: {pesos_neuronas}")
    print(f"La neurona ganadora es la posición: {indice_ganador}")

    # Ajustar la ganadora y sus vecinas
    for i in range(len(pesos_neuronas)):
        distancia_al_ganador = abs(i - indice_ganador)
        
        if distancia_al_ganador <= radio_vecindad:
            # Si es la ganadora o vecina, acerca su peso a la entrada
            # Las vecinas se ajustan menos (aquí simplificado)
            influencia = 1.0 if i == indice_ganador else 0.5
            pesos_neuronas[i] += tasa_aprendizaje * influencia * (entrada - pesos_neuronas[i])

    print(f"Nuevos pesos tras adaptación: {[round(w, 3) for w in pesos_neuronas]}")

entrenamiento_kohonen_simple()