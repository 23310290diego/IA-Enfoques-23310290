class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables
        self.dominios = dominios
        self.restricciones = restricciones

    def es_consistente(self, variable, valor, asignacion):

        for vecino in self.restricciones.get(variable, []):
            if vecino in asignacion and asignacion[vecino] == valor:
                return False  # Hay un conflicto con un vecino
        return True

#Motor de busqueda

def buscar_solucion(csp, asignacion={}):
    # Si ya asignamos todas las variables, terminamos
    if len(asignacion) == len(csp.variables):
        return asignacion

    #Elegimos la siguiente variable que falta por colorear
    variable_no_asignada = [v for v in csp.variables if v not in asignacion][0]

    #Probamos cada color del dominio
    for valor in csp.dominios[variable_no_asignada]:
        if csp.es_consistente(variable_no_asignada, valor, asignacion):
            asignacion[variable_no_asignada] = valor
            
            #Llamada recursiva para la siguiente variable
            resultado = buscar_solucion(csp, asignacion)
            if resultado is not None:
                return resultado
            
            #Si no funcionó, quitamos la marca 
            del asignacion[variable_no_asignada]

    return None




paises = ["Australia", "Nueva_Zelanda", "Tasmania"]

#Definimos los Dominios (Colores disponibles para cada país)
colores = {p: ["Rojo", "Verde", "Azul"] for p in paises}

#Definimos las Restricciones (Fronteras: quién no puede tener el mismo color)
fronteras = {
    "Australia": ["Nueva_Zelanda"],
    "Nueva_Zelanda": ["Australia", "Tasmania"],
    "Tasmania": ["Nueva_Zelanda"]
}

#Creamos el objeto CSP
mi_problema = CSP(paises, colores, fronteras)

#Corremos el algoritmo
solucion = buscar_solucion(mi_problema)

#Imprimimos el resultado
if solucion:
    print("¡Solución encontrada!")
    for pais, color in solucion.items():
        print(f"{pais}: {color}")
else:
    print("No existe una solución que cumpla las reglas.")