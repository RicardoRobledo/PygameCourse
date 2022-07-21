'''
Created on 5 may. 2020

@author: RSSpe
'''
import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Pintar texto")

#1.- Obtener una fuente: pygame.font.Font(nombre de la fuente, tamaño)
#Si queremos usar otra fuente que descargamos en lugar de 'freesansbold.ttf'
#escribimos la direccion del archivo
font = pygame.font.Font('freesansbold.ttf', 48)

#2.- Crear el texto: font.render(texto, antialias, color, )
text = font.render("Hola Cody", True, (100,30,255))# -> surface
rect = text.get_rect()
rect.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    surface.fill((255, 255, 255))
    surface.blit(text, rect)
    pygame.display.update()
