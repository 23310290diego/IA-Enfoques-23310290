# x_est: Estimación actual de la posición
# p_est: Incertidumbre de la estimación

def filtro_kalman_basico():
    # Parámetros iniciales
    posicion_real = 10.0
    x_est = 0.0  # La IA empieza creyendo que está en 0
    p_est = 100.0 # Mucha incertidumbre inicial
    
    ruido_proceso = 0.1  # Inestabilidad del sistema
    ruido_sensor = 2.0   # El sensor es poco preciso
    
    print(f"{'Medición':<10} | {'Estimación IA':<15} | {'Error (P)':<10}")
    print("-" * 45)

    for i in range(5):
        # Predicción 
        # Aquí asumimos que la posición debería mantenerse
        x_pred = x_est
        p_pred = p_est + ruido_proceso
        
        # Actualización con nueva medición
        import random
        z = posicion_real + random.gauss(0, ruido_sensor) # Lectura del sensor
        
        # Ganancia de Kalman: ¿A quién le creo más? ¿Al sensor o a mi predicción?
        K = p_pred / (p_pred + ruido_sensor)
        
        # Nueva estimación
        x_est = x_pred + K * (z - x_pred)
        p_est = (1 - K) * p_pred
        
        print(f"{z:<10.2f} | {x_est:<15.2f} | {p_est:<10.2f}")

filtro_kalman_basico()