import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False

clock=pygame.time.Clock()
x=200
y=150
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()
    if y>300:
        y=250
    if y<0:
        y=50
    if x>400:
        x=350
    if x<0:
        x=50
    if pressed[pygame.K_UP]: y -= 20 
    elif pressed[pygame.K_DOWN]: y += 20
    elif pressed[pygame.K_LEFT]: x -= 20
    elif pressed[pygame.K_RIGHT]: x += 20
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x,y), 25, width=0) 
    pygame.display.flip()
    clock.tick(20)