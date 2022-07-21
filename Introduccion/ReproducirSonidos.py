'''
Created on 6 may. 2020

@author: RSSpe
'''
import sys
import pygame

pygame.init()

width = 400
height = 500

#Dimensiones de la ventana
surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Reproducir sonidos")

pygame.mixer.music.load("C:/Users/RSSpe/Music/Motel - Dime Ven (Official Music Video).mp3")
pygame.mixer.music.set_volume(1.0)# -> Float 0.0 - 1.0
pygame.mixer.music.play()#pygame.mixer.music.play(cantidad de veces a repetirse, tiempo en que inicie), si queremos que se repite infinidad de veces colocamos -1
#pygame.mixer.music.pause() Pausar
#pygame.mixer.music.review() Reiniciar
#pygame.mixer.music.detener() Detener
#pygame.mixer.music.fadeout(cantidad de milisengundos que tomara detenerse) Se detendra poco a poco hasta quedar en silencio
pygame.mixer.music.fadeout(10000)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    surface.fill((0, 0, 255))

    pygame.display.update()  
