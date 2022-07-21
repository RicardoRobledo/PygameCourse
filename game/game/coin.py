'''
Created on 6 may. 2020

@author: RSSpe
'''
import pygame
from game.config import *

class Coin(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = self.image = pygame.image.load("C:/Users/RSSpe/Documents/Eclipse/Python/PygameProfesional(CodigoFacilito)/game/game/sources/sprites/coin.png")
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
        self.velocidad_x = SPEED
        
    def update(self):
        self.rect.left -= self.velocidad_x
        
    def stop(self):
        self.vel_x = 0
        
        
        
        
        