grafo_con_ciclos = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],  # B conecta de vuelta a A (Ciclo)
    'C': ['A', 'F'],       # C conecta de vuelta a A (Ciclo)
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def busqueda_en_grafos_general(grafo, inicio, objetivo):
    """
    Realiza una búsqueda genérica asegurando que ningún nodo se procese dos veces.
    Este es el esquema base de la 'Búsqueda en Grafos' mencionada en el documento.
    """
    
    # LA FRONTERA: En este ejemplo se usa una lista como fila (comportamiento BFS).
    # Almacena los caminos pendientes de explorar.
    frontera = [[inicio]]
    
    # CONJUNTO DE VISITADOS: Es la pieza clave que convierte una búsqueda en árbol
    # en una búsqueda en grafos. Evita ciclos infinitos.
    visitados = set()

    print(f"Iniciando búsqueda desde {inicio} hasta {objetivo}...")

    while frontera:
        # SELECCIÓN: Se extrae un camino de la frontera.
        camino = frontera.pop(0)
        nodo_actual = camino[-1]

        # PRUEBA DE OBJETIVO: Se verifica si se ha llegado al destino.
        if nodo_actual == objetivo:
            print(f"meta encontrada")
            return camino

        # CONTROL DE REPETICIÓN: Solo se expande el nodo si no ha sido visitado antes.
        if nodo_actual not in visitados:
            print(f"  Expandiendo nodo: {nodo_actual}")
            # Se marca el nodo como visitado al expandirlo.
            visitados.add(nodo_actual)

            # EXPANSIÓN: Se obtienen los vecinos del nodo.
            for vecino in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    # Se añaden los nuevos caminos descubiertos a la frontera.
                    frontera.append(nuevo_camino)
        else:
            print(f"  Nodo {nodo_actual} ya visitado, se ignora para evitar ciclos.")

    return None

# Ejecución del ejemplo
ruta_final = busqueda_en_grafos_general(grafo_con_ciclos, 'A', 'F')
print(f"\nResultado final del camino: {ruta_final}")