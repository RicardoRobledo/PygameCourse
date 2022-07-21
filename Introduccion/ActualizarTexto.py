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

pygame.display.set_caption("Actualizar texto")

font = pygame.font.Font('freesansbold.ttf', 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    surface.fill((255, 255, 255))
    
    seconds = pygame.time.get_ticks() // 1000
    text = font.render(str(seconds), True, (0, 0, 255))
    rect = text.get_rect()
    rect.center = (width//2, height//2)
    
    surface.blit(text, rect)
    
    pygame.display.update()  