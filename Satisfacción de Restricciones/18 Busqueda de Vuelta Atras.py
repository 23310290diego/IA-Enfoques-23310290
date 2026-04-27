def es_seguro(tablero, fila, col, n):
    #Verificar fila hacia la izquierda
    for i in range(col):
        if tablero[fila][i] == 1:
            return False

    #Verificar diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    #Verificar diagonal inferior izquierda
    for i, j in zip(range(fila, n, 1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    return True

def resolver_n_reinas(tablero, col, n):
  
    #Si todas las reinas están colocadas, exito
    if col >= n:
        return True

    # Intentar colocar la reina en cada fila de esta columna
    for i in range(n):
        if es_seguro(tablero, i, col, n):
            #Colocamos la reina
            tablero[i][col] = 1
            print(f"Colocando reina en ({i}, {col})")

            #Intentar colocar el resto
            if resolver_n_reinas(tablero, col + 1, n):
                return True

            # Si no funcionó, quitamos la reina
            tablero[i][col] = 0
            print(f"Retrocediendo: quitando reina de ({i}, {col})")

    return False


N = 4 #Tablero de 4x4
tablero_inicial = [[0 for _ in range(N)] for _ in range(N)]

if resolver_n_reinas(tablero_inicial, 0, N):
    print("\n¡Solución encontrada!")
    for fila in tablero_inicial:
        print(fila)
else:
    print("No hay solución.")