# La variable X representa las caras de un dado. 
# La distribución P(X) asigna un valor a cada cara.

def mostrar_distribucion_dado():
    # En una distribución, la suma de todas las probabilidades DEBE ser 1.0
    # Este dado está 'cargado' hacia el 6
    caras = [1, 2, 3, 4, 5, 6]
    distribucion = {
        1: 0.1, 
        2: 0.1, 
        3: 0.1, 
        4: 0.1, 
        5: 0.1, 
        6: 0.5  
    }

    print("Distribución de Probabilidad P(Cara):")
    for cara, prob in distribucion.items():
        # Visualizamos la distribución con una pequeña barra
        barra = "█" * int(prob * 20)
        print(f"Cara {cara}: [{prob:.1f}] {barra}")

    # Suma de la distribución
    suma_total = sum(distribucion.values())
    print(f"\nSuma total de la distribución: {suma_total} (Validación)")

mostrar_distribucion_dado()