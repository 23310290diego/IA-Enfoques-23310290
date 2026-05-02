import random
#La política es simplemente la probabilidad de saltar
#No calculamos cuánto vale el suelo o el aire, solo si la acción funcionó

def optimizar_politica():
    #Parámetro de la política
    #Iniciamos con 50% de probabilidad de saltar
    probabilidad_saltar = 0.5 
    tasa_de_aprendizaje = 0.1 

    print(f"Política Inicial: Probabilidad de saltar = {probabilidad_saltar:.2f}")

    for intento in range(1, 6):
        #La IA actúa basándose DIRECTAMENTE en su política
        if random.random() < probabilidad_saltar:
            accion = "SALTAR"
            # Supongamos que saltar siempre es la respuesta correcta (da +10)
            recompensa = 10 
        else:
            accion = "QUEDARSE QUIETO"
            #Quedarse quieto es malo (da -5)
            recompensa = -5

        #Ajuste
        #Si la acción fue buena, movemos la perilla para que sea más probable
        #Si fue mala, la movemos hacia el lado opuesto
        if recompensa > 0:
            probabilidad_saltar += tasa_de_aprendizaje
        else:
            probabilidad_saltar -= tasa_de_aprendizaje
        
        #Aseguramos que la probabilidad se mantenga entre 0 y 1
        probabilidad_saltar = max(0.0, min(1.0, probabilidad_saltar))

        print(f"Intento {intento}: Acción: {accion} | Nueva Política: {probabilidad_saltar:.2f}")

# Ejecutamos la optimización
optimizar_politica()