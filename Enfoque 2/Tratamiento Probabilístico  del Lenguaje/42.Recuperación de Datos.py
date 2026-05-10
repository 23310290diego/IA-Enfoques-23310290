import math

def calcular_relevancia():
    # Consulta del usuario
    query = ["inteligencia", "artificial"]
    
    # Documentos en la base de datos
    doc1 = "la inteligencia es una capacidad humana"
    doc2 = "el avance en inteligencia artificial es asombroso"
    
    def obtener_score(consulta, texto):
        # Contamos cuántas palabras de la consulta están en el texto
        # (Simulación simple de un vector de pesos)
        conteo = 0
        palabras_texto = texto.lower().split()
        for palabra in consulta:
            if palabra in palabras_texto:
                conteo += 1
        return conteo / len(palabras_texto) # Normalizamos por longitud

    score1 = obtener_score(query, doc1)
    score2 = obtener_score(query, doc2)
    
    print(f"Consulta: {query}")
    print(f"Relevancia Doc 1: {score1:.4f}")
    print(f"Relevancia Doc 2: {score2:.4f}")
    print(f"\nResultado: El Doc 2 es el más relevante.")

calcular_relevancia()