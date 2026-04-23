# Definición del grafo como un diccionario (Lista de adyacencia)
# Cada clave es un nodo y su valor es una lista de sus nodos hijos.
arbol_decision = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}

def busqueda_profundidad_recursiva(grafo, nodo_actual, visitados=None):
    """
    Realiza un recorrido DFS partiendo desde un nodo inicial.
    
    Funcionamiento lógico:
    Se prioriza la profundidad sobre la anchura. Se desciende por el hijo
    izquierdo hasta el final antes de evaluar los hermanos del mismo nivel.
    """
    
    # INICIALIZACIÓN: Se crea el conjunto de visitados si es la primera llamada.
    # El uso de un conjunto (set) permite búsquedas de pertenencia muy rápidas.
    if visitados is None:
        visitados = set()

    # MARCADO: Se añade el nodo actual al conjunto para no procesarlo dos veces.
    visitados.add(nodo_actual)
    
    # ACCIÓN: Se procesa el nodo (en este caso, se imprime en consola).
    print(f"Visitando nodo: {nodo_actual}")

    # EXPLORACIÓN: Se recorren los hijos del nodo actual de forma recursiva.
    # El algoritmo "baja" por la jerarquía antes de moverse lateralmente.
    for hijo in grafo.get(nodo_actual, []):
        if hijo not in visitados:
            # LLAMADA RECURSIVA: Se profundiza en el árbol.
            busqueda_profundidad_recursiva(grafo, hijo, visitados)

# EJECUCIÓN: Se inicia el algoritmo desde la raíz 'A'
print("--- Inicio de Búsqueda en Profundidad (DFS) ---")
busqueda_profundidad_recursiva(arbol_decision, 'A')