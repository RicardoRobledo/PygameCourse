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

pygame.display.set_caption("Pintar imagenes")

#Cargando imagen
imagen = pygame.image.load("C:/Users/RSSpe/Documents/Eclipse/Python/PygameProfesional(CodigoFacilito)/Introduccion/Imagenes/P1_Caminando.png")
rect = imagen.get_rect()
rect.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    surface.fill((255, 255, 255))
    
    #surface.blit(imagen, coordenadas)
    surface.blit(imagen, rect)
    
    pygame.display.update()  