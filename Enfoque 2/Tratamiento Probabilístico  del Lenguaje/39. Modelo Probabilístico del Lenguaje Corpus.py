from collections import defaultdict, Counter

def entrenar_modelo_bigramas(corpus):
    # El corpus es una lista de frases
    modelo = defaultdict(Counter)
    
    for frase in corpus:
        palabras = frase.split()
        # Recorremos la frase creando pares (palabra_actual, siguiente)
        for i in range(len(palabras) - 1):
            actual = palabras[i]
            siguiente = palabras[i+1]
            modelo[actual][siguiente] += 1
            
    # Convertimos los conteos en probabilidades (0 a 1)
    probabilidades = {}
    for palabra, siguientes in modelo.items():
        total = sum(siguientes.values())
        probabilidades[palabra] = {k: v/total for k, v in siguientes.items()}
        
    return probabilidades

# Corpus de entrenamiento (datos del mundo real)
data = [
    "la inteligencia artificial es potente",
    "la inteligencia es capacidad",
    "el lenguaje es complejo"
]

modelo_prob = entrenar_modelo_bigramas(data)

# Predicción: ¿Qué palabra sigue a inteligencia?
print(f"Probabilidades tras 'inteligencia': {modelo_prob.get('inteligencia', {})}")