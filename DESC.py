from pygame.locals import *
def DESC():
    import pygame, random, sys, os
    import MAIN

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,30)
    pygame.init()
    pygame.display.set_caption('DESCRIPTION_AIMTRAINER')
    SIZE = WIDTH, HEIGHT = (1080,1920)
    FPS = 30
    screen = pygame.display.set_mode((SIZE),pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    text = "AIMTRAINER is a game programmed in python using pygame module that is specifically designed to improve the"
    text1 = "player’s aim in various First-Person Shooter games such as Fortnite, Counter-Strike: GO, Valorant and Call of Duty"
    text2 ="AIMTRAINER can help you improve your raw aiming ability and muscle memory, which can translate into better"
    text3 = "performance in the game."
    text4 ="It is a tool custom made to help players improve accuracy,reaction time and hand-eye coordination."

    font = pygame.font.SysFont(None, 35)
    font2 = pygame.font.SysFont(None, 75)

    while True:
        screen.fill('CYAN')
        
        draw_text('DESCRIPTION', font2, (0,0,0), screen, 500, 100)
        draw_text(text, font, (0,0,0), screen, 10, 200)
        draw_text(text1, font, (0,0,0), screen, 10, 230)
        draw_text(text2, font, (0,0,0), screen, 10, 290)
        draw_text(text3, font, (0,0,0), screen, 10, 320)
        draw_text(text4, font, (0,0,0), screen, 10, 380)
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
        
        
            
DESC()
