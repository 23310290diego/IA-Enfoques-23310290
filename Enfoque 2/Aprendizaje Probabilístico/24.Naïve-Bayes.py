def clasificador_spam_naive():
    # Probabilidades previas (P(H))
    p_spam = 0.5
    p_ham = 0.5 # Correo deseado
    
    # Probabilidades condicionales de palabras: P(Palabra | Clase)
    # Ejemplo: ¿Qué tan probable es ver oferta si es Spam?
    modelo = {
        "Oferta": {"Spam": 0.8, "Ham": 0.1},
        "Reunión": {"Spam": 0.05, "Ham": 0.4}
    }
    
    # Datos del correo nuevo: Contiene oferta
    palabra_detectada = "Oferta"
    
    # Aplicamos Bayes: P(Clase | Palabra) ∝ P(Palabra | Clase) * P(Clase)
    score_spam = modelo[palabra_detectada]["Spam"] * p_spam
    score_ham = modelo[palabra_detectada]["Ham"] * p_ham
    
    # Normalización
    total = score_spam + score_ham
    prob_final_spam = score_spam / total
    
    print(f"Correo con la palabra: '{palabra_detectada}'")
    print(f"Probabilidad de que sea Spam: {prob_final_spam:.2%}")

clasificador_spam_naive()