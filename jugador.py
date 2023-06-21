import pygame
from configuracion import *

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = ANCHO // 2
        self.y = ALTO - 50
        self.velocidad = 10
        self.image = pygame.image.load('imagenes/paddle.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.direccion = 0

    def determinar_limites(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > ANCHO - 104:
            self.rect.x = ANCHO - 104

    def mover(self, direccion):
        if direccion == "izquierda":
            self.rect.x -= self.velocidad
            self.direccion = -1
        elif direccion == "derecha":
            self.rect.x += self.velocidad
            self.direccion = 1
        
    def reiniciar_posicion(self):
        self.x = ANCHO // 2
        self.y = ALTO - 50
        self.velocidad = 15
        self.rect.center = (self.x, self.y)