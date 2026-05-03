# Las reglas de transición (P(Estado_t | Estado_t-1)) son constantes
# No importa si estamos en el segundo 1 o en el 1000

class SistemaEstacionario:
    def __init__(self):
        # Regla fija: Si el sistema está OK, hay 5% de probabilidad de Fallo
        # Esta regla NO cambia con el tiempo
        self.prob_fallo = 0.05
        self.estado_actual = "OK"

    def avanzar_tiempo(self, paso):
        import random
        if self.estado_actual == "OK":
            if random.random() < self.prob_fallo:
                self.estado_actual = "Fallo"
        
        print(f"Tiempo {paso}: El sistema está {self.estado_actual}")

sistema = SistemaEstacionario()
for t in range(1, 6):
    # La IA confía en que la regla (0.05) es la misma en cada paso
    sistema.avanzar_tiempo(t)