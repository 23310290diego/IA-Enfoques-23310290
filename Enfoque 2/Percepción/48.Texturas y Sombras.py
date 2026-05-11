def analizar_textura():
    # Parche de 3x3 píxeles de una imagen, el centro es el valor de referencia
    parche_textura = [
        [40, 50, 70],
        [30, 50, 80],
        [20, 10, 0]
    ]
    
    print("Intensidades del parche de textura:")
    for fila in parche_textura: print(fila)

    centro = parche_textura[1][1] # El valor es 50
    codigo_binario = ""

    # Comparamos cada vecino con el centro para crear un patrón
    # Si vecino >= centro -> 1 más claro o igual
    # Si vecino < centro  -> 0 más oscuro
    for f in range(3):
        for c in range(3):
            if f == 1 and c == 1: continue # Saltamos el centro
            
            # La IA genera un código que describe el relieve local
            if parche_textura[f][c] >= centro:
                codigo_binario += "1"
            else:
                codigo_binario += "0"

    # El código binario resultante representa la huella digital
    print(f"\nPatrón binario de la textura: {codigo_binario}")
    print(f"Decimal (ID de textura): {int(codigo_binario, 2)}")


analizar_textura()