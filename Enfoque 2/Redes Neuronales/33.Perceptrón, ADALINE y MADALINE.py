def entrenar_perceptron():
    # Datos: [x1, x2, bias] para una compuerta AND
    entradas = [[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
    salidas_deseadas = [0, 0, 0, 1]
    pesos = [0.1, -0.2, 0.3] # Pesos iniciales aleatorios
    tasa_aprendizaje = 0.1
    
    for epoca in range(10):
        total_errores = 0
        for i in range(len(entradas)):
            # Suma ponderada + Activación escalón
            suma = sum(x * w for x, w in zip(entradas[i], pesos))
            prediccion = 1 if suma > 0 else 0
            
            error = salidas_deseadas[i] - prediccion
            if error != 0:
                # Ajuste de pesos: W = W + (Tasa * Error * X)
                for j in range(len(pesos)):
                    pesos[j] += tasa_aprendizaje * error * entradas[i][j]
                total_errores += 1
        
        if total_errores == 0: break
    
    print(f"Pesos finales tras entrenamiento: {pesos}")

entrenar_perceptron()