import copy

def forward_checking(csp_dominios, variable_actual, color_asignado, grafo):
    nuevos_dominios = copy.deepcopy(csp_dominios)
    
    #Miramos a los vecinos de la variable que acabamos de colorear
    for vecino in grafo.get(variable_actual, []):
        if color_asignado in nuevos_dominios[vecino]:
            nuevos_dominios[vecino].remove(color_asignado)
            
            #Si un vecino se queda sin colores, esta rama no sirve
            if len(nuevos_dominios[vecino]) == 0:
                return None # Fallo detectado hacia adelante
                
    return nuevos_dominios

def resolver_csp_fc(variables, dominios, asignacion, grafo):
    if len(asignacion) == len(variables):
        return asignacion

    #Seleccionar variable no asignada
    var = [v for v in variables if v not in asignacion][0]

    for valor in dominios[var]:
        #Mirar hacia adelante
        nuevos_dominios = forward_checking(dominios, var, valor, grafo)
        
        if nuevos_dominios is not None:
            #Si el futuro es viable, asignar y seguir
            asignacion[var] = valor
            print(f"Asignando {var} -> {valor}. Dominios reducidos.")
            
            resultado = resolver_csp_fc(variables, nuevos_dominios, asignacion, grafo)
            if resultado:
                return resultado
            
            #Vuelta atrás si falló después
            del asignacion[var]
            
    return None


paises = ['A', 'B', 'C', 'D']
#Solo 2 colores para forzar al algoritmo a trabajar
dominios_iniciales = {p: ['Rojo', 'Azul'] for p in paises}
restricciones = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}

solucion = resolver_csp_fc(paises, dominios_iniciales, {}, restricciones)
print(f"\nSolución: {solucion}")