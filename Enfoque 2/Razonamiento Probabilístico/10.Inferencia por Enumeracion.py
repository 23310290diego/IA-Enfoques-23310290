# Queremos saber P(Lluvia | Pasto_Mojado).
# El algoritmo 'enumera' todos los casos posibles de las variables ocultas.

def inferencia_enumeracion():
    # Definimos la Distribución Conjunta (Lluvia, Aspersor, Pasto_Mojado)
    # Formato: (Lluvia, Aspersor, Mojado) : Probabilidad
    conjunta = {
        (True,  True,  True):  0.08,
        (True,  False, True):  0.12,
        (False, True,  True):  0.16,
        (False, False, True):  0.04,
        # Casos donde el pasto NO está mojado (los ignoraremos por la evidencia)
        (True,  True,  False): 0.01,
        (False, False, False): 0.59 
    }

    print("Evidencia observada: Pasto_Mojado = True")
    
    # Sumamos casos donde Lluvia es True (dado que el pasto está mojado)
    suma_lluvia_true = 0.08 + 0.12 # (T, T, T) y (T, F, T)
    
    # Sumamos casos donde Lluvia es False (dado que el pasto está mojado)
    suma_lluvia_false = 0.16 + 0.04 # (F, T, T) y (F, F, T)
    
  
    # El total de la evidencia P(Mojado) es 0.08 + 0.12 + 0.16 + 0.04 = 0.40
    total_evidencia = suma_lluvia_true + suma_lluvia_false
    
    prob_final_lluvia = suma_lluvia_true / total_evidencia
    
    print(f"Probabilidad P(Lluvia | Mojado) calculada por enumeración: {prob_final_lluvia:.2%}")


inferencia_enumeracion()