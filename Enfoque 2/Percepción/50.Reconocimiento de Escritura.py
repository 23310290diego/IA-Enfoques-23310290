def reconocer_digito_escrito():
    # Representamos un 1 escrito a mano en una rejilla de 5x3

    digito_uno = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    
    # Representamos un 0 escrito a mano
    digito_cero = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    def clasificar(matriz):
        # Se cuenta cuánta tinta hay en el centro de la imagen
        # Un 0 suele tener un hueco vacío (0) en el centro
        # Un 1 suele tener tinta (1) en el centro vertical
        centro = matriz[2][1]
        densidad_total = sum(sum(fila) for fila in matriz)
        
        print(f"Analizando trazo... Densidad de tinta: {densidad_total}")
        
        # Lógica de decisión basada en rasgos
        if centro == 0 and densidad_total > 8:
            return "CERO (0)"
        elif centro == 1 and densidad_total < 7:
            return "UNO (1)"
        else:
            return "Carácter no identificado"

    print(f"Resultado 1: {clasificar(digito_uno)}")
    print(f"Resultado 2: {clasificar(digito_cero)}")


reconocer_digito_escrito()