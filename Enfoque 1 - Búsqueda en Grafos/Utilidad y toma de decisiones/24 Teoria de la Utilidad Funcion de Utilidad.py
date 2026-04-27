import math

def funcion_utilidad(dinero, actitud="neutral"):
    #Modela cómo el agente valora el dinero. averso: Valora menos cada dólar extra .neutral: El valor es lineal.
    if actitud == "averso":
        return math.log(dinero + 1) #Curva cóncava
    elif actitud == "buscador":
        return dinero**2 #Curva convexa
    else:
        return dinero #Lineal

def calcular_decision_racional(actitud):
    #Opcion 1: Ganar 50 dólares garantizados
    u_segura = funcion_utilidad(50, actitud)
    
    #Opcion 2: Lotería 50% ganar 100 50% ganar 0
    u_arriesgada = 0.5 * funcion_utilidad(100, actitud) + 0.5 * funcion_utilidad(0, actitud)
    
    print(f"\nAgente {actitud.upper()}:")
    print(f" - Utilidad de opción segura ($50): {u_segura:.2f}")
    print(f" - Utilidad esperada de apuesta ($100 o $0): {u_arriesgada:.2f}")
    
    if u_segura > u_arriesgada:
        return "El agente elige la opción SEGURA."
    else:
        return "El agente elige la APUESTA."

print(calcular_decision_racional("averso"))
print(calcular_decision_racional("neutral"))
print(calcular_decision_racional("buscador"))