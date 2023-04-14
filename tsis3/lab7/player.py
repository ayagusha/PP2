import pygame
from pygame import mixer
import random
import os

pygame.init()
mixer.init()
screen = pygame.display.set_mode((600,600))
done = True
i=0
songs=['music/congr.mp3', 'music/grenade.mp3', 'music/tears.mp3', 'music/wil.mp3']

pygame.mixer.music.load(songs[i])
pygame.mixer.music.play()
        #songs=songs[i+1:]+[songs[i]]
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
              
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]: pygame.mixer.music.pause() 
    elif pressed[pygame.K_RETURN]: pygame.mixer.music.unpause()
    elif pressed[pygame.K_d]: 
        pygame.mixer.music.stop()
        """
        i=i+1
        if i>=len(songs):
            i=0
        """
        i=(i+1)%len(songs)
        pygame.mixer.music.load(songs[i])
        pygame.mixer.music.play() 
    elif pressed[pygame.K_a]: 
        pygame.mixer.music.stop()
        if i-1<0:
            i=len(songs)-1
        else:
            i=i-1
        pygame.mixer.music.load(songs[i])
        pygame.mixer.music.play() 

    screen.fill((255, 255, 255))
    screen.blit(pygame.image.load('images/mus.jpg'), (100, 80))
    pygame.display.flip()