from abc import ABC, abstractmethod



class Habilidad(ABC):
    def __init__(self, nombre: str, descripcion: str, ruta_imagen: str) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        self.ruta_imagen = ruta_imagen
        self.desbloqueada = False

    def __repr__(self) -> str:
        return self.nombre

    @abstractmethod
    def activar(self) -> None:
        """Define el efecto de la habilidad sobre el jugador"""
        pass