import random

def transicion_mdp(estado_actual, accion):
   #Simula un mundo con 20% de probabilidad de error, si ordenas mover hay un 80% de éxito y 20% de quedarte quieto.
    probabilidad = random.random()
    
    if accion == "Mover":
        if probabilidad < 0.8:
            return estado_actual + 1, -1  # Avanza, costo de energía -1
        else:
            return estado_actual, -1      # Se resbala, no avanza, costo -1
    
    if accion == "Esperar":
        return estado_actual, 0           # No gasta energía, no avanza


estado = 0
print(f"Estado inicial: {estado}")

for i in range(5):
    #El agente siempre intenta mover
    nuevo_estado, recompensa = transicion_mdp(estado, "Mover")
    print(f"Intento {i+1}: Acción 'Mover' -> Nuevo Estado: {nuevo_estado} (Recompensa: {recompensa})")
    estado = nuevo_estado