from collections import deque
# GRAFO DE EJEMPLO
grafo_red = {
    'A': [('B', 1), ('C', 1)],
    'B': [('A', 1), ('D', 1)],
    'C': [('A', 1), ('E', 1)],
    'D': [('B', 1), ('F', 1)],
    'E': [('C', 1), ('F', 1)],
    'F': [('D', 1), ('E', 1)]
}

def busqueda_bidireccional(grafo, inicio, objetivo):

   #Realiza una búsqueda simultánea desde el inicio y desde el objetivo.
    
    if inicio == objetivo:
        return [inicio]

    # COLAS PARA AMBAS DIRECCIONES: Se utilizan para BFS en ambos extremos.
    # Almacenan el camino recorrido hasta el momento.
    cola_inicio = deque([[inicio]])
    cola_objetivo = deque([[objetivo]])

    # DICCIONARIOS DE VISITADOS: Almacenan {nodo: camino_recorrido}.
    # Permiten verificar rápidamente si las búsquedas se han cruzado.
    visitados_inicio = {inicio: [inicio]}
    visitados_objetivo = {objetivo: [objetivo]}

    while cola_inicio and cola_objetivo:
        # --- EXPANSIÓN DESDE EL INICIO ---
        camino_f = cola_inicio.popleft()
        nodo_f = camino_f[-1]

        for vecino, _ in grafo.get(nodo_f, []):
            if vecino not in visitados_inicio:
                nuevo_camino = camino_f + [vecino]
                visitados_inicio[vecino] = nuevo_camino
                cola_inicio.append(nuevo_camino)

                # SE VERIFICA INTERSECCIÓN: Si el vecino ya fue visitado por la meta.
                if vecino in visitados_objetivo:
                    # Se une el camino de inicio con el camino de meta invertido.
                    return unir_caminos(visitados_inicio[vecino], visitados_objetivo[vecino])

        # --- EXPANSIÓN DESDE EL OBJETIVO ---
        camino_b = cola_objetivo.popleft()
        nodo_b = camino_b[-1]

        for vecino, _ in grafo.get(nodo_b, []):
            if vecino not in visitados_objetivo:
                nuevo_camino = camino_b + [vecino]
                visitados_objetivo[vecino] = nuevo_camino
                cola_objetivo.append(nuevo_camino)

                # SE VERIFICA INTERSECCIÓN: Si el vecino ya fue visitado por el inicio.
                if vecino in visitados_inicio:
                    # Se une el camino de inicio con el camino de meta invertido.
                    return unir_caminos(visitados_inicio[vecino], visitados_objetivo[vecino])

    return None

def unir_caminos(camino_desde_inicio, camino_desde_meta):
    """
    Función auxiliar para combinar las dos mitades del camino encontrado.
    """
    # El camino desde la meta viene en orden inverso (Meta -> Encuentro).
    # Se invierte para que sea (Encuentro -> Meta) y se concatena.
    return camino_desde_inicio + camino_desde_meta[::-1][1:]


resultado = busqueda_bidireccional(grafo_red, 'A', 'F')
print(f"Camino encontrado (Bidireccional): {resultado}")