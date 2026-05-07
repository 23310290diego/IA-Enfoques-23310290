import math

def agrupar_datos_simple():
    # Datos: (x, y) que representan características de clientes
    puntos = [(1, 2), (1, 1), (10, 10), (10, 8)]
    
    # Suponer que queremos 2 grupos e inicializamos sus centros
    centro_a = (0, 0)
    centro_b = (12, 12)
    
    for i in range(3): # Iteramos para ajustar los grupos
        grupo_a, grupo_b = [], []
        
        for p in puntos:
            # Calculamos distancia Euclídea a cada centro
            dist_a = math.sqrt((p[0]-centro_a[0])**2 + (p[1]-centro_a[1])**2)
            dist_b = math.sqrt((p[0]-centro_b[0])**2 + (p[1]-centro_b[1])**2)
            
            # Asignamos al más cercano
            if dist_a < dist_b:
                grupo_a.append(p)
            else:
                grupo_b.append(p)
        
        # El aprendizaje ocurre al mover el centro al promedio del grupo
        if grupo_a:
            centro_a = (sum(x for x,y in grupo_a)/len(grupo_a), sum(y for x,y in grupo_a)/len(grupo_a))
        if grupo_b:
            centro_b = (sum(x for x,y in grupo_b)/len(grupo_b), sum(y for x,y in grupo_b)/len(grupo_b))
            
        print(f"Iteración {i+1}: Centro A en {centro_a}, Centro B en {centro_b}")

agrupar_datos_simple()