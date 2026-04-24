import heapq

def busqueda_voraz(grafo, heuristica, inicio, objetivo):
    # ESTRUCTURA DE DATOS: Cola de prioridad.
    # Se inserta una tupla: (valor_heuristico, nodo_actual, camino_recorrido)
    # Python ordena automáticamente por el primer elemento (la heurística).
    frontera = [(heuristica[inicio], inicio, [inicio])]
    
    # CONTROL DE VISITADOS: Se utiliza para no procesar el mismo nodo varias veces.
    visitados = set()

    while frontera:
        # SELECCIÓN: Se extrae el nodo que 'parece' estar más cerca de la meta.
        valor_h, nodo_actual, camino = heapq.heappop(frontera)

        # PRUEBA DE OBJETIVO: Se verifica si se ha llegado al destino.
        if nodo_actual == objetivo:
            return camino

        if nodo_actual not in visitados:
            # Se marca el nodo como visitado al expandirlo.
            visitados.add(nodo_actual)

            # EXPANSIÓN: Se evalúan los vecinos del nodo actual.
            for vecino, costo_arista in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    
                    # Se añade a la frontera usando solo la heurística del vecino.
                    # No se suma el costo real del camino, solo importa h(n).
                    heapq.heappush(frontera, (heuristica[vecino], vecino, nuevo_camino))
                    
    return None


# Grafo con conexiones y costos reales
grafo_ejemplo = {
    'A': [('B', 2), ('C', 5)],
    'B': [('D', 4)],
    'C': [('D', 1)],
    'D': []
}

# Heurística: Estimación de distancia en línea recta hasta el objetivo 'D'
# Nota: La meta siempre debe tener un valor de 0.
heuristica_estimada = {
    'A': 10,
    'B': 1,  
    'C': 8,
    'D': 0
}

ruta = busqueda_voraz(grafo_ejemplo, heuristica_estimada, 'A', 'D')
print(f"Camino encontrado por Búsqueda Voraz: {ruta}")