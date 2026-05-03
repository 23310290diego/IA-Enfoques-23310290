# Simulamos un sistema simple con estados y observaciones.

def tareas_temporales_ia():
    # Evidencia recogida ej. posiciones detectadas por un GPS con error
    evidencia = [1.1, 2.0, 2.9, 4.2] 
    
    # FILTRADO: ¿Dónde estoy en t=4?
    # Toma el último dato y lo limpia con el historial
    posicion_actual = sum(evidencia) / len(evidencia) # Simplificación pedagógica
    
    # PREDICCIÓN: ¿Dónde estaré en t=5?
    # Calcula la tendencia actual
    velocidad_estimada = evidencia[-1] - evidencia[-2]
    posicion_futura = evidencia[-1] + velocidad_estimada
    
    # SUAVIZADO: Ahora que sé que estoy en 4.2, ¿dónde estaba realmente en t=2?
    # El dato original era 2.0, pero viendo la trayectoria, quizás era 2.05
    posicion_pasada_suavizada = (evidencia[0] + evidencia[2]) / 2
    
    print(f"Filtrado (Ahora): {posicion_actual:.2f}")
    print(f"Predicción (T+1): {posicion_futura:.2f}")
    print(f"Suavizado (T=2 corregido): {posicion_pasada_suavizada:.2f}")

tareas_temporales_ia()