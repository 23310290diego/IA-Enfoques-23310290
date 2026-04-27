import random

def busqueda_haz_local(k, iteraciones, funcion_objetivo, obtener_vecinos):

    #Generamos K estados aleatorios
    estados_actuales = [random.randint(0, 100) for _ in range(k)]
    
    print(f"Iniciando haz con K={k} en los estados: {estados_actuales}")

    for i in range(iteraciones):
        todos_los_sucesores = []
        
        #Generamos todos los vecinos de todos los estados actuales
        for estado in estados_actuales:
            todos_los_sucesores.extend(obtener_vecinos(estado))
        
        #Evaluamos y nos quedamos solo con los K mejores de la lista global
        #Ordenamos por la función objetivo de mayor a menor
        todos_los_sucesores.sort(key=lambda x: funcion_objetivo(x), reverse=True)
        estados_actuales = todos_los_sucesores[:k]
        
        mejor_valor = funcion_objetivo(estados_actuales[0])
        print(f"Iteración {i+1}: Mejor valor actual es {mejor_valor} (en estado {estados_actuales[0]})")

    return estados_actuales[0], mejor_valor



def mi_funcion_objetivo(x):
    # Una función con varios picos, el máximo real está en 90
    return -(x - 20)**2 + 50 if x < 50 else -(x - 90)**2 + 500

def mis_vecinos(x):
    # Genera un rango de vecinos cercanos
    return [x + i for i in range(-5, 6) if 0 <= x + i <= 100]

# EJECUCIÓN
# Con k=3, el algoritmo tiene 3 oportunidades de caer cerca del pico más alto (90)
mejor_estado, mejor_val = busqueda_haz_local(k=3, 
iteraciones=10, 
funcion_objetivo=mi_funcion_objetivo, 
obtener_vecinos=mis_vecinos)

print(f"\nResultado Final: El haz encontró el estado {mejor_estado} con valor {mejor_val}")