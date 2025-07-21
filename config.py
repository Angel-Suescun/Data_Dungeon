import pygame

# Inicializar Pygame para poder usar fuentes
pygame.init()

# Tamaño de la ventana
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
TAMANIO_PANTALLA = (ANCHO_PANTALLA, ALTO_PANTALLA)

# Título de la ventana
TITULO_VENTANA = "Data Dungeon"

# Colores comunes (R, G, B)
COLOR_FONDO = (30, 30, 30)
COLOR_TEXTO = (255, 255, 255)
COLOR_BOTON = (70, 70, 70)
COLOR_BOTON_HOVER = (100, 100, 100)
COLOR_BORDES = (200, 200, 200)
COLOR_ALERTA = (255, 100, 100)

# Fuente
FUENTE_GENERAL = pygame.font.SysFont("consolas", 20)

# FPS
FPS = 60

# Rutas de imágenes (si usas imágenes)
RUTA_ICONO = "assets/images/icono.png"
RUTA_JUGADOR = "assets/images/jugador.png"

