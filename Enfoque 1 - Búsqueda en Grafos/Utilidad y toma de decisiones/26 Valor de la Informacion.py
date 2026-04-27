def calcular_vpi():
    #Utilidad a ciegas, si no compro paraguas: 50% sol (0) + 50% lluvia (-50) = -25, si compro paraguas: Siempre -5
    #La mejor decisión a ciegas es comprar paraguas (U = -5)
    u_a_ciegas = -5
    
    #Utilidad con información perfecta
    #Si el experto dice "Lloverá": Compro paraguas (U = -5) -> Ocurre el 50% de las veces, si el experto dice "Sol": No compro nada (U = 0) -> Ocurre el 50% de las veces
    u_con_informacion = (0.5 * -5) + (0.5 * 0)
    
    #VPI = Utilidad Con Info - Utilidad A Ciegas
    vpi = u_con_informacion - u_a_ciegas
    
    print(f"Utilidad esperada a ciegas: {u_a_ciegas}")
    print(f"Utilidad esperada con información perfecta: {u_con_informacion}")
    print(f"VALOR DE LA INFORMACIÓN (VPI): {vpi}")
    
    return vpi

7
vpi_final = calcular_vpi()
print(f"\nConclusión: Deberías pagar máximo {vpi_final} monedas por la información.")