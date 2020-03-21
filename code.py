import pygame
import time 
import random
pygame.init()
clock = pygame.time.Clock()
def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

(width, height) = (700, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('WHACK A LOKI')
background_colour = (255,255,255)
running = True
def window2() : 
    while running:
        for event in pygame.event.get():
            screen.fill(63,65,135)
            background_image2 = pygame.image.load("bg2.png").convert()   
            pygame.display.update()
            
            pygame.display.flip()
            if event.type == pygame.QUIT:
                running = False 
        screen.blit(pygame.transform.scale(background_image2, (600, 500)), [0, 0])           
        pygame.display.update()
    
#def window1() :
background_image = pygame.image.load("thorandloki.png").convert()
screen.fill(background_colour)

pygame.display.flip()

while running: 
    for event in pygame.event.get():
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
        if click[0] ==1: #and action!= None:
            window2()       
        else :
            pass
            #Closing the window and updating the display.
                   
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_image, [0, 0])            
    pygame.display.update()
                #print (click)
        
#window1()