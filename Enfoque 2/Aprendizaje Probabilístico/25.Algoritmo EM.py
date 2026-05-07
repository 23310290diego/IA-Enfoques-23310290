import random

def algoritmo_em_basico():
    # Datos observados (dos grupos mezclados que no conocemos)
    datos = [160, 162, 180, 185, 161, 178, 182, 159]
    
    # Parámetros iniciales aleatorios (Medias de dos grupos)
    mu1, mu2 = 150, 190
    
    for i in range(5):
        # A qué grupo pertenece cada dato
        pesos_g1 = []
        pesos_g2 = []
        for d in datos:
            dist1 = abs(d - mu1)
            dist2 = abs(d - mu2)
            # El peso es inversamente proporcional a la distancia
            p1 = 1 / (dist1 + 1e-6)
            p2 = 1 / (dist2 + 1e-6)
            total = p1 + p2
            pesos_g1.append(p1 / total)
            pesos_g2.append(p2 / total)
            
        # Recalcular medias basadas en los pesos 
        mu1 = sum(d * w for d, w in zip(datos, pesos_g1)) / sum(pesos_g1)
        mu2 = sum(d * w for d, w in zip(datos, pesos_g2)) / sum(pesos_g2)
        
        print(f"Iteración {i+1}: Media G1={mu1:.2f}, Media G2={mu2:.2f}")

algoritmo_em_basico()