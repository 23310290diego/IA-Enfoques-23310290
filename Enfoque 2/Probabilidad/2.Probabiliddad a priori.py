# Es el conocimiento de fábrica que tiene la IA antes de observar nada
# Aquí definimos la probabilidad de que un servidor falle basándonos en estadísticas históricas

def estimacion_inicial_riesgo():
    # Probabilidad a Priori: Basada en datos históricos generales.
    # P(Fallo) = 0.05 (Históricamente, el 5% de los servidores fallan al mes)
    p_priori_fallo = 0.05
    
    print(f"--- Análisis Inicial ---")
    print(f"Sin revisar este servidor específico, la probabilidad de que esté fallando")
    print(f"basada en nuestra estadística general (A Priori) es: {p_priori_fallo:.2%}")
    
    return p_priori_fallo


# La IA inicia su proceso de razonamiento con este valor.
probabilidad_base = estimacion_inicial_riesgo()

# Si la IA tuviera que tomar una decisión rápida sin sensores:
if probabilidad_base > 0.10:
    print("Acción: Activar protocolo de revisión preventiva.")
else:
    print("Acción: Mantener monitoreo estándar (el riesgo base es bajo).")