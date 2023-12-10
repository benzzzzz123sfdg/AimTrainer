import pygame, sys, MAIN
from pygame.locals import *

def scores():
    pygame.init()
    SIZE = WIDTH, HEIGHT = (1080,1920)
    pygame.display.set_caption('SCORES_AIMTRAINER')
    screen = pygame.display.set_mode((SIZE),pygame.FULLSCREEN)
    font = pygame.font.SysFont(None, 50)
    
    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
        
    def easy():
        import MODE_easy
        MODE_easy.DESC()

    def medium():
        import MODE_medium
        MODE_medium.DESC()

    def diff():
        import MODE_difficult
        MODE_difficult.DESC()
        
    font2 = pygame.font.SysFont(None, 75)
    click = False

    while True:
        screen.fill('CYAN')
        
        draw_text('SCOREBOARD', font2, (0,0,0), screen, 500, 100)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(570, 200, 200, 70)
        button_2 = pygame.Rect(570, 350, 200, 70)
        button_3 = pygame.Rect(570, 500, 200, 70)
                
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        
        draw_text('1.EASY', font, (255,255,255), screen, 610, 220)
        draw_text('2.MEDIUM', font, (255,255,255), screen, 590, 370)
        draw_text('3.HARD', font, (255,255,255), screen, 610, 520)
        draw_text('Click ENTER to return to MAIN MENU', font, (255,255,255), screen, 400, 650)
        draw_text('Click ESCAPE to QUIT', font, (255,255,255), screen, 500, 700)
             
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

                elif event.key == K_KP1 or event.key == K_1:
                        easy()
                elif event.key == K_KP2 or event.key == K_2:
                        medium()
                elif event.key == K_KP3 or event.key == K_3:
                        diff()
                else:
                        pass
 
        pygame.display.update()
        


