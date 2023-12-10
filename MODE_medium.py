import pygame, random, sys, os
import MAIN
from pygame.locals import *
import mysql.connector as mc

pygame.init()
pygame.display.set_caption('SCORE_MEDIUM_AIMTRAINER')

def DESC():
    co=mc.connect(host='localhost',user='root',passwd='123456',database='valo')
    cur=co.cursor()
    SIZE = WIDTH, HEIGHT = (1080,1920)
    FPS = 30
    screen = pygame.display.set_mode((SIZE),pygame.FULLSCREEN)
    clock = pygame.time.Clock()


    def blit_text(surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                
                if x + word_width >= max_width:
                    x = pos[0] 
                    y += word_height  
                surface.blit(word_surface, (x, y))
                x += word_width + space
                
            x = pos[0]  
            y += word_height  


    sql = "select PLAYER_NAME, ACCURACY, SCORE from leaderboard where mode='MEDIUM' order by score desc limit 1 offset 0;"
    cur.execute(sql)
    result = cur.fetchall()
    
    for i in result:
            a1=i[0]
            a2=str(i[1])
            a3=str(i[-1])

    sql = " select PLAYER_NAME, ACCURACY, SCORE from leaderboard where mode='MEDIUM' order by score desc limit 1 offset 1;"
    cur.execute(sql)
    result = cur.fetchall()
    
    for i in result:
            b1=i[0]
            b2=str(i[1])
            b3=str(i[-1])
    black=(0,0,0)
    font = pygame.font.SysFont('Arial', 30)
    font2 = pygame.font.SysFont(None, 75)
        
    sql = " select PLAYER_NAME, ACCURACY, SCORE from leaderboard where mode='MEDIUM' order by score desc limit 1 offset 2;"
    cur.execute(sql)
    result = cur.fetchall()
    
    for i in result:
            c1=i[0]
            c2=str(i[1])
            c3=str(i[-1])

    co.close()
    
    while True:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(pygame.Color('CYAN'))
        disp=font2.render("SCOREBOARD-MEDIUM",5,black)
        screen.blit(disp, (400,100))
        disp=font.render("NAME", 1, black)
        screen.blit(disp, (400,200))
        disp=font.render("ACCURACY", 1, black)
        screen.blit(disp, (600,200))
        disp=font.render("SCORE", 1, black)
        screen.blit(disp, (900,200))

        disp_a1 = font.render(a1, 1, black)
        screen.blit(disp_a1, (400,250))
        disp_a2 = font.render(a2, 1, black)
        screen.blit(disp_a2, (630,250))
        disp_a3 = font.render(a3, 1, black)
        screen.blit(disp_a3, (910,250))
        
        disp_b1 = font.render(b1, 1, black)
        screen.blit(disp_b1, (400,300))
        disp_b2 = font.render(b2, 1, black)
        screen.blit(disp_b2, (630,300))
        disp_b3 = font.render(b3, 1, black)
        screen.blit(disp_b3, (910,300))

        disp_c1 = font.render(c1, 1, black)
        screen.blit(disp_c1, (400,350))
        disp_c2 = font.render(c2, 1, black)
        screen.blit(disp_c2, (630,350))
        disp_c3 = font.render(c3, 1, black)
        screen.blit(disp_c3, (910,350))
            
        pygame.display.update()

        if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    MAIN.main_menu()
                    
        text2= "Click ENTER to return to MAINMENU"
        blit_text(screen, text2, (500, 500), font)
        text3= "Click ESCAPE to QUIT"
        blit_text(screen, text3, (575, 550), font)
        pygame.display.update()


