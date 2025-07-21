from abc import ABC, abstractmethod

class Objeto(ABC):
    def __init__(self, nombre: str, descripcion:str, imagen_path:str, efecto: str =None) -> None: # Inicializa un objeto con nombre, descripción, imagen y efecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.imagen = imagen_path
        self.efecto = efecto  # función o datos que describen qué hace el objeto

    def __repr__(self) -> str:
        return self.nombre

    @abstractmethod
    def usar(self): # Método abstracto que define cómo se usa el objeto
        pass
