from pygame.locals import *
import pygame, sys
import MAIN
def RESET_screen():
    pygame.init()
    SIZE = WIDTH, HEIGHT = (1080,1920)
    FPS = 30
    screen = pygame.display.set_mode((SIZE),pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    def draw_text(text, font, color, surface, x, y):
            textobj = font.render(text, 1, color)
            textrect = textobj.get_rect()
            textrect.topleft = (x, y)
            surface.blit(textobj, textrect) 


    text = "SCORES HAVE BEEN RESET TO DEFAULT"
    font = pygame.font.SysFont(None, 35)
    font2 = pygame.font.SysFont(None, 40)
    while True:
            screen.fill('CYAN')        
            draw_text('RESET', font2, (0,0,0), screen, 600, 100)
            draw_text(text, font2, (0,0,0), screen, 400, 200)
            draw_text('Click ENTER to return to MAIN MENU', font, (255,255,255), screen, 450, 670)
            draw_text('Click ESCAPE to QUIT', font, (255,255,255), screen, 550, 700)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_RETURN or event.key == K_KP_ENTER:
                        MAIN.main_menu()
            pygame.display.update()
            clock.tick(60)
    
