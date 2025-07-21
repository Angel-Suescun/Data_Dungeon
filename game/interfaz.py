import pygame
from game.mapa import Mapa
from game.jugador import Jugador

class Interfaz:
    def __init__(self, pantalla: pygame.Surface, jugador: Jugador, mapa: Mapa) -> None: # Inicializa la interfaz del juego
        self.pantalla = pantalla
        self.jugador = jugador
        self.mapa = mapa
        self.fuente = pygame.font.SysFont("consolas", 20)

    def dibujar_texto(self, texto, x, y, color=(255, 255, 255)) -> None: # Dibuja texto en la pantalla
        superficie = self.fuente.render(texto, True, color)
        self.pantalla.blit(superficie, (x, y))

    def mostrar_estado(self) -> None: # Muestra el estado actual del jugador y el mapa
        self.pantalla.fill((0, 0, 0))
        self.dibujar_texto(f"Nombre: {self.jugador.nombre}", 20, 20)
        self.dibujar_texto(f"Vida: {self.jugador.vida}", 20, 50)
        self.dibujar_texto(f"Ubicacion: {self.jugador.posicion_actual.valor}", 20, 80)

        self.dibujar_texto("Inventario:", 20, 120)
        for i, objeto in enumerate(self.jugador.inventario):
            self.dibujar_texto(f"- {objeto.nombre}", 40, 150 + i * 25)

        self.dibujar_texto("Buffs:", 300, 120)
        for i, buff in enumerate(self.jugador.buffs):
            self.dibujar_texto(f"- {buff.nombre}", 320, 150 + i * 25)

        self.dibujar_texto("Habilidades:", 600, 120)
        for i, hab in enumerate(self.jugador.habilidades):
            self.dibujar_texto(f"- {hab.nombre}", 620, 150 + i * 25)

        pygame.display.flip()

    def manejar_eventos(self) -> bool: # Maneja los eventos del juego, como teclas presionadas
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    self.intentar_mover('arriba')
                elif evento.key == pygame.K_s:
                    self.intentar_mover('abajo')
                elif evento.key == pygame.K_a:
                    self.intentar_mover('izquierda')
                elif evento.key == pygame.K_d:
                    self.intentar_mover('derecha')
        return True

    def intentar_mover(self, direccion: str) -> None: # Intenta mover al jugador en una dirección específica
        actual = self.jugador.posicion_actual.valor
        vecinos = self.mapa.obtener_adyacentes(actual)

        # Aquí puedes implementar lógica específica para direcciones si tu grafo tiene etiquetas o nombres claros.
        if vecinos:
            nuevo = vecinos[0]  # Por ahora solo se mueve al primero
            if self.mapa.mover_a(nuevo):
                self.jugador.mover_a(self.mapa.grafo.vertices[nuevo])

    def bucle_principal(self) -> None: # Bucle principal del juego
        ejecutando = True
        while ejecutando:
            ejecutando = self.manejar_eventos()
            self.mostrar_estado()
            pygame.time.delay(100)
