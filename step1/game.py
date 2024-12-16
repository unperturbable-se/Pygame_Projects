import pygame
import math
import sys

pygame.init()
width=700
height=700
screenSize=(width,height)
gameScreen=pygame.display.set_mode(screenSize)
posX=width/2
posY=height/2
jump_range=20
#block
origin=pygame.Rect(20,20,width/10,height/10)
block=pygame.Rect(posX,posY,width/10,height/10)
#borders
left_border=pygame.Rect(0,0,20,height)
right_border=pygame.Rect(width-20,0,20,height)
up_border=pygame.Rect(0,0,width,20)
down_border=pygame.Rect(0,height-20,width,20)
#colours
PINK=pygame.Color(255,0,255,255)
WHITE=pygame.Color(255,255,255,255)
GREY=pygame.Color(132,136,132,255)

def display():
    gameScreen.fill(WHITE)        
    gameScreen.fill(PINK,block)
    gameScreen.fill(GREY,left_border)
    gameScreen.fill(GREY,right_border)
    gameScreen.fill(GREY,up_border)
    gameScreen.fill(GREY,down_border)


def main():
    global posX,posY,block
    while True:    
          for event in pygame.event.get():
              if event.type==pygame.QUIT:
                 pygame.quit()
                 return 0
              if event.type==pygame.KEYDOWN:
                  key=event.key
                  if key==pygame.K_UP and posY>=20:
                     posY-=jump_range
                  if key==pygame.K_DOWN and posY<=height-100:
                     posY+=jump_range
                  if key==pygame.K_LEFT and posX>=20:
                     posX-=jump_range
                  if key==pygame.K_RIGHT and posX<=width-100:
                     posX+=jump_range

                  print(f"\n({posX},{posY})")
                  block=origin.move(posX,posY)  
          display()
          pygame.display.flip()   
       

           
          
sys.exit(main())       