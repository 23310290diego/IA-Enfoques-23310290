import random

def ascencion_colinas(estado_inicial, funcion_objetivo, obtener_vecinos):

    # Se establece el punto de partida
    estado_actual = estado_inicial
    valor_actual = funcion_objetivo(estado_actual)

    print(f"Iniciando en el estado: {estado_actual} con valor: {valor_actual}")

    while True:
        # Se obtienen los vecinos del estado actual
        vecinos = obtener_vecinos(estado_actual)
        if not vecinos:
            break

        # Se busca el mejor vecino (el que tenga el valor de función más alto)
        # Aquí se aplica la lógica de 'ascensión': solo importa el mejor inmediato.
        mejor_vecino = max(vecinos, key=lambda v: funcion_objetivo(v))
        mejor_valor_vecino = funcion_objetivo(mejor_vecino)

        # CONDICIÓN DE PARADA: 
        # Si el mejor vecino no es mejor que el estado actual, se ha llegado a una 'cima'.
        if mejor_valor_vecino <= valor_actual:
            print("Se ha alcanzado una cima (máximo local o global).")
            break

        # MOVIMIENTO: El mejor vecino se convierte en el nuevo estado actual.
        estado_actual = mejor_vecino
        valor_actual = mejor_valor_vecino
        print(f"Subiendo a: {estado_actual} con valor: {valor_actual}")

    return estado_actual, valor_actual

# --- CONFIGURACIÓN DE UN EJEMPLO SIMPLE ---

# La función objetivo define "la altura". Queremos el número más alto.
def mi_funcion_objetivo(x):
    # Ejemplo: una parábola invertida donde el máximo es 100
    return -(x - 10)**2 + 100

# Se define cómo encontrar vecinos (números cercanos)
def mis_vecinos(x):
    return [x - 1, x + 1]

# EJECUCIÓN: Se inicia en un punto aleatorio, por ejemplo, 0.
estado_final, valor_final = ascencion_colinas(0, mi_funcion_objetivo, mis_vecinos)
print(f"\nResultado: El algoritmo se detuvo en {estado_final} con un valor de {valor_final}")