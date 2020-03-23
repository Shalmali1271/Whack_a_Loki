import pygame
import time 
import random
pygame.init()
clock = pygame.time.Clock()
white=(255,255,255)
running = True
def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def hammer():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    pygame.mouse.get_rel(550,600)
    pygame.mouse.set_cursor((8,8),(4,4),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    
    if 550 > mouse[0] > 0 and 600 > mouse[1] > 0:
        pygame.mouse.set_visible( False )
        #makes mouse invisible
        MANUAL_CURSOR = pygame.image.load('hammer.png').convert_alpha()
        screen.blit(MANUAL_CURSOR,(mouse))
    elif click[0] == 1: 
        pygame.mouse.set_visible( False )
        MANUAL_CURSOR1 = pygame.image.load('clickedhammer.png').convert_alpha()   
        screen.blit(MANUAL_CURSOR1,(mouse)) 
    else :
        pygame.mouse.set_visible(True)
    
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
    hammer()
    pygame.display.flip() 


def loki():
    global running
    global clock
    
    ran_cor=[(50,90),(200,90),(350,90),(100,265),(250,265),(50,440),(200,440),(350,440)]       
    random_num = ran_cor[random.randint(0, len(ran_cor)-1)]
    img=pygame.image.load("loki.png").convert_alpha()
    screen.blit(img,random_num)
    #im_rect = im_rect.move(im_dir)
    # detect the boundaries and change directions
    # left/right boundaries are 0 to sreen width
    # top/bottom boundaries are 0 to screen height
    # if im_rect.top < 0 or im_rect.bottom > sh:
    #     im_dir[1] = -im_dir[1]
    tesseract()
    pygame.time.delay(1000)
    #pygame.display.flip()


def thor() :
    image = pygame.image.load("thor.png").convert()  
    direction = 'left'
    screen.blit(image,(550,150))
    loki()
    
def window2() :
    global running 
    global screen
    global white
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        screen.fill(white)
        background_image2 = pygame.image.load("bg2.png").convert()   
        screen.blit(background_image2, [0,0])
        clock.tick(60)
        thor() 
        pygame.display.flip()    
       
        
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
                                   #  quit button.
                                   # if 250+100 > mouse[0] > 250 and 425+50 > mouse[1] > 425:
                                   #     pygame.draw.rect(screen, (110,0,0),(250,425,100,50))
                                   # else:
                                   #     pygame.draw.rect(screen, (190,0,0),(250,425,100,50))
                                   # text = pygame.font.SysFont("freesansbold.ttf",35,bold=False,italic=True)
                                   # Surf, Rect = text_objects("QUIT", text)
                                   # Rect.center = ( (250+(100/2)), (425+(50/2)) )
                                   # screen.blit(Surf, Rect)
        
    if click[0] ==1:
        window2()       
    else :
        pass
    clock.tick(60)
    pygame.display.flip()