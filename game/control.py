from game.mapa import Mapa
from game.jugador import Jugador
from game.variacionesEnemigos import Esqueleto, Bruja, Golem
from game.objetos.variacionesHabilidad import AtaqueBasico, Congelacion
from game.objetos.variacionesBuff import BuffFuerza, BuffRegeneracion
from estructuras.lista import Lista
from estructuras.cola import Cola

class ControladorJuego:
    def __init__(self)-> None:  # Constructor del controlador del juego
        self.mapa = Mapa()
        self.jugador = Jugador("Heroe")
        self.enemigos = Lista()

        # Construir mapa
    def inicializar_juego(self):
        self.mapa.agregar_ubicacion("Entrada")
        self.mapa.agregar_ubicacion("Bosque")
        self.mapa.agregar_ubicacion("Mazmorra")
        self.mapa.agregar_ubicacion("Castillo")

        self.mapa.conectar_ubicaciones("Entrada", "Bosque")
        self.mapa.conectar_ubicaciones("Bosque", "Mazmorra")
        self.mapa.conectar_ubicaciones("Mazmorra", "Castillo")

        self.mapa.establecer_ubicacion_inicial("Entrada")
        self.jugador.posicion_actual = self.mapa.obtener_ubicacion_actual()

        # Inicializar enemigos
        self.enemigos.agregar(Esqueleto("Esqueleto", 50, self.mapa.grafo.vertices["Bosque"], self.jugador.inventario, Lista(), Cola()))
        self.enemigos.agregar(Bruja("Bruja", 30, self.mapa.grafo.vertices["Mazmorra"], self.jugador.inventario, Lista(), Cola()))
        self.enemigos.agregar(Golem("Golem", 80, self.mapa.grafo.vertices["Castillo"], self.jugador.inventario, Lista(), Cola()))


    def mostrar_estado_enemigos(self):
        for enemigo in self.enemigos:
            print(f"{enemigo.nombre} está en {enemigo.posicion_actual.valor} con {enemigo.vida} de vida.")

    def mover_jugador(self, destino: str):
        if self.mapa.mover_a(destino):
            self.jugador.mover_a(self.mapa.obtener_ubicacion_actual())
            print(f"Te has movido a {destino}")
        else:
            print(f"No puedes ir a {destino} desde tu ubicación actual.")

    def obtener_enemigos_en_ubicacion_actual(self):
        ubicacion_actual = self.mapa.obtener_ubicacion_actual()
        return [e for e in self.enemigos if e.posicion_actual == ubicacion_actual]

    def mostrar_estado(self):
        print(f"Estás en: {self.jugador.posicion_actual.valor}")
        print(f"Adyacentes: {self.mapa.obtener_adyacentes(self.jugador.posicion_actual.valor)}")
        enemigos = self.obtener_enemigos_en_ubicacion_actual()
        if enemigos:
            print("Enemigos aquí:")
            for enemigo in enemigos:
                print(f" - {enemigo.nombre} (HP: {enemigo.salud})")
        else:
            print("No hay enemigos en esta ubicación.")

