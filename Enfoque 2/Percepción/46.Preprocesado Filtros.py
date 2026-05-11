def aplicar_filtro_media():
    # Representamos una imagen con ruido 
    # 10 representa un fondo oscuro uniforme
    imagen_ruidosa = [
        [10, 10, 10, 10, 10],
        [10, 90, 10, 10, 10], 
        [10, 10, 10, 10, 10],
        [10, 10, 10, 10, 10]
    ]
    
    print("Imagen Original (con un punto de ruido '90'):")
    for fila in imagen_ruidosa: print(fila)

    # Creamos una matriz vacía para el resultado
    resultado = [[0]*5 for _ in range(4)]

    # Aplicamos el filtro Kernel 3x3
    # Para cada píxel , promediamos sus vecinos
    for f in range(1, 3):
        for c in range(1, 4):
            # Sumamos el píxel actual y sus 8 vecinos
            suma_vecinos = (
                imagen_ruidosa[f-1][c-1] + imagen_ruidosa[f-1][c] + imagen_ruidosa[f-1][c+1] +
                imagen_ruidosa[f][c-1]   + imagen_ruidosa[f][c]   + imagen_ruidosa[f][c+1] +
                imagen_ruidosa[f+1][c-1] + imagen_ruidosa[f+1][c] + imagen_ruidosa[f+1][c+1]
            )
            
            # Dividimos entre 9, el tamaño del kernel
            # Esto disuelve el valor alto del ruido entre sus vecinos
            resultado[f][c] = int(suma_vecinos / 9)

    print("\nImagen Suavizada (el ruido se ha reducido):")
    for f in range(1, 3):
        print(resultado[f][1:4])


aplicar_filtro_media()