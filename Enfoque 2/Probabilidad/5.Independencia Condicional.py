# Queremos saber la probabilidad de dos efectos (E1 y E2) dada una Causa (C)
# Si E1 y E2 son independientes dado C, entonces:
# P(E1, E2 | C) = P(E1 | C) * P(E2 | C)

def calcular_probabilidad_simplificada():
    # Supongamos que C es Tener Gripe
    # E1 es Tener Fiebre y E2 es Tener Tos
    
    prob_gripe = 0.1
    
    # Probabilidades condicionadas a la causa
    p_fiebre_dado_gripe = 0.8
    p_tos_dado_gripe = 0.7
    
    # Cálcuo con independencia condicional
    # Mltiplicamos sus relaciones individuales con la gripe
    p_ambos_sintomas_si_hay_gripe = p_fiebre_dado_gripe * p_tos_dado_gripe
    
    print(f"Si el paciente tiene gripe:")
    print(f"Probabilidad de tener fiebre y tos: {p_ambos_sintomas_si_hay_gripe:.2%}")
    print("\nComentario: Se calculó multiplicando probabilidades directas,")
    print("ignorando cualquier relación secreta entre fiebre y tos.")


calcular_probabilidad_simplificada()