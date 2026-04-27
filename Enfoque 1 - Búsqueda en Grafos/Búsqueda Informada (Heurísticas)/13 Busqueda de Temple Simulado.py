import math
import random

def temple_simulado(estado_inicial, funcion_objetivo, obtener_vecinos, temp_inicial, enfriamiento):

    estado_actual = estado_inicial
    valor_actual = funcion_objetivo(estado_actual)
    
    mejor_estado_global = estado_actual
    valor_mejor_global = valor_actual
    
    temperatura = temp_inicial

    print(f"Inicio: {estado_actual} (Valor: {valor_actual}) | Temp: {temperatura}")

    # El proceso continúa hasta que el metal se "enfría"
    while temperatura > 0.01:
        # Elegimos un vecino al azar
        vecinos = obtener_vecinos(estado_actual)
        vecino = random.choice(vecinos)
        valor_vecino = funcion_objetivo(vecino)
        
        # Calculamos la diferencia de "energía" (calidad)
        # Si delta > 0, el vecino es mejor.
        delta = valor_vecino - valor_actual
        
        # DECISIÓN CRÍTICA:
        # Si el vecino es mejor, lo aceptamos siempre.
        # Si es peor, lo aceptamos con una probabilidad basada en la temperatura.
        if delta > 0 or random.random() < math.exp(delta / temperatura):
            estado_actual = vecino
            valor_actual = valor_vecino
            
            # Guardamos el mejor global histórico
            if valor_actual > valor_mejor_global:
                mejor_estado_global = estado_actual
                valor_mejor_global = valor_actual

        # ENFRIAMIENTO: Reducimos la temperatura en cada paso
        temperatura *= enfriamiento

    return mejor_estado_global, valor_mejor_global


def funcion_con_trampas(x):
    # Una función con un máximo local en 10 y el global en 30
    if 0 <= x <= 15: return -(x - 10)**2 + 100
    else: return -(x - 30)**2 + 400

def mis_vecinos(x):
    return [x - 1, x + 1]

# Empezamos en 10 
mejor_x, mejor_v = temple_simulado(estado_inicial=10, 
                                   funcion_objetivo=funcion_con_trampas, 
                                   obtener_vecinos=mis_vecinos, 
                                   temp_inicial=100.0, 
                                   enfriamiento=0.95)

print(f"\nResultado Final: Mejor estado encontrado {mejor_x} con valor {mejor_v}")