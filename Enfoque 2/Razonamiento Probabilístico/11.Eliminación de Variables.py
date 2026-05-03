# Calcular una probabilidad donde intervienen A y B.
# En lugar de hacer: Suma_A (Suma_B ( P(A) * P(B|A) ))
# Hacemos: P(A) * (Suma_B ( P(B|A) ))  <-- Eliminamos B primero.

def eliminacion_de_variables_basica():
    # Definir factores (tablas pequeñas)
    # Factor de la Causa (A)
    f_a = {"Culpable": 0.1, "Inocente": 0.9}
    
    # Factor de la Evidencia (B) dado A
    # P(Huella | Culpable) = 0.8, P(Huella | Inocente) = 0.1
    f_b_dado_a = {
        ("Culpable", "Huella"): 0.8,
        ("Inocente", "Huella"): 0.1
    }

    print("Objetivo: Calcular probabilidad de evidencia total sin enumerar todo.")

    
    # Eliminar la variable 'A' multiplicando sus factores correspondientes
    prob_final = (f_a["Culpable"] * f_b_dado_a[("Culpable", "Huella")]) + \
                 (f_a["Inocente"] * f_b_dado_a[("Inocente", "Huella")])

    # En una red gigante, este orden de limpiar variables ahorra millones de pasos
    print(f"Probabilidad de encontrar la huella: {prob_final:.2f}")


eliminacion_de_variables_basica()