import pygame, sys
import webview

 
# Setup pygame/window
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('JEE MOCK TEST')
width, height = 640, 760
screen = pygame.display.set_mode((width, height),0,32)

font = pygame.font.SysFont('arialblack', 40)
font1 = pygame.font.SysFont('arialblack', 26)
font2 = pygame.font.SysFont('arialblack', 20)

#images
logo = pygame.image.load("images/logo.jpg")
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False

intro = True
def main():
    if intro == True:
            INTRO()
    while True:
        
        screen.fill(('white'))
        pygame.draw.rect(screen, 'black', (0,0,640,100))
        pygame.draw.rect(screen, 'yellow', (10,10,620,80))
        draw_text('JEE MOCK TEST', font, 'black', screen, 150, 20)
        draw_text('Choose as per your choice: ', font1, 'black', screen, 20, 200)
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(width//2-95, height//2-16, 200, 50)
        button_2 = pygame.Rect(width//2-95, height//2+84, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                MAINS()
        if button_2.collidepoint((mx, my)):
            if click:
                ADVANCE()
        pygame.draw.rect(screen, ('dark grey'), button_1)
        draw_text('MAINS', font1, 'black', screen, width//2-40, height//2-10)
        pygame.draw.rect(screen, ('dark grey'), button_2)
        draw_text('ADVANCE', font1, 'black', screen, width//2-60, height//2+90)        
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)

def INTRO():
    running = True 
    while running:
        screen.fill(('white'))
        screen.blit(logo, (220, 200))
        draw_text("Press SPACE to START", font, 'black', screen, 80, 450)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False  
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)
    
def MAINS():
    running = True 
    while running:
        screen.fill(('white'))
        pygame.draw.rect(screen, 'black', (0,0,640,100))
        pygame.draw.rect(screen, 'yellow', (10,10,620,80))
        draw_text('JEE MAINS TEST', font, 'black', screen, 130, 20)
        webview.create_window('JEE MAINS', 'https://www.selfstudys.com/mcq/jee/online/mock-test/mix-test/jee-main-test-142')
        webview.start()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False  
        pygame.display.update()
        mainClock.tick(60)
        
        
def ADVANCE():
    running = True
    while running:
        screen.fill(('white'))
        pygame.draw.rect(screen, 'black', (0,0,640,100))
        pygame.draw.rect(screen, 'yellow', (10,10,620,80))
        draw_text('JEE ADVANCE TEST', font, 'black', screen, 100, 20)
        webview.create_window('JEE ADVANCE', 'https://www.selfstudys.com/mcq/jee/online/mock-test/jee-advanced/jee-advanced-mix-test-5')
        webview.start()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)
 
main()