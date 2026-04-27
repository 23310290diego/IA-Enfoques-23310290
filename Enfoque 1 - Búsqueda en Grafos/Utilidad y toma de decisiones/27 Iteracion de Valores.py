def iteracion_valores(recompensas, descuento, iteraciones):
    #Inicialn las utilidades de todos los estados en 0
    utilidades = [0.0] * len(recompensas)
    
    for i in range(iteraciones):
        nuevas_utilidades = utilidades[:]
        for s in range(len(recompensas) - 1): #El último es meta, no se mueve
        #El valor del estado actual es: 
        #Recompensa actual + (Descuento * Utilidad del mejor vecino)
        #Simplificado: el único movimiento es ir a la derecha (s+1)
            nuevas_utilidades[s] = recompensas[s] + descuento * utilidades[s+1]
        
        utilidades = nuevas_utilidades
        print(f"Iteración {i+1}: {['%.2f' % u for u in utilidades]}")
    
    return utilidades


#Celda 0 y 1: castigo por caminar (-1). Celda 2: Meta (+10)
mapa_recompensas = [-1, -1, 10]
#Factor de descuento: 0.9
gamma = 0.9

print("Evolución de la utilidad de los estados:")
utilidades_finales = iteracion_valores(mapa_recompensas, gamma, iteraciones=5)