'''
Created on 6 may. 2020

@author: RSSpe
'''
import pygame
import sys

pygame.init()

#Vamos a hacer colisiones perfectas usando mascaras, un ejemplo de uso es cuando vamo a colisionar un cuadrado con un circulo, pero se aplicara donde haya transparencia

width = 600
height = 400

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Colisiones entre circulos")

imagen2 = pygame.image.load("C:/Users/RSSpe/Documents/Eclipse/Python/PygameProfesional(CodigoFacilito)/Introduccion/Imagenes/P1_Quieto.png")
rect2 = imagen2.get_rect()
rect2.center = (width//2, height//2)
mask_circle = pygame.mask.from_surface(imagen2)#Mascara

imagen = pygame.image.load("C:/Users/RSSpe/Documents/Eclipse/Python/PygameProfesional(CodigoFacilito)/Introduccion/Imagenes/P1_Caminando.png")
rect = imagen.get_rect()
rect.center = (width//2, height//2)
mask_rect = pygame.mask.from_surface(imagen)#Mascara

font = pygame.font.Font("freesansbold.ttf", 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    surface.fill((0, 0, 255))
    
    rect2.center = pygame.mouse.get_pos()
    
    surface.blit(imagen2, rect)
    surface.blit(imagen, rect2)
    
    message = ""
    
    offset = (rect2.x - rect.x, rect2.y - rect.y) #Es una tupla: offset(x, y)
    #OJO: El orden si importa con respecto a que mascara pusimos en el if y como los colocamos en offset()
    
    #mask_circle.overlap(mascara a validar colision, offset)
    if mask_circle.overlap(mask_rect, offset):
        message = "Existe una colision"
        
    text = font.render(message, True, (0, 255, 0))
    rect3 = text.get_rect()
    rect3.midtop = (width//2, 50)
    
    surface.blit(text, rect3)
        
    pygame.display.update()
    
    
    
    
    
    
    
    
    
    
    
    
    