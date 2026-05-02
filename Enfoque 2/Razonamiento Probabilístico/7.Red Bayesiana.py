# Estructura: [Lluvia] -> [Tráfico] -> [Tarde]
# El nodo 'Tarde' depende directamente de Tráfico
# El nodo 'Tráfico' depende directamente de Lluvia

def simular_red_bayesiana(lluvia_detectada):
    # Probabilidades del primer nodo (Lluvia)
    # P(Lluvia) ya viene definida por la observación del usuario
    
    # Tabla de Probabilidad Condicionada (CPT) para Tráfico
    # Si llueve, hay 80% de tráfico. Si no, solo 20%.
    if lluvia_detectada:
        prob_trafico = 0.8
    else:
        prob_trafico = 0.2
        
    # Simulación de Tráfico (basada en la probabilidad anterior)
    hay_trafico = True if random.random() < prob_trafico else False
    
    # CPT para Llegar Tarde
    # Si hay tráfico, 90% de probabilidad de llegar tarde. Si no, 10%.
    if hay_trafico:
        prob_tarde = 0.9
    else:
        prob_tarde = 0.1
        
    return hay_trafico, prob_tarde


import random
lloviendo = True
trafico, riesgo_tarde = simular_red_bayesiana(lloviendo)

print(f"Escenario: ¿Está lloviendo? {lloviendo}")
print(f"Resultado del nodo intermedio (Tráfico): {trafico}")
print(f"Probabilidad final del nodo (Tarde): {riesgo_tarde:.2%}")