'''
Created on 6 may. 2020

@author: RSSpe
'''
import sys
import pygame

pygame.init()

width = 400
height = 500

pygame.display.set_caption("Colision entre rectangulos")

surface = pygame.display.set_mode((width, height))

rect1 = pygame.Rect(0, 0, 100, 80)
rect1.center = (width//2, height//2)

rect2 = pygame.Rect(0, 0, 100, 80)

font = pygame.font.Font("freesansbold.ttf", 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    surface.fill((0, 0, 255))
    
    rect2.center = pygame.mouse.get_pos()
    
    pygame.draw.rect(surface, (0, 255, 0), rect1)
    pygame.draw.rect(surface, (255, 0, 0), rect2)
    
    message=""
    
    #Detectar colision
    if rect1.colliderect(rect2):
        message = "Existe una colision"
    
    text = font.render(message, True, (200, 200, 100))
    rect3 = text.get_rect()
    rect3.midtop = (width//2, 50)
    surface.blit(text, rect3)
    
    pygame.display.update() 
    
    
    
    
    