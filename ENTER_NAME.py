import pygame
import time
 
def name(): 
    pygame.init()
    screen = pygame.display.set_mode((1080,1920),pygame.FULLSCREEN)
    
    text = 'ENTER NAME AND CLICK ENTER:'
    a =''
    
    font = pygame.font.SysFont(None, 50)
    img = font.render(text, True, (255, 0, 0))
    rect = img.get_rect()
    rect.topleft = (200, 300)
    cursor = pygame.Rect(rect.topright, (3, rect.height))
    running = True
 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    return a
                    
                if event.key == pygame.K_BACKSPACE:
                    if len(a) > 0:
                        a = a[:-1]
 
                else:
                    a += event.unicode
                 
                img = font.render(a, True, (255, 255, 0))
                rect.size = img.get_size()
                cursor.topleft = rect.topright
 
        screen.fill('CYAN')
        screen.blit(img, rect)
     
        if time.time() % 1 > 0.5:
            pygame.draw.rect(screen, (255, 0, 0), cursor)
         
        pygame.display.update()
 

    return a
