import random
import pygame
from pygame import *
import time

class GameManager():
    def __init__(self):
        # Define constants
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.FPS = 60
        self.LOKI_WIDTH = 80
        self.LOKI_HEIGHT = 90
        self.FONT_SIZE = 31
        self.FONT_TOP_MARGIN = 26
        self.FONT_BOTTOM_MARGIN = 574
        self.LEVEL_SCORE_GAP = 4
        self.LEFT_MOUSE_BUTTON = 1
        self.GAME_TITLE = "Whack A Loki"
        self.cycle_time = 0
        self.clicked=False
        # Initialize player's score, number of missed hits and level
        self.score = 0
        self.missed = 0
        self.level = 1
        self.time_to_over=0
        self.time_to_over_in_seconds = 0
        # Initialize screen
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption(self.GAME_TITLE)
        self.background = pygame.image.load("bg4.jpg")
        # Font object for displaying text
        self.font_obj = pygame.font.Font('./fonts/GROBOLD.ttf', self.FONT_SIZE)
        # Initialize the loki's sprite sheet
        # 6 different states
        sprite_sheet = pygame.image.load("loki_sprites.png")
        self.loki = []
        self.loki.append(sprite_sheet.subsurface(13, 0, 60, 102))
        self.loki.append(sprite_sheet.subsurface(68, 0, 60, 102))
        self.loki.append(sprite_sheet.subsurface(135, 0, 60, 102))
        self.loki.append(sprite_sheet.subsurface(195, 0, 60, 102))
        self.loki.append(sprite_sheet.subsurface(262, 0, 60, 102))
        #self.loki.append(sprite_sheet.subsurface(853, 0, 116, 81))
        # Positions of the tesseract in background
        self.tes_positions = []
        self.tes_positions.append((70, 57))
        self.tes_positions.append((370, 57))
        self.tes_positions.append((670, 57))
        self.tes_positions.append((220, 207))
        self.tes_positions.append((520, 207))
        self.tes_positions.append((70, 382))
        self.tes_positions.append((370, 382))
        self.tes_positions.append((670, 382))
        #self.tes_positions.append((603, 11))
        #self.tes_positions.append((603, 11))
        # Init debugger
        self.debugger = Debugger("debug")
        # Sound effects
        self.soundEffect = SoundEffect()
    # Calculate the player level according to his current score & the LEVEL_SCORE_GAP constant
    def get_player_level(self):
        newLevel = 1 + int(self.score / self.LEVEL_SCORE_GAP)
        if newLevel != self.level:
            # if player get a new level play this sound
            self.soundEffect.playLevelUp()
        return 1 + int(self.score / self.LEVEL_SCORE_GAP)

    # Get the new duration between the time the loki pop up and down the tesseract
    # It's in inverse ratio to the player's current level
    def get_interval_by_level(self, initial_interval):
        new_interval = initial_interval - self.level * 0.15
        if new_interval > 0:
            return new_interval
        else:
            return 0.05

    # Check whether the mouse click hit the loki or not
    def is_loki_hit(self, mouse_position, current_tes_position):
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]
        current_tes_x = current_tes_position[0]
        current_tes_y = current_tes_position[1]
        if (mouse_x > current_tes_x) and (mouse_x < current_tes_x + self.LOKI_WIDTH) and (mouse_y > current_tes_y) and (mouse_y < current_tes_y + self.LOKI_HEIGHT):
            return True
        else:
            return False

    # Update the game states, re-calculate the player's score, missed, level
    def update(self):
        # Update the player's score
        current_score_string = "SCORE: " + str(self.score)
        score_text = self.font_obj.render(current_score_string, True, (255, 255, 255))
        score_text_pos = score_text.get_rect()
        score_text_pos.centerx = self.background.get_rect().centerx
        score_text_pos.centery = self.FONT_TOP_MARGIN
        screen.blit(score_text, score_text_pos)
        # Update the player's missed
        current_missed_string = "MISSED: " + str(self.missed)
        missed_text = self.font_obj.render(current_missed_string, True, (255, 255, 255))
        missed_text_pos = missed_text.get_rect()
        missed_text_pos.centerx = self.SCREEN_WIDTH / 5 * 4
        missed_text_pos.centery = self.FONT_TOP_MARGIN
        screen.blit(missed_text, missed_text_pos)
        # Update the player's level
        current_level_string = "LEVEL: " + str(self.level)
        level_text = self.font_obj.render(current_level_string, True, (255, 255, 255))
        level_text_pos = level_text.get_rect()
        level_text_pos.centerx = self.SCREEN_WIDTH / 5 * 1
        level_text_pos.centery = self.FONT_TOP_MARGIN
        screen.blit(level_text, level_text_pos)
        #Update time remaining to gameover.
        current_time="Time: "+str(self.time_to_over_in_seconds)
        time_text = self.font_obj.render(current_time, True, (255, 255, 255))
        time_text_pos = time_text.get_rect()
        time_text_pos.centerx = self.SCREEN_WIDTH / 5 * 4
        time_text_pos.centery = self.FONT_BOTTOM_MARGIN
        screen.blit(time_text, time_text_pos)

    def gameover_screen(self) :
        scale = 0
        s = self.screen    # the size of your rect
        s.set_alpha(300)                # alpha level
        s.fill((50,50,50))           # this fills the entire surface
        #display the score in last window 
        current_score_string = "LOKI GOT HIT " + str(self.score) + " TIMES"
        score_text = self.font_obj.render(current_score_string, True, (255, 255, 255))
        score_text_pos = score_text.get_rect()
        score_text_pos.centerx = self.background.get_rect().centerx
        score_text_pos.centery = 100
        screen.blit(score_text, score_text_pos)
        # Update the player's missed
        current_missed_string = "LOKI ESCAPED " + str(self.missed) + " TIMES"
        missed_text = self.font_obj.render(current_missed_string, True, (255, 255, 255))
        missed_text_pos = missed_text.get_rect()
        missed_text_pos.centerx = self.background.get_rect().centerx
        missed_text_pos.centery = 200
        screen.blit(missed_text, missed_text_pos)

        # if player wants to play again
        string4 = "TO PLAY AGAIN CLICK PLAY!"
        text4 = self.font_obj.render(string4, True, (255, 255, 255))
        text_pos4 = text4.get_rect()
        text_pos4.centerx = self.background.get_rect().centerx
        text_pos4.centery = 400
        screen.blit(text4, text_pos4)

        if self.missed > self.score:
            scale = 1
        elif self.missed < self.score:
            scale = 2
        elif self.missed == self.score:
            scale = 3

        if scale == 1:
            string1 = "LOKI WINS"
            text1 = self.font_obj.render(string1, True, (255, 255, 255))
            text_pos1 = text1.get_rect()
            text_pos1.centerx = self.background.get_rect().centerx
            text_pos1.centery = 300
            screen.blit(text1, text_pos1)
        elif scale == 2:
            string2 = "THOR WINS"
            text2 = self.font_obj.render(string2, True, (255, 255, 255))
            text_pos2 = text2.get_rect()
            text_pos2.centerx = self.background.get_rect().centerx
            text_pos2.centery = 300
            screen.blit(text2, text_pos2)
        elif scale == 3:
            string3 = "DRAW"
            text3 = self.font_obj.render(string3, True, (255, 255, 255))
            text_pos3 = text3.get_rect()
            text_pos3.centerx = self.background.get_rect().centerx
            text_pos3.centery = 300
            screen.blit(text3, text_pos3)

        self.screen.blit(s, (0,0))    # (0,0) are the top-left coordinates 
        pygame.display.update()

    # Start the game's main loop
    # Contains some logic for handling animations, loki hit events, etc..

    def start(self):
        num = -1
        loop = True
        is_down = False
        interval = 0.1
        initial_interval = 1
        frame_num = 0
        left = 0
        # Time control variables
        clock = pygame.time.Clock()
        start_ticks=pygame.time.get_ticks() 
        for i in range(len(self.loki)):
            self.loki[i].set_colorkey((0, 0, 0))
            self.loki[i] = self.loki[i].convert_alpha()
        while loop:
            self.time_to_over=(pygame.time.get_ticks()-start_ticks)/1000   #calculate how many seconds
            self.time_to_over_in_seconds= int(self.time_to_over)
            self.update()
            if self.time_to_over > 30: # if more than 30 seconds close the game
                loop=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN and event.button == self.LEFT_MOUSE_BUTTON:
                    self.soundEffect.playFire()
                    if self.is_loki_hit(mouse.get_pos(), self.tes_positions[frame_num]) and num > 0 and left == 0:
                        num = 4
                        left = 20
                        is_down = False
                        interval = 0
                        self.score += 1  # Increase player's score
                        self.level = self.get_player_level()  # Calculate player's level
                        # Stop popping sound effect
                        self.soundEffect.stopPop()
                        # Play hurt sound
                        self.soundEffect.playHurt()
                        self.update()
                    else:
                        self.missed += 1
                        self.update()
            if num > 4:
                screen.blit(self.background, (0, 0))
                self.update()                    
                num = -1
                left = 0
            if num == -1:
                screen.blit(self.background, (0, 0))
                self.update()
                num = 0
                is_down = False
                interval = 0.5
                frame_num = random.randint(0, 6)
            mil = clock.tick(self.FPS)
            sec = mil / 1000.0
            self.cycle_time += sec
            if self.cycle_time > interval:
                pic = self.loki[num]
                screen.blit(self.background, (0, 0))
                screen.blit(pic, (self.tes_positions[frame_num][0] - left, self.tes_positions[frame_num][1]))
                self.update()
                if is_down is False:
                    num += 1
                else:
                    num -= 1
                if num == 5:
                    interval = 0.3
                elif num == 4:
                    num -= 1
                    is_down = True
                    self.soundEffect.playPop()
                    interval = self.get_interval_by_level(initial_interval) 
                    # get the newly decreased interval value
                else:
                    interval = 0.1
                self.cycle_time = 0
            # Update the display
            pygame.display.flip()
        self.gameover_screen()


