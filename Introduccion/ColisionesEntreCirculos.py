'''
Created on 6 may. 2020

@author: RSSpe
'''
import pygame
import sys
import math

pygame.init()

#Suponiendo que las 2 figuras son circulos, en este caso no es asi por experimentacion

width = 600
height = 400

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Colisiones entre circulos")

imagen = pygame.image.load("C:/Users/RSSpe/Documents/Eclipse/Python/PygameProfesional(CodigoFacilito)/Introduccion/Imagenes/P1_Caminando.png")
rect = imagen.get_rect()
rect.center = (width//2, height//2)

surface2 = pygame.Surface( (rect.width, rect.height), pygame.SRCALPHA)
surface2.fill( (0, 0, 0, 50) )

rect2 = surface2.get_rect()
rect2.center = rect.center

font = pygame.font.Font("freesansbold.ttf", 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    surface.fill((0, 0, 255))
    
    surface.blit(imagen, rect)
    surface.blit(surface2, rect2)
    
    circle_pos = pygame.mouse.get_pos()
    
    circle = pygame.draw.circle(surface, (0, 255, 0), circle_pos, 50)
    
    message=""
    
    pygame.draw.line(surface, (0, 0, 0), rect2.center, circle.center, 4)
    
    #Calcular distancia
    dist = math.hypot(rect.x-circle.x, rect.y-circle.y)
    
    #Detectar colision
    #distancia < (suma de radios de los circulos)
    if dist < (50 + 50):
        message = "Existe una colision"
            
    text = font.render(message, True, (255, 0, 0))
    rect3 = text.get_rect()
    rect3.midtop = (width//2, 50)
    surface.blit(text, rect3)
            
    pygame.display.update()