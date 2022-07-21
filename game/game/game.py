'''
Created on 6 may. 2020

@author: RSSpe
'''
import os#Para ruta absoluta de archivos
import pygame
import sys
import random
from .config import *
from .platform import Platform
from .player import *
from .wall import *
from .coin import Coin

class Game:
    def __init__(self):
        pygame.init()
        
        self.surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption(TITLE)
        
        self.running = True
        
        self.clock = pygame.time.Clock()
        
        #Obtener direccion absoluta
        self.dir = os.path.dirname(__file__)
        self.dir_sounds = os.path.join(self.dir, 'source/sounds')
        self.dir_image = os.path.join(self.dir, 'source/sprites')
        
        self.background = pygame.image.load("C:/Users/RSSpe/Documents/Eclipse/Python/PygameProfesional(CodigoFacilito)/game/game/sources/sprites/fondo.jpg")
        
        #Obtener fuente del sistema
        self.font = pygame.font.match_font(FONT)
        
    
    def start(self):#Comenzar el juego
        #Este es un menu: self.menu()
        self.new()

    
    def new(self):#Generar nuevo juego
        self.playing = True
        self.score = 0
        self.level = 0
        #pygame.mixer.music.load("C:/Users/RSSpe/Documents/Eclipse/Python/PygameProfesional(CodigoFacilito)/game/game\/sources/sounds/cancion.mp3")
        #pygame.mixer.music.play()
        self.generate_elements()
        self.run()
    
    
    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top-200)
        self.wall = Wall(500, self.platform.rect.top)
        
        #Esto permitira agrupar sprites
        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        
        self.sprites.add(self.platform)
        self.sprites.add(self.player)
        
        self.generate_walls()


    def generate_walls(self):
        
        last_position = WIDTH + 100
        
        if not len(self.sprites)>0:
            for w in range(0, MAX_WALLS):
                
                left = random.randrange(last_position + 200, last_position + 400)
                wall = Wall(left, self.platform.rect.top)
                
                last_position = wall.rect.right
                
                self.sprites.add(wall)
                self.walls.add(wall)
            
            self.level += 1
            self.generate_coins()
                
                
    def generate_coins(self):
        last_position = WIDTH + 100

        for c in range(0, MAX_COINS):
            pos_x = random.randrange(last_position + 180, last_position+300)
            
            coin = Coin(pos_x, 100)
            
            last_position = coin.rect.right
            
            self.sprites.add(coin)
            self.coins.add(coin)
    
    
    def run(self):#Ejecutar el juego
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
    
    def events(self):#Estara a la escucha de eventos en el juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
                
        key = pygame.key.get_pressed()
        
        if key[pygame.K_UP]:
            self.player.jump()
            
        if key[pygame.K_r] and not self.playing:
            self.new()
    
    
    def draw(self):#Pintar los elementos en el juego
        self.surface.blit(self.background, (0, 0))
        
        self.draw_text()
        
        #Con self.sprites.draw(superficie) podremos pintar sprites y recibe de parametro en donde queremos pintarlo
        self.sprites.draw(self.surface)
        
        pygame.display.flip()#Con flip tambie actualizamos la pantalla solo que se realizara sobre toda la superficie
    
    
    def update(self):#Actualizara la pantalla
        if self.playing:
        
            wall = self.player.collide_with(self.walls)
        
            if wall:
                if self.player.collide_bottom(wall):
                    self.player.skid(wall)
                else:
                    self.stop()
                    
            coin = self.player.collide_with(self.coins)
            
            if coin:
                self.score += 1
                coin.kill()
                
                #sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, "cancion.wav"))
                #sound.play()
            
            self.sprites.update()
            self.player.validate_platform(self.platform)
            self.update_elements(self.walls)
            self.update_elements(self.coins)
            self.generate_walls()
            
            
    def update_elements(self, elements):#Para liberar memoria ram
        for element in elements:
            if not element.rect.right>0:
                element.kill()#Eliminar objeto
                
    
    def stop(self):#Detendra el juego
        #sound = pygame.mixer.Sound(os.path.join(self.dir_sounds, "perdiste.wav"))
        #sound.play()
        
        pygame.mixer.stop()
        
        self.player.stop()
        self.stop_elements(self.walls)
        
        self.playing = False;
    
    
    def stop_elements(self, elements):
        for element in elements:
            element.stop()
            
    
    def level_format(self):
        return f"Level: {self.level}"
    
            
    def draw_text(self):
        self.display_text(self.score_format(), 36, WIDTH//2, 30)
        self.display_text(self.level_format(), 36, 60, 30)
        
        if not self.playing:
            self.display_text("Perdiste", 60, WIDTH//2, HEIGHT//2)
            self.display_text("Presiona r para comenzar de nuevo", 60, WIDTH//2, 100)
        
        
    def score_format(self):
        return f"Score: {self.score}"
            
            
    def display_text(self, text, size, pos_x, pos_y):
        font = pygame.font.Font(self.font, size)
        
        text = font.render(text, True, (255, 255, 255))
        rect = text.get_rect()
        rect.midtop = (pos_x, pos_y)
        
        #print(FPS)
        self.surface.blit(text, rect)    
        
    
    def menu(self):
        self.surface.fill(GREEN_LIGHT)
        self.display_text('Presiona una tecla para comezar', 36, BLACK, WIDTH//2, 10)
        
        pygame.display.flip()
        
        self.wait()
    
    
    def wait(self):
        wait = True
        
        while wait:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYUP:
                    wait = False
    