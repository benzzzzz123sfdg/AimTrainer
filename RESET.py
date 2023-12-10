from pygame.locals import *
import pygame, sys
import MAIN
import RESETCONFIRM
def reset():
        import mysql.connector as mc
        co=mc.connect(host='localhost',user='root',passwd='123456',database='valo')
        cur=co.cursor()
        cur.execute("DROP TABLE LEADERBOARD;")
        cur.execute("CREATE TABLE LEADERBOARD (PLAYER_NAME VARCHAR(20), MODE VARCHAR(15), ACCURACY int, SCORE int)")

        def ins(lst):
                sql = ("INSERT INTO LEADERBOARD(PLAYER_NAME, MODE, ACCURACY, SCORE)"
               "VALUES (%s, %s, %s, %s)")
                try:
                    cur.execute(sql,lst)
                    co.commit()
                except:
                    co.rollback()
                
        for i in range (3):
            lst = ('BOT' , 'EASY' , 0 , 0)
            ins(lst)
        for i in range (3):
            lst = ('BOT' , 'MEDIUM' , 0 , 0)
            ins(lst)
        for i in range (3):
            lst = ('BOT' , 'DIFFICULT' , 0 , 0)
            ins(lst)
        co.close()

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


        text = "Click R to reset"
        font = pygame.font.SysFont(None, 35)
        font2 = pygame.font.SysFont(None, 40)

        while True:
                screen.fill('CYAN')
        
                draw_text('RESET', font2, (0,0,0), screen, 600, 100)
                draw_text(text, font2, (0,0,0), screen, 550, 200)
                draw_text('Click ENTER to return to MAIN MENU', font, (255,255,255), screen, 450, 670)
                draw_text('Click ESCAPE to QUIT', font, (255,255,255), screen, 550, 700)

                while True:
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
                                if event.key == K_r:
                                        RESETCONFIRM.RESET_screen()
                                    
                        pygame.display.update()
                        clock.tick(60)
       
