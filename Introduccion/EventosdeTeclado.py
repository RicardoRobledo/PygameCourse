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

pygame.display.set_caption("Eventos del teclado")

font = pygame.font.Font('freesansbold.ttf', 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            print(event)
            print("Tecla presionada")
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("Izquierda")
                
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                print("Arriba")
                
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("Abajo")
                
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("Derecha")
            
            """if event.key == pygame.K_s:
                print("Tecla s presionada")"""
        
        if event.type == pygame.KEYUP:    
            #print("Tecla liberada")
            pass

                
    surface.fill((0,0,255))
    
    pygame.display.update()  
    
    
    
    
    
    
    
    
    
    
    