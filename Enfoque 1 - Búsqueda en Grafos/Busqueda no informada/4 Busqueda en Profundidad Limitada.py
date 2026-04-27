# Grafo de ejemplo 
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': []
}

def dls_recursivo(nodo, objetivo, limite, profundidad_actual=0):
    # Realiza una búsqueda en profundidad limitada (DLS).
    # SE MUESTRA EL PROCESO: Se indica el nodo y la profundidad actual.
    print(f"Explorando nodo {nodo} en profundidad {profundidad_actual}")

    # PRUEBA DE OBJETIVO: Se verifica si el nodo es la meta.
    if nodo == objetivo:
        return [nodo]

    # COMPROBACIÓN DEL LÍMITE: Se detiene la expansión si se alcanza el límite.
    if profundidad_actual >= limite:
        return None

    # EXPANSIÓN: Se exploran los hijos solo si no se ha superado el límite.
    for vecino in grafo.get(nodo, []):
        camino = dls_recursivo(vecino, objetivo, limite, profundidad_actual + 1)
        if camino:
            # Se construye el camino de retorno si se encontró el objetivo.
            return [nodo] + camino

    return None

# PARÁMETROS: Se busca el nodo 'H' con un límite de profundidad de 2.
nodo_inicio = 'A'
nodo_meta = 'H'
limite_maximo = 2

print(f"--- Iniciando DLS (Límite: {limite_maximo}) ---")
resultado = dls_recursivo(nodo_inicio, nodo_meta, limite_maximo)

if resultado:
    print(f"\nObjetivo encontrado: {resultado}")
else:
    print(f"\nObjetivo no encontrado dentro del límite {limite_maximo}")