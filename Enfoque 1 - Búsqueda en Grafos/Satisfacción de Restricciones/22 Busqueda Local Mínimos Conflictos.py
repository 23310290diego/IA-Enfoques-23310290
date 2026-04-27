import random

def obtener_conflictos(tablero, fila, col, n):
    conflictos = 0
    for c in range(n):
        if c == col: continue
        r = tablero[c]
        # Misma fila o misma diagonal
        if r == fila or abs(r - fila) == abs(c - col):
            conflictos += 1
    return conflictos

def resolver_min_conflictos(n, max_pasos=1000):
    #Cada reina en una columna, fila al azar
    tablero = [random.randint(0, n-1) for _ in range(n)]
    
    for paso in range(max_pasos):
        #Identificar conflictos
        reinas_con_conflicto = [c for c in range(n) if obtener_conflictos(tablero, tablero[c], c, n) > 0]
        
        if not reinas_con_conflicto:
            return tablero # ¡Éxito! No hay conflictos.

        #Elegir una reina con problemas al azar
        col = random.choice(reinas_con_conflicto)
        
        #Buscar la fila en esa columna que minimice los choques
        mejor_fila = tablero[col]
        min_c = obtener_conflictos(tablero, mejor_fila, col, n)
        
        for fila_test in range(n):
            c = obtener_conflictos(tablero, fila_test, col, n)
            if c < min_c:
                min_c = c
                mejor_fila = fila_test
        
        tablero[col] = mejor_fila
        if paso % 100 == 0:
            print(f"Paso {paso}: Conflictos restantes...")

    return None

N = 8
solucion = resolver_min_conflictos(N)
print(f"Tablero final (filas por columna): {solucion}")