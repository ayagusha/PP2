import pygame 
from random import randint 
import time

pygame.init()
screen=pygame.display.set_mode((400, 600))
clock=pygame.time.Clock()
done=True

bg = pygame.image.load('image/bg.png') 
bg_y = 0  
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
cnt = 0 
black=(0,0,0)
speed=3
score=0
game_over = font.render("Game Over", True, black)

class Player(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = pygame.image.load('image/player.png') 
        self.rect = self.image.get_rect() 
        self.rect.x = 200 
        self.rect.y = 500 
     #a function that does not allow to go beyond the field boundary
    def update(self,x = 0): 
        if 0 >= self.rect.x: 
            x = 0 
            self.rect.x = 1 
        if self.rect.x > 351: 
            x = 0 
            self.rect.x = 350 
        self.rect.move_ip(x, 0) 
 
class Enemy(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = pygame.image.load('image/enemy.png') 
        self.rect = self.image.get_rect() 
        self.rect.x = randint(0,360) 
        self.rect.y = -100 
 #if the enemy goes over the border, he is respawned at the top in a random x value
    def update(self): 
        if self.rect.y > 700: 
            self.rect.y = -100 
            self.rect.x = randint(0,360) 
        self.rect.move_ip(0,speed) 
 
 
class Coin(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = pygame.image.load('image/coin.png') 
        self.image = pygame.transform.scale(self.image, (50,50)) 
        self.rect = self.image.get_rect() 
        self.rect.x = randint(0,360) 
        self.rect.y = -100 
        #if the coin goes over the border, he is respawned at the top in a random x value
    def update(self): 
        if self.rect.y > 700: 
            self.newcoordinates() 
        self.rect.move_ip(0, 10) 
 
 #function that gives us coordinates where coin will be created
    def newcoordinates(self): 
        self.rect.y = -100 
        self.rect.x = randint(0,360) 

 
P = Player() 
E = Enemy() 
C = Coin() 
allsprites = pygame.sprite.Group() #create groups
allsprites.add(P) 
allsprites.add(E) 
allsprites.add(C) 

INC_SPEED = pygame.USEREVENT + 1
 
while done: 
    bg_y %= 600 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=False
 
    screen.blit(bg, (0,0)) 
    pressed = pygame.key.get_pressed() 
     
    if pressed[pygame.K_RIGHT]: 
        P.update(5) 
    elif pressed[pygame.K_LEFT]: 
        P.update(-5) 
 
    if E.rect.collideobjects([P]): 
        screen.fill((255, 0, 0))
        screen.blit(game_over, (30,250))
        pygame.display.update()
        for entity in allsprites:
            entity.kill()
        time.sleep(2)
        done=False
 
    if C.rect.collideobjects([P]): 
        cnt += 1 
        if cnt>5 or cnt>10 or cnt>15:
            speed+=2
        C.newcoordinates() 
 
    screen.blit(bg, (0, -600 + bg_y)) 
    screen.blit(bg, (0, bg_y)) 
    bg_y += 5 
    screen.blit(font_small.render(f'Your coins: {cnt}', True, black), (10,10)) 
    allsprites.update() 
    allsprites.draw(screen) 
 
    pygame.display.update() 
 
    clock.tick(60) 