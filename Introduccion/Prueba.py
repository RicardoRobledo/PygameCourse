'''
Created on 6 may. 2020

@author: RSSpe
'''
import pygame
import sys

pygame.init()

surface = pygame.display.set_mode((800,400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP]:
        print("Arriba")
        
    if pressed[pygame.K_DOWN]:
        print("Abajo")
        
    if pressed[pygame.K_LEFT]:
        print("Izquierda")
        
    if pressed[pygame.K_RIGHT]:
        print("Derecha")
    
    surface.fill((30,50,150))
    pygame.display.update()