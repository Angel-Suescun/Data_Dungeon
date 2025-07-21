from game.objetos.objeto import Objeto
from game.jugador import Jugador

class Pocion(Objeto):
    def __init__(self, nombre: str, descripcion: str, path_imagen:str, cantidad_recuperacion: int) -> None:
        # Inicializa una poción con nombre, descripción, imagen y cantidad de recuperación
        super().__init__(nombre, descripcion, path_imagen)
        self.cantidad_recuperacion = cantidad_recuperacion

    def usar(self, jugador: 'Jugador') -> None: # Método para usar la poción
        jugador.recuperar_vida(self.cantidad_recuperacion)

class Llave(Objeto):
    def __init__(self, nombre:str, descripcion:str, path_imagen:str, color: str) -> None:
        super().__init__(nombre, descripcion, path_imagen)
        self.color = color

    def usar(self, jugador: 'Jugador') -> None:
        print(f"Llave {self.color} usada para abrir una puerta")

class Arma(Objeto):
    def __init__(self, nombre: str, descripcion:str, path_imagen:str, danio:int)-> None:
        super().__init__(nombre, descripcion, path_imagen)
        self.danio = danio

    def usar(self, jugador: 'Jugador') -> None:
        print(f"{jugador} ataca con {self.nombre} causando {self.danio} de daño")