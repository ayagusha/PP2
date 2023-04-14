import pygame
import math
import datetime

pygame.init()
screen=pygame.display.set_mode((1400,1050))
screen.blit(pygame.image.load('images/bg.png'),(0,0))
clock=pygame.time.Clock()
done=True

minutes=pygame.image.load('images/min.png')
minutes_copy=minutes
minutes_rect=minutes.get_rect()

seconds=pygame.image.load('images/sec.png')
seconds_copy=seconds
seconds_rect=seconds.get_rect()

def rotate(hand, rect, angle):
    newHand=pygame.transform.rotate(hand, angle)
    rect=newHand.get_rect(center=rect.center)
    return newHand, rect

while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done=False
    
    t=datetime.datetime.now()
    s=t.microsecond + t.second*(10**6)
    m=t.minute
    minutes, minutes_rect = rotate(minutes_copy, minutes_rect, -(m*6))
    seconds, seconds_rect = rotate(seconds_copy, seconds_rect, -(s*0.000006))
    
    screen.blit(pygame.image.load('images/bg.png'),(0,0))
    screen.blit(minutes, minutes_rect)
    screen.blit(seconds, seconds_rect)
    pygame.display.flip()
    clock.tick(60)