import pygame
import math
import sys
           
pygame.init()
borderThickness=20
width=500
height=500
playerWidth=50
playerHeight=50
move=50
posX=width/2
posY=height/2
screenSize=(width,height)
screenDisplay=pygame.display.set_mode(screenSize)
#colors
brown=pygame.Color(205,127,50,255)
black=pygame.Color(0,0,0,0)
white=pygame.Color(255,255,255,255)
blue=pygame.Color(51,180,255,0)
#blocks
#expansion is always (top->bottom and left->right)
playerOrigin=pygame.Rect(0,0,playerWidth,playerHeight)
player=playerOrigin.move(posX,posY)
leftPadding=pygame.Rect(0,0,borderThickness,height)
topPadding=pygame.Rect(0,0,width,borderThickness)
bottomPadding=pygame.Rect(0,height-borderThickness,width,borderThickness)
rightPadding=pygame.Rect(width-borderThickness,0,borderThickness,height)

def main():
    global player,posX,posY,playerOrigin,playerWidth
    while(True):
         for event in pygame.event.get():
              if event.type==pygame.QUIT:
                 pygame.quit()
                 return 0
              if event.type==pygame.KEYDOWN:
                 print(f"COORDINATE:({posX},{posY})")
                 match event.key:
                     case pygame.K_UP:
                         if posY-move>=(0+borderThickness):
                            posY-=move
                     case pygame.K_DOWN:
                         playerWidth+=2
                         playerOrigin=pygame.Rect(0,0,playerWidth,playerHeight)
                         if posY+move+playerHeight<=(height-borderThickness):
                            posY+=move
                     case pygame.K_LEFT:
                         if posX-move>=(0+borderThickness):
                            posX-=move
                     case pygame.K_RIGHT:
                        if posX+move+playerWidth<=(width-borderThickness):
                           posX+=move

         player=playerOrigin.move(posX,posY)                          
         screenDisplay.fill(black)
         screenDisplay.fill(brown,leftPadding)
         screenDisplay.fill(brown,rightPadding)
         screenDisplay.fill(brown,topPadding)
         screenDisplay.fill(brown,bottomPadding)
         screenDisplay.fill(blue,player)
         pygame.display.flip()      



sys.exit(main())