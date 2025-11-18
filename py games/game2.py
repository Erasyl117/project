import pygame
pygame.init()
pygame.font.init()

sc_width= 800
sc_height = 400
sc = pygame.display.set_mode((sc_width,sc_height))

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN =(0,255,0)

clock=pygame.time.Clock()
fps= 60

def draw_score(score,sc):
        font = pygame.font.Font(None,36)
        score_text=font.render(f'score: {score}', True, BLACK)
        sc.blit(score_text,(10,10))

    
class Dino:
    def __init__(self):
        self.x =60
        self.y=300
        self.width=40
        self.height=60
        self.is_jp =False
        self.jp_count= 10
        self.gravity = 1
        
    def draw(self,sc):
        pygame.draw.rect(sc,BLACK, (self.x,self.y,self.width,self.height))
        
    def jump(self):
        if self.is_jp:
            if self.jp_count>= -10:
                neg=1
                if self.jp_count <0:
                    neg =-1 
                self.y -=(self.jp_count **2)*0.5*neg
                self.jp_count-= 1
            else:
                self.is_jp= False
                self.jp_count=10
                
class Obstacle():
    def __init__(self,x,y,speed,width,height):
        self.x= x
        self.y= y
        self.speed= speed
        self.width= width
        self.height=height
        
    def draw(self,sc):
        pygame.draw.rect(sc,BLACK, (self.x,self.y,self.width,self.height))
        
    def move(self):
        self.x -= self.speed
        if self.x < -self.width:
            self.x = sc_width
            return True
        return False

    def reset(self,):
        self.x=self.init_x
        
def reset_game():
    return Dino(),Obstacle(800,300,4,20,50,),Obstacle(900,300,7,25,70),0
    
obstacle2= Obstacle(800,300,4,20,50)
obstacle1= Obstacle(900,300,7,25,70)
dino= Dino()
score = 0
running = True    
    
while running:
    
    sc.fill(WHITE)
    dino.draw(sc)
    obstacle1.draw(sc)
    obstacle1.move()
    obstacle2.draw(sc)
    obstacle2.move()
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
            
    keys= pygame.key.get_pressed()
    if not dino.is_jp:
        if keys[pygame.K_SPACE]:
            dino.is_jp = True
            
    dino.jump()
    dino.draw(sc)
    
    if (obstacle1.x < dino.x + dino.width and obstacle1.x + obstacle1.width > dino.x and obstacle1.y < dino.y + dino.height and obstacle1.y + obstacle1.height > dino.y) or \
        (obstacle2.x < dino.x + dino.width and obstacle2.x + obstacle2.width > dino.x and obstacle2.y < dino.y + dino.height and obstacle2.y + obstacle2.height > dino.y):
        pygame.display.update()
        pygame.time.delay(2000)
        dino,obstacle2,obstacle1,score = reset_game()
        continue
    
    if obstacle1.x + obstacle1.width < dino.x:
        score +=1
    if obstacle2.x + obstacle2.width < dino.x:
        score +=1
     
        
        if score %25 == 0 and obstacle1.speed <15:
            obstacle1.speed +=1   
    
    draw_score(score,sc)
    pygame.display.update()
    clock.tick(fps)
pygame.quit()
   
            
        
        
    
    