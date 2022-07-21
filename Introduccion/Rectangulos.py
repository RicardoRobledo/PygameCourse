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
pygame.display.set_caption("Rectangulos")

#Color
my_color = (0, 0, 255)

#Clase Rect(x, y, width, height)
rect = pygame.Rect(100, 150, 120, 60)

#Colocando rectangulo en el centro: "rectangulo".center = (width//2 , height//2)
rect.center = (width//2 , height//2)

#Atributos de la clase rect
print(rect.x)
print(rect.y)

#Rectangulos con tuplas
rect2 = (100, 100, 80, 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    surface.fill(my_color)
    
    #Dibujando rectangulo pygame.draw.rect(superficie, color, rectangulo)
    pygame.draw.rect(surface, (255, 0, 0), rect)
    pygame.draw.rect(surface, (0, 255, 0), rect2)

    pygame.display.update()  