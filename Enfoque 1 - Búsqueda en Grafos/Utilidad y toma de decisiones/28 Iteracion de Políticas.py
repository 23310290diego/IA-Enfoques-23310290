def iteracion_politicas():
    #Estados: 0 (Cansado), 1 (Descansado)
    #Política inicial: Siempre Esperar (Acción 0)
    politica = [0, 0] 
    utilidades = [0.0, 0.0]
    gamma = 0.9 #Descuento
    
    #Recompensas: [Estado][Acción]
    recompensas = {
        0: {0: 1, 1: 5}, #Cansado: Esperar=+1, Trabajar=+5
        1: {0: 2, 1: 10} #Descansado: Esperar=+2, Trabajar=+10
    }

    for i in range(3):
        print(f"--- Iteración {i} ---")
        #Calcular valor de seguir la política actual
        for s in range(2):
            accion = politica[s]
            utilidades[s] = recompensas[s][accion] + gamma * utilidades[s]
        
        print(f"Utilidades estimadas: {utilidades}")

        #Ver si hay una acción mejor que la de la política actual
        politica_estable = True
        for s in range(2):
            vieja_accion = politica[s]
            #Elegir la acción que maximiza: R + gamma * U
            mejor_accion = max(recompensas[s].keys(), 
            key=lambda a: recompensas[s][a] + gamma * utilidades[s])
            
            if mejor_accion != vieja_accion:
                politica[s] = mejor_accion
                politica_estable = False
        
        print(f"Política actual (0:Esperar, 1:Trabajar): {politica}")
        if politica_estable: break

    return politica

mejor_estrategia = iteracion_politicas()
print(f"\nResultado Final: La mejor política es {mejor_estrategia}")