from collections import deque

def bfs(grafo, inicio, objetivo):
    # Cola para explorar nodos
    cola = deque([inicio])
    
    # Visitados para no repetir nodos
    visitados = set([inicio])
    
    # Para reconstruir el camino
    padres = {inicio: None}
    
    while cola:
        nodo = cola.popleft()
        
        if nodo == objetivo:
            # Reconstruir camino
            camino = []
            while nodo is not None:
                camino.append(nodo)
                nodo = padres[nodo]
            return camino[::-1]  # invertido
        
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                padres[vecino] = nodo
                cola.append(vecino)
    
    return None  # No hay camino


# Ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS:", bfs(grafo, 'A', 'F')) 