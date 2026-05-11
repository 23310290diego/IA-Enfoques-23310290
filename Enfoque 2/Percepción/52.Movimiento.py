def estimar_movimiento():
    # Cuadro en el tiempo T El objeto 8 está en la posición 1
    frame_t0 = [0, 8, 0, 0, 0]
    
    # Cuadro en el tiempo T+1 El objeto 8 se movió a la posición 3
    frame_t1 = [0, 0, 0, 8, 0]
    
    print(f"Frame T:   {frame_t0}")
    print(f"Frame T+1: {frame_t1}")

    # La IA busca el objeto 8 en el nuevo cuadro
    objeto = 8
    pos_inicial = frame_t0.index(objeto)
    
    # Búsqueda de la nueva posición
    try:
        pos_final = frame_t1.index(objeto)
        # El vector de movimiento es la diferencia de posiciones
        vector_movimiento = pos_final - pos_inicial
        
        print(f"\nAnálisis de movimiento:")
        print(f"- Posición inicial: {pos_inicial}")
        print(f"- Posición final:   {pos_final}")
        
        if vector_movimiento > 0:
            print(f"-> Resultado: Movimiento detectado hacia la DERECHA (Velocidad: {vector_movimiento} px/frame)")
        elif vector_movimiento < 0:
            print(f"-> Resultado: Movimiento detectado hacia la IZQUIERDA")
            
    except ValueError:
        print("-> Resultado: El objeto desapareció de la escena.")

estimar_movimiento()