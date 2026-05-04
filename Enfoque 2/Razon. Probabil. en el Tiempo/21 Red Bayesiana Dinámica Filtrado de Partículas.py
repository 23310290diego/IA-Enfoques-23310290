import random


def filtrar_particulas(iteraciones=5):
    posicion_real = 50.0
    # Inicializamos 1000 partículas en posiciones aleatorias entre 0 y 100
    particulas = [random.uniform(0, 100) for _ in range(1000)]
    
    for i in range(iteraciones):
        # Las partículas se mueven (con un poco de ruido)
        particulas = [p + random.uniform(-1, 1) for p in particulas]
        
        # PESADO (Verosimilitud): Qué tan cerca está cada partícula de la realidad
        # Simulamos una lectura de sensor con ruido
        lectura_sensor = posicion_real + random.uniform(-2, 2)
        
        pesos = []
        for p in particulas:
            distancia = abs(p - lectura_sensor)
            # A menor distancia, mayor peso (importancia)
            pesos.append(1.0 / (distancia + 0.1))
        
        # Remuestreo: Seleccionamos nuevas partículas basadas en sus pesos
        suma_pesos = sum(pesos)
        probabilidades = [w / suma_pesos for w in pesos]
        particulas = random.choices(particulas, weights=probabilidades, k=1000)
        
        estimacion = sum(particulas) / 1000
        print(f"Iteración {i+1}: Posición estimada = {estimacion:.2f}")

filtrar_particulas()