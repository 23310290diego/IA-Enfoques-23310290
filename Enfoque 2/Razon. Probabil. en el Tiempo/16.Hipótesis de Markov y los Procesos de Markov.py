import random

# Definimos una matriz de transición
# Si hoy es Soleado, hay 80% de probabilidad de que mañana sea Soleado
# Si hoy es Lluvioso, hay 70% de probabilidad de que mañana sea Lluvioso

def simular_clima_markov(dias=7):
    estados = ["Soleado", "Lluvioso"]
    estado_actual = "Soleado"  # Punto de partida
    
    print(f"Estado inicial: {estado_actual}")
    
    for dia in range(1, dias + 1):
        # La decisión SOLO depende de estado_actual (Hipótesis de Markov)
        if estado_actual == "Soleado":
            # P(S|S)=0.8, P(L|S)=0.2
            estado_actual = random.choices(estados, weights=[0.8, 0.2])[0]
        else:
            # P(L|L)=0.7, P(S|L)=0.3
            estado_actual = random.choices(estados, weights=[0.3, 0.7])[0]
            
        print(f"Día {dia}: El clima es {estado_actual}")

simular_clima_markov()