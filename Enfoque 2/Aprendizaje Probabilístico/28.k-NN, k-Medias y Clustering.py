import math
from collections import Counter

# Logica de k-NN Supervisado
def knn_clasificar(punto_nuevo, datos_entrenamiento, k=3):
    distancias = []
    for p, etiqueta in datos_entrenamiento:
        d = math.dist(punto_nuevo, p)
        distancias.append((d, etiqueta))
    
    # Ordenar por distancia y tomar los k más cercanos
    distancias.sort(key=lambda x: x[0])
    vecinos = [etiqueta for d, etiqueta in distancias[:k]]
    return Counter(vecinos).most_common(1)[0][0]

# Logica de k-Medias No Supervisado)
def k_medias_centros(puntos, k=2):
    # Simplificación: solo mostramos la asignación inicial
    centros = [puntos[0], puntos[-1]]
    grupos = [[] for _ in range(k)]
    
    for p in puntos:
        distancias = [math.dist(p, c) for c in centros]
        indice_cercano = distancias.index(min(distancias))
        grupos[indice_cercano].append(p)
    return grupos


entrenamiento = [((1, 2), "Rojo"), ((2, 1), "Rojo"), ((10, 9), "Azul")]
print(f"k-NN: El punto (2, 2) es {knn_clasificar((2, 2), entrenamiento)}")

puntos_libres = [(1, 2), (2, 1), (10, 9), (11, 10)]
print(f"k-Medias: Grupos encontrados: {k_medias_centros(puntos_libres)}")