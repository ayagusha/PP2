import pygame
import time
import random
from os import scandir
from select import select

pygame.init()
h=400
w=400
block=20
maxlvl=2
screen=pygame.display.set_mode((w,h))
clock=pygame.time.Clock()
done=True

black=(0,0,0)
colorline=(50,50,50)
screen.fill(black)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)
cnt=0

class Point:
    def __init__(self, _x, _y):
        self.x=_x
        self.y=_y

class Wall(pygame.sprite.Sprite):
    def __init__(self,lvl):
        super().__init__()
        self.body=[]
        f=open("lvl{}.txt".format(lvl), "r")
        for y in range (0, h//block+1):
            for x in range (0, w//block+1):
                if f.read(1)=='#':
                    self.body.append(Point(x,y))
    def draw(self):
        for point in self.body:
            rect = pygame.Rect(block * point.x, block * point.y, block, block)
            pygame.draw.rect(screen, (226,135,67), rect)
            
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.body=[Point(10,11)]
        self.dx=0
        self.dy=0
        self.level=0
    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x=self.body[i-1].x
            self.body[i].y=self.body[i-1].y
        self.body[0].x+=self.dx
        self.body[0].y+=self.dy   
        
        if self.body[0].x*block>w:
            self.body[0].x=0
        if self.body[0].y*block>h:
            self.body[0].y=0
        if self.body[0].x<0:
            self.body[0].x=w/block
        if self.body[0].y<0:
            self.body[0].y=h/block
    def draw(self):
        point=self.body[0]
        s=pygame.image.load('image/head.png')
        s=pygame.transform.scale(s, (20,20))
        s_rect=s.get_rect()
        rect = pygame.Rect(block * point.x, block * point.y, block, block)
        screen.blit(s, (block*point.x,block *point.y))
        
        for point in self.body[1:]:
            rect=pygame.Rect(block*point.x, block*point.y, block, block)
            pygame.draw.rect(screen, (0, 255,0), rect)
    def check_collision(self, food):
        if self.body[0].x==food.location.x:
            if self.body[0].y==food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
             
class Food(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__() 
        self.image = pygame.Surface((50, 50))  
        self.rect = self.image.get_rect()  
        
        self.PlaceApple() 
    def PlaceApple(self): 
        x, y = random.randrange(0, 350, 50), random.randrange(0, 350, 50) 
        Point(x, y)
    def draw(self):
        point=self.location
        f=pygame.image.load('image/orange.jpg')
        f=pygame.transform.scale(f, (20,20))
        f_rect=f.get_rect()
        rect=pygame.Rect(block*point.x, block*point.y, block, block)
        screen.blit(f, (block*point.x,block *point.y))
def drawGrid():
    for x in range(0, w, block):
        for y in range(0,h,block):
            rect=pygame.Rect(x,y,block,block)
            pygame.draw.rect(screen, colorline, rect, 1)
       
snake=Snake()
food=Food()
wall=Wall(snake.level)
walls=pygame.sprite.Group()
walls.add(wall)
sprites=pygame.sprite.Group()
sprites.add(snake)
sprites.add(food)
sprites.add(wall)


while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                snake.dx=1
                snake.dy=0
            if event.key==pygame.K_LEFT:
                snake.dx=-1
                snake.dy=0
            if event.key==pygame.K_UP:
                snake.dx=0
                snake.dy=-1
            if event.key==pygame.K_DOWN:
                snake.dx=0
                snake.dy=1
            
    snake.move()
    snake.check_collision(food)
    '''
    if pygame.sprite.spritecollideany(snake, walls): 
        
        screen.fill((255, 0, 0))
        screen.blit(game_over, (30,250))
        pygame.display.update()
        
        for entity in sprites:
            entity.kill()
            
        time.sleep(2)
        done=False
        '''
    if len(snake.body)>6 and len(snake.body)%2==1:
        newLevel=(snake.level+1)%maxlvl
        snake=Snake()
        snake.level=newLevel
        wall=Wall(snake.level)
    screen.fill(black)
    snake.draw()
    food.draw()
    wall.draw()
    drawGrid()
                     
    pygame.display.update() 
    clock.tick(5)