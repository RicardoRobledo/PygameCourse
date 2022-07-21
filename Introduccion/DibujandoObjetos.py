'''
Created on 5 may. 2020

@author: RSSpe
'''
import sys
import pygame

pygame.init()

width = 400
height = 500

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Dibujando objetos")

my_color = (0, 0, 255)

rect = pygame.Rect(0, 0, 120, 60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    surface.fill(my_color)
    
    #draw
    #1.- Donde se pintara la figura
    #2.- De que color sera la figura
    pygame.draw.rect(surface, (0, 255, 0), rect)
    
    #pygame.draw.circle(superficie, color, coordenadas del circulo, radio)
    pygame.draw.circle(surface, (0, 255, 0), (200, 300), 100)
    
    #pygame.draw.line(superficie, color,  punto a, punto b, grosor)
    pygame.draw.line(surface, (255, 0, 0), (100, 100), (200,300), 100)

    #Poligonos
    
    #Triangulo: pygame.draw.polygon(surface, (255, 0, 0), ((punto a),(punto b),(punto c)))
    pygame.draw.polygon(surface, (100, 100, 100), ((0,400),(100,300),(200,400)))
    
    #Pentagono: pygame.draw.polygon(surface, (255, 0, 0), ((punto a),(punto b),(punto c),(punto d),(punto e))
    pygame.draw.polygon(surface, (100, 100, 100), ((146,0),(291, 106),(236, 277),(56, 277),(0,106)))

    pygame.display.update()  