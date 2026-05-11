def reconocer_objeto():
    # La imagen donde buscamos 
    # El 7 representa una característica clave de un objeto
    escena = [
        [0, 0, 0, 0],
        [0, 7, 7, 0],
        [0, 7, 7, 0],
        [0, 0, 0, 0]
    ]
    
    # La plantilla de lo que queremos encontrar
    plantilla = [
        [7, 7],
        [7, 7]
    ]
    
    print("Buscando el objeto en la escena...")

    # Deslizamos la plantilla sobre la escena 
    for f in range(len(escena) - 1):
        for c in range(len(escena[0]) - 1):
            # Extraemos el trozo de la escena actual
            sub_cuadro = [
                [escena[f][c],   escena[f][c+1]],
                [escena[f+1][c], escena[f+1][c+1]]
            ]
            
            # Si el trozo es idéntico a la plantilla lo encontramos
            # La IA mide la similitud entre ambos
            if sub_cuadro == plantilla:
                print(f"¡OBJETO DETECTADO! En las coordenadas: Fila {f}, Columna {c}")
                return

    print("Objeto no encontrado.")


reconocer_objeto()