import numpy as np

def simular_svm_kernel():
    # Datos en 2D que forman un anillo no separables linealmente
    # Punto cerca del origen (Clase 0) y punto alejado (Clase 1)
    puntos = np.array([[0, 0], [10, 10]]) 
    etiquetas = [0, 1]
    
    # Función de Núcleo RBF (Simulada)
    # Proyecta la distancia a una medida de similitud
    def kernel_rbf(x1, x2, gamma=0.1):
        distancia = np.linalg.norm(x1 - x2)**2
        return np.exp(-gamma * distancia)
    
    # Clasificación de un nuevo punto (5, 5)
    nuevo_punto = np.array([5, 5])
    
    # La IA compara la similitud con los vectores de soporte
    similitud_c0 = kernel_rbf(nuevo_punto, puntos[0])
    similitud_c1 = kernel_rbf(nuevo_punto, puntos[1])
    
    clase_predicha = 0 if similitud_c0 > similitud_c1 else 1
    print(f"Punto (5,5) - Similitud C0: {similitud_c0:.4f}, C1: {similitud_c1:.4f}")
    print(f"Resultado: Clase {clase_predicha}")

simular_svm_kernel()