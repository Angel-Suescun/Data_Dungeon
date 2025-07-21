import pygame
from estructuras.lista import Lista
from objetos.objeto import Objeto

class Renderer:
    def __init__(self) -> None:
        # cache para imágenes
        self.cache_imagenes = Lista()

    def cargar_imagen(self, path:str) -> pygame.Surface: # Carga una imagen desde el disco y la almacena en caché
        for imagen in self.cache_imagenes:
            if imagen.path == path:
                return imagen
        imagen = pygame.image.load(path)
        self.cache_imagenes.agregar(imagen)
        return imagen

    def dibujar_objeto(self, pantalla: 'pygame.surface' , objeto:'Objeto', x: int, y: int)-> None: # Dibuja un objeto en la pantalla
        imagen = self.cargar_imagen(objeto.path_imagen)
        pantalla.blit(imagen, (x, y))

