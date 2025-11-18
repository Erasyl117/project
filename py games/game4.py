import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

jp_sound=pygame.mixer.Sound("jump.wav")
hit_sound=pygame.mixer.Sound("stolknovenie.wav")
looping= pygame.mixer.Sound("fon.wav")


width,height=900,450
screen=pygame.display.set_mode((width,height))

dino_img=pygame.image.load("dino1.png")
obstacle_img=pygame.image.load("Cactus.png")
ground_img=pygame.image.load("ground.png")

dino_img=pygame.transform.scale(dino_img,(60,60))
obstacle_img=pygame.transform.scale(obstacle_img,(30,60))
ground_img=pygame.transform.scale(ground_img,(width,90))

WHITE = (255,255,255)
GREEN =(0,255,0)

clock=pygame.time.Clock()
fps= 60


def draw_score(score, screen):
    font = pygame.font.Font(None,36)
    score_txt= font.render(f"score: {score}",True, (0, 0, 0))
    screen.blit(score_txt,(10,10))
    

class Dino:
    def __init__(self):
        self.image=dino_img
        self.width=40
        self.x=50
        self.y=height-self.image.get_height()-50
        self.vel_y=0
        self.grav=1
        self.jp_height=-20
        self.is_jp=False
        self.rect=pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
        
    def update(self):
        if self.is_jp:
            self.vel_y+=self.grav
            self.y+=self.vel_y
            if self.y>=height-self.image.get_height()-50:
                self.y=height-self.image.get_height()-50
                self.vel_y=0
                self.is_jp= False
        self.rect.topleft=(self.x,self.y)    
        
    def jump(self):
        if not self.is_jp:
            self.is_jp=True
            self.vel_y=self.jp_height
            jp_sound.play()
            
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))

class Obstacle:
    def __init__(self,speed):
        self.image=obstacle_img
        self.x=width
        self.y=height-self.image.get_height()-50
        self.vel=speed 
        self.rect=pygame.Rect(self.x,self.y,self.image.get_width(),self.image.get_height())
        
    def update(self):
        self.x-=self.vel
        if self.x<-self.image.get_width():
            self.x=width
        self.rect.topleft=(self.x,self.y)
        
    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))
        
    def move(self):
        self.x -= self.vel
        if self.x < -self.x:
            self.x = width
            return True
        return False
    
class Ground():
    def __init__(self,speed):
        self.image=ground_img
        self.x=0
        self.vel=speed
        self.rect=pygame.Rect(self.x,height-100,width,50)
        
    def update(self):
        self.x-=self.vel
        if self.x<=-width:
            self.x=0
        self.rect.topleft=(self.x,height-100)
        
    def draw(self,screen):
         screen.blit(self.image,(self.x,height-100))
         screen.blit(self.image,(self.x+width,height-100))
         
def show_start_menu():
    waiting = True
    while waiting:
        screen.fill((255, 255, 255))
        title_font = pygame.font.Font(None, 48)
        info_font = pygame.font.Font(None, 30)
        title_text = title_font.render("Dino Game", True, (0, 0, 0))
        info_text = info_font.render("Нажми ПРОБЕЛ, чтобы начать", True, (0, 0, 0))
        
        
        
        screen.blit(title_text, (width//2 - title_text.get_width()//2, height//2 - 60))
        screen.blit(info_text, (width//2 - info_text.get_width()//2, height//2))
        
         
        

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False 
                          
         

def main():
    clock=pygame.time.Clock()
    font=pygame.font.Font(None,20)
    looping.play(loops=-1)
   
    
    show_start_menu()
    
    game_speed=4
    
    run=True
    init_start=True
    game_active=False
    
    score=0
    record=0
    
    while run:
        clock.tick(30)
        screen.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if not game_active:
                        dino=Dino()
                        obstacle=Obstacle(game_speed)
                        ground=Ground(game_speed)
                        init_start=False
                        game_active=True
                        score=0
                    else:
                        dino.jump()
        if game_active:
            dino.update()
            obstacle.update()
            ground.update()
            
            if dino.rect.colliderect(obstacle.rect):
                game_active=False
                hit_sound.play()
                
            if obstacle.x<0:
                score += 1
                if score>record:
                    record=score
                    
                if score %1==0 and game_speed<16:
                   game_speed +=1
                    
                obstacle=Obstacle(game_speed)
                ground = Ground(game_speed)
                
                
            ground.draw(screen)
            dino.draw(screen)
            obstacle.draw(screen)
            
            score_t=font.render("score:"+str(score),True,(0,0,0))
            record_t=font.render("record:"+str(record),True,(0,0,0))
            
            screen.blit(score_t,(10,10))
            screen.blit(record_t,(width-290,10))
        else:
            if init_start:
                start_t=font.render("to start press space",True,(0,0,0))
                screen.blit(start_t,(width//2-start_t.get_width()//2,height//2-start_t.get_height()//2))
            else:
                game_o_text=font.render("wanna try again?", True,(0,0,0))
                game_o_text1=font.render("press space to start",True,(0,0,0))
                screen.blit(game_o_text,(width//2-game_o_text.get_width()//2,height//2-game_o_text.get_height() // 2))
                screen.blit(game_o_text1,(width//2-game_o_text.get_width()//2,height//1.5-game_o_text.get_height() // 1.5))
                
                
                
                
        pygame.display.update()
    pygame.quit()
if __name__ =="__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
# obstacle1= Obstacle(3)
# obstacle2= Obstacle(6)
# dino = Dino()
# score = 0
# running = True
# jpscore = 0

# while running:
#     screen.fill(WHITE)
#     screen.blit(ground_img, (0, 350))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

    # keys = pygame.key.get_pressed()
#     if not dino.is_jp:
#         if   keys[pygame.K_SPACE]:
#             dino.jump()
#             jpscore += 1
#             print("дино прыгнаул: ", jpscore)
            
#     if score >= 100:
#         screen.fill(GREEN)
#         screen.blit(ground_img, (0, 350))
            
#     dino.update()
#     dino.draw(screen)

#     if obstacle1.move():
#         score += 1
#     if obstacle2.move():
#         score += 0

#     obstacle1.update()
#     obstacle2.update()
#     obstacle1.draw(screen)
#     obstacle2.draw(screen)

#     if dino.rect.colliderect(obstacle1.rect) or dino.rect.colliderect(obstacle2.rect):
#         print("Game Over!")
#         running = False

#     draw_score(score, screen)
    
#     pygame.display.update()
#     clock.tick(fps)
# pygame.quit()