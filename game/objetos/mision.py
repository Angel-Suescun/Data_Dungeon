

class Mision:
    def __init__(self, titulo: str, descripcion: str, objetivo: callable, recompensa=None): # Constructor de la misión
        self.titulo = titulo
        self.descripcion = descripcion
        self.objetivo = objetivo  # función que recibe el jugador y devuelve True/False
        self.completada = False
        self.recompensa = recompensa

    def __repr__(self) -> str:
        estado = "✓" if self.completada else "○"
        return f"{estado} {self.titulo}"

    def revisar(self) -> bool: # Verifica si la misión puede marcarse como completada
        if not self.completada and self.objetivo():
            self.completada = True
            self.otorgar_recompensa()
            print(f"¡Misión completada: {self.titulo}!")
            return True
        return False
