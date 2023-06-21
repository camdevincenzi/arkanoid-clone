import pygame
from configuracion import *
from puntuacion import Puntuacion
import pygame.mixer

pygame.mixer.init()

bloques = [
    'imagenes/bloque_violeta.png',
    'imagenes/bloque_gris.png',
    'imagenes/bloque_azul.png',
    'imagenes/bloque_verde.png',
    'imagenes/bloque_amarillo.png',
    'imagenes/bloque_rojo.png'
]

patrones = [
    [2, 2, 1, 1, 0, 0],
    [5, 4, 3, 2, 1, 0],
    [5, 5, 4, 4, 3, 3]
]

sonido_colision = pygame.mixer.Sound("sonidos/Sonido_colision.wav")
sonido_colision.set_volume(0.1)

class Patron:
    def __init__(self, sprites, patron):
        self.sprites = sprites
        self.bloques = pygame.sprite.Group()

        for fila in range(FILAS):
            for columna in range(COLUMNAS):
                bloque = Bloque(fila, columna, patron[fila])
                self.bloques.add(bloque)
                self.sprites.add(bloque)


    # CONTROLA LAS COLISIONES ENTRE LA PELOTA Y LOS BLOQUES

    def detectar_colisiones(self, pelota):
        colisiones = pygame.sprite.spritecollide(pelota, self.bloques, False)

        for bloque in colisiones:
            bloque.kill()
            sonido_colision.play()
            pelota.rebotar()
        
            # SE DEFINEN LOS PUNTOS DE CADA BLOQUE SEGÚN SU COLOR
            puntos = 10 * (bloque.color + 1) * 10

            Puntuacion.actualizar_puntuacion(puntos)

    def reiniciar_nivel(patron):
        for bloque in patron.bloques:
            bloque.kill()

class Bloque(pygame.sprite.Sprite):
    def __init__(self, fila, columna, color):
        super().__init__()
        self.x = MARGEN + (columna * 64) + 32
        self.y = MARGEN + 16 + (fila * 32) + 16
        self.image = pygame.image.load(bloques[color])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.color = color