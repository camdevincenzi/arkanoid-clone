import pygame
import sys
import sqlite3
from configuracion import *
import pantalla_inicio

def mostrar_ranking():

    with sqlite3.connect("db_ranking.db") as conexion:

        cursor = conexion.execute('SELECT nombre, puntaje FROM puntajes ORDER BY puntaje DESC')
        resultados = cursor.fetchall()

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    fuente = pygame.font.SysFont("JetBrains Mono", 18)
    fuente2 = pygame.font.SysFont('XD', 36)

    puntajes_titulo = fuente2.render("TOP 10 PUNTAJES", True, NARANJA)
    ventana.blit(puntajes_titulo, (ANCHO // 2 - 160, ALTO // 2 - 250))

    columna_nombre = fuente.render('NOMBRE', True, ROSA)
    columna_puntos = fuente.render('PUNTOS', True, ROSA)
    ventana.blit(columna_nombre, (ANCHO // 2 - 135, 140))
    ventana.blit(columna_puntos, (ANCHO // 2 + 70, 140))

    y = -120
    for nombre, puntaje in resultados:
        nombre_texto = fuente.render(nombre, True, BLANCO)
        puntaje_texto = fuente.render(str(puntaje), True, BLANCO)
        ventana.blit(nombre_texto, (ANCHO // 2 - 135, ALTO // 2 + y))
        ventana.blit(puntaje_texto, (ANCHO // 2 + 70, ALTO // 2 + y))
        y += 30

    pantalla_ranking = True

    while pantalla_ranking:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pantalla_ranking = False
                    pantalla_inicio.mostrar_pantalla_inicio()
        
        pygame.display.flip()