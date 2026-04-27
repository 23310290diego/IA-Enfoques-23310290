from collections import deque

def ac3(csp_dominios, restricciones):
    #Se crea una cola con todos los arcos (conexiones entre variables)
    cola = deque([(u, v) for u in restricciones for v in restricciones[u]])
    
    while cola:
        (x, y) = cola.popleft()
        
        #Se intenta reducir el dominio de x respecto a y
        if revisar(csp_dominios, x, y):
            #Si el dominio de x queda vacío, no hay solución
            if not csp_dominios[x]:
                return False
            
            #Si el dominio de x cambió, sus otros vecinos deben ser revisados
            for z in restricciones[x]:
                if z != y:
                    cola.append((z, x))
    return True

def revisar(dominios, x, y):
    reducido = False
    for valor_x in dominios[x][:]:
        # ¿Existe algún valor_y que sea diferente a valor_x? (Restricción binaria típica)
        if not any(valor_y != valor_x for valor_y in dominios[y]):
            dominios[x].remove(valor_x)
            reducido = True
    return reducido


dominios = {
    'A': [1, 2],
    'B': [1, 2],
    'C': [1]
}
#A conectado a B, B conectado a C
restricciones = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}

print(f"Dominios antes de AC-3: {dominios}")
if ac3(dominios, restricciones):
    print(f"Dominios después de AC-3: {dominios}")