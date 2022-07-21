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

pygame.display.set_caption("Tecla presionada")

font = pygame.font.Font('freesansbold.ttf', 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #get_pressed() retornara la tecla presionada
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        print("Arriba")
        
    if pressed[pygame.K_a]:
        print("Izquierda")
        
    if pressed[pygame.K_s]:
        print("Abajo")
        
    if pressed[pygame.K_d]:
        print("Derecha")
        
                
    surface.fill((0,0,255))
    
    pygame.display.update()  