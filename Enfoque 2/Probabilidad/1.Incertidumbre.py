import random
# En un mundo perfecto, el sensor diría 'Obstáculo' solo si hay uno
# En el mundo real, hay INCERTIDUMBRE: el sensor puede fallar

def detectar_objeto_con_ruido():
    # El estado real del mundo 
    hay_obstaculo_real = random.choice([True, False])
    
    # El sensor tiene incertidumbre: acierta el 80% de las veces
    if random.random() < 0.8:
        lectura_sensor = hay_obstaculo_real
    else:
        # Aquí ocurre el error debido a la incertidumbre del sensor
        lectura_sensor = not hay_obstaculo_real
        
    return hay_obstaculo_real, lectura_sensor


real, sensor = detectar_objeto_con_ruido()

print(f"LECTURA DEL SENSOR: {sensor}")
print(f"VALOR REAL DEL MUNDO: {real}")

# La IA debe actuar bajo INCERTIDUMBRE
if sensor == True:
    print("Acción de la IA: Frenar (por si acaso, aunque no esté 100% segura)")
else:
    print("Acción de la IA: Avanzar (confiando en la lectura, con un margen de duda)")