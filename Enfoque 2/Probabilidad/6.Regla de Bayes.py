# Queremos calcular P(Spam | Palabra), que es la probabilidad de que 
# sea Spam dado que contiene una palabra específica (ej. 'Oferta')

def filtro_spam_bayesiano():
    # Probabilidad a Priori: P(Spam)
    # 30% de los correos son spam.
    p_spam = 0.3
    p_no_spam = 0.7

    # Verosimilitud (Likelihood): 
    # P(Palabra | Spam): El 60% de los spam usan la palabra 'Oferta'.
    p_palabra_dado_spam = 0.6
    # P(Palabra | No_Spam): Solo el 10% de los correos buenos la usan.
    p_palabra_dado_no_spam = 0.1

    # 3. Evidencia Total: P(Palabra) 
    # Es la probabilidad total de que aparezca la palabra en cualquier correo.
    p_evidencia = (p_palabra_dado_spam * p_spam) + (p_palabra_dado_no_spam * p_no_spam)

    # 4. APLICACIÓN DE LA REGLA DE BAYES
    # P(Spam | Palabra) = [P(Palabra | Spam) * P(Spam)] / P(Palabra)
    p_final_spam = (p_palabra_dado_spam * p_spam) / p_evidencia

    print(f"--- Resultado del Filtro ---")
    print(f"Probabilidad de que el correo sea SPAM: {p_final_spam:.2%}")

# Ejecutamos el filtro
filtro_spam_bayesiano()