# The Debugger class - use this class for printing out debugging information
class Debugger:
    def __init__(self, mode):
        self.mode = mode

    def log(self, message):
        if self.mode is "debug":
            print("> DEBUG: " + str(message))



class SoundEffect:
    def __init__(self):
        self.mainTrack = pygame.mixer.music.load("sounds/themesong.wav")
        self.fireSound = pygame.mixer.Sound("sounds/fire.wav")
        self.fireSound.set_volume(1.0)
        self.popSound = pygame.mixer.Sound("sounds/pop.wav")
        self.hurtSound = pygame.mixer.Sound("sounds/hurt.wav")
        self.levelSound = pygame.mixer.Sound("sounds/point.wav")
        pygame.mixer.music.play(-1)

    def playFire(self):
        self.fireSound.play()

    def stopFire(self):
        self.fireSound.sop()

    def playPop(self):
        self.popSound.play()

    def stopPop(self):
        self.popSound.stop()

    def playHurt(self):
        self.hurtSound.play()

    def stopHurt(self):
        self.hurtSound.stop()

    def playLevelUp(self):
        self.levelSound.play()

    def stopLevelUp(self):
        self.levelSound.stop()

# Initialize the game
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()
def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('WHACK A LOKI')
background_colour = (255,255,255)
#def window1() :
background_image = pygame.image.load("thorandloki.jpg").convert()
screen.fill(background_colour)
screen.blit(background_image, [0, 0]) 
running=True
while running: 
    for event in pygame.event.get():              
        if event.type == pygame.QUIT:
            running = False
    mouse1 = pygame.mouse.get_pos()
    click1 = pygame.mouse.get_pressed()
    #play Button
    if 350+100 > mouse1[0] > 350 and 450+50 > mouse1[1] > 450:
        pygame.draw.rect(screen, (0,45,0),(350,450,100,50))
    else:
        pygame.draw.rect(screen, (0,80,0),(350,450,100,50))
    smallText = pygame.font.SysFont("freesansbold.ttf",35,bold=False,italic=True)            
    textSurf, textRect = text_objects("PLAY!", smallText)
    textRect.center = ( (350+(100/2)), (450+(50/2)) )
    screen.blit(textSurf, textRect)
    if click1[0] ==1 and (350+100 > mouse1[0] > 350 and 450+50 > mouse1[1] > 450):
        # Run the main loop
        t1 = GameManager()
        t1.start()
    pygame.display.flip()
# Exit the game if the main loop ends
pygame.quit()
