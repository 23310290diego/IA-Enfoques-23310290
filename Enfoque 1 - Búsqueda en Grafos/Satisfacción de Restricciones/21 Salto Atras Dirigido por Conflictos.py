def resolver_con_salto_atras(variables, indice_actual, asignacion, grafo):
    #Si terminamos todas las variables
    if indice_actual == len(variables):
        return True, None

    var_actual = variables[indice_actual]
    
    #Simula que esta variable mantiene un conjunto de conflictos
    #En un caso real, esto se llena dinámicamente
    conjunto_conflictos = set()

    for valor in ["Rojo", "Azul"]:
        # Verificamos si el valor es seguro
        conflicto = obtener_conflicto(var_actual, valor, asignacion, grafo)
        
        if conflicto is None:
            asignacion[var_actual] = valor
            exito, salto_hacia = resolver_con_salto_atras(variables, indice_actual + 1, asignacion, grafo)
            
            if exito: return True, None
            
            #Si regresamos con una orden de salto, verificamos si es para nosotros
            if salto_hacia is not None and salto_hacia != var_actual:
                return False, salto_hacia
            
            del asignacion[var_actual]
        else:
            #Si hay conflicto, registramos qué variable lo causó
            conjunto_conflictos.add(conflicto)

    #Si agotamos valores, saltamos a la variable más reciente que nos causó problemas
    if conjunto_conflictos:
        mas_reciente = max(conjunto_conflictos, key=lambda v: variables.index(v))
        print(f"!!! Error en {var_actual}. Saltando atrás hasta: {mas_reciente}")
        return False, mas_reciente

    return False, None

def obtener_conflicto(var, val, asignacion, grafo):
    for vecino in grafo.get(var, []):
        if vecino in asignacion and asignacion[vecino] == val:
            return vecino
    return None


vars_ejemplo = ['A', 'B', 'C', 'D']
restricciones = {'D': ['A']} # D solo choca con A (un error en D debería saltar hasta A)
# (A=Rojo, B=Rojo, C=Rojo, D=??) -> Si D falla, no sirve de nada cambiar B o C.
resolver_con_salto_atras(vars_ejemplo, 0, {}, restricciones)