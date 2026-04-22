from collections import deque

def bfs_explicado(grafo, inicio, objetivo):
    # Guardamos rutas completas para saber cómo llegamos a cada nodo.
    cola = deque([[inicio]])
    
    # nodos visitados:
    visitados = {inicio}

    while cola:
        # se extrae el primer camino de la fila el más antiguo
        camino = cola.popleft()
        # El nodo actual es el último elemento del camino que estamos siguiendo
        nodo_actual = camino[-1]

        # Prueba si llegamos a la meta
        if nodo_actual == objetivo:
            return camino

        # se ven a los vecinos del nodo actual
        for vecino, costo in grafo.get(nodo_actual, []):
            if vecino not in visitados:
                visitados.add(vecino)
                # Creamos una copia del camino actual y le añadimos el nuevo vecino
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                # Lo mandamos al final de la cola para ser procesado después
                cola.append(nuevo_camino)
                
    return "Objetivo no alcanzado"

grafo_ejemplo = {
    'A': [('B', 1), ('C', 1)],
    'B': [('D', 1), ('E', 1)],
    'C': [('F', 1)],
    'D': [], 'E': [], 'F': []
}

print(f"Resultado BFS: {bfs_explicado(grafo_ejemplo, 'A', 'F')}")