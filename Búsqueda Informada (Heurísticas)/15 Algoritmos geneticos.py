import random
OBJETIVO = 100 # La suma que queremos alcanzar
TAMANO_POBLACION = 10 # Cuántas soluciones tenemos a la vez
LONGITUD_GENES = 5 # Cuántos números tiene cada solución
TASA_MUTACION = 0.1 # Probabilidad de que un número cambie al azar
GENERACIONES = 50 # Cuántas veces evolucionaremos la población

def calcular_fitness(individuo):
   
    suma = sum(individuo)
    return abs(OBJETIVO - suma)

def crear_individuo():
   #Solucion aleatoria
    return [random.randint(0, 50) for _ in range(LONGITUD_GENES)]

def cruce(padre1, padre2):
   
    punto_corte = random.randint(1, LONGITUD_GENES - 1)
    hijo = padre1[:punto_corte] + padre2[punto_corte:]
    return hijo

def mutacion(individuo):
    #Cambia un gen al azar basado en la tasa de mutación
    for i in range(len(individuo)):
        if random.random() < TASA_MUTACION:
            individuo[i] = random.randint(0, 50)
    return individuo

# 1. Crear población inicial
poblacion = [crear_individuo() for _ in range(TAMANO_POBLACION)]

print(f"Buscando una combinación de {LONGITUD_GENES} números que sumen {OBJETIVO}...\n")

# CICLO EVOLUTIVO
for gen in range(GENERACIONES):
    # 2. Evaluación: Ordenar la población por su fitness (el menor error primero)
    poblacion = sorted(poblacion, key=lambda ind: calcular_fitness(ind))
    
    mejor_actual = poblacion[0]
    error = calcular_fitness(mejor_actual)
    
    if gen % 10 == 0:
        print(f"Generación {gen}: Mejor individuo {mejor_actual} (Suma: {sum(mejor_actual)}, Error: {error})")

    # Si encontramos la solución perfecta, nos detenemos
    if error == 0:
        print(f"\nSolución óptima encontrada en la generación {gen}")
        break

    # 3. Selección: Nos quedamos con los 2 mejores para procrear
    nueva_poblacion = [poblacion[0], poblacion[1]]

    # 4 y 5. Cruce y Mutación para completar la nueva población
    while len(nueva_poblacion) < TAMANO_POBLACION:
        padre1, padre2 = random.sample(poblacion[:5], 2) # Seleccionamos de los mejores 5
        hijo = cruce(padre1, padre2)
        hijo = mutacion(hijo)
        nueva_poblacion.append(hijo)

    poblacion = nueva_poblacion

print(f"\nResultado Final: {poblacion[0]} Suma: {sum(poblacion[0])}")