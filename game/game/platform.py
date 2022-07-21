'''
Created on 6 may. 2020

@author: RSSpe
'''
import pygame

from .config import *

#En este caso la clase debe de heredar de pygame.sprite.Sprite y al hacerlo debemos de importar pygame
class Platform(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        #Generando superficie(plataforma) donde nos desplazaremos
        self.image = pygame.Surface( (WIDTH, 40) )
        self.image.fill(GREEN)
        
        #Esto es obligatorio al pintar elementos
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - 40
        