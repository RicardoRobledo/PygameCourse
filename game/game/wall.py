'''
Created on 6 may. 2020

@author: RSSpe
'''
import pygame
from game.config import *

class Wall(pygame.sprite.Sprite):
    
    def __init__(self, left, bottom):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = self.image = pygame.image.load("C:/Users/RSSpe/Documents/Eclipse/Python/PygameProfesional(CodigoFacilito)/game/game/sources/sprites/bloque.png")
        
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
        
        self.vel_x = SPEED
        
        self.rect_top = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, 1)
        
        
    def update(self):
        self.rect.left -= self.vel_x
        
        self.rect_top.x = self.rect.x
        
        
    def stop(self):
        self.vel_x = 0
        
        
        
        
        
        
        
        
        
        
        
        
        