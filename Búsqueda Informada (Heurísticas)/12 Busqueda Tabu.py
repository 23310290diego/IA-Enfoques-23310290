def busqueda_tabu(estado_inicial, funcion_objetivo, obtener_vecinos, tamaño_tabu, iteraciones):
    # Se inicializa el estado actual y el mejor estado encontrado hasta ahora
    estado_actual = estado_inicial
    mejor_estado_global = estado_inicial
    valor_mejor_global = funcion_objetivo(estado_inicial)
    
    # LISTA TABÚ: Almacena los estados visitados recientemente (Memoria de corto plazo)
    lista_tabu = [estado_inicial]

    print(f"Inicio en: {estado_inicial} con valor: {valor_mejor_global}")

    for i in range(iteraciones):
        vecinos = obtener_vecinos(estado_actual)
        
        # FILTRADO: Se descartan los vecinos que están en la lista tabú.
        # Esto obliga al algoritmo a moverse a lugares nuevos.
        vecinos_permitidos = [v for v in vecinos if v not in lista_tabu]

        if not vecinos_permitidos:
            print("No hay más vecinos permitidos. Fin de la búsqueda.")
            break

        # SELECCIÓN: Se elige el mejor vecino de los permitidos.
        # Nota: Puede que este vecino sea PEOR que el actual, pero se acepta para explorar.
        mejor_vecino_local = max(vecinos_permitidos, key=lambda v: funcion_objetivo(v))
        valor_vecino_local = funcion_objetivo(mejor_vecino_local)

        # Se actualiza el estado actual
        estado_actual = mejor_vecino_local
        
        # Se registra si este nuevo estado es el mejor que hemos visto en toda la ejecución
        if valor_vecino_local > valor_mejor_global:
            mejor_estado_global = mejor_vecino_local
            valor_mejor_global = valor_vecino_local
            print(f"Iteración {i+1}: ¡Nuevo mejor global encontrado! {mejor_estado_global} (Valor: {valor_mejor_global})")

        # GESTIÓN DE LA LISTA TABÚ: Se añade el estado actual a la lista
        lista_tabu.append(estado_actual)
        
        # Si la lista excede el tamaño máximo, se elimina el elemento más antiguo (FIFO)
        if len(lista_tabu) > tamaño_tabu:
            lista_tabu.pop(0)

    return mejor_estado_global, valor_mejor_global


# Una función con varios "picos" (máximos locales)
def funcion_compleja(x):
    # Esta función tiene un pico pequeño y luego uno más grande
    if x < 10: return x 
    elif x < 20: return 5 # Caída (valle)
    else: return x * 2 # Pico más alto

def mis_vecinos(x):
    return [x - 1, x + 1]

# Sin lista tabú, el algoritmo se quedaría atrapado en 10.
mejor_x, mejor_val = busqueda_tabu(9, funcion_compleja, mis_vecinos, tamaño_tabu=5, iteraciones=30)

print(f"\nResultado Final: Mejor estado {mejor_x} con valor {mejor_val}")