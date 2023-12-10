import pygame, random, sys, os
import MAIN
from pygame.locals import *
import mysql.connector as mc

def GAME():
    co=mc.connect(host='localhost',user='root',passwd='123456',database='valo')
    cur=co.cursor()
    #when running first time
    #cur.execute("CREATE TABLE LEADERBOARD (PLAYER_NAME VARCHAR(20), MODE VARCHAR(15), ACCURACY int, SCORE int)")
    #def ins(lst):
        #sql = ("INSERT INTO LEADERBOARD(PLAYER_NAME, MODE, ACCURACY, SCORE)"
        #"VALUES (%s, %s, %s, %s)")
        #try:
         #   cur.execute(sql,lst)
          #  co.commit()
        #except:
         #   co.rollback()
            
    #for i in range (3):
        #lst = ('BOT' , 'EASY' , 0 , 0)
        #ins(lst)
    #for i in range (3):
        #lst = ('BOT' , 'MEDIUM' , 0 , 0)
        #ins(lst)
    #for i in range (3):
        #lst = ('BOT' , 'DIFFICULT' , 0 , 0)
        #ins(lst)

    global rec
    rec=[]

    import ENTER_NAME
    a = ENTER_NAME.name()
    rec.append(a.upper())
    
    def terminate():
        pygame.quit()
        sys.exit()

    def ins(rec):       
        sql = ("INSERT INTO LEADERBOARD(PLAYER_NAME, MODE, ACCURACY, SCORE)"
       "VALUES (%s, %s, %s, %s)")
        try:
            cur.execute(sql,rec)
            co.commit()
        except:
            co.rollback()
        co.close()

    def populateConfig(difficulty):
            global targetImage
            targetImage = pygame.image.load(r"..\images\target.png")
            config = {}
            
            if(difficulty == "easy"):
                difficultyFile = open(r"..\modes\easy.txt", "r")
                rec.append("EASY")
            
            if(difficulty == "medium"):
                difficultyFile = open(r"..\modes\medium.txt", "r")
                rec.append("MEDIUM")
            
            if(difficulty == "hard"):
                difficultyFile = open(r"..\modes\hard.txt", "r")
                rec.append("DIFFICULT")
            
            for line in difficultyFile:
                splitLine = line.split(":")
                splitLine[1] = splitLine[1].strip("\n")
                config[splitLine[0]] = int(splitLine[1])
            
            targetImage = pygame.transform.scale(targetImage, (config["enemySize"],config["enemySize"]))
            difficultyFile.close()
            return config

    def gameOver(totalShots, hitShots, difficulty, score):
        pygame.mouse.set_visible(True)
        
        if totalShots != 0 and hitShots != 0:
            accuracy = round(hitShots/totalShots * 100)
            
        else:
            accuracy = 0
  
        windowSurface.fill('CYAN')
        drawText("GAME OVER", windowSurface, 520, 225, pygame.font.SysFont(None, 72, True))
        drawText("Accuracy: " + str(accuracy) + "%", windowSurface, 550, 314)
        drawText("Score: " + str(score), windowSurface, 590, 350)
        drawText('Click ENTER to return to MAIN MENU',windowSurface, 400,600, FONT, (255,255,255))
        drawText('Click ESCAPE to QUIT', windowSurface, 510,650, FONT, (255,255,255))
        
        pygame.display.update()
        rec.append(accuracy)
        rec.append(score)
        
        while True:
            for event in pygame.event.get():                   
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        ins(rec)
                        terminate()
                    elif event.key == K_RETURN or event.key == K_KP_ENTER:
                        ins(rec)
                        MAIN.main_menu()
    
    def game(difficulty):
        config = populateConfig(difficulty)
        pygame.mouse.set_visible(False)
        mouseY = (round(WINDOWHEIGHT / 2))
        mouseX = (round(WINDOWWIDTH / 2))
        tickCounter = 0
        enemies = []
        amountOfEnemies = 0
        score = 0
        FPS = 75
        hitShots = 0
        totalShots = 0
        STARTINGTIME = config.get("time")
        CIRCLERADIUS = 20

        while True:
            if(config.get("time") <= 0):
                gameOver(totalShots, hitShots, difficulty, score)
            tickCounter += 1
            
            if(tickCounter % FPS == 0):
                config["time"] -= 1
            windowSurface.fill(WHITE)

            if (amountOfEnemies == 0):
                while(amountOfEnemies != config.get("maxAmountOfEnemies")):
                    enemies.append(pygame.Rect((random.randint(0,WINDOWWIDTH - config.get("enemySize"))),
                                               (random.randint(0,WINDOWHEIGHT - config.get("enemySize"))),
                                               config.get("enemySize"), config.get("enemySize")))
                    
                    if enemies[amountOfEnemies].topleft[0] < 135 and enemies[amountOfEnemies].topleft[1] < 65:
                        enemies.pop(amountOfEnemies)
                        
                    else:
                        amountOfEnemies += 1
                        
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                    
                if event.type == KEYDOWN:
                    pass
                
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        terminate()
                        
                if event.type == MOUSEMOTION:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    
                if event.type == MOUSEBUTTONDOWN:
                    totalShots += 1
                    for enemy in enemies[:]:
                        if mouseX > enemy.topleft[0] and mouseX < enemy.bottomright[0]\
                           and mouseY > enemy.topleft[1] and mouseY < enemy.bottomright[1]:
                            enemies.remove(enemy)
                            amountOfEnemies -= 1
                            score += 1
                            hitShots += 1
                            
            pygame.draw.circle(windowSurface, WHITE, (mouseX,mouseY),CIRCLERADIUS,0)
            
            for enemy in enemies:
                windowSurface.blit(targetImage, enemy)
                
            font = pygame.font.SysFont(None, 200)
            text_surf = font.render(str(config.get("time")), True, (255, 0, 0))
            text_surf.set_alpha(127)
            windowSurface.blit(text_surf, (630,300))
            pygame.draw.circle(windowSurface, BLACK, (mouseX,mouseY),CIRCLERADIUS + 1, 3)
            pygame.draw.line(windowSurface, BLACK, (mouseX, mouseY + 20),(mouseX, mouseY - 20), 2)
            pygame.draw.line(windowSurface, BLACK, (mouseX + 20, mouseY),(mouseX - 20, mouseY), 2)
            drawText("SCORE: " + str(score), windowSurface, 100,50)
            pygame.display.update()
            mainClock.tick(FPS)

    pygame.init()
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)
    BLUE = (0,0,255)
    FONT = pygame.font.SysFont(None, 48)
    WINDOWWIDTH, WINDOWHEIGHT = 800,750
    
    def drawText(text, surface, x, y, font = FONT, color = RED):
        textObject = font.render(text, 1, color)
        textRect = textObject.get_rect()
        textRect.topleft = (x,y)
        surface.blit(textObject, textRect)
        
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),pygame.FULLSCREEN)
    pygame.display.set_caption("AIMTRAINER")
    enemies = []

    timer = 0
    color = 'CYAN'
    switch = False
    
    while True:
        difficultyRects = []
        difficultyRects.append(pygame.Rect(335, 450, 240, 100))
        difficultyRects.append(pygame.Rect(570, 450, 240, 100))
        difficultyRects.append(pygame.Rect(810, 450, 240, 100))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_KP1 or event.key == K_1:
                        game("easy")
                elif event.key == K_KP2 or event.key == K_2:
                        game("medium")
                elif event.key == K_KP3 or event.key == K_3:
                        game("hard")
                
        for rect in difficultyRects:
            pygame.draw.rect(windowSurface, WHITE, rect)

        windowSurface.fill(('CYAN'))
        drawText("AIMTRAINER", windowSurface, 450, 150, pygame.font.SysFont(None, 100), BLACK)
        
        button_1 = pygame.Rect(335, 475, 200, 50)
        button_2 = pygame.Rect(570, 475, 200, 50)
        button_3 = pygame.Rect(810, 475, 200, 50)

        pygame.draw.rect(windowSurface, RED, button_1)
        pygame.draw.rect(windowSurface, RED, button_2)
        pygame.draw.rect(windowSurface, RED, button_3)

        drawText("1.Easy", windowSurface, 390, 484, FONT , WHITE)
        drawText("2.Medium", windowSurface, 602, 484, FONT , WHITE)
        drawText("3.Hard", windowSurface, 860, 484, FONT , WHITE)
        
        mainClock.tick(50)
            
        if timer % 100 == 0:
            color = BLUE
        
        elif timer % 50 == 0:
            color = RED
        
        pygame.display.update()
        


