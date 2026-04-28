def red_bayesiana_dinamica(creencia_ayer, observacion_hoy):
    #P(Clima_t | Clima_t-1)
    #Si ayer llovió, hay 70% de que hoy llueva, si no, solo 30%
    transicion = {
        "Lluvia": {"Lluvia": 0.7, "Sol": 0.3},
        "Sol":    {"Lluvia": 0.3, "Sol": 0.7}
    }

    #P(Sensor | Clima)
    #El sensor dice húmedo ,si llueve, acierta 90%,si hace sol, falla y dice húmedo 20%.
    sensor = {
        "Lluvia": {"Humedo": 0.9, "Seco": 0.1},
        "Sol":    {"Humedo": 0.2, "Seco": 0.8}
    }

    #Paso de tiempo
    p_lluvia_pred = (creencia_ayer["Lluvia"] * transicion["Lluvia"]["Lluvia"]) + \
                    (creencia_ayer["Sol"] * transicion["Sol"]["Lluvia"])
    p_sol_pred = 1 - p_lluvia_pred

    #Incorporar evidencia de hoy
    p_lluvia_final = p_lluvia_pred * sensor["Lluvia"][observacion_hoy]
    p_sol_final = p_sol_pred * sensor["Sol"][observacion_hoy]

    #Normalizar
    total = p_lluvia_final + p_sol_final
    return {"Lluvia": p_lluvia_final / total, "Sol": p_sol_final / total}

ayer = {"Lluvia": 0.5, "Sol": 0.5} # No sabemos nada de ayer
hoy = red_bayesiana_dinamica(ayer, "Humedo")

print(f"Probabilidades para hoy tras ver 'Húmedo':")
print(f"Lluvia: {hoy['Lluvia']:.2%}, Sol: {hoy['Sol']:.2%}")