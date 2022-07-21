'''
Created on 5 may. 2020

@author: RSSpe
'''
import sys
import pygame

pygame.init()

width = 400
height = 500

#Dimensiones de la ventana
surface = pygame.display.set_mode((width, height))

#Titulo
pygame.display.set_caption("Colores")

#RGB
Red = 255
Green = 0
Blue = 0
newColorRed = pygame.Color(Red, Green, Blue) #0-255
Red = 0
Green = 255
Blue = 0
newColorGreen = pygame.Color(Red, Green, Blue)
Red = 0
Green = 0
Blue = 255
newColorBlue = pygame.Color(Red, Green, Blue)

my_color = (Red, Green, Blue)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Pintar pantalla
    surface.fill(my_color)
    
    #Actualizar pantalla
    pygame.display.update()  
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            