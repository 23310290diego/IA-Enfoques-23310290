def actualizar_creencia(creencia_actual, observacion, modelo_sensor):
    #Actualiza la probabilidad de dónde estamos basada en lo que vemos
    nueva_creencia = []
    for i in range(len(creencia_actual)):
        #Probabilidad de estar aquí * Probabilidad de ver eso en este estado
        p_estado = creencia_actual[i] * modelo_sensor[i][observacion]
        nueva_creencia.append(p_estado)
    
    #Normalizar para que la suma sea 1.0 (100%)
    total = sum(nueva_creencia)
    return [p / total for p in nueva_creencia]


#[Celda 1, Celda 2, Celda 3 (Meta/Pared)]
#Creencia inicial: 33% en cada una (No tengo idea de dónde estoy)
creencia = [0.33, 0.33, 0.33]

#El sensor dice veo pared (Estado 2 es el que tiene pared)
#{Estado: {Observacion: Probabilidad}}
modelo = [
    {"Pared": 0.1, "Pasillo": 0.9}, # Celda 1 (lejos de pared)
    {"Pared": 0.1, "Pasillo": 0.9}, # Celda 2 (lejos de pared)
    {"Pared": 0.8, "Pasillo": 0.2}  # Celda 3 (es la pared)
]

print(f"Creencia inicial: {creencia}")
creencia = actualizar_creencia(creencia, "Pared", modelo)
print(f"Creencia tras ver 'Pared': {['%.2f' % p for p in creencia]}")