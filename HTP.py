import pygame, random, sys, os
import MAIN
from pygame.locals import *

pygame.init()
pygame.display.set_caption('HOW2PLAY_AIMTRAINER')

def htp():
    SIZE = WIDTH, HEIGHT = (1080,1920)
    FPS = 30
    screen = pygame.display.set_mode((SIZE),pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect) 


    text = "AIMTRAINER is very easy to play. Targets will be shown randomly on the screen; try to shoot down as many as"
    text1 = "you can within the given time limit(10sec)."
    text2 = "Your score increases by 1 every time you hit a target. "
    text3 = "Your accuracy will be measured by how many shots you fire and the number of shots that hit the target."
    text4 ="Every bullet counts."

    font = pygame.font.SysFont(None, 35)
    font2 = pygame.font.SysFont(None, 75)

    while True:
        screen.fill('CYAN')
        
        draw_text('HOW TO PLAY', font2, (0,0,0), screen, 500, 100)
        draw_text(text, font, (0,0,0), screen, 10, 200)
        draw_text(text1, font, (0,0,0), screen, 10, 230)
        draw_text(text2, font, (0,0,0), screen, 10, 290)
        draw_text(text3, font, (0,0,0), screen, 10, 350)
        draw_text(text4, font, (0,0,0), screen, 10, 410)
        draw_text('Click ENTER to return to MAIN MENU', font, (255,255,255), screen, 450, 670)
        draw_text('Click ESCAPE to QUIT', font, (255,255,255), screen, 550, 700)        
    
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    MAIN.main_menu()
 
        pygame.display.update()
        
        


    
