import pygame
from random import randint
from configuracion import *
import pygame.mixer 


pygame.mixer.init()

sonido_colision_jugador = pygame.mixer.Sound("sonidos/Sonido_colision_jugador.wav") 
sonido_colision_jugador.set_volume(0.1)

sonido_colision_paredes = pygame.mixer.Sound("sonidos/Sonido_colision_paredes.wav") 
sonido_colision_paredes.set_volume(0.1)

class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = ANCHO // 2
        self.y = ALTO // 2
        self.image = pygame.image.load('imagenes/pelota.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.velocidad_x = randint(2, 5)
        self.velocidad_y = randint(1, 3)
        self.velocidad_maxima = 4
        self.rect.center = (self.x, self.y)


    # CONTROLA QUE NO PASE LOS LÍMITES DE LA PANTALLA

    def determinar_limites(self):
        if self.x <= 11 or self.x > ANCHO - 11:
            sonido_colision_paredes.play()
            self.velocidad_x = -self.velocidad_x
        if self.y < 11:
            sonido_colision_paredes.play()
            self.velocidad_y = -self.velocidad_y
        if self.velocidad_x == 0:
            sonido_colision_paredes.play()
            self.velocidad_x += 1
        if self.velocidad_y == 0:
            self.velocidad_y += 1
        self.x += self.velocidad_x
        self.y += self.velocidad_y
        self.rect.center = (self.x, self.y)


    # CONTROLA LA COLISIÓN CON EL PADDLE (JUGADOR)

    def detectar_colisiones(self, jugador):
        if self.rect.colliderect(jugador.rect):
            if abs(self.rect.bottom - jugador.rect.top) < 10 and self.velocidad_y > 0:
                sonido_colision_jugador.play()
                self.velocidad_y = -self.velocidad_y
                self.velocidad_x += jugador.direccion
                if self.velocidad_x > self.velocidad_maxima:
                    self.velocidad_x = self.velocidad_maxima
                if self.velocidad_x < -self.velocidad_maxima:
                    self.velocidad_x = -self.velocidad_maxima
            else:
                self.velocidad_x *= -1
        self.x += self.velocidad_x
        self.y += self.velocidad_y

    def supera_alto(self):
        return self.y > ALTO
    
    
    # REINICIA LA POSICIÓN EN CASO DE QUE LA PELOTA CAIGA

    def reiniciar_posicion(self):
        self.x = ANCHO // 2
        self.y = ALTO // 2
        self.velocidad_x = randint(2, 5)
        self.velocidad_y = randint(1, 3)
        self.rect.center = (self.x, self.y)

    def rebotar(self):
        self.velocidad_x = -self.velocidad_x
        self.velocidad_y = randint(1, 3)