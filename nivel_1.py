import pygame
import sys
from configuracion import *
from jugador import Jugador
from pelota import Pelota
from patron import Patron, patrones
from puntuacion import Puntuacion
from vidas import Vidas
import pygame.mixer 

pygame.init()
pygame.mixer.init()

ventana = pygame.display.set_mode((ANCHO, ALTO))

fondo1 = pygame.image.load("imagenes/bg1.png").convert()

fuente = pygame.font.SysFont('JetBrains Mono', 16)

clock = pygame.time.Clock()

jugador = Jugador()
pelota = Pelota()
sprites = pygame.sprite.Group()
sprites.add(jugador, pelota)

sonido_perder_vida = pygame.mixer.Sound("sonidos/Sonido_perder_vida.wav")
sonido_perder_vida.set_volume(0.1)

sonido_pasar_nivel = pygame.mixer.Sound("sonidos/Sonido_pasar_de_nivel.wav") 
sonido_pasar_nivel.set_volume(0.1)

def jugar_nivel_1():
    patron1 = Patron(sprites, patrones[0])

    game_over = False
    nivel_1 = True

    while nivel_1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            jugador.mover("izquierda")
        elif keys[pygame.K_d]:
            jugador.mover("derecha")

        ventana.blit(fondo1, (0, 0))


        # SE ESTABLECEN LOS LÍMITES Y LAS COLISIONES

        pelota.determinar_limites()
        jugador.determinar_limites()

        sprites.update()

        pelota.detectar_colisiones(jugador)
        patron1.detectar_colisiones(pelota)


        # MANEJO DE VIDAS

        if pelota.supera_alto():
            Vidas.restar_vida()
            sonido_perder_vida.play()
            pygame.time.delay(2500)
            if Vidas.vidas <= 0:
                game_over = True
                Patron.reiniciar_nivel(patron1)
            jugador.reiniciar_posicion()
            pelota.reiniciar_posicion()

        if game_over:
            return "game over"
        else:
            sprites.draw(ventana)
            vidas_texto = fuente.render('VIDAS: {0}'.format(Vidas.vidas), True, ROSA)
            ventana.blit(vidas_texto, (16, 0))
            puntaje_texto = fuente.render('PUNTUACION: {0}'.format(Puntuacion.puntuacion), True, ROSA)
            ventana.blit(puntaje_texto, (200, 0))

        if len(sprites) == 2:
            sonido_pasar_nivel.play()
            pygame.time.delay(1000)
            nivel_1 = False

        clock.tick(60)
        
        pygame.display.flip()