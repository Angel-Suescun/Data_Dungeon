from game.objetos.habilidad import Habilidad

from game.jugador import Jugador
from game.objetos.variacionesBuff import BuffRegeneracion

class GolpePesado(Habilidad):
    def __init__(self) -> None: # Inicializa la habilidad Golpe Pesado
        super().__init__("Golpe Pesado", "Aumenta el daño en 10 por un turno", "assets/images/golpe_pesado.png")

    def activar(self, jugador: Jugador) -> None: # Activa la habilidad Golpe Pesado
        jugador.danio += 10
        print("Usaste Golpe Pesado: daño +10")

class CuracionRapida(Habilidad):
    def __init__(self) -> None: # Inicializa la habilidad Curación Rápida
        super().__init__("Curación Rápida", "Cura 30 puntos de vida", "assets/images/curacion_rapida.png")

    def activar(self, jugador: Jugador) -> None: # Activa la habilidad Curación Rápida
        jugador.vida = min(jugador.vida + 30, jugador.vida_max)
        print("Te curaste 30 puntos de vida")

class DobleGolpe(Habilidad):
    def __init__(self) -> None: # Inicializa la habilidad Doble Golpe
        super().__init__("Doble Golpe", "Realiza dos ataques en un turno", "assets/images/doble_golpe.png")

    def activar(self, jugador: Jugador) -> None: # Activa la habilidad Doble Golpe
        jugador.turnos_extra += 1
        print("Doble Golpe activado: puedes atacar dos veces")

class Invisibilidad(Habilidad):
    def __init__(self) -> None: # Inicializa la habilidad Invisibilidad
        super().__init__("Invisibilidad", "Evita recibir daño por 1 turno", "assets/images/invisibilidad.png")

    def activar(self, jugador: Jugador) -> None: # Activa la habilidad Invisibilidad
        jugador.invisible = True
        print("Eres invisible por un turno")

class EscudoEnergetico(Habilidad):
    def __init__(self) -> None: # Inicializa la habilidad Escudo Energético
        super().__init__("Escudo Energético", "Aumenta la defensa +5", "assets/images/escudo_energetico.png")

    def activar(self, jugador: Jugador) -> None: # Activa la habilidad Escudo Energético
        jugador.defensa += 5
        print("Tu defensa aumentó en +5")

class Regeneracion(Habilidad):
    def __init__(self) -> None: # Inicializa la habilidad Regeneración
        super().__init__("Regeneración", "Recuperas 5 de vida por turno durante 3 turnos", "assets/images/regeneracion.png")

    def activar(self, jugador: Jugador) -> None: # Activa la habilidad Regeneración
        jugador.buff_activos.encolar(BuffRegeneracion())  # Buff separado
        print("Activaste regeneración")

class CargaRelampago(Habilidad):
    def __init__(self) -> None: # Inicializa la habilidad Carga Relámpago
        super().__init__("Carga Relámpago", "Te mueves dos veces seguidas", "assets/images/carga_relampago.png")

    def activar(self, jugador: Jugador) -> None: # Activa la habilidad Carga Relámpago
        jugador.turnos_extra += 1
        print("Carga Relámpago: tienes un movimiento adicional")
        
class AtaqueBasico(Habilidad):
    def __init__(self) -> None: # Inicializa la habilidad Ataque Básico
        super().__init__("Ataque Básico", "Inflige 10 puntos de daño al enemigo", "assets/images/ataque_basico.png")

    def activar(self, jugador: Jugador) -> None: # Activa la habilidad Ataque Básico
        jugador.danio += 10
        print("Ataque Básico activado: infliges 10 puntos de daño")

class Congelacion(Habilidad):
    def __init__(self) -> None: # Inicializa la habilidad Congelación
        super().__init__("Congelación", "Congela al enemigo por un turno", "assets/images/congelacion.png")

    def activar(self, jugador: Jugador) -> None: # Activa la habilidad Congelación
        jugador.enemigo_congelado = True
        print("Enemigo congelado por 1 turno")

class AumentoVelocidad(Habilidad):
    def __init__(self) -> None: # Inicializa la habilidad Aumento de Velocidad
        super().__init__("Aumento de Velocidad", "Aumenta velocidad en +2", "assets/images/aumento_velocidad.png")

    def activar(self, jugador: Jugador) -> None: # Activa la habilidad Aumento de Velocidad
        jugador.velocidad += 2
        print("Tu velocidad aumentó en +2")

class MaestriaArmas(Habilidad):
    def __init__(self) -> None: # Inicializa la habilidad Maestría con Armas
        super().__init__("Maestría con Armas", "Incrementa daño permanente en +5", "assets/images/maestria_armas.png")

    def activar(self, jugador: Jugador) -> None: # Activa la habilidad Maestría con Armas
        jugador.danio += 5
        print("¡Tu dominio con armas mejora: daño +5 permanente!")
