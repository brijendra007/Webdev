import pygame
import time
import random
pygame.init()
AppleThickness=30
display_width=800
display_height=600
block_size=20
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Slither")
icon=pygame.image.load('apple.png')
pygame.display.set_icon(icon)
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)
clock=pygame.time.Clock()
img=pygame.image.load('C:\Python27\snakehead2.png')
appleimg=pygame.image.load('apple.png')
smallfont=pygame.font.SysFont("comicsansms",25)
medfont=pygame.font.SysFont("comicsansms",50)
larfont=pygame.font.SysFont("comicsansms",80)
direction="right"
def pause():
    pause=True
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    pause=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        gamedisplay.fill(white)
        message_to_screen("Paused",black,-100,"large")
        message_to_screen("press C to continue or Q to quit:",black,30)
        pygame.display.update()
        clock.tick(5)
def scoregen(score):
    text=smallfont.render("Score:"+str(score),True,black)
    gamedisplay.blit(text,[0,0])
def randAppleGen():
    randomAppleX=round(random.randrange(0,display_width-AppleThickness)/10.0)*10.0
    randomAppleY=round(random.randrange(0,display_height-AppleThickness)/10.0)*10.0
    return randomAppleX,randomAppleY    
def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    intro=False
                if event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        gamedisplay.fill(white)
        message_to_screen("Welcome to Slither",green,-100,"large")
        message_to_screen("the objective of snake is to eat red Apples",black,-30)
        #message_to_screen("the more apples you getlonger you get",black,10)
        message_to_screen("if you run into yourself,you gonna be die!",black,50)
        message_to_screen("Press C to play or Q to quit",black,180)
        pygame.display.update()
        clock.tick(5)
def text_objects(text,color,size):
    if size=="small":
        textSurface=smallfont.render(text,True,color)
    elif size=="medium":
        textSurface=medfont.render(text,True,color)
    elif size=="large":
        textSurface=larfont.render(text,True,color)
    return textSurface,textSurface.get_rect()
def snake(block_size,snakelist):
    if direction=="right":
        head=pygame.transform.rotate(img,270)
    if direction=="left":
        head=pygame.transform.rotate(img,90)
    if direction=="up":
        head=img
    if direction=="down":
        head=pygame.transform.rotate(img,180)    
    gamedisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gamedisplay,green,[XnY[0],XnY[1],block_size,block_size])

def message_to_screen(msg,color,y_display,size="small"):
    textSurf,textRect=text_objects(msg,color,size)
    textRect.center=(display_width/2),(display_height/2)+y_display
    gamedisplay.blit(textSurf,textRect)
def gameloop():
    global direction
    direction="right"
    lead_x=display_width/2
    lead_y=display_height/2
    lead_x_change=10
    lead_y_change=0
    snakelist=[]
    snakelength=2
    randomAppleX,randomAppleY=randAppleGen()
    gameExit=False
    gameover=False
    while not gameExit:
        while gameover==True:
            gamedisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to Play or Q to Quit",black,50,size="medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True
                    gameover=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameExit=True
                        gameover=False
                    if event.key==pygame.K_c:
                        gameloop()
            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
                gameover=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction="left"
                    lead_x_change=-block_size
                    lead_y_change=0
                elif event.key==pygame.K_RIGHT:
                    direction="right"
                    lead_x_change=block_size
                    lead_y_change=0
                elif event.key==pygame.K_UP:
                    direction="up"
                    lead_y_change=-block_size
                    lead_x_change=0
                elif event.key==pygame.K_DOWN:
                    direction="down"
                    lead_y_change=block_size
                    lead_x_change=0
                elif event.key==pygame.K_p:
                    pause()
        if lead_x>=display_width or lead_x<0 or lead_y>=display_height or lead_y<0:
            gameover=True
        lead_x+=lead_x_change
        lead_y+=lead_y_change
        gamedisplay.fill(white)
        gamedisplay.blit(appleimg,(randomAppleX,randomAppleY))
        snakehead=[]
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        
        if len(snakelist)>snakelength:
            del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment==snakehead:
                gameover=True
        snake(block_size,snakelist)
        scoregen(snakelength-1)
        pygame.display.update()
        
        if lead_x>=randomAppleX and lead_x<=randomAppleX+AppleThickness or lead_x+block_size>=randomAppleX and lead_x+block_size<=randomAppleX+AppleThickness:
            if lead_y>=randomAppleY and lead_y<=randomAppleY+AppleThickness:
                randomAppleX,randomAppleY=randAppleGen()
                snakelength+=1
            elif lead_y+block_size>=randomAppleY and lead_y+block_size<=randomAppleY+AppleThickness:
                randomAppleX,randomAppleY=randAppleGen()
                snakelength+=1                
        clock.tick(15)
    pygame.quit()
    quit()
game_intro()    
gameloop()
