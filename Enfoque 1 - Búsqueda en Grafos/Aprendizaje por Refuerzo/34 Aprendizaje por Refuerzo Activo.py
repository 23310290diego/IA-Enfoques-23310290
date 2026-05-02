import random

def aprendizaje_activo():
    #Estados: 0 (Inicio), 1 (Pasillo), 2 (Meta)
    utilidades = {0: 0.0, 1: 0.0, 2: 10.0} # La meta ya vale 10
    intentos = 5
    alfa = 0.5 #Tasa de aprendizaje
    estado = 0

    for i in range(intentos):
        # El agente decide: ¿Qué acción me lleva al estado con mayor utilidad?
        # En este caso simplificado: quedarse en 0 o intentar ir a 1
        print(f"Intento {i+1}")
        print(f"Estado actual: {estado}. Utilidades conocidas: {utilidades}")
        
        #El agente elige la mejor opción según lo que sabe (Explotación)
        if utilidades[estado + 1] >= utilidades[estado]:
            accion = "Avanzar"
            nuevo_estado = estado + 1
        else:
            accion = "Quedarse"
            nuevo_estado = estado

        recompensa = -1 #Costo de moverse
        
        #Actualización de utilidad (similar al modo pasivo)
        error = recompensa + utilidades[nuevo_estado] - utilidades[estado]
        utilidades[estado] += alfa * error
        
        print(f"Decisión: {accion}. Nueva utilidad de estado {estado}: {utilidades[estado]:.2f}")
        
        if nuevo_estado == 2:
            print("¡Llegó a la meta!")
            estado = 0 # Reiniciar para el siguiente intento
        else:
            estado = nuevo_estado

aprendizaje_activo()