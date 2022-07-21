'''
Created on 6 may. 2020

@author: RSSpe
'''
import sys
import pygame

pygame.init()

width = 500
height = 600

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Obtener posicion del mouse")

font = pygame.font.Font('freesansbold.ttf', 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    pos_x, pos_y = pygame.mouse.get_pos()  #Tupla(x, y)
    message = f'pos x :{pos_x}, pos y: {pos_y}'
    
    text = font.render(message, True, (4,50,80))
    rect = text.get_rect()
    rect.center = (width//2, height//2)
      
    surface.fill((255, 255, 255))
    surface.blit(text, rect)
    pygame.display.update()
    
    
    
    
    
    
    
    