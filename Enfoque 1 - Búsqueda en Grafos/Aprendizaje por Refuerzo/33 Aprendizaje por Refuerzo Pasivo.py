def aprendizaje_pasivo_td(trayectoria, alfa=0.1, gamma=0.9):

    #trayectoria: Lista de estados visitados y recompensa recibida, alfa: Tasa de aprendizaje (qué tanto confiamos en lo nuevo) #gamma: Descuento

    utilidades = {s: 0.0 for s, r in trayectoria}
    
    # Recorremos la experiencia del agente
    for i in range(len(trayectoria) - 1):
        s = trayectoria[i][0]      # Estado actual
        r = trayectoria[i][1]      # Recompensa recibida
        s_siguiente = trayectoria[i+1][0] # Estado al que llegó
        
        #Ecuación TD: 
        #Nueva_U = U_actual + alfa * (Recompensa + gamma * U_siguiente - U_actual)
        error = r + (gamma * utilidades[s_siguiente]) - utilidades[s]
        utilidades[s] = utilidades[s] + alfa * error
        
        print(f"Observado {s} -> {s_siguiente}. Nueva utilidad de {s}: {utilidades[s]:.2f}")
    
    return utilidades


#El agente siguió esta ruta fija: Inicio -> Pasillo -> Meta (recompensa 10)
camino_fijo = [("Inicio", -1), ("Pasillo", -1), ("Meta", 10)]

print("El agente pasivo observa y aprende:")
aprendizaje_pasivo_td(camino_fijo)