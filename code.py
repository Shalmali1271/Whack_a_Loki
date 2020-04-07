import pygame
import time 
from threading import *
import random
pygame.init()
clock = pygame.time.Clock()
white=(255,255,255)
running = True
bool=True
run=True



def text_objects1(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
    
def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()


def tesseract() :
        image = pygame.image.load("tes.png").convert_alpha()   
        screen.blit(image,(50,100))
        screen.blit(image,(200,100))
        screen.blit(image,(350,100))
        screen.blit(image,(100,275))
        screen.blit(image,(250,275))
        screen.blit(image,(50,450))
        screen.blit(image,(200,450))
        screen.blit(image,(350,450))
        thor()
    
    #pygame.display.flip() 

class loki(Thread):
        
    def run(self) :
#def loki():
        global running
        global clock
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
            ran_cor=[(50,90),(200,90),(350,90),(100,265),(250,265),(50,440),(200,440),(350,440)]       
            random_num = ran_cor[random.randint(0, len(ran_cor)-1)]
            y_change = 0
            img=pygame.image.load("loki.png").convert_alpha()
            x=random_num[0]
            y=random_num[1]
            y_change=random_num[1]-70  
            num1=(x,y_change)
            max_time=2
            start_time=time.time()
            while (time.time()-start_time) < max_time :
                screen.blit(img,num1)
                
                score=0
                pygame.draw.rect(screen, (255,255,255),(550,350,150,50))
                if random_num[0]+65 > mouse[0] > random_num[0] and random_num[1]+90 > mouse[1] > random_num[1]:
                    if click[0] ==1:
                        score=score+1
                            #pygame.draw.rect(screen, (255,255,255),(550,350,150,50))
                        Text = pygame.font.SysFont("freesansbold.ttf",35,bold=False,italic=True)          
                        Surf1, Rect1 = text_objects1(str(score), Text)
                        Rect1.center = ( (550+(150/2)), (350+(50/2)) )
                        screen.blit(Surf1, Rect1)

                    elif click[0] !=1 :
                        score=score
                        Text = pygame.font.SysFont("freesansbold.ttf",35,bold=False,italic=True)          
                        Surf1, Rect1 = text_objects1(str(score), Text)
                        Rect1.center = ((550+(150/2)), (350+(50/2)))
                        screen.blit(Surf1, Rect1)
                    else :
                        pass
              
        #pygame.display.flip()
    #loki()

class hammer(Thread):
    def run(self) : 
        global running 
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            pygame.mouse.set_visible( False )
            pygame.mouse.set_cursor((8,8),(4,4),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
            if click[0] == 1: 
                MANUAL_CURSOR1 = pygame.image.load('clickedhammer.png').convert_alpha()   
                screen.blit(MANUAL_CURSOR1,mouse)
            elif 550 > mouse[0] > 0 and 600 > mouse[1] > 0:
                MANUAL_CURSOR = pygame.image.load('hammer.png').convert_alpha()
                screen.blit(MANUAL_CURSOR,mouse)
            #random_num=loki.__init__(self.random_num)
            
            else :
                pass       
            #clock.tick(90)
def score():
    #score=0
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global screen
    pygame.draw.rect(screen, (255,255,255),(550,300,150,50))
    Text = pygame.font.SysFont("freesansbold.ttf",35,bold=False,italic=True)            
    Surf, Rect = text_objects1("SCORE ", Text)
    Rect.center = ( (550+(150/2)), (300+(50/2)) )
    screen.blit(Surf, Rect)
        

def thor() :
    image = pygame.image.load("thor.png").convert()  
    direction = 'left'
    screen.blit(image,(550,150))
    score()


def window2() :
    global running 
    global screen
    global white
    global bool
        
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        screen.fill(white)
        background_image2 = pygame.image.load("bg4.jpg").convert()   
        screen.blit(background_image2, [0,0])
    
        tesseract()

        while bool:
            
            t3=loki()
            t3.start()
            t5=hammer() 
            t5.start() 
            bool=False
        
        pygame.display.flip()  
#t3=loki()


(width, height) = (700, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('WHACK A LOKI')
background_colour = (255,255,255)
#def window1() :
background_image = pygame.image.load("thorandloki.png").convert()
screen.fill(background_colour)
screen.blit(background_image, [0, 0]) 
while running: 
    for event in pygame.event.get():              
        if event.type == pygame.QUIT:
            running = False
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #play Button
    if 250+100 > mouse[0] > 250 and 350+50 > mouse[1] > 350:
        pygame.draw.rect(screen, (0,45,0),(250,350,100,50))
    else:
        pygame.draw.rect(screen, (0,80,0),(250,350,100,50))
    smallText = pygame.font.SysFont("freesansbold.ttf",35,bold=False,italic=True)            
    textSurf, textRect = text_objects("PLAY!", smallText)
    textRect.center = ( (250+(100/2)), (350+(50/2)) )
    screen.blit(textSurf, textRect)
    
    
    if click[0] ==1:
        window2()       
    else :
        pass
    clock.tick(90)
    pygame.display.flip()  
