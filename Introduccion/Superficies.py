'''
Created on 5 may. 2020

@author: RSSpe
'''
import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height)) #surface

pygame.display.set_caption("Superficies")

surface2 = pygame.Surface((200, 200))
surface2.fill((0, 250, 0))

rect = surface2.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    surface.fill((0, 0, 250))
    
    #Pintando superficie sobre otra: "Primera superficie".blit(superficie a pintar, posicion en coordenadas
    surface.blit(surface2, rect)
    
    pygame.draw.rect(surface2, (250, 0, 0), (100, 50, 30, 50))

    pygame.display.update()  