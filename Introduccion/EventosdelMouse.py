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

pygame.display.set_caption("Eventos del mouse")

font = pygame.font.Font('freesansbold.ttf', 48)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print("Boton presionado: ", event)
            
            print("Coordenadas: ",event.pos)
            
            if event.button == 1:
                print("Click izquierda")
                
            if event.button == 2:
                print("Click centro")
                
            if event.button == 3:
                print("Click derecha")
                
            if event.button == 4:
                print("Scroll hacia arriba")
                
            if event.button == 5:
                print("Scroll hacia abajoa")
            
        if event.type == pygame.MOUSEBUTTONUP:
            #print("Boton liberado")
            pass
                
    surface.fill((0,0,255))
    
    pygame.display.update() 