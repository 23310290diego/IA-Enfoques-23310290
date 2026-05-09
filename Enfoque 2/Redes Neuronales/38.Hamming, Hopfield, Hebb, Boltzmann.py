import numpy as np

def memoria_hebbiana_simple():
    # Patrón a recordar: [1, -1, 1] 
    patron = np.array([1, -1, 1])
    
    # (Regla de Hebb): 
    # La matriz de pesos se crea multiplicando el patrón por sí mismo
    # W = x * x.T (Correlación)
    pesos = np.outer(patron, patron)
    np.fill_diagonal(pesos, 0) # Una neurona no se conecta consigo misma
    
    print("Matriz de memoria (Pesos) creada mediante Hebb:")
    print(pesos)

    # Intentamos recuperar el recuerdo con un patrón ruidoso [1, 0, 1]
    ruido = np.array([1, 0, 1])
    
    # La red piensa: multiplica el ruido por los pesos
    recuperacion = np.dot(pesos, ruido)
    
    # Aplicar activación (Signo) para reconstruir
    resultado = np.sign(recuperacion)
    
    print(f"\nPatrón ruidoso de entrada: {ruido}")
    print(f"Patrón recuperado por la memoria: {resultado}")

memoria_hebbiana_simple()