'''
Created on 6 may. 2020

@author: RSSpe
'''
import sys
import pygame

pygame.init()

width = 800
height = 600

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Mover imagen por teclado")

image = pygame.image.load("C:/Users/RSSpe/Documents/Eclipse/Python/PygameProfesional(CodigoFacilito)/Introduccion/Imagenes/P1_Caminando.png")
rect = image.get_rect()
rect.center = (width//2, height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        rect.y -= 5
        
    if pressed[pygame.K_a]:
        rect.x -= 5
        
    if pressed[pygame.K_s]:
        rect.y += 5
        
    if pressed[pygame.K_d]:
        rect.x += 5
    
    #Validaciones
    if rect.left<0:
        rect.left = 0
        
    if rect.right>width:
        rect.right = width
        
    if rect.top<0:
        rect.top = 0
        
    if rect.bottom>height:
        rect.bottom = height
    
    surface.fill((255, 255, 255))
    surface.blit(image,rect)
    pygame.display.update()  
    
    
    
    
    
    
    