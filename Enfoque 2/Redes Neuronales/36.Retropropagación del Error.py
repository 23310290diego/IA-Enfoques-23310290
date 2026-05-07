def backpropagation_step():
    # Estamos en una capa oculta, suposicion
    salida_oculta = 0.7  # Valor que la neurona envió hacia adelante
    peso_hacia_salida = 0.5
    error_en_salida = 0.1 # El error que detectó la capa final
    tasa_aprendizaje = 0.1

    # Calculamos el Gradiente Local
    # Derivada de la sigmoide: f'(z) = out * (1 - out)
    derivada_activacion = salida_oculta * (1 - salida_oculta)
    
    # Retropropagamos el error:
    # Error que le corresponde a esta neurona oculta
    error_retropropagado = error_en_salida * peso_hacia_salida
    
    # Calculamos el ajuste Delta
    # Delta = Tasa * Error * Derivada * Entrada
    ajuste_peso = tasa_aprendizaje * error_retropropagado * derivada_activacion
    
    print(f"Error recibido de la capa siguiente: {error_en_salida}")
    print(f"Responsabilidad de esta neurona (Gradiente): {error_retropropagado:.4f}")
    print(f"Ajuste sugerido para el peso: {ajuste_peso:.4f}")

backpropagation_step()