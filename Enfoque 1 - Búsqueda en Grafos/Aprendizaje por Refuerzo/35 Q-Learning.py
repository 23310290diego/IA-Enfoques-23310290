import random

#Estados (0, 1, 2) y Acciones (Izquierda, Derecha)
#La Tabla Q empieza llena de ceros
q_table = {0: [0.0, 0.0], 1: [0.0, 0.0], 2: [0.0, 0.0]}
alfa = 0.5   # Tasa de aprendizaje
gamma = 0.9  # Descuento (importancia del futuro)

def entrenar_q_learning(episodios):
    for _ in range(episodios):
        estado = 0
        while estado < 2: #Mientras no llegue a la meta (estado 2)
            #Elegir acción al azar para explorar
            accion = random.choice([0, 1]) # 0: Izquierda, 1: Derecha
            
            #Simular el movimiento
            nuevo_estado = min(2, max(0, estado + (1 if accion == 1 else -1)))
            recompensa = 10 if nuevo_estado == 2 else -1
            
            #ACTUALIZACIÓN DE LA FÓRMULA Q:
            #Q(s,a) = Q(s,a) + alfa * [Recompensa + gamma * max(Q(s_sig)) - Q(s,a)]
            mejor_futuro = max(q_table[nuevo_estado])
            q_table[estado][accion] += alfa * (recompensa + gamma * mejor_futuro - q_table[estado][accion])
            
            estado = nuevo_estado


entrenar_q_learning(100)
print("Tabla Q Final (Estado: [Izquierda, Derecha]):")
for estado, valores in q_table.items():
    print(f"Estado {estado}: {['%.2f' % v for v in valores]}")