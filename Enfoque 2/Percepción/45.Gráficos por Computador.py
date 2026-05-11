import math

def proyectar_3d_a_2d(punto_3d, distancia_focal):
    # Un punto en el mundo real tiene coordenadas (X, Y, Z)
    x_mundo, y_mundo, z_mundo = punto_3d
    
    print(f"Punto en el mundo 3D: X={x_mundo}, Y={y_mundo}, Z={z_mundo}")
    
    # Si el objeto está detrás de la cámara (Z <= 0), no se ve
    if z_mundo <= 0:
        return None, None
        
    # La Proyección Perspectiva simula cómo funciona el ojo humano: Los objetos más lejanos (mayor Z) se ven más pequeños
    
    # La matemática es simple: dividir X e Y por la profundidad Z y multiplicar por la distancia focal (el zoom de la lente)
    
    x_pantalla = (x_mundo * distancia_focal) / z_mundo
    y_pantalla = (y_mundo * distancia_focal) / z_mundo
    
    return x_pantalla, y_pantalla

#Un objeto a 10 metros de distancia
distancia_lente = 1.0 # 1 metro de focal
objeto_lejos = (2, 2, 10)
objeto_cerca = (2, 2, 2)  # Mismo objeto, pero a 2 metros

px1, py1 = proyectar_3d_a_2d(objeto_lejos, distancia_lente)
px2, py2 = proyectar_3d_a_2d(objeto_cerca, distancia_lente)

print("-" * 30)
print(f"Proyección en pantalla del objeto LEJOS: ({px1:.2f}, {py1:.2f})")
print(f"Proyección en pantalla del objeto CERCA: ({px2:.2f}, {py2:.2f})")
print("\nNota: El objeto cerca se proyecta más lejos del centro de la pantalla,")
print("lo que significa que la IA lo 've' más grande.")