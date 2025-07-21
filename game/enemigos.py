from abc import ABC, abstractmethod
import random
from estructuras.grafo import Grafo
from estructuras.pila import Pila
from estructuras.lista import Lista
from estructuras.cola import Cola
from estructuras.arreglo import Arreglo
from estructuras.nodo import Nodo
from estructuras.vertice import Vertice
from game.jugador import Jugador
from game.objetos.buff import Buff


class Enemigo(ABC):
    def __init__(self, nombre: str, vida: int, posicion: Vertice, inventario: Arreglo, habilidades: Lista, buffs: Cola, ruta: str) -> None: # Inicializa un enemigo con nombre, vida y posición inicial
        self.nombre = nombre
        self.vida = vida
        self.posicion_actual = posicion
        self.inventario = inventario
        self.buff_activos = buffs
        self.ruta = ruta
        self.historial_acciones = Pila()
        self.habilidades = habilidades

    def mover(self, grafo) -> None: # Mueve al enemigo a un vértice adyacente
        # Movimiento aleatorio a un vértice adyacente
        if self.posicion_actual.aristas:
            nuevo_vertice = random.choice(self.posicion_actual.aristas)
            self.posicion_actual = nuevo_vertice
            self.registrar_accion(f"{self.nombre} se movió a {nuevo_vertice.valor}")

    def recibir_daño(self, cantidad: int) -> None: # Reduce la vida del enemigo al recibir daño
        self.vida -= cantidad
        self.registrar_accion(f"{self.nombre} recibió {cantidad} de daño. Vida restante: {self.vida}")

    def esta_vivo(self) -> bool: # Verifica si el enemigo sigue con vida
        return self.vida > 0

    def registrar_accion(self, descripcion: str) -> None: # Registra una acción en el historial del enemigo
        self.historial_acciones.apilar(descripcion)

    def aplicar_buff(self, buff: 'Buff') -> None: # Aplica un buff al enemigo y lo agrega a la cola de buffs activos
        self.buff_activos.encolar(buff)
        self.registrar_accion(f"{self.nombre} recibió el buff: {buff.nombre}")

    def usar_habilidad(self, jugador: 'Jugador') -> None: # Usa una habilidad del enemigo contra el jugador
        if not self.habilidades.esta_vacia():
            habilidad = self.habilidades.obtener(0)
            habilidad.ejecutar(self, jugador)

    @abstractmethod
    def comportamiento(self, jugador: 'Jugador', grafo: 'Grafo') -> None:
        """Define el comportamiento del enemigo frente al jugador"""
        pass

