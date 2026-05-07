import math

def funciones_activacion(z):
    # Sigmoide: Para probabilidades
    sigmoide = 1 / (1 + math.exp(-z))
    
    # Tanh: Para centrar datos entre -1 y 1
    tanh = math.tanh(z)
    
    # ReLU: La más usada en Deep Learning
    relu = max(0, z)
    
    return sigmoide, tanh, relu

# Prueba con un valor negativo y uno positivo
val_neg, val_pos = -2.5, 2.5

print(f"{'Función':<10} | {'Entrada -2.5':<12} | {'Entrada 2.5':<12}")
print("-" * 40)
s1, t1, r1 = funciones_activacion(val_neg)
s2, t2, r2 = funciones_activacion(val_pos)

print(f"{'Sigmoide':<10} | {s1:<12.4f} | {s2:<12.4f}")
print(f"{'Tanh':<10} | {t1:<12.4f} | {t2:<12.4f}")
print(f"{'ReLU':<10} | {r1:<12.4f} | {r2:<12.4f}")