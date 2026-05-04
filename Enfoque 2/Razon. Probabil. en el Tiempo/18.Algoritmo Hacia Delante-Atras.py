# El algoritmo combina un mensaje 'f' (forward) y uno 'b' (backward).

def forward_backward_demo():
    # Supongamos una secuencia de 3 pasos , suavizar el paso k=2.
    
    # Mensaje Forward (f1:2): Probabilidad del estado en k=2 dada evidencia [1, 2]
    # La IA cree que hay 60% de probabilidad de estar en estado A
    f_k = {"A": 0.6, "B": 0.4}
    
    # Mensaje Backward (b3:2): Probabilidad de la evidencia en k=3 dado el estado en k=2
    # El futuro sugiere que el estado en k=2 era más probablemente B
    b_k = {"A": 0.2, "B": 0.8}
    
    # COMBINACIÓN 
    # Multiplicamos ambos mensajes y normalizamos
    prob_sin_norm = {estado: f_k[estado] * b_k[estado] for estado in f_k}
    suma = sum(prob_sin_norm.values())
    
    prob_suavizada = {estado: p / suma for estado, p in prob_sin_norm.items()}
    
    print(f"Estimación Forward (Solo pasado): {f_k}")
    print(f"Estimación Backward (Solo futuro): {b_k}")
    print(f"RESULTADO SUAVIZADO (Combinado): {prob_suavizada}")

forward_backward_demo()