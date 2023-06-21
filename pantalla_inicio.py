import pygame
import sys
from configuracion import *
from pygame.locals import *
from puntuacion import Puntuacion
from vidas import Vidas
import ranking
import pygame.mixer

pygame.init()
pygame.mixer.init()

ventana = pygame.display.set_mode((ANCHO, ALTO))

fuente = pygame.font.SysFont('JetBrains Mono', 16)
fuente2 = pygame.font.SysFont('XD', 40)

sonido_seleccionar = pygame.mixer.Sound("sonidos/Sonido_seleccionar.wav")
sonido_seleccionar.set_volume(0.1)

logo = pygame.image.load("imagenes/logo.png")

def mostrar_pantalla_inicio():

    Vidas.reiniciar_vidas()
    Puntuacion.reiniciar_puntuacion()

    pantalla_inicio = True

    while pantalla_inicio:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pantalla_inicio = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sonido_seleccionar.play()
                    pantalla_inicio = False
                    return "nivel_1"
                if event.key == pygame.K_r:
                    sonido_seleccionar.play()
                    pantalla_inicio = False
                    ranking.mostrar_ranking()

        ventana.fill(NEGRO)

        ventana.blit(logo, (ANCHO // 2 - 250, ALTO // 2 - 180))

        empezar_juego_texto = fuente.render("Presiona ENTER para comenzar a jugar", True, CELESTE)
        ventana.blit(empezar_juego_texto, (ANCHO // 2 - 175, ALTO // 2 + 100))

        ver_ranking_texto = fuente.render("Presiona R para ver el ranking de puntos", True, CELESTE)
        ventana.blit(ver_ranking_texto, (ANCHO // 2 - 200, ALTO // 2 + 130))

        pygame.display.flip()
    return "nivel_1"
