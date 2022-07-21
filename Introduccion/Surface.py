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
pygame.display.set_caption("Curso de Pygame")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()