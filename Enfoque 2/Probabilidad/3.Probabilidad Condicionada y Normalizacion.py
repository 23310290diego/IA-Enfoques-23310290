# Queremos saber P(Lluvia | Suelo_Mojado)
# 1. Necesitamos la probabilidad conjunta: P(Lluvia y Suelo_Mojado)
# 2. Necesitamos la probabilidad de la evidencia: P(Suelo_Mojado)

def calcular_probabilidad_condicionada():
    # Datos de ejemplo (Probabilidades conjuntas)
    p_lluvia_y_mojado = 0.14  # Probabilidad de que llueva y el suelo se moje
    p_no_lluvia_y_mojado = 0.06 # Probabilidad de que NO llueva pero el suelo esté mojado (ej. regaron)

    #Probabilidad de la evidencia (Total de suelo mojado) 
    p_evidencia_mojado = p_lluvia_y_mojado + p_no_lluvia_y_mojado # 0.20

    #Cálculo Condicionado 
    #P(A|B) = P(A y B) / P(B)
    prob_final_lluvia = p_lluvia_y_mojado / p_evidencia_mojado
    prob_final_no_lluvia = p_no_lluvia_y_mojado / p_evidencia_mojado

    # Normalización
    # Al dividir entre el total (0.20), estamos normalizando los valores 
    # para que la suma de (0.70 + 0.30) sea igual a 1.0
    
    print(f"Probabilidad de que esté lloviendo dado que el suelo está mojado:")
    print(f"Lluvia: {prob_final_lluvia:.2%}")
    print(f"No Lluvia: {prob_final_no_lluvia:.2%}")
    print(f"Suma total (Normalizada): {prob_final_lluvia + prob_final_no_lluvia}")

# Ejecutar
calcular_probabilidad_condicionada()