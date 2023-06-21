import pygame
from configuracion import *
import re
import base_datos
import pygame.mixer
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

pygame.init()
pygame.mixer.init()

ventana = pygame.display.set_mode((800, 600))

input_box = pygame.Rect(ANCHO // 2 - 100, ALTO // 2, 200, 30)
fuente = pygame.font.SysFont("JetBrains Mono", 16)
fuente2 = pygame.font.SysFont("XD", 30)

sonido_seleccionar = pygame.mixer.Sound("sonidos/Sonido_seleccionar.wav")
sonido_seleccionar.set_volume(0.1)

sonido_escribir = pygame.mixer.Sound("sonidos/Sonido_escribir.wav")
sonido_escribir.set_volume(0.1)

sonido_borrar = pygame.mixer.Sound("sonidos/Sonido_borrar.wav")
sonido_borrar.set_volume(0.1)

def validar_nombre(str)->str:
    expresion = r'^[a-zA-Z]{1,16}$'
    if re.match(expresion, str):
        return True
    else:
        return False

def mostrar_pantalla_final():
    nombre = ''

    pantalla_final = True

    while pantalla_final:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pantalla_final = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sonido_seleccionar.play()
                    messagebox.showinfo("Nombre", "El nombre ingresado contiene caracteres no válidos")
                    if validar_nombre(nombre):
                        pantalla_final = False
                        base_datos.crear_base_de_datos(nombre.capitalize())
                        nombre = ''
                        return "inicio"
                elif event.key == pygame.K_BACKSPACE:
                    sonido_borrar.play()
                    nombre = nombre[:-1]
                elif event.unicode:
                    sonido_escribir.play()
                    nombre += event.unicode

        ventana.fill(NEGRO)

        pygame.draw.rect(ventana, ROJO, input_box, 2)

        txt_surface = fuente.render(nombre, True, (255, 255, 255))
        ventana.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        juego_terminado_nombreo = fuente2.render("JUEGO TERMINADO", True, BLANCO)
        ventana.blit(juego_terminado_nombreo, (ANCHO // 2 - 135, ALTO // 2 - 160))

        ingresar_nombre_nombreo = fuente.render("Ingresa tu nombre", True, BLANCO)
        ventana.blit(ingresar_nombre_nombreo, (ANCHO // 2 - 85, ALTO // 2 - 40))

        presionar_tecla_nombreo = fuente.render("Presiona ENTER para continuar", True, BLANCO)
        ventana.blit(presionar_tecla_nombreo, (ANCHO // 2 - 145, ALTO // 2 + 100))

        pygame.display.flip()