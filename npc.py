import pygame
import random
import numpy as np
#import math 
pygame.init()
pygame_icon = pygame.image.load('.\\resources\\icon.png')
screen = pygame.display.set_mode((880,560))
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption("npcs are becomeing retarded")
running = True
X=400
Y=250
Xspeed=0/2
Yspeed=0/2
directo=0
def walking():
    global X
    global Y
    global Xspeed
    global Yspeed
    MAXSPEED=10
    MINSPEED=-10
    global playerX
    global playerY
    up=2
    global directo
    randomMov=random.randint(1,4)
    mov=random.randint(0,20)
    slowDown=0.02
    playerVisible=False
    #i would make a new file but its to late
    veiwBoxMinX=X-230
    veiwBoxMaxX=X+230

    if mov>6 and Xspeed<MAXSPEED and Yspeed<MAXSPEED and playerVisible==False:
        if randomMov==1:
            Xspeed+=up
        if randomMov==2:
            Xspeed-=up
        if randomMov==3:
            Yspeed+=up
        if randomMov==4:    
            Yspeed-=up
        if Yspeed>=79%MAXSPEED:
            slowDown+0.05
        if Xspeed>=79%MAXSPEED:
            slowDown+0.05
        if Xspeed<60%MAXSPEED:
            slowdown=0.02
        if Yspeed<79%MAXSPEED:
            slowDown=0.02
    elif playerVisible == False:
        if Xspeed>0:
            Xspeed-=slowDown
        if Yspeed>0:
            Yspeed-=slowDown
        if Yspeed<0:
            Yspeed+=slowDown
        if Xspeed<0:
            Xspeed+=slowDown
    X+=Xspeed
    Y+=Yspeed
    if X>700*1.2 or X<0:
        X=700*1.2/2
    if Y>500*1.2 or Y<0:
        Y=500*1.2/2
    if Xspeed>MAXSPEED or Xspeed<MINSPEED:
        Xspeed=0
    if Yspeed>MAXSPEED or Yspeed<MINSPEED:
        Yspeed=0
    if Xspeed>Yspeed:
        directo=1
    if Yspeed>Xspeed:
        directo=0
font = pygame.font.Font('.\\resources\\JetBrainsMono-Medium.ttf', 32)
printX=str(X)
printY=str(Y)
printer=printX+" "+printY
text = font.render(printer, True, (255,32,49))
logan = font.render("made by zzach, please give star",True,(255,0,0))
textRect = text.get_rect()
textRect.topleft = (0, 42)
clock = pygame.time.Clock()
#player
Playerspeed=20
playerX=30
playerY=100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type==pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX-=Playerspeed
        if event.key == pygame.K_RIGHT:
            playerX+=Playerspeed
        if event.key==pygame.K_UP:
            playerY-=Playerspeed
        if event.key==pygame.K_DOWN:
            playerY+=Playerspeed
    printX=str(X)
    printY=str(Y)
    printer=printX+" "+printY
    text = font.render(printer, True, (255,32,49), (49,0,0))
    screen.fill((255,255,255))
    #screen.blit(text, textRect)
    #screen.blit(logan)
    veiw=pygame.draw.circle(screen,(255,0,0), (X, Y), 230)
    pygame.draw.circle(screen,(0,0,200), (X+9, Y+9), 30)
    pygame.draw.circle(screen,(0,255,0), (playerX, playerY), 40)
    screen.blit(text, textRect)
    screen.blit(logan)
    walking()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
