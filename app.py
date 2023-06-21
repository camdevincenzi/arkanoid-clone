import pygame
from configuracion import *
import pantalla_inicio
import pantalla_final
import nivel_1
import nivel_2
import nivel_3

pygame.init()

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("ARKANOID")
fuente = pygame.font.SysFont('JetBrains Mono', 16)

logo = pygame.image.load("imagenes/logo.png")
pygame.display.set_icon(logo)

en_ejecucion = True

estado = "inicio"

while en_ejecucion:
    
    if estado == "inicio":
        resultado = pantalla_inicio.mostrar_pantalla_inicio()
        if resultado == "nivel_1":
            estado = "nivel_1"

    elif estado == "nivel_1":
        resultado = nivel_1.jugar_nivel_1()
        if resultado == "game over":
            estado = "pantalla final"
        else:
            estado = "nivel_2"

    elif estado == "nivel_2":
        resultado = nivel_2.jugar_nivel_2()
        if resultado == "game over":
            estado = "pantalla final"
        else:
            estado = "nivel_3"

    elif estado == "nivel_3":
        resultado = nivel_3.jugar_nivel_3()
        if resultado == "game over":
            estado = "pantalla final"
    
    elif estado == "pantalla final":
        resultado = pantalla_final.mostrar_pantalla_final()
        if resultado == "inicio":
            estado = "inicio"

    pygame.display.flip()
pygame.quit()