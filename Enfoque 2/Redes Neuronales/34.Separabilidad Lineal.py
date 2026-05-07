# Intentaremos encontrar una línea que separe el XOR.
# Lógica XOR: (0,0)->0, (1,1)->0  vs  (0,1)->1, (1,0)->1

def prueba_separabilidad_lineal():
    # Definimos los pesos y el umbral de una neurona simple
    # Intentamos configurar la neurona para que "entienda" el XOR
    w1, w2, bias = 0.5, 0.5, -0.7 
    
    entradas = [[0,0], [0,1], [1,0], [1,1]]
    esperado = [0, 1, 1, 0] # Resultado real del XOR
    
    print(f"{'Entrada':<10} | {'Deseado':<10} | {'Suma (z)':<10} | {'Predicción':<12}")
    print("-" * 50)
    
    for i in range(len(entradas)):
        x1, x2 = entradas[i]
        # Operación lineal: z = x1*w1 + x2*w2 + b
        # Esto representa una línea recta en el plano
        z = (x1 * w1) + (x2 * w2) + bias
        
        # Función de activación escalón (Heaviside)
        prediccion = 1 if z >= 0 else 0
        
        resultado = "Correcto" if prediccion == esperado[i] else "ERROR"
        print(f"{str(entradas[i]):<10} | {esperado[i]:<10} | {z:<10.2f} | {prediccion:<12} -> {resultado}")

# Es imposible que los 4 resultados sean Correcto al mismo tiempo
prueba_separabilidad_lineal()