from game.objetos.buff import Buff
from game.jugador import Jugador


class BuffVelocidad(Buff):
    def __init__(self) -> None:
        super().__init__("Velocidad Aumentada", ruta_imagen="assets/images/buff_velocidad.png", duracion=3)

    def aplicar(self, jugador: 'Jugador') -> None:
        jugador.velocidad += 2
        print(f"{jugador} gana velocidad +2")

    def remover(self, jugador: 'Jugador') -> None:
        jugador.velocidad -= 2
        print(f"{jugador} pierde velocidad +2")

class BuffFuerza(Buff):
    def __init__(self) -> None:
        super().__init__("Fuerza Potenciada", ruta_imagen="assets/images/buff_fuerza.png", duracion=4)

    def aplicar(self, jugador: 'Jugador') -> None:
        jugador.danio += 5
        print(f"{jugador} gana fuerza +5")

    def remover(self, jugador: 'Jugador') -> None:
        jugador.danio -= 5
        print(f"{jugador} pierde fuerza +5")

class BuffDefensa(Buff):
    def __init__(self) -> None:
        super().__init__("Defensa Reforzada", ruta_imagen="assets/images/buff_defensa.png", duracion=3)

    def aplicar(self, jugador: 'Jugador') -> None:
        jugador.defensa += 3
        print(f"{jugador} gana defensa +3")

    def remover(self, jugador: 'Jugador') -> None:
        jugador.defensa -= 3
        print(f"{jugador} pierde defensa +3")

class BuffInvisibilidad(Buff):
    def __init__(self) -> None:
        super().__init__("Invisibilidad", ruta_imagen="assets/images/buff_invisibilidad.png", duracion=2)

    def aplicar(self, jugador: 'Jugador') -> None:
        jugador.invisible = True
        print(f"{jugador} ahora es invisible")

    def remover(self, jugador: 'Jugador') -> None:
        jugador.invisible = False
        print(f"{jugador} ya no es invisible")


class BuffRegeneracion(Buff):
    def __init__(self) -> None:
        super().__init__("Regeneración", ruta_imagen="assets/images/buff_regeneracion.png", duracion=5)

    def aplicar(self, jugador: 'Jugador') -> None:
        jugador.vida += 5
        if jugador.vida > jugador.vida_max:
            jugador.vida = jugador.vida_max
        print(f"{jugador} se cura 5 puntos de vida")

    def remover(self, jugador):
        print(f"{jugador} ya no se regenera")
