from game.jugador import Jugador
from estructuras.grafo import Grafo
from estructuras.vertice import Vertice
from estructuras.arreglo import Arreglo
from estructuras.lista import Lista
from estructuras.cola import Cola
from game.enemigos import Enemigo
import random

class Esqueleto(Enemigo):
    def __init__(self, nombre: str, vida: int, posicion: Vertice, inventario: Arreglo, habilidades: Lista, buffs: Cola, ruta: str) -> None: # Inicializa un esqueleto con nombre, vida y posición inicial
        super().__init__(nombre, vida, posicion, inventario, habilidades, buffs, ruta)

    def comportamiento(self, jugador: Jugador, grafo: Grafo) -> None: # Define el comportamiento del esqueleto frente al jugador
        if self.posicion_actual == jugador.posicion_actual:
            self.usar_habilidad(jugador)
        else:
            self.mover(grafo)


class Bruja(Enemigo):
    def __init__(self, nombre: str, vida: int, posicion: Vertice, inventario: Arreglo, habilidades: Lista, buffs: Cola, ruta: str) -> None: # Inicializa una bruja con nombre, vida y posición inicial
        super().__init__(nombre, vida, posicion, inventario, habilidades, buffs, ruta)

    def comportamiento(self, jugador: Jugador, grafo: Grafo) -> None: # Define el comportamiento de la bruja frente al jugador
        if random.random() < 0.5:
            self.usar_habilidad(jugador)
        else:
            self.mover(grafo)


class Golem(Enemigo):
    def __init__(self, nombre: str, vida: int, posicion: Vertice, inventario: Arreglo, habilidades: Lista, buffs: Cola, ruta: str) -> None: # Inicializa un gólem con nombre, vida y posición inicial
        super().__init__(nombre, vida, posicion, inventario, habilidades, buffs, ruta)

    def comportamiento(self, jugador: Jugador, grafo: Grafo) -> None: # Define el comportamiento del gólem frente al jugador
        self.usar_habilidad(jugador)