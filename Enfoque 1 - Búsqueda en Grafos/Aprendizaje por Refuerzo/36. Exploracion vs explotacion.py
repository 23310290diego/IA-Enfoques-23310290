import random

def elegir_accion_epsilon(estado, q_table, epsilon):
    # Decide si explorar o explotar.
    # 1. Generar probabilidad aleatoria
    probabilidad = random.random()
    
    if probabilidad < epsilon:
        #EXPLORACIÓN
        print("Explorando: Acción aleatoria elegida.")
        return random.choice([0, 1]) # 0: Izquierda, 1: Derecha
    else:
        #EXPLOTACIÓN
        print("Explotando: Usando el mejor conocimiento previo.")
        valores_q = q_table[estado]
        # Retorna el índice del valor más alto (la mejor acción)
        return 0 if valores_q[0] > valores_q[1] else 1


# En el Estado 0, la IA cree que la Derecha (indice 1) es mejor (valor 5.0)
mi_q_table = {0: [1.2, 5.0]} 

# Simulamos la decisión con un 20% de probabilidad de explorar
accion = elegir_accion_epsilon(estado=0, q_table=mi_q_table, epsilon=0.2)