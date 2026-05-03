import random
# Estimar P(Lluvia | Sensor_Rojo)
# Generar muestras de (Lluvia, Sensor)
# Si el sensor NO es rojo, rechazamos la muestra
# Al final, contamos cuántas veces llovió en las muestras aceptadas

def muestreo_por_rechazo(n_muestras=1000):
    muestras_aceptadas = 0
    conteo_lluvia = 0
    
    # Probabilidades base
    p_lluvia = 0.2
    p_sensor_si_llueve = 0.9  # El sensor se pone rojo si llueve
    p_sensor_si_no_llueve = 0.1 # Falsa alarma
    
    for _ in range(n_muestras):
        # Muestreo Directo Generar el mundo
        llueve = random.random() < p_lluvia
        
        prob_sensor = p_sensor_si_llueve if llueve else p_sensor_si_no_llueve
        sensor_rojo = random.random() < prob_sensor
        
    
        # Solo nos interesan los casos donde el SENSOR es ROJO (nuestra evidencia)
        if sensor_rojo == True:
            muestras_aceptadas += 1
            if llueve:
                conteo_lluvia += 1
    
    # Estimación
    if muestras_aceptadas == 0: return 0
    
    prob_estimada = conteo_lluvia / muestras_aceptadas
    print(f"Muestras totales: {n_muestras} | Aceptadas por evidencia: {muestras_aceptadas}")
    print(f"Probabilidad estimada de Lluvia: {prob_estimada:.2%}")

muestreo_por_rechazo()