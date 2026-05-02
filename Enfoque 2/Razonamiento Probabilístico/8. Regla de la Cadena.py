# Queremos calcular P(Lluvia, Pasto_Mojado.
# Según la regla, esto es: P(Lluvia) * P(Pasto_Mojado | Lluvia)

def calcular_escenario_completo():
    # Probabilidad de la raíz (Padre): P(Lluvia)
    p_lluvia = 0.2
    
    # Probabilidad condicionada (Hijo): P(Pasto_Mojado | Lluvia)
    # Si llueve, el pasto se moja el 95% de las veces.
    p_mojado_dado_lluvia = 0.95
    
    # Multiplicamos la probabilidad de cada nodo por la de sus padres.
    p_escenario_total = p_lluvia * p_mojado_dado_lluvia
    
    print(f"Probabilidad de que llueva y el pasto se moje:")
    print(f"P(Lluvia) * P(Mojado | Lluvia) = {p_lluvia} * {p_mojado_dado_lluvia}")
    print(f"Resultado Final: {p_escenario_total:.4f} (o {p_escenario_total:.2%})")


calcular_escenario_completo()