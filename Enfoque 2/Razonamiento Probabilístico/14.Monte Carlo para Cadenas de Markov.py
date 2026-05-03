import random

# En lugar de generar muestras independientes, saltamos de un estado a otro
# El estado actual depende del estado anterior.

def mcmc_gibbs(iteraciones=1000):
    # Estado inicial aleatorio (Lluvia, Tráfico)
    lluvia = True
    trafico = False
    
    conteo_lluvia = 0
    
    for i in range(iteraciones):
        # Actualizamos Lluvia dado el valor actual de Tráfico
        # P(Lluvia | Trafico) - Valores simplificados para el ejemplo
        prob_lluvia_dado_trafico = 0.7 if trafico else 0.1
        lluvia = random.random() < prob_lluvia_dado_trafico
        
        # Actualizamos Tráfico dado el valor nuevo de Lluvia
        # P(Trafico | Lluvia)
        prob_trafico_dado_lluvia = 0.8 if lluvia else 0.2
        trafico = random.random() < prob_trafico_dado_lluvia
        
        # Contabilizamos el estado actual después de un tiempo de calentamiento
        if i > 200: # Ignoramos los primeros saltos para que la cadena se estabilice
            if lluvia:
                conteo_lluvia += 1
                
    prob_estimada = conteo_lluvia / (iteraciones - 200)
    print(f"Muestras de la cadena: {iteraciones}")
    print(f"Probabilidad estimada de Lluvia mediante MCMC: {prob_estimada:.2%}")


mcmc_gibbs()