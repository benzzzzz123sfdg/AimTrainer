import pygame, sys
import GAME
mainClock = pygame.time.Clock()
from pygame.locals import *
import os

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
def main_menu():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,40)
    pygame.init()
    SIZE = WIDTH, HEIGHT = (1080,1920)
    pygame.display.set_caption('HOME_AIMTRAINER')
    screen = pygame.display.set_mode((SIZE),pygame.FULLSCREEN)
    font = pygame.font.SysFont(None, 50)
    font2 = pygame.font.SysFont(None, 150)
    font3 = pygame.font.SysFont(None, 75)
    click = False

    while True:
        screen.fill('CYAN')
        draw_text('AIMTRAINER', font2, (0,0,0), screen, 350, 0) 
        draw_text('MAIN MENU', font3, (0,0,0), screen, 540, 140)
        draw_text('Please press corresponding number', font, (0,0,0), screen, 400, 200)        

        button_1 = pygame.Rect(270, 300, 350, 75)
        button_2 = pygame.Rect(270, 480, 350, 75)
        button_3 = pygame.Rect(790, 300, 350, 75)
        button_4 = pygame.Rect(790, 480, 350, 75)
        button_5 = pygame.Rect(270, 640, 350, 75)
        button_6 = pygame.Rect(790, 640, 350, 75)

        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        pygame.draw.rect(screen, (255, 0, 0), button_4)
        pygame.draw.rect(screen, (255, 0, 0), button_5)
        pygame.draw.rect(screen, (255, 0, 0), button_6)
 
        draw_text('1.PLAY', font, (255,255,255), screen, 370, 320)
        draw_text('2.DESCRIPTION', font, (255,255,255), screen, 300, 500)
        draw_text('3.HOW TO PLAY', font, (255,255,255), screen, 830, 320)
        draw_text('4.SCORES', font, (255,255,255), screen, 880, 500)
        draw_text('5.RESET ', font, (255,255,255), screen, 370, 660)
        draw_text('6.QUIT', font, (255,255,255), screen, 900, 660)
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()                        
                    elif event.key == K_KP1 or event.key == K_1:
                        game()
                    elif event.key == K_KP2 or event.key == K_2:
                        desc()
                    elif event.key == K_KP3 or event.key == K_3:
                        HTP()
                    elif event.key == K_KP4 or event.key == K_4:
                        score()
                    elif event.key == K_KP5 or event.key == K_5:
                        reset()
                    elif event.key == K_KP6 or event.key == K_6:
                        pygame.quit()
                        sys.exit()
                    else:
                        pass
 
            pygame.display.update()
            mainClock.tick(60)
 

def game():
    a=GAME.GAME()
    
def desc():
    import DESC
    DESC.DESC()
    
def HTP():
    import HTP
    HTP.htp()

def score():
    import SCORE
    SCORE.scores()
    
def reset():
    import RESET
    RESET.reset()
    
    

