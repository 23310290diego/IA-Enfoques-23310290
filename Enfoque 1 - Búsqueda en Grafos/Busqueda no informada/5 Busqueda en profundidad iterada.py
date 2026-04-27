# Grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': [], 'F': [], 'G': [], 'H': [], 'I': []
}

def dls_para_iterativa(nodo, objetivo, limite, profundidad_actual):
    #Función auxiliar que realiza la búsqueda limitada para un nivel específico.
    # PRUEBA DE OBJETIVO: Se verifica si el nodo es la meta.
    if nodo == objetivo:
        return [nodo]
    
    # Se detiene si se alcanza el límite de esta iteración
    if profundidad_actual >= limite:
        return None

    for vecino in grafo.get(nodo, []):
        camino = dls_para_iterativa(vecino, objetivo, limite, profundidad_actual + 1)
        if camino:
            return [nodo] + camino
    return None

def busqueda_profundidad_iterativa(inicio, objetivo, limite_maximo):
    """
    Ejecuta la búsqueda incrementando el límite progresivamente.
    """
    # Se recorren todos los niveles desde 0 hasta el límite máximo
    for limite in range(limite_maximo + 1):
        print(f"--- Probando con Límite de Profundidad: {limite} ---")
        
        # Se reinicia la búsqueda desde la raíz en cada nueva iteración de límite
        resultado = dls_para_iterativa(inicio, objetivo, limite, 0)
        
        if resultado:
            return resultado, limite
            
    return None, None

# EJECUCIÓN
nodo_inicio = 'A'
nodo_meta = 'H'
max_profundidad_a_probar = 3

ruta, nivel = busqueda_profundidad_iterativa(nodo_inicio, nodo_meta, max_profundidad_a_probar)

if ruta:
    print(f"\n¡Objetivo encontrado!")
    print(f"Ruta: {ruta}")
    print(f"Encontrado en el nivel: {nivel}")
else:
    print("\nNo se encontró el objetivo en los límites probados.")