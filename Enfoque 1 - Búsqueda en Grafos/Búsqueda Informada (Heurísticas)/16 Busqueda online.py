entorno_desconocido = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

def busqueda_online_dfs(estado_actual, meta, visitados, camino_retorno):
    print(f"Agente en: {estado_actual}")

    if estado_actual == meta:
        print("¡Meta encontrada!")
        return True

    #El agente marca como visitado el lugar donde está parado
    visitados.add(estado_actual)

    #El agente mira a su alrededor 
    vecinos = entorno_desconocido.get(estado_actual, [])

    for vecino in vecinos:
        if vecino not in visitados:
            #El agente se mueve físicamente al vecino
            camino_retorno[vecino] = estado_actual # Guarda cómo volver
            
            if busqueda_online_dfs(vecino, meta, visitados, camino_retorno):
                return True
                
            #Si el camino no llevó a la meta, el agente regresa
            print(f"Regresando de {vecino} hacia {estado_actual}...")

    return False

visitados = set()
retorno = {} # Memoria para saber cómo volver atrás
busqueda_online_dfs('A', 'F', visitados, retorno)