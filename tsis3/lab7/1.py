import pygame
import os


pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue=False

x = 30
y = 30


clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue

        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, color, (x,y), 25, width=0)
        pygame.display.flip()
        clock.tick(60)