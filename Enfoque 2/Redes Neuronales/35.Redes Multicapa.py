# RED MULTICAPA: RESOLVIENDO XOR 
import math

def red_multicapa_xor(x1, x2):
    # CAPA OCULTA 2 Neuronas
    # Neurona H1: Actúa como una compuerta OR
    # Neurona H2: Actúa como una compuerta NAND
    
    # Pesos y sesgos pre-entrenados para demostración
    # H1 = x1*20 + x2*20 - 10
    h1_z = (x1 * 20) + (x2 * 20) - 10
    h1_out = 1 / (1 + math.exp(-h1_z)) # Activación Sigmoide
    
    # H2 = x1*-20 + x2*-20 + 30
    h2_z = (x1 * -20) + (x2 * -20) + 30
    h2_out = 1 / (1 + math.exp(-h2_z))
    
    # CAPA DE SALIDA 1 Neurona
    # Combina H1 y H2 para obtener el XOR
    # Salida = H1*20 + H2*20 - 30
    out_z = (h1_out * 20) + (h2_out * 20) - 30
    final_out = 1 / (1 + math.exp(-out_z))
    
    return 1 if final_out > 0.5 else 0

# Prueba de la lógica XOR
print("Probando Red Multicapa para XOR:")
for x in [[0,0], [0,1], [1,0], [1,1]]:
    res = red_multicapa_xor(x[0], x[1])
    print(f"Entrada: {x} -> Salida Red: {res}")