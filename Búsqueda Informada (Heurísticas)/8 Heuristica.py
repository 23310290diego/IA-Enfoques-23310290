import heapq

def busqueda_heuristica_pura(grafo, heuristica, inicio, objetivo):
    
    # COLA DE PRIORIDAD: Se utiliza para extraer siempre el nodo con menor h(n).
    # La tupla contiene: (valor_heuristico, nodo_actual, camino_recorrido)
    frontera = [(heuristica[inicio], inicio, [inicio])]
    
    # CONJUNTO DE VISITADOS: Se utiliza para evitar ciclos y repeticiones.
    visitados = set()

    while frontera:
        # SELECCIÓN: Se extrae el nodo que 'parece' estar más cerca de la meta.
        # Se ignora por completo la distancia recorrida desde el inicio.
        valor_h, nodo_actual, camino = heapq.heappop(frontera)

        # PRUEBA DE OBJETIVO: Se verifica si el nodo extraído es el destino.
        if nodo_actual == objetivo:
            return camino

        # CONTROL DE NODOS: Si el nodo no ha sido expandido previamente, se procesa.
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            # EXPANSIÓN: Se obtienen los sucesores del nodo actual.
            for vecino, costo_real in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    
                    # INSERCIÓN: Se añade a la frontera usando UNICAMENTE h(n).
                    # Se ignora el 'costo_real' de la arista.
                    h_n = heuristica[vecino]
                    heapq.heappush(frontera, (h_n, vecino, nuevo_camino))
                    
    return None
 
grafo_ejemplo = {
    'A': [('B', 10), ('C', 2)],
    'B': [('D', 5)],
    'C': [('D', 20)],
    'D': []
}

# La heurística h(n) es el único factor de decisión.
# Aquí 'B' parece mucho mejor que 'C' para llegar a 'D'.
dict_heuristica = {
    'A': 10,
    'B': 2, 
    'C': 9,
    'D': 0
}

resultado = busqueda_heuristica_pura(grafo_ejemplo, dict_heuristica, 'A', 'D')
print(f"Camino decidido por heurística pura: {resultado}")