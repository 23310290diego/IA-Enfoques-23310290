import heapq

def busqueda_a_estrella(grafo, heuristica, inicio, objetivo):
    # COLA DE PRIORIDAD: Se ordena por f(n) = g(n) + h(n)
    # Formato: (prioridad_f, costo_g, nodo_actual, camino)
    frontera = [(heuristica[inicio], 0, inicio, [inicio])]
    
    # REGISTRO DE COSTOS: Se guarda el menor costo 'g' hallado para cada nodo.
    costos_conocidos = {inicio: 0}

    while frontera:
        # SELECCIÓN: Se extrae el nodo con el valor f(n) más bajo.
        f_actual, g_actual, nodo_actual, camino = heapq.heappop(frontera)

        # PRUEBA DE OBJETIVO: Se verifica si se ha llegado a la meta.
        if nodo_actual == objetivo:
            return camino, g_actual

        # EXPANSIÓN: Se evalúan los vecinos del nodo.
        for vecino, costo_arista in grafo.get(nodo_actual, []):
            # Se calcula el costo g(n) para este nuevo vecino.
            nuevo_costo_g = g_actual + costo_arista
            
            # Si se descubre un camino nuevo o uno más barato hacia el vecino:
            if vecino not in costos_conocidos or nuevo_costo_g < costos_conocidos[vecino]:
                costos_conocidos[vecino] = nuevo_costo_g
                # Cálculo de f(n) = g(n) + h(n)
                f_total = nuevo_costo_g + heuristica[vecino]
                
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                
                # Se añade a la frontera priorizando por el costo total estimado.
                heapq.heappush(frontera, (f_total, nuevo_costo_g, vecino, nuevo_camino))
                
    return None, float('inf')


grafo_ejemplo = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 10)],
    'C': [('D', 1)],
    'D': []
}
heuristica = {'A': 10, 'B': 1, 'C': 8, 'D': 0}

ruta, costo = busqueda_a_estrella(grafo_ejemplo, heuristica, 'A', 'D')
print(f"Ruta óptima A*: {ruta} con costo total: {costo}")