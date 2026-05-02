# Imagina una red de 100 nodos. Para conocer el estado de 'Mi_Nodo',
# solo necesitamos observar su Manto de Markov.

def inferencia_con_manto(padres, hijos, copadres, resto_de_red):
 
    # El Manto de Markov es la frontera de conocimiento
    manto_de_markov = {
        "padres": padres,
        "hijos": hijos,
        "copadres": copadres
    }
    
    print("--- Analizando el Manto de Markov ---")
    for relacion, nodos in manto_de_markov.items():
        print(f"Observando {relacion}: {nodos}")
    
    # La IA ignora el resto de la red porque es irrelevante dado el manto
    print(f"\nIGNORANDO por ser irrelevantes: {resto_de_red}")
    
    # El razonamiento se basa SOLO en los datos del manto
    probabilidad_final = sum(padres) / len(padres) if padres else 0.5
    return probabilidad_final


# Mi_Nodo depende de sus padres [1, 0] (ej. sensores).
# El resto de la red (nodos lejanos) tiene valores que NO afectarán el cálculo.
resultado = inferencia_con_manto(padres=[1, 0], hijos=["Nodo_C"], copadres=["Nodo_D"], resto_de_red=["Nodo_Z", "Nodo_W", "Nodo_X"])

print(f"\nProbabilidad calculada basada solo en el Manto: {resultado}")