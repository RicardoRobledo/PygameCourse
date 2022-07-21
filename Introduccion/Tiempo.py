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

pygame.display.set_caption("Tiempo")

font = pygame.font.Font('freesansbold.ttf', 48)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    time = pygame.time.get_ticks() // 1000 #Milisegundos y diviendo entre 1000 obtendremos segundos
    print(time)
    
    surface.fill((255, 255, 255))
    pygame.display.update()  