def procesar_neurona(entradas, pesos):
    # El procesamiento es una combinación lineal, Producto Punto
    # Representa la integración de señales en el cuerpo celular
    suma_potencial = sum(x * w for x, w in zip(entradas, pesos))
    
    # Decisión simple: si la suma supera el umbral (0), la neurona se activa
    activacion = 1 if suma_potencial > 0 else 0
    
    return activacion

# 2 señales de entrada (estimulantes o inhibitorias)
senales = [1.0, 0.5]
pesos_sinapticos = [0.6, -0.8] # El segundo peso es inhibitorio

resultado = procesar_neurona(senales, pesos_sinapticos)
print(f"Suma potencial: {sum(x*w for x,w in zip(senales, pesos_sinapticos))}")
print(f"¿La neurona dispara (1) o calla (0)?: {resultado}")