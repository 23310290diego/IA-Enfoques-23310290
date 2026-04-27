import heapq

def buscar_costo_uniforme(grafo, inicio, objetivo):
    # ESTRUCTURA DE DATOS: Se utiliza una cola de prioridad (Priority Queue).
    # En Python, heapq siempre mantiene el elemento con el valor más pequeño en la cima.
    # Formato de la tupla: (costo_acumulado, camino_completo)
    cola_prioridad = [(0, [inicio])]
    
    # REGISTRO DE COSTOS: Se almacenan los costos mínimos para llegar a cada nodo.
    # Si se encuentra una ruta más barata a un nodo ya conocido, se actualiza.
    costos_minimos = {inicio: 0}

    while cola_prioridad:
        # SELECCIÓN ÓPTIMA: Se extrae el camino con el costo acumulado más bajo.
        costo_total, camino = heapq.heappop(cola_prioridad)
        nodo_actual = camino[-1]

        # VERIFICACIÓN DE OBJETIVO: En UCS, la meta se comprueba al extraer de la cola.
        # Esto garantiza que no haya un camino más barato aún por procesar.
        if nodo_actual == objetivo:
            return camino, costo_total

        # EXPANSIÓN: Se evalúan las conexiones hacia los nodos vecinos.
        for vecino, costo_arista in grafo.get(nodo_actual, []):
            # Se calcula el costo potencial sumando el costo actual y el de la nueva arista.
            costo_nuevo = costo_total + costo_arista
            
            # Si el vecino no se ha visitado o se ha encontrado una ruta más económica:
            if vecino not in costos_minimos or costo_nuevo < costos_minimos[vecino]:
                costos_minimos[vecino] = costo_nuevo
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                # Se inserta en la cola de prioridad para ser evaluado según su costo.
                heapq.heappush(cola_prioridad, (costo_nuevo, nuevo_camino))
                
    return None, float('inf')

# Grafo con pesos en las aristas (Nodo: [(Vecino, Peso), ...])
grafo_pesado = {
    'A': [('B', 5), ('C', 2)],
    'B': [('D', 1)],
    'C': [('B', 1), ('D', 10)],
    'D': []
}

ruta, costo = buscar_costo_uniforme(grafo_pesado, 'A', 'D')
print(f"Ruta óptima por UCS: {ruta} con un costo total de: {costo}")