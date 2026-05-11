#detección de aristas y segmentación
def detectar_aristas():
    # Representamos una imagen con un cambio de color
    # 255 = Blanco, 0 = Negro
    imagen = [
        [255, 255, 0, 0],
        [255, 255, 0, 0],
        [255, 255, 0, 0]
    ]
    
    print("Imagen Original Pared y Sombra:")
    for fila in imagen: print(fila)

    # El mapa de aristas almacenará dónde detectamos el cambio
    aristas = [[0]*4 for _ in range(3)]

    # Calcular el gradiente horizontal: |Píxel_Izquierda - Píxel_Derecha|
    for f in range(3):
        for c in range(1, 3):
            # Calculamos la diferencia de intensidad
            # Un valor alto significa que hay una arista o cambio brusco
            diferencia = abs(imagen[f][c-1] - imagen[f][c+1])
            
            # Si la diferencia supera un umbral se marca la arista
            if diferencia > 100:
                aristas[f][c] = 1 # 1 indica que aquí hay un borde
            else:
                aristas[f][c] = 0

    print("\nMapa de Aristas Detectado (1 = Borde):")
    for fila in aristas:
        print(fila)

# Ejecución
detectar_aristas()