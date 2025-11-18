import pygame
import sys
pygame.init()

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 150)
RED = (255, 0, 0)
GREEN = (0,255,0)

clock = pygame.time.Clock()
fps = 60




def draw_score(screen,playscore1,playscore2):
    font = pygame.font.Font(None,36)
    score_text = font.render(f'Player 1: {playscore1} Player 2: {playscore2}',True,BLACK)
    screen.blit(score_text, (screen_width // 2 - 100, 10 ))
    
    
    
class Player:
    def __init__(self, x, y, width, height, color): 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 3
        self.rect = pygame.Rect(x, y, width, height)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class Ball:
    def __init__(self, x, y, radius, color, speed_x,speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color 
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.yFac =-1
        self.xFac=1
        self.first =1
        self.rect = pygame.Rect(x- radius, y- radius, radius *2, radius*2)
        
        
    def update(self):
        self.x+=self.speed_x*self.xFac
        self.y+=self.speed_y*self.yFac
        
        if self.y<=0 or self.y >= screen_height:
            self.yFac*=-1
        if self.x <=0 and self.first:
            self.first=0
            return 1
        elif self.x >= screen_width and self.first:
            self.first=0
            return -1 
        else:
            return 0
        
    def reset(self):
        self.x = screen_width//2
        self.y = screen_height//2
        self.xFac*=-1
        self.first= 1
            
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
    def move(self):
        # self.x += self.speed_x
        # self.y += self.speed_y
        self.rect.y = self.y - self.radius
        self.rect.x = self.x - self.radius
        
    def check_border_collision(self,screen_width,screen_height):
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.speed_y *= -1
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.speed_x *= 1
            
player1 = Player(50, 250, 30, 100, BLACK)
player2 = Player(820, 250, 30, 100, BLUE)
listplayer= [player1,player2]
        
ball = Ball(100,100,13, RED, 3,3)
    
playscore1=0
playscore2=0


running = True
while running:  
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2.rect.y -= player2.speed
    if keys[pygame.K_DOWN]:
        player2.rect.y += player2.speed
    if keys[pygame.K_w]:
        player1.rect.y -= player1.speed
    if keys[pygame.K_s]:
        player1.rect.y += player1.speed
        
    
    point=ball.update()
    
    if point== -1:
        playscore1 += 1
    elif point == 1:
        playscore2 += 1
        
    if point:
        ball.reset()
            
    ball.draw(screen)
    ball.move()
    ball.check_border_collision(screen_width,screen_height)

    if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
        ball.speed_x *= -1
        
        ball.speed_x *=1.1
        ball.speed_y *=1.1
        
        maxspeed =10
        ball.speed_x = max(-maxspeed,min(ball.speed_x,maxspeed))
        ball.speed_y = max(-maxspeed,min(ball.speed_y,maxspeed))
        
    player1.draw(screen)
    player2.draw(screen)
    ball.draw(screen)
    draw_score(screen, playscore1, playscore2)
    
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
