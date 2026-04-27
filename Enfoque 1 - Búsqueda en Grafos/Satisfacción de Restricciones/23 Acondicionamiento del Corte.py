def resolver_arbol(nodos_restantes, dominios, grafo):
    print(f"Resolviendo el resto del grafo como árbol: {nodos_restantes}")
    #En un arbol solo necesitamos recorrer de hojas a raíz y luego asignar
    return {nodo: dominios[nodo][0] for nodo in nodos_restantes}

def acondicionamiento_corte(variable_corte, valor_corte, variables_arbol, dominios, grafo):
    print(f"--- Probando con {variable_corte} = {valor_corte} ---")
    
    #Se crea una copia de los dominios para no alterar el original
    nuevos_dominios = {k: v[:] for k, v in dominios.items()}
    
    #Eliminar la variable del corte propagando su valor a los vecinos
    for vecino in grafo[variable_corte]:
        if valor_corte in nuevos_dominios[vecino]:
            nuevos_dominios[vecino].remove(valor_corte)
            if not nuevos_dominios[vecino]:
                print(f"Fallo: {vecino} se quedó sin opciones.")
                return None

    #El resto es un arbol se resuelve fácil
    solucion_arbol = resolver_arbol(variables_arbol, nuevos_dominios, grafo)
    solucion_arbol[variable_corte] = valor_corte
    return solucion_arbol


#Grafo con un ciclo: A-B, B-C, C-A (Triángulo)
# i fijamos 'A', el resto (B-C) es una línea (un árbol).
vars_arbol = ['B', 'C']
var_corte = 'A'
doms = {'A': ['Rojo', 'Verde'], 'B': ['Rojo', 'Verde'], 'C': ['Rojo', 'Verde']}
grafo = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}

#Probar una opción del corte
solucion = acondicionamiento_corte(var_corte, 'Rojo', vars_arbol, doms, grafo)
print(f"Solución final: {solucion}")