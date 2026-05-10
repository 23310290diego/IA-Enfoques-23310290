import re

def extractor_info_basico(texto):
    # 1. NER Simple: Buscar nombres (Palabras que empiezan con Mayúscula)
    # 2. NER Simple: Buscar fechas (Formato DD/MM/AAAA)
    
    nombres = re.findall(r'\b[A-Z][a-z]+\b', texto)
    fechas = re.findall(r'\d{2}/\d{2}/\d{4}', texto)
    
    # Simulación de extracción de relación
    entidades = {"Personas": nombres, "Fechas": fechas}
    
    return entidades

# Texto de entrada (No estructurado)
noticia = "Elon visitó la oficina de SpaceX el 12/05/2024 para revisar los cohetes."

datos_estructurados = extractor_info_basico(noticia)

print(f"Texto original: {noticia}")
print("-" * 30)
print(f"Datos Extraídos (Estructurados):")
for categoria, valores in datos_estructurados.items():
    print(f"  {categoria}: {valores}")