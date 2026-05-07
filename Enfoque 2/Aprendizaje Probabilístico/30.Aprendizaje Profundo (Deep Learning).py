import math

def neurona_profunda(entradas, pesos, sesgo):
    # Suma ponderada: z = (w1*x1 + w2*x2 + ...) + b
    z = sum(e * p for e, p in zip(entradas, pesos)) + sesgo
    
    # Función de activación (Sigmoide)
    # Convierte el valor en una probabilidad entre 0 y 1
    activacion = 1 / (1 + math.exp(-z))
    
    return activacion

# sensores de entrada
datos_sensores = [0.8, 0.2, 0.5]
pesos_sinapticos = [0.4, -0.5, 0.2]
b = -0.1

resultado = neurona_profunda(datos_sensores, pesos_sinapticos, b)
print(f"Activación de la neurona: {resultado:.4f}")