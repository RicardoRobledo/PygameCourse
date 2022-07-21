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

pygame.display.set_caption("Mover imagen por mouse")

image = pygame.image.load("C:/Users/RSSpe/Documents/Eclipse/Python/PygameProfesional(CodigoFacilito)/Introduccion/Imagenes/P1_Caminando.png")
rect = image.get_rect()
rect.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    rect.center = pygame.mouse.get_pos()# Tupla -> (x, y)
    
    surface.fill((255, 255, 255))
    surface.blit(image,rect)
    pygame.display.update()  