def encontrar_equilibrio(matriz, acciones_A, acciones_B):
    #matriz[accion_A][accion_B] -> (Pago_A, Pago_B)
    print("Analizando matriz de pagos...")
    
    equilibrios = []

    for a in acciones_A:
        for b in acciones_B:
            pago_a, pago_b = matriz[a][b]
            
            #¿Es la mejor respuesta de A ante la jugada de B?
            mejor_para_A = all(pago_a >= matriz[otra_a][b][0] for otra_a in acciones_A)
            
            #¿Es la mejor respuesta de B ante la jugada de A?
            mejor_para_B = all(pago_b >= matriz[a][otra_b][1] for otra_b in acciones_B)
            
            if mejor_para_A and mejor_para_B:
                equilibrios.append((a, b))

    return equilibrios


acciones = ["Callar", "Traicionar"]
#Matriz: (Utilidad para A, Utilidad para B) Entre más alto, mejor (menos cárcel)
matriz_pagos = {
    "Callar":     {"Callar": (-1, -1), "Traicionar": (-10, 0)},
    "Traicionar": {"Callar": (0, -10), "Traicionar": (-5, -5)}
}

eqs = encontrar_equilibrio(matriz_pagos, acciones, acciones)
print(f"\nEquilibrio(s) de Nash encontrado(s): {eqs}")