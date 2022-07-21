'''
Created on 6 may. 2020

@author: RSSpe
'''
import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Reproducir sonidos")

imagen = pygame.image.load("C:/Users/RSSpe/Documents/Eclipse/Python/PygameProfesional(CodigoFacilito)/Introduccion/Imagenes/P1_Caminando.png")
rect = imagen.get_rect()
rect.center = (width//2, height//2)

#Este rectangulo tendra las mismas dimensiones que el primer rectangulo
#pygame.SRCALPHA indica que trabajaremos con transparencia
surface2 = pygame.Surface( (rect.width, rect.height), pygame.SRCALPHA)

#"nombre de la superficie".fill( (Rojo, Verde, Azul, transparencia) )
surface2.fill( (0, 0, 0, 50) )

#Obtener rectangulo 
rect2 = surface2.get_rect()

#Situamos rectangulo
rect2.center = rect.center

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    surface.fill((255, 255, 255))
    surface.blit(imagen, rect)
    surface.blit(surface2, rect2)
    pygame.display.update()  
    
    
    
    
    