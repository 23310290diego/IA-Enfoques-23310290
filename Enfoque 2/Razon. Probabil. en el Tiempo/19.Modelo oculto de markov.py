# Estado Oculto (X): {Lluvia, No Lluvia}
# Observación (E): {Trae Paraguas, No Trae Paraguas}

def simular_hmm_paraguas(dias=5):
    import random
    
    # Modelo de Transición: P(Xt | Xt-1)
    # Si ayer llovió, hoy llueve con 70% de probabilidad. Si ayer no llovió, hoy llueve con 30%.
    transicion = {"Lluvia": 0.7, "No Lluvia": 0.3} 
    
    # Modelo de Emisión (Sensor): P(Et | Xt)
    # Si LLUEVE, trae paraguas el 90%. Si NO LLUEVE, el 20%
    emision = {"Lluvia": 0.9, "No Lluvia": 0.2}
    
    estado_oculto = "Lluvia" # Estado inicial
    
    print(f"{'Día':<5} | {'Realidad (Oculta)':<18} | {'Observación (Visible)':<20}")
    print("-" * 50)
    
    for d in range(1, dias + 1):
        # El estado cambia 
        prob = transicion["Lluvia"] if estado_oculto == "Lluvia" else 0.3
        estado_oculto = "Lluvia" if random.random() < prob else "No Lluvia"
        
        # Evidencia 
        prob_e = emision[estado_oculto]
        trae_paraguas = "☂️ Trae paraguas" if random.random() < prob_e else "☀️ No trae"
        
        print(f"{d:<5} | {estado_oculto:<18} | {trae_paraguas:<20}")

simular_hmm_paraguas()