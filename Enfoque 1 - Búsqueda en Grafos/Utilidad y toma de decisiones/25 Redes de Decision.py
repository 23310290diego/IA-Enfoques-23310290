def red_decision_helados(pronostico):
    #Probabilidades basadas en el pronóstico (Nodo de Azar)
    #Si el pronóstico es "Soleado", hay 90% de probabilidad de calor.
    prob_calor = 0.9 if pronostico == "Soleado" else 0.2
    prob_frio = 1 - prob_calor

    #Opciones 
    opciones = ["Helado", "Chocolate"]
    
    #Tabla de Utilidad (Nodo de Utilidad / Rombo)
    #[Clima][Decisión] -> Puntos de utilidad
    utilidad = {
        "Calor": {"Helado": 100, "Chocolate": -20},
        "Frio":  {"Helado": -50, "Chocolate": 80}
    }

    mejor_utilidad = -float('inf')
    mejor_opcion = ""

    for opcion in opciones:
        #Calcular Utilidad Esperada (UE) para cada opción
        ue = (prob_calor * utilidad["Calor"][opcion]) + \
             (prob_frio  * utilidad["Frio"][opcion])
        
        print(f"Opción: {opcion} -> Utilidad Esperada: {ue:.1f}")

        if ue > mejor_utilidad:
            mejor_utilidad = ue
            mejor_opcion = opcion

    return mejor_opcion


print(f"Resultado con Pronóstico Soleado: {red_decision_helados('Soleado')}")
print(f"Resultado con Pronóstico Nublado: {red_decision_helados('Nublado')}")