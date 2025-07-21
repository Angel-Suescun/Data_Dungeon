from  abc import ABC, abstractmethod


class Buff(ABC):
    def __init__(self, nombre: str, ruta_imagen: str, duracion: int) -> None:
        self.nombre = nombre
        self.duracion = duracion
        self.ruta_imagen = ruta_imagen

    def __repr__(self) -> str:
        return f"{self.nombre} ({self.duracion} turnos)"

    @abstractmethod
    def aplicar(self) -> None:
        pass

    @abstractmethod
    def remover(self) -> None:
        pass

    def actualizar(self) -> None:
        self.duracion -= 1
        return self.duracion <= 0  # True si debe eliminarse

